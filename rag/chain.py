"""
Production RAG Chain using LCEL.

Responsibilities:
- Build context
- Compress context
- Rerank documents
- Invoke GPT model
- Maintain conversation memory
- Return answer and sources
"""

from __future__ import annotations

from operator import itemgetter

from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_openai import ChatOpenAI

from rag.config import Config
from rag.context_compressor import ContextCompressor
from rag.logger import get_logger
from rag.memory import ConversationMemory
from rag.prompt import PromptFactory
from rag.utils import format_documents

logger = get_logger(__name__)


class RAGChain:
    """
    Production Retrieval-Augmented Generation chain.
    """

    def __init__(
        self,
        retriever,
        reranker,
        memory: ConversationMemory,
    ):

        self.retriever = retriever
        self.reranker = reranker
        self.memory = memory
        self.compressor = ContextCompressor()

        self.llm = ChatOpenAI(
            model=Config.CHAT_MODEL,
            temperature=Config.TEMPERATURE,
        )

        self.prompt = PromptFactory.create()

        self.chain = self._build_chain()

    # ---------------------------------------------------------
    # Document Preparation
    # ---------------------------------------------------------

    def _prepare_documents(
        self,
        question: str,
        documents: list[Document],
    ) -> list[Document]:
        """
        Compress and rerank retrieved documents.
        """

        documents = self.compressor.compress(
            question=question,
            documents=documents,
        )

        documents = self.reranker.rerank(
            question=question,
            documents=documents,
        )

        return documents

    # ---------------------------------------------------------
    # Context Formatting
    # ---------------------------------------------------------

    def _prepare_context(
        self,
        inputs: dict,
    ) -> str:
        """
        Convert reranked documents into prompt context.
        """

        return format_documents(
            inputs["documents"]
        )

    # ---------------------------------------------------------
    # Conversation History
    # ---------------------------------------------------------

    def _history(
        self,
        _: dict,
    ) -> str:
        """
        Return formatted conversation history.
        """

        return self.memory.formatted_history()

    # ---------------------------------------------------------
    # Build LCEL Chain
    # ---------------------------------------------------------

    def _build_chain(self):

        context_chain = (
            RunnableParallel(
                documents=itemgetter("documents"),
            )
            | RunnableLambda(self._prepare_context)
        )

        history_chain = RunnableLambda(self._history)

        return (
            {
                "history": history_chain,
                "context": context_chain,
                "question": itemgetter("question"),
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    # ---------------------------------------------------------
    # Core Generation
    # ---------------------------------------------------------

    def _generate(
        self,
        question: str,
        documents: list[Document],
    ) -> tuple[str, list[Document]]:
        """
        Shared generation logic.
        """

        logger.info(
            "Question: %s",
            question,
        )

        documents = self._prepare_documents(
            question,
            documents,
        )

        if not documents:

            logger.warning(
                "No document passed reranker threshold."
            )

            answer = (
                "I couldn't find any relevant information "
                "in the knowledge base to answer your question."
            )

            self.memory.add_user_message(question)
            self.memory.add_ai_message(answer)

            return answer, []

        answer = self.chain.invoke(
            {
                "question": question,
                "documents": documents,
            }
        )

        self.memory.add_user_message(question)
        self.memory.add_ai_message(answer)

        logger.info(
            "Answer generated."
        )

        return answer, documents

    # ---------------------------------------------------------
    # Invoke
    # ---------------------------------------------------------

    def invoke(
        self,
        question: str,
        documents: list[Document],
    ) -> str:
        """
        Generate an answer only.
        """

        answer, _ = self._generate(
            question,
            documents,
        )

        return answer

    # ---------------------------------------------------------
    # Stream
    # ---------------------------------------------------------

    def stream(
        self,
        question: str,
        documents: list[Document],
    ):
        """
        Stream the generated answer.
        """

        logger.info(
            "Streaming question: %s",
            question,
        )

        documents = self._prepare_documents(
            question,
            documents,
        )

        if not documents:

            yield (
                "I couldn't find any relevant information "
                "in the knowledge base to answer your question."
            )
            return

        answer = ""

        for chunk in self.chain.stream(
            {
                "question": question,
                "documents": documents,
            }
        ):
            answer += chunk
            yield chunk

        self.memory.add_user_message(question)
        self.memory.add_ai_message(answer)

    # ---------------------------------------------------------
    # Retrieve Only
    # ---------------------------------------------------------

    def retrieve(
        self,
        questions: str | list[str],
    ) -> list[Document]:
        """
        Return retrieved documents only.
        """

        return self.retriever.invoke(
            questions
        )

    # ---------------------------------------------------------
    # Answer + Sources
    # ---------------------------------------------------------

    def ask(
        self,
        question: str,
        documents: list[Document],
    ) -> dict:
        """
        Return answer, documents, and sources.
        """

        answer, documents = self._generate(
            question,
            documents,
        )

        return {
            "question": question,
            "answer": answer,
            "documents": documents,
            "sources": self.retriever.sources(
                documents
            ),
        }
