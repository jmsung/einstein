"""Fourier-domain alternating projections for Problem 3.

Gerchberg-Saxton style: alternate between
  1. Space domain: project to f ≥ 0
  2. Fourier domain: modify power spectrum |f̂|² toward flat autoconvolution

Since g = f*f has ĝ = |f̂|², a flat g means |f̂|² ≈ constant.
So we want |f̂| ≈ constant (flat spectrum) while f ≥ 0.

Also try: target a specific autoconvolution shape (rectangle/plateau).
"""

import sys

sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

from einstein.autocorrelation_fast import fast_evaluate, diagnose

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def save_result(f, score, tag=""):
    result = {
        "problem": "second-autocorrelation-inequality",
        "n_points": len(f),
        "score": score,
        "values": f.tolist(),
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"c2_n{len(f)}_{score:.8f}_{tag}.json"
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")


def gerchberg_saxton(n, n_iter=500, target_type="flat_spectrum", seed=42,
                     alpha=0.5, beta_anneal=True):
    """Alternating projections between non-negativity and spectral target.

    Args:
        n: Function length.
        n_iter: Number of iterations.
        target_type: 'flat_spectrum', 'plateau_autoconv', or 'soft_clip'.
        seed: Random seed.
        alpha: Blending factor (0=keep old, 1=full update).
        beta_anneal: Gradually sharpen the target.
    """
    rng = np.random.default_rng(seed)
    f = rng.uniform(0.1, 1.0, n)
    best_score = 0.0
    best_f = f.copy()

    for t in range(n_iter):
        # Anneal: start soft, end sharp
        progress = t / max(n_iter - 1, 1)
        sharpness = 1.0 + 9.0 * progress if beta_anneal else 5.0

        # 1. Compute current spectrum and autoconvolution
        f_hat = np.fft.rfft(f)
        f_mag = np.abs(f_hat)
        f_phase = np.angle(f_hat)

        # 2. Fourier-domain projection: modify magnitude
        if target_type == "flat_spectrum":
            # Target: flat |f̂| (white spectrum)
            target_mag = np.mean(f_mag) * np.ones_like(f_mag)
            # Blend toward target
            new_mag = (1 - alpha) * f_mag + alpha * target_mag

        elif target_type == "plateau_autoconv":
            # Target: autoconvolution is a plateau
            # g_hat = |f_hat|^2, want g to be rectangular
            # A rectangular g has g_hat = sinc, so |f_hat|^2 = sinc
            # → |f_hat| = sqrt(|sinc|)
            freqs = np.arange(len(f_hat))
            width = 0.3  # fraction of bandwidth
            sinc_target = np.sinc(freqs * width / len(f_hat))
            target_mag = np.sqrt(np.abs(sinc_target)) * np.mean(f_mag) / max(np.mean(np.sqrt(np.abs(sinc_target))), 1e-30)
            new_mag = (1 - alpha) * f_mag + alpha * target_mag

        elif target_type == "soft_clip":
            # Soft-clip the autoconvolution: reduce peaks, boost valleys
            conv = fftconvolve(f, f, mode="full")
            c_max = np.max(conv)
            if c_max > 0:
                # Target autoconv: clip to sharpness% of max
                clip_level = c_max * (1.0 - 0.1 / sharpness)
                target_conv = np.minimum(conv, clip_level)
                # Scale to preserve mass
                target_conv *= np.sum(conv) / max(np.sum(target_conv), 1e-30)
                # Get target spectrum: g_hat = FFT(target_g), |f_hat| = sqrt(|g_hat|)
                # Need nfft matching f's rfft length
                nfft_gs = 1
                while nfft_gs < len(target_conv):
                    nfft_gs <<= 1
                g_hat = np.fft.rfft(target_conv, n=nfft_gs)
                # Resample to match f_hat length
                target_mag_full = np.sqrt(np.maximum(np.abs(g_hat), 0))
                target_mag = np.interp(
                    np.linspace(0, 1, len(f_mag)),
                    np.linspace(0, 1, len(target_mag_full)),
                    target_mag_full
                )
                # Normalize
                target_mag *= np.sum(f_mag) / max(np.sum(target_mag), 1e-30)
                new_mag = (1 - alpha) * f_mag + alpha * target_mag
            else:
                new_mag = f_mag

        else:
            new_mag = f_mag

        # 3. Reconstruct f with modified magnitude, original phase
        f_hat_new = new_mag * np.exp(1j * f_phase)
        f_new = np.fft.irfft(f_hat_new, n=n)

        # 4. Space-domain projection: enforce non-negativity
        f = np.maximum(f_new, 0)

        # Track best score
        if (t + 1) % 20 == 0:
            score = fast_evaluate(f)
            if score > best_score:
                best_score = score
                best_f = f.copy()

    score = fast_evaluate(f)
    if score > best_score:
        best_score = score
        best_f = f.copy()

    return best_f, best_score


def hybrid_gs_adam(n, n_gs=200, n_adam=3000, seed=42, device='cpu'):
    """Gerchberg-Saxton for initialization, then Adam for refinement."""
    import torch

    # Phase 1: GS to find structure
    f, score_gs = gerchberg_saxton(n, n_iter=n_gs, target_type="soft_clip",
                                    seed=seed, alpha=0.3)
    print(f"    GS init: C={score_gs:.8f}")

    # Phase 2: Adam refinement
    h = torch.tensor(f, dtype=torch.float32, device=device).unsqueeze(0)
    h.requires_grad_(True)
    opt = torch.optim.Adam([h], lr=1e-2)

    best_score = score_gs
    best_f = f.copy()

    nc = 2 * n - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    for t in range(n_adam):
        opt.zero_grad()
        ff = torch.clamp(h, min=0)
        F = torch.fft.rfft(ff, n=nfft, dim=1)
        conv = torch.fft.irfft(F * F, n=nfft, dim=1)[:, :nc]
        c_sq = torch.sum(conv * conv, dim=1)
        c_shift = torch.sum(conv[:, :-1] * conv[:, 1:], dim=1)
        c_sum = torch.sum(conv, dim=1)
        c_max = torch.max(conv, dim=1).values
        C = (2 * c_sq + c_shift) / (3 * c_sum * c_max + 1e-30)
        (-C.mean()).backward()
        opt.step()
        with torch.no_grad():
            h.clamp_(min=0)

        if (t + 1) % 500 == 0:
            c_val = C.item()
            if c_val > best_score and c_val < 1.0:
                best_score = c_val
                best_f = h[0].detach().cpu().numpy().copy()
                best_f = np.maximum(best_f, 0)

    c_val = C.item()
    if c_val > best_score and c_val < 1.0:
        best_score = c_val
        best_f = h[0].detach().cpu().numpy().copy()
        best_f = np.maximum(best_f, 0)

    verified = fast_evaluate(best_f)
    return best_f, verified


def main():
    print("=" * 60)
    print("Fourier Alternating Projections (Gerchberg-Saxton)")
    print("=" * 60)

    import torch
    device = 'mps' if torch.backends.mps.is_available() else 'cpu'

    results = []

    # Test all target types at multiple n values
    for n in [500, 1000, 2000]:
        print(f"\n--- n={n} ---")
        for target in ["flat_spectrum", "plateau_autoconv", "soft_clip"]:
            best_s = 0
            for seed in range(10):
                f, s = gerchberg_saxton(n, n_iter=300, target_type=target,
                                        seed=seed, alpha=0.3)
                if s > best_s:
                    best_s = s
                    best_f_gs = f.copy()
            print(f"  {target:20s}: C={best_s:.8f}")
            results.append((f"gs_{target}_n{n}", best_s, best_f_gs))

    # Hybrid: GS init + Adam refinement
    print(f"\n--- Hybrid GS+Adam ---")
    for n in [768, 2000]:
        best_hybrid_s = 0
        best_hybrid_f = None
        for seed in range(5):
            f, s = hybrid_gs_adam(n, n_gs=200, n_adam=5000, seed=seed, device=device)
            if s > best_hybrid_s:
                best_hybrid_s = s
                best_hybrid_f = f.copy()
            print(f"  n={n} seed={seed}: C={s:.8f}")
        results.append((f"hybrid_n{n}", best_hybrid_s, best_hybrid_f))
        save_result(best_hybrid_f, best_hybrid_s, f"fourier_hybrid_n{n}")

    # Compare all
    results.sort(key=lambda x: x[1], reverse=True)
    print(f"\n{'='*60}")
    print("Results ranking:")
    for name, score, _ in results[:10]:
        print(f"  {score:.8f}  {name}")

    # Best overall
    best_name, best_score, best_f = results[0]
    d = diagnose(best_f)
    print(f"\nBEST: {best_name}, C={best_score:.8f}")
    print(f"  n={len(best_f)}, nnz={d['nnz']}, blocks={d['n_blocks']}")
    save_result(best_f, best_score, "fourier_final")


if __name__ == "__main__":
    main()
