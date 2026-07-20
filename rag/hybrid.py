from __future__ import annotations

from langchain_core.documents import Document
from langchain_core.runnables import RunnableLambda

from rag.bm25 import BM25Retriever
from rag.logger import get_logger

logger = get_logger(__name__)


class HybridRetriever(RunnableLambda):
    """
    Hybrid Retriever.

    Combines semantic retrieval (Chroma)
    with lexical retrieval (BM25).
    """

    def __init__(
        self,
        chroma_retriever,
        bm25_retriever: BM25Retriever,
    ) -> None:

        self.chroma = chroma_retriever
        self.bm25 = bm25_retriever

        super().__init__(self._retrieve)

    def _retrieve(
        self,
        query: str,
    ) -> list[Document]:

        semantic_docs = self.chroma.invoke(query)

        keyword_docs = self.bm25.search(query)

        logger.info(
            "Hybrid Retrieval: %s semantic + %s keyword",
            len(semantic_docs),
            len(keyword_docs),
        )

        merged: list[Document] = []
        seen: set[str] = set()

        for document in semantic_docs + keyword_docs:

            key = (
                document.metadata.get("source", "")
                + str(document.metadata.get("start_index", ""))
            )

            if key in seen:
                continue

            seen.add(key)
            merged.append(document)

        logger.info(
            "Hybrid Retrieval: %s merged documents",
            len(merged),
        )

        return merged
