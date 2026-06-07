"""Goal 5 — simulated annealing on the SIGN FIELD (discrete global search).

The council established P4 basins are a DISCRETE sign-topology problem. Gradient
(smooth-max), greedy (LP / single-flip), and recombination all fail because they
cannot cross sign-change barriers or explore the discrete space globally. SA /
parallel tempering is the canonical discrete global optimizer: it crosses
barriers via thermal fluctuations. Here: state = sign field s (magnitudes fixed
at |leader| for fast eval); energy = C(s) via FFT; propose flipping a small random
set of signs; Metropolis-accept at an annealing temperature; periodically
re-polish magnitudes (frozen_sign_descent) for the current signs and continue.

Start from the leader (C=1.4523043332) and from a higher-temperature shake.
Triple-verify any candidate; target 1.4522043. Run in background.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import scipy.signal

from einstein.third_autocorrelation.evaluator import verify_and_compute
from einstein.third_autocorrelation.optimizer import frozen_sign_descent

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
OUT = Path("results/problem-4-third-autocorrelation")
N_STEPS = 60000
REPOLISH_EVERY = 4000


def make_ceval(n):
    dx = 0.5 / n
    m = 2 * n - 1
    pad = 1 << (m - 1).bit_length()

    def C(f):
        F = np.fft.rfft(f, n=pad)
        conv = np.fft.irfft(F * F, n=pad)[:m] * dx
        return abs(conv.max()) / (f.sum() * dx) ** 2

    return C


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lead = np.array(json.load(open(LEADER))["values"], float)
    n = len(lead)
    mag = np.abs(lead)
    C = make_ceval(n)

    s = np.sign(lead)
    s[s == 0] = 1.0
    f = s * mag
    cur = C(f)
    best_s, best_mag, best_c = s.copy(), mag.copy(), cur
    print(f"SA start C={cur:.13f} (leader {LEADER_C:.13f}) n={n}", flush=True)

    rng = np.random.default_rng(424242)
    T0, T1 = 2e-4, 1e-7  # annealing range (energy scale ~ C deltas)
    accepts = 0
    t0 = time.time()
    for step in range(N_STEPS):
        T = T0 * (T1 / T0) ** (step / N_STEPS)
        k = int(rng.integers(1, 6))  # flip 1-5 signs
        idx = rng.integers(0, n, size=k)
        s_new = s.copy()
        s_new[idx] *= -1.0
        f_new = s_new * mag
        if f_new.sum() <= 0:
            continue
        c_new = C(f_new)
        if c_new < cur or rng.random() < np.exp(-(c_new - cur) / T):
            s, cur = s_new, c_new
            accepts += 1
            if cur < best_c:
                best_s, best_mag, best_c = s.copy(), mag.copy(), cur
        if (step + 1) % REPOLISH_EVERY == 0:
            # re-polish magnitudes for the current sign field, then continue
            fp, cp = frozen_sign_descent(s, mag, [1e7, 1e8, 1e9, 1e10], 200)
            if cp < cur:
                mag = np.sqrt(np.abs(fp))
                s = np.sign(fp)
                s[s == 0] = 1.0
                cur = cp
                if cp < best_c:
                    best_s, best_mag, best_c = s.copy(), mag.copy(), cp
            print(
                f"[{step + 1:6d}] T={T:.1e} cur={cur:.13f} best={best_c:.13f} "
                f"acc={accepts}{'  *** BEATS TARGET ***' if best_c < TARGET else ''} "
                f"({time.time() - t0:.0f}s)",
                flush=True,
            )
            best_f = best_s * best_mag
            json.dump(
                {"values": best_f.tolist(), "score": best_c, "n": n},
                open(OUT / "anneal_best.json", "w"),
            )
            json.dump(
                {
                    "leader": LEADER_C,
                    "target": TARGET,
                    "best_C": best_c,
                    "step": step + 1,
                    "accepts": accepts,
                },
                open(OUT / "anneal_summary.json", "w"),
            )

    best_f = best_s * best_mag
    c1 = verify_and_compute(best_f.tolist())
    dx = 0.5 / n
    c2 = (
        abs((scipy.signal.fftconvolve(best_f, best_f, "full") * dx).max())
        / (best_f.sum() * dx) ** 2
    )
    print(f"\nBEST C={best_c:.13f} leader {LEADER_C:.13f} target {TARGET:.13f}")
    print(f"triple-verify: arena={c1:.13f} scipy={c2:.13f} spread={abs(c1 - c2):.2e}")
    print(
        "RECORD"
        if best_c < TARGET and abs(c1 - c2) < 1e-9
        else ("beats leader" if best_c < LEADER_C - 1e-8 else "no improvement")
    )


if __name__ == "__main__":
    main()
