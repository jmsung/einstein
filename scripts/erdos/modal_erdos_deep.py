"""Deep optimization for Erdos overlap on Modal A100.

Two strategies:
1. Extended cold-start: 1M iterations with cosine restart
2. Curriculum: optimize at small n, upsample, repeat

Usage:
    modal run scripts/modal_erdos_deep.py
"""

import json
import modal

app = modal.App("erdos-deep")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch==2.3.1", "numpy", "scipy")
)


@app.function(image=image, gpu="A100", timeout=7200)  # 2 hours
def deep_optimize(strategy: str, seed: int = 0) -> dict:
    """Deep optimization with extended compute budget."""
    import torch
    import numpy as np
    from scipy.signal import fftconvolve
    import time

    device = "cuda"
    dtype = torch.float64
    n = 600
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
        h = h * (n / 2.0) / s
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
        nc_local = 2 * N - 1
        nfft_local = 1
        while nfft_local < nc_local:
            nfft_local <<= 1
        H = torch.fft.rfft(h, n=nfft_local, dim=1)
        G = torch.fft.rfft(one_minus_h.flip(1), n=nfft_local, dim=1)
        corr = torch.fft.irfft(H * G, n=nfft_local, dim=1)[:, :nc_local]
        beta = 5000.0
        corr_max = corr.max(dim=1, keepdim=True).values
        lse = corr_max.squeeze(1) + (1.0 / beta) * torch.log(
            torch.sum(torch.exp(beta * (corr - corr_max)), dim=1)
        )
        return lse * 2.0 / N

    def adam_phase(h_init, n_size, batch_size, n_iters, lr, seed_val):
        torch.manual_seed(seed_val)
        if h_init is not None:
            h_t = torch.tensor(h_init, dtype=dtype, device=device).unsqueeze(0).repeat(batch_size, 1)
            h_t[1:] += 0.01 * torch.randn(batch_size - 1, n_size, dtype=dtype, device=device)
        else:
            h_t = torch.rand(batch_size, n_size, dtype=dtype, device=device) * 0.8 + 0.1
        h_t = h_t.clamp(0, 1)
        h_t.requires_grad_(True)

        opt = torch.optim.Adam([h_t], lr=lr)
        sched = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(opt, T_0=n_iters // 5, T_mult=2)

        best_score = float("inf")
        best_h = None

        for t in range(n_iters):
            opt.zero_grad()
            C = compute_C_batch(h_t)
            C.mean().backward()
            opt.step()
            sched.step()

            with torch.no_grad():
                h_t.clamp_(0, 1)
                s = h_t.sum(dim=1, keepdim=True)
                h_t.mul_(n_size / 2.0 / (s + 1e-30))
                h_t.clamp_(0, 1)

            if (t + 1) % 50000 == 0:
                with torch.no_grad():
                    for b in range(min(batch_size, 64)):
                        hb = h_t[b].cpu().numpy()
                        sc = exact_score(np.interp(np.linspace(0, 1, 600),
                                                   np.linspace(0, 1, n_size), hb)
                                         if n_size != 600 else hb)
                        if sc < best_score and sc > 0.35:
                            best_score = sc
                            best_h = h_t[b].cpu().numpy().copy()
                    print(f"    n={n_size} iter {t+1}: best={best_score:.10f}")

            # Elitist respawn every 100k
            if (t + 1) % 100000 == 0:
                with torch.no_grad():
                    C_vals = compute_C_batch(h_t)
                    _, idx = torch.sort(C_vals)
                    keep = batch_size // 2
                    top = h_t[idx[:keep]].clone()
                    fresh = torch.rand(batch_size - keep, n_size, dtype=dtype, device=device) * 0.8 + 0.1
                    h_t = torch.cat([top, fresh], dim=0)
                    h_t.requires_grad_(True)
                    opt = torch.optim.Adam([h_t], lr=lr / 2)
                    sched = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(
                        opt, T_0=max(1, (n_iters - t) // 5), T_mult=2)

        # Final extraction
        with torch.no_grad():
            for b in range(batch_size):
                hb = h_t[b].cpu().numpy()
                if n_size != 600:
                    hb = np.interp(np.linspace(0, 1, 600), np.linspace(0, 1, n_size), hb)
                sc = exact_score(hb)
                if sc < best_score and sc > 0.35:
                    best_score = sc
                    best_h = hb if n_size == 600 else np.interp(
                        np.linspace(0, 1, 600), np.linspace(0, 1, n_size),
                        h_t[b].cpu().numpy())

        return best_h, best_score

    def mass_transport(h, max_iters=5_000_000, time_limit=1800):
        step = 2**-40
        h_q = np.round(h / step) * step
        h_q = np.clip(h_q, 0, 1)
        target = n / 2.0
        diff = round((target - h_q.sum()) / step)
        if diff > 0:
            c = np.where(h_q <= 1.0 - step)[0]
            np.random.shuffle(c)
            for i in c[:abs(diff)]:
                h_q[i] += step
        elif diff < 0:
            c = np.where(h_q >= step)[0]
            np.random.shuffle(c)
            for i in c[:abs(diff)]:
                h_q[i] -= step

        best_score = exact_score(h_q)
        best_h = h_q.copy()
        rng = np.random.default_rng(seed)
        deltas = [1, 2, 4, 8, 16]
        improved = 0
        t0 = time.time()

        for i in range(max_iters):
            if time.time() - t0 > time_limit:
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
                improved += 1
            else:
                h_q[i1] += d
                h_q[i2] += d
                h_q[j1] -= d
                h_q[j2] -= d
            if (i + 1) % 1_000_000 == 0:
                print(f"    MT {i+1}: C={best_score:.12f}, impr={improved}")

        return best_h, best_score

    t0 = time.time()

    if strategy == "extended_coldstart":
        print(f"=== Extended Cold-Start (seed {seed}) ===")
        # Phase 1: 1M iterations at n=600
        h, score = adam_phase(None, 600, 256, 1_000_000, 5e-3, seed)
        print(f"  Adam phase: C={score:.12f}")

        # Phase 2: Mass transport
        if h is not None:
            h_mt, score_mt = mass_transport(h, max_iters=5_000_000, time_limit=3600)
            print(f"  MT phase: C={score_mt:.12f}")
            if score_mt < score:
                h, score = h_mt, score_mt

    elif strategy == "curriculum":
        print(f"=== Curriculum Learning (seed {seed}) ===")
        best_h = None
        best_score = float("inf")

        # Start at small n, increase gradually
        for n_stage, n_iters, bs in [
            (50, 200_000, 512),
            (100, 200_000, 256),
            (200, 200_000, 128),
            (400, 200_000, 64),
            (600, 500_000, 256),
        ]:
            print(f"\n  Stage: n={n_stage}")
            if best_h is not None and len(best_h) != n_stage:
                # Upsample
                best_h = np.interp(
                    np.linspace(0, 1, n_stage),
                    np.linspace(0, 1, len(best_h)),
                    best_h
                )
                best_h = np.clip(best_h, 0, 1)

            h, score = adam_phase(best_h, n_stage, bs, n_iters, 5e-3, seed)
            if h is not None:
                # Convert to n=600 for scoring
                if n_stage != 600:
                    h_600 = np.interp(np.linspace(0, 1, 600), np.linspace(0, 1, n_stage), h)
                else:
                    h_600 = h
                sc = exact_score(h_600)
                print(f"  -> n=600 score: {sc:.12f}")
                if sc < best_score:
                    best_score = sc
                    best_h = h.copy()

        # Final mass transport at n=600
        if best_h is not None:
            if len(best_h) != 600:
                best_h = np.interp(np.linspace(0, 1, 600), np.linspace(0, 1, len(best_h)), best_h)
            best_h = np.clip(best_h, 0, 1)
            s = best_h.sum()
            best_h = best_h * 300 / s
            best_h = np.clip(best_h, 0, 1)
            h_mt, score_mt = mass_transport(best_h, max_iters=5_000_000, time_limit=1800)
            if score_mt < best_score:
                best_score = score_mt
                best_h = h_mt
            h, score = best_h, best_score

    elapsed = time.time() - t0
    final = exact_score(h) if h is not None else float("inf")
    print(f"\nFINAL: C={final:.12f} ({elapsed:.0f}s)")

    return {
        "strategy": strategy,
        "seed": seed,
        "score": float(final),
        "values": h.tolist() if h is not None else [],
        "elapsed": elapsed,
    }


@app.local_entrypoint()
def main():
    jobs = []

    # Extended cold-start with best seeds from previous run
    for seed in [2, 6, 1, 4]:
        tag = f"extended_seed{seed}"
        print(f"Launching: {tag}")
        job = deep_optimize.spawn("extended_coldstart", seed)
        jobs.append((tag, job))

    # Curriculum learning
    for seed in [0, 1, 2, 3]:
        tag = f"curriculum_seed{seed}"
        print(f"Launching: {tag}")
        job = deep_optimize.spawn("curriculum", seed)
        jobs.append((tag, job))

    best_score = float("inf")
    best_result = None
    for tag, job in jobs:
        try:
            result = job.get()
            score = result["score"]
            print(f"{tag}: C={score:.12f}")
            if score < best_score:
                best_score = score
                best_result = result
        except Exception as e:
            print(f"{tag}: ERROR: {e}")

    if best_result:
        print(f"\nBest: C={best_score:.12f}")
        print(f"SOTA: C=0.380870310586")
        with open("results/problem-1-erdos-overlap/best_deep.json", "w") as f:
            json.dump(best_result, f)
        print("Saved!")
