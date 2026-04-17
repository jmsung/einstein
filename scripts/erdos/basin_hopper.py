"""Basin-hopping and population-based optimizer for Erdős Minimum Overlap (P1).

Goal: escape the current SOTA basin (C ≈ 0.3809) and find a DIFFERENT basin
that might be globally better. Three methods run in sequence:

  Method 1: Large perturbation + polish (basin hopping from SOTA)
  Method 2: Population-based search (diverse cold starts → Adam polish)
  Method 3: Simulated annealing with large structural moves

Saves the best solution found to /tmp/p1_basin_best.json.

Usage:
    cd /Users/jmsung/projects/einstein/cb-feat-auto-p1
    uv run python3 scripts/erdos/basin_hopper.py
"""

import json
import os
import sys
import time
import warnings
from functools import partial
from pathlib import Path

# Suppress noisy torch warnings about tensor resizing
warnings.filterwarnings("ignore", message=".*was resized since it had shape.*")
os.environ["PYTHONUNBUFFERED"] = "1"

import numpy as np
import torch
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

# Force unbuffered output
print = partial(print, flush=True)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
N = 600
TARGET_SUM = N / 2.0
SOTA_SCORE = 0.3808703105862199
OUTPUT_PATH = Path("/tmp/p1_basin_best.json")

# Global tracker for discovered basins
basins: list[dict] = []  # {score, h, correlation_with_sota, method}

# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------


def project(h: np.ndarray) -> np.ndarray:
    """Project h onto feasible set: h in [0,1], sum = n/2."""
    h = np.clip(h, 0.0, 1.0)
    s = h.sum()
    if s > 0:
        h = h * (TARGET_SUM / s)
    h = np.clip(h, 0.0, 1.0)
    return h


def correlation(a: np.ndarray, b: np.ndarray) -> float:
    """Pearson correlation between two vectors."""
    a_c = a - a.mean()
    b_c = b - b.mean()
    denom = np.sqrt((a_c ** 2).sum() * (b_c ** 2).sum())
    if denom < 1e-15:
        return 0.0
    return float((a_c * b_c).sum() / denom)


def generate_sota_proxy() -> np.ndarray:
    """Generate a proxy for the SOTA solution.

    Since we don't have the actual SOTA file, we cold-start Adam and take
    the best result. This function generates a known good construction
    (Haugland-style 3-piece piecewise linear) as the starting reference.
    """
    # Haugland-style construction: piecewise linear
    # h(x) ≈ 1 for x in [0, 0.5], linear decrease for x in [0.5, 1.5], 0 for [1.5, 2]
    x = np.linspace(0, 2, N, endpoint=False)
    h = np.zeros(N)
    for i, xi in enumerate(x):
        if xi < 0.5:
            h[i] = 1.0
        elif xi < 1.5:
            h[i] = 1.0 - (xi - 0.5)
        else:
            h[i] = 0.0
    return project(h)


