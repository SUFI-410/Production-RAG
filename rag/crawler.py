"""
Website crawler.

Recursively crawls pages from one domain and returns
LangChain Documents.
"""

from __future__ import annotations

from collections import deque
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document

from rag.logger import get_logger

logger = get_logger(__name__)


class WebsiteCrawler:
    """
    Crawl an entire website.
    """

    def __init__(
        self,
        max_pages: int = 100,
    ) -> None:

        self.max_pages = max_pages

    def crawl(
        self,
        start_url: str,
    ) -> list[Document]:

        visited: set[str] = set()

        queue = deque([start_url])

        documents: list[Document] = []

        domain = urlparse(start_url).netloc

        while queue and len(visited) < self.max_pages:

            url = queue.popleft()

            if url in visited:
                continue

            visited.add(url)

            logger.info("Crawling %s", url)

            try:

                response = requests.get(
                    url,
                    timeout=20,
                    headers={
                        "User-Agent": "Mozilla/5.0",
                    },
                )

                response.raise_for_status()

            except Exception:

                continue

            soup = BeautifulSoup(
                response.text,
                "html.parser",
            )

            text = soup.get_text(
                separator="\n",
                strip=True,
            )

            if text:

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "document_type": "web",
                            "url": url,
                            "source": url,
                        },
                    )
                )

            for link in soup.find_all(
                "a",
                href=True,
            ):

                absolute = urljoin(
                    url,
                    link["href"],
                )

                parsed = urlparse(absolute)

                if parsed.netloc != domain:
                    continue

                absolute = parsed._replace(
                    fragment=""
                ).geturl()

                if absolute not in visited:

                    queue.append(
                        absolute
                    )

        logger.info(
            "Crawled %s page(s).",
            len(documents),
        )

        return documents
