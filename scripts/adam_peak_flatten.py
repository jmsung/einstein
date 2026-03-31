"""Batched Adam optimizer with peak-flattening for Problem 3.

Based on Jaech & Joseph (arXiv:2508.02803) who achieved C=0.941 from scratch.

Key insight: L∞ in the denominator creates a gradient that naturally flattens
the tallest autoconvolution peak at each step (peak-flattening), instead of
reinforcing it (peak-locking). This is why direct gradient ascent on C works.

Algorithm:
  Phase 1: Exploration — batch of B candidates, Adam + noise, 10k iters
  Phase 2: Exploitation — top candidates, Adam no noise, 10k iters
  Phase 3: Upsample 4x + refine, repeat
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
        "values": f.tolist() if isinstance(f, np.ndarray) else f,
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"c2_n{len(f)}_{score:.8f}_{tag}.json"
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")


def compute_C_batch(h_batch, device):
    """Compute C for a batch of candidates. h_batch: (B, N) tensor."""
    f = torch.clamp(h_batch, min=0)
    B, N = f.shape
    nc = 2 * N - 1

    # FFT-based autoconvolution
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    F = torch.fft.rfft(f, n=nfft, dim=1)
    conv = torch.fft.irfft(F * F, n=nfft, dim=1)[:, :nc]  # (B, nc)

    # Simpson's rule L2² (exact arena formula)
    # C = (2*sum(c²) + sum(c*c_shift)) / (3 * sum(c) * max(c))
    c_sq = torch.sum(conv * conv, dim=1)  # (B,)
    c_shift = torch.sum(conv[:, :-1] * conv[:, 1:], dim=1)  # (B,)
    c_sum = torch.sum(conv, dim=1)  # (B,)
    c_max = torch.max(conv, dim=1).values  # (B,)

    numerator = 2 * c_sq + c_shift
    denominator = 3 * c_sum * c_max

    C = numerator / (denominator + 1e-30)
    return C


def adam_optimize(n, batch_size=64, n_explore=5000, n_exploit=5000,
                  lr_explore=3e-2, lr_exploit=5e-3, device='cpu',
                  seed=42, time_limit=120):
    """Batched Adam optimization with peak-flattening gradient.

    Args:
        n: Function length.
        batch_size: Number of parallel candidates.
        n_explore: Exploration iterations (with noise).
        n_exploit: Exploitation iterations (clean gradients).
        lr_explore: Learning rate for exploration.
        lr_exploit: Learning rate for exploitation.
        device: 'cpu' or 'mps'.
        seed: Random seed.
        time_limit: Max seconds.

    Returns:
        (best_f, best_score): Best function and its C score.
    """
    torch.manual_seed(seed)
    dtype = torch.float32

    # Initialize: random uniform
    h = torch.rand(batch_size, n, device=device, dtype=dtype) * 0.5
    h.requires_grad_(True)

    best_score = 0.0
    best_f = None
    t0 = time.time()

    # Phase 1: Exploration with noise
    optimizer = torch.optim.Adam([h], lr=lr_explore)
    eta, gamma = 1e-3, 0.65

    print(f"  Phase 1: Exploration (n={n}, B={batch_size}, {n_explore} iters)")
    for t in range(n_explore):
        if time.time() - t0 > time_limit * 0.4:
            print(f"    Time limit (explore), stopping at iter {t}")
            break

        optimizer.zero_grad()
        C = compute_C_batch(h, device)
        loss = -C.mean()
        loss.backward()

        # Add gradient noise for exploration
        noise_scale = eta / (t + 1) ** gamma
        with torch.no_grad():
            h.grad += noise_scale * torch.randn_like(h.grad)

        optimizer.step()

        # Project to non-negative
        with torch.no_grad():
            h.clamp_(min=0)

        # Track best (every 100 iters to save time)
        if (t + 1) % 200 == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h, device)
                best_idx = torch.argmax(C_vals)
                c_val = C_vals[best_idx].item()
                if c_val > best_score and c_val < 1.0:
                    best_score = c_val
                    best_f = h[best_idx].detach().cpu().numpy().copy()
                if (t + 1) % 1000 == 0:
                    print(f"    iter {t+1}: best C={best_score:.8f}, "
                          f"batch mean={C_vals.mean().item():.6f}")

    # Phase 2: Exploitation — elitist selection + clean gradients
    print(f"  Phase 2: Exploitation ({n_exploit} iters)")

    # Keep top 50%, replace rest
    with torch.no_grad():
        C_vals = compute_C_batch(h, device)
        _, sorted_idx = torch.sort(C_vals, descending=True)
        keep = batch_size // 2
        top_h = h[sorted_idx[:keep]].clone()
        # Replace bottom half with fresh random
        fresh = torch.rand(batch_size - keep, n, device=device, dtype=dtype) * 0.5
        h = torch.cat([top_h, fresh], dim=0)
        h.requires_grad_(True)

    optimizer = torch.optim.Adam([h], lr=lr_exploit)

    for t in range(n_exploit):
        if time.time() - t0 > time_limit * 0.85:
            print(f"    Time limit (exploit), stopping at iter {t}")
            break

        optimizer.zero_grad()
        C = compute_C_batch(h, device)
        loss = -C.mean()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            h.clamp_(min=0)

        # Elitist respawn every 2000 iters
        if (t + 1) % 2000 == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h, device)
                _, sorted_idx = torch.sort(C_vals, descending=True)
                keep = batch_size // 2
                top_h = h[sorted_idx[:keep]].clone()
                fresh = torch.rand(batch_size - keep, n, device=device, dtype=dtype) * 0.5
                h = torch.cat([top_h, fresh], dim=0)
                h.requires_grad_(True)
                optimizer = torch.optim.Adam([h], lr=lr_exploit)

        if (t + 1) % 1000 == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h, device)
                best_idx = torch.argmax(C_vals)
                c_val = C_vals[best_idx].item()
                if c_val > best_score and c_val < 1.0:
                    best_score = c_val
                    best_f = h[best_idx].detach().cpu().numpy().copy()
                print(f"    iter {t+1}: best C={best_score:.8f}, "
                      f"batch mean={C_vals.mean().item():.6f}")

    # Final extraction
    with torch.no_grad():
        C_vals = compute_C_batch(h, device)
        best_idx = torch.argmax(C_vals)
        c_val = C_vals[best_idx].item()
        if c_val > best_score and c_val < 1.0:
            best_score = c_val
            best_f = h[best_idx].detach().cpu().numpy().copy()

    # Verify with float64 scorer
    if best_f is not None:
        best_f = np.maximum(best_f, 0)
        verified = fast_evaluate(best_f)
        print(f"  Verified (float64): C={verified:.10f}")
        return best_f, verified

    return np.zeros(n), 0.0


def upscale_linear(f, new_n):
    """4x linear interpolation upsampling."""
    x_old = np.linspace(0, 1, len(f))
    x_new = np.linspace(0, 1, new_n)
    f_new = np.interp(x_new, x_old, f)
    return np.maximum(f_new, 0.0)


def main():
    print("=" * 60)
    print("Batched Adam — Peak-Flattening Optimizer")
    print("Based on Jaech & Joseph (arXiv:2508.02803)")
    print("=" * 60)

    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"Device: {device}")

    # Stage 1: Small n, find good structure
    n_start = 768
    print(f"\n=== Stage 1: n={n_start} ===")
    f, score = adam_optimize(
        n_start, batch_size=128, n_explore=8000, n_exploit=8000,
        lr_explore=3e-2, lr_exploit=5e-3, device=device,
        time_limit=120
    )
    save_result(f, score, f"adam_n{n_start}")

    # Trim leading/trailing zeros
    nz = np.nonzero(f > 1e-8)[0]
    if len(nz) > 0:
        f_trimmed = f[nz[0]:nz[-1]+1]
        score_trimmed = fast_evaluate(f_trimmed)
        print(f"  Trimmed: {len(f)}→{len(f_trimmed)}, C={score_trimmed:.8f}")
        if score_trimmed > score:
            f = f_trimmed
            score = score_trimmed

    # Stage 2: Upsample and refine
    for scale_factor in [4, 4, 4]:
        new_n = len(f) * scale_factor
        if new_n > 50000:
            break

        print(f"\n=== Stage 2: Upsample to n={new_n} ===")
        f_up = upscale_linear(f, new_n)
        score_up = fast_evaluate(f_up)
        print(f"  After upscale: C={score_up:.8f}")

        # Refine at new scale (fewer iters, smaller batch)
        # Convert to torch, run Adam
        f_refined, score_refined = adam_optimize(
            new_n, batch_size=16, n_explore=3000, n_exploit=3000,
            lr_explore=1e-2, lr_exploit=3e-3, device=device,
            seed=0, time_limit=90
        )

        # Also try refining the upscaled version directly
        h = torch.tensor(f_up, dtype=torch.float32, device=device).unsqueeze(0)
        h.requires_grad_(True)
        opt = torch.optim.Adam([h], lr=1e-3)
        best_up = score_up
        best_f_up = f_up.copy()

        for t in range(3000):
            opt.zero_grad()
            C = compute_C_batch(h, device)
            (-C).backward()
            opt.step()
            with torch.no_grad():
                h.clamp_(min=0)
            if (t+1) % 1000 == 0:
                cv = C.item()
                if cv > best_up and cv < 1.0:
                    best_up = cv
                    best_f_up = h[0].detach().cpu().numpy().copy()
                print(f"    Refine upscaled iter {t+1}: C={best_up:.8f}")

        # Verify both
        best_f_up = np.maximum(best_f_up, 0)
        verified_up = fast_evaluate(best_f_up)
        print(f"  Upscaled+refined: C={verified_up:.8f}")
        print(f"  From-scratch:     C={score_refined:.8f}")

        if verified_up > score_refined:
            f = best_f_up
            score = verified_up
        else:
            f = f_refined
            score = score_refined

        save_result(f, score, f"adam_n{new_n}")

    # Final report
    print("\n" + "=" * 60)
    d = diagnose(f)
    print(f"FINAL: C={score:.10f}, n={len(f)}")
    print(f"  nnz={d['nnz']}, blocks={d['n_blocks']}")
    print(f"  flat_0.1%={d['flatness_0.1pct']}")
    print(f"  Target: 0.962086")
    print(f"  {'BEATS TARGET!' if score > 0.962086 else 'Below target'}")
    print("=" * 60)

    save_result(f, score, "adam_final")


if __name__ == "__main__":
    main()
