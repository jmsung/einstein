"""Deep CUDA Dinkelbach at n=100k — aggressive beta cascade, many iterations.

Extended beta cascade with many inner iterations. Arena caps at n=100,000.
"""

import modal
import json
import struct

app = modal.App("c2-dinkelbach-deep")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(
    image=image,
    gpu="A100",
    timeout=3600,  # 1 hour max
)
def dinkelbach_deep(f_init_list: list[float]) -> dict:
    """Deep Dinkelbach at n=100k with extended beta cascade and many iterations."""
    import torch
    import numpy as np
    import time

    device = 'cuda'
    dtype = torch.float64

    f_init = np.array(f_init_list, dtype=np.float64)
    n = len(f_init)
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

    def dinkelbach_inner(f_np, lam, beta, n_inner):
        w = np.sqrt(np.maximum(f_np, 0.0))
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
            l2sq = (hh / 3.0) * torch.sum(y0**2 + y0 * y1 + y1**2)
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
        except Exception as e:
            print(f"    L-BFGS exception: {e}")

        f_new = (best_w ** 2).cpu().numpy()
        C_new = gpu_score(torch.tensor(f_new, dtype=dtype, device=device))
        return f_new, C_new

    # Extended beta cascade with MORE outer iterations
    betas = [1e5, 5e5, 1e6, 5e6, 1e7, 5e7, 1e8, 5e8, 1e9, 5e9, 1e10]
    n_outer = 10  # more iterations per beta
    n_inner = 5000  # more L-BFGS steps

    f_best = np.maximum(f_init, 0.0)
    f_t = torch.tensor(f_best, dtype=dtype, device=device)
    C_best = gpu_score(f_t)
    print(f"Initial: n={n}, C={C_best:.15f}")
    t0 = time.time()

    for beta in betas:
        f_current = f_best.copy()
        lam = C_best
        improved_this_beta = False

        for outer in range(n_outer):
            f_new, C_new = dinkelbach_inner(f_current, lam, beta=beta, n_inner=n_inner)
            lam = C_new

            if C_new > C_best and C_new < 1.0 and np.all(np.isfinite(f_new)):
                improvement = C_new - C_best
                C_best = C_new
                f_best = f_new.copy()
                f_current = f_new
                improved_this_beta = True
                print(f"  beta={beta:.0e}, outer={outer}: C={C_best:.15f} (+{improvement:.2e})")

            if outer > 0 and abs(C_new - C_best) < 1e-15:
                break

        elapsed = time.time() - t0
        status = "IMPROVED" if improved_this_beta else "no change"
        print(f"  beta={beta:.0e} done: C={C_best:.15f} ({elapsed:.0f}s) [{status}]")

        # Stop if we've been running > 50 min
        if elapsed > 3000:
            print("  Time limit approaching, stopping.")
            break

    elapsed = time.time() - t0
    print(f"\nFinal: C={C_best:.15f} ({elapsed:.0f}s)")
    print(f"Improvement over seed: {C_best - gpu_score(torch.tensor(f_init, dtype=dtype, device=device)):.2e}")

    return {
        "n": n,
        "score": C_best,
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
    n_floats = len(data) // 8
    f_list = list(struct.unpack(f"<{n_floats}d", data))
    print(f"Loaded {n_floats} values")

    print("=" * 60)
    print("Deep CUDA Dinkelbach at n=100k")
    print("Extended beta cascade [1e5 → 1e10], 10 outer, 5000 inner")
    print("=" * 60)

    t0 = time.time()
    result = dinkelbach_deep.remote(f_list)
    elapsed = time.time() - t0

    print(f"\nResult: C={result['score']:.15f} ({elapsed:.0f}s)")
    print(f"Done.")

    with open(f"results/modal_deep_n100k_{result['score']:.10f}.json", "w") as fh:
        json.dump({
            "problem": "second-autocorrelation-inequality",
            "n_points": result["n"],
            "score": result["score"],
            "values": result["values"],
            "tag": "modal_deep_n100k",
            "elapsed": result["elapsed"],
        }, fh)
    print(f"Saved to results/modal_deep_n100k_{result['score']:.10f}.json")
