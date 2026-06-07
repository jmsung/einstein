"""Goal 5 — sign-topology crossover of the two known-good parents.

The council established the optimal sign topology is incompressible (no ansatz
represents it) and must come from a good source. We HAVE two good sources: the
leader (1.4523043332, 27.5% neg) and ours (1.4525211550, 23.6% neg). A record is
a THIRD topology. Genetic recombination: build child sign fields by splicing the
parents' signs block-wise, take each cell's magnitude from its sign-source parent
(local coherence), then frozen-sign magnitude descent (f = s·v²). This explores
the topology space BETWEEN two good basins — where a better third may sit —
instead of cold/periodic patterns that fail.

Run in background; triple-verify any candidate vs leader and target 1.4522043.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import scipy.signal

from einstein.third_autocorrelation.evaluator import verify_and_compute
from einstein.third_autocorrelation.optimizer import frozen_sign_descent

SOL = Path(".mb/problems/4-third-autocorrelation/solutions")
LEADER = SOL / "sol-organon-rank1-p4-1.4523043332.json"
OURS = SOL / "solution-feat-third-autocorrelation-1.4525211550469.json"
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
BETAS = [1e5, 1e6, 1e7, 1e8, 1e9, 1e10]
ITERS = 350
OUT = Path("results/problem-4-third-autocorrelation")
N_TRIALS = 30
BLOCK_WIDTHS = [50, 150, 400, 1000, 3000]


def triple_spread(f):
    n = len(f)
    dx = 0.5 / n
    c1 = verify_and_compute(f.tolist())
    c2 = abs((scipy.signal.fftconvolve(f, f, "full") * dx).max()) / (f.sum() * dx) ** 2
    return float(abs(c1 - c2)), c1


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lead = np.array(json.load(open(LEADER))["values"], float)
    ours = np.array(json.load(open(OURS))["values"], float)
    n = len(lead)
    sL, sO = np.sign(lead), np.sign(ours)
    sL[sL == 0] = 1
    sO[sO == 0] = 1
    magL, magO = np.abs(lead), np.abs(ours)

    best = {"C": 1e9, "f": None, "w": None, "p": None}
    rows = []
    trial = 0
    for w in BLOCK_WIDTHS:
        nblk = (n + w - 1) // w
        for p in [0.25, 0.5, 0.75]:  # fraction of blocks taken from the leader
            rng = np.random.default_rng(900 + trial)
            take_leader = rng.random(nblk) < p
            mask = np.repeat(take_leader, w)[:n]  # True → leader, False → ours
            s_child = np.where(mask, sL, sO)
            mag_child = np.sqrt(np.where(mask, magL, magO))  # v s.t. v²=|parent|
            t0 = time.time()
            f, c = frozen_sign_descent(s_child, mag_child, BETAS, ITERS)
            dt = time.time() - t0
            beats_t = c < TARGET
            beats_l = c < LEADER_C - 1e-8
            rows.append(
                {
                    "w": w,
                    "p": p,
                    "C": c,
                    "neg": float((f < 0).mean()),
                    "beats_leader": bool(beats_l),
                    "beats_target": bool(beats_t),
                }
            )
            flag = "  *** BEATS TARGET ***" if beats_t else ("  << beats leader" if beats_l else "")
            print(
                f"  w={w:5d} p={p:.2f}: C={c:.13f} neg={(f < 0).mean() * 100:.1f}%{flag} ({dt:.0f}s)",
                flush=True,
            )
            if c < best["C"]:
                best = {"C": c, "f": f.copy(), "w": w, "p": p}
                json.dump(
                    {"values": f.tolist(), "score": c, "n": n, "w": w, "p": p},
                    open(OUT / "crossover_best.json", "w"),
                )
            json.dump(
                {"leader": LEADER_C, "target": TARGET, "best_C": best["C"], "rows": rows},
                open(OUT / "crossover_summary.json", "w"),
                indent=2,
            )
            trial += 1

    print(f"\nBEST C={best['C']:.13f} (w={best['w']}, p={best['p']})  leader {LEADER_C:.13f}")
    if best["f"] is not None:
        sp, c = triple_spread(best["f"])
        verdict = (
            "RECORD"
            if best["C"] < TARGET and sp < 1e-9
            else ("beats leader" if best["C"] < LEADER_C - 1e-8 else "no improvement")
        )
        print(f"triple-verify spread={sp:.2e}  → {verdict}")


if __name__ == "__main__":
    main()
