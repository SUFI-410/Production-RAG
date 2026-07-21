"""
Utility helpers for the Production RAG application.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from langchain_core.documents import Document

from rag.logger import get_logger

logger = get_logger(__name__)


# ----------------------------------------------------------------------
# Document Formatting
# ----------------------------------------------------------------------


def format_documents(
    documents: list[Document],
) -> str:
    """
    Convert retrieved documents into a numbered context string
    for citation-aware prompting.
    """

    if not documents:
        return ""

    sections: list[str] = []

    for index, document in enumerate(documents, start=1):

        content = document.page_content.strip()

        if not content:
            continue

        source = source_name(document)
        page = page_number(document)

        sections.append(
            f"""
[{index}]
Source: {source}
Page: {page}

{content}
""".strip()
        )

    return "\n\n" + ("-" * 70).join(
        f"\n\n{section}" for section in sections
    )


# ----------------------------------------------------------------------
# Source Helpers
# ----------------------------------------------------------------------


def source_name(
    document: Document,
) -> str:
    """
    Return a human-readable source name.
    """

    source = document.metadata.get("source")

    if not source:
        return "Unknown"

    if isinstance(source, str) and source.startswith("http"):
        return source

    return Path(str(source)).name


def page_number(
    document: Document,
) -> str:
    """
    Return the page number if available.
    """

    page = document.metadata.get("page")

    if page is None:
        return "-"

    if isinstance(page, int):
        return str(page + 1)

    return str(page)


def unique_sources(
    documents: Iterable[Document],
) -> list[tuple[str, str]]:
    """
    Return unique (source, page) tuples.
    """

    seen: set[tuple[str, str]] = set()
    result: list[tuple[str, str]] = []

    for document in documents:

        source = source_name(document)
        page = page_number(document)

        key = (source, page)

        if key not in seen:
            seen.add(key)
            result.append(key)

    return result


def print_sources(
    documents: list[Document],
) -> None:
    """
    Log retrieved document sources.
    """

    logger.info("Sources")
    logger.info("-" * 60)

    for source, page in unique_sources(documents):
        logger.info("• %s (page %s)", source, page)

    logger.info("-" * 60)


# ----------------------------------------------------------------------
# Text Helpers
# ----------------------------------------------------------------------


def truncate(
    text: str,
    length: int = 250,
) -> str:
    """
    Truncate text for previews.
    """

    text = text.strip()

    if len(text) <= length:
        return text

    truncated = text[:length]

    if " " in truncated:
        truncated = truncated.rsplit(" ", 1)[0]

    return truncated + "..."


# ----------------------------------------------------------------------
# Validation
# ----------------------------------------------------------------------


def ensure_documents(
    documents: list[Document],
) -> None:
    """
    Raise an error if no documents exist.
    """

    if not documents:
        raise ValueError(
            "No documents were loaded."
        )


# ----------------------------------------------------------------------
# Metadata
# ----------------------------------------------------------------------


def chunk_metadata(
    document: Document,
) -> dict:
    """
    Return normalized metadata.
    """

    return {
        "source": source_name(document),
        "page": page_number(document),
        "characters": len(document.page_content),
    }


# ----------------------------------------------------------------------
# Pretty Printing
# ----------------------------------------------------------------------


def print_banner(
    title: str,
) -> None:
    """
    Log a section banner.
    """

    line = "=" * 70

    logger.info("")
    logger.info(line)
    logger.info(title)
    logger.info(line)
