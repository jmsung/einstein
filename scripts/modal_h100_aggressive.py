"""Aggressive H100 optimizer — find new basins at n=100k to beat SOTA.

The existing 100k basin is proven exhausted. We need a NEW basin.
Strategy:
  1. Batched Adam from scratch at n=768 (find diverse structures)
  2. Upsample best to 100k
  3. Dinkelbach refinement at 100k
  4. Repeat with many random seeds — search for better basins
  5. Also try: Adam directly at n=100k from the public best (different optimizer = different basin?)
"""

import modal
import json
import struct

app = modal.App("c2-h100-aggressive")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(
    image=image,
    gpu="H100",
    timeout=5400,  # 90 min
    memory=32768,  # 32GB RAM
)
def aggressive_search(f_seed_list: list[float]) -> dict:
    """Multi-strategy search for new basins at n<=100k."""
    import torch
    import numpy as np
    import time

    device = 'cuda'
    print(f"GPU: {torch.cuda.get_device_name()}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

    # ---------------------------------------------------------------
    # Scoring functions
    # ---------------------------------------------------------------
    def score_exact(f_np):
        """Exact C using float64 numpy (matches arena)."""
        from scipy.signal import fftconvolve
        f = np.maximum(np.asarray(f_np, dtype=np.float64), 0)
        if np.sum(f) == 0:
            return 0.0
        conv = fftconvolve(f, f, mode="full")
        nc = len(conv)
        dx = np.diff(np.linspace(-0.5, 0.5, nc + 2))
        y = np.concatenate(([0], conv, [0]))
        y1, y2 = y[:-1], y[1:]
        l2_sq = np.sum((dx / 3.0) * (y1**2 + y1*y2 + y2**2))
        l1 = np.sum(np.abs(conv)) / (nc + 1)
        l_inf = np.max(np.abs(conv))
        if l1 == 0 or l_inf == 0:
            return 0.0
        return float(l2_sq / (l1 * l_inf))

    def compute_C_batch_gpu(h_batch):
        """Batch C on GPU, float64."""
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
        return (2 * c_sq + c_shift) / (3 * c_sum * c_max + 1e-30)

    def dinkelbach_refine(f_np, betas=None, n_outer=5, n_inner=3000):
        """Dinkelbach refinement on GPU float64."""
        n = len(f_np)
        nc = 2 * n - 1
        nfft = 1
        while nfft < nc:
            nfft <<= 1
        dtype = torch.float64

        if betas is None:
            betas = [1e5, 1e6, 1e7, 5e7, 1e8, 5e8, 1e9, 5e9, 1e10]

        def gpu_score(f_t):
            F = torch.fft.rfft(f_t, n=nfft)
            conv = torch.fft.irfft(F * F, n=nfft)[:nc]
            c_sq = torch.sum(conv * conv)
            c_shift = torch.sum(conv[:-1] * conv[1:])
            c_sum = torch.sum(conv)
            c_max = torch.max(conv)
            return ((2 * c_sq + c_shift) / (3 * c_sum * c_max)).item()

        f_best = np.maximum(f_np.copy(), 0.0)
        C_best = gpu_score(torch.tensor(f_best, dtype=dtype, device=device))

        for beta in betas:
            f_current = f_best.copy()
            lam = C_best
            for outer in range(n_outer):
                w = np.sqrt(np.maximum(f_current, 0.0))
                w_t = torch.tensor(w, dtype=dtype, device=device).requires_grad_(True)
                best_w = w_t.data.clone()
                best_C = 0.0

                optimizer = torch.optim.LBFGS(
                    [w_t], lr=1.0, max_iter=n_inner,
                    line_search_fn='strong_wolfe',
                    tolerance_grad=1e-16, tolerance_change=1e-17
                )

                def closure():
                    nonlocal best_w, best_C
                    optimizer.zero_grad()
                    f = w_t ** 2
                    F = torch.fft.rfft(f, n=nfft)
                    conv = torch.fft.irfft(F * F, n=nfft)[:nc]
                    conv = torch.maximum(conv, torch.zeros(1, device=device, dtype=dtype))
                    hh = 1.0 / (nc + 1)
                    zz = torch.zeros(1, device=device, dtype=dtype)
                    y = torch.cat([zz, conv, zz])
                    y0, y1 = y[:-1], y[1:]
                    l2sq = (hh / 3.0) * torch.sum(y0**2 + y0*y1 + y1**2)
                    l1 = torch.sum(conv) / (nc + 1)
                    g_max = torch.max(conv)
                    linf_proxy = g_max * torch.exp(
                        torch.logsumexp(beta * (conv / (g_max + 1e-18) - 1.0), dim=0) / beta
                    )
                    obj = l2sq - lam * l1 * linf_proxy
                    C_exact = l2sq.item() / (l1.item() * g_max.item()) if l1.item() > 0 and g_max.item() > 0 else 0.0
                    if C_exact > best_C and C_exact < 1.0:
                        best_C = C_exact
                        best_w = w_t.data.clone()
                    loss = -obj
                    loss.backward()
                    return loss

                try:
                    optimizer.step(closure)
                except:
                    pass

                f_new = (best_w ** 2).cpu().numpy()
                C_new = gpu_score(torch.tensor(f_new, dtype=dtype, device=device))
                lam = C_new
                if C_new > C_best and C_new < 1.0 and np.all(np.isfinite(f_new)):
                    C_best = C_new
                    f_best = f_new.copy()
                    f_current = f_new
                if outer > 0 and abs(C_new - C_best) < 1e-15:
                    break

        return f_best, C_best

    # ---------------------------------------------------------------
    # Strategy 1: Batched Adam at small n, then upsample to 100k
    # ---------------------------------------------------------------
    t0 = time.time()
    dtype = torch.float64
    all_results = []

    print("\n=== Strategy 1: Batched Adam at n=768 → upsample to 100k ===")
    for seed in range(20):  # 20 diverse seeds
        torch.manual_seed(seed * 137)
        n_small = 768
        B = 256
        h = torch.rand(B, n_small, device=device, dtype=dtype) * 0.5
        h.requires_grad_(True)

        # Phase 1: Explore (15k iters)
        opt = torch.optim.Adam([h], lr=3e-2)
        for t in range(15000):
            opt.zero_grad()
            C = compute_C_batch_gpu(h)
            (-C.mean()).backward()
            with torch.no_grad():
                eta = 1e-3 / (t + 1) ** 0.65
                h.grad += eta * torch.randn_like(h.grad)
            opt.step()
            with torch.no_grad():
                h.clamp_(min=0)

        # Phase 2: Exploit (15k iters)
        with torch.no_grad():
            C_vals = compute_C_batch_gpu(h)
            _, idx = torch.sort(C_vals, descending=True)
            top = h[idx[:B//2]].clone()
            fresh = torch.rand(B - B//2, n_small, device=device, dtype=dtype) * 0.5
            h = torch.cat([top, fresh], dim=0).requires_grad_(True)
        opt = torch.optim.Adam([h], lr=5e-3)
        for t in range(15000):
            opt.zero_grad()
            C = compute_C_batch_gpu(h)
            (-C.mean()).backward()
            opt.step()
            with torch.no_grad():
                h.clamp_(min=0)
            if (t + 1) % 5000 == 0:
                with torch.no_grad():
                    C_vals = compute_C_batch_gpu(h)
                    _, idx = torch.sort(C_vals, descending=True)
                    top = h[idx[:B//2]].clone()
                    fresh = torch.rand(B - B//2, n_small, device=device, dtype=dtype) * 0.5
                    h = torch.cat([top, fresh], dim=0).requires_grad_(True)
                    opt = torch.optim.Adam([h], lr=5e-3)

        # Extract best
        with torch.no_grad():
            C_vals = compute_C_batch_gpu(h)
            best_idx = torch.argmax(C_vals)
            f_small = h[best_idx].clamp(min=0).cpu().numpy()
        C_small = score_exact(f_small)

        # Upsample to 100k
        x_old = np.linspace(0, 1, len(f_small))
        x_new = np.linspace(0, 1, 100000)
        f_100k = np.maximum(np.interp(x_new, x_old, f_small), 0)
        C_100k = score_exact(f_100k)

        # Dinkelbach refine at 100k (quick: 3 betas)
        f_ref, C_ref = dinkelbach_refine(f_100k, betas=[1e6, 1e8, 1e10], n_outer=3, n_inner=2000)

        elapsed = time.time() - t0
        print(f"  seed={seed}: small C={C_small:.6f}, 100k C={C_100k:.6f}, refined C={C_ref:.10f} ({elapsed:.0f}s)")
        all_results.append({"seed": seed, "score": C_ref, "values": f_ref.tolist(), "strategy": "adam_upsample"})

        if elapsed > 2400:  # 40 min budget for strategy 1
            break

    # ---------------------------------------------------------------
    # Strategy 2: Adam directly at n=100k from public best (different optimizer)
    # ---------------------------------------------------------------
    print(f"\n=== Strategy 2: Adam at n=100k from seed ({time.time()-t0:.0f}s) ===")
    f_seed = np.array(f_seed_list, dtype=np.float64)

    for lr_mult in [1.0, 0.1, 0.01]:
        h = torch.tensor(f_seed, dtype=dtype, device=device).unsqueeze(0)
        h = h + torch.randn_like(h) * 0.001  # tiny noise
        h = h.clone().requires_grad_(True)
        opt = torch.optim.Adam([h], lr=1e-3 * lr_mult)
        best_s = score_exact(f_seed)
        best_f = f_seed.copy()

        for t in range(20000):
            opt.zero_grad()
            C = compute_C_batch_gpu(h)
            (-C).backward()
            opt.step()
            with torch.no_grad():
                h.clamp_(min=0)
            if (t + 1) % 5000 == 0:
                f_np = h[0].clamp(min=0).detach().cpu().numpy()
                s = score_exact(f_np)
                if s > best_s and s < 1.0:
                    best_s = s
                    best_f = f_np.copy()
                print(f"    lr={1e-3*lr_mult:.0e}, iter {t+1}: C={best_s:.12f}")

        all_results.append({"seed": f"adam_lr{lr_mult}", "score": best_s, "values": best_f.tolist(), "strategy": "adam_100k"})

        if time.time() - t0 > 4200:  # 70 min total budget
            break

    # ---------------------------------------------------------------
    # Strategy 3: Perturb public best structure (support modifications)
    # ---------------------------------------------------------------
    print(f"\n=== Strategy 3: Structural perturbation of seed ({time.time()-t0:.0f}s) ===")
    rng = np.random.default_rng(42)
    best_struct_s = score_exact(f_seed)
    best_struct_f = f_seed.copy()

    for trial in range(500):
        f_trial = f_seed.copy()
        # Random structural changes
        action = rng.integers(5)
        if action == 0:
            # Shift a block of support
            start = rng.integers(len(f_trial) - 100)
            shift = rng.integers(-5, 6)
            block = f_trial[start:start+100].copy()
            f_trial[start:start+100] = 0
            new_start = max(0, min(start + shift, len(f_trial) - 100))
            f_trial[new_start:new_start+100] = block
        elif action == 1:
            # Scale a random region
            start = rng.integers(len(f_trial) - 50)
            f_trial[start:start+50] *= rng.uniform(0.5, 2.0)
        elif action == 2:
            # Add mass at a new position
            pos = rng.integers(len(f_trial))
            f_trial[pos] += rng.exponential(1.0)
        elif action == 3:
            # Remove mass from a position
            nz = np.where(f_trial > 0)[0]
            if len(nz) > 0:
                idx = rng.choice(nz)
                f_trial[idx] = 0
        elif action == 4:
            # Swap two regions
            a = rng.integers(len(f_trial) - 20)
            b = rng.integers(len(f_trial) - 20)
            tmp = f_trial[a:a+20].copy()
            f_trial[a:a+20] = f_trial[b:b+20]
            f_trial[b:b+20] = tmp

        f_trial = np.maximum(f_trial, 0)
        s = score_exact(f_trial)
        if s > best_struct_s:
            best_struct_s = s
            best_struct_f = f_trial.copy()
            print(f"  trial {trial}: C={best_struct_s:.12f} (action={action})")

        if time.time() - t0 > 4800:  # 80 min total
            break

    # Dinkelbach refine best structural perturbation
    if best_struct_s > score_exact(f_seed):
        f_ref, C_ref = dinkelbach_refine(best_struct_f, betas=[1e7, 1e8, 1e9, 1e10], n_outer=5, n_inner=3000)
        all_results.append({"seed": "struct_perturb", "score": C_ref, "values": f_ref.tolist(), "strategy": "structural"})
        print(f"  After Dinkelbach: C={C_ref:.12f}")

    # ---------------------------------------------------------------
    # Final summary
    # ---------------------------------------------------------------
    elapsed = time.time() - t0
    all_results.sort(key=lambda x: x["score"], reverse=True)

    print(f"\n{'='*60}")
    print(f"Top 5 results ({elapsed:.0f}s total):")
    for i, r in enumerate(all_results[:5]):
        marker = " *** BEST" if i == 0 else ""
        print(f"  {r['score']:.15f}  {r['strategy']} seed={r['seed']}{marker}")

    best = all_results[0]
    print(f"\nBest: C={best['score']:.15f}")
    print(f"Target: > 0.96209")
    print(f"{'BEATS TARGET!' if best['score'] > 0.96209 else 'Below target'}")

    return best


@app.local_entrypoint()
def main():
    import time

    with open("results/public_best_100k.npy", "rb") as fh:
        magic = fh.read(6)
        version = struct.unpack("<BB", fh.read(2))
        header_len = struct.unpack("<H", fh.read(2))[0] if version[0] == 1 else struct.unpack("<I", fh.read(4))[0]
        fh.read(header_len)
        data = fh.read()
    f_list = list(struct.unpack(f"<{len(data)//8}d", data))

    print("=" * 60)
    print("H100 Aggressive Basin Search")
    print("3 strategies × many seeds, 90 min budget")
    print("=" * 60)

    t0 = time.time()
    result = aggressive_search.remote(f_list)
    elapsed = time.time() - t0

    print(f"\nFinal: C={result['score']:.15f} ({elapsed:.0f}s)")
    print(f"Target: > 0.96209")
    print(f"{'BEATS TARGET!' if result['score'] > 0.96209 else 'Below target'}")

    with open(f"results/modal_h100_{result['score']:.10f}.json", "w") as fh:
        json.dump({
            "problem": "second-autocorrelation-inequality",
            "n_points": len(result["values"]),
            "score": result["score"],
            "values": result["values"],
            "tag": f"h100_{result['strategy']}",
        }, fh)
    print(f"Saved to results/modal_h100_{result['score']:.10f}.json")
