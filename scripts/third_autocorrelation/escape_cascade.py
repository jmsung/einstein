"""Goal 5 branch-sampling escape cascade — find a 3rd piecewise-constant basin.

User confirmed: a step-function solution in a DIFFERENT basin reaches C≈1.45220
(~1e-4 below the leader 1.4523043332). Branches diverge only at large n: the
n=400 optimum is shared, but the larger-n escape (block-repeat + noise +
re-optimise) lands in different basins depending on the perturbation. The leader
sampled one branch (→1.45230), we sampled another (→1.45250). This samples MANY
branches from the shared n=400 anchor with varied per-level noise, hunting one
that lands ≤ 1.45220.

Run in background; checkpoints after each run. Triple-verify happens downstream.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import signed_descent, upsample

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4  # 1.4522043... — the real arena record threshold
LEVELS = [800, 1600, 3200, 6400, 12800, 25600, 51200, 100000]
OUT = Path("results/problem-4-third-autocorrelation")
N_RUNS = 20
# per-level noise scale (fraction of std) is sampled from this set each level;
# larger noise lets a run jump to a different branch instead of refining in place.
NOISE_CHOICES = [1e-6, 1e-5, 1e-4, 3e-4, 1e-3, 3e-3]


def betas_for(n: int) -> list[float]:
    if n >= 100000:
        return [1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 1e10]
    if n >= 12800:
        return [1e4, 1e5, 1e6, 1e7, 1e8]
    return [1e4, 3e4, 1e5, 1e6, 1e7]


def block_repeat(v: np.ndarray, n: int) -> np.ndarray:
    """Exact block-repeat upsample (preserves score) when n is a multiple."""
    if n % len(v) == 0:
        return np.repeat(v, n // len(v))
    return upsample(v, n)


def make_anchor() -> np.ndarray:
    """Shared n=400 anchor: leader downsampled to 400 then polished (~1.45404)."""
    lead = np.array(json.load(open(LEADER))["values"], float)
    blk = len(lead) // 400
    seed = lead[: blk * 400].reshape(400, blk).mean(axis=1)
    v, c = signed_descent(seed, [1e4, 1e5, 1e6, 1e7, 1e8], 800, 0.8, 0.0, 0.0)
    print(f"anchor n=400: C={c:.10f}", flush=True)
    return v


def run_branch(anchor: np.ndarray, seed: int) -> tuple[np.ndarray, float, list]:
    rng = np.random.default_rng(seed)
    v = anchor.copy()
    trace = []
    for n in LEVELS:
        v = block_repeat(v, n)
        scale = float(rng.choice(NOISE_CHOICES))
        v = v + rng.normal(scale=scale * v.std(), size=n)
        v, c = signed_descent(v, betas_for(n), 600 if n < 100000 else 900, 0.8, 0.0, 0.0)
        trace.append({"n": n, "scale": scale, "C": c})
    return v, c, trace


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    anchor = make_anchor()
    best = {"C": 1e9, "v": None, "seed": -1}
    rows = []
    for r in range(N_RUNS):
        t0 = time.time()
        v, c, trace = run_branch(anchor, 5000 + r)
        dt = time.time() - t0
        beats = bool(c < TARGET)
        rows.append(
            {
                "run": r,
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
            f"[{r + 1}/{N_RUNS}] C_100k={c:.13f}{flag} neg={(v < 0).mean() * 100:.1f}% ({dt:.0f}s)",
            flush=True,
        )
        if c < best["C"]:
            best = {"C": c, "v": v.copy(), "seed": 5000 + r}
            with open(OUT / "cascade_best.json", "w") as fh:
                json.dump(
                    {
                        "values": best["v"].tolist(),
                        "score": best["C"],
                        "n": 100000,
                        "seed": best["seed"],
                    },
                    fh,
                )
        with open(OUT / "cascade_summary.json", "w") as fh:
            json.dump(
                {
                    "leader": LEADER_C,
                    "target": TARGET,
                    "best_C": best["C"],
                    "best_seed": best["seed"],
                    "rows": rows,
                },
                fh,
                indent=2,
            )
    print(f"\nBEST C_100k = {best['C']:.13f}  leader {LEADER_C:.13f}  target {TARGET:.13f}")
    print(
        "RECORD CANDIDATE — triple-verify next."
        if best["C"] < TARGET
        else (
            "beats leader (sub-1e-4)"
            if best["C"] < LEADER_C - 1e-8
            else "no branch beat the leader"
        )
    )


if __name__ == "__main__":
    main()
