"""GPU-accelerated MTS for Problem 12 — Flat Polynomials.

Runs massively parallel tabu search on A100 GPU using PyTorch.
Each CUDA thread runs an independent tabu search trajectory.

Usage:
    modal run scripts/modal_flat_poly.py
"""

import modal
import json
import time

app = modal.App("flat-poly-mts")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy")
)

# Known solutions (descending order)
SOTA_DESC = [
    -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, 1,
    1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, 1,
    -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1,
    1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1,
]

THIRD_DESC = [
    1, 1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, -1,
    1, -1, 1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1,
    1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1,
    -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, 1, -1, 1, -1,
]


@app.function(
    image=image,
    gpu="A100",
    timeout=3600,
)
def gpu_mts_campaign(n_trajectories: int = 1000, n_iters: int = 100_000) -> dict:
    """Run many parallel tabu search trajectories on GPU."""
    import torch
    import numpy as np

    device = "cuda"
    dtype = torch.float64
    N_EVAL = 8192  # power of 2 for fast FFT
    N_COEFFS = 70
    NORM = np.sqrt(71)

    print(f"GPU MTS: {n_trajectories} trajectories x {n_iters} iters")
    print(f"Eval points: {N_EVAL}, Device: {torch.cuda.get_device_name()}")

    # Precompute twiddle factors on GPU
    k = torch.arange(N_EVAL, device=device, dtype=dtype)
    j = torch.arange(N_COEFFS, device=device, dtype=dtype)
    # twiddle[j, k] = exp(-2πi j k / N)
    angles = -2 * torch.pi * j[:, None] * k[None, :] / N_EVAL
    twiddle_re = torch.cos(angles)  # (70, N_EVAL)
    twiddle_im = torch.sin(angles)  # (70, N_EVAL)

    # Initialize trajectories: mix of warm-starts + random
    rng = np.random.default_rng(42)
    init = np.zeros((n_trajectories, N_COEFFS), dtype=np.float64)

    # First few are SOTA and #3 perturbed
    sota_asc = SOTA_DESC[::-1]
    third_asc = THIRD_DESC[::-1]
    for i in range(min(100, n_trajectories)):
        base = sota_asc if i < 50 else third_asc
        init[i] = base
        # Perturb by 5-20 random flips
        k_flips = rng.integers(5, 21)
        flips = rng.choice(N_COEFFS, size=k_flips, replace=False)
        for f in flips:
            init[i, f] *= -1

    # Rest are random
    for i in range(100, n_trajectories):
        init[i] = rng.choice([-1, 1], size=N_COEFFS)

    # Move to GPU
    coeffs = torch.tensor(init, device=device, dtype=dtype)  # (B, 70)

    # Compute initial FFT values for all trajectories
    # fft_re[b, k] = sum_j coeffs[b, j] * cos(angles[j, k])
    fft_re = coeffs @ twiddle_re  # (B, N_EVAL)
    fft_im = coeffs @ twiddle_im  # (B, N_EVAL)
    power = fft_re ** 2 + fft_im ** 2  # (B, N_EVAL)
    scores = torch.sqrt(torch.max(power, dim=1).values) / NORM  # (B,)

    best_scores = scores.clone()
    best_coeffs = coeffs.clone()

    # Tabu lists: tabu_until[b, j] = iteration when position j becomes available
    tabu_until = torch.zeros(n_trajectories, N_COEFFS, device=device, dtype=torch.long)

    global_best_score = float(torch.min(best_scores).item())
    global_best_idx = int(torch.argmin(best_scores).item())
    print(f"Init best: {global_best_score:.10f}")

    t0 = time.time()

    for it in range(n_iters):
        # For each trajectory, evaluate all 70 neighbors
        # delta[b, j] = -2 * coeffs[b, j]
        deltas = -2.0 * coeffs  # (B, 70)

        # Compute score for each flip: batch over trajectories, loop over flips
        # For efficiency, process in chunks of 10 flips
        all_neighbor_scores = torch.full(
            (n_trajectories, N_COEFFS), float("inf"), device=device, dtype=dtype
        )

        for j in range(N_COEFFS):
            # new_fft_re = fft_re + deltas[:, j:j+1] * twiddle_re[j:j+1, :]
            d = deltas[:, j:j+1]  # (B, 1)
            new_re = fft_re + d * twiddle_re[j:j+1, :]  # (B, N_EVAL)
            new_im = fft_im + d * twiddle_im[j:j+1, :]  # (B, N_EVAL)
            new_power = new_re ** 2 + new_im ** 2
            new_score = torch.sqrt(torch.max(new_power, dim=1).values) / NORM
            all_neighbor_scores[:, j] = new_score

        # Mask tabu positions (except aspiration)
        is_tabu = tabu_until > it
        is_aspiration = all_neighbor_scores < best_scores.unsqueeze(1)
        blocked = is_tabu & ~is_aspiration
        all_neighbor_scores[blocked] = float("inf")

        # Pick best neighbor for each trajectory
        best_j = torch.argmin(all_neighbor_scores, dim=1)  # (B,)
        best_neighbor_score = all_neighbor_scores[
            torch.arange(n_trajectories, device=device), best_j
        ]

        # Accept moves
        for b_start in range(0, n_trajectories, 100):
            b_end = min(b_start + 100, n_trajectories)
            for b in range(b_start, b_end):
                j = best_j[b].item()
                d = deltas[b, j].item()
                coeffs[b, j] *= -1
                fft_re[b] += d * twiddle_re[j]
                fft_im[b] += d * twiddle_im[j]
                tenure = rng.integers(n_iters // 10, n_iters * 12 // 100 + 1)
                tabu_until[b, j] = it + tenure

        scores = best_neighbor_score

        # Update best
        improved = scores < best_scores
        best_scores[improved] = scores[improved]
        best_coeffs[improved] = coeffs[improved]

        current_best = float(torch.min(best_scores).item())
        if current_best < global_best_score:
            global_best_score = current_best
            global_best_idx = int(torch.argmin(best_scores).item())
            elapsed = time.time() - t0
            print(f"  iter {it}: NEW BEST {global_best_score:.10f} ({elapsed:.0f}s)")

        if it % 10000 == 0 and it > 0:
            elapsed = time.time() - t0
            rate = it * n_trajectories * N_COEFFS / elapsed
            print(
                f"  iter {it}/{n_iters}: best={global_best_score:.10f} "
                f"({rate/1e6:.1f}M evals/s, {elapsed:.0f}s)"
            )

    elapsed = time.time() - t0
    total_evals = n_iters * n_trajectories * N_COEFFS
    print(f"\nDone in {elapsed:.0f}s ({elapsed/60:.1f} min)")
    print(f"Total evals: {total_evals/1e9:.1f}B")
    print(f"Rate: {total_evals/elapsed/1e6:.1f}M evals/s")
    print(f"Best score (N={N_EVAL}): {global_best_score:.10f}")

    # Get best coefficients
    best = best_coeffs[global_best_idx].cpu().numpy().astype(int).tolist()

    # Verify at N=1M on CPU
    coeffs_np = np.array(best, dtype=np.float64)
    fft_1m = np.fft.fft(coeffs_np, n=1_000_000)
    exact_score = float(np.max(np.abs(fft_1m)) / np.sqrt(71))
    print(f"Exact score (N=1M): {exact_score:.10f}")
    print(f"Arena SOTA: 1.2809320528")
    print(f"Arena #3:   1.3409252795")
    print(f"Gap to #3:  {exact_score - 1.3409252795:+.8f}")

    # Collect top 10 unique solutions
    top_indices = torch.argsort(best_scores)[:10]
    top_solutions = []
    for idx in top_indices:
        c = best_coeffs[idx].cpu().numpy().astype(int).tolist()
        s = float(best_scores[idx].item())
        fft_v = np.fft.fft(np.array(c, dtype=np.float64), n=1_000_000)
        exact = float(np.max(np.abs(fft_v)) / np.sqrt(71))
        top_solutions.append({
            "score_fast": s,
            "score_exact": exact,
            "coefficients_ascending": c,
        })

    return {
        "best_score_fast": global_best_score,
        "best_score_exact": exact_score,
        "best_coefficients_ascending": best,
        "best_coefficients_descending": best[::-1],
        "top_10": top_solutions,
        "n_trajectories": n_trajectories,
        "n_iters": n_iters,
        "total_evals": total_evals,
        "elapsed_seconds": elapsed,
    }


@app.local_entrypoint()
def main():
    print("Launching GPU MTS campaign on A100...")
    print("1000 trajectories x 100K iters = 7B evals")
    print()

    result = gpu_mts_campaign.remote(n_trajectories=1000, n_iters=100_000)

    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    print(f"Best exact score: {result['best_score_exact']:.10f}")
    print(f"Arena SOTA:       1.2809320528")
    print(f"Arena #3:         1.3409252795")
    print(f"Gap to #3:        {result['best_score_exact'] - 1.3409252795:+.8f}")
    print()

    print("Top 10 solutions:")
    for i, sol in enumerate(result["top_10"]):
        print(f"  #{i+1}: exact={sol['score_exact']:.10f}")

    # Save results
    fname = f"results/problem-12-flat-polynomials/gpu_mts_{result['best_score_exact']:.8f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {fname}")

    if result["best_score_exact"] < 1.3409252795 - 1e-5:
        print("\n>>> BEATS #3! Ready for submission.")
    elif result["best_score_exact"] < 1.2809320528 - 1e-5:
        print("\n>>> BEATS SOTA! Ready for submission.")
