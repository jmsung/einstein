"""problems/ — per-problem triple-verify registrations.

Each module here calls ``triple_verify.register(problem_id, ...)`` at import
time. This package's ``__init__`` imports every module so that importing
``einstein.triple_verify`` populates the registry as a side effect.

Registrations cover the 14 manifest ids: P1/P2/P3/P4/P5/P10/P11/P12/P14/P15/P16/P18/P19/P22
(P22 is an honest unavailable_reason stub). The registry-coverage CI gate
(tests/test_triple_verify_registry.py) fails if a manifest id has no entry.
"""

from __future__ import annotations

# Per-problem modules are imported here for their register() side effects.
_MODULES: tuple[str, ...] = (
    "p01_erdos",
    "p02_first_autocorrelation",
    "p03_autocorrelation",
    "p04_third_autocorrelation",
    "p05_min_distance_ratio",
    "p10_thomson",
    "p11_tammes",
    "p12_flat_poly",
    "p14_circle_packing_square",
    "p15_heilbronn_triangles",
    "p16_heilbronn_convex",
    "p18_circles_rectangle",
    "p19_difference_bases",
    "p22_kissing_d12",
)

for _m in _MODULES:
    __import__(f"{__name__}.{_m}")
