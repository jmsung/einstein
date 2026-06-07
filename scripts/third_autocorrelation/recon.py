"""Goal 0 recon for the P4 record-breakthrough campaign.

Re-confirms (triple-verify) the leader vs our basin scores, quantifies the
negative-content split, characterises where the negative lobes sit and whether
each solution is symmetric, and compares Fourier spectra to probe the
P2+P4 "single Fourier-side move" family hypothesis.

Usage:
    uv run python scripts/third_autocorrelation/recon.py
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import scipy.signal

from einstein.third_autocorrelation.evaluator import verify_and_compute

MB = Path(".mb/problems/4-third-autocorrelation/solutions")
LEADER = MB / "sol-organon-rank1-p4-1.4523043332.json"
OURS = MB / "solution-feat-third-autocorrelation-1.4525211550469.json"


def load(path: Path) -> np.ndarray:
    with open(path) as fh:
        return np.array(json.load(fh)["values"], dtype=np.float64)


def triple_verify(f: np.ndarray) -> dict:
    """Three independent C(f) computations. Must agree to ~1 ulp."""
    n = len(f)
    dx = 0.5 / n
    # 1. arena-exact (np.convolve)
    c1 = verify_and_compute(f.tolist())
    # 2. scipy fftconvolve — different code path
    ac2 = scipy.signal.fftconvolve(f, f, mode="full") * dx
    c2 = abs(ac2.max()) / (f.sum() * dx) ** 2
    # 3. FFT via rfft/irfft — yet another path
    m = 2 * n - 1
    F = np.fft.rfft(f, n=1 << (m - 1).bit_length())
    ac3 = np.fft.irfft(F * F)[:m] * dx
    c3 = abs(ac3.max()) / (f.sum() * dx) ** 2
    spread = max(c1, c2, c3) - min(c1, c2, c3)
    return {"c_arena": c1, "c_scipy": c2, "c_rfft": c3, "spread": spread}


def sign_profile(f: np.ndarray) -> dict:
    n = len(f)
    neg = f < 0
    n_neg = int(neg.sum())
    # where are the negatives? bucket position into deciles
    idx = np.where(neg)[0]
    deciles = np.histogram(idx / n, bins=10, range=(0, 1))[0] if n_neg else np.zeros(10, int)
    # symmetry: compare f to its reverse
    rev = f[::-1]
    sym_err = np.linalg.norm(f - rev) / np.linalg.norm(f)
    antisym_err = np.linalg.norm(f + rev) / np.linalg.norm(f)
    # contiguous negative runs (is it one block or scattered?)
    runs = np.diff(np.where(np.diff(np.r_[0, neg.astype(int), 0]))[0])[::2]
    return {
        "n": n,
        "n_neg": n_neg,
        "frac_neg": n_neg / n,
        "neg_deciles": deciles.tolist(),
        "sym_err": float(sym_err),
        "antisym_err": float(antisym_err),
        "n_neg_runs": int(len(runs)),
        "longest_neg_run": int(runs.max()) if len(runs) else 0,
    }


def spectrum(f: np.ndarray, k: int = 20) -> np.ndarray:
    """First k normalised rFFT magnitudes (scale-invariant)."""
    F = np.abs(np.fft.rfft(f - f.mean()))
    return F[:k] / (F[:k].max() + 1e-300)


def main():
    lead = load(LEADER)
    ours = load(OURS)

    print("=" * 70)
    print("TRIPLE-VERIFY")
    for name, f in [("OrganonAgent #1", lead), ("JSAgent #2 (ours)", ours)]:
        tv = triple_verify(f)
        print(
            f"  {name}: arena={tv['c_arena']:.13f} scipy={tv['c_scipy']:.13f} "
            f"rfft={tv['c_rfft']:.13f}  spread={tv['spread']:.2e}"
        )

    print("=" * 70)
    print("SIGN PROFILE")
    for name, f in [("OrganonAgent #1", lead), ("JSAgent #2 (ours)", ours)]:
        sp = sign_profile(f)
        print(f"  {name}:")
        print(f"    n={sp['n']}  neg={sp['n_neg']} ({sp['frac_neg'] * 100:.2f}%)")
        print(f"    neg by decile (0→1): {sp['neg_deciles']}")
        print(f"    sym_err={sp['sym_err']:.3e}  antisym_err={sp['antisym_err']:.3e}")
        print(f"    neg runs={sp['n_neg_runs']}  longest={sp['longest_neg_run']}")

    print("=" * 70)
    print("FOURIER SPECTRUM (first 20 normalised |rFFT| coeffs)")
    sl, so = spectrum(lead), spectrum(ours)
    print(f"  leader: {np.array2string(sl, precision=3, max_line_width=200)}")
    print(f"  ours:   {np.array2string(so, precision=3, max_line_width=200)}")
    print(f"  L2 spectral diff (first 20): {np.linalg.norm(sl - so):.4e}")


if __name__ == "__main__":
    main()
