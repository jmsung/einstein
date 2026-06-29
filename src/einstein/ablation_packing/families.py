"""Problem-family registry — maps a config `family` name to its generic scorer.

Lets the runner stay family-agnostic: the config picks the family, the runner
resolves the objective + triple-verify here. Adding a family = one entry; no
runner change. Each scorer is the BARE objective (no baked method), per the
generic-solvers rule (pre-reg §4).
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from . import evaluator as ev
from . import heilbronn as heil


@dataclass(frozen=True)
class Family:
    name: str
    score: Callable  # centers -> float (higher = better; all families maximize)
    triple_verify: Callable  # centers -> TripleVerify


FAMILIES: dict[str, Family] = {
    "equal_circles_in_unit_square": Family(
        "equal_circles_in_unit_square", ev.common_radius, ev.triple_verify_radius
    ),
    "heilbronn_triangle": Family(
        "heilbronn_triangle", heil.min_triangle_area, heil.triple_verify_heilbronn
    ),
}


def get_family(name: str) -> Family:
    if name not in FAMILIES:
        raise KeyError(f"unknown family {name!r}; known: {sorted(FAMILIES)}")
    return FAMILIES[name]
