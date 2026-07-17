from __future__ import annotations

from langchain_core.documents import Document

from rag.bm25 import BM25Retriever


class HybridRetriever:
    """
    Combines semantic search (Chroma) with keyword search (BM25).
    """

    def __init__(
        self,
        chroma_retriever,
        bm25_retriever: BM25Retriever,
    ) -> None:

        self.chroma = chroma_retriever
        self.bm25 = bm25_retriever

    def invoke(
        self,
        query: str,
    ) -> list[Document]:

        semantic_docs = self.chroma.invoke(query)

        keyword_docs = self.bm25.search(query)

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

        return merged
