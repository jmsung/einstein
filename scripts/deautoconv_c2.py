"""Deautoconvolution optimizer for Problem 3 (Second Autocorrelation Inequality).

Novel approach: instead of maximizing C directly, find f≥0 whose autoconvolution
is as flat as possible using EM-style multiplicative updates (Finesso & Spreij).

Target: flat autoconvolution → C close to 1.

Algorithm:
  Given target g_target (constant), iteratively update f so that f*f → g_target.
  Each update: f_new[j] = f[j]/c * Σ_l f[l] * g_target[l+j] / (f*f)[l+j]
  This is a correlation of f with (g_target / (f*f)).
"""

import sys

sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

from einstein.autocorrelation_fast import diagnose, fast_evaluate, score_from_conv

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


def deautoconv_flat(n, n_iter=500, target_shape="constant", seed=42):
    """Find f of length n whose f*f is approximately flat.

    Uses EM-style multiplicative updates that preserve positivity
    and monotonically decrease I-divergence from the target.

    Args:
        n: Length of f.
        n_iter: Number of iterations.
        target_shape: 'constant' for flat target, 'plateau' for flat-top with tails.
        seed: Random seed.

    Returns:
        (f, score): Best function and its C score.
    """
    rng = np.random.default_rng(seed)
    conv_len = 2 * n - 1

    # Build target autoconvolution
    if target_shape == "constant":
        target = np.ones(conv_len)
    elif target_shape == "plateau":
        # Flat in the middle, tapering at edges
        target = np.ones(conv_len)
        taper = min(n // 4, conv_len // 8)
        for i in range(taper):
            w = (i + 1) / (taper + 1)
            target[i] = w
            target[conv_len - 1 - i] = w
    else:
        target = np.ones(conv_len)

    # Initialize: random positive values
    f = rng.uniform(0.1, 1.0, n)

    best_score = 0.0
    best_f = f.copy()

    for t in range(n_iter):
        # Current autoconvolution
        conv = fftconvolve(f, f, mode="full")
        conv_safe = np.maximum(conv, 1e-30)

        # Ratio: target / current
        ratio = target / conv_safe

        # Multiplicative update:
        # f_new[j] = f[j]/c * sum_l f[l] * ratio[l+j]
        # The sum is a cross-correlation of f with ratio
        # Implemented as: fftconvolve(f, ratio[::-1]) at correct indices
        update = fftconvolve(f, ratio[::-1], mode="full")
        # Extract the right n elements (centered)
        update = update[n - 1 : 2 * n - 1]
        update = np.maximum(update, 0.0)

        c = np.sum(f)
        if c > 0:
            f = f * update / c
        else:
            break

        # Ensure positivity
        f = np.maximum(f, 1e-30)

        # Track best score
        if (t + 1) % 10 == 0 or t == 0:
            score = fast_evaluate(f)
            if score > best_score:
                best_score = score
                best_f = f.copy()

    # Final evaluation
    score = fast_evaluate(f)
    if score > best_score:
        best_score = score
        best_f = f.copy()

    return best_f, best_score


def deautoconv_multi_start(n, n_starts=20, n_iter=500, target_shape="constant"):
    """Run deautoconvolution from multiple random initializations."""
    best_f = None
    best_score = 0.0

    for s in range(n_starts):
        f, score = deautoconv_flat(n, n_iter=n_iter, target_shape=target_shape, seed=s)
        if score > best_score:
            best_score = score
            best_f = f.copy()
        if (s + 1) % 5 == 0:
            print(f"  Start {s+1}/{n_starts}: best C={best_score:.8f}")

    return best_f, best_score


def refine_with_adam_style(f, n_iter=5000, lr=0.01):
    """Refine a solution using gradient-free perturbation (Adam-style momentum)."""
    f = f.copy()
    best_score = fast_evaluate(f)
    best_f = f.copy()
    rng = np.random.default_rng(42)

    # Momentum-based perturbation
    momentum = np.zeros_like(f)
    beta = 0.9

    for t in range(n_iter):
        # Random perturbation direction
        direction = rng.standard_normal(len(f))
        direction *= lr / (1 + t * 0.001)

        # Apply with momentum
        momentum = beta * momentum + (1 - beta) * direction
        trial = np.maximum(f + momentum, 0)

        score = fast_evaluate(trial)
        if score > best_score:
            best_score = score
            best_f = trial.copy()
            f = trial
        else:
            # Reject — decay momentum
            momentum *= 0.5

    return best_f, best_score


def upscale_and_refine(f, target_n):
    """Upscale solution via linear interpolation and refine."""
    old_n = len(f)
    x_old = np.linspace(0, 1, old_n)
    x_new = np.linspace(0, 1, target_n)
    f_new = np.interp(x_new, x_old, f)
    f_new = np.maximum(f_new, 0.0)

    old_score = fast_evaluate(f)
    new_score = fast_evaluate(f_new)
    print(f"  Upscale: n={old_n}→{target_n}, C={old_score:.8f}→{new_score:.8f}")
    return f_new


def main():
    print("=" * 60)
    print("Deautoconvolution Optimizer — Novel Approach")
    print("Find f whose f*f is flat → C close to 1")
    print("=" * 60)

    # Phase 1: Small n, many starts, both target shapes
    for n in [500, 1000, 2000]:
        print(f"\n--- Phase 1: Deautoconvolution at n={n} ---")

        for shape in ["constant", "plateau"]:
            print(f"\n  Target shape: {shape}")
            t0 = time.time()
            f, score = deautoconv_multi_start(
                n, n_starts=20, n_iter=300, target_shape=shape
            )
            elapsed = time.time() - t0
            d = diagnose(f)
            print(
                f"  Best: C={score:.8f}, nnz={d['nnz']}, "
                f"blocks={d['n_blocks']}, flat_0.1%={d['flatness_0.1pct']}, "
                f"{elapsed:.1f}s"
            )
            save_result(f, score, f"deautoconv_{shape}_n{n}")

    # Phase 2: Take best small-n result and refine
    print(f"\n--- Phase 2: Refine best result ---")
    # Find best result file
    best_score = 0
    best_f = None
    for fname in RESULTS_DIR.glob("c2_*_deautoconv_*.json"):
        with open(fname) as fh:
            d = json.load(fh)
        if d["score"] > best_score:
            best_score = d["score"]
            best_f = np.array(d["values"])

    if best_f is not None:
        print(f"  Starting from C={best_score:.8f}, n={len(best_f)}")
        f_refined, score_refined = refine_with_adam_style(best_f, n_iter=5000)
        print(f"  After refinement: C={score_refined:.8f}")
        save_result(f_refined, score_refined, "deautoconv_refined")

        # Phase 3: Multi-scale upsampling
        print(f"\n--- Phase 3: Multi-scale upsampling ---")
        f_current = f_refined
        for target_n in [4000, 8000, 16000]:
            f_up = upscale_and_refine(f_current, target_n)
            # Quick deautoconv refinement at new scale
            f_deconv, score_deconv = deautoconv_flat(
                target_n, n_iter=100, seed=42
            )
            # Use whichever is better
            score_up = fast_evaluate(f_up)
            if score_deconv > score_up:
                f_current = f_deconv
                print(f"  n={target_n}: deautoconv wins C={score_deconv:.8f}")
            else:
                f_current = f_up
                print(f"  n={target_n}: upscaled wins C={score_up:.8f}")
            save_result(f_current, fast_evaluate(f_current), f"deautoconv_n{target_n}")

    # Final report
    print("\n" + "=" * 60)
    if best_f is not None:
        final_score = fast_evaluate(f_current)
        d = diagnose(f_current)
        print(f"FINAL: C={final_score:.8f}, n={len(f_current)}")
        print(f"  nnz={d['nnz']}, blocks={d['n_blocks']}")
        print(f"  flat_0.1%={d['flatness_0.1pct']}, flat_1%={d['flatness_1pct']}")
        print(f"  Done.")
    print("=" * 60)


if __name__ == "__main__":
    main()
