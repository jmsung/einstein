"""Goal 5 fragmentation-frequency sweep — the council consensus move.

Council (Tao/Hilbert/Hadamard, independently): the basin is selected by a
DISCRETE parameter — the sign-change count / fragmentation frequency — that
continuous descent cannot change (it's trapped in its starting sign topology).
Every prior method let the optimiser CHOOSE the signs; none IMPOSED them. The
one un-swept axis is the run-count itself (leader = 4705 runs; nobody swept
finer). So: freeze an imposed sign pattern on the shared leader envelope,
optimise only magnitudes (f = s·v²), and sweep the run-count R (and mid-domain
concentration). Hadamard's prediction: C(R) is U-shaped — find its minimum.

Run at n=100000 (the leader's fragmentation only exists at high n). Triple-verify
any candidate; report against leader 1.4523043332 and target 1.4522043.
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
N = 100000
BETAS = [1e4, 3e4, 1e5, 3e5, 1e6, 3e6, 1e7, 3e7, 1e8, 3e8, 1e9, 1e10]
ITERS = 700
OUT = Path("results/problem-4-third-autocorrelation")
# run-counts to sweep: ours(≈823), leader(≈4705), and FINER (the un-probed axis)
RUN_COUNTS = [823, 1600, 3000, 4705, 7000, 10000, 14000, 20000, 28000, 40000]
CONCENTRATIONS = ["uniform", "mid"]  # mid = recon's deciles 2–6 weighting


def sign_pattern(n, n_runs, mode):
    """Imposed sign field with ~n_runs sign changes; 'mid' concentrates them
    in the central domain (recon: leader's extra negatives sit mid-domain)."""
    x = np.linspace(0.0, 1.0, n)
    if mode == "uniform":
        density = np.ones(n)
    else:  # mid-domain Gaussian weighting (peak at x=0.5)
        density = 0.4 + np.exp(-((x - 0.5) ** 2) / (2 * 0.22**2))
    density *= n_runs / density.sum()  # ∫density ≈ n_runs sign changes
    phi = np.cumsum(density)
    return np.sign(np.cos(np.pi * phi) + 1e-12)


def triple_verify(f):
    n = len(f)
    dx = 0.5 / n
    c1 = verify_and_compute(f.tolist())
    c2 = abs((scipy.signal.fftconvolve(f, f, "full") * dx).max()) / (f.sum() * dx) ** 2
    m = 2 * n - 1
    F = np.fft.rfft(f, n=1 << (m - 1).bit_length())
    c3 = abs((np.fft.irfft(F * F)[:m] * dx).max()) / (f.sum() * dx) ** 2
    return float(max(c1, c2, c3) - min(c1, c2, c3))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lead = np.array(json.load(open(LEADER))["values"], float)
    # magnitudes = FULL |leader| (fine structure preserved — a low-pass envelope
    # loses the magnitude detail and the n=100k magnitude opt gets stuck at 1.54).
    # The imposed sign pattern s_R is what varies; magnitudes start leader-faithful.
    v_init = np.sqrt(np.abs(lead))
    print(
        f"sweep at n={N}; magnitudes=|leader|; leader={LEADER_C:.10f} target={TARGET:.10f}",
        flush=True,
    )

    best = {"C": 1e9, "v": None, "R": None, "mode": None}
    rows = []
    for mode in CONCENTRATIONS:
        for R in RUN_COUNTS:
            s = sign_pattern(N, R, mode)
            t0 = time.time()
            f, c = frozen_sign_descent(s, v_init, BETAS, ITERS)
            dt = time.time() - t0
            runs = int((np.diff(np.sign(f)) != 0).sum())
            beats_leader = bool(c < LEADER_C - 1e-8)
            beats_target = bool(c < TARGET)
            rows.append(
                {
                    "R": R,
                    "mode": mode,
                    "C": c,
                    "actual_runs": runs,
                    "neg": float((f < 0).mean()),
                    "beats_leader": beats_leader,
                    "beats_target": beats_target,
                    "secs": round(dt, 1),
                }
            )
            flag = (
                "  *** BEATS TARGET ***"
                if beats_target
                else ("  << beats leader" if beats_leader else "")
            )
            print(
                f"  R={R:6d} {mode:7s}: C={c:.13f} runs={runs:5d} neg={(f < 0).mean() * 100:4.1f}%{flag} ({dt:.0f}s)",
                flush=True,
            )
            if c < best["C"]:
                best = {"C": c, "v": f.copy(), "R": R, "mode": mode}
                json.dump(
                    {"values": f.tolist(), "score": c, "n": N, "R": R, "mode": mode},
                    open(OUT / "fragfreq_best.json", "w"),
                )
            json.dump(
                {
                    "leader": LEADER_C,
                    "target": TARGET,
                    "best_C": best["C"],
                    "best_R": best["R"],
                    "best_mode": best["mode"],
                    "rows": rows,
                },
                open(OUT / "fragfreq_summary.json", "w"),
                indent=2,
            )

    print(f"\nBEST C={best['C']:.13f} at R={best['R']} ({best['mode']})  leader {LEADER_C:.13f}")
    if best["v"] is not None:
        sp = triple_verify(best["v"])
        print(
            f"triple-verify spread={sp:.2e}  {'RECORD' if best['C'] < TARGET and sp < 1e-9 else ''}"
        )


if __name__ == "__main__":
    main()