def quick_adam_polish(h_init: np.ndarray, n_iters: int = 5000,
                      lr: float = 0.005, batch_size: int = 1,
                      time_limit: float = 30.0) -> tuple[np.ndarray, float]:
    """Polish a single solution with batched Adam (torch).

    Returns (best_h_numpy, best_score).
    """
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    dtype = torch.float32

    h_t = torch.tensor(h_init, dtype=dtype, device=device)
    if batch_size > 1:
        h = h_t.unsqueeze(0).repeat(batch_size, 1)
        # add small noise to extra copies
        noise = 0.005 * torch.randn(batch_size - 1, N, device=device, dtype=dtype)
        h[1:] += noise
    else:
        h = h_t.unsqueeze(0)

    h = h.clamp(0, 1)
    h.requires_grad_(True)
    optimizer = torch.optim.Adam([h], lr=lr)

    best_score = float("inf")
    best_h = None
    t0 = time.time()

    for t in range(n_iters):
        if time.time() - t0 > time_limit:
            break

        optimizer.zero_grad()
        # Compute C for batch
        B, Ni = h.shape
        hc = torch.clamp(h, 0, 1)
        s = hc.sum(dim=1, keepdim=True)
        hc = hc * (Ni / 2.0) / (s + 1e-30)
        hc = torch.clamp(hc, 0, 1)
        one_minus_h = 1.0 - hc

        nc = 2 * Ni - 1
        nfft = 1
        while nfft < nc:
            nfft <<= 1

        H = torch.fft.rfft(hc, n=nfft, dim=1)
        G = torch.fft.rfft(one_minus_h.flip(1), n=nfft, dim=1)
        corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]
        C = corr.max(dim=1).values * 2.0 / Ni

        loss = C.mean()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            h.clamp_(0, 1)
            s = h.sum(dim=1, keepdim=True)
            h.mul_(Ni / 2.0 / (s + 1e-30))
            h.clamp_(0, 1)

    # Extract best
    with torch.no_grad():
        hc = torch.clamp(h, 0, 1)
        s = hc.sum(dim=1, keepdim=True)
        hc = hc * (N / 2.0) / (s + 1e-30)
        hc = torch.clamp(hc, 0, 1)
        one_minus_h = 1.0 - hc
        nc = 2 * N - 1
        nfft = 1
        while nfft < nc:
            nfft <<= 1
        H = torch.fft.rfft(hc, n=nfft, dim=1)
        G = torch.fft.rfft(one_minus_h.flip(1), n=nfft, dim=1)
        corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]
        C = corr.max(dim=1).values * 2.0 / N
        best_idx = torch.argmin(C)
        best_score = C[best_idx].item()
        best_h = h[best_idx].detach().cpu().numpy().copy()

    best_h = np.clip(best_h, 0.0, 1.0)
    verified = fast_evaluate(best_h)
    return best_h, verified


def batched_adam_polish(h_inits: list[np.ndarray], n_iters: int = 10000,
                        lr: float = 0.005, time_limit: float = 120.0
                        ) -> list[tuple[np.ndarray, float]]:
    """Polish multiple solutions simultaneously with batched Adam.

    Args:
        h_inits: List of numpy arrays to polish.
        n_iters: Max iterations.
        lr: Learning rate.
        time_limit: Max seconds.

    Returns:
        List of (best_h, score) for each input.
    """
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    dtype = torch.float32
    B = len(h_inits)

    h = torch.stack([torch.tensor(hi, dtype=dtype, device=device) for hi in h_inits])
    h = h.clamp(0, 1)
    h.requires_grad_(True)
    optimizer = torch.optim.Adam([h], lr=lr)

    t0 = time.time()
    for t in range(n_iters):
        if time.time() - t0 > time_limit:
            break

        optimizer.zero_grad()
        Bi, Ni = h.shape
        hc = torch.clamp(h, 0, 1)
        s = hc.sum(dim=1, keepdim=True)
        hc = hc * (Ni / 2.0) / (s + 1e-30)
        hc = torch.clamp(hc, 0, 1)
        one_minus_hc = 1.0 - hc

        nc = 2 * Ni - 1
        nfft = 1
        while nfft < nc:
            nfft <<= 1

        H = torch.fft.rfft(hc, n=nfft, dim=1)
        G = torch.fft.rfft(one_minus_hc.flip(1), n=nfft, dim=1)
        corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]
        C = corr.max(dim=1).values * 2.0 / Ni

        loss = C.mean()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            h.clamp_(0, 1)
            s = h.sum(dim=1, keepdim=True)
            h.mul_(Ni / 2.0 / (s + 1e-30))
            h.clamp_(0, 1)

    # Extract results
    results = []
    with torch.no_grad():
        hc = torch.clamp(h, 0, 1)
        s = hc.sum(dim=1, keepdim=True)
        hc = hc * (N / 2.0) / (s + 1e-30)
        hc = torch.clamp(hc, 0, 1)
        for i in range(B):
            hi = hc[i].cpu().numpy().copy()
            hi = np.clip(hi, 0.0, 1.0)
            score = fast_evaluate(hi)
            results.append((hi, score))

    return results


