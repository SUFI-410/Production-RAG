"""
Main RAG application orchestrator.
"""

from __future__ import annotations

from pathlib import Path

from rag.chain import RAGChain
from rag.loader import DocumentLoader
from rag.logger import get_logger
from rag.memory import ConversationMemory
from rag.query_rewriter import QueryRewriter
from rag.reranker import Reranker
from rag.vector_store import VectorStoreManager

logger = get_logger(__name__)


class RAGApplication:
    """
    High-level interface for the Production RAG system.
    """

    def __init__(self) -> None:

        self.vector_manager = VectorStoreManager()

        self.reranker = Reranker()

        self.memory = ConversationMemory()

        self.query_rewriter = QueryRewriter()

        self.chain: RAGChain | None = None

    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _create_chain(
        self,
        metadata_filter: dict[str, str] | None = None,
    ) -> RAGChain:
        """
        Create a RAG chain using the requested metadata filter.
        """

        retriever = self.vector_manager.as_retriever(
            metadata_filter=metadata_filter,
        )

        return RAGChain(
            retriever=retriever,
            reranker=self.reranker,
            memory=self.memory,
        )

    # ---------------------------------------------------------
    # Initialization
    # ---------------------------------------------------------

    def initialize_pdf(
        self,
        pdf_path: str | Path,
    ) -> None:

        logger.info("Initializing from PDF...")

        documents = DocumentLoader.load_pdf(pdf_path)

        self.vector_manager.load_or_create(documents)

        self.chain = self._create_chain()

        logger.info("Application initialized.")

    def initialize_pdfs(
        self,
        pdfs: list[str | Path],
    ) -> None:

        logger.info("Initializing from PDFs...")

        documents = DocumentLoader.load_pdfs(pdfs)

        self.vector_manager.load_or_create(documents)

        self.chain = self._create_chain()

        logger.info("Application initialized.")

    def initialize_web(
        self,
        url: str,
    ) -> None:

        logger.info("Initializing from website...")

        documents = DocumentLoader.load_web(url)

        self.vector_manager.load_or_create(documents)

        self.chain = self._create_chain()

        logger.info("Application initialized.")

    def initialize_sources(
        self,
        sources: list[dict],
    ) -> None:

        logger.info("Initializing from mixed sources...")

        documents = DocumentLoader.load_sources(sources)

        self.vector_manager.load_or_create(documents)

        self.chain = self._create_chain()

        logger.info("Application initialized.")

    def load_existing(self) -> None:

        logger.info("Loading existing database...")

        self.vector_manager.load()

        self.chain = self._create_chain()

        logger.info("Existing database loaded.")

    # ---------------------------------------------------------
    # Incremental Ingestion
    # ---------------------------------------------------------

    def add_pdf(
        self,
        pdf_path: str | Path,
    ) -> None:
        """
        Add a PDF to the existing database.
        """

        logger.info("Adding PDF: %s", pdf_path)

        documents = DocumentLoader.load_pdf(pdf_path)

        self.vector_manager.add_documents(documents)

        self.chain = self._create_chain()

        logger.info("PDF added successfully.")

    def add_pdfs(
        self,
        pdfs: list[str | Path],
    ) -> None:
        """
        Add multiple PDFs to the existing database.
        """

        logger.info("Adding multiple PDFs...")

        documents = DocumentLoader.load_pdfs(pdfs)

        self.vector_manager.add_documents(documents)

        self.chain = self._create_chain()

        logger.info("PDFs added successfully.")

    def add_web(
        self,
        url: str,
    ) -> None:
        """
        Add a website to the existing database.
        """

        logger.info("Adding website: %s", url)

        documents = DocumentLoader.load_web(url)

        self.vector_manager.add_documents(documents)

        self.chain = self._create_chain()

        logger.info("Website added successfully.")

    # ---------------------------------------------------------
    # Ask
    # ---------------------------------------------------------

    def ask(
        self,
        question: str,
        metadata_filter: dict[str, str] | None = None,
    ) -> str:
        """
        Return only the generated answer.
        """

        if self.chain is None:
            raise RuntimeError(
                "Application has not been initialized."
            )

        history = self.memory.formatted_history()

        rewritten_question = (
            self.query_rewriter.rewrite(
                question=question,
                history=history,
            )
            if history.strip()
            else question
        )

        chain = (
            self.chain
            if metadata_filter is None
            else self._create_chain(metadata_filter)
        )

        # Retrieve documents ONCE
        documents = chain.retrieve(rewritten_question)

        return chain.invoke(
            question=rewritten_question,
            documents=documents,
        )

    def ask_with_sources(
        self,
        question: str,
        metadata_filter: dict[str, str] | None = None,
    ) -> dict:
        """
        Return answer plus retrieved documents.
        """

        if self.chain is None:
            raise RuntimeError(
                "Application has not been initialized."
            )

        history = self.memory.formatted_history()

        rewritten_question = (
            self.query_rewriter.rewrite(
                question=question,
                history=history,
            )
            if history.strip()
            else question
        )

        chain = (
            self.chain
            if metadata_filter is None
            else self._create_chain(metadata_filter)
        )

        # Retrieve documents ONCE
        documents = chain.retrieve(rewritten_question)

        return chain.ask(
            question=rewritten_question,
            documents=documents,
        )

    # ---------------------------------------------------------
    # Database
    # ---------------------------------------------------------

    def reset_database(self) -> None:
        """
        Delete the Chroma database.
        """

        self.vector_manager.reset()

    def database_size(self) -> int:
        """
        Return indexed chunk count.
        """

        return self.vector_manager.document_count()
