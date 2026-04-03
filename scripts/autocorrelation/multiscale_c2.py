"""Multi-scale upsampling optimizer for Problem 3.

Based on Jaech & Joseph (arXiv:2508.02803) + Boyer & Li upsampling insight.

Strategy:
  1. Optimize HARD at n=768 (many iters, large batch) — find the best structure
  2. 4x linear upsample to 3k
  3. Optimize at 3k (medium iters) — refine structure at higher resolution
  4. 4x upsample to 12k, optimize
  5. 4x upsample to 48k, optimize
  6. 4x upsample to ~200k, optimize

Key insight from experiments: small n finds BETTER structure than large n.
The upsampling preserves structure; refinement at each scale polishes it.
"""

import sys

sys.path.insert(0, "src")

import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.autocorrelation.fast import fast_evaluate, diagnose

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


def compute_C_batch(h_batch, device):
    """Compute C for a batch of candidates."""
    f = torch.clamp(h_batch, min=0)
    B, N = f.shape
    nc = 2 * N - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    F = torch.fft.rfft(f, n=nfft, dim=1)
    conv = torch.fft.irfft(F * F, n=nfft, dim=1)[:, :nc]

    c_sq = torch.sum(conv * conv, dim=1)
    c_shift = torch.sum(conv[:, :-1] * conv[:, 1:], dim=1)
    c_sum = torch.sum(conv, dim=1)
    c_max = torch.max(conv, dim=1).values

    numerator = 2 * c_sq + c_shift
    denominator = 3 * c_sum * c_max
    return numerator / (denominator + 1e-30)


def adam_optimize_stage(n, batch_size, n_iters, lr, device, seed=42,
                        init_f=None, noise_scale=0.0, respawn_every=0):
    """Single-stage Adam optimization."""
    torch.manual_seed(seed)
    dtype = torch.float32

    if init_f is not None:
        # Warm-start: replicate init with small perturbations
        base = torch.tensor(init_f, dtype=dtype, device=device)
        noise = torch.randn(batch_size, n, device=device, dtype=dtype) * 0.01
        h = base.unsqueeze(0).expand(batch_size, -1) + noise
        h = torch.clamp(h, min=0)
    else:
        h = torch.rand(batch_size, n, device=device, dtype=dtype) * 0.5

    h = h.clone().requires_grad_(True)
    optimizer = torch.optim.Adam([h], lr=lr)

    best_score = 0.0
    best_f = None

    for t in range(n_iters):
        optimizer.zero_grad()
        C = compute_C_batch(h, device)
        loss = -C.mean()
        loss.backward()

        if noise_scale > 0:
            with torch.no_grad():
                eta = noise_scale / (t + 1) ** 0.65
                h.grad += eta * torch.randn_like(h.grad)

        optimizer.step()

        with torch.no_grad():
            h.clamp_(min=0)

        # Elitist respawn
        if respawn_every > 0 and (t + 1) % respawn_every == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h, device)
                _, sorted_idx = torch.sort(C_vals, descending=True)
                keep = batch_size // 2
                top_h = h[sorted_idx[:keep]].clone()
                if init_f is not None:
                    base = torch.tensor(init_f, dtype=dtype, device=device)
                    fresh = base.unsqueeze(0).expand(batch_size - keep, -1).clone()
                    fresh += torch.randn_like(fresh) * 0.02
                    fresh = torch.clamp(fresh, min=0)
                else:
                    fresh = torch.rand(batch_size - keep, n, device=device, dtype=dtype) * 0.5
                h = torch.cat([top_h, fresh], dim=0).requires_grad_(True)
                optimizer = torch.optim.Adam([h], lr=lr)

        # Track best
        if (t + 1) % 500 == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h, device)
                best_idx = torch.argmax(C_vals)
                c_val = C_vals[best_idx].item()
                if c_val > best_score and c_val < 1.0:
                    best_score = c_val
                    best_f = h[best_idx].detach().cpu().numpy().copy()
                    best_f = np.maximum(best_f, 0)

    # Final extraction
    with torch.no_grad():
        C_vals = compute_C_batch(h, device)
        best_idx = torch.argmax(C_vals)
        c_val = C_vals[best_idx].item()
        if c_val > best_score and c_val < 1.0:
            best_score = c_val
            best_f = h[best_idx].detach().cpu().numpy().copy()
            best_f = np.maximum(best_f, 0)

    if best_f is not None:
        verified = fast_evaluate(best_f)
        return best_f, verified
    return np.zeros(n), 0.0


