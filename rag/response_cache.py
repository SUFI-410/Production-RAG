"""
Response cache for the Production RAG application.

Caches complete RAG responses to avoid repeated retrieval
and LLM calls for identical questions.
"""

from __future__ import annotations

import threading
import time


class ResponseCache:
    """
    In-memory response cache with TTL support.
    """

    def __init__(
        self,
        ttl_seconds: int = 3600,
    ) -> None:

        self.ttl_seconds = ttl_seconds

        self._cache: dict[str, dict] = {}

        self._lock = threading.Lock()

    # ---------------------------------------------------------
    # Internal
    # ---------------------------------------------------------

    def _expired(
        self,
        timestamp: float,
    ) -> bool:
        """
        Return True if a cached item has expired.
        """

        return (
            time.time() - timestamp
            > self.ttl_seconds
        )

    # ---------------------------------------------------------
    # Get
    # ---------------------------------------------------------

    def get(
        self,
        question: str,
    ) -> dict | None:
        """
        Return cached response if available.
        """

        key = question.strip().lower()

        with self._lock:

            item = self._cache.get(key)

            if item is None:
                return None

            if self._expired(item["timestamp"]):

                del self._cache[key]

                return None

            return item["response"]

    # ---------------------------------------------------------
    # Set
    # ---------------------------------------------------------

    def set(
        self,
        question: str,
        response: dict,
    ) -> None:
        """
        Store a response.
        """

        key = question.strip().lower()

        with self._lock:

            self._cache[key] = {
                "timestamp": time.time(),
                "response": response,
            }

    # ---------------------------------------------------------
    # Clear
    # ---------------------------------------------------------

    def clear(self) -> None:
        """
        Remove every cached response.
        """

        with self._lock:

            self._cache.clear()

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def size(self) -> int:
        """
        Return number of cached responses.
        """

        with self._lock:

            return len(self._cache)
