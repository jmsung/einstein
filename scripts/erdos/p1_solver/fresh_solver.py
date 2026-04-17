"""Fresh solver for Erdős Minimum Overlap — Session 9 (2026-04-17).

Novel approaches not previously tried:
1. Coordinate descent with exact 1D minimax line search
2. Augmented Lagrangian with smooth minimax (p-norm, varying p)
3. Multi-resolution warm-start: solve at n=300, upsample, polish at n=600
4. KKT residual minimization
5. Random subspace optimization (Johnson-Lindenstrauss style)
"""

import json
import time
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

SOTA_SCORE = 0.3808703105862199
MIN_IMPROVEMENT = 1e-6
TARGET_SCORE = SOTA_SCORE - MIN_IMPROVEMENT  # Must beat this


# ─── Core evaluation ─────────────────────────────────────────────
def score(h: np.ndarray) -> float:
    """Compute Erdős overlap score (arena formula). Lower is better."""
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s != target and s > 0:
        h = h * (target / s)
    if np.any(h < 0) or np.any(h > 1):
        return float("inf")
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def score_exact(h: np.ndarray) -> float:
    """Exact score using np.correlate (arena verifier)."""
    n = len(h)
    h = np.array(h, dtype=np.float64)
    s = np.sum(h)
    target = n / 2.0
    if s != target and s > 0:
        h = h * (target / s)
    if np.any(h < 0) or np.any(h > 1):
        return float("inf")
    corr = np.correlate(h, 1.0 - h, mode="full")
    return float(np.max(corr)) / n * 2


def correlation_vector(h: np.ndarray) -> np.ndarray:
    """Full correlation vector C(k) for all shifts."""
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s != target and s > 0:
        h = h * (target / s)
    return fftconvolve(h, (1.0 - h)[::-1], mode="full")


def project(h: np.ndarray) -> np.ndarray:
    """Project onto feasible set: h ∈ [0,1]^n, sum = n/2."""
    h = np.clip(h, 0.0, 1.0)
    n = len(h)
    target = n / 2.0
    s = np.sum(h)
    if s > 0 and abs(s - target) > 1e-15:
        h = h * (target / s)
        h = np.clip(h, 0.0, 1.0)
        # Second pass for exact normalization
        s = np.sum(h)
        if s > 0 and abs(s - target) > 1e-15:
            h = h * (target / s)
    return h


def load_sota(path: str = None) -> np.ndarray:
    """Load SOTA solution."""
    if path is None:
        path = str(RESULTS_DIR / "sota_together_ai_n600.json")
    with open(path) as f:
        data = json.load(f)
    return np.array(data["values"], dtype=np.float64)


