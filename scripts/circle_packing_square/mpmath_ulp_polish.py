#!/usr/bin/env python3
"""mpmath_ulp_polish.py — ULP-step coordinate descent for P14 (Circle Packing, n=26).

The body the autosynthesis loop has been asking for (cycles 49–51): the
`mpmath-ulp-polish` technique exists in `docs/wiki/techniques/mpmath-ulp-polish.md`
and the skill-library, but had no script for problem 14. This is it.

What it does (per the technique spec)
-------------------------------------
After float64 SLSQP saturates at the basin floor (`slsqp_polish`), every gain
left sits *below* the float64 line-search noise floor. The move that still
works at that scale is **discrete ±1/±2 ulp coordinate descent**, with mpmath
(dps ≥ 50) used only to *evaluate* candidate moves so we never trust a float64
rounding artifact.

P14 is **maximize Σ rᵢ** s.t. strict-disjoint (`‖cᵢ−cⱼ‖ ≥ rᵢ+rⱼ`) and
inside-square. Unlike the P6 overlap-minimisation case, the productive ulp move
here is a **2-coordinate move**: nudge a circle's centre toward where exact
arithmetic shows it has room, then grow its radius by a ulp. A pure radius
bump only lands when float64 rounding left a circle with exact slack its
binding constraints hid — rare at a jammed optimum, so we sweep both.

A move (a ulp bump that *grows* a radius, optionally with a centre nudge) is
accepted iff circle ``i``'s constraints stay feasible under BOTH:
  1. the arena's float64 strict check (tol=0) — the leaderboard ground truth, and
  2. mpmath-exact at `--dps` (gap ≥ 0) — so we never bank a float64 rounding
     artifact (the 2026-04-09 false-breakthrough trap; axiom A1).
Because every proposed move only ever *increases* a radius, any feasible move
strictly increases exact Σ rᵢ — so feasibility (not a float64-sum tick, which a
single radius ulp ~1e-17 sits below) is the accept gate. The float64 score is
reported at the end.

Because only circle ``i`` changes per candidate, only ``i``'s constraints
(its 4 walls + 25 pairs) need re-evaluation — the rest were feasible and are
untouched. That's the float64-active-screen idea applied per-circle: O(n) work
per candidate instead of O(n²).

Usage (via dispatch):
    uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy mpmath_ulp_polish

Usage (standalone):
    uv run python scripts/circle_packing_square/mpmath_ulp_polish.py --dps 80 --max-iter 500
"""

from __future__ import annotations

import argparse
import json
import logging
import struct
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

# Make src/einstein importable when invoked as a script (cwd=repo root).
_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.circle_packing_square.evaluator import (  # noqa: E402
    N_CIRCLES,
    SQUARE_SIDE,
    evaluate_strict,
)

DEFAULT_SEED = _REPO / "scripts" / "circle_packing_square" / "seeds" / "p14_canonical.json"
DEFAULT_OUTPUT = _REPO / "results" / "circle_packing_square" / "mpmath_ulp_polish_result.json"

log = logging.getLogger("mpmath_ulp_polish")


def ulp_neighbors(x: float, steps: tuple[int, ...] = (-2, -1, 1, 2)) -> list[float]:
    """Return the float64 values ``steps`` ulps away from ``x``.

    Bit-level integer arithmetic on the IEEE-754 representation — NOT
    multiplicative scaling. ``x * (1 + 1e-16)`` is not 1 ulp (lesson from
    the technique page). Handles the sign boundary correctly because the
    int64 reinterpretation of float64 is monotone for x ≥ 0 and we only
    ever deal with coordinates in [0, 1].
    """
    bits = struct.unpack("<q", struct.pack("<d", x))[0]
    out = []
    for s in steps:
        nb = bits + s
        out.append(struct.unpack("<d", struct.pack("<q", nb))[0])
    return out


def _to_mp(circles: np.ndarray) -> list[list[mp.mpf]]:
    """Exact-precision copy of the configuration (current dps)."""
    return [[mp.mpf(repr(float(v))) for v in row] for row in circles]


