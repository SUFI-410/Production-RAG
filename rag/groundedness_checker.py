"""
Groundedness checker.

Validates whether an AI-generated answer
is supported by retrieved context.

Purpose:
- Reduce hallucinations
- Ensure answers are based on sources
- Provide confidence before returning responses
"""

from __future__ import annotations

import json
from dataclasses import dataclass

from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from rag.config import Config
from rag.logger import get_logger


logger = get_logger(__name__)


@dataclass
class GroundednessResult:
    """
    Result returned by groundedness validation.
    """

    grounded: bool
    explanation: str


class GroundednessChecker:
    """
    Checks if the generated answer is supported
    by retrieved documents.
    """

    def __init__(self) -> None:

        self.llm = ChatOpenAI(
            model=Config.CHAT_MODEL,
            temperature=0,
        )

    # ---------------------------------------------------------
    # Validate
    # ---------------------------------------------------------

    def validate(
        self,
        answer: str,
        documents: list[Document],
    ) -> GroundednessResult:
        """
        Determine whether the answer is supported
        by retrieved context.
        """

        if not documents:
            logger.warning(
                "Groundedness check skipped: no documents."
            )

            return GroundednessResult(
                grounded=False,
                explanation="No supporting documents found.",
            )

        context = self._build_context(
            documents
        )

        prompt = f"""
You are a groundedness validator for a RAG system.

Your task:
Determine whether the answer is fully supported
by the provided context.

Rules:
- Return ONLY JSON.
- grounded must be true or false.
- If any important claim is unsupported,
  grounded must be false.

Context:
----------------
{context}
----------------

Answer:
----------------
{answer}
----------------

Return:

{{
    "grounded": true,
    "explanation": "short reason"
}}
"""

        try:

            response = self.llm.invoke(
                prompt
            )

            content = response.content

            # LangChain allows multimodal content blocks,
            # but validator requires plain text JSON.
            if not isinstance(content, str):
                content = str(content)

            return self._parse_result(
                content
            )

        except Exception as exc:

            logger.exception(
                "Groundedness validation failed: %s",
                exc,
            )

            # Fail open:
            # Do not block production responses
            # if validator fails.

            return GroundednessResult(
                grounded=True,
                explanation="Validation unavailable.",
            )

    # ---------------------------------------------------------
    # Context builder
    # ---------------------------------------------------------

    @staticmethod
    def _build_context(
        documents: list[Document],
    ) -> str:
        """
        Convert documents into validator context.
        """

        parts = []

        for index, document in enumerate(
            documents,
            start=1,
        ):

            parts.append(
                f"""
Document {index}:

{document.page_content}
"""
            )

        return "\n".join(parts)

    # ---------------------------------------------------------
    # JSON parser
    # ---------------------------------------------------------

    @staticmethod
    def _parse_result(
        content: str,
    ) -> GroundednessResult:
        """
        Parse validator JSON response.
        """

        try:

            data = json.loads(
                content
            )

            return GroundednessResult(
                grounded=bool(
                    data.get(
                        "grounded",
                        False,
                    )
                ),
                explanation=str(
                    data.get(
                        "explanation",
                        "",
                    )
                ),
            )

        except Exception:

            logger.warning(
                "Invalid validator response: %s",
                content,
            )

            return GroundednessResult(
                grounded=False,
                explanation=(
                    "Validator returned invalid output."
                ),
            )
