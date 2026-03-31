"""Knowledge layer — loads structured learnings to inform strategy selection.

The knowledge base lives in the private memory bank and accumulates
cross-problem insights: which strategies work on which problem types,
common pitfalls, and transferable optimization patterns.
"""

from __future__ import annotations

import os
from pathlib import Path

import yaml

_PROJECT = "einstein"
KNOWLEDGE_PATH = (
    Path(os.path.expanduser("~"))
    / "projects"
    / "workbench"
    / "memory-bank"
    / _PROJECT
    / "docs"
    / "knowledge.yaml"
)


def load_knowledge() -> dict:
    """Load the knowledge base from YAML."""
    with open(KNOWLEDGE_PATH) as f:
        return yaml.safe_load(f)


def get_strategy_priors(category: str) -> list[tuple[str, float]]:
    """Return (strategy_name, weight) pairs for a problem category.

    If the category matches a solved problem, use its ranked strategies.
    Otherwise, return uniform weights over all known strategies.
    """
    kb = load_knowledge()
    strategies = list(kb["strategies"].keys())

    # Check if any solved problem shares this category
    for _slug, info in kb["problems"].items():
        if info.get("category") == category and "strategies_ranked" in info:
            ranked = info["strategies_ranked"]
            # Weight by inverse rank: rank 1 → N points, rank N → 1 point
            n = len(ranked)
            priors = [(name, float(n - i)) for i, name in enumerate(ranked)]
            # Add unseen strategies with weight 0.5 (explore)
            seen = {name for name, _ in priors}
            for s in strategies:
                if s not in seen:
                    priors.append((s, 0.5))
            return priors

    # No match — check which strategies list this category in best_for
    priors = []
    for name, info in kb["strategies"].items():
        best_for = info.get("best_for", [])
        weight = 2.0 if category in best_for else 1.0
        priors.append((name, weight))
    return priors


def get_problem_insights(slug: str) -> dict:
    """Return insights and pitfalls for a problem, or empty lists if unknown."""
    kb = load_knowledge()
    info = kb.get("problems", {}).get(slug, {})
    return {
        "insights": info.get("insights", []),
        "pitfalls": info.get("pitfalls", []),
        "strategies_ranked": info.get("strategies_ranked", []),
    }


def get_patterns() -> list[dict]:
    """Return all transferable optimization patterns."""
    kb = load_knowledge()
    return kb.get("patterns", [])
