"""
Production RAG Chain using LCEL.

Responsibilities:
- Build context
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

        self.llm = ChatOpenAI(
            model=Config.CHAT_MODEL,
            temperature=Config.TEMPERATURE,
        )

        self.prompt = PromptFactory.create()

        self.chain = self._build_chain()

    # ---------------------------------------------------------
    # Context Preparation
    # ---------------------------------------------------------

    def _prepare_context(
        self,
        inputs: dict,
    ) -> str:
        """
        Prepare the context for the LLM.
        """

        question: str = inputs["question"]
        documents: list[Document] = inputs["documents"]

        documents = self.reranker.rerank(
            question=question,
            documents=documents,
        )

        return format_documents(documents)

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
                question=itemgetter("question"),
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
    # Ask
    # ---------------------------------------------------------

    def invoke(
        self,
        question: str,
        documents: list[Document],
    ) -> str:
        """
        Generate a complete answer.
        """

        logger.info("Question: %s", question)

        answer = self.chain.invoke(
            {
                "question": question,
                "documents": documents,
            }
        )

        self.memory.add_user_message(question)
        self.memory.add_ai_message(answer)

        logger.info("Answer generated.")

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
        Stream the generated answer chunk by chunk.
        """

        logger.info("Streaming question: %s", question)

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
        question: str,
    ) -> list[Document]:
        """
        Return retrieved documents only.
        """

        return self.retriever.invoke(question)

    # ---------------------------------------------------------
    # Answer + Sources
    # ---------------------------------------------------------

    def ask(
        self,
        question: str,
        documents: list[Document],
    ) -> dict:
        """
        Return both answer and retrieved documents.
        """

        answer = self.invoke(
            question=question,
            documents=documents,
        )

        return {
            "question": question,
            "answer": answer,
            "documents": documents,
        }
