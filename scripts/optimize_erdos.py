"""Optimizer for Erdos Minimum Overlap (Problem 1).

Multi-stage pipeline:
  Stage 1: Batched Adam at small n (exploration + exploitation)
  Stage 2: Upsample 4x, refine at each scale
  Stage 3: Hill-climb polishing

Scoring: C = max(correlate(h, 1-h, 'full')) * 2/n  (minimize)
Constraints: h in [0,1], sum(h) = n/2

Usage:
    uv run python scripts/optimize_erdos.py
    uv run python scripts/optimize_erdos.py --warm-start results/problem-1-erdos-overlap/best.json
"""

import sys

sys.path.insert(0, "src")

import argparse
import json
import time
from pathlib import Path

import numpy as np
import torch

from einstein.erdos import evaluate as exact_evaluate
from einstein.erdos_fast import fast_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def save_result(h, score, tag=""):
    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": len(h),
        "score": float(score),
        "values": h.tolist() if isinstance(h, np.ndarray) else h,
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"erdos_n{len(h)}_{score:.10f}_{tag}.json"
    with open(fname, "w") as fh:
        json.dump(result, fh)
    print(f"  Saved to {fname}")
    return fname


def compute_C_batch(h_batch, device):
    """Compute C for a batch of candidates. h_batch: (B, N) tensor.

    C = max(correlate(h, 1-h, 'full')) * 2/n  (minimize this)

    Uses FFT: correlate(h, 1-h) = conv(h, flip(1-h))
    """
    B, N = h_batch.shape

    # Clamp to [0, 1]
    h = torch.clamp(h_batch, 0, 1)

    # Normalize sum to N/2
    s = h.sum(dim=1, keepdim=True)
    h = h * (N / 2.0) / (s + 1e-30)
    h = torch.clamp(h, 0, 1)

    one_minus_h = 1.0 - h

    # Cross-correlation via FFT: correlate(h, 1-h) = conv(h, flip(1-h))
    nc = 2 * N - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    H = torch.fft.rfft(h, n=nfft, dim=1)
    G = torch.fft.rfft(one_minus_h.flip(1), n=nfft, dim=1)
    corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]

    # Score = max(corr) * 2/N
    C = corr.max(dim=1).values * 2.0 / N

    return C


def project_constraints(h):
    """Project h onto feasible set: h in [0,1], sum = n/2."""
    with torch.no_grad():
        h.clamp_(0, 1)
        B, N = h.shape
        s = h.sum(dim=1, keepdim=True)
        h.mul_(N / 2.0 / (s + 1e-30))
        h.clamp_(0, 1)


def adam_optimize(n, batch_size=64, n_iters=10000, lr=1e-2,
                  device="cpu", seed=42, time_limit=120,
                  warm_start=None):
    """Batched Adam optimization for Erdos overlap.

    Args:
        n: Discretization size.
        batch_size: Number of parallel candidates.
        n_iters: Total iterations.
        lr: Learning rate.
        device: 'cpu' or 'mps'.
        seed: Random seed.
        time_limit: Max seconds.
        warm_start: Optional numpy array to warm-start from.

    Returns:
        (best_h, best_score): Best function and its C score.
    """
    torch.manual_seed(seed)
    dtype = torch.float32

    # Initialize
    if warm_start is not None:
        # Warm-start: seed first candidate, rest random perturbations
        ws = torch.tensor(warm_start, dtype=dtype, device=device)
        if len(ws) != n:
            # Interpolate to target size
            ws_np = warm_start if isinstance(warm_start, np.ndarray) else np.array(warm_start)
            ws_np = np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(ws_np)), ws_np)
            ws = torch.tensor(ws_np, dtype=dtype, device=device)
        h = ws.unsqueeze(0).repeat(batch_size, 1)
        # Add noise to all but first
        h[1:] += 0.02 * torch.randn(batch_size - 1, n, device=device, dtype=dtype)
    else:
        h = torch.rand(batch_size, n, device=device, dtype=dtype)

    h = h.clamp(0, 1)
    h.requires_grad_(True)

    best_score = float("inf")
    best_h = None
    t0 = time.time()

    optimizer = torch.optim.Adam([h], lr=lr)

    print(f"  Adam: n={n}, B={batch_size}, iters={n_iters}, lr={lr}")

    for t in range(n_iters):
        if time.time() - t0 > time_limit:
            print(f"    Time limit, stopping at iter {t}")
            break

        optimizer.zero_grad()
        C = compute_C_batch(h, device)
        loss = C.mean()  # minimize
        loss.backward()
        optimizer.step()

        project_constraints(h)

        if (t + 1) % 500 == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h, device)
                best_idx = torch.argmin(C_vals)
                c_val = C_vals[best_idx].item()
                if c_val < best_score and c_val > 0:
                    best_score = c_val
                    best_h = h[best_idx].detach().cpu().numpy().copy()
                print(f"    iter {t+1}: best C={best_score:.10f}, "
                      f"batch mean={C_vals.mean().item():.8f}")

    # Final extraction
    with torch.no_grad():
        C_vals = compute_C_batch(h, device)
        best_idx = torch.argmin(C_vals)
        c_val = C_vals[best_idx].item()
        if c_val < best_score and c_val > 0:
            best_score = c_val
            best_h = h[best_idx].detach().cpu().numpy().copy()

    # Verify with float64
    if best_h is not None:
        best_h = np.clip(best_h, 0, 1)
        verified = fast_evaluate(best_h)
        print(f"  Verified (float64): C={verified:.10f}")
        return best_h, verified

    return np.full(n, 0.5), 0.5