# ─── Approach 1: Coordinate Descent with Exact Line Search ──────
def coord_descent_minimax(h: np.ndarray, max_iters: int = 50,
                          verbose: bool = True) -> tuple[np.ndarray, float]:
    """Coordinate descent with exact 1D minimax line search.

    For each coordinate h_j, the overlap at each shift d is affine in h_j.
    So the minimax over h_j is a 1D problem solvable exactly.
    """
    h = h.copy()
    n = len(h)
    best_score = score(h)
    if verbose:
        print(f"  CD-Minimax: n={n}, start={best_score:.13f}")

    for iteration in range(max_iters):
        improved_count = 0
        for j in range(n):
            # Current full correlation vector
            corr = correlation_vector(h)
            current_max = np.max(corr)

            # For each shift d, compute how O(d) depends on h_j
            # O(d) = (2/n) * sum_i h_i * (1 - h_{i+d})
            # Partial derivative of sum_i h_i*(1-h_{i+d}) w.r.t. h_j:
            #   = (1 - h_{j+d}) [if j+d valid, from i=j term]
            #     - h_{j-d}     [if j-d valid, from i=j-d term where h_j appears as (1-h_j)]
            # So corr(d) as function of h_j:
            # corr(d)(h_j) = corr(d)|_{h_j=old} + (h_j - old_j) * dC_dhj(d)

            old_j = h[j]

            # Compute the affine coefficients for each shift
            # corr has length 2n-1, shift d maps to index d+n-1
            n_shifts = 2 * n - 1
            # dC/dh_j for each shift
            grad_j = np.zeros(n_shifts)
            for d_idx in range(n_shifts):
                d = d_idx - (n - 1)  # actual shift
                # i=j term: h_j * (1-h_{j+d}) if j+d in [0,n)
                if 0 <= j + d < n:
                    grad_j[d_idx] += (1.0 - h[j + d])
                # i=j-d term: h_{j-d} * (1-h_j) -> derivative w.r.t. h_j = -h_{j-d}
                if 0 <= j - d < n:
                    grad_j[d_idx] -= h[j - d]

            # Now corr(d_idx)(h_j) = corr[d_idx] + (h_j - old_j) * grad_j[d_idx]
            # We want to minimize max_{d_idx} corr(d_idx)(h_j)
            # = minimize max_{d_idx} [corr[d_idx] + (h_j - old_j) * grad_j[d_idx]]

            # This is a 1D minimax: min_{h_j in [0,1]} max_i (a_i + b_i * h_j)
            # where a_i = corr[d_idx] - old_j * grad_j[d_idx], b_i = grad_j[d_idx]

            a = corr - old_j * grad_j
            b = grad_j

            # Find optimal h_j by sweeping candidate breakpoints
            # The max of affine functions is piecewise linear, convex
            # Optimal is at an intersection or boundary

            # Quick approach: evaluate on a grid + refine
            candidates = [0.0, 1.0, old_j]

            # Add intersections of active constraints
            active = np.where(corr >= current_max - 1e-10)[0]
            for i1 in range(len(active)):
                for i2 in range(i1 + 1, min(len(active), i1 + 20)):
                    d1, d2 = active[i1], active[i2]
                    if abs(b[d1] - b[d2]) > 1e-15:
                        h_star = (a[d2] - a[d1]) / (b[d1] - b[d2])
                        if 0 <= h_star <= 1:
                            candidates.append(h_star)

            best_hj = old_j
            best_max_corr = current_max
            for hj_cand in candidates:
                new_corr_max = np.max(a + b * hj_cand)
                if new_corr_max < best_max_corr - 1e-15:
                    best_max_corr = new_corr_max
                    best_hj = hj_cand

            if best_hj != old_j:
                h[j] = best_hj
                # Re-project to maintain sum constraint
                h = project(h)
                new_s = score(h)
                if new_s < best_score:
                    best_score = new_s
                    improved_count += 1
                else:
                    h[j] = old_j
                    h = project(h)

        if verbose:
            print(f"    Iter {iteration+1}: score={best_score:.13f}, improved={improved_count}")
        if improved_count == 0:
            break

    return h, best_score


# ─── Approach 2: P-norm smoothing with increasing p ──────────────
def pnorm_optimize(h: np.ndarray, max_iters: int = 5000,
                   lr: float = 1e-5, p_schedule=None,
                   verbose: bool = True) -> tuple[np.ndarray, float]:
    """Optimize using p-norm approximation to max, with increasing p.

    max(x) ≈ (Σ x_i^p)^(1/p) for large p.
    Start with small p (smooth), increase to large p (sharp).
    """
    try:
        import torch
    except ImportError:
        print("  PyTorch not available, skipping p-norm optimization")
        return h, score(h)

    if p_schedule is None:
        p_schedule = [(2000, 10), (2000, 50), (1000, 200)]

    n = len(h)
    h_torch = torch.tensor(h, dtype=torch.float64, requires_grad=True)

    best_h = h.copy()
    best_score = score(h)
    if verbose:
        print(f"  P-norm opt: n={n}, start={best_score:.13f}")

    for stage, (n_iters, p) in enumerate(p_schedule):
        h_torch = torch.tensor(best_h, dtype=torch.float64, requires_grad=True)
        optimizer = torch.optim.Adam([h_torch], lr=lr)

        for i in range(n_iters):
            optimizer.zero_grad()

            # Normalize sum
            h_val = torch.clamp(h_torch, 0.0, 1.0)
            target = n / 2.0
            h_val = h_val * (target / torch.sum(h_val))

            # Compute correlation via conv1d
            one_minus_h = 1.0 - h_val
            # Use manual correlation
            h_pad = torch.nn.functional.pad(h_val.unsqueeze(0).unsqueeze(0),
                                            (n - 1, n - 1))
            kernel = one_minus_h.flip(0).unsqueeze(0).unsqueeze(0)
            corr = torch.nn.functional.conv1d(h_pad, kernel).squeeze()

            # P-norm approximation to max
            corr_shifted = corr - corr.max().detach() + 1  # numerical stability
            p_norm = (torch.sum(torch.abs(corr) ** p)) ** (1.0 / p)
            loss = p_norm / n * 2

            loss.backward()
            optimizer.step()

            if (i + 1) % 1000 == 0:
                with torch.no_grad():
                    h_np = torch.clamp(h_torch, 0.0, 1.0).numpy().copy()
                    h_np = project(h_np)
                    s = score(h_np)
                    if s < best_score:
                        best_score = s
                        best_h = h_np.copy()
                    if verbose:
                        print(f"    Stage {stage} iter {i+1}: p={p}, loss={loss.item():.10f}, "
                              f"score={s:.13f}, best={best_score:.13f}")

        # Extract and evaluate
        with torch.no_grad():
            h_np = torch.clamp(h_torch, 0.0, 1.0).numpy().copy()
            h_np = project(h_np)
            s = score(h_np)
            if s < best_score:
                best_score = s
                best_h = h_np.copy()

    return best_h, best_score