def upscale_linear(f, new_n):
    """Linear interpolation upsampling."""
    x_old = np.linspace(0, 1, len(f))
    x_new = np.linspace(0, 1, new_n)
    f_new = np.interp(x_new, x_old, f)
    return np.maximum(f_new, 0.0)


def main():
    print("=" * 60)
    print("Multi-Scale Upsampling Optimizer")
    print("Strategy: optimize hard at small n, upsample, refine")
    print("=" * 60)

    device = 'mps' if torch.backends.mps.is_available() else 'cpu'
    print(f"Device: {device}")

    # ---------------------------------------------------------------
    # Scale 1: n=768, large batch, long optimization
    # ---------------------------------------------------------------
    n1 = 768
    print(f"\n=== Scale 1: n={n1} (foundation) ===")

    # Exploration: large batch, noise
    print("  Exploration phase...")
    f1, s1 = adam_optimize_stage(
        n1, batch_size=256, n_iters=15000, lr=3e-2, device=device,
        noise_scale=1e-3, respawn_every=5000, seed=42
    )
    print(f"  Exploration: C={s1:.8f}")

    # Exploitation: clean gradients, from best
    print("  Exploitation phase...")
    f1b, s1b = adam_optimize_stage(
        n1, batch_size=64, n_iters=10000, lr=5e-3, device=device,
        init_f=f1, respawn_every=3000, seed=123
    )
    if s1b > s1:
        f1, s1 = f1b, s1b
    print(f"  Scale 1 final: C={s1:.8f}")

    d = diagnose(f1)
    print(f"  nnz={d['nnz']}, blocks={d['n_blocks']}, flat_0.1%={d['flatness_0.1pct']}")
    save_result(f1, s1, f"multiscale_n{n1}")

    # Trim zeros
    nz = np.nonzero(f1 > 1e-8)[0]
    if len(nz) > 0:
        f1 = f1[nz[0]:nz[-1]+1]
        s1 = fast_evaluate(f1)
        print(f"  Trimmed to {len(f1)} points, C={s1:.8f}")

    # ---------------------------------------------------------------
    # Scales 2-5: Upsample 4x and refine at each scale
    # ---------------------------------------------------------------
    f_current = f1
    scale_configs = [
        # (scale_factor, batch_size, n_iters, lr)
        (4, 32, 8000, 1e-2),   # ~3k points
        (4, 16, 5000, 5e-3),   # ~12k points
        (4, 8, 3000, 3e-3),    # ~48k points
    ]

    for i, (sf, bs, ni, lr) in enumerate(scale_configs):
        new_n = len(f_current) * sf
        print(f"\n=== Scale {i+2}: n={new_n} (4x upsample) ===")

        f_up = upscale_linear(f_current, new_n)
        score_up = fast_evaluate(f_up)
        print(f"  After upscale: C={score_up:.8f}")

        # Refine the upscaled solution
        print("  Refining upscaled...")
        f_ref, s_ref = adam_optimize_stage(
            new_n, batch_size=bs, n_iters=ni, lr=lr, device=device,
            init_f=f_up, respawn_every=2000, seed=i*100
        )

        # Also try from scratch at this scale (smaller batch)
        print("  Trying from scratch...")
        f_scratch, s_scratch = adam_optimize_stage(
            new_n, batch_size=bs, n_iters=ni, lr=2e-2, device=device,
            noise_scale=5e-4, respawn_every=2000, seed=i*100+50
        )

        # Pick the best
        best_s = max(score_up, s_ref, s_scratch)
        if s_ref >= best_s:
            f_current = f_ref
            winner = "refined"
        elif score_up >= best_s:
            f_current = f_up
            winner = "upscaled"
        else:
            f_current = f_scratch
            winner = "scratch"

        best_s = fast_evaluate(f_current)
        d = diagnose(f_current)
        print(f"  Winner: {winner}, C={best_s:.8f}")
        print(f"  nnz={d['nnz']}, blocks={d['n_blocks']}, flat_0.1%={d['flatness_0.1pct']}")
        save_result(f_current, best_s, f"multiscale_n{new_n}")

    # ---------------------------------------------------------------
    # Final report
    # ---------------------------------------------------------------
    final_score = fast_evaluate(f_current)
    d = diagnose(f_current)
    print("\n" + "=" * 60)
    print(f"FINAL: C={final_score:.10f}, n={len(f_current)}")
    print(f"  nnz={d['nnz']}, blocks={d['n_blocks']}")
    print(f"  flat_0.1%={d['flatness_0.1pct']}, flat_1%={d['flatness_1pct']}")
    print(f"  Done.")
    print("=" * 60)

    save_result(f_current, final_score, "multiscale_final")


if __name__ == "__main__":
    main()
