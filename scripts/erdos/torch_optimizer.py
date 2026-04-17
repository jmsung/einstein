"""Torch-based optimizer for Erdős Minimum Overlap with temperature annealing.

Uses autograd through FFT-based correlation and LogSumExp smooth max.
Starts with tight temperature, anneals tighter over training.
"""

import json
import time
import numpy as np
import torch
from scipy.signal import fftconvolve

import sys
sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate
from einstein.erdos.fast import fast_evaluate


def torch_correlate(h: torch.Tensor) -> torch.Tensor:
    """Compute correlate(h, 1-h, 'full') using FFT."""
    n = h.shape[0]
    one_minus_h = 1.0 - h
    # Cross-correlation via FFT
    pad_size = 2 * n - 1
    H = torch.fft.rfft(h, n=pad_size)
    G = torch.fft.rfft(one_minus_h.flip(0), n=pad_size)
    corr = torch.fft.irfft(H * G, n=pad_size)
    return corr[:2 * n - 1]


def smooth_max(x: torch.Tensor, temperature: float) -> torch.Tensor:
    """LogSumExp smooth approximation to max."""
    return temperature * torch.logsumexp(x / temperature, dim=0)


def optimize_torch(h_init: np.ndarray, lr: float = 1e-5,
                    max_iters: int = 50000, temp_start: float = 1e-3,
                    temp_end: float = 1e-6, label: str = "") -> tuple[float, np.ndarray]:
    """Optimize h using torch autograd with smooth max."""
    n = len(h_init)
    device = torch.device('cpu')

    # Parametrize in unconstrained space via sigmoid
    # h = sigmoid(u), then normalize sum
    h0 = torch.tensor(h_init, dtype=torch.float64, device=device)
    # Initialize u from h: u = logit(h)
    h_clipped = torch.clamp(h0, 1e-8, 1 - 1e-8)
    u = torch.log(h_clipped / (1 - h_clipped))
    u.requires_grad_(True)

    optimizer = torch.optim.Adam([u], lr=lr)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=max_iters)

    best_score = float('inf')
    best_h = h_init.copy()

    t0 = time.time()
    for it in range(max_iters):
        optimizer.zero_grad()

        # Map to h via sigmoid
        h = torch.sigmoid(u)
        # Normalize sum to n/2
        h = h * (n / 2.0) / h.sum()

        # Temperature annealing (log-linear)
        frac = it / max(max_iters - 1, 1)
        temp = temp_start * (temp_end / temp_start) ** frac

        # Compute correlation
        corr = torch_correlate(h)
        C = corr * 2.0 / n

        # Smooth max loss
        loss = smooth_max(C, temp)

        loss.backward()
        optimizer.step()
        scheduler.step()

        # Check actual score periodically
        if (it + 1) % 5000 == 0 or it == max_iters - 1:
            with torch.no_grad():
                h_np = torch.sigmoid(u).numpy()
                h_np = np.clip(h_np, 0, 1)
                s = np.sum(h_np)
                if s > 0:
                    h_np = h_np * (n / 2.0 / s)
                h_np = np.clip(h_np, 0, 1)
                s = np.sum(h_np)
                if s > 0:
                    h_np = h_np * (n / 2.0 / s)

                score = fast_evaluate(h_np)
                if score < best_score:
                    best_score = score
                    best_h = h_np.copy()

                elapsed = time.time() - t0
                print(f"  [{label}] iter {it+1}/{max_iters}: loss={loss.item():.10f} "
                      f"score={score:.12f} best={best_score:.12f} temp={temp:.2e} "
                      f"time={elapsed:.0f}s")

    return best_score, best_h


