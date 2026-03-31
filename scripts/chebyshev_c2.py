"""Chebyshev basis optimizer for Problem 3.

Inspired by Rechnitzer (arXiv:2602.07292): parameterize f using
(1-4x²)^(j-1/2) basis functions. This reduces optimization from
n=100k parameters to ~50-100 coefficients.

Also tries arcsine distribution seed (Martin & O'Bryant):
f(x) = 1/sqrt(1-4x²) — near-minimal autoconvolution L2.
"""

import sys

sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
import torch

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


def build_basis(n_points, n_coeffs, support=0.499):
    """Build (1-4x²)^(j-1/2) basis on n_points grid."""
    x = np.linspace(-support, support, n_points)
    inner = np.maximum(1 - 4 * x**2, 1e-30)
    basis = np.zeros((n_coeffs, n_points))
    for j in range(n_coeffs):
        basis[j] = inner ** (j - 0.5)
    return basis, x


def coeffs_to_f(coeffs, basis):
    """Reconstruct f from basis coefficients, enforce non-negativity."""
    return np.maximum(np.dot(coeffs, basis), 0)


def optimize_chebyshev(n_points, n_coeffs, n_iters=5000, device='cpu', seed=42):
    """Optimize in the Chebyshev basis via Adam."""
    basis, x = build_basis(n_points, n_coeffs)
    basis_t = torch.tensor(basis, dtype=torch.float32, device=device)

    torch.manual_seed(seed)

    # Initialize coefficients — start with arcsine-like shape
    c = torch.zeros(n_coeffs, dtype=torch.float32, device=device)
    c[0] = 1.0  # (1-4x²)^(-1/2) = arcsine distribution
    c.requires_grad_(True)

    opt = torch.optim.Adam([c], lr=1e-2)
    best_score = 0.0
    best_f = None

    nc = 2 * n_points - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    for t in range(n_iters):
        opt.zero_grad()

        f = torch.clamp(c @ basis_t, min=0).unsqueeze(0)  # (1, n)
        F = torch.fft.rfft(f, n=nfft, dim=1)
        conv = torch.fft.irfft(F * F, n=nfft, dim=1)[:, :nc]

        c_sq = torch.sum(conv * conv, dim=1)
        c_shift = torch.sum(conv[:, :-1] * conv[:, 1:], dim=1)
        c_sum = torch.sum(conv, dim=1)
        c_max = torch.max(conv, dim=1).values
        C = (2 * c_sq + c_shift) / (3 * c_sum * c_max + 1e-30)

        (-C).backward()
        opt.step()

        if (t + 1) % 500 == 0:
            c_val = C.item()
            if c_val > best_score and c_val < 1.0:
                best_score = c_val
                best_f = torch.clamp(c @ basis_t, min=0).detach().cpu().numpy()

    if best_f is None:
        best_f = torch.clamp(c @ basis_t, min=0).detach().cpu().numpy()

    verified = fast_evaluate(best_f)
    return best_f, verified, c.detach().cpu().numpy()


def optimize_free_basis(n_points, n_basis, n_iters=5000, device='cpu', seed=42):
    """Optimize with learned Gaussian-bump basis (position + width + height)."""
    torch.manual_seed(seed)

    # n_basis bumps: each has (center, width, height)
    centers = torch.linspace(0.1, 0.9, n_basis, device=device, dtype=torch.float32)
    widths = torch.full((n_basis,), 0.05, device=device, dtype=torch.float32)
    heights = torch.ones(n_basis, device=device, dtype=torch.float32)

    centers = centers.clone().requires_grad_(True)
    widths = widths.clone().requires_grad_(True)
    heights = heights.clone().requires_grad_(True)

    opt = torch.optim.Adam([centers, widths, heights], lr=5e-3)
    x = torch.linspace(0, 1, n_points, device=device, dtype=torch.float32)

    nc = 2 * n_points - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    best_score = 0.0
    best_f = None

    for t in range(n_iters):
        opt.zero_grad()

        # Build f from Gaussian bumps
        w = torch.clamp(widths, min=0.001)
        h = torch.clamp(heights, min=0)
        f = torch.zeros(n_points, device=device, dtype=torch.float32)
        for i in range(n_basis):
            f = f + h[i] * torch.exp(-0.5 * ((x - centers[i]) / w[i])**2)
        f = torch.clamp(f, min=0).unsqueeze(0)

        F = torch.fft.rfft(f, n=nfft, dim=1)
        conv = torch.fft.irfft(F * F, n=nfft, dim=1)[:, :nc]

        c_sq = torch.sum(conv * conv, dim=1)
        c_shift = torch.sum(conv[:, :-1] * conv[:, 1:], dim=1)
        c_sum = torch.sum(conv, dim=1)
        c_max = torch.max(conv, dim=1).values
        C = (2 * c_sq + c_shift) / (3 * c_sum * c_max + 1e-30)

        (-C).backward()
        opt.step()

        if (t + 1) % 500 == 0:
            c_val = C.item()
            f_np = f[0].detach().cpu().numpy()
            verified = fast_evaluate(f_np)
            if verified > best_score:
                best_score = verified
                best_f = f_np.copy()

    if best_f is None:
        best_f = f[0].detach().cpu().numpy()
        best_score = fast_evaluate(best_f)

    return best_f, best_score


