"""Sweep n from 50k to 100k — find the best resolution under the arena cap.

For each n: interpolate seed → Dinkelbach optimize → report C.
"""

import modal
import json
import struct

app = modal.App("c2-resolution-sweep")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(
    image=image,
    gpu="A100",
    timeout=3600,
)
def optimize_at_n(f_seed_list: list[float], n_target: int) -> dict:
    """Dinkelbach at a specific resolution."""
    import torch
    import numpy as np
    import time

    device = 'cuda'
    dtype = torch.float64

    # Resample seed to target n
    f_seed = np.array(f_seed_list, dtype=np.float64)
    if len(f_seed) != n_target:
        x_old = np.linspace(0, 1, len(f_seed))
        x_new = np.linspace(0, 1, n_target)
        f_init = np.maximum(np.interp(x_new, x_old, f_seed), 0)
    else:
        f_init = np.maximum(f_seed, 0)

    n = n_target
    nc = 2 * n - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    def gpu_score(f_t):
        F = torch.fft.rfft(f_t, n=nfft)
        conv = torch.fft.irfft(F * F, n=nfft)[:nc]
        c_sq = torch.sum(conv * conv)
        c_shift = torch.sum(conv[:-1] * conv[1:])
        c_sum = torch.sum(conv)
        c_max = torch.max(conv)
        return ((2 * c_sq + c_shift) / (3 * c_sum * c_max)).item()

    # Extended beta cascade
    betas = [1e5, 1e6, 1e7, 5e7, 1e8, 5e8, 1e9, 5e9, 1e10]

    f_best = f_init.copy()
    f_t = torch.tensor(f_best, dtype=dtype, device=device)
    C_best = gpu_score(f_t)
    C_init = C_best

    print(f"  n={n}: init C={C_init:.10f}")
    t0 = time.time()

    for beta in betas:
        f_current = f_best.copy()
        lam = C_best

        for outer in range(7):  # 7 outer iters per beta
            w = np.sqrt(np.maximum(f_current, 0.0))
            w_t = torch.tensor(w, dtype=dtype, device=device).requires_grad_(True)
            best_w = w_t.data.clone()
            best_C_inner = 0.0

            optimizer = torch.optim.LBFGS(
                [w_t], lr=1.0, max_iter=3000,
                line_search_fn='strong_wolfe',
                tolerance_grad=1e-15, tolerance_change=1e-16
            )

            def closure():
                nonlocal best_w, best_C_inner
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
                if C_exact > best_C_inner and C_exact < 1.0:
                    best_C_inner = C_exact
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

        elapsed = time.time() - t0
        if elapsed > 600:  # 10 min per resolution max
            break

    elapsed = time.time() - t0
    improvement = C_best - C_init
    print(f"  n={n}: final C={C_best:.13f} (init={C_init:.6f}, +{improvement:.2e}, {elapsed:.0f}s)")

    return {
        "n": n,
        "score": C_best,
        "score_init": C_init,
        "values": f_best.tolist(),
        "elapsed": elapsed,
    }


@app.local_entrypoint()
def main():
    import time

    # Load 100k seed
    with open("results/public_best_100k.npy", "rb") as fh:
        magic = fh.read(6)
        version = struct.unpack("<BB", fh.read(2))
        header_len = struct.unpack("<H", fh.read(2))[0] if version[0] == 1 else struct.unpack("<I", fh.read(4))[0]
        fh.read(header_len)
        data = fh.read()
    f_list = list(struct.unpack(f"<{len(data)//8}d", data))

    print("=" * 60)
    print("Resolution Sweep: n = 50k to 100k")
    print("Find the sweet spot under the arena n≤100k cap")
    print("=" * 60)

    # Sweep resolutions — focus on range near 100k
    resolutions = [50000, 60000, 70000, 80000, 85000, 90000, 95000, 97000, 99000, 100000]

    results = []
    for n in resolutions:
        print(f"\n--- n={n:,} ---")
        t0 = time.time()
        result = optimize_at_n.remote(f_list, n)
        elapsed = time.time() - t0
        results.append(result)
        print(f"  C={result['score']:.13f} ({elapsed:.0f}s)")

        # Save
        with open(f"results/modal_sweep_n{n}_{result['score']:.8f}.json", "w") as fh:
            json.dump({
                "problem": "second-autocorrelation-inequality",
                "n_points": result["n"],
                "score": result["score"],
                "values": result["values"],
                "tag": f"resolution_sweep_n{n}",
                "elapsed": result["elapsed"],
            }, fh)

    # Summary
    print("\n" + "=" * 60)
    print("Resolution sweep results:")
    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        print(f"  n={r['n']:>6,}: C={r['score']:.13f} (init={r['score_init']:.6f})")

    best = max(results, key=lambda x: x["score"])
    print(f"\nBest: n={best['n']:,}, C={best['score']:.15f}")
