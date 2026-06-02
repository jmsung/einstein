"""Generic mpmath ULP-polish — dual-gate coordinate descent at the float64 ceiling.

Phase 2a extraction from ``scripts/circle_packing_square/mpmath_ulp_polish.py``
(P14). The reusable core is two things:

1. **Bit-level ulp stepping** (``ulp_neighbors``) and an exact-binary mpmath copy
   (``to_mp``) — the primitives a sub-ulp polisher needs to be honest.
2. **The DUAL gate** (``dual_gate_accept``) that makes a sub-ulp move
   trustworthy. A candidate is accepted only if it
     - is feasible under BOTH the arena's float64 strict check AND mpmath-exact
       (when a hard constraint exists), and
     - STRICTLY improves the exact (mpmath) objective — the trustworthy signal, and
     - does NOT regress the arena float64 objective — so we never bank a move the
       arena (which scores in float64) would see as worse.

   Gating on a single evaluator is unsafe: exact-only admits a move whose float64
   distance overlaps (the arena rejects it); float64-only re-opens the
   tolerance-band exploit. See
   ``docs/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md``.

What changes per problem is only the *adapter* — the merit functions, the
optional feasibility predicate, and how candidate ulp moves are generated. The
accept logic and the sweep engine are invariant. Merit functions are always
"higher is better"; a minimization problem negates its objective.

Used by: P14 (circle_packing_square), P11 (tammes), P5 (min_distance_ratio).
See each ``scripts/<problem>/mpmath_ulp_polish.py``. The technique has a
soundness boundary — it does NOT apply to P18 (tolerance-band seed), P17
(penalty-shaped score), or P22/P23 (O(n^2) mpmath); see
``docs/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md`` and the three
``dead-end-ulp-polish-*`` findings for why.
"""

from __future__ import annotations

import struct
from collections.abc import Callable, Iterable
from dataclasses import dataclass

import mpmath as mp
import numpy as np


def ulp_neighbors(x: float, steps: tuple[int, ...] = (-2, -1, 1, 2)) -> list[float]:
    """Return the float64 values ``steps`` ulps away from ``x``.

    Bit-level integer arithmetic on the IEEE-754 representation — NOT
    multiplicative scaling. ``x * (1 + 1e-16)`` is not 1 ulp. The int64
    reinterpretation of float64 is monotone in *magnitude* for finite values:
    for ``x < 0`` a ``+1``-bit step makes ``x`` more negative. The step→sign
    mapping is irrelevant to correctness — every candidate is independently
    gated and ranked by its exact merit (negative coordinates occur in the P5
    and P11 seeds, and are handled by the per-candidate gate, not by the step).
    """
    bits = struct.unpack("<q", struct.pack("<d", x))[0]
    out = []
    for s in steps:
        nb = bits + s
        out.append(struct.unpack("<d", struct.pack("<q", nb))[0])
    return out


def to_mp(arr: np.ndarray) -> list[list[mp.mpf]]:
    """Exact-binary-precision copy of a 2-D configuration.

    ``mp.mpf(float(v))`` converts each Python float to its *exact* binary value
    (the same bits the arena verifier reads). ``mp.mpf(repr(v))`` would instead
    parse the shortest round-trip *decimal*, drifting ~0.1 ULP per coordinate —
    fatal for a sub-ULP polisher, since the gate would then certify a
    decimal-rounded copy rather than the configuration actually scored.
    """
    return [[mp.mpf(float(v)) for v in row] for row in np.atleast_2d(arr)]


