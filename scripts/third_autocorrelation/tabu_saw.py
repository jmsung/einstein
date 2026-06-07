"""Goal 5 — tabu self-avoiding-walk steepest descent on the sign field.

The LABS / merit-factor SOTA (lssOrel/lssMAts) algorithm class — proven to find
fragmented ±1 incompressible optima where gradient/random-SA fail (web research).
Distinct from our earlier random-Metropolis SA and crossover:
  - STEEPEST: each step pick the candidate sign-flip that most reduces C
    (over a random non-tabu candidate subset).
  - TABU: forbid recently-flipped cells (tenure) → self-avoiding walk.
  - SAW RESTART: on stall, kick from the best-so-far and continue.
  - height re-polish (frozen_sign_descent) periodically co-adapts magnitudes.

Run at moderate n where all-candidate eval is feasible; the diagnostic is whether
it finds a basin BELOW the equioscillation/escape value at that n (a better basin
to lift). Triple-verify; target 1.4522043.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.third_autocorrelation.optimizer import arena_c, frozen_sign_descent

SOL = Path(".mb/problems/4-third-autocorrelation/solutions")
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
N = 2000
ESCAPE_AT_N = 1.4531  # leader/our family value near n=2000 (progression) — beat this
K_CAND = 200  # candidate flips evaluated per step
TABU_TENURE = N // 8
STEPS = 6000
STALL_RESTART = 400
REPOLISH_EVERY = 800
OUT = Path("results/problem-4-third-autocorrelation")


def C_of(s, mag):
    return arena_c(s * mag)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lead = np.array(
        json.load(open(SOL / "sol-organon-rank1-p4-1.4523043332.json"))["values"], float
    )
    ds = lead[: (len(lead) // N) * N].reshape(N, -1).mean(1)
    mag = np.abs(ds)
    mag = np.clip(mag, 1e-3, None)
    s = np.sign(ds)
    s[s == 0] = 1.0
    cur = C_of(s, mag)
    best_s, best_mag, best_c = s.copy(), mag.copy(), cur
    print(
        f"tabu-SAW n={N} start C={cur:.13f} (escape@n≈{ESCAPE_AT_N}, leader {LEADER_C:.10f})",
        flush=True,
    )

    rng = np.random.default_rng(2026)
    tabu = np.zeros(N, dtype=int)  # step index until which cell i is tabu
    since_improve = 0
    t0 = time.time()
    for step in range(STEPS):
        cand = rng.choice(N, size=min(K_CAND, N), replace=False)
        cand = cand[tabu[cand] <= step]
        if len(cand) == 0:
            continue
        # evaluate each candidate flip (steepest over the subset)
        best_i, best_ci = -1, cur
        for i in cand:
            s[i] *= -1.0
            ci = C_of(s, mag)
            s[i] *= -1.0
            if ci < best_ci:
                best_ci, best_i = ci, i
        if best_i >= 0:
            s[best_i] *= -1.0
            cur = best_ci
            tabu[best_i] = step + TABU_TENURE
            since_improve = 0
            if cur < best_c:
                best_s, best_mag, best_c = s.copy(), mag.copy(), cur
        else:
            since_improve += 1

        if since_improve >= STALL_RESTART:  # SAW kick from best
            s = best_s.copy()
            flip = rng.choice(N, size=rng.integers(3, 12), replace=False)
            s[flip] *= -1.0
            cur = C_of(s, mag)
            since_improve = 0

        if (step + 1) % REPOLISH_EVERY == 0:
            f, cp = frozen_sign_descent(s, np.sqrt(mag), [1e6, 1e7, 1e8, 1e9, 1e10], 200)
            if cp < cur:
                mag = np.abs(f)
                mag = np.clip(mag, 1e-3, None)
                s = np.sign(f)
                s[s == 0] = 1.0
                cur = cp
                if cp < best_c:
                    best_s, best_mag, best_c = s.copy(), mag.copy(), cp
            print(
                f"[{step + 1:5d}] cur={cur:.13f} best={best_c:.13f} "
                f"{'BELOW ESCAPE' if best_c < ESCAPE_AT_N - 1e-5 else ''} ({time.time() - t0:.0f}s)",
                flush=True,
            )
            json.dump(
                {
                    "n": N,
                    "escape_at_n": ESCAPE_AT_N,
                    "leader": LEADER_C,
                    "best_C": best_c,
                    "step": step + 1,
                },
                open(OUT / "tabu_summary.json", "w"),
            )
            json.dump(
                {"values": (best_s * best_mag).tolist(), "score": best_c, "n": N},
                open(OUT / "tabu_best_n2000.json", "w"),
            )

    print(f"\nBEST(n={N}) C={best_c:.13f}  escape@n≈{ESCAPE_AT_N}  leader {LEADER_C:.13f}")
    print(
        "found a better basin → lift to 100k"
        if best_c < ESCAPE_AT_N - 1e-5
        else "no better basin than the escape family at this n"
    )


if __name__ == "__main__":
    main()
