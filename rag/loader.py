"""
Document loading utilities.

Supports:
- PDF
- Markdown
- Multiple PDFs
- Web pages
- Multiple web pages
- Mixed sources
"""

from __future__ import annotations

import os
from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)

from rag.config import Config
from rag.exceptions import (
    DocumentNotFoundError,
    EmptyDocumentError,
    UnsupportedDocumentError,
)
from rag.crawler import WebsiteCrawler
from rag.logger import get_logger

logger = get_logger(__name__)

# Prevent WebBaseLoader warning
os.environ.setdefault("USER_AGENT", Config.USER_AGENT)


class DocumentLoader:
    """
    Loads documents from supported sources.
    """

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @staticmethod
    def _validate_documents(
        documents: list[Document],
    ) -> list[Document]:

        if not documents:
            raise EmptyDocumentError(
                "No content was loaded."
            )

        documents = [
            doc
            for doc in documents
            if doc.page_content.strip()
        ]

        if not documents:
            raise EmptyDocumentError(
                "Loaded documents are empty."
            )

        return documents

    # ---------------------------------------------------------
    # PDF
    # ---------------------------------------------------------

    @classmethod
    def load_pdf(
        cls,
        pdf_path: str | Path,
    ) -> list[Document]:

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise DocumentNotFoundError(
                f"PDF not found: {pdf_path}"
            )

        logger.info(
            "Loading PDF: %s",
            pdf_path,
        )

        loader = PyPDFLoader(str(pdf_path))

        documents = loader.load()

        for document in documents:
            document.metadata["document_type"] = "pdf"
            document.metadata["file_name"] = pdf_path.name

        logger.info(
            "Loaded %s pages.",
            len(documents),
        )

        return cls._validate_documents(
            documents
        )

    # ---------------------------------------------------------
    # Markdown
    # ---------------------------------------------------------

    @classmethod
    def load_markdown(
        cls,
        md_path: str | Path,
    ) -> list[Document]:

        md_path = Path(md_path)

        if not md_path.exists():
            raise DocumentNotFoundError(
                f"Markdown file not found: {md_path}"
            )

        logger.info(
            "Loading Markdown: %s",
            md_path,
        )

        loader = TextLoader(
            str(md_path),
            encoding="utf-8",
        )

        documents = loader.load()

        for document in documents:
            document.metadata["document_type"] = "markdown"
            document.metadata["file_name"] = md_path.name

        logger.info(
            "Loaded %s markdown document(s).",
            len(documents),
        )

        return cls._validate_documents(
            documents
        )

    # ---------------------------------------------------------
    # Multiple PDFs
    # ---------------------------------------------------------

    @classmethod
    def load_pdfs(
        cls,
        pdfs: list[str | Path],
    ) -> list[Document]:

        all_documents: list[Document] = []

        for pdf in pdfs:
            all_documents.extend(
                cls.load_pdf(pdf)
            )

        logger.info(
            "Loaded %s total PDF pages.",
            len(all_documents),
        )

        return cls._validate_documents(
            all_documents
        )

    # ---------------------------------------------------------
    # Multiple Markdown Files
    # ---------------------------------------------------------

    @classmethod
    def load_markdowns(
        cls,
        markdowns: list[str | Path],
    ) -> list[Document]:

        all_documents: list[Document] = []

        for markdown in markdowns:
            all_documents.extend(
                cls.load_markdown(markdown)
            )

        logger.info(
            "Loaded %s markdown document(s).",
            len(all_documents),
        )

        return cls._validate_documents(
            all_documents
        )

    # ---------------------------------------------------------
    # Website
    # ---------------------------------------------------------

    @classmethod
    def load_web(
        cls,
        url: str,
    ) -> list[Document]:
        """
        Crawl an entire website.
        """

        logger.info(
            "Crawling website: %s",
            url,
        )

        crawler = WebsiteCrawler(
            max_pages=100,
        )

        documents = crawler.crawl(url)

        for document in documents:

            document.metadata.setdefault(
                "document_type",
                "web",
            )

            document.metadata.setdefault(
                "url",
                document.metadata.get(
                    "source",
                    url,
                ),
            )

        logger.info(
            "Loaded %s webpage document(s).",
            len(documents),
        )

        return cls._validate_documents(
            documents
        )

    # ---------------------------------------------------------
    # Multiple Websites
    # ---------------------------------------------------------

    @classmethod
    def load_websites(
        cls,
        urls: list[str],
    ) -> list[Document]:

        all_documents: list[Document] = []

        for url in urls:
            all_documents.extend(
                cls.load_web(url)
            )

        return cls._validate_documents(
            all_documents
        )

    # ---------------------------------------------------------
    # Mixed Sources
    # ---------------------------------------------------------

    @classmethod
    def load_sources(
        cls,
        sources: list[dict],
    ) -> list[Document]:

        documents: list[Document] = []

        for source in sources:

            source_type = (
                source.get("type", "")
                .strip()
                .lower()
            )

            if source_type == "pdf":

                documents.extend(
                    cls.load_pdf(
                        source["path"]
                    )
                )

            elif source_type == "markdown":

                documents.extend(
                    cls.load_markdown(
                        source["path"]
                    )
                )

            elif source_type == "web":

                documents.extend(
                    cls.load_web(
                        source["url"]
                    )
                )

            else:

                raise UnsupportedDocumentError(
                    f"Unsupported source type: {source_type}"
                )

        logger.info(
            "Loaded %s document(s).",
            len(documents),
        )

        return cls._validate_documents(
            documents
        )

    # ---------------------------------------------------------
    # Directory
    # ---------------------------------------------------------

    @classmethod
    def load_directory(
        cls,
        directory: str | Path,
    ) -> list[Document]:

        directory = Path(directory)

        if not directory.exists():

            raise DocumentNotFoundError(
                f"Directory not found: {directory}"
            )

        documents: list[Document] = []

        pdfs = sorted(
            directory.glob("*.pdf")
        )

        markdowns = sorted(
            directory.glob("*.md")
        )

        if pdfs:
            documents.extend(
                cls.load_pdfs(pdfs)
            )

        if markdowns:
            documents.extend(
                cls.load_markdowns(markdowns)
            )

        if not documents:

            raise DocumentNotFoundError(
                "No supported documents found."
            )

        return cls._validate_documents(
            documents
        )