def dual_gate_accept(
    cand: np.ndarray,
    key: object,
    *,
    cur_f64: float,
    cur_mp: mp.mpf,
    merit_f64: Callable[[np.ndarray], float],
    merit_mp: Callable[[np.ndarray, int], mp.mpf],
    dps: int,
    feasible: Callable[[np.ndarray, object], bool] | None = None,
) -> mp.mpf | None:
    """Decide whether ``cand`` is a trustworthy improvement; return its exact
    merit if accepted, else ``None``.

    ``cur_f64`` / ``cur_mp`` are the current config's float64 / mpmath merits,
    passed in so the caller computes them once per coordinate rather than once
    per candidate. ``key`` identifies the changed coordinate block, letting the
    feasibility predicate check only the constraints that block can affect
    (O(n) instead of O(n²)). All merits are "higher is better".

    The gate, in order (cheap checks first):
      1. feasibility (if a hard constraint exists) must hold for the candidate;
      2. the arena float64 merit must NOT regress (cheap; rejects most moves);
      3. the exact mpmath merit must STRICTLY improve (the trustworthy signal).
    """
    if feasible is not None and not feasible(cand, key):
        return None
    if merit_f64(cand) < cur_f64:
        return None
    m = merit_mp(cand, dps)
    return m if m > cur_mp else None


@dataclass
class PolishInfo:
    """Outcome of one ``ulp_polish`` run."""

    score: float
    start_score: float
    delta: float
    n_accept: int
    sweeps: int
    dps: int


def ulp_polish(
    coords0: np.ndarray,
    *,
    keys: Iterable[object],
    candidates_for: Callable[[np.ndarray, object], Iterable[np.ndarray]],
    merit_f64: Callable[[np.ndarray], float],
    merit_mp: Callable[[np.ndarray, int], mp.mpf],
    report_f64: Callable[[np.ndarray], float],
    feasible: Callable[[np.ndarray, object], bool] | None = None,
    dps: int = 80,
    max_iter: int = 500,
) -> tuple[np.ndarray, PolishInfo]:
    """Dual-gate ulp coordinate descent.

    Each *sweep* iterates over ``keys`` (e.g. point/circle indices). For each
    key, ``candidates_for(coords, key)`` yields full candidate configurations
    that differ from ``coords`` only in that key's block; the best dual-gate-
    accepted candidate (largest exact merit) is applied immediately, so later
    keys in the same sweep see the updated configuration (the float64-active-
    screen idea: only the changed block's constraints can be affected). Sweeps
    repeat until one passes with no accepted move.

    Args:
        coords0: initial configuration, array-like; copied, not mutated.
        keys: the coordinate groups to sweep (re-materialised each sweep).
        candidates_for: ``(coords, key) -> iterable of candidate configs``.
        merit_f64 / merit_mp: "higher is better" objective in float64 / mpmath.
        report_f64: the arena-reported score (start/final) — usually ``merit_f64``
            up to sign, but kept separate so a minimization problem can report
            the un-negated score.
        feasible: optional hard-constraint predicate on a candidate config.
        dps: mpmath precision for ``merit_mp`` and ``to_mp``.
        max_iter: cap on sweeps.

    Returns:
        ``(polished_coords float64, PolishInfo)``.
    """
    mp.mp.dps = dps
    coords = np.array(coords0, dtype=np.float64).copy()
    keys = list(keys)

    start_score = report_f64(coords)
    n_accept = 0
    sweeps = 0

    for sweep in range(max_iter):
        sweeps = sweep + 1
        improved = False
        for key in keys:
            cur_f64 = merit_f64(coords)
            cur_mp = merit_mp(coords, dps)
            best: tuple[mp.mpf, np.ndarray] | None = None
            for cand in candidates_for(coords, key):
                m = dual_gate_accept(
                    cand,
                    key,
                    cur_f64=cur_f64,
                    cur_mp=cur_mp,
                    merit_f64=merit_f64,
                    merit_mp=merit_mp,
                    dps=dps,
                    feasible=feasible,
                )
                if m is not None and (best is None or m > best[0]):
                    best = (m, cand)
            if best is not None:
                coords = best[1]
                n_accept += 1
                improved = True
        if not improved:
            break

    final_score = report_f64(coords)
    info = PolishInfo(
        score=final_score,
        start_score=start_score,
        delta=final_score - start_score,
        n_accept=n_accept,
        sweeps=sweeps,
        dps=dps,
    )
    return coords, info
