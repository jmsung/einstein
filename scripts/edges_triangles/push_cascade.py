"""Push P13 score via multi-resolution cascade + free x-optimization.

Strategy:
1. Load current best 500-point solution
2. Double resolution to 1000+ points by interpolation
3. Optimize all x-positions with L-BFGS (float64, scallop-aware)
4. Greedily prune back to 500 points
5. Polish the 500-point solution
6. Repeat cascade at higher resolution if improved

The key insight: our 500-point basin may be a discretization artifact.
Working at higher resolution explores a smoother landscape.
"""

import json
import sys
from pathlib import Path

import numpy as np
import torch
from scipy.optimize import minimize

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import (
    compute_densities,
    compute_score,
    turan_row,
)

SOLUTION_PATH = Path("results/problem-13-edges-triangles/solution-best.json")
RESULTS_DIR = Path("results/problem-13-edges-triangles")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def load_best():
    with open(SOLUTION_PATH) as f:
        sol = json.load(f)
    w = np.array(sol["weights"])
    return w


def extract_xs(w):
    """Extract sorted x-positions from weight matrix."""
    xs = []
    for row in w:
        row = row / row.sum()
        x, _ = compute_densities(row)
        xs.append(x)
    return np.sort(xs)


def xs_to_score(xs_inner):
    """Compute score from x-positions using Turán y-values."""
    xs_inner = np.sort(xs_inner)
    xs = np.concatenate([[0.0], xs_inner, [1.0]])

    # Compute y-values via Turán construction
    ys = np.zeros_like(xs)
    ys[-1] = 1.0
    for i in range(1, len(xs) - 1):
        p = turan_row(np.clip(xs[i], 0.0, 0.95))
        _, ys[i] = compute_densities(p)

    # Score
    area = 0.0
    max_gap = 0.0
    for i in range(len(xs) - 1):
        h = xs[i + 1] - xs[i]
        if h <= 0:
            continue
        max_gap = max(max_gap, h)
        dy = ys[i + 1] - ys[i]
        if dy < 0:
            area += ys[i + 1] * h
        elif dy <= 3 * h:
            area += -dy**2 / 6 + ys[i + 1] * h
        else:
            area += ys[i] * h + 1.5 * h**2
    return -(area + 10 * max_gap)


def xs_to_weights(xs_inner):
    """Convert x-positions to weight matrix."""
    xs_inner = np.sort(xs_inner)
    m = len(xs_inner)
    w = np.zeros((m, 20))
    for i, x in enumerate(xs_inner):
        w[i] = turan_row(np.clip(x, 1e-14, 0.95))
    return w


# ---------- Torch-based L-BFGS optimizer ----------

def razborov_y_torch(x):
    """Compute Razborov minimum triangle density for edge density x (torch)."""
    # Bipartite region
    y = torch.zeros_like(x)
    mask_scallop = x > 0.5

    if mask_scallop.any():
        xs = x[mask_scallop]
        # k = floor(1/(1-x))
        k = torch.floor(1.0 / (1.0 - xs + 1e-15)).clamp(min=2, max=19)

        # For each scallop k, the Razborov envelope is:
        # y = 1 - 3*s2 + 2*s3 where s2 = kc^2 + r^2, s3 = kc^3 + r^3
        # c = (2k + sqrt(4k^2 - 4k(k+1)x)) / (2k(k+1))
        # r = 1 - kc

        disc = 4 * k**2 - 4 * k * (k + 1) * xs
        disc = disc.clamp(min=0)
        sqrt_disc = torch.sqrt(disc)
        c = (2 * k + sqrt_disc) / (2 * k * (k + 1))

        # Clamp c
        c_lo = 1.0 / (k + 1)
        c_hi = 1.0 / k
        c = c.clamp(min=0).clamp(max=1)
        c = torch.where(c < c_lo, c_lo, c)
        c = torch.where(c > c_hi, c_hi, c)

        r = (1.0 - k * c).clamp(min=0)
        s2 = k * c**2 + r**2
        s3 = k * c**3 + r**3
        y_scallop = 1.0 - 3.0 * s2 + 2.0 * s3
        y[mask_scallop] = y_scallop.clamp(min=0)

    return y


