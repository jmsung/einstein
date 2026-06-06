"""Goal 5 diverse-seed escape search — hunt for a basin better than the leader's.

The leader's basin limits to C≈1.45230; ours to ≈1.45250. Distinct sign-structure
basins have distinct continuous limits, so a record (C ≤ 1.4522043, the 1e-4 arena
threshold below the leader) requires a THIRD, better basin — not polishing the
leader. This screens many diverse signed seeds at n=3200 (the larger-n escape
regime) with a strong smooth-max cascade. Diagnostic: the leader family scores
≈1.4530065 at n=3200; any seed whose n=3200 optimum is meaningfully below that is
a candidate better basin worth lifting to n=100000.

Run in background; checkpoints after each seed. Prints basins sorted at the end.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import (
    both_sign_fourier_init,
    signed_descent,
    upsample,
)

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
OURS = Path(
    ".mb/problems/4-third-autocorrelation/solutions/solution-feat-third-autocorrelation-1.4525211550469.json"
)
N = 3200
N100K_REF = 1.4530065851775  # leader-family score at n=3200 (progression table)
BETAS = [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 1e8]
ITERS = 600
OUT = Path("results/problem-4-third-autocorrelation")
N_SEEDS = 48


def downsample(v: np.ndarray, n: int) -> np.ndarray:
    blk = len(v) // n
    return v[: blk * n].reshape(n, blk).mean(axis=1)


def make_seed(kind: str, idx: int) -> np.ndarray:
    """Diverse signed seed families. Variety in SIGN STRUCTURE is the point."""
    rng = np.random.default_rng(7000 + idx)
    t = np.linspace(0.0, np.pi, N)
    if kind == "fourier":
        return both_sign_fourier_init(
            N, n_modes=rng.integers(10, 120), neg_bias=rng.uniform(0.2, 0.7), rng=rng
        )
    if kind == "sign-block":
        # smooth positive envelope × random sign blocks of random width
        env = np.abs(np.cos(rng.uniform(0.5, 3.0) * t)) + 0.3
        sign = np.ones(N)
        i = 0
        while i < N:
            w = rng.integers(20, 400)
            if rng.random() < 0.35:
                sign[i : i + w] = -1.0
            i += w
        return env * sign + 0.1
    if kind == "chirp":
        freq = np.linspace(rng.uniform(1, 5), rng.uniform(20, 120), N)
        return np.cos(np.cumsum(freq) * np.pi / N) + rng.uniform(0.1, 0.6)
    if kind == "leader-flip":
        v = downsample(np.array(json.load(open(LEADER))["values"], float), N)
        # structurally perturb: flip sign of several random contiguous blocks
        for _ in range(rng.integers(2, 8)):
            a = rng.integers(0, N - 1)
            b = min(N, a + rng.integers(50, 600))
            v[a:b] *= -1.0
        return v + rng.normal(scale=0.05 * v.std(), size=N)
    if kind == "ours-flip":
        v = downsample(np.array(json.load(open(OURS))["values"], float), N)
        for _ in range(rng.integers(2, 8)):
            a = rng.integers(0, N - 1)
            b = min(N, a + rng.integers(50, 600))
            v[a:b] *= -1.0
        return v + rng.normal(scale=0.05 * v.std(), size=N)
    raise ValueError(kind)


KINDS = ["fourier", "sign-block", "chirp", "leader-flip", "ours-flip"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    best = {"C": 1e9, "v": None, "kind": None, "seed": -1}
    for i in range(N_SEEDS):
        kind = KINDS[i % len(KINDS)]
        seed = make_seed(kind, i)
        t0 = time.time()
        v, c = signed_descent(seed, BETAS, ITERS, lr=0.8, neg_target=0.0, neg_base=0.0)
        dt = time.time() - t0
        below = bool(c < N100K_REF - 1e-6)
        rows.append(
            {
                "seed": i,
                "kind": kind,
                "C_n3200": c,
                "below_leader_family": below,
                "neg_frac": float((v < 0).mean()),
                "secs": round(dt, 1),
            }
        )
        flag = "  <-- BELOW LEADER FAMILY" if below else ""
        print(f"[{i + 1}/{N_SEEDS}] {kind:11s} C={c:.10f}{flag} ({dt:.0f}s)", flush=True)
        if c < best["C"]:
            best = {"C": c, "v": v.copy(), "kind": kind, "seed": i}
        rows_sorted = sorted(rows, key=lambda r: r["C_n3200"])
        with open(OUT / "escape_summary.json", "w") as fh:
            json.dump(
                {
                    "n": N,
                    "leader_family_n3200": N100K_REF,
                    "best": {k: best[k] for k in ("C", "kind", "seed")},
                    "rows_sorted": rows_sorted,
                },
                fh,
                indent=2,
            )
        if best["v"] is not None:
            with open(OUT / "escape_best_n3200.json", "w") as fh:
                json.dump(
                    {
                        "values": best["v"].tolist(),
                        "score": best["C"],
                        "n": N,
                        "kind": best["kind"],
                    },
                    fh,
                )

    print(
        f"\nBest n=3200 basin: C={best['C']:.10f} ({best['kind']}) vs leader-family {N100K_REF:.10f}"
    )
    if best["C"] < N100K_REF - 1e-6:
        print("FOUND A BETTER BASIN at n=3200 — lift to n=100000 next.")
    else:
        print("No basin beats the leader family at n=3200.")
    # also lift the best to 100k as a quick check (block-repeat + polish)
    v100 = upsample(best["v"], 100000)
    v100p, c100 = signed_descent(v100, [1e6, 1e7, 1e8, 1e9, 1e10], 800, 0.8, 0.0, 0.0)
    print(f"lifted best to n=100000: C={c100:.13f} (leader 1.4523043331832, target 1.4522043)")
    with open(OUT / "escape_best_n100k.json", "w") as fh:
        json.dump({"values": v100p.tolist(), "score": c100, "n": 100000}, fh)


if __name__ == "__main__":
    main()
