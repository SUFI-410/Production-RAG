"""
Markdown document importer.
"""

from __future__ import annotations

from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

from rag.logger import get_logger

logger = get_logger(__name__)


class MarkdownImporter:
    """
    Imports markdown documents into the knowledge base.
    """

    def __init__(
        self,
        docs_directory: str | Path = "data/docs",
    ) -> None:

        self.docs_directory = Path(docs_directory)

        self.docs_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ---------------------------------------------------------
    # Save Markdown
    # ---------------------------------------------------------

    def save_document(
        self,
        filename: str,
        content: str,
    ) -> Path:

        if not filename.endswith(".md"):
            filename += ".md"

        path = self.docs_directory / filename

        path.write_text(
            content.strip(),
            encoding="utf-8",
        )

        logger.info(
            "Saved %s",
            path,
        )

        return path

    # ---------------------------------------------------------
    # Download Web Page
    # ---------------------------------------------------------

    def download_page(
        self,
        url: str,
        filename: str,
    ) -> Path:

        logger.info(
            "Downloading %s",
            url,
        )

        response = requests.get(
            url,
            timeout=30,
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser",
        )

        # Remove unwanted elements
        for tag in soup(
            [
                "script",
                "style",
                "header",
                "footer",
                "nav",
                "noscript",
                "svg",
            ]
        ):
            tag.decompose()

        converter = html2text.HTML2Text()

        converter.ignore_links = False
        converter.ignore_images = True
        converter.body_width = 0

        markdown = converter.handle(
            str(soup)
        )

        return self.save_document(
            filename,
            markdown,
        )

    # ---------------------------------------------------------
    # List Documents
    # ---------------------------------------------------------

    def list_documents(
        self,
    ) -> list[Path]:

        return sorted(
            self.docs_directory.glob("*.md")
        )
