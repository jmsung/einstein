"""Goal 5 basin-hopping from the leader at n=100000 — escape the floor.

Goal 2 only nudged within the leader's basin (and away from its optimum). This
does the real escape test: perturb the leader at increasing scales, re-polish
with the FULL strong β-cascade (→1e10, long iters, no nudge), keep the global
best. If any restart lands strictly below 1.4523043332 − 1e-8, save it.

Run in background; checkpoints after every restart.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import signed_descent

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
LEADER_C = 1.4523043331832
BETAS = [1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 1e10]
ITERS = 1200
OUT = Path("results/problem-4-third-autocorrelation")
N_RESTARTS = 24
# perturbation scales (fraction of f's std), cycled across restarts: small→large
SCALES = [0.002, 0.005, 0.01, 0.02, 0.05, 0.1]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lead = np.array(json.load(open(LEADER))["values"], dtype=np.float64)
    sigma = lead.std()
    best_c, best_v, best_meta = LEADER_C, lead.copy(), {"scale": 0.0, "restart": -1}
    rows = []
    for r in range(N_RESTARTS):
        scale = SCALES[r % len(SCALES)]
        rng = np.random.default_rng(1000 + r)
        # high-frequency perturbation (the lever is fine sign structure)
        pert = rng.normal(scale=scale * sigma, size=len(lead))
        init = lead + pert
        t0 = time.time()
        v, c = signed_descent(init, BETAS, ITERS, lr=0.8, neg_target=0.0, neg_base=0.0)
        dt = time.time() - t0
        beats = bool(c < LEADER_C - 1e-8)
        rows.append({"restart": r, "scale": scale, "C": c, "beats": beats, "secs": round(dt, 1)})
        print(
            f"[{r + 1}/{N_RESTARTS}] scale={scale:.3f} C={c:.13f} "
            f"{'*** BEATS ***' if beats else ''} ({dt:.0f}s)",
            flush=True,
        )
        if c < best_c:
            best_c, best_v, best_meta = c, v.copy(), {"scale": scale, "restart": r}
            with open(OUT / "basinhop_best.json", "w") as fh:
                json.dump(
                    {"values": best_v.tolist(), "score": best_c, "n": len(best_v), **best_meta}, fh
                )
        with open(OUT / "basinhop_summary.json", "w") as fh:
            json.dump(
                {"leader": LEADER_C, "best_C": best_c, "best_meta": best_meta, "rows": rows},
                fh,
                indent=2,
            )
    print(
        f"\nBEST C = {best_c:.13f} (leader {LEADER_C:.13f}) "
        f"{'BEATS' if best_c < LEADER_C - 1e-8 else 'does NOT beat'}"
    )


if __name__ == "__main__":
    main()
