"""
Custom exceptions used throughout the RAG application.
"""

from __future__ import annotations


class RAGError(Exception):
    """
    Base exception for the application.
    """

    pass


# ------------------------------------------------------------------
# Configuration
# ------------------------------------------------------------------


class ConfigurationError(RAGError):
    """
    Raised when configuration is invalid.
    """

    pass


# ------------------------------------------------------------------
# Documents
# ------------------------------------------------------------------


class DocumentError(RAGError):
    """
    Base document exception.
    """

    pass


class DocumentNotFoundError(DocumentError):
    """
    Raised when a document cannot be found.
    """

    pass


class UnsupportedDocumentError(DocumentError):
    """
    Raised when an unsupported document type is supplied.
    """

    pass


class EmptyDocumentError(DocumentError):
    """
    Raised when a document contains no text.
    """

    pass


# ------------------------------------------------------------------
# Vector Store
# ------------------------------------------------------------------


class VectorStoreError(RAGError):
    """
    Base vector store exception.
    """

    pass


class VectorStoreNotInitializedError(VectorStoreError):
    """
    Raised when the vector database has not been initialized.
    """

    pass


class CollectionNotFoundError(VectorStoreError):
    """
    Raised when a Chroma collection cannot be found.
    """

    pass


# ------------------------------------------------------------------
# Retrieval
# ------------------------------------------------------------------


class RetrievalError(RAGError):
    """
    Base retrieval exception.
    """

    pass


class NoDocumentsRetrievedError(RetrievalError):
    """
    Raised when no relevant documents are returned.
    """

    pass


# ------------------------------------------------------------------
# LLM
# ------------------------------------------------------------------


class LLMError(RAGError):
    """
    Base language model exception.
    """

    pass


class LLMConnectionError(LLMError):
    """
    Raised when communication with the language model fails.
    """

    pass


# ------------------------------------------------------------------
# Application
# ------------------------------------------------------------------


class ApplicationNotInitializedError(RAGError):
    """
    Raised when the application is used before initialization.
    """

    pass
