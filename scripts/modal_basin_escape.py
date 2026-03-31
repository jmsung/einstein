"""Basin escape strategies for n=100k — find a DIFFERENT local maximum.

The current basin (C=0.96199) is exhausted. We need to escape it.

Strategies:
  1. Deep Dinkelbach from our own 0.916 basin (different block structure)
  2. Large-LR Adam to kick out + reconverge
  3. Basin hopping: noisy restarts from perturbed public best
  4. Very high beta Dinkelbach (1e11-1e12) with many inner iterations
"""

import modal
import json
import struct

app = modal.App("c2-basin-escape")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("torch", "numpy", "scipy")
)


@app.function(
    image=image,
    gpu="A100",
    timeout=5400,  # 90 min
)
def basin_escape(f_public_list: list[float], f_own_list: list[float]) -> dict:
    """Try multiple strategies to escape the n=100k basin."""
    import torch
    import numpy as np
    import time

    device = 'cuda'
    dtype = torch.float64

    def score_exact_np(f_np):
        from scipy.signal import fftconvolve
        f = np.maximum(np.asarray(f_np, dtype=np.float64), 0)
        if np.sum(f) == 0: return 0.0
        conv = fftconvolve(f, f, mode="full")
        nc = len(conv)
        dx = np.diff(np.linspace(-0.5, 0.5, nc + 2))
        y = np.concatenate(([0], conv, [0]))
        y1, y2 = y[:-1], y[1:]
        l2sq = np.sum((dx / 3.0) * (y1**2 + y1*y2 + y2**2))
        l1 = np.sum(np.abs(conv)) / (nc + 1)
        linf = np.max(np.abs(conv))
        if l1 == 0 or linf == 0: return 0.0
        return float(l2sq / (l1 * linf))

    def compute_C_gpu(h):
        f = torch.clamp(h, min=0)
        if f.dim() == 1:
            f = f.unsqueeze(0)
        B, N = f.shape
        nc = 2*N-1
        nfft = 1
        while nfft < nc: nfft <<= 1
        F = torch.fft.rfft(f, n=nfft, dim=1)
        conv = torch.fft.irfft(F*F, n=nfft, dim=1)[:, :nc]
        csq = torch.sum(conv*conv, dim=1)
        csh = torch.sum(conv[:,:-1]*conv[:,1:], dim=1)
        csum = torch.sum(conv, dim=1)
        cmax = torch.max(conv, dim=1).values
        return (2*csq + csh) / (3*csum*cmax + 1e-30)

    def dinkelbach_refine(f_np, betas, n_outer=7, n_inner=5000, label=""):
        """Full Dinkelbach refinement."""
        n = len(f_np)
        nc = 2*n-1
        nfft = 1
        while nfft < nc: nfft <<= 1

        f_best = np.maximum(f_np.copy(), 0.0)
        C_best = score_exact_np(f_best)
        t0 = time.time()

        for beta in betas:
            f_current = f_best.copy()
            lam = C_best
            for outer in range(n_outer):
                w = np.sqrt(np.maximum(f_current, 0.0))
                w_t = torch.tensor(w, dtype=dtype, device=device).requires_grad_(True)
                best_w = w_t.data.clone()
                best_C_inner = 0.0
                opt = torch.optim.LBFGS([w_t], lr=1.0, max_iter=n_inner,
                    line_search_fn='strong_wolfe', tolerance_grad=1e-16, tolerance_change=1e-17)
                def closure():
                    nonlocal best_w, best_C_inner
                    opt.zero_grad()
                    f = w_t**2
                    F = torch.fft.rfft(f, n=nfft)
                    conv = torch.fft.irfft(F*F, n=nfft)[:nc]
                    conv = torch.maximum(conv, torch.zeros(1, device=device, dtype=dtype))
                    hh = 1.0/(nc+1)
                    zz = torch.zeros(1, device=device, dtype=dtype)
                    y = torch.cat([zz, conv, zz])
                    y0, y1 = y[:-1], y[1:]
                    l2sq = (hh/3.0)*torch.sum(y0**2+y0*y1+y1**2)
                    l1 = torch.sum(conv)/(nc+1)
                    gmax = torch.max(conv)
                    linf = gmax * torch.exp(torch.logsumexp(beta*(conv/(gmax+1e-18)-1.0), dim=0)/beta)
                    obj = l2sq - lam*l1*linf
                    ce = l2sq.item()/(l1.item()*gmax.item()) if l1.item()>0 and gmax.item()>0 else 0.0
                    if ce > best_C_inner and ce < 1.0:
                        best_C_inner = ce
                        best_w = w_t.data.clone()
                    (-obj).backward()
                    return -obj
                try: opt.step(closure)
                except: pass
                f_new = (best_w**2).cpu().numpy()
                C_new = score_exact_np(f_new)
                lam = C_new
                if C_new > C_best and C_new < 1.0 and np.all(np.isfinite(f_new)):
                    C_best = C_new; f_best = f_new.copy(); f_current = f_new
                if outer > 0 and abs(C_new-C_best) < 1e-15: break
            elapsed = time.time()-t0
            if C_best > 0.96199:
                print(f"  [{label}] beta={beta:.0e}: C={C_best:.13f} ({elapsed:.0f}s) !!!")
        return f_best, C_best

    f_public = np.array(f_public_list, dtype=np.float64)
    f_own = np.array(f_own_list, dtype=np.float64)
    n = len(f_public)

    all_results = []
    t0_global = time.time()

    # ---------------------------------------------------------------
    # Strategy 1: Deep Dinkelbach from OUR OWN basin (0.916)
    # ---------------------------------------------------------------
    print("=== Strategy 1: Dinkelbach from our own 0.916 basin ===")
    # Resample own solution to 100k if needed
    if len(f_own) != n:
        x_old = np.linspace(0, 1, len(f_own))
        x_new = np.linspace(0, 1, n)
        f_own_100k = np.maximum(np.interp(x_new, x_old, f_own), 0)
    else:
        f_own_100k = f_own
    C_own_init = score_exact_np(f_own_100k)
    print(f"  Own basin init: C={C_own_init:.10f}")

    f1, C1 = dinkelbach_refine(f_own_100k,
        betas=[1e5, 1e6, 1e7, 5e7, 1e8, 5e8, 1e9, 5e9, 1e10],
        n_outer=7, n_inner=5000, label="own_basin")
    print(f"  Own basin final: C={C1:.13f}")
    all_results.append({"strategy": "own_basin", "score": C1, "values": f1.tolist()})

    # ---------------------------------------------------------------
    # Strategy 2: Large-LR Adam kick + reconverge
    # ---------------------------------------------------------------
    print(f"\n=== Strategy 2: Large-LR Adam kick ({time.time()-t0_global:.0f}s) ===")
    best_kick = score_exact_np(f_public)
    best_kick_f = f_public.copy()

    for lr in [0.1, 0.5, 1.0, 5.0]:
        for seed in range(3):
            torch.manual_seed(seed * 100 + int(lr * 10))
            h = torch.tensor(f_public, dtype=dtype, device=device).unsqueeze(0)
            h = h + torch.randn_like(h) * lr * 0.1  # big noise
            h.requires_grad_(True)
            opt = torch.optim.Adam([h], lr=lr * 0.01)

            # Kick phase: 2000 iters with big LR
            for t in range(2000):
                opt.zero_grad()
                C = compute_C_gpu(h)
                (-C).backward()
                opt.step()
                with torch.no_grad(): h.clamp_(min=0)

            # Reconverge phase: 5000 iters with small LR
            opt2 = torch.optim.Adam([h], lr=1e-4)
            for t in range(5000):
                opt2.zero_grad()
                C = compute_C_gpu(h)
                (-C).backward()
                opt2.step()
                with torch.no_grad(): h.clamp_(min=0)

            f_np = h[0].clamp(min=0).detach().cpu().numpy()
            s = score_exact_np(f_np)
            if s > best_kick:
                best_kick = s
                best_kick_f = f_np.copy()
            print(f"  lr={lr}, seed={seed}: C={s:.12f}")

            if time.time() - t0_global > 2400: break
        if time.time() - t0_global > 2400: break

    # Dinkelbach refine the best kick result
    if best_kick > 0.962:
        f2, C2 = dinkelbach_refine(best_kick_f, betas=[1e8, 1e9, 1e10], n_outer=5, n_inner=3000, label="kick")
    else:
        C2 = best_kick
        f2 = best_kick_f
    print(f"  Best kick: C={C2:.13f}")
    all_results.append({"strategy": "large_lr_kick", "score": C2, "values": f2.tolist()})

    # ---------------------------------------------------------------
    # Strategy 3: Basin hopping — interpolate between public best and random
    # ---------------------------------------------------------------
    print(f"\n=== Strategy 3: Basin hopping ({time.time()-t0_global:.0f}s) ===")
    rng = np.random.default_rng(42)
    best_hop = score_exact_np(f_public)
    best_hop_f = f_public.copy()

    for alpha in [0.01, 0.02, 0.05, 0.1, 0.2]:
        for seed in range(5):
            rng2 = np.random.default_rng(seed + int(alpha * 1000))
            f_perturbed = (1 - alpha) * f_public + alpha * rng2.exponential(np.mean(f_public[f_public > 0]), size=n)
            f_perturbed = np.maximum(f_perturbed, 0)

            # Quick Dinkelbach from this perturbed start
            f_hop, C_hop = dinkelbach_refine(f_perturbed,
                betas=[1e7, 1e9, 1e10], n_outer=3, n_inner=2000, label=f"hop_a{alpha}_s{seed}")

            if C_hop > best_hop:
                best_hop = C_hop
                best_hop_f = f_hop.copy()
                print(f"  alpha={alpha}, seed={seed}: C={C_hop:.13f} ***NEW BEST***")
            else:
                print(f"  alpha={alpha}, seed={seed}: C={C_hop:.13f}")

            if time.time() - t0_global > 4200: break
        if time.time() - t0_global > 4200: break

    all_results.append({"strategy": "basin_hopping", "score": best_hop, "values": best_hop_f.tolist()})

    # ---------------------------------------------------------------
    # Summary
    # ---------------------------------------------------------------
    elapsed = time.time() - t0_global
    all_results.sort(key=lambda x: x["score"], reverse=True)
    print(f"\n{'='*60}")
    print(f"Results ({elapsed:.0f}s, {elapsed/60:.1f}min):")
    for r in all_results:
        beats = " *** BEATS TARGET" if r["score"] > 0.96209 else ""
        print(f"  {r['score']:.15f}  {r['strategy']}{beats}")

    best = all_results[0]
    print(f"\nBest: C={best['score']:.15f} ({best['strategy']})")
    print(f"Target: > 0.96209")
    print(f"Public best: 0.96199")
    print(f"Gap: {best['score'] - 0.96199:.2e}")
    print(f"{'BEATS TARGET!' if best['score'] > 0.96209 else 'Below target'}")

    return best


