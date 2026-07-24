"""
Evaluation metrics for the Production AI Platform.

This module contains reusable metrics for evaluating
retrieval quality and system performance.
"""

from __future__ import annotations

from statistics import mean


class Metrics:
    """
    Collection of evaluation metrics.
    """

    # ---------------------------------------------------------
    # Retrieval Metrics
    # ---------------------------------------------------------

    @staticmethod
    def retrieval_accuracy(
        expected: list[str],
        retrieved: list[str],
    ) -> float:
        """
        Calculate retrieval accuracy.

        Returns
        -------
        float
            Percentage of expected documents retrieved.
        """

        if not expected:
            return 0.0

        matches = sum(
            document in retrieved
            for document in expected
        )

        return matches / len(expected)

    @staticmethod
    def hit_at_k(
        expected: list[str],
        retrieved: list[str],
        k: int,
    ) -> int:
        """
        Hit@K metric.

        Returns
        -------
        int
            1 if any expected document appears
            in the top-k retrieved documents,
            otherwise 0.
        """

        top_k = retrieved[:k]

        return int(
            any(
                document in top_k
                for document in expected
            )
        )

    # ---------------------------------------------------------
    # Performance Metrics
    # ---------------------------------------------------------

    @staticmethod
    def average_latency(
        latencies: list[float],
    ) -> float:
        """
        Average response latency in seconds.
        """

        if not latencies:
            return 0.0

        return mean(latencies)
