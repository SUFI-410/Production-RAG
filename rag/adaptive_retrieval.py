"""
Adaptive retrieval.

Chooses the retrieval depth (Top-K) based on
the complexity of the user's question.
"""

from __future__ import annotations

import re

from rag.config import Config


class AdaptiveRetrieval:
    """
    Determine an appropriate retrieval depth.
    """

    def top_k(
        self,
        question: str,
    ) -> int:

        question = question.lower()

        # ----------------------------------------
        # Very short factual questions
        # ----------------------------------------

        if len(question.split()) <= 5:
            return 4

        # ----------------------------------------
        # Complex questions
        # ----------------------------------------

        complex_patterns = (
            "compare",
            "difference",
            "advantages",
            "disadvantages",
            "summarize",
            "summary",
            "explain",
            "how",
            "why",
            "analyze",
            "architecture",
            "workflow",
            "step by step",
        )

        if any(
            pattern in question
            for pattern in complex_patterns
        ):
            return 12

        # ----------------------------------------
        # Multiple questions
        # ----------------------------------------

        if len(
            re.findall(r"\?", question)
        ) > 1:
            return 15

        # ----------------------------------------
        # Default
        # ----------------------------------------

        return Config.TOP_K