def register_basin(h: np.ndarray, score: float, method: str,
                   ref_h: np.ndarray | None = None):
    """Register a discovered basin, computing correlation with reference."""
    corr = correlation(h, ref_h) if ref_h is not None else 0.0
    basins.append({
        "score": score,
        "h": h.copy(),
        "correlation_with_ref": corr,
        "method": method,
    })


def save_best():
    """Save the overall best solution to OUTPUT_PATH."""
    if not basins:
        return
    best = min(basins, key=lambda b: b["score"])
    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": N,
        "score": float(best["score"]),
        "values": best["h"].tolist(),
        "method": best["method"],
        "correlation_with_ref": best["correlation_with_ref"],
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "basins_found": len(basins),
    }
    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f)
    print(f"  Saved best to {OUTPUT_PATH}")


def print_basin_summary(ref_h: np.ndarray | None = None):
    """Print summary of all discovered basins."""
    print(f"\n{'=' * 70}")
    print(f"BASIN SUMMARY: {len(basins)} basins discovered")
    print(f"{'=' * 70}")
    sorted_basins = sorted(basins, key=lambda b: b["score"])
    for i, b in enumerate(sorted_basins[:20]):
        corr_str = f"corr={b['correlation_with_ref']:.3f}" if ref_h is not None else ""
        beat = " *** BEATS SOTA ***" if b["score"] < SOTA_SCORE else ""
        print(f"  #{i+1}: C={b['score']:.10f} {corr_str} [{b['method']}]{beat}")
    if len(sorted_basins) > 20:
        print(f"  ... and {len(sorted_basins) - 20} more")
    print(f"{'=' * 70}")


# ===========================================================================
# Method 1: Basin Hopping (large perturbation + polish)
# ===========================================================================