def hillclimb(h, n_iters=5000, step_size=0.01, time_limit=60):
    """Coordinate-wise hill climbing with adaptive step sizes."""
    n = len(h)
    h = np.clip(h.copy(), 0, 1)
    best_score = fast_evaluate(h)
    best_h = h.copy()
    t0 = time.time()
    improved = 0

    print(f"  Hillclimb: n={n}, iters={n_iters}, start C={best_score:.10f}")

    for t in range(n_iters):
        if time.time() - t0 > time_limit:
            break

        # Pick random index and perturbation
        idx = np.random.randint(n)
        delta = np.random.uniform(-step_size, step_size)
        old_val = h[idx]
        new_val = np.clip(old_val + delta, 0, 1)

        h[idx] = new_val
        score = fast_evaluate(h)

        if score < best_score and score > 0:
            best_score = score
            best_h = h.copy()
            improved += 1
        else:
            h[idx] = old_val  # revert

        if (t + 1) % 1000 == 0:
            print(f"    iter {t+1}: C={best_score:.10f}, improved={improved}")

    print(f"  Hillclimb done: C={best_score:.10f}, improved={improved}")
    return best_h, best_score


def upscale_linear(h, new_n):
    """Linear interpolation upsampling."""
    x_old = np.linspace(0, 1, len(h))
    x_new = np.linspace(0, 1, new_n)
    h_new = np.interp(x_new, x_old, h)
    return np.clip(h_new, 0, 1)


def main():
    parser = argparse.ArgumentParser(description="Erdos Minimum Overlap Optimizer")
    parser.add_argument("--warm-start", type=str, help="Path to JSON with warm-start solution")
    parser.add_argument("--n-start", type=int, default=600, help="Starting discretization size")
    parser.add_argument("--time-limit", type=int, default=300, help="Total time limit (seconds)")
    args = parser.parse_args()

    print("=" * 60)
    print("Erdos Minimum Overlap Optimizer (Problem 1)")
    print("=" * 60)

    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Device: {device}")

    warm_start = None
    if args.warm_start:
        with open(args.warm_start) as f:
            data = json.load(f)
        warm_start = np.array(data["values"], dtype=np.float64)
        ws_score = fast_evaluate(warm_start)
        print(f"Warm-start: n={len(warm_start)}, C={ws_score:.10f}")

    t_total = time.time()

    # Stage 1: Adam at starting resolution
    n = args.n_start
    print(f"\n=== Stage 1: Adam at n={n} ===")
    h, score = adam_optimize(
        n, batch_size=64, n_iters=10000, lr=1e-2,
        device=device, seed=42, time_limit=args.time_limit * 0.3,
        warm_start=warm_start,
    )
    save_result(h, score, f"adam_n{n}")

    # Stage 2: Upsample and refine
    for scale in [4, 4]:
        new_n = len(h) * scale
        if new_n > 100_000:
            break
        remaining = args.time_limit - (time.time() - t_total)
        if remaining < 30:
            print("  Time running low, skipping upscale")
            break

        print(f"\n=== Stage 2: Upsample to n={new_n} ===")
        h_up = upscale_linear(h, new_n)
        score_up = fast_evaluate(h_up)
        print(f"  After upscale: C={score_up:.10f}")

        # Refine upscaled with Adam
        h_refined, score_refined = adam_optimize(
            new_n, batch_size=16, n_iters=5000, lr=5e-3,
            device=device, seed=0,
            time_limit=min(remaining * 0.4, 90),
            warm_start=h_up,
        )

        if score_refined < score_up:
            h, score = h_refined, score_refined
        else:
            h, score = h_up, score_up

        save_result(h, score, f"adam_n{new_n}")

    # Stage 3: Hill-climb polishing
    remaining = args.time_limit - (time.time() - t_total)
    if remaining > 10:
        print(f"\n=== Stage 3: Hill-climb polishing ===")
        h, score = hillclimb(h, n_iters=50000, step_size=0.005,
                             time_limit=remaining - 5)
        save_result(h, score, "hillclimb_final")

    # Final verification with exact evaluator
    print(f"\n=== Final Verification ===")
    exact_score = exact_evaluate({"values": h.tolist()})
    fast_score = fast_evaluate(h)
    print(f"  Fast:  C={fast_score:.12f}")
    print(f"  Exact: C={exact_score:.12f}")
    print(f"  Match: {abs(fast_score - exact_score) < 1e-10}")

    save_result(h, exact_score, "final")

    print(f"\n{'=' * 60}")
    print(f"DONE: C={exact_score:.12f}, n={len(h)}")
    elapsed = time.time() - t_total
    print(f"Total time: {elapsed:.0f}s")
    print("=" * 60)


if __name__ == "__main__":
    main()