def _circle_gap_min(mpc: list[list[mp.mpf]], i: int) -> mp.mpf:
    """Minimum constraint gap over every constraint that touches circle ``i``.

    Returns ``min`` over: the 4 wall slacks of ``i`` and the pair slacks
    ``‖cᵢ−cⱼ‖ − rᵢ − rⱼ`` for all ``j ≠ i``. ≥ 0 ⇒ circle ``i`` is feasible.
    Evaluated in mpmath at the active dps.
    """
    cx, cy, r = mpc[i]
    side = mp.mpf(SQUARE_SIDE)
    gaps = [cx - r, side - cx - r, cy - r, side - cy - r]
    for j in range(len(mpc)):
        if j == i:
            continue
        dx = cx - mpc[j][0]
        dy = cy - mpc[j][1]
        gaps.append(mp.sqrt(dx * dx + dy * dy) - r - mpc[j][2])
    return min(gaps)


def _float64_circle_feasible(circles: np.ndarray, i: int) -> bool:
    """Arena-matching float64 strict check (tol=0) for circle ``i``'s constraints.

    Mirrors ``evaluator.verify_circles_disjoint`` / ``verify_inside_square`` at
    tol=0 — ``center_distance < radii_sum`` (in float64) is an overlap; any wall
    slack < 0 is outside. This is the ground-truth gate: the arena runs exactly
    this float64 arithmetic, so a candidate must pass it to be a real score.
    """
    cx, cy, r = circles[i]
    if r < 0:
        return False
    # walls (tol=0)
    if min(cx - r, SQUARE_SIDE - (cx + r), cy - r, SQUARE_SIDE - (cy + r)) < 0:
        return False
    # pairs (tol=0): center_distance < radii_sum ⇒ overlap
    for j in range(circles.shape[0]):
        if j == i:
            continue
        d = np.sqrt((cx - circles[j, 0]) ** 2 + (cy - circles[j, 1]) ** 2)
        if d < r + circles[j, 2]:
            return False
    return True


def _sum_r(circles: np.ndarray) -> float:
    """float64 Σ rᵢ — the arena score."""
    return float(np.sum(circles[:, 2]))