def method1_basin_hopping(ref_h: np.ndarray, time_limit: float = 1200.0):
    """Basin hopping: large perturbation from reference, then Adam polish.

    Tries many random perturbation scales to jump out of the current basin.
    """
    print("\n" + "=" * 70)
    print("METHOD 1: Basin Hopping (large perturbation + polish)")
    print("=" * 70)

    rng = np.random.default_rng(42)
    t0 = time.time()
    n_hops = 0
    sigmas = [0.05, 0.08, 0.10, 0.15, 0.20, 0.30, 0.40, 0.50]

    ref_score = fast_evaluate(ref_h)
    print(f"  Reference score: {ref_score:.10f}")

    # Collect candidates in batches for efficient Adam polishing
    batch_size = 16  # Process this many in parallel
    batch_candidates = []
    batch_meta = []

    while time.time() - t0 < time_limit:
        sigma = rng.choice(sigmas)

        # Several perturbation strategies
        strategy = rng.integers(4)

        if strategy == 0:
            # Gaussian perturbation
            perturbed = ref_h + sigma * rng.standard_normal(N)
        elif strategy == 1:
            # Block swap: swap two random blocks
            perturbed = ref_h.copy()
            block_len = rng.integers(N // 20, N // 4)
            i1 = rng.integers(N - block_len)
            i2 = rng.integers(N - block_len)
            perturbed[i1:i1 + block_len], perturbed[i2:i2 + block_len] = (
                perturbed[i2:i2 + block_len].copy(),
                perturbed[i1:i1 + block_len].copy(),
            )
            perturbed += sigma * 0.3 * rng.standard_normal(N)
        elif strategy == 2:
            # Circular shift + noise
            shift = rng.integers(N // 10, N // 2)
            perturbed = np.roll(ref_h, shift) + sigma * 0.5 * rng.standard_normal(N)
        else:
            # Flip/reverse sections
            perturbed = ref_h.copy()
            seg_len = rng.integers(N // 10, N // 3)
            start = rng.integers(N - seg_len)
            perturbed[start:start + seg_len] = perturbed[start:start + seg_len][::-1]
            perturbed += sigma * 0.3 * rng.standard_normal(N)

        perturbed = project(perturbed)
        batch_candidates.append(perturbed)
        batch_meta.append(f"hop_s{strategy}_sig{sigma:.2f}")
        n_hops += 1

        # Process batch when full or near time limit
        remaining = time_limit - (time.time() - t0)
        if len(batch_candidates) >= batch_size or (remaining < 60 and batch_candidates):
            polish_time = min(remaining * 0.7, 30.0 * len(batch_candidates))
            results = batched_adam_polish(
                batch_candidates, n_iters=8000, lr=0.005,
                time_limit=polish_time,
            )
            for (h_pol, score), meta in zip(results, batch_meta):
                register_basin(h_pol, score, f"M1:{meta}", ref_h)
                corr = correlation(h_pol, ref_h)
                if score < SOTA_SCORE:
                    print(f"  *** HOP {n_hops}: BEATS SOTA! C={score:.10f}, "
                          f"corr={corr:.3f} [{meta}]")
                elif n_hops <= 5 or score < SOTA_SCORE + 0.005:
                    print(f"  hop {n_hops}: C={score:.10f}, corr={corr:.3f} [{meta}]")

            batch_candidates = []
            batch_meta = []

        if n_hops % 50 == 0:
            elapsed = time.time() - t0
            best_so_far = min(basins, key=lambda b: b["score"])["score"] if basins else float("inf")
            print(f"  [{elapsed:.0f}s] hops={n_hops}, best={best_so_far:.10f}")

    print(f"  Method 1 done: {n_hops} hops in {time.time() - t0:.0f}s")
    save_best()


# ===========================================================================
# Method 2: Population-based search (diverse cold starts)
# ===========================================================================

def generate_diverse_starts(n_pop: int, rng: np.random.Generator,
                            ref_h: np.ndarray) -> list[np.ndarray]:
    """Generate diverse starting points using different constructions."""
    starts = []
    x = np.linspace(0, 2, N, endpoint=False)

    # 1. Random uniform (normalized)
    for _ in range(n_pop // 5):
        h = rng.random(N)
        starts.append(project(h))

    # 2. Perturbed reference at various scales
    for sigma in [0.05, 0.1, 0.2, 0.3, 0.5]:
        for _ in range(n_pop // 10):
            h = ref_h + sigma * rng.standard_normal(N)
            starts.append(project(h))

    # 3. Tent construction: h = max(0, 1 - |x - c|) for various c
    for c in np.linspace(0.5, 1.5, n_pop // 10):
        h = np.maximum(0, 1 - np.abs(x - c))
        starts.append(project(h))

    # 4. Parabolic constructions
    for c in np.linspace(0.5, 1.5, n_pop // 10):
        h = np.maximum(0, 1 - (x - c) ** 2)
        starts.append(project(h))

    # 5. Step function variants
    for frac in np.linspace(0.3, 0.7, n_pop // 10):
        h = np.zeros(N)
        h[:int(N * frac)] = 1.0
        # Smooth edges
        edge = N // 20
        for i in range(edge):
            h[int(N * frac) - edge + i] = 1.0 - i / edge
        starts.append(project(h))

    # 6. Fourier random: h = 0.5 + sum of random cosines
    for _ in range(n_pop // 5):
        h = np.full(N, 0.5)
        n_harmonics = rng.integers(3, 20)
        for k in range(1, n_harmonics + 1):
            amp = rng.uniform(0, 0.3) / k
            phase = rng.uniform(0, 2 * np.pi)
            h += amp * np.cos(2 * np.pi * k * x / 2.0 + phase)
        starts.append(project(h))

    # 7. Haugland-style piecewise linear (multiple breakpoints)
    for _ in range(n_pop // 10):
        n_breaks = rng.integers(3, 8)
        breaks = np.sort(rng.uniform(0, 2, n_breaks))
        vals = rng.uniform(0, 1, n_breaks)
        h = np.interp(x, breaks, vals)
        starts.append(project(h))

    # 8. Sigmoid-based constructions
    for _ in range(n_pop // 10):
        c = rng.uniform(0.5, 1.5)
        sharpness = rng.uniform(2, 20)
        h = 1.0 / (1.0 + np.exp(sharpness * (x - c)))
        starts.append(project(h))

    # 9. Triangular wave
    for period in [0.5, 1.0, 1.5, 2.0]:
        h = 1.0 - 2.0 * np.abs(((x / period) % 1.0) - 0.5)
        starts.append(project(h))

    # 10. Sawtooth variants
    for period in [0.5, 1.0, 2.0]:
        h = (x / period) % 1.0
        starts.append(project(h))
        h = 1.0 - (x / period) % 1.0
        starts.append(project(h))

    return starts[:n_pop]


def method2_population(ref_h: np.ndarray, time_limit: float = 1200.0):
    """Population-based search: diverse cold starts, each polished with Adam."""
    print("\n" + "=" * 70)
    print("METHOD 2: Population-Based Search")
    print("=" * 70)

    rng = np.random.default_rng(123)
    t0 = time.time()

    # Generate diverse population
    n_pop = 50
    population = generate_diverse_starts(n_pop, rng, ref_h)
    print(f"  Generated {len(population)} diverse starting points")

    # Evaluate initial scores
    init_scores = [fast_evaluate(h) for h in population]
    print(f"  Initial score range: [{min(init_scores):.6f}, {max(init_scores):.6f}]")

    # Polish in batches
    batch_sz = 16  # GPU batch size
    n_processed = 0

    for batch_start in range(0, len(population), batch_sz):
        remaining = time_limit - (time.time() - t0)
        if remaining < 30:
            print(f"  Time running low ({remaining:.0f}s), stopping early")
            break

        batch = population[batch_start:batch_start + batch_sz]
        actual_bs = len(batch)
        polish_time = min(remaining * 0.6, 60.0)

        results = batched_adam_polish(
            batch, n_iters=15000, lr=0.005, time_limit=polish_time,
        )

        for i, (h_pol, score) in enumerate(results):
            idx = batch_start + i
            init_s = init_scores[idx] if idx < len(init_scores) else float("inf")
            corr = correlation(h_pol, ref_h)
            register_basin(h_pol, score, f"M2:pop{idx}", ref_h)

            if score < SOTA_SCORE:
                print(f"  *** POP {idx}: BEATS SOTA! C={score:.10f}, "
                      f"corr={corr:.3f}")
            elif score < SOTA_SCORE + 0.01:
                print(f"  pop {idx}: C={score:.10f} (init {init_s:.6f}), "
                      f"corr={corr:.3f}")

        n_processed += actual_bs
        elapsed = time.time() - t0
        best_so_far = min(basins, key=lambda b: b["score"])["score"] if basins else float("inf")
        print(f"  [{elapsed:.0f}s] processed={n_processed}/{len(population)}, "
              f"best={best_so_far:.10f}")

    print(f"  Method 2 done: {n_processed} candidates in {time.time() - t0:.0f}s")
    save_best()


# ===========================================================================
# Method 3: Simulated Annealing with large structural moves
# ===========================================================================

def method3_simulated_annealing(ref_h: np.ndarray, time_limit: float = 1200.0):
    """Simulated annealing with large structural moves."""
    print("\n" + "=" * 70)
    print("METHOD 3: Simulated Annealing with Large Moves")
    print("=" * 70)

    rng = np.random.default_rng(999)
    t0 = time.time()

    # Start from a few different points (ref + best basins found so far)
    starting_points = [ref_h.copy()]
    if basins:
        sorted_b = sorted(basins, key=lambda b: b["score"])
        for b in sorted_b[:3]:
            if b["score"] < SOTA_SCORE + 0.05:
                starting_points.append(b["h"].copy())

    overall_best_score = float("inf")
    overall_best_h = None

    for sp_idx, h_start in enumerate(starting_points):
        remaining = time_limit - (time.time() - t0)
        if remaining < 30:
            break

        sa_time = remaining / (len(starting_points) - sp_idx)
        h = project(h_start.copy())
        current_score = fast_evaluate(h)
        best_score = current_score
        best_h = h.copy()

        # SA parameters
        T_init = 0.01  # Initial temperature (relative to score ~0.38)
        T_final = 1e-6
        n_iters = 1_000_000
        accepts = 0
        improves = 0

        print(f"\n  SA run {sp_idx + 1}/{len(starting_points)}: "
              f"start C={current_score:.10f}, time budget={sa_time:.0f}s")

        sa_t0 = time.time()
        for it in range(n_iters):
            if time.time() - sa_t0 > sa_time:
                break

            # Temperature schedule (exponential cooling)
            progress = it / n_iters
            T = T_init * (T_final / T_init) ** progress

            # Choose move type
            move_type = rng.integers(6)

            if move_type == 0:
                # Gaussian perturbation (small to medium)
                sigma = rng.uniform(1e-4, 0.05)
                delta = sigma * rng.standard_normal(N)
                delta -= delta.mean()  # zero-sum to preserve constraint
                h_new = h + delta
            elif move_type == 1:
                # Swap two random blocks
                block_len = rng.integers(2, N // 5)
                i1 = rng.integers(N - block_len)
                i2 = rng.integers(N - block_len)
                h_new = h.copy()
                h_new[i1:i1 + block_len], h_new[i2:i2 + block_len] = (
                    h[i2:i2 + block_len].copy(),
                    h[i1:i1 + block_len].copy(),
                )
            elif move_type == 2:
                # Circular shift of a subsection
                seg_len = rng.integers(N // 10, N // 2)
                start = rng.integers(N - seg_len)
                shift = rng.integers(1, seg_len)
                h_new = h.copy()
                h_new[start:start + seg_len] = np.roll(
                    h[start:start + seg_len], shift
                )
            elif move_type == 3:
                # Reverse a subsection
                seg_len = rng.integers(N // 10, N // 2)
                start = rng.integers(N - seg_len)
                h_new = h.copy()
                h_new[start:start + seg_len] = h[start:start + seg_len][::-1]
            elif move_type == 4:
                # Scale a subsection up/down (balance with complement)
                seg_len = rng.integers(N // 10, N // 3)
                start = rng.integers(N - seg_len)
                scale = rng.uniform(0.8, 1.2)
                h_new = h.copy()
                old_sum = h_new[start:start + seg_len].sum()
                h_new[start:start + seg_len] *= scale
                new_sum = h_new[start:start + seg_len].sum()
                # Distribute difference across the rest
                diff = new_sum - old_sum
                rest_mask = np.ones(N, dtype=bool)
                rest_mask[start:start + seg_len] = False
                rest_count = rest_mask.sum()
                if rest_count > 0:
                    h_new[rest_mask] -= diff / rest_count
            else:
                # Pair-wise zero-sum random walk (k pairs)
                k = rng.integers(2, 20)
                h_new = h.copy()
                for _ in range(k):
                    i, j = rng.choice(N, size=2, replace=False)
                    delta = rng.uniform(1e-5, 0.02)
                    if rng.random() < 0.5:
                        delta = -delta
                    h_new[i] += delta
                    h_new[j] -= delta

            h_new = project(h_new)
            new_score = fast_evaluate(h_new)

            # Accept or reject
            delta_score = new_score - current_score
            if delta_score < 0:
                h = h_new
                current_score = new_score
                accepts += 1
                improves += 1
                if new_score < best_score:
                    best_score = new_score
                    best_h = h_new.copy()
            elif T > 0 and rng.random() < np.exp(-delta_score / T):
                h = h_new
                current_score = new_score
                accepts += 1

            if (it + 1) % 100_000 == 0:
                elapsed = time.time() - sa_t0
                print(f"    iter {it+1}: best={best_score:.10f}, "
                      f"current={current_score:.10f}, T={T:.6f}, "
                      f"accepts={accepts}, improves={improves}, "
                      f"time={elapsed:.0f}s")

        # Polish best with quick Adam
        remaining_sa = sa_time - (time.time() - sa_t0)
        if remaining_sa > 10:
            print(f"  Polishing SA best (C={best_score:.10f}) with Adam...")
            polished_h, polished_score = quick_adam_polish(
                best_h, n_iters=5000, lr=0.003, batch_size=4,
                time_limit=min(remaining_sa - 5, 30.0),
            )
            if polished_score < best_score:
                best_h = polished_h
                best_score = polished_score
                print(f"  Polished to C={best_score:.10f}")

        corr = correlation(best_h, ref_h)
        register_basin(best_h, best_score, f"M3:SA_run{sp_idx}", ref_h)

        if best_score < SOTA_SCORE:
            print(f"  *** SA RUN {sp_idx}: BEATS SOTA! C={best_score:.10f}, "
                  f"corr={corr:.3f}")
        else:
            print(f"  SA run {sp_idx} best: C={best_score:.10f}, corr={corr:.3f}")

        if best_score < overall_best_score:
            overall_best_score = best_score
            overall_best_h = best_h.copy()

    print(f"\n  Method 3 done: best={overall_best_score:.10f}, "
          f"time={time.time() - t0:.0f}s")
    save_best()


# ===========================================================================
# Main
# ===========================================================================

def main():
    print("=" * 70)
    print("Erdős Minimum Overlap — Basin Hopper")
    print(f"n={N}, SOTA={SOTA_SCORE}")
    print("=" * 70)

    t_total = time.time()

    # Generate reference solution (proxy for SOTA)
    print("\nGenerating reference solution via cold-start Adam...")
    ref_h_init = generate_sota_proxy()
    ref_score_init = fast_evaluate(ref_h_init)
    print(f"  Initial construction: C={ref_score_init:.10f}")

    # Polish reference with Adam
    ref_h, ref_score = quick_adam_polish(
        ref_h_init, n_iters=15000, lr=0.008, batch_size=32,
        time_limit=120.0,
    )
    print(f"  Polished reference: C={ref_score:.10f}")
    register_basin(ref_h, ref_score, "reference", ref_h)

    # Time allocation: ~20 min per method
    total_budget = 60.0 * 60  # 60 min total max
    method_budget = 20.0 * 60  # 20 min per method

    # Method 1: Basin Hopping
    remaining = total_budget - (time.time() - t_total)
    method1_basin_hopping(ref_h, time_limit=min(method_budget, remaining - 120))

    # Method 2: Population-Based Search
    remaining = total_budget - (time.time() - t_total)
    method2_population(ref_h, time_limit=min(method_budget, remaining - 120))

    # Method 3: Simulated Annealing
    remaining = total_budget - (time.time() - t_total)
    method3_simulated_annealing(ref_h, time_limit=min(method_budget, remaining - 30))

    # Final summary
    print_basin_summary(ref_h)

    # Verify best with exact evaluator
    if basins:
        best = min(basins, key=lambda b: b["score"])
        exact_score = exact_evaluate({"values": best["h"].tolist()})
        fast_score = fast_evaluate(best["h"])
        print(f"\nFinal verification:")
        print(f"  Fast:  {fast_score:.13f}")
        print(f"  Exact: {exact_score:.13f}")
        print(f"  Match: {abs(fast_score - exact_score) < 1e-10}")

        if exact_score < SOTA_SCORE:
            print(f"\n  *** NEW RECORD: {exact_score:.13f} < {SOTA_SCORE:.13f} ***")
        else:
            print(f"\n  Gap to SOTA: {exact_score - SOTA_SCORE:.2e}")

    save_best()

    elapsed = time.time() - t_total
    print(f"\nTotal time: {elapsed:.0f}s ({elapsed / 60:.1f} min)")
    print("=" * 70)


if __name__ == "__main__":
    main()
