"""Goal 5 — discrete sign-flip basin-hopping from the leader (Tao's Backup 1).

The basin is selected by sign topology; continuous descent can't change it, and
imposed PERIODIC sign patterns are too crude (→2.5). The right move: start from
the leader (a known good aperiodic sign topology, C=1.4523043332) and make
DISCRETE single-edits — flip the sign of a contiguous block (insert/delete sign
changes) — then re-polish magnitudes with signs frozen (f = s·v²). Accept on
improvement (Metropolis at tiny T). This walks the combinatorial sign-topology
neighbourhood of the leader, reachable by single discrete edits that gradient
descent forbids, hunting the adjacent C≈1.4522043 basin.

Run in background; checkpoints best. Triple-verify downstream.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import arena_c, frozen_sign_descent

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
N = 100000
# short warm re-polish per proposal (signs change little, magnitudes adapt fast)
BETAS = [1e6, 1e7, 1e8, 1e9, 1e10]
ITERS = 250
N_PROPOSALS = 400
OUT = Path("results/problem-4-third-autocorrelation")


def propose(s, mag, rng):
    """One discrete sign-topology edit: flip a contiguous block of random width."""
    s2 = s.copy()
    move = rng.random()
    a = rng.integers(0, N)
    if move < 0.5:
        w = int(rng.integers(2, 60))  # flip a short block (fine edit)
    else:
        w = int(rng.integers(60, 800))  # flip a longer block (coarse edit)
    s2[a : a + w] *= -1.0
    return s2


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lead = np.array(json.load(open(LEADER))["values"], float)
    s = np.sign(lead)
    s[s == 0] = 1.0
    mag = np.sqrt(np.abs(lead))  # v such that v² = |leader|
    cur_c = arena_c(s * mag**2)
    best_s, best_mag, best_c = s.copy(), mag.copy(), cur_c
    print(f"start: C={cur_c:.13f} (leader {LEADER_C:.13f})", flush=True)

    rng = np.random.default_rng(20260606)
    accepts = 0
    rows = []
    for it in range(N_PROPOSALS):
        s_prop = propose(best_s, best_mag, rng)
        t0 = time.time()
        f, c = frozen_sign_descent(s_prop, best_mag, BETAS, ITERS)
        dt = time.time() - t0
        improved = c < best_c - 1e-12
        if improved:
            best_s = np.sign(f)
            best_s[best_s == 0] = 1.0
            best_mag = np.sqrt(np.abs(f))
            best_c = c
            accepts += 1
            json.dump(
                {"values": f.tolist(), "score": c, "n": N}, open(OUT / "signflip_best.json", "w")
            )
        beats_t = c < TARGET
        rows.append({"it": it, "C": c, "best_C": best_c, "improved": bool(improved)})
        tag = "  *** BEATS TARGET ***" if beats_t else ("  <improved>" if improved else "")
        if it % 10 == 0 or improved or beats_t:
            print(f"[{it:3d}] propose C={c:.13f} best={best_c:.13f}{tag} ({dt:.0f}s)", flush=True)
        json.dump(
            {
                "leader": LEADER_C,
                "target": TARGET,
                "best_C": best_c,
                "accepts": accepts,
                "n_proposals": it + 1,
            },
            open(OUT / "signflip_summary.json", "w"),
        )

    print(f"\nBEST C={best_c:.13f} after {N_PROPOSALS} proposals ({accepts} improvements)")
    print(
        f"leader {LEADER_C:.13f}  target {TARGET:.13f}  "
        f"{'RECORD' if best_c < TARGET else 'beats leader' if best_c < LEADER_C - 1e-8 else 'no improvement'}"
    )


if __name__ == "__main__":
    main()