# ─── Approach 3: Multi-resolution warm-start ─────────────────────
def multi_resolution_search(n_low: int = 300, n_high: int = 600,
                            n_starts: int = 20, iters_per_start: int = 10000,
                            verbose: bool = True) -> tuple[np.ndarray, float]:
    """Solve at lower resolution, then upsample and polish.

    At n=300, the problem has half the variables, making global search easier.
    """
    try:
        import torch
    except ImportError:
        print("  PyTorch not available, skipping multi-resolution")
        return np.zeros(n_high), float("inf")

    best_h = None
    best_score = float("inf")

    if verbose:
        print(f"  Multi-res: {n_starts} starts at n={n_low}, upsample to n={n_high}")

    for start_idx in range(n_starts):
        rng = np.random.default_rng(start_idx * 137 + 42)

        # Random initialization at low resolution
        h_init = rng.random(n_low)
        h_init = h_init / np.sum(h_init) * (n_low / 2)
        h_init = np.clip(h_init, 0.0, 1.0)

        # Optimize at low resolution with PyTorch Adam
        h_torch = torch.tensor(h_init, dtype=torch.float64, requires_grad=True)
        optimizer = torch.optim.Adam([h_torch], lr=1e-4)

        for i in range(iters_per_start):
            optimizer.zero_grad()
            h_val = torch.clamp(h_torch, 0.0, 1.0)
            target = n_low / 2.0
            h_val = h_val * (target / torch.sum(h_val))
            one_minus_h = 1.0 - h_val
            h_pad = torch.nn.functional.pad(h_val.unsqueeze(0).unsqueeze(0),
                                            (n_low - 1, n_low - 1))
            kernel = one_minus_h.flip(0).unsqueeze(0).unsqueeze(0)
            corr = torch.nn.functional.conv1d(h_pad, kernel).squeeze()
            # LogSumExp smooth max
            beta = 100.0
            loss = torch.logsumexp(corr * beta, dim=0) / beta / n_low * 2
            loss.backward()
            optimizer.step()

        with torch.no_grad():
            h_low = torch.clamp(h_torch, 0.0, 1.0).numpy().copy()
            h_low = project(h_low)
            s_low = score(h_low)

        # Upsample to high resolution
        x_low = np.linspace(0, 1, n_low)
        x_high = np.linspace(0, 1, n_high)
        h_high = np.interp(x_high, x_low, h_low)
        h_high = project(h_high)
        s_high = score(h_high)

        if s_high < best_score:
            best_score = s_high
            best_h = h_high.copy()
            if verbose:
                print(f"    Start {start_idx}: low={s_low:.10f}, high={s_high:.10f} ** NEW BEST")
        elif verbose and start_idx < 5:
            print(f"    Start {start_idx}: low={s_low:.10f}, high={s_high:.10f}")

    if verbose:
        print(f"  Multi-res best: {best_score:.13f}")

    return best_h, best_score


