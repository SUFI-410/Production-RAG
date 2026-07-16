"""
Embedding model factory.

Responsible for creating embedding models.
"""

from __future__ import annotations

from langchain_core.embeddings import Embeddings
from langchain_openai import OpenAIEmbeddings

from rag.config import Config
from rag.logger import get_logger

logger = get_logger(__name__)


class EmbeddingFactory:
    """
    Factory class for embedding models.
    """

    @staticmethod
    def create() -> Embeddings:
        """
        Create and return the configured embedding model.
        """

        logger.info(
            "Loading embedding model: %s",
            Config.EMBEDDING_MODEL,
        )

        embeddings = OpenAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            api_key=Config.OPENAI_API_KEY,
            max_retries=3,
            request_timeout=Config.REQUEST_TIMEOUT,
        )

        logger.info(
            "Embedding model initialized."
        )

        return embeddings
