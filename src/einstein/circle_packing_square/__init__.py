"""Problem 14: Circle Packing in a Square (n=26).

Maximize Σ r_i over n=26 circles packed in the unit square [0,1]^2,
disjoint, fully contained.
"""

from .evaluator import (
    N_CIRCLES,
    OVERLAP_TOL,
    evaluate,
    evaluate_strict,
    evaluate_verbose,
)

__all__ = [
    "N_CIRCLES",
    "OVERLAP_TOL",
    "evaluate",
    "evaluate_strict",
    "evaluate_verbose",
]
