"""
Evaluation report utilities.

Responsible for:
- Printing evaluation summaries
- Saving evaluation reports
"""

from __future__ import annotations

import json
from pathlib import Path


class Report:
    """
    Utility class for evaluation reports.
    """

    # ---------------------------------------------------------
    # Console
    # ---------------------------------------------------------

    @staticmethod
    def print(results: dict) -> None:
        """
        Print evaluation summary.
        """

        print("\n" + "=" * 50)
        print("Production RAG Evaluation")
        print("=" * 50)

        for key, value in results.items():

            print(
                f"{key:<25}: {value}"
            )

        print("=" * 50)

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    @staticmethod
    def save(
        results: dict,
        output_file: str | Path,
    ) -> None:
        """
        Save evaluation report as JSON.
        """

        output_file = Path(output_file)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                results,
                file,
                indent=4,
            )
