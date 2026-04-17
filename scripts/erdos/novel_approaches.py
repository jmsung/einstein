"""Novel approaches for Erdős Minimum Overlap.

These are approaches NOT tried in prior work (34+ experiments):

1. Piecewise constant with variable piece widths (optimize both heights and breakpoints)
2. SOCP relaxation for minimax overlap
3. Spectral construction (Fourier-optimal h)
4. Binary (characteristic function) search at high n
5. Interpolation trick: optimize at multiple n, combine
"""

import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from scipy.signal import fftconvolve
from scipy.optimize import minimize, differential_evolution, linprog

from einstein.erdos.fast import fast_evaluate
from einstein.erdos.evaluator import evaluate as exact_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

SOTA_SCORE = 0.3808703105862199


def fast_eval(h):
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    if n == 0:
        return float("inf")
    h = np.clip(h, 0, 1)
    s = np.sum(h)
    if s == 0:
        return float("inf")
    h = h * (n / 2.0 / s)
    if np.any(h > 1.0):
        return float("inf")
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def normalize(h):
    h = np.clip(h, 0, 1)
    n = len(h)
    s = np.sum(h)
    if s > 0:
        h = h * (n / 2.0 / s)
    h = np.clip(h, 0, 1)
    return h


# ============================================================
# 1. Variable-width piecewise constant
# ============================================================
def piecewise_variable_width(n_pieces=50, n_eval=600, n_iters=5000,
                              time_limit=120, seed=0):
    """Optimize a piecewise constant function with variable piece widths.

    Parameters: heights h_i and widths w_i (i=1..n_pieces).
    The widths are softmax-normalized to sum to 2 (domain [0,2]).
    Heights are sigmoid-clamped to [0,1].
    Integral constraint: sum(h_i * w_i) = 1.
    """
    import torch
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    dtype = torch.float32
    torch.manual_seed(seed)

    # Parameters: raw heights and raw widths
    raw_h = torch.randn(n_pieces, device=device, dtype=dtype) * 0.5
    raw_w = torch.zeros(n_pieces, device=device, dtype=dtype)
    raw_h.requires_grad_(True)
    raw_w.requires_grad_(True)

    opt = torch.optim.Adam([raw_h, raw_w], lr=0.01)
    best_score = float("inf")
    best_h_vec = None
    t0 = time.time()

    for it in range(n_iters):
        if time.time() - t0 > time_limit:
            break

        opt.zero_grad()

        # Convert to heights and widths
        heights = torch.sigmoid(raw_h)  # [0, 1]
        widths = torch.softmax(raw_w, dim=0) * 2.0  # sum = 2

        # Normalize integral to 1: sum(h_i * w_i) = 1
        integral = (heights * widths).sum()
        heights = heights * (1.0 / (integral + 1e-10))
        heights = torch.clamp(heights, 0, 1)

        # Discretize to n_eval points
        cum_widths = torch.cumsum(widths, dim=0)
        cum_widths = cum_widths / cum_widths[-1] * n_eval  # map to [0, n_eval]
        cum_widths = torch.cat([torch.zeros(1, device=device), cum_widths])

        # Build h vector
        h_vec = torch.zeros(n_eval, device=device, dtype=dtype)
        for p in range(n_pieces):
            start = cum_widths[p]
            end = cum_widths[p + 1]
            # Soft assignment: which indices fall in this piece?
            idx = torch.arange(n_eval, device=device, dtype=dtype)
            # Smooth step function
            weight = torch.sigmoid(10 * (idx - start)) * torch.sigmoid(10 * (end - idx))
            h_vec = h_vec + weight * heights[p]

        # Clamp and normalize
        h_vec = torch.clamp(h_vec, 0, 1)
        s = h_vec.sum()
        h_vec = h_vec * (n_eval / 2.0) / (s + 1e-10)
        h_vec = torch.clamp(h_vec, 0, 1)

        # Compute score
        h_batch = h_vec.unsqueeze(0)
        omh = 1.0 - h_batch
        nc = 2 * n_eval - 1
        nfft = 1
        while nfft < nc:
            nfft <<= 1
        H = torch.fft.rfft(h_batch, n=nfft, dim=1)
        G = torch.fft.rfft(omh.flip(1), n=nfft, dim=1)
        corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]
        C = corr.max(dim=1).values * 2.0 / n_eval

        C.backward()
        opt.step()

        if (it + 1) % 500 == 0:
            with torch.no_grad():
                score = C.item()
                if score < best_score:
                    best_score = score
                    best_h_vec = h_vec.detach().cpu().numpy().astype(np.float64)
                    best_h_vec = normalize(best_h_vec)
                    best_score = fast_eval(best_h_vec)
                print(f"  iter {it+1}: C={best_score:.13f}")

    return best_h_vec, best_score