def score_torch(xs_inner_sorted):
    """Differentiable score computation in torch (float64)."""
    zeros = torch.zeros(1, dtype=torch.float64)
    ones = torch.ones(1, dtype=torch.float64)

    xs = torch.cat([zeros, xs_inner_sorted, ones])
    ys_inner = razborov_y_torch(xs_inner_sorted)
    ys = torch.cat([zeros, ys_inner, ones])

    hs = xs[1:] - xs[:-1]
    dys = ys[1:] - ys[:-1]

    area = torch.zeros(1, dtype=torch.float64)
    for i in range(len(hs)):
        h = hs[i]
        if h <= 1e-15:
            continue
        dy = dys[i]
        y1 = ys[i + 1]
        y0 = ys[i]

        # Smooth piecewise using soft conditions
        # dy < 0:     area += y1 * h
        # 0<=dy<=3h:  area += -dy^2/6 + y1*h
        # dy > 3h:    area += y0*h + 1.5*h^2
        if dy.item() < 0:
            area = area + y1 * h
        elif dy.item() <= 3 * h.item():
            area = area + (-dy**2 / 6 + y1 * h)
        else:
            area = area + (y0 * h + 1.5 * h**2)

    max_gap = hs.max()
    return -(area + 10 * max_gap)


def optimize_lbfgs_torch(xs_inner, n_iters=200, lr=1e-4):
    """Optimize x-positions using PyTorch L-BFGS with scallop bounds."""
    xs_sorted = np.sort(xs_inner)
    raw = torch.tensor(xs_sorted, dtype=torch.float64, requires_grad=True)

    best_score = -1e10
    best_xs = xs_sorted.copy()

    optimizer = torch.optim.LBFGS([raw], lr=lr, max_iter=20,
                                   line_search_fn="strong_wolfe")

    for iteration in range(n_iters):
        def closure():
            optimizer.zero_grad()
            # Sort and clamp
            sorted_x, _ = torch.sort(raw)
            sorted_x = sorted_x.clamp(min=1e-6, max=0.95 - 1e-6)
            neg_score = -score_torch(sorted_x)  # minimize negative score
            neg_score.backward()
            return neg_score

        optimizer.step(closure)

        with torch.no_grad():
            sorted_x, _ = torch.sort(raw)
            sorted_x = sorted_x.clamp(min=1e-6, max=0.95 - 1e-6)
            s = score_torch(sorted_x).item()

        if s > best_score:
            best_score = s
            best_xs = sorted_x.detach().numpy().copy()
            if iteration % 10 == 0:
                print(f"  iter {iteration}: {s:.16f} (new best)")
        elif iteration % 50 == 0:
            print(f"  iter {iteration}: {s:.16f}")

    return best_xs, best_score


# ---------- Multi-resolution cascade ----------

def upsample(xs_inner, factor=2):
    """Insert midpoints between every pair of consecutive x-positions."""
    xs = np.sort(xs_inner)
    new_xs = []
    for i in range(len(xs)):
        new_xs.append(xs[i])
        if i < len(xs) - 1:
            for j in range(1, factor):
                frac = j / factor
                mid = xs[i] + frac * (xs[i + 1] - xs[i])
                new_xs.append(mid)
    return np.array(new_xs)


def prune_greedy(xs_inner, target_n):
    """Greedily remove points that contribute least to score."""
    xs = list(np.sort(xs_inner))
    while len(xs) > target_n:
        best_score = -1e10
        best_idx = -1
        for i in range(len(xs)):
            trial = xs[:i] + xs[i + 1:]
            s = xs_to_score(np.array(trial))
            if s > best_score:
                best_score = s
                best_idx = i
        xs.pop(best_idx)
        if len(xs) % 100 == 0:
            print(f"  pruned to {len(xs)}: {best_score:.16f}")
    return np.array(xs)


