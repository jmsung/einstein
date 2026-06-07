"""Goal 5 — Hilbert's spectral sign-texture descent (aperiodic sign search).

Periodic imposed signs fail (too crude); good sign topologies are APERIODIC. So
parameterise the sign field by the FOURIER COEFFICIENTS of a mid-band texture and
optimise them directly:

    f = E ⊙ tanh(κ · texture),   texture = irfft( coeffs on band [k_lo, k_hi] )

- E = |leader| magnitude profile (the shared envelope, fixed).
- coeffs (a_k, b_k) on a mid-band are the ~few-thousand smooth DOF whose optimum
  is an APERIODIC sign texture — exactly the class periodic ansätze miss.
- κ-sharpening homotopy (1 → 60) turns the smooth texture into hard signs while
  the objective stays the exact-ish smooth-max C; this CREATES sign flips instead
  of the β-cascade smoothing them away.

Optimise via autograd (torch) through tanh + FFT autoconvolution. Sweep the band
and seed (leader's own sign-texture vs random). Triple-verify; report vs leader
1.4523043332 and target 1.4522043. Run in background.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.third_autocorrelation.optimizer import arena_c, autoconv_fft, smooth_max

LEADER = Path(
    ".mb/problems/4-third-autocorrelation/solutions/sol-organon-rank1-p4-1.4523043332.json"
)
LEADER_C = 1.4523043331832
TARGET = LEADER_C - 1e-4
N = 100000
OUT = Path("results/problem-4-third-autocorrelation")
KAPPAS = [1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0]
BETAS = [1e5, 1e6, 1e7, 1e8, 1e9]  # per-kappa smooth-max sharpness
ITERS = 120
# (k_lo, k_hi) mid-bands to sweep; leader has ~4705 runs → texture energy ~k≈2350
BANDS = [(20, 2400), (20, 4000), (200, 4000), (20, 6000), (1000, 5000)]


def run(band, seed_mode, mag, lead_sign_tex, base_seed):
    klo, khi = band
    dev = "mps" if torch.backends.mps.is_available() else "cpu"
    E = torch.tensor(mag, dtype=torch.float64)
    # texture coeffs (real DOF a_k,b_k packed as a real vector over the band)
    nband = khi - klo
    if seed_mode == "leader":
        # project leader's sign field onto the band as the seed
        F = np.fft.rfft(lead_sign_tex)
        ar = np.zeros(2 * nband)
        ar[:nband] = F[klo:khi].real
        ar[nband:] = F[klo:khi].imag
        ar = ar / (np.abs(ar).max() + 1e-12)
    else:
        rng = np.random.default_rng(base_seed)
        ar = rng.normal(scale=0.1, size=2 * nband)
    a = torch.tensor(ar, dtype=torch.float64, requires_grad=True)

    def texture():
        full = torch.zeros(N // 2 + 1, dtype=torch.complex128)
        re = a[:nband]
        im = a[nband:]
        full[klo:khi] = torch.complex(re, im)
        t = torch.fft.irfft(full, n=N)
        return t / (t.detach().abs().mean() + 1e-12)

    best_c, best_f = float("inf"), None
    for kappa in KAPPAS:
        for beta in BETAS:
            opt = torch.optim.LBFGS(
                [a],
                lr=0.5,
                max_iter=ITERS,
                history_size=50,
                line_search_fn="strong_wolfe",
                tolerance_grad=1e-12,
            )

            def closure():
                opt.zero_grad()
                s = torch.tanh(kappa * texture())
                f = E * s
                dx = 0.5 / N
                conv = autoconv_fft(f) * dx
                integ = f.sum() * dx
                loss = smooth_max(conv, beta) / (integ**2 + 1e-30)
                loss.backward()
                return loss

            opt.step(closure)
            with torch.no_grad():
                s = torch.sign(torch.tanh(kappa * texture()))
                f = (E * s).cpu().numpy()
                if f.sum() < 0:
                    f = -f
                c = arena_c(f)
                if c < best_c:
                    best_c, best_f = c, f.copy()
    return best_f, best_c


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lead = np.array(json.load(open(LEADER))["values"], float)
    mag = np.abs(lead)
    lead_sign = np.sign(lead)
    lead_sign[lead_sign == 0] = 1.0
    print(
        f"spectral sign-texture at n={N}; E=|leader|; leader={LEADER_C:.10f} target={TARGET:.10f}",
        flush=True,
    )
    best = {"C": 1e9, "f": None, "band": None, "seed": None}
    rows = []
    for band in BANDS:
        for seed_mode in ["leader", "random"]:
            t0 = time.time()
            try:
                f, c = run(band, seed_mode, mag, lead_sign, base_seed=hash(band) % 9999)
            except Exception as e:
                print(f"  band={band} {seed_mode}: ERROR {e}", flush=True)
                continue
            dt = time.time() - t0
            runs = int((np.diff(np.sign(f)) != 0).sum())
            flag = (
                "  *** BEATS TARGET ***"
                if c < TARGET
                else ("  << beats leader" if c < LEADER_C - 1e-8 else "")
            )
            print(
                f"  band={str(band):12s} {seed_mode:6s}: C={c:.13f} runs={runs} neg={(f < 0).mean() * 100:.1f}%{flag} ({dt:.0f}s)",
                flush=True,
            )
            rows.append({"band": band, "seed": seed_mode, "C": c, "runs": runs})
            if c < best["C"]:
                best = {"C": c, "f": f.copy(), "band": band, "seed": seed_mode}
                json.dump(
                    {"values": f.tolist(), "score": c, "n": N, "band": band, "seed": seed_mode},
                    open(OUT / "spectral_best.json", "w"),
                )
            json.dump(
                {
                    "leader": LEADER_C,
                    "target": TARGET,
                    "best_C": best["C"],
                    "best_band": best["band"],
                    "rows": rows,
                },
                open(OUT / "spectral_summary.json", "w"),
                indent=2,
            )
    print(
        f"\nBEST C={best['C']:.13f} band={best['band']} seed={best['seed']}  leader {LEADER_C:.13f}"
    )


if __name__ == "__main__":
    main()