# ─── Approach 4: Aggressive perturbation + reconvergence ─────────
def perturb_and_reconverge(h_sota: np.ndarray, n_perturbations: int = 50,
                           perturbation_scale: float = 0.05,
                           reconverge_iters: int = 20000,
                           verbose: bool = True) -> tuple[np.ndarray, float]:
    """Large random perturbation of SOTA + reconvergence.

    Previous work used small perturbations (1e-7). Here we try larger ones
    (0.01-0.1) to potentially escape the current basin.
    """
    try:
        import torch
    except ImportError:
        print("  PyTorch not available, skipping perturbation search")
        return h_sota, score(h_sota)

    n = len(h_sota)
    best_h = h_sota.copy()
    best_score = score(h_sota)
    if verbose:
        print(f"  Perturb+reconverge: {n_perturbations} trials, scale={perturbation_scale}")

    for trial in range(n_perturbations):
        rng = np.random.default_rng(trial * 31 + 7)

        # Large perturbation
        delta = rng.standard_normal(n) * perturbation_scale
        delta -= delta.mean()  # zero-sum to preserve sum constraint
        h_pert = h_sota + delta
        h_pert = project(h_pert)

        # Reconverge with Adam
        h_torch = torch.tensor(h_pert, dtype=torch.float64, requires_grad=True)
        optimizer = torch.optim.Adam([h_torch], lr=1e-4)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, reconverge_iters)

        for i in range(reconverge_iters):
            optimizer.zero_grad()
            h_val = torch.clamp(h_torch, 0.0, 1.0)
            target = n / 2.0
            h_val = h_val * (target / torch.sum(h_val))
            one_minus_h = 1.0 - h_val
            h_pad = torch.nn.functional.pad(h_val.unsqueeze(0).unsqueeze(0),
                                            (n - 1, n - 1))
            kernel = one_minus_h.flip(0).unsqueeze(0).unsqueeze(0)
            corr = torch.nn.functional.conv1d(h_pad, kernel).squeeze()
            beta = 100.0 + i * 0.01  # slowly increase sharpness
            loss = torch.logsumexp(corr * beta, dim=0) / beta / n * 2
            loss.backward()
            optimizer.step()
            scheduler.step()

        with torch.no_grad():
            h_np = torch.clamp(h_torch, 0.0, 1.0).numpy().copy()
            h_np = project(h_np)
            s = score(h_np)

        if s < best_score:
            best_score = s
            best_h = h_np.copy()
            if verbose:
                print(f"    Trial {trial}: score={s:.13f} ** NEW BEST (gap to SOTA: {SOTA_SCORE - s:.2e})")
        elif verbose and trial < 5:
            print(f"    Trial {trial}: score={s:.13f}")

    return best_h, best_score


# ─── Approach 5: Alternating block optimization ──────────────────
def alternating_block_opt(h: np.ndarray, block_size: int = 50,
                          max_iters: int = 10,
                          verbose: bool = True) -> tuple[np.ndarray, float]:
    """Optimize blocks of variables while holding others fixed.

    Each block subproblem is a smaller optimization problem.
    """
    try:
        import torch
    except ImportError:
        print("  PyTorch not available, skipping block optimization")
        return h, score(h)

    n = len(h)
    h = h.copy()
    best_score = score(h)
    if verbose:
        print(f"  Alternating block opt: n={n}, block_size={block_size}, start={best_score:.13f}")

    for iteration in range(max_iters):
        improved = False
        blocks = list(range(0, n, block_size))
        np.random.shuffle(blocks)

        for block_start in blocks:
            block_end = min(block_start + block_size, n)
            block_idx = list(range(block_start, block_end))
            bs = len(block_idx)

            # Optimize this block with Adam
            h_block = torch.tensor(h[block_idx], dtype=torch.float64, requires_grad=True)
            h_fixed = torch.tensor(h, dtype=torch.float64)
            optimizer = torch.optim.Adam([h_block], lr=1e-5)

            for step in range(500):
                optimizer.zero_grad()
                h_full = h_fixed.clone()
                h_full[block_idx] = torch.clamp(h_block, 0.0, 1.0)
                target = n / 2.0
                h_full = h_full * (target / torch.sum(h_full))
                one_minus_h = 1.0 - h_full
                h_pad = torch.nn.functional.pad(h_full.unsqueeze(0).unsqueeze(0),
                                                (n - 1, n - 1))
                kernel = one_minus_h.flip(0).unsqueeze(0).unsqueeze(0)
                corr = torch.nn.functional.conv1d(h_pad, kernel).squeeze()
                beta = 200.0
                loss = torch.logsumexp(corr * beta, dim=0) / beta / n * 2
                loss.backward()
                optimizer.step()

            with torch.no_grad():
                h_new = h.copy()
                h_new[block_idx] = np.clip(h_block.numpy(), 0.0, 1.0)
                h_new = project(h_new)
                s = score(h_new)
                if s < best_score:
                    best_score = s
                    h = h_new.copy()
                    improved = True

        if verbose:
            print(f"    Iter {iteration+1}: score={best_score:.13f}, improved={improved}")
        if not improved:
            break

    return h, best_score


