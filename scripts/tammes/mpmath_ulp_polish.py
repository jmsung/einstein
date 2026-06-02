#!/usr/bin/env python3
"""mpmath_ulp_polish.py — dual-gate ULP coordinate descent for P11 (Tammes n=50).

Phase 2a: the generic `einstein.ulp_polish` engine wired to the Tammes
objective. P11 **maximises the minimum pairwise distance** of 50 points on S²
(the arena normalises each point to the unit sphere before scoring). Unlike the
packing problems there is no hard disjointness constraint — the score *is* a min
over 1225 pair distances, so the dual gate runs on the OBJECTIVE itself: a
single-coordinate ulp step is accepted only if it strictly increases the exact
(mpmath, normalised) min distance AND does not decrease the arena float64 min
distance. At a jammed contact-graph optimum almost every ulp move shrinks some
active pair, so the expected — and honest — outcome is ~zero accepts: a
triple-verified confirmation that the seed already sits at its float64 ceiling
(see docs/wiki/concepts/float64-ceiling.md).

Usage (via dispatch):
    uv run python -m einstein.optimizer_dispatch --problem-id 11 --strategy mpmath_ulp_polish

Usage (standalone):
    uv run python scripts/tammes/mpmath_ulp_polish.py --dps 80 --max-iter 30
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

from einstein.tammes.evaluator import DIMENSION, N_VECTORS, evaluate  # noqa: E402
from einstein.ulp_polish import ulp_neighbors, ulp_polish  # noqa: E402

DEFAULT_SEED = _REPO / "scripts" / "tammes" / "seeds" / "best.json"
DEFAULT_OUTPUT = _REPO / "results" / "tammes" / "mpmath_ulp_polish_result.json"

log = logging.getLogger("tammes_ulp_polish")


def _min_dist_mp(coords: np.ndarray, dps: int) -> mp.mpf:
    """Exact min pairwise distance after unit-normalising each row at ``dps``.

    Mirrors ``evaluator.evaluate`` (normalise then min Euclidean distance), but
    in mpmath from the exact binary float64 values — the trustworthy objective
    the dual gate ranks by.
    """
    mp.mp.dps = dps
    floor = mp.mpf(10) ** -12
    rows: list[list[mp.mpf]] = []
    for row in coords:
        vals = [mp.mpf(float(v)) for v in row]
        norm = mp.sqrt(mp.fsum(v * v for v in vals))
        if norm < floor:
            norm = floor
        rows.append([v / norm for v in vals])
    best: mp.mpf | None = None
    n = len(rows)
    for i in range(n):
        for j in range(i + 1, n):
            d = mp.sqrt(mp.fsum((rows[i][k] - rows[j][k]) ** 2 for k in range(DIMENSION)))
            if best is None or d < best:
                best = d
    return best


def _score_f64(coords: np.ndarray) -> float:
    return evaluate({"vectors": coords})


def mpmath_ulp_polish(
    initial_vectors,
    dps: int = 80,
    max_iter: int = 30,
    steps: tuple[int, ...] = (-2, -1, 1, 2),
) -> tuple[np.ndarray, dict]:
    """Dual-gate ulp descent maximising the exact min pairwise distance."""
    coords = np.array(initial_vectors, dtype=np.float64).copy()
    assert coords.shape == (N_VECTORS, DIMENSION), f"got {coords.shape}"

    def candidates_for(c: np.ndarray, i: int):
        for axis in range(DIMENSION):
            for v in ulp_neighbors(c[i, axis], steps):
                cand = c.copy()
                cand[i, axis] = v
                yield cand

    polished, info = ulp_polish(
        coords,
        keys=range(N_VECTORS),
        candidates_for=candidates_for,
        merit_f64=_score_f64,  # maximise min distance (higher is better)
        merit_mp=_min_dist_mp,
        report_f64=_score_f64,
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
    if not isinstance(vectors, list) or len(vectors) != N_VECTORS:
        raise ValueError(f"seed {path} must contain a {N_VECTORS}-element vectors list")
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
    log.info("loaded warm-start: %d vectors from %s", len(vectors), args.seed)

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

    # Triple-verify shoulder: the arena float64 evaluator must agree.
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
