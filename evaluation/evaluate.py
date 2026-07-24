"""
Evaluation runner for the Production AI Platform.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from evaluation.metrics import Metrics
from evaluation.report import Report
from rag.application import RAGApplication


DATASET = Path("evaluation/dataset.json")
OUTPUT = Path("evaluation/results/report.json")


def load_dataset() -> list[dict]:
    """
    Load evaluation dataset.
    """

    with DATASET.open(
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def main() -> None:

    app = RAGApplication()

    app.load_existing()

    dataset = load_dataset()

    retrieval_scores: list[float] = []

    hit_scores: list[int] = []

    latencies: list[float] = []

    print(
        f"\nRunning {len(dataset)} evaluation(s)...\n"
    )

    for sample in dataset:

        question = sample["question"]

        expected = sample["expected_documents"]

        start = time.perf_counter()

        result = app.ask_with_sources(
            question
        )

        latency = (
            time.perf_counter() - start
        )

        latencies.append(latency)

        retrieved = [
            source["document"]
            for source in result["sources"]
        ]

        retrieval_scores.append(
            Metrics.retrieval_accuracy(
                expected,
                retrieved,
            )
        )

        hit_scores.append(
            Metrics.hit_at_k(
                expected,
                retrieved,
                k=3,
            )
        )

        print(
            f"✓ {question}"
        )

    results = {
        "Questions Tested": len(dataset),
        "Average Retrieval Accuracy":
            round(
                sum(retrieval_scores)
                / len(retrieval_scores),
                3,
            ),
        "Hit@3":
            round(
                sum(hit_scores)
                / len(hit_scores),
                3,
            ),
        "Average Latency (sec)":
            round(
                Metrics.average_latency(
                    latencies
                ),
                3,
            ),
    }

    Report.print(results)

    Report.save(
        results,
        OUTPUT,
    )


if __name__ == "__main__":

    main()
