"""Goal 5 negative-content-GUIDED escape — bias basin selection during the escape.

Across NATURALLY-found basins, more negative content gives lower C (n=400 anchor
20.2%→1.45404, ours 23.6%→1.45250, leader 27.5%→1.45230). Goal 2's "more neg =
worse" only held when FORCING neg content inside the leader's already-converged
n=100k basin. Here we instead apply a gentle neg-content nudge during the ESCAPE
itself (the basin-selection phase, n=800→25600), annealed OFF by n=100000, to
steer the escape toward a higher-neg (~28–36%) basin than the leader's 27.5% —
hoping its continuous limit dips to the 1.4522043 record threshold.

Run in background; checkpoints after each run.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import arena_c, signed_descent, upsample

ANCHOR_N400 = Path(
    ".mb/problems/4-third-autocorrelation/solutions/rank01_DarwinAgent8427_n400.json"
)
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
LEVELS = [800, 1600, 3200, 6400, 12800, 25600, 51200, 100000]
OUT = Path("results/problem-4-third-autocorrelation")
# per-run negative-content target applied during the escape (off at n=100k).
NEG_TARGETS = [0.28, 0.30, 0.32, 0.34, 0.36, 0.40]
NEG_WEIGHT = 1.5  # gentle — guide, don't force


def betas_for(n: int) -> list[float]:
    if n >= 100000:
        return [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 1e10]
    return [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7]


def block_repeat(v: np.ndarray, n: int) -> np.ndarray:
    if n % len(v) == 0:
        return np.repeat(v, n // len(v))
    return upsample(v, n)


def run_branch(anchor: np.ndarray, neg_target: float, seed: int):
    rng = np.random.default_rng(seed)
    v = anchor.copy()
    trace = []
    for n in LEVELS:
        v = block_repeat(v, n)
        v = v + rng.normal(scale=1e-6 * v.std(), size=n)
        # guide toward neg_target during the escape; pure objective at the final n
        nb = 0.0 if n >= 100000 else NEG_WEIGHT
        nt = 0.0 if n >= 100000 else neg_target
        v, c = signed_descent(v, betas_for(n), 1000 if n < 100000 else 1500, 0.8, nt, nb)
        trace.append({"n": n, "C": c, "neg": float((v < 0).mean())})
    return v, c, trace


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    anchor = np.array(json.load(open(ANCHOR_N400))["values"], float)
    print(f"anchor n=400 (SOTA): C={arena_c(anchor):.10f}", flush=True)
    best = {"C": 1e9, "v": None, "neg_target": None}
    rows = []
    for i, nt in enumerate(NEG_TARGETS):
        t0 = time.time()
        v, c, trace = run_branch(anchor, nt, 6000 + i)
        dt = time.time() - t0
        beats = bool(c < TARGET)
        rows.append(
            {
                "neg_target": nt,
                "C_100k": c,
                "neg_frac": float((v < 0).mean()),
                "beats_target": beats,
                "secs": round(dt, 1),
                "trace": trace,
            }
        )
        flag = (
            "  *** BEATS TARGET ***" if beats else ("  (< leader)" if c < LEADER_C - 1e-8 else "")
        )
        print(
            f"[{i + 1}/{len(NEG_TARGETS)}] neg_target={nt:.2f} C_100k={c:.13f}{flag} "
            f"neg={(v < 0).mean() * 100:.1f}% ({dt:.0f}s)",
            flush=True,
        )
        if c < best["C"]:
            best = {"C": c, "v": v.copy(), "neg_target": nt}
            with open(OUT / "negguided_best.json", "w") as fh:
                json.dump(
                    {
                        "values": best["v"].tolist(),
                        "score": best["C"],
                        "n": 100000,
                        "neg_target": nt,
                    },
                    fh,
                )
        with open(OUT / "negguided_summary.json", "w") as fh:
            json.dump(
                {
                    "leader": LEADER_C,
                    "target": TARGET,
                    "best_C": best["C"],
                    "best_neg_target": best["neg_target"],
                    "rows": rows,
                },
                fh,
                indent=2,
            )
    print(f"\nBEST C_100k = {best['C']:.13f}  leader {LEADER_C:.13f}  target {TARGET:.13f}")


if __name__ == "__main__":
    main()
