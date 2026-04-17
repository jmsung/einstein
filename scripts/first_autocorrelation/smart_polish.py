"""Smart polishing strategies for P2 First Autocorrelation.

Multiple approaches to squeeze tiny improvements from OrganonAgent's solution:
1. Exact gradient descent with adaptive step and Armijo line search
2. Block-wise coordinate descent
3. Random perturbation lottery (structured noise patterns)
4. Equioscillation-aware optimization
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from einstein.first_autocorrelation.evaluator import verify_and_compute

RESULTS = Path("results/problem-2-first-autocorrelation")


def exact_score(f: np.ndarray) -> float:
    return float(verify_and_compute(f.astype(np.float64).tolist()))


def compute_gradient(f: np.ndarray, topk: int = 2000) -> tuple[np.ndarray, float, np.ndarray]:
    """Compute subgradient of C w.r.t. f using weighted top-K peaks."""
    n = len(f)
    dx = 0.5 / n
    s = f.sum()

    # FFT-based convolution
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    conv = np.fft.irfft(F * F, n=m_pad)[:m]
    ratios = conv * dx / (s * dx) ** 2

    # Weighted top-K peaks
    top_idx = np.argpartition(ratios, -topk)[-topk:]
    top_vals = ratios[top_idx]
    max_val = top_vals.max()
    C = max_val

    beta = 1e8
    z = beta * (top_vals - max_val)
    w = np.exp(np.clip(z, -500, 0))
    w /= w.sum()

    # Gradient
    mirror_sum = np.zeros(n, dtype=np.float64)
    c_sum = 0.0
    for wi, ti in zip(w, top_idx):
        if wi < 1e-20:
            continue
        lo = max(0, ti - (n - 1))
        hi = min(n - 1, ti)
        i_idx = np.arange(lo, hi + 1)
        j_idx = ti - i_idx
        mirror_sum[i_idx] += wi * f[j_idx]
        c_sum += wi * ratios[ti]
    grad = (2.0 * mirror_sum) / (s * s * dx) - (2.0 * c_sum) / s

    return grad, C, ratios


def approach_gradient_descent(f0: np.ndarray, max_iters: int = 5000,
                              lr0: float = 1e-6) -> tuple[np.ndarray, float]:
    """Exact gradient descent with Armijo line search."""
    print("\n=== Approach: Exact Gradient Descent ===")
    f = f0.astype(np.float64).copy()
    best_c = exact_score(f)
    best_f = f.copy()
    lr = lr0
    no_improve = 0
    print(f"Start: C={best_c:.18f}")

    for it in range(max_iters):
        grad, C_approx, ratios = compute_gradient(f, topk=2000)

        # Direction: negative gradient, only on active set
        active = (f > 1e-30) | (grad < 0)
        d = np.where(active, -grad, 0.0)
        gnorm = np.linalg.norm(d)
        if gnorm < 1e-30:
            print(f"  Gradient vanished at iter {it}")
            break
        d = d / gnorm

        # Armijo line search
        accepted = False
        for _ in range(40):
            f_try = np.maximum(f + lr * d, 0.0)
            if f_try.sum() <= 0:
                lr *= 0.5
                continue
            c_try = exact_score(f_try)
            if c_try < best_c:
                f = f_try
                if c_try < best_c:
                    delta = best_c - c_try
                    best_c = c_try
                    best_f = f.copy()
                    if it % 50 == 0 or delta > 1e-10:
                        print(f"  iter={it}: C={best_c:.18f} delta={delta:.3e} lr={lr:.2e}",
                              flush=True)
                lr = min(lr * 1.5, lr0 * 100)
                accepted = True
                no_improve = 0
                break
            lr *= 0.5

        if not accepted:
            no_improve += 1
            lr = lr0
            if no_improve >= 15:
                print(f"  Stalled at iter {it}")
                break

    print(f"Final: C={best_c:.18f} (delta from start={exact_score(f0) - best_c:.3e})")
    return best_f, best_c


def approach_block_coord_descent(f0: np.ndarray, block_size: int = 300,
                                  rounds: int = 3) -> tuple[np.ndarray, float]:
    """Block coordinate descent: optimize one block at a time."""
    print(f"\n=== Approach: Block Coordinate Descent (block_size={block_size}) ===")
    n = len(f0)
    f = f0.astype(np.float64).copy()
    best_c = exact_score(f)
    best_f = f.copy()
    print(f"Start: C={best_c:.18f}")

    n_blocks = (n + block_size - 1) // block_size
    improved_count = 0

    for rd in range(rounds):
        # Random block order
        block_order = np.random.default_rng(rd).permutation(n_blocks)
        for bi, block_idx in enumerate(block_order):
            start = block_idx * block_size
            end = min(start + block_size, n)

            # Try several perturbation patterns for this block
            original = f[start:end].copy()
            block_best_c = best_c
            block_best_vals = original.copy()

            grad, _, _ = compute_gradient(f, topk=1000)
            block_grad = grad[start:end]

            for trial in range(10):
                rng = np.random.default_rng(rd * 10000 + block_idx * 100 + trial)
                if trial == 0:
                    # Gradient step
                    perturbation = -block_grad * 1e-4
                elif trial < 5:
                    # Random perturbation scaled by gradient magnitude
                    scale = np.abs(block_grad).mean() * (0.5 ** trial)
                    perturbation = rng.normal(scale=scale, size=end - start)
                else:
                    # Random proportional perturbation
                    perturbation = original * rng.normal(scale=1e-4 * (0.5 ** (trial - 5)),
                                                          size=end - start)

                f[start:end] = np.maximum(original + perturbation, 0.0)
                if f.sum() <= 0:
                    f[start:end] = original
                    continue
                c_try = exact_score(f)
                if c_try < block_best_c:
                    block_best_c = c_try
                    block_best_vals = f[start:end].copy()

                f[start:end] = original

            if block_best_c < best_c:
                delta = best_c - block_best_c
                f[start:end] = block_best_vals
                best_c = block_best_c
                best_f = f.copy()
                improved_count += 1
                print(f"  round={rd} block={block_idx}/{n_blocks} C={best_c:.18f} "
                      f"delta={delta:.3e}", flush=True)
            else:
                f[start:end] = original

            if bi % 50 == 0 and bi > 0:
                elapsed_blocks = bi + 1
                print(f"  round={rd} progress: {elapsed_blocks}/{n_blocks} blocks, "
                      f"improved={improved_count}", flush=True)

    print(f"Final: C={best_c:.18f} (improved {improved_count} times)")
    return best_f, best_c


def approach_perturbation_lottery(f0: np.ndarray,
                                   n_trials: int = 1000) -> tuple[np.ndarray, float]:
    """Try many random perturbation patterns, keep improvements."""
    print(f"\n=== Approach: Perturbation Lottery ({n_trials} trials) ===")
    f = f0.astype(np.float64).copy()
    best_c = exact_score(f)
    best_f = f.copy()
    n = len(f)
    print(f"Start: C={best_c:.18f}")

    nonzero_mask = f > 1e-20
    n_nonzero = nonzero_mask.sum()
    print(f"  Nonzero cells: {n_nonzero}/{n}")

    improved = 0
    for trial in range(n_trials):
        rng = np.random.default_rng(trial)

        # Various perturbation strategies
        strategy = trial % 8
        if strategy == 0:
            # Global proportional noise
            noise = f * rng.normal(scale=1e-5, size=n)
        elif strategy == 1:
            # Sparse random perturbation (only 1% of cells)
            mask = rng.random(n) < 0.01
            noise = np.zeros(n)
            noise[mask] = rng.normal(scale=1e-4, size=mask.sum()) * np.maximum(f[mask], 1e-10)
        elif strategy == 2:
            # Swap mass between random pairs
            noise = np.zeros(n)
            i1, i2 = rng.choice(n, 2, replace=False)
            delta = f[i1] * rng.uniform(-0.1, 0.1)
            noise[i1] = -delta
            noise[i2] = delta
        elif strategy == 3:
            # Gradient-directed noise
            grad, _, _ = compute_gradient(f, topk=500)
            noise = -grad * rng.uniform(1e-8, 1e-5)
        elif strategy == 4:
            # Zero out small cells
            noise = np.zeros(n)
            small = (f > 0) & (f < np.percentile(f[f > 0], rng.uniform(1, 10)))
            noise[small] = -f[small]
        elif strategy == 5:
            # Grow zero cells slightly
            noise = np.zeros(n)
            zero_cells = f < 1e-20
            grow_mask = zero_cells & (rng.random(n) < 0.001)
            noise[grow_mask] = rng.uniform(0, 1e-6, size=grow_mask.sum())
        elif strategy == 6:
            # Frequency-domain perturbation
            V = np.fft.rfft(f)
            # Perturb random low frequencies
            k = rng.integers(1, min(1000, len(V)))
            V_noise = np.zeros_like(V)
            V_noise[k] = rng.normal(scale=abs(V[k]) * 1e-4) + 1j * rng.normal(scale=abs(V[k]) * 1e-4)
            noise = np.fft.irfft(V_noise, n=n)
        else:
            # Scale perturbation (multiply by 1+epsilon)
            eps = rng.normal(scale=1e-6)
            noise = f * eps

        f_try = np.maximum(f + noise, 0.0)
        if f_try.sum() <= 0:
            continue
        c_try = exact_score(f_try)
        if c_try < best_c:
            delta = best_c - c_try
            best_c = c_try
            best_f = f_try.copy()
            f = f_try.copy()
            improved += 1
            print(f"  trial={trial} strategy={strategy} C={best_c:.18f} delta={delta:.3e}",
                  flush=True)

        if trial % 200 == 0 and trial > 0:
            print(f"  progress: {trial}/{n_trials}, improved={improved}", flush=True)

    print(f"Final: C={best_c:.18f} ({improved} improvements)")
    return best_f, best_c


def approach_equioscillation(f0: np.ndarray) -> tuple[np.ndarray, float]:
    """Analyze and exploit the equioscillation structure."""
    print(f"\n=== Approach: Equioscillation Analysis ===")
    n = len(f0)
    dx = 0.5 / n
    f = f0.astype(np.float64).copy()
    s = f.sum()
    best_c = exact_score(f)
    best_f = f.copy()
    print(f"Start: C={best_c:.18f}")

    # Compute convolution
    m = 2 * n - 1
    m_pad = 1 << (m - 1).bit_length()
    F = np.fft.rfft(f, n=m_pad)
    conv = np.fft.irfft(F * F, n=m_pad)[:m]
    ratios = conv * dx / (s * dx) ** 2
    max_ratio = ratios.max()

    # Find near-maximum peaks
    threshold = 0.999 * max_ratio
    near_max_mask = ratios > threshold
    n_near_max = near_max_mask.sum()
    near_max_idx = np.where(near_max_mask)[0]
    print(f"  Max ratio: {max_ratio:.18f}")
    print(f"  Near-max peaks (>99.9%): {n_near_max}")
    print(f"  Near-max range: [{near_max_idx[0]}, {near_max_idx[-1]}]")

    # The argmax location
    argmax_t = np.argmax(ratios)
    print(f"  Argmax t: {argmax_t}")

    # Strategy: try to reduce the peak by redistributing mass
    # From the KKT conditions, at optimality, the gradient at nonzero
    # cells should be equal, and at zero cells should be >= 0
    grad, _, _ = compute_gradient(f, topk=5000)

    # Find cells that contribute most to the peak
    lo = max(0, argmax_t - (n - 1))
    hi = min(n - 1, argmax_t)
    peak_contributors = np.arange(lo, hi + 1)
    # Weight by f[j] where j = argmax_t - i
    contrib_weights = np.zeros(n)
    for i in peak_contributors:
        j = argmax_t - i
        if 0 <= j < n:
            contrib_weights[i] = f[j]

    # Try reducing top contributors and growing small contributors
    top_contrib = np.argsort(contrib_weights)[-100:]
    small_nonzero = np.where((f > 0) & (f < np.median(f[f > 0])))[0]

    for trial in range(500):
        rng = np.random.default_rng(300 + trial)

        # Reduce a random top contributor
        i_reduce = rng.choice(top_contrib)
        # Grow a random small cell
        i_grow = rng.choice(small_nonzero) if len(small_nonzero) > 0 else rng.integers(n)

        delta_mass = f[i_reduce] * rng.uniform(1e-6, 1e-4)

        f_try = f.copy()
        f_try[i_reduce] = max(f_try[i_reduce] - delta_mass, 0.0)
        f_try[i_grow] = f_try[i_grow] + delta_mass

        c_try = exact_score(f_try)
        if c_try < best_c:
            delta = best_c - c_try
            best_c = c_try
            best_f = f_try.copy()
            f = f_try.copy()
            print(f"  trial={trial} C={best_c:.18f} delta={delta:.3e} "
                  f"(moved mass from {i_reduce} to {i_grow})", flush=True)

    print(f"Final: C={best_c:.18f}")
    return best_f, best_c


def main():
    t_start = time.time()

    with open(RESULTS / "sol-01-OrganonAgent-1798.json") as f:
        org = json.load(f)
    f_org = np.array(org["values"], dtype=np.float64)
    c_org = exact_score(f_org)
    print(f"OrganonAgent: C={c_org:.18f}")
    print(f"Target: < {c_org - 1e-7:.18f}")

    global_best_c = c_org
    global_best_f = f_org.copy()

    def update(f, c, label):
        nonlocal global_best_c, global_best_f
        if c < global_best_c:
            global_best_c = c
            global_best_f = f.copy()
            save_path = RESULTS / f"smart-polish-{label}-{c:.10f}.json"
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, "w") as fh:
                json.dump({"values": f.tolist(), "score": c, "n": len(f), "tag": label}, fh)
            print(f"  Saved: {save_path}")
            return True
        return False

    # Run approaches
    f1, c1 = approach_gradient_descent(f_org, max_iters=2000, lr0=1e-6)
    update(f1, c1, "grad-descent")

    elapsed = time.time() - t_start
    print(f"\n--- Elapsed: {elapsed/60:.1f} min ---")

    f2, c2 = approach_perturbation_lottery(global_best_f, n_trials=2000)
    update(f2, c2, "perturbation")

    elapsed = time.time() - t_start
    print(f"\n--- Elapsed: {elapsed/60:.1f} min ---")

    f3, c3 = approach_equioscillation(global_best_f)
    update(f3, c3, "equioscillation")

    elapsed = time.time() - t_start
    print(f"\n--- Elapsed: {elapsed/60:.1f} min ---")

    if elapsed < 7200:
        f4, c4 = approach_block_coord_descent(global_best_f, block_size=300, rounds=2)
        update(f4, c4, "block-cd")

    # Summary
    elapsed = time.time() - t_start
    print(f"\n{'='*60}")
    print(f"SMART POLISH COMPLETE")
    print(f"{'='*60}")
    print(f"OrganonAgent: {c_org:.18f}")
    print(f"Our best:     {global_best_c:.18f}")
    print(f"Delta:        {c_org - global_best_c:+.6e}")
    print(f"Time:         {elapsed/60:.1f} min")


if __name__ == "__main__":
    main()
