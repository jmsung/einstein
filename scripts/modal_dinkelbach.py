"""CUDA float64 Dinkelbach optimizer on Modal GPU.

Runs the proven Dinkelbach + LogSumExp + L-BFGS approach on A100 GPU
with float64 precision — the same method REDACTED used to reach C=REDACTED.

Strategy:
  1. Upload public best 100k solution as starting point
  2. Run Dinkelbach at multiple resolutions (100k, 150k, 200k, 250k, 300k)
  3. Download best result for arena submission
"""

import modal
import json

app = modal.App("c2-dinkelbach")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(
    image=image,
    gpu="A100",
    timeout=1800,  # 30 min max
)
def dinkelbach_gpu(f_init_list: list[float], n_target: int,
                   betas: list[float] | None = None,
                   n_outer: int = 5, n_inner: int = 5000) -> dict:
    """Run Dinkelbach optimization on GPU with float64."""
    import torch
    import numpy as np
    from scipy.signal import fftconvolve
    import time

    device = 'cuda'
    dtype = torch.float64

    # Prepare initial solution
    f_init = np.array(f_init_list, dtype=np.float64)

    # Resample to target n if needed
    if len(f_init) != n_target:
        x_old = np.linspace(0, 1, len(f_init))
        x_new = np.linspace(0, 1, n_target)
        f_init = np.maximum(np.interp(x_new, x_old, f_init), 0)

    n = n_target
    nc = 2 * n - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    if betas is None:
        betas = [1e5, 1e6, 1e7, 5e7, 1e8, 5e8, 1e9]

    def gpu_score(f_t):
        """Exact C on GPU."""
        F = torch.fft.rfft(f_t, n=nfft)
        conv = torch.fft.irfft(F * F, n=nfft)[:nc]
        c_sq = torch.sum(conv * conv)
        c_shift = torch.sum(conv[:-1] * conv[1:])
        c_sum = torch.sum(conv)
        c_max = torch.max(conv)
        return ((2 * c_sq + c_shift) / (3 * c_sum * c_max)).item()

    def dinkelbach_inner(f_np, lam, beta, n_inner_iters):
        """One Dinkelbach inner problem via L-BFGS."""
        w = np.sqrt(np.maximum(f_np, 0.0))
        w_t = torch.tensor(w, dtype=dtype, device=device).requires_grad_(True)
        best_w = w_t.data.clone()
        best_C = 0.0

        optimizer = torch.optim.LBFGS(
            [w_t], lr=1.0, max_iter=n_inner_iters,
            line_search_fn='strong_wolfe',
            tolerance_grad=1e-14, tolerance_change=1e-15
        )

        def closure():
            nonlocal best_w, best_C
            optimizer.zero_grad()
            f = w_t ** 2
            F = torch.fft.rfft(f, n=nfft)
            conv = torch.fft.irfft(F * F, n=nfft)[:nc]
            conv = torch.maximum(conv, torch.zeros(1, device=device, dtype=dtype))

            # Simpson's rule L2²
            hh = 1.0 / (nc + 1)
            zz = torch.zeros(1, device=device, dtype=dtype)
            y = torch.cat([zz, conv, zz])
            y0, y1 = y[:-1], y[1:]
            l2sq = (hh / 3.0) * torch.sum(y0**2 + y0 * y1 + y1**2)
            l1 = torch.sum(conv) / (nc + 1)

            # LogSumExp L∞ proxy
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
        except Exception as e:
            print(f"    L-BFGS exception: {e}")

        f_new = (best_w ** 2).cpu().numpy()
        C_new = gpu_score(torch.tensor(f_new, dtype=dtype, device=device))
        return f_new, C_new

    # Main optimization loop
    f_best = np.maximum(f_init.astype(np.float64), 0.0)
    f_t = torch.tensor(f_best, dtype=dtype, device=device)
    C_best = gpu_score(f_t)

    print(f"Initial: n={n}, C={C_best:.13f}")
    t0 = time.time()

    for beta in betas:
        f_current = f_best.copy()
        lam = C_best

        for outer in range(n_outer):
            f_new, C_new = dinkelbach_inner(f_current, lam, beta=beta, n_inner_iters=n_inner)
            lam = C_new

            if C_new > C_best and C_new < 1.0 and np.all(np.isfinite(f_new)):
                improvement = C_new - C_best
                C_best = C_new
                f_best = f_new.copy()
                f_current = f_new
                print(f"  beta={beta:.0e}, outer={outer}: C={C_best:.13f} (+{improvement:.2e})")

            if outer > 0 and abs(C_new - C_best) < 1e-14:
                break

        elapsed = time.time() - t0
        print(f"  beta={beta:.0e} done: C={C_best:.13f} ({elapsed:.0f}s)")

    # Final exact score
    f_t = torch.tensor(f_best, dtype=dtype, device=device)
    final_C = gpu_score(f_t)

    elapsed = time.time() - t0
    print(f"\nFinal: n={n}, C={final_C:.15f} ({elapsed:.0f}s)")

    return {
        "n": n,
        "score": final_C,
        "values": f_best.tolist(),
        "elapsed": elapsed,
    }


@app.local_entrypoint()
def main():
    import struct
    import time

    # Load public best 100k solution — read .npy manually to avoid numpy dependency
    # .npy format: 6-byte magic + 2-byte version + 2-byte header_len + header + data
    with open("results/public_best_100k.npy", "rb") as fh:
        magic = fh.read(6)
        version = struct.unpack("<BB", fh.read(2))
        if version[0] == 1:
            header_len = struct.unpack("<H", fh.read(2))[0]
        else:
            header_len = struct.unpack("<I", fh.read(4))[0]
        header = fh.read(header_len).decode("latin1")
        data = fh.read()

    # Parse as float64 array
    n_floats = len(data) // 8
    f_list = list(struct.unpack(f"<{n_floats}d", data))
    print(f"Loaded {n_floats} values from public_best_100k.npy")

    print("=" * 60)
    print("CUDA Float64 Dinkelbach on Modal A100")
    print("=" * 60)

    # Run at multiple resolutions — the unexplored ones
    resolutions = [100_000, 150_000, 200_000]
    results = []

    for n in resolutions:
        print(f"\n--- n={n:,} ---")
        t0 = time.time()

        result = dinkelbach_gpu.remote(
            f_list, n,
            betas=[1e5, 1e6, 1e7, 5e7, 1e8, 5e8, 1e9],
            n_outer=5, n_inner=3000,
        )

        elapsed = time.time() - t0
        print(f"  Score: C={result['score']:.15f} ({elapsed:.0f}s total)")
        results.append(result)

        # Save result
        with open(f"results/modal_n{n}_{result['score']:.8f}.json", "w") as fh:
            json.dump({
                "problem": "second-autocorrelation-inequality",
                "n_points": result["n"],
                "score": result["score"],
                "values": result["values"],
                "tag": f"modal_dinkelbach_n{n}",
                "elapsed": result["elapsed"],
            }, fh)
        print(f"  Saved to results/modal_n{n}_{result['score']:.8f}.json")

    # Summary
    print("\n" + "=" * 60)
    print("Results:")
    for r in sorted(results, key=lambda x: x["score"], reverse=True):
        marker = " *** BEST" if r["score"] == max(x["score"] for x in results) else ""
        print(f"  n={r['n']:>7,}: C={r['score']:.15f}{marker}")

    best = max(results, key=lambda x: x["score"])
    print(f"\nBest: n={best['n']:,}, C={best['score']:.15f}")
    print(f"Target: C > REDACTED")
    print(f"{'DONE!' if best['score'] > REDACTED else 'Below target'}")