def mpmath_ulp_polish(
    initial_circles,
    dps: int = 80,
    max_iter: int = 500,
    steps: tuple[int, ...] = (1, 2),
    center_steps: tuple[int, ...] = (-2, -1, 1, 2),
) -> tuple[np.ndarray, dict]:
    """ULP coordinate descent maximising Σ rᵢ with mpmath-exact feasibility.

    Args:
        initial_circles: (26, 3) array-like of [cx, cy, r].
        dps: mpmath decimal precision for the feasibility evaluator.
        max_iter: cap on full sweeps (each sweep = 1-coord pass + 2-coord pass).
        steps: ulp deltas to try when *growing* a radius (positive only).
        center_steps: ulp deltas to try when nudging a centre coordinate.

    Returns:
        (polished_circles (26,3) float64, info dict).
    """
    mp.mp.dps = dps
    circles = np.array(initial_circles, dtype=np.float64).copy()
    assert circles.shape == (N_CIRCLES, 3), f"got {circles.shape}"

    start_score = _sum_r(circles)
    n_accept = 0
    sweeps = 0

    def feasible_after(i: int, cand: tuple[float, float, float]) -> bool:
        # A move is safe iff circle i's constraints hold in BOTH:
        #   (a) the arena's float64 strict check (tol=0) — the ground truth the
        #       leaderboard verifier actually runs, and
        #   (b) mpmath-exact at the active dps — so we never bank a gain that is
        #       only a float64 rounding artifact (the 2026-04-09 false-breakthrough
        #       500-pt trap; axiom A1).
        # Both required: float64-feasible-but-exact-overlapping is the exploit we
        # reject; exact-feasible-but-float64-overlapping is rejected by the arena.
        saved = circles[i].copy()
        circles[i] = cand
        ok = _float64_circle_feasible(circles, i) and (_circle_gap_min(_to_mp(circles), i) >= 0)
        circles[i] = saved
        return ok

    for sweep in range(max_iter):
        sweeps = sweep + 1
        improved = False

        # Score (= Σ rᵢ) depends only on radii, and we only ever propose a
        # *larger* radius, so any feasible candidate strictly increases exact
        # Σ rᵢ. We therefore rank feasible candidates by largest radius (most
        # growth) and accept the best — NOT by whether the float64 *sum* ticked
        # up, because a single radius ulp (~1e-17) is far below the sum's ulp
        # (~4e-16) and would be spuriously rejected until it happened to
        # accumulate past a sum-ulp boundary. The float64 score is reported at
        # the end; the descent itself works in radius-space.

        # ---- 1-coord pass: pure radius growth (lands only on exact slack) ----
        for i in range(N_CIRCLES):
            cx, cy, r = circles[i]
            best = None  # (r_new, cand)
            for r_new in ulp_neighbors(r, steps):
                if r_new <= r:
                    continue
                cand = (cx, cy, r_new)
                if feasible_after(i, cand) and (best is None or r_new > best[0]):
                    best = (r_new, cand)
            if best is not None:
                circles[i] = best[1]
                n_accept += 1
                improved = True

        # ---- 2-coord pass: centre nudge + radius growth ----
        for i in range(N_CIRCLES):
            cx0, cy0, r0 = circles[i]
            best = None  # (r_new, cand)
            for axis in (0, 1):  # cx, then cy
                c_base = (cx0, cy0)[axis]
                for c_new in ulp_neighbors(c_base, center_steps):
                    for r_new in ulp_neighbors(r0, steps):
                        if r_new <= r0:
                            continue
                        cand = (c_new, cy0, r_new) if axis == 0 else (cx0, c_new, r_new)
                        if feasible_after(i, cand) and (best is None or r_new > best[0]):
                            best = (r_new, cand)
            if best is not None:
                circles[i] = best[1]
                n_accept += 1
                improved = True

        if not improved:
            break

    final_score = _sum_r(circles)
    info = {
        "score": final_score,
        "start_score": start_score,
        "delta": final_score - start_score,
        "n_accept": n_accept,
        "sweeps": sweeps,
        "dps": dps,
    }
    return circles, info


def _load_seed(path: Path) -> list[list[float]]:
    if not path.is_file():
        raise FileNotFoundError(
            f"warm-start seed not found at {path}. The seed lives in-repo at "
            f"`scripts/circle_packing_square/seeds/p14_canonical.json`."
        )
    data = json.loads(path.read_text())
    circles = data.get("circles") or data
    if not isinstance(circles, list) or len(circles) != N_CIRCLES:
        raise ValueError(
            f"seed {path} must contain a {N_CIRCLES}-element circles list, got "
            f"{type(circles).__name__} of length "
            f"{len(circles) if hasattr(circles, '__len__') else '?'}"
        )
    return circles


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dps", type=int, default=80, help="mpmath precision (default 80).")
    parser.add_argument("--max-iter", type=int, default=500, help="full-sweep cap (default 500).")
    args = parser.parse_args(argv)

    circles = _load_seed(args.seed)
    log.info("loaded warm-start: %d circles from %s", len(circles), args.seed)

    polished, info = mpmath_ulp_polish(circles, dps=args.dps, max_iter=args.max_iter)
    log.info(
        "ulp polish: start=%.16f final=%.16f delta=%.3e accepts=%d sweeps=%d (dps=%d)",
        info["start_score"],
        info["score"],
        info["delta"],
        info["n_accept"],
        info["sweeps"],
        info["dps"],
    )

    # Triple-verify shoulder: the arena (float64, tol=0) must agree the polished
    # config is strict-disjoint and report the same score. evaluate_strict raises
    # on any overlap/wall violation.
    payload = {"circles": polished.tolist()}
    strict_score = evaluate_strict(payload)
    log.info("strict evaluator score: %.16f", strict_score)
    if abs(strict_score - info["score"]) > 1e-12:
        log.warning(
            "score disagreement: ulp=%.16f strict=%.16f — NOT trustworthy (axiom A1)",
            info["score"],
            strict_score,
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"score": float(strict_score), "payload": payload}, indent=2))
    log.info("wrote %s", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