def prune_fast(xs_inner, target_n):
    """Fast greedy pruning using segment area estimates."""
    xs_sorted = np.sort(xs_inner)

    while len(xs_sorted) > target_n:
        # Compute contribution of each point
        xs_full = np.concatenate([[0.0], xs_sorted, [1.0]])
        ys_full = np.zeros_like(xs_full)
        ys_full[-1] = 1.0
        for i in range(1, len(xs_full) - 1):
            p = turan_row(np.clip(xs_full[i], 0.0, 0.95))
            _, ys_full[i] = compute_densities(p)

        # Score without each interior point
        min_loss = 1e10
        best_drop = -1
        for idx in range(1, len(xs_full) - 1):
            # Removing this point merges two segments into one
            i = idx
            if i == 0 or i == len(xs_full) - 1:
                continue
            # Current: seg (i-1,i) + seg(i,i+1)
            h1 = xs_full[i] - xs_full[i - 1]
            h2 = xs_full[i + 1] - xs_full[i]
            h_merged = h1 + h2

            dy1 = ys_full[i] - ys_full[i - 1]
            dy2 = ys_full[i + 1] - ys_full[i]
            dy_merged = ys_full[i + 1] - ys_full[i - 1]

            def seg_area(y0, y1, h):
                if h <= 0:
                    return 0
                dy = y1 - y0
                if dy < 0:
                    return y1 * h
                elif dy <= 3 * h:
                    return -dy**2 / 6 + y1 * h
                else:
                    return y0 * h + 1.5 * h**2

            a_current = seg_area(ys_full[i - 1], ys_full[i], h1) + \
                        seg_area(ys_full[i], ys_full[i + 1], h2)
            a_merged = seg_area(ys_full[i - 1], ys_full[i + 1], h_merged)

            loss = a_merged - a_current  # how much area increases by removing
            # Also check if gap penalty increases
            if h_merged > 0.05:
                loss += 10 * (h_merged - 0.05)

            if loss < min_loss:
                min_loss = loss
                best_drop = idx - 1  # index into xs_sorted

        xs_sorted = np.delete(xs_sorted, best_drop)
        if len(xs_sorted) % 100 == 0:
            s = xs_to_score(xs_sorted)
            print(f"  pruned to {len(xs_sorted)}: {s:.16f}")

    return xs_sorted


# ---------- Scipy L-BFGS-B with scallop bounds ----------

def optimize_scipy_lbfgsb(xs_inner, max_iter=500):
    """L-BFGS-B optimization with box bounds per scallop."""
    xs_sorted = np.sort(xs_inner)

    def neg_score(x_flat):
        return -xs_to_score(np.sort(x_flat))

    # Bounds: each x in [epsilon, 0.95-epsilon]
    bounds = [(1e-6, 0.95 - 1e-6)] * len(xs_sorted)

    result = minimize(
        neg_score, xs_sorted, method="L-BFGS-B",
        bounds=bounds,
        options={"maxiter": max_iter, "ftol": 1e-18, "gtol": 1e-14,
                 "maxfun": 50000},
    )
    print(f"  L-BFGS-B: {-result.fun:.16f} ({result.nit} iters, {result.message})")
    return np.sort(result.x), -result.fun


# ---------- Random restart + local optimization ----------

def random_restart(xs_inner, n_restarts=50, noise_scale=1e-5):
    """Random perturbations + local optimization."""
    best_score = xs_to_score(xs_inner)
    best_xs = xs_inner.copy()
    print(f"  baseline: {best_score:.16f}")

    for restart in range(n_restarts):
        # Perturb
        noise = np.random.randn(len(xs_inner)) * noise_scale
        xs_trial = np.clip(xs_inner + noise, 1e-6, 0.95 - 1e-6)

        # Local optimization
        xs_opt, score = optimize_scipy_lbfgsb(xs_trial, max_iter=100)
        if score > best_score:
            best_score = score
            best_xs = xs_opt.copy()
            print(f"  restart {restart}: NEW BEST {score:.16f} (Δ={score - xs_to_score(xs_inner):.2e})")
        elif restart % 10 == 0:
            print(f"  restart {restart}: {score:.16f}")

    return best_xs, best_score


# ---------- Point swap optimization ----------

