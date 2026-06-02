#!/usr/bin/env python3
"""mpmath_ulp_polish.py — dual-gate ULP coordinate descent for P5 (Min Distance Ratio).

Phase 2a: the generic `einstein.ulp_polish` engine wired to P5. The objective is
**minimise (max_pairwise_distance / min_pairwise_distance)²** over 16 points in
2-D (the proven-global Cantrell (22,8) configuration). The engine maximises, so
the merit is the NEGATED ratio: a single-coordinate ulp step is accepted only if
it strictly *decreases* the exact (mpmath) ratio AND does not *increase* the
arena float64 ratio. With 22 pairs pinned at min distance and 8 at max, the
contact graph is rigid, so the honest expectation is ~zero accepts — a
triple-verified confirmation of the float64 ceiling (the basin floor sits
2.35e-11 below arena #1, blocked by minImprovement regardless).

Usage (via dispatch):
    uv run python -m einstein.optimizer_dispatch --problem-id 5 --strategy mpmath_ulp_polish

Usage (standalone):
    uv run python scripts/min_distance_ratio/mpmath_ulp_polish.py --dps 80 --max-iter 30
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import logging
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.min_distance_ratio.evaluator import evaluate  # noqa: E402
from einstein.ulp_polish import ulp_neighbors, ulp_polish  # noqa: E402

N_POINTS = 16
DIMENSION = 2
DEFAULT_SEED = _REPO / "scripts" / "min_distance_ratio" / "seeds" / "best.json"
DEFAULT_OUTPUT = _REPO / "results" / "min_distance_ratio" / "mpmath_ulp_polish_result.json"

log = logging.getLogger("min_distance_ratio_ulp_polish")


def _ratio_sq_mp(coords: np.ndarray, dps: int) -> mp.mpf:
    """Exact (max_dist / min_dist)² from the exact binary float64 values."""
    mp.mp.dps = dps
    pts = [[mp.mpf(float(v)) for v in row] for row in coords]
    n = len(pts)
    mind: mp.mpf | None = None
    maxd: mp.mpf | None = None
    for i in range(n):
        for j in range(i + 1, n):
            d = mp.sqrt(mp.fsum((pts[i][k] - pts[j][k]) ** 2 for k in range(DIMENSION)))
            if mind is None or d < mind:
                mind = d
            if maxd is None or d > maxd:
                maxd = d
    return (maxd / mind) ** 2


def _neg_ratio_mp(coords: np.ndarray, dps: int) -> mp.mpf:
    """Negated exact ratio² — 'higher is better' merit for the engine."""
    return -_ratio_sq_mp(coords, dps)


def _neg_score_f64(coords: np.ndarray) -> float:
    return -evaluate({"vectors": coords})


def mpmath_ulp_polish(
    initial_vectors,
    dps: int = 80,
    max_iter: int = 30,
    steps: tuple[int, ...] = (-2, -1, 1, 2),
) -> tuple[np.ndarray, dict]:
    """Dual-gate ulp descent minimising the exact (max/min)² ratio."""
    coords = np.array(initial_vectors, dtype=np.float64).copy()
    assert coords.shape == (N_POINTS, DIMENSION), f"got {coords.shape}"

    def candidates_for(c: np.ndarray, i: int):
        for axis in range(DIMENSION):
            for v in ulp_neighbors(c[i, axis], steps):
                cand = c.copy()
                cand[i, axis] = v
                yield cand

    polished, info = ulp_polish(
        coords,
        keys=range(N_POINTS),
        candidates_for=candidates_for,
        merit_f64=_neg_score_f64,
        merit_mp=_neg_ratio_mp,
        report_f64=lambda c: evaluate({"vectors": c}),  # report the true (lower-better) score
        feasible=None,
        dps=dps,
        max_iter=max_iter,
    )
    return polished, dataclasses.asdict(info)


def _load_seed(path: Path) -> list[list[float]]:
    if not path.is_file():
        raise FileNotFoundError(f"seed not found at {path}")
    data = json.loads(path.read_text())
    vectors = data.get("vectors") or data
    if not isinstance(vectors, list) or len(vectors) != N_POINTS:
        raise ValueError(f"seed {path} must contain a {N_POINTS}-element vectors list")
    return vectors


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    parser.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dps", type=int, default=80, help="mpmath precision (default 80).")
    parser.add_argument("--max-iter", type=int, default=30, help="full-sweep cap (default 30).")
    args = parser.parse_args(argv)

    vectors = _load_seed(args.seed)
    log.info("loaded warm-start: %d points from %s", len(vectors), args.seed)

    polished, info = mpmath_ulp_polish(vectors, dps=args.dps, max_iter=args.max_iter)
    log.info(
        "ulp polish: start=%.16f final=%.16f delta=%.3e accepts=%d sweeps=%d (dps=%d)",
        info["start_score"],
        info["score"],
        info["delta"],
        info["n_accept"],
        info["sweeps"],
        info["dps"],
    )

    payload = {"vectors": polished.tolist()}
    strict_score = evaluate(payload)
    log.info("arena evaluator score: %.16f", strict_score)
    if abs(strict_score - info["score"]) > 1e-12:
        log.error(
            "score disagreement: ulp=%.16f arena=%.16f — refusing to write (axiom A1)",
            info["score"],
            strict_score,
        )
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({"score": float(strict_score), "payload": payload}, indent=2))
    log.info("wrote %s", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
