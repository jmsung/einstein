"""Massive cold-start optimizer for Erdos overlap on Modal A100.

Runs many seeds in parallel with 500k iterations each at float64.
The hypothesis: with enough compute, cold-start might find the SOTA basin
or a new basin below 0.38087.

Usage:
    modal run scripts/modal_erdos_coldstart.py
"""

import json
import modal

app = modal.App("erdos-coldstart")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(image=image, gpu="A100", timeout=3600)
def coldstart_gpu(seed: int, n: int = 600, n_iters: int = 300000,
                  batch_size: int = 256, lr: float = 5e-3) -> dict:
    """Cold-start Adam optimization on A100 with float64."""
    import torch
    import numpy as np
    from scipy.signal import fftconvolve
    import time

    device = "cuda"
    dtype = torch.float64
    torch.manual_seed(seed)
    np.random.seed(seed)

    nc = 2 * n - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    def exact_score(h):
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

    def compute_C_batch(h_batch):
        B, N = h_batch.shape
        h = torch.clamp(h_batch, 0, 1)
        s = h.sum(dim=1, keepdim=True)
        h = h * (N / 2.0) / (s + 1e-30)
        h = torch.clamp(h, 0, 1)

        one_minus_h = 1.0 - h
        H = torch.fft.rfft(h, n=nfft, dim=1)
        G = torch.fft.rfft(one_minus_h.flip(1), n=nfft, dim=1)
        corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]

        # LogSumExp smooth max with adaptive beta
        beta = 5000.0
        corr_max = corr.max(dim=1, keepdim=True).values
        lse = corr_max.squeeze(1) + (1.0 / beta) * torch.log(
            torch.sum(torch.exp(beta * (corr - corr_max)), dim=1)
        )
        return lse * 2.0 / N

    t0 = time.time()
    print(f"Seed {seed}: n={n}, B={batch_size}, iters={n_iters}, float64 A100")

    # Random initialization
    h = torch.rand(batch_size, n, device=device, dtype=dtype) * 0.8 + 0.1
    h.requires_grad_(True)

    optimizer = torch.optim.Adam([h], lr=lr)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, n_iters, eta_min=lr/100)

    best_score = float("inf")
    best_h = None
    stagnant = 0

    for t in range(n_iters):
        optimizer.zero_grad()
        C = compute_C_batch(h)
        loss = C.mean()
        loss.backward()
        optimizer.step()
        scheduler.step()

        with torch.no_grad():
            h.clamp_(0, 1)
            s = h.sum(dim=1, keepdim=True)
            h.mul_(n / 2.0 / (s + 1e-30))
            h.clamp_(0, 1)

        # Elitist respawn every 50k iters
        if (t + 1) % 50000 == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h)
                _, sorted_idx = torch.sort(C_vals)
                keep = batch_size // 2
                top_h = h[sorted_idx[:keep]].clone()
                fresh = torch.rand(batch_size - keep, n, device=device, dtype=dtype) * 0.8 + 0.1
                h = torch.cat([top_h, fresh], dim=0)
                h.requires_grad_(True)
                optimizer = torch.optim.Adam([h], lr=lr / (1 + t / n_iters))
                scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                    optimizer, n_iters - t, eta_min=lr/100)

        if (t + 1) % 10000 == 0:
            with torch.no_grad():
                C_vals = compute_C_batch(h)
                best_idx = torch.argmin(C_vals)
                c_val = C_vals[best_idx].item()

                # Verify with exact scorer periodically
                if (t + 1) % 50000 == 0:
                    hb = h[best_idx].cpu().numpy()
                    sc = exact_score(hb)
                    if sc < best_score and sc > 0.35:
                        best_score = sc
                        best_h = hb.copy()
                        stagnant = 0
                    else:
                        stagnant += 1

                elapsed = time.time() - t0
                lr_now = optimizer.param_groups[0]['lr']
                print(f"  seed {seed} iter {t+1}: torch_best={c_val:.10f}, "
                      f"exact_best={best_score:.10f}, lr={lr_now:.6f}, {elapsed:.0f}s")

    # Final extraction
    with torch.no_grad():
        for b in range(batch_size):
            hb = h[b].cpu().numpy()
            sc = exact_score(hb)
            if sc < best_score and sc > 0.35:
                best_score = sc
                best_h = hb.copy()

    # Mass transport refinement
    if best_h is not None:
        print(f"\n  seed {seed}: Mass transport from C={best_score:.10f}")
        step = 2**-32
        h_q = np.round(best_h / step) * step
        h_q = np.clip(h_q, 0, 1)
        target = n / 2.0
        diff = round((target - h_q.sum()) / step)
        if diff > 0:
            cands = np.where(h_q <= 1.0 - step)[0]
            np.random.shuffle(cands)
            for idx in cands[:abs(diff)]:
                h_q[idx] += step
        elif diff < 0:
            cands = np.where(h_q >= step)[0]
            np.random.shuffle(cands)
            for idx in cands[:abs(diff)]:
                h_q[idx] -= step

        mt_score = exact_score(h_q)
        if mt_score < best_score:
            best_score = mt_score
            best_h = h_q.copy()

        rng = np.random.default_rng(seed)
        deltas = [1, 2, 4, 8]
        mt_improved = 0
        for i in range(2_000_000):
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
            if (i + 1) % 500_000 == 0:
                print(f"  seed {seed} MT {i+1}: C={best_score:.12f}, impr={mt_improved}")

    elapsed = time.time() - t0
    final = exact_score(best_h) if best_h is not None else float("inf")
    print(f"\n  seed {seed} FINAL: C={final:.12f} ({elapsed:.0f}s)")

    return {
        "seed": seed,
        "score": float(final),
        "values": best_h.tolist() if best_h is not None else [],
        "elapsed": elapsed,
    }


@app.local_entrypoint()
def main():
    # Launch 16 seeds in parallel
    jobs = []
    for seed in range(16):
        print(f"Launching seed {seed}")
        job = coldstart_gpu.spawn(seed)
        jobs.append((seed, job))

    best_score = float("inf")
    best_result = None
    for seed, job in jobs:
        try:
            result = job.get()
            score = result["score"]
            print(f"seed {seed}: C={score:.12f}")
            if score < best_score:
                best_score = score
                best_result = result
        except Exception as e:
            print(f"seed {seed}: ERROR: {e}")

    if best_result:
        print(f"\nBest: C={best_score:.12f}")
        print(f"SOTA: C=0.380870310586")
        with open("results/problem-1-erdos-overlap/best_coldstart.json", "w") as f:
            json.dump(best_result, f)
        print("Saved!")
