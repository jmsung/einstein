"""CUDA float64 optimizer for Erdős Minimum Overlap on Modal GPU.

Runs massive parallel Adam + LogSumExp from multiple starting points
on A100 GPU with float64 precision.

Usage:
    modal run scripts/modal_erdos.py
"""

import json
import modal

app = modal.App("erdos-overlap")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(
    image=image,
    gpu="A100",
    timeout=3600,  # 60 min max
)
def optimize_gpu(h_init_list: list[float], tag: str = "",
                 n_iters: int = 50000, batch_size: int = 128,
                 lr: float = 1e-3, beta: float = 5000.0) -> dict:
    """Run LogSumExp Adam optimization on A100 GPU with float64."""
    import torch
    import numpy as np
    from scipy.signal import fftconvolve
    import time

    device = "cuda"
    dtype = torch.float64

    h_init = np.array(h_init_list, dtype=np.float64)
    n = len(h_init)
    nc = 2 * n - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    def exact_score(h):
        """Exact arena verifier score."""
        h = np.array(h, dtype=np.float64)
        h = np.clip(h, 0, 1)
        s = h.sum()
        if s == 0:
            return float("inf")
        target = n / 2.0
        if s != target:
            h = h * (target / s)
        if np.any(h > 1) or np.any(h < 0):
            return float("inf")
        corr = np.correlate(h, 1 - h, mode="full")
        return float(np.max(corr)) / n * 2

    def compute_C_lse(h_batch, beta):
        """Compute smooth-max C via LogSumExp."""
        B, N = h_batch.shape
        h = torch.clamp(h_batch, 0, 1)
        s = h.sum(dim=1, keepdim=True)
        h = h * (N / 2.0) / (s + 1e-30)
        h = torch.clamp(h, 0, 1)

        one_minus_h = 1.0 - h
        H = torch.fft.rfft(h, n=nfft, dim=1)
        G = torch.fft.rfft(one_minus_h.flip(1), n=nfft, dim=1)
        corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]

        # LogSumExp smooth max
        corr_max = corr.max(dim=1, keepdim=True).values
        lse = corr_max.squeeze(1) + (1.0 / beta) * torch.log(
            torch.sum(torch.exp(beta * (corr - corr_max)), dim=1)
        )
        return lse * 2.0 / N

    t0 = time.time()
    start_score = exact_score(h_init)
    print(f"Start: n={n}, C={start_score:.15f}, tag={tag}")
    print(f"Device: {device}, dtype: {dtype}, B={batch_size}, iters={n_iters}")

    # Initialize batch: first is SOTA, rest are small perturbations
    h_t = torch.tensor(h_init, dtype=dtype, device=device).unsqueeze(0).repeat(batch_size, 1)
    noise_scales = [0.0001, 0.0005, 0.001, 0.005]
    for i in range(1, batch_size):
        scale = noise_scales[i % len(noise_scales)]
        h_t[i] += scale * torch.randn(n, dtype=dtype, device=device)
    h_t = h_t.clamp(0, 1)
    h_t.requires_grad_(True)

    optimizer = torch.optim.Adam([h_t], lr=lr)
    best_score = start_score
    best_h = h_init.copy()
    improved_count = 0

    # Beta cascade: start low, increase
    beta_schedule = [(0, beta / 10), (n_iters // 4, beta / 2),
                     (n_iters // 2, beta), (3 * n_iters // 4, beta * 2)]

    current_beta = beta_schedule[0][1]
    schedule_idx = 1

    for t in range(n_iters):
        # Update beta
        if schedule_idx < len(beta_schedule) and t >= beta_schedule[schedule_idx][0]:
            current_beta = beta_schedule[schedule_idx][1]
            schedule_idx += 1

        optimizer.zero_grad()
        C = compute_C_lse(h_t, current_beta)
        loss = C.mean()
        loss.backward()
        optimizer.step()

        with torch.no_grad():
            h_t.clamp_(0, 1)
            s = h_t.sum(dim=1, keepdim=True)
            h_t.mul_(n / 2.0 / (s + 1e-30))
            h_t.clamp_(0, 1)

        if (t + 1) % 2000 == 0:
            with torch.no_grad():
                for b in range(min(batch_size, 32)):
                    hb = h_t[b].cpu().numpy()
                    sc = exact_score(hb)
                    if sc < best_score:
                        best_score = sc
                        best_h = hb.copy()
                        improved_count += 1

                elapsed = time.time() - t0
                print(f"  iter {t+1}: best={best_score:.15f}, "
                      f"beta={current_beta:.0f}, improved={improved_count}, "
                      f"{elapsed:.0f}s")

    # Final extraction
    with torch.no_grad():
        for b in range(batch_size):
            hb = h_t[b].cpu().numpy()
            sc = exact_score(hb)
            if sc < best_score:
                best_score = sc
                best_h = hb.copy()
                improved_count += 1

    # Dyadic mass-transport refinement
    print("\n=== Dyadic mass-transport refinement ===")
    step = 2**-40
    h_q = np.round(best_h / step) * step
    h_q = np.clip(h_q, 0, 1)
    target = n / 2.0
    diff_steps = round((target - h_q.sum()) / step)
    if diff_steps > 0:
        cands = np.where(h_q <= 1.0 - step)[0]
        np.random.shuffle(cands)
        for idx in cands[:abs(diff_steps)]:
            h_q[idx] += step
    elif diff_steps < 0:
        cands = np.where(h_q >= step)[0]
        np.random.shuffle(cands)
        for idx in cands[:abs(diff_steps)]:
            h_q[idx] -= step

    mt_score = exact_score(h_q)
    if mt_score < best_score:
        best_score = mt_score
        best_h = h_q.copy()

    # Run mass transport
    deltas = [1, 2, 4, 8, 16]
    rng = np.random.default_rng(42)
    mt_improved = 0
    for iteration in range(5_000_000):
        if time.time() - t0 > 3500:
            break
        indices = rng.integers(n, size=4)
        if len(set(indices)) < 4:
            continue
        i1, i2, j1, j2 = indices
        d = int(rng.choice(deltas)) * step

        if (h_q[i1] - d < 0 or h_q[i2] - d < 0 or
                h_q[j1] + d > 1 or h_q[j2] + d > 1):
            continue

        h_q[i1] -= d
        h_q[i2] -= d
        h_q[j1] += d
        h_q[j2] += d

        corr = fftconvolve(h_q, (1 - h_q)[::-1], mode="full")
        s = float(np.max(corr)) / n * 2
        if s < best_score:
            best_score = s
            best_h = h_q.copy()
            mt_improved += 1
        else:
            h_q[i1] += d
            h_q[i2] += d
            h_q[j1] -= d
            h_q[j2] -= d

        if (iteration + 1) % 1_000_000 == 0:
            print(f"  MT iter {iteration+1}: C={best_score:.15f}, "
                  f"improved={mt_improved}")

    final_score = exact_score(best_h)
    elapsed = time.time() - t0
    print(f"\nFinal: C={final_score:.15f}, total improved={improved_count + mt_improved}")
    print(f"Total time: {elapsed:.0f}s")

    return {
        "score": float(final_score),
        "values": best_h.tolist(),
        "tag": tag,
        "n": n,
        "improved": improved_count + mt_improved,
        "elapsed": elapsed,
    }


@app.local_entrypoint()
def main():
    # Load all available starting points
    starts = {}

    try:
        with open("results/problem-1-erdos-overlap/together_ai.json") as f:
            starts["together_ai"] = json.load(f)["values"]
    except FileNotFoundError:
        pass

    try:
        with open("results/problem-1-erdos-overlap/ttt_discover.json") as f:
            starts["ttt_discover"] = json.load(f)["values"]
    except FileNotFoundError:
        pass

    if not starts:
        print("No starting solutions found!")
        return

    # Launch parallel GPU jobs with different hyperparameters
    jobs = []
    configs = [
        {"lr": 1e-3, "beta": 5000, "n_iters": 50000, "batch_size": 128},
        {"lr": 5e-4, "beta": 10000, "n_iters": 50000, "batch_size": 128},
        {"lr": 2e-3, "beta": 2000, "n_iters": 50000, "batch_size": 128},
        {"lr": 1e-4, "beta": 20000, "n_iters": 50000, "batch_size": 64},
    ]

    for name, h_init in starts.items():
        for i, cfg in enumerate(configs):
            tag = f"{name}_cfg{i}"
            print(f"Launching: {tag} (lr={cfg['lr']}, beta={cfg['beta']})")
            job = optimize_gpu.spawn(
                h_init, tag=tag,
                n_iters=cfg["n_iters"],
                batch_size=cfg["batch_size"],
                lr=cfg["lr"],
                beta=cfg["beta"],
            )
            jobs.append((tag, job))

    # Collect results
    best_score = float("inf")
    best_result = None
    for tag, job in jobs:
        try:
            result = job.get()
            score = result["score"]
            print(f"{tag}: C={score:.15f}")
            if score < best_score:
                best_score = score
                best_result = result
        except Exception as e:
            print(f"{tag}: ERROR: {e}")

    if best_result:
        print(f"\nBest overall: C={best_score:.15f}")
        with open("results/problem-1-erdos-overlap/best_gpu.json", "w") as f:
            json.dump(best_result, f)
        print("Saved to results/problem-1-erdos-overlap/best_gpu.json")
