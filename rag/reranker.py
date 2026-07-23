"""
Cross Encoder reranker.

Reorders retrieved documents using a cross encoder model.
"""

from __future__ import annotations

from langchain_core.documents import Document
from sentence_transformers import CrossEncoder

from rag.config import Config
from rag.logger import get_logger

logger = get_logger(__name__)


class Reranker:
    """
    Cross-encoder reranker.

    Uses the model configured in Config.RERANKER_MODEL.
    """

    def __init__(self) -> None:

        model_name = Config.RERANKER_MODEL

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
        top_k: int | None = None,
    ) -> list[Document]:
        """
        Rerank retrieved documents and discard irrelevant ones.
        """

        if not documents:
            return []

        if top_k is None:
            top_k = Config.RERANK_TOP_K

        logger.info(
            "Reranking %d document(s)...",
            len(documents),
        )

        pairs = [
            (
                question,
                document.page_content,
            )
            for document in documents
        ]

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(scores, documents),
            key=lambda x: float(x[0]),
            reverse=True,
        )

        logger.info("=" * 60)
        logger.info("Cross-Encoder Ranking")
        logger.info("=" * 60)

        filtered_documents: list[Document] = []

        for index, (score, document) in enumerate(
            ranked,
            start=1,
        ):
            score = float(score)

            # Save score into metadata
            document.metadata["rerank_score"] = score

            logger.info(
                "[%d] %.6f | %s",
                index,
                score,
                document.metadata.get(
                    "source",
                    "Unknown",
                ),
            )

            # Apply threshold
            if score >= Config.RERANK_THRESHOLD:
                filtered_documents.append(document)

        logger.info("=" * 60)
        logger.info(
            "Threshold : %.3f",
            Config.RERANK_THRESHOLD,
        )
        logger.info(
            "Kept      : %d document(s)",
            len(filtered_documents),
        )
        logger.info(
            "Removed   : %d document(s)",
            len(documents) - len(filtered_documents),
        )

        # Keep only top_k after filtering
        filtered_documents = filtered_documents[:top_k]

        logger.info(
            "Returning %d reranked document(s).",
            len(filtered_documents),
        )

        return filtered_documents
