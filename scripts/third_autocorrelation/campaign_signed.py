"""Goal 2 signed-search campaign for P4 — the decisive nudge experiment.

Question (ask-the-question-first): does forcing the negative fraction past the
leader's 27.5% (via the annealed nudge) discover a basin with C below the leader
1.4523043331832, or does the configuration relax back to the leader's floor?

Sweeps neg_target × detail_scale at n=100000 warm-started from the leader's full
structure, full β-cascade. Saves every result to results/ and the best to a
campaign summary. Designed to run in the background; checkpoints after each cell.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import (
    lowpass_envelope,
    signed_descent,
    upsample,
)

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
LEADER_C = 1.4523043331832
N = 100000
BETAS = [1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9]
ITERS = 400
OUT = Path("results/problem-4-third-autocorrelation")

# (neg_target, detail_scale) cells. neg_target=0 → pure polish control.
CELLS = [
    (0.00, 0.002),  # control: tiny perturbation, no nudge → expect ~leader floor
    (0.30, 0.005),
    (0.32, 0.010),
    (0.35, 0.020),
    (0.40, 0.030),
]
NEG_WEIGHT = 3.0


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with open(LEADER) as fh:
        lead = np.array(json.load(fh)["values"], dtype=np.float64)
    if len(lead) != N:
        lead = upsample(lead, N)
    env = lowpass_envelope(lead, keep=60000)  # ≈ full leader structure

    summary = []
    best_c, best_path = float("inf"), None
    for i, (nt, ds) in enumerate(CELLS):
        rng = np.random.default_rng(100 + i)
        init_v = env + rng.normal(scale=ds * np.abs(env).mean(), size=N)
        t0 = time.time()
        nw = 0.0 if nt == 0.0 else NEG_WEIGHT
        v, c = signed_descent(init_v, BETAS, ITERS, lr=0.8, neg_target=nt, neg_base=nw)
        frac = float((v < 0).mean())
        dt = time.time() - t0
        path = OUT / f"signed_nt{nt:.2f}_ds{ds:.3f}.json"
        with open(path, "w") as fh:
            json.dump(
                {
                    "values": v.tolist(),
                    "score": c,
                    "n": N,
                    "neg_target": nt,
                    "detail_scale": ds,
                    "neg_frac": frac,
                },
                fh,
            )
        row = {
            "neg_target": nt,
            "detail_scale": ds,
            "C": c,
            "neg_frac": frac,
            "beats_leader": bool(c < LEADER_C - 1e-8),
            "secs": round(dt, 1),
        }
        summary.append(row)
        print(
            f"[{i + 1}/{len(CELLS)}] nt={nt:.2f} ds={ds:.3f} "
            f"C={c:.13f} neg={frac * 100:.2f}% beats={row['beats_leader']} ({dt:.0f}s)",
            flush=True,
        )
        if c < best_c:
            best_c, best_path = c, str(path)
        with open(OUT / "campaign_summary.json", "w") as fh:
            json.dump(
                {"leader": LEADER_C, "best_C": best_c, "best_path": best_path, "rows": summary},
                fh,
                indent=2,
            )

    print(f"\nBEST C = {best_c:.13f}  (leader {LEADER_C:.13f})")
    print("BEATS LEADER" if best_c < LEADER_C - 1e-8 else "does NOT beat leader")
    print(f"best file: {best_path}")


if __name__ == "__main__":
    main()
