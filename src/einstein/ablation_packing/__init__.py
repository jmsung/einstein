"""Generic equal-circle-in-unit-square evaluator for the knowledge-compounding
ablation's held-out problem family (config/ablation_problems.yaml).

Deliberately generic — the bare objective + triple-verify + a seeded cold init —
with NO problem-specific wisdom baked in (pre-reg §4 generic-solvers-only rule).
The harness uses this to score whatever configuration the agent-under-test
produces; the agent's self-reported score is never trusted (triple-verify rule).
"""

from .evaluator import (
    TripleVerify,
    cold_init,
    common_radius,
    common_radius_mpmath,
    triple_verify_radius,
)

__all__ = [
    "TripleVerify",
    "cold_init",
    "common_radius",
    "common_radius_mpmath",
    "triple_verify_radius",
]
