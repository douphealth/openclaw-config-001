#!/usr/bin/env python3
"""Simple priority scorer for WordPress task queue."""

from dataclasses import dataclass

@dataclass
class Task:
    name: str
    impact: int      # 1-5
    risk: int        # 1-5 (higher = worse)
    reversible: int  # 1-5
    confidence: int  # 1-5


def score(t: Task) -> float:
    return (t.impact * 2.0) + (t.reversible * 1.0) + (t.confidence * 1.0) - (t.risk * 1.5)


if __name__ == '__main__':
    tasks = [
        Task('Fix canonical blocker', 5, 2, 4, 5),
        Task('Rewrite money page intro', 4, 2, 5, 4),
        Task('Bulk plugin change', 3, 4, 2, 3),
    ]
    ranked = sorted(tasks, key=score, reverse=True)
    for t in ranked:
        print(f"{score(t):.1f} :: {t.name}")
