"""
Query Rewriter for Production RAG.

Converts follow-up questions into standalone questions using
conversation history before retrieval.
"""

from __future__ import annotations

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from rag.config import Config
from rag.logger import get_logger

logger = get_logger(__name__)


class QueryRewriter:
    """
    Rewrites follow-up questions into standalone questions.
    """

    def __init__(self):

        self.llm = ChatOpenAI(
            model=Config.CHAT_MODEL,
            temperature=0,
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an expert at rewriting follow-up questions.

Conversation History:
{history}

Current Question:
{question}

Rewrite the current question so it is completely self-contained.

Rules:
- Preserve the original meaning.
- Do NOT answer the question.
- Do NOT add extra information.
- Return ONLY the rewritten question.
- If the question is already standalone, return it unchanged.
"""
        )

        self.chain = (
            self.prompt
            | self.llm
            | StrOutputParser()
        )

    def rewrite(
        self,
        question: str,
        history: str,
    ) -> str:
        """
        Rewrite a question using conversation history.
        """

        if not history.strip():
            return question

        rewritten = self.chain.invoke(
            {
                "question": question,
                "history": history,
            }
        ).strip()

        logger.info("Original Query : %s", question)
        logger.info("Rewritten Query: %s", rewritten)

        return rewritten