# ─── Approach 6: Differential Evolution at n=300 (global) ───────
def de_global_search(n: int = 300, pop_size: int = 100,
                     max_iters: int = 500,
                     verbose: bool = True) -> tuple[np.ndarray, float]:
    """Differential evolution at reduced resolution for global basin search."""
    from scipy.optimize import differential_evolution

    if verbose:
        print(f"  DE global search: n={n}, pop_size={pop_size}")

    def objective(x):
        h = np.array(x)
        h = project(h)
        return score(h)

    bounds = [(0, 1)] * n

    # Use Latin hypercube initialization
    result = differential_evolution(
        objective, bounds, maxiter=max_iters, popsize=pop_size,
        mutation=(0.5, 1.5), recombination=0.9, seed=42,
        tol=1e-12, atol=1e-12, polish=True,
        callback=lambda xk, convergence: print(f"    DE: f={objective(xk):.10f}, conv={convergence:.6f}") if verbose else None,
        updating='deferred', workers=1
    )

    h_best = project(result.x)
    s_best = score(h_best)
    if verbose:
        print(f"  DE best at n={n}: {s_best:.13f}")

    # Upsample to n=600
    x_low = np.linspace(0, 1, n)
    x_high = np.linspace(0, 1, 600)
    h_high = np.interp(x_high, x_low, h_best)
    h_high = project(h_high)
    s_high = score(h_high)
    if verbose:
        print(f"  DE upsampled to n=600: {s_high:.13f}")

    return h_high, s_high


