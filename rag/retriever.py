"""
Retriever utilities.

Responsible for retrieving relevant documents from
the vector store.
"""

from __future__ import annotations

from langchain_core.documents import Document

from rag.exceptions import (
    NoDocumentsRetrievedError,
)
from rag.logger import get_logger

logger = get_logger(__name__)


class Retriever:
    """
    Wrapper around a LangChain retriever.
    """

    def __init__(self, retriever):

        self._retriever = retriever

    # ---------------------------------------------------------
    # Retrieve
    # ---------------------------------------------------------

    def retrieve(
        self,
        question: str,
    ) -> list[Document]:
        """
        Retrieve relevant documents.
        """

        logger.info(
            "Searching for: %s",
            question,
        )

        documents = self._retriever.invoke(
            question
        )

        if not documents:

            raise NoDocumentsRetrievedError(
                "No relevant documents found."
            )

        logger.info(
            "Retrieved %s document(s).",
            len(documents),
        )

        return documents

    # ---------------------------------------------------------
    # Preview
    # ---------------------------------------------------------

    @staticmethod
    def preview(
        documents: list[Document],
        limit: int = 3,
    ) -> None:
        """
        Preview retrieved documents.
        """

        logger.info("=" * 60)
        logger.info("Retrieved Context")
        logger.info("=" * 60)

        for index, document in enumerate(
            documents[:limit],
            start=1,
        ):

            logger.info(
                "[%s]\n%s\n",
                index,
                document.page_content[:300],
            )

        logger.info("=" * 60)

    # ---------------------------------------------------------
    # Sources
    # ---------------------------------------------------------

    @staticmethod
    def sources(
        documents: list[Document],
    ) -> list[dict]:
        """
        Return unique document sources.
        """

        seen = set()
        result = []

        for document in documents:

            source = document.metadata.get(
                "source",
                "Unknown",
            )

            page = document.metadata.get(
                "page",
                "-",
            )

            key = (source, page)

            if key in seen:
                continue

            seen.add(key)

            result.append(
                {
                    "source": source,
                    "page": page,
                }
            )

        return result
