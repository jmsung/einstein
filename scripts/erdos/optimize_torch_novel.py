"""Torch-based smooth optimization for Erdős Minimum Overlap.

Novel approaches:
1. Multi-frequency initialization (not from SOTA) with LogSumExp + Adam
2. Bilevel optimization: outer=architecture search, inner=gradient descent
3. Spectral constraint: optimize DFT magnitudes/phases directly
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
ARENA_SOTA = 0.3808703105862199
TARGET = ARENA_SOTA - 1e-6


def torch_score(h: torch.Tensor, beta: float = 1e5) -> torch.Tensor:
    """Differentiable scoring via FFT correlation + LogSumExp smooth max."""
    n = h.shape[0]
    # FFT-based correlation: corr = ifft(fft(h) * conj(fft(1-h)))
    H = torch.fft.rfft(h)
    G = torch.fft.rfft(1.0 - h)
    # Cross-correlation via FFT: need to compute correlate(h, 1-h, 'full')
    # Pad to avoid circular correlation artifacts
    n_fft = 2 * n - 1
    H_padded = torch.fft.rfft(h, n=n_fft)
    G_padded = torch.fft.rfft(1.0 - h, n=n_fft)
    # correlate(a, b) = ifft(fft(a) * conj(fft(b_reversed)))
    # But b_reversed's fft = conj(fft(b)) for real b
    corr = torch.fft.irfft(H_padded * G_padded.conj(), n=n_fft)
    corr_scaled = corr * 2.0 / n

    # LogSumExp smooth max
    c_max = corr_scaled.max()
    lse = c_max + torch.logsumexp(beta * (corr_scaled - c_max), dim=0) / beta
    return lse


def project_to_feasible(h: torch.Tensor) -> torch.Tensor:
    """Project to [0, 1] with sum = n/2."""
    n = h.shape[0]
    h = h.clamp(0, 1)
    target = n / 2.0
    s = h.sum()
    if s > 0:
        h = h * (target / s)
    h = h.clamp(0, 1)
    s = h.sum()
    if s > 0:
        h = h * (target / s)
    return h


def approach_torch_multistart(n: int = 600, n_starts: int = 20, n_iters: int = 5000,
                               lr: float = 1e-3):
    """Multi-start Adam optimization from diverse initializations."""
    print("\n" + "=" * 60)
    print("TORCH APPROACH 1: Multi-start Adam + LogSumExp")
    print("=" * 60)

    best_overall = ARENA_SOTA
    best_h = None

    for start_idx in range(n_starts):
        rng = np.random.default_rng(start_idx * 7 + 13)
        x = np.linspace(0, 1, n, endpoint=False)

        # Diverse initialization strategies
        if start_idx < 5:
            # Random Fourier: sum of random sinusoids
            h_np = np.full(n, 0.5)
            K = rng.integers(5, 30)
            for k in range(1, K + 1):
                amp = rng.uniform(-0.4, 0.4) / np.sqrt(k)
                phase = rng.uniform(0, 2 * np.pi)
                h_np += amp * np.cos(2 * np.pi * k * x + phase)
        elif start_idx < 10:
            # Random binary-ish with smoothing
            h_np = (rng.random(n) > 0.5).astype(float)
            # Gaussian smooth
            from scipy.ndimage import gaussian_filter1d
            sigma = rng.uniform(2, 20)
            h_np = gaussian_filter1d(h_np, sigma)
        elif start_idx < 15:
            # Power-tent variants
            alpha = rng.uniform(0.3, 3.0)
            center = rng.uniform(0.3, 0.7)
            h_np = np.maximum(0, 1 - np.abs((x - center) / 0.4) ** alpha)
        else:
            # Pure random
            h_np = rng.random(n)

        h_np = np.clip(h_np, 0, 1)
        target = n / 2.0
        s = np.sum(h_np)
        if s > 0:
            h_np *= target / s
        h_np = np.clip(h_np, 0, 1)
        s = np.sum(h_np)
        if s > 0:
            h_np *= target / s

        init_score = fast_evaluate(h_np)

        # Optimize with Adam
        h_param = torch.tensor(h_np, dtype=torch.float64, requires_grad=True)
        optimizer = torch.optim.Adam([h_param], lr=lr)

        best_local = init_score
        best_local_h = h_np.copy()

        for it in range(n_iters):
            # Anneal beta (temperature) for LogSumExp
            beta = 100 + (1e6 - 100) * min(1.0, it / (n_iters * 0.8))

            optimizer.zero_grad()
            h_proj = project_to_feasible(h_param)
            loss = torch_score(h_proj, beta=beta)
            loss.backward()

            # Project gradient to sum-preserving subspace
            if h_param.grad is not None:
                h_param.grad.data -= h_param.grad.data.mean()

            optimizer.step()

            # Project parameters
            with torch.no_grad():
                h_param.data = project_to_feasible(h_param.data)

            if (it + 1) % 1000 == 0:
                with torch.no_grad():
                    h_np_curr = h_param.detach().numpy()
                    s = fast_evaluate(h_np_curr)
                    if s < best_local:
                        best_local = s
                        best_local_h = h_np_curr.copy()

        # Final score
        h_np_final = h_param.detach().numpy()
        final_score = fast_evaluate(h_np_final)
        if final_score < best_local:
            best_local = final_score
            best_local_h = h_np_final.copy()

        print(f"  Start {start_idx}: init={init_score:.8f} -> final={best_local:.8f}")

        if best_local < best_overall:
            best_overall = best_local
            best_h = best_local_h.copy()

    print(f"\n  Best multi-start: {best_overall:.13f}")
    return best_h, best_overall


def approach_spectral_direct(n: int = 600, n_iters: int = 10000, lr: float = 1e-3):
    """Optimize DFT magnitudes and phases directly.

    h = IFFT(H) where H[0] = n/2, |H[k]| and angle(H[k]) are optimized.
    Constraint: h in [0,1] enforced via penalty.
    """
    print("\n" + "=" * 60)
    print("TORCH APPROACH 2: Direct spectral optimization")
    print("=" * 60)

    # Load SOTA and extract its spectrum
    sota_path = RESULTS_DIR / "sota_rank1_Together-AI_0.380870310586.json"
    with open(sota_path) as f:
        sol = json.load(f)
    h_sota = np.array(sol["data"]["values"], dtype=np.float64)

    H_sota = np.fft.rfft(h_sota)
    mags_init = np.abs(H_sota[1:])  # Skip DC (fixed at n/2)
    phases_init = np.angle(H_sota[1:])

    K = len(mags_init)  # n//2 components
    print(f"  Spectral components: K={K}")
    print(f"  Top 5 magnitudes: {sorted(mags_init, reverse=True)[:5]}")

    # Initialize from SOTA spectrum with small perturbation
    rng = np.random.default_rng(42)

    best_overall = ARENA_SOTA
    best_h = None

    for trial in range(5):
        mags = torch.tensor(mags_init + rng.normal(0, 0.1, K), dtype=torch.float64, requires_grad=True)
        phases = torch.tensor(phases_init + rng.normal(0, 0.1, K), dtype=torch.float64, requires_grad=True)

        optimizer = torch.optim.Adam([mags, phases], lr=lr)

        for it in range(n_iters):
            optimizer.zero_grad()

            # Reconstruct H
            H = torch.zeros(K + 1, dtype=torch.complex128)
            H[0] = n / 2.0  # DC component (sum constraint)
            H[1:] = mags.abs() * torch.exp(1j * phases)

            # IFFT to get h
            h = torch.fft.irfft(H, n=n)

            # Box constraint via penalty
            penalty_lo = torch.relu(-h).pow(2).sum() * 1e4
            penalty_hi = torch.relu(h - 1.0).pow(2).sum() * 1e4

            # Score
            h_clamped = h.clamp(0, 1)
            target = n / 2.0
            s = h_clamped.sum()
            if s > 0:
                h_clamped = h_clamped * (target / s)
            h_clamped = h_clamped.clamp(0, 1)

            beta = 100 + (1e5 - 100) * min(1.0, it / (n_iters * 0.8))
            score = torch_score(h_clamped, beta=beta)

            loss = score + penalty_lo + penalty_hi
            loss.backward()
            optimizer.step()

            if (it + 1) % 2000 == 0:
                with torch.no_grad():
                    h_np = h_clamped.detach().numpy()
                    s = fast_evaluate(h_np)
                    print(f"    trial {trial}, iter {it+1}: C={s:.10f}, "
                          f"penalty={float(penalty_lo + penalty_hi):.2e}")

        # Final evaluation
        with torch.no_grad():
            H = torch.zeros(K + 1, dtype=torch.complex128)
            H[0] = n / 2.0
            H[1:] = mags.abs() * torch.exp(1j * phases)
            h_final = torch.fft.irfft(H, n=n).numpy()
            h_final = np.clip(h_final, 0, 1)
            target = n / 2.0
            h_final *= target / np.sum(h_final)
            h_final = np.clip(h_final, 0, 1)
            h_final *= target / np.sum(h_final)

        final_score = fast_evaluate(h_final)
        print(f"  Trial {trial}: final C={final_score:.13f}")

        if final_score < best_overall:
            best_overall = final_score
            best_h = h_final.copy()

    print(f"\n  Best spectral: {best_overall:.13f}")
    return best_h, best_overall


def approach_large_perturbation_basin_hop(n: int = 600, n_hops: int = 50,
                                          polish_iters: int = 3000):
    """Large perturbation + gradient polish to escape current basin."""
    print("\n" + "=" * 60)
    print("TORCH APPROACH 3: Large perturbation basin hopping")
    print("=" * 60)

    sota_path = RESULTS_DIR / "sota_rank1_Together-AI_0.380870310586.json"
    with open(sota_path) as f:
        sol = json.load(f)
    h_sota = np.array(sol["data"]["values"], dtype=np.float64)

    best_overall = ARENA_SOTA
    best_h = None

    for hop in range(n_hops):
        rng = np.random.default_rng(hop * 31 + 7)

        # Large structured perturbation
        perturb_type = hop % 5
        h = h_sota.copy()

        if perturb_type == 0:
            # Shuffle a random segment
            seg_start = rng.integers(0, n - 100)
            seg_len = rng.integers(20, 100)
            seg = h[seg_start:seg_start+seg_len].copy()
            rng.shuffle(seg)
            h[seg_start:seg_start+seg_len] = seg

        elif perturb_type == 1:
            # Add random Fourier component
            x = np.linspace(0, 1, n, endpoint=False)
            k = rng.integers(1, 50)
            amp = rng.uniform(0.05, 0.3)
            phase = rng.uniform(0, 2 * np.pi)
            h += amp * np.cos(2 * np.pi * k * x + phase)

        elif perturb_type == 2:
            # Flip random region
            seg_start = rng.integers(0, n - 50)
            seg_len = rng.integers(10, 50)
            h[seg_start:seg_start+seg_len] = 1.0 - h[seg_start:seg_start+seg_len]

        elif perturb_type == 3:
            # Random Gaussian noise
            h += rng.normal(0, 0.1, n)

        elif perturb_type == 4:
            # Swap two random segments
            s1 = rng.integers(0, n - 50)
            s2 = rng.integers(0, n - 50)
            L = rng.integers(10, 50)
            h[s1:s1+L], h[s2:s2+L] = h[s2:s2+L].copy(), h[s1:s1+L].copy()

        # Project
        h = np.clip(h, 0, 1)
        target = n / 2.0
        h *= target / np.sum(h)
        h = np.clip(h, 0, 1)
        h *= target / np.sum(h)

        perturbed_score = fast_evaluate(h)

        # Polish with Adam
        h_param = torch.tensor(h, dtype=torch.float64, requires_grad=True)
        optimizer = torch.optim.Adam([h_param], lr=5e-4)

        best_local = perturbed_score
        for it in range(polish_iters):
            optimizer.zero_grad()
            h_proj = project_to_feasible(h_param)
            beta = 1000 + (1e5 - 1000) * min(1.0, it / (polish_iters * 0.7))
            loss = torch_score(h_proj, beta=beta)
            loss.backward()
            if h_param.grad is not None:
                h_param.grad.data -= h_param.grad.data.mean()
            optimizer.step()
            with torch.no_grad():
                h_param.data = project_to_feasible(h_param.data)

        h_final = h_param.detach().numpy()
        final_score = fast_evaluate(h_final)
        if final_score < best_local:
            best_local = final_score

        if hop % 10 == 0 or best_local < best_overall:
            print(f"  Hop {hop}: type={perturb_type}, perturbed={perturbed_score:.8f}, "
                  f"polished={best_local:.8f}")

        if best_local < best_overall:
            best_overall = best_local
            best_h = h_final.copy()

    print(f"\n  Best basin hop: {best_overall:.13f}")
    return best_h, best_overall


def main():
    t_start = time.time()

    print("=" * 60)
    print("Erdős Minimum Overlap — Torch-based Novel Approaches")
    print(f"SOTA: {ARENA_SOTA:.16f}")
    print(f"TARGET: {TARGET:.16f}")
    print("=" * 60)

    results = {}

    # Approach 1: Multi-start Adam
    t0 = time.time()
    h1, s1 = approach_torch_multistart(n=600, n_starts=20, n_iters=5000, lr=1e-3)
    results["multistart_adam"] = (s1, time.time() - t0)

    # Approach 2: Direct spectral optimization
    t0 = time.time()
    h2, s2 = approach_spectral_direct(n=600, n_iters=10000, lr=1e-3)
    results["spectral_direct"] = (s2, time.time() - t0)

    # Approach 3: Basin hopping
    t0 = time.time()
    h3, s3 = approach_large_perturbation_basin_hop(n=600, n_hops=50, polish_iters=3000)
    results["basin_hop"] = (s3, time.time() - t0)

    # Summary
    elapsed = time.time() - t_start
    print("\n" + "=" * 60)
    print("TORCH SUMMARY")
    print("=" * 60)
    print(f"{'Approach':<20} {'Score':<20} {'vs SOTA':<15} {'Time':<10}")
    print("-" * 65)
    for name, (score, t) in sorted(results.items(), key=lambda x: x[1][0]):
        diff = score - ARENA_SOTA
        status = "BEATS!" if score < TARGET else "no"
        print(f"{name:<20} {score:.13f}  {diff:+.2e}  {t:.0f}s  {status}")

    best_name = min(results, key=lambda k: results[k][0])
    best_score = results[best_name][0]

    print(f"\nBest: {best_name} = {best_score:.16f}")
    print(f"Beats SOTA by 1e-6? {'YES' if best_score < TARGET else 'NO'}")
    print(f"Total time: {elapsed:.0f}s")

    # Save best
    all_results = [(h1, s1), (h2, s2), (h3, s3)]
    best_idx = min(range(3), key=lambda i: all_results[i][1] if all_results[i][0] is not None else float("inf"))
    best_h, best_s = all_results[best_idx]

    if best_h is not None:
        out = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(best_h),
            "score": float(best_s),
            "values": best_h.tolist(),
            "approach": best_name,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"torch_novel_best_{best_s:.10f}.json"
        with open(fname, "w") as f:
            json.dump(out, f)
        print(f"\nSaved: {fname}")


if __name__ == "__main__":
    main()
