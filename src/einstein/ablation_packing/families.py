"""Problem-family registry — maps a config `family` name to its generic solver adapter.

Lets the runner stay family-agnostic across problem DOMAINS, not just objectives. A
family owns everything the runner needs to drive a cold/warm solve in that domain:

- `score` / `triple_verify` — the bare objective + A1 three-way check (no baked method)
- `cold_init(n, seed)` — a deterministic random start in the family's representation
- `answer_key` — the JSON key the agent emits (`centers` / `vectors` / `values`)
- `config_space(n)` — one-line description of the config space (for the prompt)
- `parse(raw, n)` — validate+coerce the agent's emitted config to an ndarray (or None)
- `format_init(init)` — JSON-serializable form of the start config (for the prompt)

Adding a family that shares the 2D-points representation is one entry; a family in a
NEW representation (sphere vectors, 1D sequences) supplies its own adapters here — no
runner change. This generalization is what makes cross-DOMAIN transfer (Heilbronn →
autocorrelation) possible (pre-reg §0b). Before it, the runner hardcoded
points-in-[0,1]^2 in cold_init, the prompt, and the parser.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

from . import evaluator as ev
from . import heilbronn as heil


@dataclass(frozen=True)
class Family:
    name: str
    score: Callable  # repr -> float (higher = better; all families maximize)
    triple_verify: Callable  # repr -> TripleVerify
    cold_init: Callable  # (n, seed) -> np.ndarray in this family's representation
    answer_key: str  # JSON key the agent writes its config under
    config_space: Callable  # (n) -> str, one-line config-space description for the prompt
    parse: Callable  # (raw, n) -> np.ndarray | None
    format_init: Callable  # (np.ndarray) -> json-serializable start config


# --- 2D points-in-[0,1]^2 representation (equal-circles, Heilbronn) -------------------


def _points2d_parse(raw: object, n: int) -> np.ndarray | None:
    if not isinstance(raw, list) or len(raw) != n:
        return None
    try:
        arr = np.asarray(raw, dtype=np.float64)
    except (ValueError, TypeError):
        return None
    return arr if arr.shape == (n, 2) else None


def _points2d_format(init: np.ndarray) -> list:
    return [[float(x), float(y)] for x, y in init]


def _points2d_space(n: int) -> str:
    return f"{n} points in the unit square [0,1]^2 (each point is [x, y])"


def _points2d_family(name: str, score: Callable, triple_verify: Callable) -> Family:
    return Family(
        name=name,
        score=score,
        triple_verify=triple_verify,
        cold_init=ev.cold_init,
        answer_key="centers",
        config_space=_points2d_space,
        parse=_points2d_parse,
        format_init=_points2d_format,
    )


FAMILIES: dict[str, Family] = {
    "equal_circles_in_unit_square": _points2d_family(
        "equal_circles_in_unit_square", ev.common_radius, ev.triple_verify_radius
    ),
    "heilbronn_triangle": _points2d_family(
        "heilbronn_triangle", heil.min_triangle_area, heil.triple_verify_heilbronn
    ),
}


def register(family: Family) -> None:
    """Register a family (idempotent overwrite). Used by domain modules at import."""
    FAMILIES[family.name] = family


def get_family(name: str) -> Family:
    if name not in FAMILIES:
        # Import side-effect module that self-registers non-geometric families
        # (sphere, 1D-sequence). Defensive: a missing/broken module must still surface
        # the clean KeyError below, not an ImportError.
        try:
            from . import family_domains  # noqa: F401
        except ImportError:
            pass
        if name not in FAMILIES:
            raise KeyError(f"unknown family {name!r}; known: {sorted(FAMILIES)}")
    return FAMILIES[name]