def main():
    print("=" * 60)
    print("Chebyshev / Low-Dim Basis Optimizer")
    print("=" * 60)

    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"Device: {device}")
    results = []

    # Test 1: Chebyshev basis with varying n_coeffs
    print("\n--- Chebyshev basis (arcsine seed) ---")
    for n in [500, 1000, 2000]:
        for nc in [10, 20, 50]:
            f, s, coeffs = optimize_chebyshev(n, nc, n_iters=5000, device=device)
            print(f"  n={n}, coeffs={nc}: C={s:.8f}")
            results.append((f"cheby_n{n}_c{nc}", s, f))

    # Test 2: Free Gaussian-bump basis
    print("\n--- Free Gaussian bumps ---")
    for n in [500, 1000, 2000]:
        for nb in [10, 20, 50, 100]:
            f, s = optimize_free_basis(n, nb, n_iters=5000, device=device)
            print(f"  n={n}, bumps={nb}: C={s:.8f}")
            results.append((f"bumps_n{n}_b{nb}", s, f))

    # Test 3: Arcsine distribution as initialization for full Adam
    print("\n--- Arcsine seed + full Adam ---")
    for n in [768, 2000]:
        x = np.linspace(-0.499, 0.499, n)
        f_arc = (2 / np.pi) / np.sqrt(np.maximum(1 - 4 * x**2, 1e-10))
        s_arc = fast_evaluate(f_arc)
        print(f"  Arcsine raw n={n}: C={s_arc:.8f}")

        # Adam refinement
        h = torch.tensor(f_arc, dtype=torch.float32, device=device).unsqueeze(0)
        h.requires_grad_(True)
        opt = torch.optim.Adam([h], lr=1e-2)
        best_s = s_arc
        best_f = f_arc.copy()

        nc = 2 * n - 1
        nfft = 1
        while nfft < nc:
            nfft <<= 1

        for t in range(8000):
            opt.zero_grad()
            ff = torch.clamp(h, min=0)
            F = torch.fft.rfft(ff, n=nfft, dim=1)
            conv = torch.fft.irfft(F * F, n=nfft, dim=1)[:, :nc]
            c_sq = torch.sum(conv * conv, dim=1)
            c_shift = torch.sum(conv[:, :-1] * conv[:, 1:], dim=1)
            c_sum = torch.sum(conv, dim=1)
            c_max = torch.max(conv, dim=1).values
            C = (2 * c_sq + c_shift) / (3 * c_sum * c_max + 1e-30)
            (-C).backward()
            opt.step()
            with torch.no_grad():
                h.clamp_(min=0)

            if (t + 1) % 2000 == 0:
                cv = C.item()
                if cv > best_s and cv < 1.0:
                    best_s = cv
                    best_f = h[0].detach().cpu().numpy().copy()
                    best_f = np.maximum(best_f, 0)
                print(f"    iter {t+1}: C={best_s:.8f}")

        verified = fast_evaluate(best_f)
        print(f"  Arcsine+Adam n={n}: C={verified:.8f}")
        results.append((f"arcsine_adam_n{n}", verified, best_f))

    # Ranking
    results.sort(key=lambda x: x[1], reverse=True)
    print(f"\n{'='*60}")
    print("Top 10:")
    for name, score, _ in results[:10]:
        print(f"  {score:.8f}  {name}")

    best_name, best_score, best_f = results[0]
    d = diagnose(best_f)
    print(f"\nBEST: {best_name}, C={best_score:.8f}")
    print(f"  n={len(best_f)}, nnz={d['nnz']}, blocks={d['n_blocks']}")
    save_result(best_f, best_score, "chebyshev_final")


if __name__ == "__main__":
    main()
