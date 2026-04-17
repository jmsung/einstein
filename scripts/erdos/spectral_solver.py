"""Spectral-domain solver for Erdős Minimum Overlap.

Key mathematical insight:
  C(t) = sum(h) - autocorr_h(t), scaled by 2/n
  So max_t C(t) = sum(h)*2/n - min_t autocorr_h(t)*2/n = 1 - min_t autocorr(t)*2/n

We want to minimize max_t C(t) = minimize (1 - min_t autocorr(t)*2/n)
= maximize min_t autocorr_h(t) * 2/n

Now, autocorr_h(t) = IDFT(|H(w)|^2) where H = DFT(h).

So we want: max min_t IDFT(|H(w)|^2)(t)

This is a spectral flatness problem: we want |H(w)|^2 to be such that
its inverse DFT (= the autocorrelation) is as FLAT as possible from below.

For perfectly flat autocorrelation, |H(w)|^2 = const, meaning h has flat
power spectrum. This gives autocorr(t) = const for t=0,...,n-1.

But we also need h ∈ [0,1] and sum(h) = n/2. The challenge is finding
h with flat power spectrum AND bounded values.

This script optimizes in the spectral domain, using the power spectrum
as the optimization variable.
"""

import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from scipy.signal import fftconvolve
from scipy.optimize import minimize as scipy_minimize

from einstein.erdos.fast import fast_evaluate
from einstein.erdos.evaluator import evaluate as exact_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")


def fast_eval(h):
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    if n == 0:
        return float("inf")
    h = np.clip(h, 0, 1)
    s = np.sum(h)
    if s == 0:
        return float("inf")
    h = h * (n / 2.0 / s)
    if np.any(h > 1.0):
        return float("inf")
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def normalize(h):
    h = np.clip(h, 0, 1)
    n = len(h)
    s = np.sum(h)
    if s > 0:
        h = h * (n / 2.0 / s)
    h = np.clip(h, 0, 1)
    return h


def analyze_solution(h, label=""):
    """Analyze spectral properties of a solution."""
    n = len(h)
    h_norm = normalize(h.copy())
    score = fast_eval(h_norm)

    # Autocorrelation
    corr = fftconvolve(h_norm, h_norm[::-1], mode="full")
    autocorr = corr[n-1:]  # lags 0 to n-1

    # Cross-correlation with 1-h
    cross = fftconvolve(h_norm, (1.0 - h_norm)[::-1], mode="full")

    # Power spectrum
    H = np.fft.rfft(h_norm)
    power = np.abs(H) ** 2

    # Equioscillation analysis
    max_cross = np.max(cross)
    threshold = max_cross - 1e-8 * n
    active_lags = np.sum(cross >= threshold)

    print(f"\n{label} Analysis:")
    print(f"  Score: {score:.16f}")
    print(f"  Autocorr range: [{autocorr.min():.6f}, {autocorr.max():.6f}]")
    print(f"  Autocorr std: {autocorr[1:].std():.6f}")
    print(f"  Power spectrum range: [{power[1:].min():.2f}, {power[1:].max():.2f}]")
    print(f"  Power spectrum CV: {power[1:].std()/power[1:].mean():.4f}")
    print(f"  Active lags (equioscillation): {active_lags}/{len(cross)}")

    return score, autocorr, power


