"""problems/ — per-problem triple-verify registrations.

Each module here calls ``triple_verify.register(problem_id, ...)`` at import
time. This package's ``__init__`` imports every module so that importing
``einstein.triple_verify`` populates the registry as a side effect.

Goal 1 (skeleton) ships this empty. Goal 2 adds P2/P4/P5/P11/P14/P15/P16/P18/P19.
"""

from __future__ import annotations

# Per-problem modules are imported here for their register() side effects.
_MODULES: tuple[str, ...] = (
    "p02_first_autocorrelation",
    "p04_third_autocorrelation",
    "p05_min_distance_ratio",
    "p11_tammes",
    "p14_circle_packing_square",
    "p15_heilbronn_triangles",
    "p16_heilbronn_convex",
    "p18_circles_rectangle",
    "p19_difference_bases",
    "p22_kissing_d12",
)

for _m in _MODULES:
    __import__(f"{__name__}.{_m}")