@app.local_entrypoint()
def main():
    import time

    # Load public best 100k
    with open("results/public_best_100k.npy", "rb") as fh:
        magic = fh.read(6)
        version = struct.unpack("<BB", fh.read(2))
        hl = struct.unpack("<H", fh.read(2))[0] if version[0] == 1 else struct.unpack("<I", fh.read(4))[0]
        fh.read(hl)
        data = fh.read()
    f_public = list(struct.unpack(f"<{len(data)//8}d", data))

    # Load our best from-scratch solution (from H100 run)
    try:
        with open("results/modal_h100_0.9619870594.json") as fh:
            d = json.load(fh)
        f_own = d["values"]
    except:
        # Fallback: use the multiscale Adam result
        with open("results/c2_n48640_0.90828955_multiscale_final.json") as fh:
            d = json.load(fh)
        f_own = d["values"]

    print("=" * 60)
    print("Basin Escape — 3 strategies to break 0.96209")
    print("=" * 60)

    t0 = time.time()
    result = basin_escape.remote(f_public, f_own)
    elapsed = time.time() - t0

    print(f"\nResult: C={result['score']:.15f} ({elapsed:.0f}s)")
    print(f"{'BEATS TARGET!' if result['score'] > 0.96209 else 'Below target'}")

    with open(f"results/modal_escape_{result['score']:.10f}.json", "w") as fh:
        json.dump({
            "problem": "second-autocorrelation-inequality",
            "n_points": len(result["values"]),
            "score": result["score"],
            "values": result["values"],
            "tag": f"basin_escape_{result['strategy']}",
        }, fh)