def spectral_optimizer(n=600, n_iters=10000, lr=0.01, time_limit=300, seed=0):
    """Optimize power spectrum to flatten autocorrelation from below.

    Strategy: parameterize h via phase-only reconstruction.
    Given a target flat power spectrum P(w) = const, find phases phi(w)
    such that h = IDFT(sqrt(P) * exp(i*phi)) ∈ [0,1].

    The phases control the time-domain shape of h.
    """
    import torch
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    dtype = torch.float32
    torch.manual_seed(seed)

    n_freq = n // 2 + 1
    best_score = float("inf")
    best_h = None
    t0 = time.time()

    # Try multiple initializations
    for trial in range(20):
        if time.time() - t0 > time_limit:
            break

        # Parameters: log-power spectrum and phases
        log_power = torch.zeros(n_freq, device=device, dtype=dtype)
        phases = torch.randn(n_freq, device=device, dtype=dtype) * np.pi
        phases[0] = torch.tensor(0.0)  # DC is real

        log_power.requires_grad_(True)
        phases.requires_grad_(True)
        opt = torch.optim.Adam([log_power, phases], lr=lr)

        trial_best = float("inf")

        for it in range(n_iters // 20):
            if time.time() - t0 > time_limit:
                break

            opt.zero_grad()

            # Construct H(w) = sqrt(exp(log_power)) * exp(i*phases)
            magnitude = torch.exp(log_power / 2)
            H = magnitude * torch.exp(1j * phases)

            # Inverse FFT to get h
            h = torch.fft.irfft(H, n=n)

            # Soft clamp to [0, 1] using sigmoid
            h = torch.sigmoid(5 * (h - 0.5)) * 0.98 + 0.01

            # Normalize
            s = h.sum()
            h = h * (n / 2.0) / (s + 1e-10)
            h = torch.clamp(h, 0, 1)

            # Compute score via FFT correlation
            h_batch = h.unsqueeze(0)
            omh = 1.0 - h_batch
            nc = 2 * n - 1
            nfft = 1
            while nfft < nc:
                nfft <<= 1
            Hf = torch.fft.rfft(h_batch, n=nfft, dim=1)
            Gf = torch.fft.rfft(omh.flip(1), n=nfft, dim=1)
            corr = torch.fft.irfft(Hf * Gf, n=nfft, dim=1)[:, :nc]
            C = corr.max(dim=1).values * 2.0 / n

            # Add penalty for being far from [0,1]
            penalty = torch.relu(-h).sum() + torch.relu(h - 1).sum()
            loss = C + 0.01 * penalty

            loss.backward()
            opt.step()

            with torch.no_grad():
                score = C.item()
                if score < trial_best:
                    trial_best = score

        # Extract best from this trial
        with torch.no_grad():
            magnitude = torch.exp(log_power / 2)
            H = magnitude * torch.exp(1j * phases)
            h = torch.fft.irfft(H, n=n)
            h = torch.sigmoid(5 * (h - 0.5)) * 0.98 + 0.01
            h_np = h.cpu().numpy().astype(np.float64)
            h_np = normalize(h_np)
            score = fast_eval(h_np)

            if score < best_score:
                best_score = score
                best_h = h_np.copy()

        if (trial + 1) % 5 == 0:
            print(f"  trial {trial+1}: trial_best={trial_best:.10f}, "
                  f"global_best={best_score:.10f}")

    return best_h, best_score


def gradient_masking_optimizer(h_init, n_iters=50000, time_limit=300, seed=0):
    """Novel approach: mask gradient updates to only modify non-equioscillation lags.

    The SOTA has 437 lags at equioscillation. These create a 'wall' that gradient
    methods can't penetrate. But what if we focus on reducing the SECOND-highest
    lag first, creating a 'gap' in the equioscillation?

    Strategy: identify the top-K contributing lags, temporarily ignore the top lag
    in the loss, and try to reduce all others. If successful, the max might shift
    to a new (lower) lag.
    """
    import torch
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    dtype = torch.float32
    torch.manual_seed(seed)

    n = len(h_init)
    best_score = fast_eval(h_init)
    best_h = h_init.copy()
    t0 = time.time()

    for k_ignore in [1, 5, 10, 50, 100, 200, 437]:
        if time.time() - t0 > time_limit:
            break

        h = torch.tensor(h_init, dtype=dtype, device=device).unsqueeze(0)
        h.requires_grad_(True)
        opt = torch.optim.Adam([h], lr=0.001)

        for it in range(n_iters // 7):
            if time.time() - t0 > time_limit:
                break

            opt.zero_grad()

            hc = torch.clamp(h, 0, 1)
            s = hc.sum(dim=1, keepdim=True)
            hc = hc * (n / 2.0) / (s + 1e-30)
            hc = torch.clamp(hc, 0, 1)

            omh = 1.0 - hc
            nc = 2 * n - 1
            nfft = 1
            while nfft < nc:
                nfft <<= 1
            H = torch.fft.rfft(hc, n=nfft, dim=1)
            G = torch.fft.rfft(omh.flip(1), n=nfft, dim=1)
            corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]

            # Mask top-k lags
            with torch.no_grad():
                corr_np = corr[0].cpu().numpy()
                top_k_idx = np.argsort(corr_np)[-k_ignore:]
                mask = torch.ones(nc, device=device, dtype=dtype)
                mask[top_k_idx] = 0.0

            # Loss = max of MASKED correlation
            masked_corr = corr * mask.unsqueeze(0)
            C = masked_corr.max(dim=1).values * 2.0 / n

            C.backward()
            opt.step()
            with torch.no_grad():
                h.clamp_(0, 1)

        # Evaluate actual score
        with torch.no_grad():
            h_np = h[0].cpu().numpy().astype(np.float64)
            h_np = normalize(h_np)
            score = fast_eval(h_np)
            if score < best_score:
                best_score = score
                best_h = h_np.copy()
                print(f"  k_ignore={k_ignore}: NEW BEST {score:.13f}")
            else:
                print(f"  k_ignore={k_ignore}: {score:.13f}")

    return best_h, best_score


def main():
    print("=" * 70)
    print("SPECTRAL SOLVER: Erdős Minimum Overlap (Problem 1)")
    print("=" * 70)

    # Load SOTA
    sota_file = RESULTS_DIR / "sota_together_ai_id9_n600.json"
    with open(sota_file) as f:
        h_sota = np.array(json.load(f)["values"], dtype=np.float64)

    # Analyze SOTA
    print("\n--- SOTA Solution Analysis ---")
    analyze_solution(h_sota, "SOTA")

    results = {}

    # 1. Spectral optimizer
    print("\n--- Spectral optimizer ---")
    t0 = time.time()
    h1, s1 = spectral_optimizer(n=600, n_iters=10000, lr=0.01,
                                 time_limit=300, seed=42)
    print(f"  Spectral: {s1:.13f} ({time.time()-t0:.0f}s)")
    results["spectral"] = (h1, s1)
    if h1 is not None:
        analyze_solution(h1, "Spectral")

    # 2. Gradient masking
    print("\n--- Gradient masking optimizer ---")
    t0 = time.time()
    h2, s2 = gradient_masking_optimizer(h_sota, n_iters=50000,
                                         time_limit=300, seed=42)
    print(f"  Grad mask: {s2:.13f} ({time.time()-t0:.0f}s)")
    results["grad_mask"] = (h2, s2)

    # 3. Spectral at different n
    print("\n--- Spectral at different n ---")
    for n in [300, 400, 500, 800]:
        t0 = time.time()
        h3, s3 = spectral_optimizer(n=n, n_iters=5000, lr=0.01,
                                     time_limit=90, seed=42)
        print(f"  Spectral n={n}: {s3:.13f} ({time.time()-t0:.0f}s)")
        results[f"spectral_n{n}"] = (h3, s3)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY (sorted by score)")
    print("=" * 70)
    sota_score = fast_eval(h_sota)
    for name, (h, s) in sorted(results.items(), key=lambda x: x[1][1]):
        delta = sota_score - s
        marker = " *** BEATS SOTA ***" if s < sota_score - 1e-6 else ""
        print(f"  {name:25s} score={s:.13f} improve={delta:.2e}{marker}")


if __name__ == "__main__":
    main()