def optimize_direct_params(h_init: np.ndarray, lr: float = 1e-6,
                            max_iters: int = 100000,
                            label: str = "") -> tuple[float, np.ndarray]:
    """Direct parametrization with projected gradient descent."""
    n = len(h_init)
    h = torch.tensor(h_init, dtype=torch.float64, requires_grad=True)

    optimizer = torch.optim.Adam([h], lr=lr)

    best_score = fast_evaluate(h_init)
    best_h = h_init.copy()

    t0 = time.time()
    for it in range(max_iters):
        optimizer.zero_grad()

        # Normalize sum
        h_norm = h * (n / 2.0) / h.sum()

        # Correlation via FFT
        corr = torch_correlate(h_norm)
        C = corr * 2.0 / n

        # Use tight smooth max
        temp = 1e-5
        loss = smooth_max(C, temp)

        loss.backward()
        optimizer.step()

        # Project h back to [0, 1]
        with torch.no_grad():
            h.data.clamp_(0, 1)

        if (it + 1) % 10000 == 0:
            with torch.no_grad():
                h_np = h.numpy().copy()
                h_np = np.clip(h_np, 0, 1)
                h_np *= n / 2.0 / np.sum(h_np)
                h_np = np.clip(h_np, 0, 1)
                h_np *= n / 2.0 / np.sum(h_np)
                score = fast_evaluate(h_np)
                if score < best_score:
                    best_score = score
                    best_h = h_np.copy()
                elapsed = time.time() - t0
                print(f"  [{label}] iter {it+1}: score={score:.12f} best={best_score:.12f} "
                      f"time={elapsed:.0f}s")

    return best_score, best_h


def polish_mass_transport(h: np.ndarray, iters: int = 500000,
                           seed: int = 42) -> tuple[float, np.ndarray]:
    """Mass transport polishing."""
    n = len(h)
    best_score = fast_evaluate(h)
    best_h = h.copy()
    rng = np.random.default_rng(seed)
    improved = 0

    for it in range(iters):
        k = rng.integers(2, 5)
        indices = rng.choice(n, k, replace=False)
        deltas = rng.standard_normal(k) * rng.choice([1e-9, 1e-8, 1e-7, 1e-6])
        deltas -= np.mean(deltas)

        h_new = h.copy()
        h_new[indices] += deltas
        if np.any(h_new < 0) or np.any(h_new > 1):
            continue

        score = fast_evaluate(h_new)
        if score < best_score:
            best_score = score
            h = h_new
            best_h = h.copy()
            improved += 1

        if (it + 1) % 100000 == 0:
            print(f"    polish iter {it+1}: {best_score:.14f} ({improved} imp)")

    return best_score, best_h