def optimize_swap(xs_inner, n_candidates=5000, n_rounds=10):
    """Try swapping each point with a candidate from a fine grid."""
    xs = np.sort(xs_inner).copy()
    candidates = np.linspace(1e-6, 0.95 - 1e-6, n_candidates)

    best_score = xs_to_score(xs)
    improved = True
    round_num = 0

    while improved and round_num < n_rounds:
        improved = False
        round_num += 1
        for i in range(len(xs)):
            original_x = xs[i]
            best_local_score = best_score
            best_candidate = original_x

            for cand in candidates:
                xs[i] = cand
                s = xs_to_score(xs)
                if s > best_local_score:
                    best_local_score = s
                    best_candidate = cand
                    improved = True

            xs[i] = best_candidate
            if best_candidate != original_x:
                best_score = best_local_score

        print(f"  swap round {round_num}: {best_score:.16f}")

    return xs, best_score


# ---------- Main ----------

def main():
    print("Loading best solution...")
    w = load_best()
    xs_inner = extract_xs(w)
    baseline_score = xs_to_score(xs_inner)
    print(f"Baseline score: {baseline_score:.16f}")
    print(f"N points: {len(xs_inner)}")

    best_xs = xs_inner.copy()
    best_score = baseline_score

    # Phase 1: L-BFGS-B optimization from current position
    print("\n=== Phase 1: L-BFGS-B from current position ===")
    xs_opt, score = optimize_scipy_lbfgsb(xs_inner, max_iter=1000)
    if score > best_score:
        best_score = score
        best_xs = xs_opt.copy()
        print(f"  Improved to {best_score:.16f} (Δ={best_score - baseline_score:.2e})")

    # Phase 2: Random restarts
    print("\n=== Phase 2: Random restarts with L-BFGS-B ===")
    for scale in [1e-6, 1e-5, 1e-4, 1e-3]:
        print(f"\n  noise_scale={scale:.0e}")
        xs_opt, score = random_restart(best_xs, n_restarts=20, noise_scale=scale)
        if score > best_score:
            best_score = score
            best_xs = xs_opt.copy()
            print(f"  >>> NEW BEST: {best_score:.16f}")

    # Phase 3: Multi-resolution cascade
    print("\n=== Phase 3: Multi-resolution cascade ===")
    for factor in [2, 3]:
        print(f"\n  upsample factor={factor}")
        xs_up = upsample(best_xs, factor=factor)
        n_up = len(xs_up)
        print(f"  upsampled to {n_up} points")

        # Score at higher resolution
        score_up = xs_to_score(xs_up)
        print(f"  upsampled score: {score_up:.16f}")

        # Optimize at higher resolution (use a few L-BFGS-B iterations)
        print(f"  optimizing {n_up} points...")
        xs_up_opt, score_up_opt = optimize_scipy_lbfgsb(xs_up, max_iter=200)
        print(f"  optimized upsampled score: {score_up_opt:.16f}")

        # Prune back to 500
        print(f"  pruning to 500...")
        xs_pruned = prune_fast(xs_up_opt, target_n=500)
        score_pruned = xs_to_score(xs_pruned)
        print(f"  pruned score: {score_pruned:.16f}")

        # Polish after pruning
        xs_polished, score_polished = optimize_scipy_lbfgsb(xs_pruned, max_iter=500)
        print(f"  polished score: {score_polished:.16f}")

        if score_polished > best_score:
            best_score = score_polished
            best_xs = xs_polished.copy()
            print(f"  >>> CASCADE IMPROVED: {best_score:.16f}")

    # Phase 4: Fine-grained point swaps
    print("\n=== Phase 4: Point swap optimization ===")
    xs_swapped, score_swapped = optimize_swap(best_xs, n_candidates=2000, n_rounds=3)
    if score_swapped > best_score:
        best_score = score_swapped
        best_xs = xs_swapped.copy()
        print(f"  >>> SWAP IMPROVED: {best_score:.16f}")

    # Save result
    print(f"\n=== FINAL RESULT ===")
    print(f"Baseline: {baseline_score:.16f}")
    print(f"Best:     {best_score:.16f}")
    print(f"Δ:        {best_score - baseline_score:.2e}")

    if best_score > baseline_score:
        w_best = xs_to_weights(best_xs)
        verify_score = compute_score(w_best)
        print(f"Verified: {verify_score:.16f}")

        sol = {"weights": w_best.tolist()}
        out_path = RESULTS_DIR / "solution-cascade.json"
        with open(out_path, "w") as f:
            json.dump(sol, f)
        print(f"Saved to {out_path}")
    else:
        print("No improvement found.")


if __name__ == "__main__":
    main()
