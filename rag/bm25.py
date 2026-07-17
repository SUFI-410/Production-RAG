"""
BM25 keyword retriever.

Provides lexical retrieval alongside vector search.
"""

from __future__ import annotations

from langchain_core.documents import Document
from rank_bm25 import BM25Okapi

from rag.logger import get_logger

logger = get_logger(__name__)


class BM25Retriever:
    """
    Simple BM25 retriever for keyword search.
    """

    def __init__(self) -> None:
        self.documents: list[Document] = []
        self.bm25: BM25Okapi | None = None

    # ---------------------------------------------------------
    # Build Index
    # ---------------------------------------------------------

    def build(
        self,
        documents: list[Document],
    ) -> None:

        logger.info(
            "Building BM25 index from %s chunks...",
            len(documents),
        )

        self.documents = documents

        corpus = [
            doc.page_content.lower().split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(corpus)

        logger.info("BM25 index ready.")

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def search(
        self,
        query: str,
        k: int = 5,
    ) -> list[Document]:

        if self.bm25 is None:
            raise RuntimeError(
                "BM25 index has not been built."
            )

        tokens = query.lower().split()

        scores = self.bm25.get_scores(tokens)

        ranked = sorted(
            zip(scores, self.documents),
            reverse=True,
            key=lambda x: x[0],
        )

        return [
            document
            for _, document in ranked[:k]
        ]
