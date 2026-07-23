"""
Context compression using embedding similarity.

Keeps only the most relevant retrieved documents before
sending context to the LLM.
"""

from __future__ import annotations

from langchain_core.documents import Document

from rag.embeddings import get_embeddings
from rag.logger import get_logger

logger = get_logger(__name__)


class ContextCompressor:
    """
    Compress retrieved documents by semantic similarity.
    """

    def __init__(
        self,
        top_k: int = 5,
    ) -> None:

        self.top_k = top_k
        self.embeddings = get_embeddings()

    def compress(
        self,
        question: str,
        documents: list[Document],
    ) -> list[Document]:

        if not documents:
            return []

        logger.info(
            "Compressing %d document(s)...",
            len(documents),
        )

        query_embedding = self.embeddings.embed_query(question)

        scored_documents = []

        for document in documents:

            document_embedding = self.embeddings.embed_query(
                document.page_content
            )

            score = sum(
                q * d
                for q, d in zip(
                    query_embedding,
                    document_embedding,
                )
            )

            scored_documents.append(
                (
                    score,
                    document,
                )
            )

        scored_documents.sort(
            key=lambda x: x[0],
            reverse=True,
        )

        compressed = [
            document
            for _, document in scored_documents[: self.top_k]
        ]

        logger.info(
            "Compressed to %d document(s).",
            len(compressed),
        )

        return compressed