# ============================================================
# 2. Spectral construction
# ============================================================
def spectral_construction(n=600, seed=0):
    """Construct h from spectral properties.

    Key insight: C(t) = n/2 - autocorr(t) / n * 2, where autocorr = sum h[i]h[i+t].
    Minimize max(C) = minimize (n/2 - min(autocorr) / n * 2).
    Equivalently: maximize min autocorrelation.

    For maximum flatness of autocorrelation, use a function whose power spectrum
    |H(w)|^2 is as flat as possible (white-ish spectrum).
    """
    rng = np.random.default_rng(seed)

    best_score = float("inf")
    best_h = None

    for trial in range(50):
        # Generate random phase, flat magnitude spectrum
        # h = IDFT(A * exp(i*phi)) where A is constant
        freqs = np.fft.rfftfreq(n)
        A = np.ones(len(freqs))
        phi = rng.uniform(0, 2 * np.pi, len(freqs))
        phi[0] = 0  # DC component is real

        H = A * np.exp(1j * phi)
        h = np.fft.irfft(H, n=n)

        # Scale to [0, 1] with mean 0.5
        h = (h - h.min()) / (h.max() - h.min() + 1e-30)
        h = normalize(h)

        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()

    # Now try power-law spectra
    for alpha in np.linspace(-2, 2, 20):
        freqs = np.fft.rfftfreq(n)
        A = np.abs(freqs + 1e-10) ** alpha
        A[0] = 1
        phi = rng.uniform(0, 2 * np.pi, len(freqs))
        phi[0] = 0

        H = A * np.exp(1j * phi)
        h = np.fft.irfft(H, n=n)
        h = (h - h.min()) / (h.max() - h.min() + 1e-30)
        h = normalize(h)

        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()

    return best_h, best_score


