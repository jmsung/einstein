"""Goal 5 — two-sided signed LP–Frank–Wolfe (the published MV/AlphaEvolve method).

Web research (no public value < 1.4523; method unpublished) points to the
Kolountzakis–Matolcsi LP fixed-point as the record-producing algorithm — but our
prior LP was ONE-SIDED (conv ≤ M) seeded from the leader. The published recipe
uses the TWO-SIDED signed polytope (−M ≤ conv ≤ M) with a proper Frank–Wolfe
line search, and scales by GRID-REFINEMENT (split each cell into k and re-solve).
That is a different active-set geometry and is untried here.

  maximize Σg s.t. −M ≤ (f★g)_k ≤ M ∀k   (g free/signed; M=current |peak|)
  → renormalise g, line-search t on exact C of (1−t)f + t·g, iterate to fixed pt.
  → refine: split each cell into k copies (value-preserving), re-solve at larger n.

Seeds: n=400 SOTA, ours-downsampled, and cold. Triple-verify; target 1.4522043.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from einstein.third_autocorrelation.optimizer import _conv_matrix, arena_c

SOL = Path(".mb/problems/4-third-autocorrelation/solutions")
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
OUT = Path("results/problem-4-third-autocorrelation")
REFINE_LEVELS = [200, 400, 800, 1600]  # grid-refinement ladder (LP cost ~ n^3)


def two_sided_step(f):
    """One signed two-sided LP step → improved f (or f unchanged at fixed point)."""
    n = len(f)
    A = _conv_matrix(f)  # (2n-1, n): (A g)_k = (f★g)_k
    m = float(np.abs(np.convolve(f, f, mode="full")).max())
    # two-sided: A g ≤ m·1  AND  −A g ≤ m·1
    A_ub = np.vstack([A, -A])
    b_ub = np.full(2 * (2 * n - 1), m)
    res = linprog(c=-np.ones(n), A_ub=A_ub, b_ub=b_ub, bounds=[(None, None)] * n, method="highs")
    if not res.success or res.x.sum() <= 0:
        return f, arena_c(f), False
    g = res.x * (f.sum() / res.x.sum())  # renormalise Σg = Σf
    best_c, best_h = arena_c(f), f
    improved = False
    for t in np.linspace(0.02, 1.0, 30):
        h = (1 - t) * f + t * g
        if h.sum() <= 0:
            continue
        c = arena_c(h)
        if c < best_c - 1e-13:
            best_c, best_h, improved = c, h, True
    return best_h, best_c, improved


def lp_fw(f, max_iter=30):
    c = arena_c(f)
    for _ in range(max_iter):
        f, c, improved = two_sided_step(f)
        if not improved:
            break
    return f, c


def refine(v, n):
    """Grid-refine: value-preserving split of each cell to length n."""
    if n % len(v) == 0:
        return np.repeat(v, n // len(v))
    return np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(v)), v)


def seeds(n0):
    out = {}
    lead = np.array(
        json.load(open(SOL / "sol-organon-rank1-p4-1.4523043332.json"))["values"], float
    )
    ours = np.array(
        json.load(open(SOL / "solution-feat-third-autocorrelation-1.4525211550469.json"))["values"],
        float,
    )
    sota = np.array(json.load(open(SOL / "rank01_DarwinAgent8427_n400.json"))["values"], float)
    out["sota400"] = refine(sota, n0)
    out["leader_ds"] = lead[: (len(lead) // n0) * n0].reshape(n0, -1).mean(1)
    out["ours_ds"] = ours[: (len(ours) // n0) * n0].reshape(n0, -1).mean(1)
    rng = np.random.default_rng(0)
    out["cold"] = rng.normal(0.3, 1.0, n0)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    n0 = REFINE_LEVELS[0]
    best = {"C": 1e9, "v": None, "seed": None}
    rows = []
    for name, v in seeds(n0).items():
        if v.sum() <= 0:
            v = v - v.min() + 0.1
        t0 = time.time()
        # LP-FW with grid-refinement up the ladder
        for n in REFINE_LEVELS:
            v = refine(v, n)
            v, c = lp_fw(v, max_iter=25)
        dt = time.time() - t0
        rows.append({"seed": name, "C": c, "n": REFINE_LEVELS[-1], "neg": float((v < 0).mean())})
        flag = "  << beats leader" if c < LEADER_C - 1e-8 else ""
        print(
            f"  seed={name:10s}: C={c:.13f} (n={REFINE_LEVELS[-1]}) neg={(v < 0).mean() * 100:.1f}%{flag} ({dt:.0f}s)",
            flush=True,
        )
        if c < best["C"]:
            best = {"C": c, "v": v.copy(), "seed": name}
            json.dump(
                {"values": v.tolist(), "score": c, "n": len(v), "seed": name},
                open(OUT / "lpfw_best.json", "w"),
            )
        json.dump(
            {"leader": LEADER_C, "target": TARGET, "best_C": best["C"], "rows": rows},
            open(OUT / "lpfw_summary.json", "w"),
            indent=2,
        )
    print(
        f"\nBEST (n={REFINE_LEVELS[-1]}) C={best['C']:.13f} seed={best['seed']}  leader {LEADER_C:.13f}"
    )
    print(
        "Note: LP-FW is moderate-n only (LP ~ n^3); lift the best basin to 100k via escape_from_seed if it beats our basin here."
    )


if __name__ == "__main__":
    main()
