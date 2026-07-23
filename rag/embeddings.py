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

_embeddings: Embeddings | None = None


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
            max_retries=3,
        )

        logger.info(
            "Embedding model initialized."
        )

        return embeddings


def get_embeddings() -> Embeddings:
    """
    Return a singleton embedding model.
    """

    global _embeddings

    if _embeddings is None:
        _embeddings = EmbeddingFactory.create()

    return _embeddings