# ─── Master orchestrator ─────────────────────────────────────────
def run_all(time_budget_sec: int = 7200):
    """Run all approaches and track results."""
    t0 = time.time()
    results = []

    print("=" * 70)
    print("Erdős Minimum Overlap — Fresh Solver (Session 9)")
    print(f"SOTA: {SOTA_SCORE:.16f}")
    print(f"Target (rank #1): < {TARGET_SCORE:.16f}")
    print(f"Time budget: {time_budget_sec}s")
    print("=" * 70)

    h_sota = load_sota()
    s_sota = score(h_sota)
    print(f"\nSOTA loaded: n={len(h_sota)}, score={s_sota:.16f}")

    def elapsed():
        return time.time() - t0

    def remaining():
        return time_budget_sec - elapsed()

    def log_result(name, h, s):
        results.append({"name": name, "score": s, "n": len(h)})
        gap = SOTA_SCORE - s
        status = "BEATS SOTA!" if gap > MIN_IMPROVEMENT else f"gap={gap:.2e}"
        print(f"\n>>> {name}: {s:.13f} ({status})")
        if s < SOTA_SCORE - MIN_IMPROVEMENT:
            # Save immediately
            fname = RESULTS_DIR / f"candidate_{name.replace(' ', '_')}_{s:.10f}.json"
            with open(fname, "w") as f:
                json.dump({"values": h.tolist(), "score": s}, f)
            print(f"    SAVED: {fname}")
        return s

    # ── Approach 1: Coordinate descent from SOTA ──
    if remaining() > 300:
        print(f"\n{'─'*60}")
        print("APPROACH 1: Coordinate Descent (exact line search)")
        print(f"{'─'*60}")
        try:
            h1, s1 = coord_descent_minimax(h_sota.copy(), max_iters=3)
            log_result("coord_descent", h1, s1)
        except Exception as e:
            print(f"  FAILED: {e}")

    # ── Approach 2: Multi-resolution search ──
    if remaining() > 600:
        print(f"\n{'─'*60}")
        print("APPROACH 2: Multi-resolution (n=300 → n=600)")
        print(f"{'─'*60}")
        try:
            h2, s2 = multi_resolution_search(n_low=300, n_high=600,
                                              n_starts=30, iters_per_start=15000)
            log_result("multi_res", h2, s2)

            # Polish best with mass transport
            if s2 < 0.382:
                print("  Polishing with mass transport...")
                h2_polish = mass_transport_polish(h2, n_iters=500000)
                s2_polish = score(h2_polish)
                log_result("multi_res_polished", h2_polish, s2_polish)
        except Exception as e:
            print(f"  FAILED: {e}")

    # ── Approach 3: Large perturbation + reconverge ──
    if remaining() > 600:
        print(f"\n{'─'*60}")
        print("APPROACH 3: Large perturbation + reconvergence")
        print(f"{'─'*60}")
        try:
            for scale in [0.02, 0.05, 0.1, 0.2]:
                if remaining() < 300:
                    break
                h3, s3 = perturb_and_reconverge(
                    h_sota.copy(), n_perturbations=20,
                    perturbation_scale=scale, reconverge_iters=20000)
                log_result(f"perturb_scale={scale}", h3, s3)
        except Exception as e:
            print(f"  FAILED: {e}")

    # ── Approach 4: P-norm smoothing ──
    if remaining() > 300:
        print(f"\n{'─'*60}")
        print("APPROACH 4: P-norm smoothing (cold start)")
        print(f"{'─'*60}")
        try:
            rng = np.random.default_rng(99)
            h_init = rng.random(600)
            h_init = project(h_init)
            h4, s4 = pnorm_optimize(h_init, max_iters=5000,
                                     p_schedule=[(3000, 4), (3000, 20), (2000, 100), (2000, 500)])
            log_result("pnorm_cold", h4, s4)
        except Exception as e:
            print(f"  FAILED: {e}")

    # ── Approach 5: Block optimization from SOTA ──
    if remaining() > 300:
        print(f"\n{'─'*60}")
        print("APPROACH 5: Alternating block optimization from SOTA")
        print(f"{'─'*60}")
        try:
            h5, s5 = alternating_block_opt(h_sota.copy(), block_size=30, max_iters=5)
            log_result("block_opt", h5, s5)
        except Exception as e:
            print(f"  FAILED: {e}")

    # ── Summary ──
    print(f"\n{'='*70}")
    print("SUMMARY")
    print(f"{'='*70}")
    results.sort(key=lambda x: x["score"])
    for i, r in enumerate(results):
        gap = SOTA_SCORE - r["score"]
        print(f"  {i+1}. {r['name']}: {r['score']:.13f} (gap={gap:.2e})")

    best = results[0] if results else None
    if best and best["score"] < SOTA_SCORE - MIN_IMPROVEMENT:
        print(f"\n*** RANK #1 ACHIEVABLE: {best['name']} ***")
    else:
        print(f"\n  No solution beats SOTA by {MIN_IMPROVEMENT}")

    print(f"\nTotal time: {elapsed():.0f}s")

    return results


def mass_transport_polish(h: np.ndarray, n_iters: int = 500000,
                          seed: int = 0) -> np.ndarray:
    """Quick mass transport polishing (same as warm-start optimizer)."""
    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    best = score(h)
    for trial in range(n_iters):
        n_pts = rng.choice([2, 3, 4, 5])
        idx = rng.choice(n, size=n_pts, replace=False)
        delta = rng.standard_normal(n_pts) * 1e-7
        delta -= delta.mean()
        old = h[idx].copy()
        new = old + delta
        if np.any(new < 0) or np.any(new > 1):
            continue
        h[idx] = new
        s = score(h)
        if s < best:
            best = s
        else:
            h[idx] = old
    return h


if __name__ == "__main__":
    run_all(time_budget_sec=7200)