def main():
    print("=" * 60)
    print("Erdős Minimum Overlap — Torch Differentiable Optimizer")
    print("=" * 60)

    with open('/tmp/p1_sota.json') as f:
        sota_data = json.load(f)
    h_sota = np.array(sota_data['values'])
    print(f"SOTA: {fast_evaluate(h_sota):.16f}")

    overall_best = fast_evaluate(h_sota)
    overall_best_h = h_sota.copy()

    # Run 1: Sigmoid parametrization from SOTA, tight temperature
    print("\n--- Run 1: Sigmoid param, tight temp, from SOTA ---")
    s1, h1 = optimize_torch(h_sota, lr=1e-5, max_iters=30000,
                             temp_start=1e-4, temp_end=1e-7, label="sigmoid-tight")
    if s1 < overall_best:
        overall_best, overall_best_h = s1, h1
        print(f"  *** New best: {s1:.14f}")

    # Run 2: Direct param from SOTA
    print("\n--- Run 2: Direct param, projected gradient ---")
    s2, h2 = optimize_direct_params(h_sota, lr=1e-7, max_iters=50000, label="direct")
    if s2 < overall_best:
        overall_best, overall_best_h = s2, h2
        print(f"  *** New best: {s2:.14f}")

    # Run 3: Sigmoid from perturbed starts
    print("\n--- Run 3: Perturbed starts ---")
    rng = np.random.default_rng(1234)
    for trial in range(3):
        noise = rng.standard_normal(len(h_sota)) * 0.02
        h_start = np.clip(h_sota + noise, 0, 1)
        h_start *= 300 / np.sum(h_start)
        h_start = np.clip(h_start, 0, 1)
        h_start *= 300 / np.sum(h_start)

        s, h = optimize_torch(h_start, lr=5e-5, max_iters=20000,
                               temp_start=1e-3, temp_end=1e-6,
                               label=f"perturb-{trial}")
        if s < overall_best:
            overall_best, overall_best_h = s, h
            print(f"  *** New best: {s:.14f}")

    # Run 4: Fourier parametrization
    print("\n--- Run 4: Fourier param (cosine series) ---")
    n = 600
    K = 100  # number of Fourier modes
    x = np.linspace(0, 2, n, endpoint=False)
    # Initialize coefficients from SOTA's DFT
    h_centered = h_sota - 0.5
    dft = np.fft.rfft(h_centered)
    a_init = np.real(dft[:K]) / n * 2
    b_init = -np.imag(dft[:K]) / n * 2

    a = torch.tensor(a_init, dtype=torch.float64, requires_grad=True)
    b = torch.tensor(b_init, dtype=torch.float64, requires_grad=True)

    optimizer = torch.optim.Adam([a, b], lr=1e-5)
    basis_cos = torch.zeros(K, n, dtype=torch.float64)
    basis_sin = torch.zeros(K, n, dtype=torch.float64)
    for k in range(K):
        basis_cos[k] = torch.tensor(np.cos(np.pi * k * x))
        basis_sin[k] = torch.tensor(np.sin(np.pi * k * x))

    best_fourier = float('inf')
    best_fourier_h = None
    t0 = time.time()

    for it in range(30000):
        optimizer.zero_grad()

        # Reconstruct h
        h_recon = 0.5 + (a.unsqueeze(1) * basis_cos + b.unsqueeze(1) * basis_sin).sum(0)
        h_clamp = torch.clamp(h_recon, 0, 1)
        h_norm = h_clamp * (n / 2.0) / h_clamp.sum()

        corr = torch_correlate(h_norm)
        C = corr * 2.0 / n

        temp = 1e-4 * (1e-7 / 1e-4) ** (it / 29999)
        loss = smooth_max(C, temp)
        loss.backward()
        optimizer.step()

        if (it + 1) % 5000 == 0:
            with torch.no_grad():
                h_np = h_norm.numpy().copy()
                h_np = np.clip(h_np, 0, 1)
                h_np *= 300 / np.sum(h_np)
                h_np = np.clip(h_np, 0, 1)
                h_np *= 300 / np.sum(h_np)
                score = fast_evaluate(h_np)
                if score < best_fourier:
                    best_fourier = score
                    best_fourier_h = h_np.copy()
                elapsed = time.time() - t0
                print(f"  [fourier K={K}] iter {it+1}: score={score:.12f} "
                      f"best={best_fourier:.12f} time={elapsed:.0f}s")

    if best_fourier < overall_best:
        overall_best, overall_best_h = best_fourier, best_fourier_h
        print(f"  *** New best from Fourier: {best_fourier:.14f}")

    # Polish the overall best
    print(f"\n--- Polish best ({overall_best:.14f}) ---")
    sp, hp = polish_mass_transport(overall_best_h, iters=500000, seed=7777)
    if sp < overall_best:
        overall_best, overall_best_h = sp, hp

    # Final verification
    exact = evaluate({"values": overall_best_h.tolist()})
    print(f"\n{'='*60}")
    print(f"FINAL RESULT")
    print(f"Best (fast):  {overall_best:.16f}")
    print(f"Best (exact): {exact:.16f}")
    print(f"SOTA:         0.3808703105862199")
    print(f"Improvement:  {0.3808703105862199 - exact:.2e}")
    print(f"Need >= 1e-6: {'YES!' if 0.3808703105862199 - exact >= 1e-6 else 'NO'}")

    with open('/tmp/p1_torch_best.json', 'w') as f:
        json.dump({"values": overall_best_h.tolist()}, f)


if __name__ == "__main__":
    main()