# ============================================================
# 3. Binary search at high n
# ============================================================
def binary_search_high_n(n=2000, n_trials=100, time_limit=120, seed=0):
    """Search for good binary (0/1) solutions at high n.

    Binary solutions avoid the equioscillation trap.
    h[i] ∈ {0, 1}, exactly n/2 ones.
    """
    rng = np.random.default_rng(seed)
    best_score = float("inf")
    best_h = None
    t0 = time.time()

    for trial in range(n_trials):
        if time.time() - t0 > time_limit:
            break

        # Generate random binary vector with n/2 ones
        h = np.zeros(n)
        ones_idx = rng.choice(n, n // 2, replace=False)
        h[ones_idx] = 1.0

        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()

        # Local search: swap 0s and 1s
        for _ in range(1000):
            zero_idx = np.where(h == 0)[0]
            one_idx = np.where(h == 1)[0]
            i = rng.choice(zero_idx)
            j = rng.choice(one_idx)
            h[i], h[j] = 1.0, 0.0
            new_score = fast_eval(h)
            if new_score < score:
                score = new_score
                if score < best_score:
                    best_score = score
                    best_h = h.copy()
            else:
                h[i], h[j] = 0.0, 1.0

        if (trial + 1) % 10 == 0:
            print(f"  trial {trial+1}: best={best_score:.13f}")

    return best_h, best_score


# ============================================================
# 4. L-BFGS-B with smooth max approximation
# ============================================================
def lbfgsb_smooth_max(h_init, beta=1000, time_limit=120):
    """L-BFGS-B with LogSumExp smooth approximation of max.

    smooth_max(x) = (1/beta) * log(sum(exp(beta * x)))
    """
    n = len(h_init)

    def objective(x):
        h = x.copy()
        s = np.sum(h)
        if s == 0:
            return 1e10, np.zeros(n)
        h = h * (n / 2.0 / s)
        if np.any(h > 1):
            return 1e10, np.zeros(n)

        # Full correlation
        omh = 1.0 - h
        corr = fftconvolve(h, omh[::-1], mode="full")
        C = corr / n * 2

        # Smooth max
        C_shifted = C - np.max(C)  # for numerical stability
        exp_C = np.exp(beta * C_shifted)
        smooth_max = np.max(C) + np.log(np.sum(exp_C)) / beta

        # Approximate gradient via finite differences (for simplicity)
        # Full analytical gradient would be complex
        return smooth_max

    result = minimize(
        objective, h_init,
        method='L-BFGS-B',
        bounds=[(0, 1)] * n,
        options={'maxiter': 5000, 'ftol': 1e-15, 'gtol': 1e-12},
    )

    h_best = normalize(result.x)
    score = fast_eval(h_best)
    return h_best, score


# ============================================================
# 5. Multi-resolution interpolation trick
# ============================================================
def multi_resolution_combine(h_600, n_values=[300, 400, 500, 700, 800],
                              time_limit=120, seed=0):
    """Optimize at multiple resolutions, upsample all to n=600, average the best."""
    import torch
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    dtype = torch.float32

    solutions = []
    t0 = time.time()

    for n in n_values:
        if time.time() - t0 > time_limit:
            break

        # Resample SOTA to this n
        ws = np.interp(np.linspace(0, 1, n), np.linspace(0, 1, 600), h_600)
        ws = normalize(ws)

        # Quick Adam optimization
        h = torch.tensor(ws, dtype=dtype, device=device).unsqueeze(0)
        h.requires_grad_(True)
        opt = torch.optim.Adam([h], lr=0.005)

        for t in range(2000):
            opt.zero_grad()
            hc = torch.clamp(h, 0, 1)
            s = hc.sum(dim=1, keepdim=True)
            hc = hc * (n / 2.0) / (s + 1e-30)
            hc = torch.clamp(hc, 0, 1)
            omh = 1.0 - hc
            nc = 2 * n - 1
            nfft = 1
            while nfft < nc:
                nfft <<= 1
            H = torch.fft.rfft(hc, n=nfft, dim=1)
            G = torch.fft.rfft(omh.flip(1), n=nfft, dim=1)
            corr = torch.fft.irfft(H * G, n=nfft, dim=1)[:, :nc]
            C = corr.max(dim=1).values * 2.0 / n
            C.backward()
            opt.step()
            with torch.no_grad():
                h.clamp_(0, 1)

        h_np = h[0].detach().cpu().numpy().astype(np.float64)
        h_np = normalize(h_np)
        score = fast_eval(h_np)

        # Upsample to 600
        h_600_new = np.interp(np.linspace(0, 1, 600), np.linspace(0, 1, n), h_np)
        h_600_new = normalize(h_600_new)
        score_600 = fast_eval(h_600_new)
        solutions.append((h_600_new, score_600, n))
        print(f"  n={n}: score_native={score:.10f}, score_600={score_600:.10f}")

    # Try averaging combinations
    best_score = SOTA_SCORE
    best_h = h_600.copy()

    # Add SOTA to the pool
    solutions.append((h_600.copy(), SOTA_SCORE, 600))

    rng = np.random.default_rng(seed)
    for _ in range(1000):
        # Random convex combination
        n_pick = rng.integers(2, len(solutions) + 1)
        indices = rng.choice(len(solutions), n_pick, replace=False)
        weights = rng.dirichlet(np.ones(n_pick))
        h_avg = sum(w * solutions[i][0] for i, w in zip(indices, weights))
        h_avg = normalize(h_avg)
        score = fast_eval(h_avg)
        if score < best_score:
            best_score = score
            best_h = h_avg.copy()

    return best_h, best_score


# ============================================================
# 6. Gradient-free coordinate descent with restart
# ============================================================
def coordinate_descent_restart(h_init, n_restarts=10, n_iters=100000,
                                time_limit=300, seed=0):
    """Coordinate descent with periodic random restarts from best."""
    rng = np.random.default_rng(seed)
    global_best_score = fast_eval(h_init)
    global_best_h = h_init.copy()
    t0 = time.time()

    for restart in range(n_restarts):
        if time.time() - t0 > time_limit:
            break

        if restart == 0:
            h = h_init.copy()
        else:
            # Restart from best with perturbation
            sigma = 0.02 * (1 + restart / n_restarts)
            h = global_best_h + rng.normal(0, sigma, len(global_best_h))
            h = normalize(h)

        n = len(h)
        score = fast_eval(h)
        improved = 0

        for it in range(n_iters):
            if time.time() - t0 > time_limit:
                break

            # Pick random coordinate
            j = rng.integers(n)

            # Try a few values
            old_val = h[j]
            best_local_score = score
            best_local_val = old_val

            for delta in [0.001, -0.001, 0.01, -0.01, 0.0001, -0.0001]:
                new_val = np.clip(old_val + delta, 0, 1)
                h[j] = new_val
                # Renormalize
                h_test = normalize(h.copy())
                new_score = fast_eval(h_test)
                if new_score < best_local_score:
                    best_local_score = new_score
                    best_local_val = new_val

            if best_local_val != old_val:
                h[j] = best_local_val
                h = normalize(h)
                score = best_local_score
                improved += 1

                if score < global_best_score:
                    global_best_score = score
                    global_best_h = h.copy()
            else:
                h[j] = old_val

        print(f"  restart {restart}: score={global_best_score:.13f}, improved={improved}")

    return global_best_h, global_best_score


def main():
    print("=" * 70)
    print("NOVEL APPROACHES: Erdős Minimum Overlap (Problem 1)")
    print("=" * 70)

    # Load SOTA
    sota_file = RESULTS_DIR / "sota_together_ai_id9_n600.json"
    with open(sota_file) as f:
        h_sota = np.array(json.load(f)["values"], dtype=np.float64)

    sota_score = fast_eval(h_sota)
    print(f"SOTA: {sota_score:.16f}")

    results = {}

    # 1. Variable-width piecewise constant
    print("\n--- Variable-width piecewise constant ---")
    for n_pieces in [20, 50, 100]:
        t0 = time.time()
        h, s = piecewise_variable_width(n_pieces=n_pieces, n_eval=600,
                                         n_iters=3000, time_limit=60, seed=42)
        if h is not None:
            elapsed = time.time() - t0
            print(f"  {n_pieces} pieces: {s:.13f} ({elapsed:.0f}s)")
            results[f"varwidth_{n_pieces}"] = (h, s)

    # 2. Spectral construction
    print("\n--- Spectral construction ---")
    t0 = time.time()
    h, s = spectral_construction(n=600, seed=42)
    print(f"  Spectral: {s:.13f} ({time.time()-t0:.0f}s)")
    results["spectral"] = (h, s)

    # 3. Binary search
    print("\n--- Binary search at high n ---")
    for n in [600, 1000, 2000]:
        t0 = time.time()
        h, s = binary_search_high_n(n=n, n_trials=20, time_limit=60, seed=42)
        print(f"  Binary n={n}: {s:.13f} ({time.time()-t0:.0f}s)")
        results[f"binary_n{n}"] = (h, s)

    # 4. L-BFGS-B smooth max
    print("\n--- L-BFGS-B smooth max from SOTA ---")
    for beta in [100, 1000, 10000]:
        t0 = time.time()
        h, s = lbfgsb_smooth_max(h_sota.copy(), beta=beta, time_limit=60)
        print(f"  beta={beta}: {s:.13f} ({time.time()-t0:.0f}s)")
        results[f"lbfgsb_beta{beta}"] = (h, s)

    # 5. Multi-resolution combine
    print("\n--- Multi-resolution combination ---")
    t0 = time.time()
    h, s = multi_resolution_combine(h_sota, time_limit=120, seed=42)
    print(f"  Multi-res: {s:.13f} ({time.time()-t0:.0f}s)")
    results["multi_res"] = (h, s)

    # 6. Coordinate descent with restarts
    print("\n--- Coordinate descent with restarts ---")
    t0 = time.time()
    h, s = coordinate_descent_restart(h_sota, n_restarts=5, n_iters=50000,
                                       time_limit=180, seed=42)
    print(f"  Coord descent: {s:.13f} ({time.time()-t0:.0f}s)")
    results["coord_descent"] = (h, s)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY (sorted by score)")
    print("=" * 70)
    for name, (h, s) in sorted(results.items(), key=lambda x: x[1][1]):
        delta = sota_score - s
        print(f"  {name:25s} score={s:.13f} improve={delta:.2e}")

    # Save best
    best_name = min(results, key=lambda k: results[k][1])
    best_h, best_score = results[best_name]
    print(f"\nBest: {best_name} = {best_score:.16f}")

    if best_score < sota_score:
        exact = exact_evaluate({"values": best_h.tolist()})
        print(f"Exact verification: {exact:.16f}")
        result = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(best_h), "score": float(exact),
            "values": [round(float(v), 14) for v in best_h],
            "tag": f"novel_{best_name}",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"novel_best_{best_name}_{exact:.12f}.json"
        with open(fname, "w") as f:
            json.dump(result, f)
        print(f"Saved: {fname}")


if __name__ == "__main__":
    main()
