"""
Cross Encoder reranker.

Reorders retrieved documents using a cross encoder model.
"""

from __future__ import annotations

from langchain_core.documents import Document
from sentence_transformers import CrossEncoder

from rag.logger import get_logger

logger = get_logger(__name__)


class Reranker:
    """
    Cross-encoder reranker.

    Uses:
        BAAI/bge-reranker-base
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-base",
    ) -> None:

        logger.info(
            "Loading reranker model: %s",
            model_name,
        )

        self.model = CrossEncoder(model_name)

        logger.info(
            "Reranker ready."
        )

    # ---------------------------------------------------------
    # Rerank
    # ---------------------------------------------------------

    def rerank(
        self,
        question: str,
        documents: list[Document],
        top_k: int = 5,
    ) -> list[Document]:
        """
        Rerank retrieved documents.
        """

        if not documents:
            return []

        logger.info(
            "Reranking %s document(s)...",
            len(documents),
        )

        pairs = [
            (
                question,
                document.page_content,
            )
            for document in documents
        ]

        scores = self.model.predict(
            pairs
        )

        ranked = sorted(
            zip(scores, documents),
            key=lambda x: x[0],
            reverse=True,
        )

        results = [
            document
            for _, document in ranked[:top_k]
        ]

        logger.info(
            "Returning top %s reranked document(s).",
            len(results),
        )

        return results

    # ---------------------------------------------------------
    # Preview Scores
    # ---------------------------------------------------------

    def preview(
        self,
        question: str,
        documents: list[Document],
        limit: int = 5,
    ) -> None:

        if not documents:
            return

        pairs = [
            (
                question,
                document.page_content,
            )
            for document in documents
        ]

        scores = self.model.predict(
            pairs
        )

        logger.info("=" * 60)
        logger.info("Reranker Scores")
        logger.info("=" * 60)

        for index, (score, document) in enumerate(
            zip(scores, documents),
            start=1,
        ):

            if index > limit:
                break

            logger.info(
                "[%s] %.4f | %s",
                index,
                float(score),
                document.metadata.get(
                    "source",
                    "Unknown",
                ),
            )

        logger.info("=" * 60)
