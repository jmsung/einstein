"""Multi-approach solver for Erdős Minimum Overlap (P1).

Strategies:
1. Resolution sweep — try many n values, warm-start from SOTA
2. Aggressive simulated annealing from SOTA
3. Large-scale SLP with all-active-lag Jacobian
4. Population-based search with crossover
5. Haugland-inspired piecewise constructions
6. Analytical constructions (exponential decay, spline-based)

Target: beat 0.3808703105862199 by >= 1e-6
"""

import sys
import json
import time
import numpy as np
from pathlib import Path
from scipy.signal import fftconvolve
from scipy.optimize import linprog, minimize

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from einstein.erdos.evaluator import compute_upper_bound
from einstein.erdos.fast import fast_evaluate

SOTA_SCORE = 0.3808703105862199
TARGET = SOTA_SCORE - 1e-6
RESULTS_DIR = Path("/tmp/p1_results")
RESULTS_DIR.mkdir(exist_ok=True)

# ─── Helpers ────────────────────────────────────────────────────────────

def score(h):
    """Fast score via FFT."""
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s > 0 and s != target:
        h = h * (target / s)
    h = np.clip(h, 0.0, 1.0)
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def triple_verify(h, label=""):
    """Triple verify: fast, exact, and recomputed."""
    h = np.asarray(h, dtype=np.float64)
    s1 = fast_evaluate(h)
    s2 = compute_upper_bound(h.tolist())
    s3 = score(h)
    match = abs(s1 - s2) < 1e-12 and abs(s1 - s3) < 1e-12
    if label:
        print(f"  [{label}] fast={s1:.16f} exact={s2:.16f} score={s3:.16f} match={match}")
    return s2, match


def save_solution(h, method, s=None):
    """Save solution to results dir."""
    if s is None:
        s = score(h)
    result = {
        "values": h.tolist(),
        "score": float(s),
        "method": method,
        "n": len(h),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"p1_{method}_n{len(h)}_{s:.12f}.json"
    with open(fname, "w") as f:
        json.dump(result, f)
    return fname


def project(h):
    """Project onto feasible set: h in [0,1], sum = n/2."""
    n = len(h)
    h = np.clip(h, 0.0, 1.0)
    target = n / 2.0
    s = np.sum(h)
    if s > 0 and abs(s - target) > 1e-12:
        h = h * (target / s)
        h = np.clip(h, 0.0, 1.0)
    return h


def resample(h, new_n):
    """Resample step function to different resolution."""
    n = len(h)
    x_old = np.linspace(0, 1, n, endpoint=False)
    x_new = np.linspace(0, 1, new_n, endpoint=False)
    h_new = np.interp(x_new, x_old, h)
    return project(h_new)


def correlation_vector(h):
    """Full correlation vector."""
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    s = np.sum(h)
    target = n / 2.0
    if s > 0 and s != target:
        h = h * (target / s)
    return fftconvolve(h, (1.0 - h)[::-1], mode="full")


# ─── Approach 1: Resolution Sweep ──────────────────────────────────────

def resolution_sweep(sota_h, n_values=None, polish_iters=500000):
    """Try different resolutions with warm-start from SOTA."""
    if n_values is None:
        n_values = [50, 51, 95, 100, 150, 200, 250, 300, 400, 480, 500,
                    550, 600, 650, 700, 720, 750, 800, 900, 1000, 1200,
                    1500, 2000, 2400, 3000]

    print("\n=== Approach 1: Resolution Sweep ===")
    best_score = float("inf")
    best_h = None
    best_n = None

    for n in n_values:
        h = resample(sota_h, n)
        s0 = score(h)

        # Quick polish with random local search
        h_polished, s = quick_polish(h, n_iters=min(polish_iters, 200000), seed=42)

        gap = s - SOTA_SCORE
        marker = " ***" if s < SOTA_SCORE else ""
        print(f"  n={n:5d}: resample={s0:.12f} polished={s:.12f} (gap={gap:+.2e}){marker}")

        if s < best_score:
            best_score = s
            best_h = h_polished.copy()
            best_n = n
            save_solution(h_polished, f"resweep_n{n}", s)

    print(f"\n  Best resolution: n={best_n}, score={best_score:.16f}")
    return best_h, best_score


def quick_polish(h, n_iters=200000, seed=42):
    """Quick random local search polish."""
    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    best = score(h)

    for trial in range(n_iters):
        # Multi-point perturbation
        n_pts = rng.choice([2, 3, 4, 5])
        idx = rng.choice(n, size=n_pts, replace=False)
        delta = rng.standard_normal(n_pts) * 1e-6
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

    return h, best


# ─── Approach 2: Simulated Annealing ──────────────────────────────────

def simulated_annealing(h_init, time_limit=600, seed=42):
    """Aggressive simulated annealing with multi-scale moves."""
    print("\n=== Approach 2: Simulated Annealing ===")
    rng = np.random.default_rng(seed)
    h = h_init.copy()
    n = len(h)
    current_score = score(h)
    best_h = h.copy()
    best_score = current_score

    # Temperature schedule
    T_start = 1e-4
    T_end = 1e-10

    t0 = time.time()
    n_iters = 0
    n_accepted = 0
    n_improved = 0

    print(f"  Start: score={current_score:.16f}, n={n}")

    while time.time() - t0 < time_limit:
        # Exponential cooling
        elapsed_frac = (time.time() - t0) / time_limit
        T = T_start * (T_end / T_start) ** elapsed_frac

        # Multi-scale moves
        scale = rng.choice([1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2])
        n_pts = rng.choice([2, 3, 4, 5, 6, 8, 10, 20])
        idx = rng.choice(n, size=n_pts, replace=False)
        delta = rng.standard_normal(n_pts) * scale
        delta -= delta.mean()  # sum-preserving

        old = h[idx].copy()
        new = old + delta
        if np.any(new < 0) or np.any(new > 1):
            n_iters += 1
            continue

        h[idx] = new
        new_score = score(h)

        delta_score = new_score - current_score
        if delta_score < 0:
            # Improvement — always accept
            current_score = new_score
            n_accepted += 1
            if new_score < best_score:
                best_score = new_score
                best_h = h.copy()
                n_improved += 1
        elif T > 0 and rng.random() < np.exp(-delta_score / T):
            # Accept worse solution with probability
            current_score = new_score
            n_accepted += 1
        else:
            h[idx] = old

        n_iters += 1
        if n_iters % 500000 == 0:
            elapsed = time.time() - t0
            print(f"    iter {n_iters}: best={best_score:.16f} curr={current_score:.16f} "
                  f"T={T:.2e} acc={n_accepted}/{n_iters} imp={n_improved} [{elapsed:.0f}s]")

    print(f"  SA done: best={best_score:.16f}, iters={n_iters}, improved={n_improved}")
    return best_h, best_score


# ─── Approach 3: SLP with Full Jacobian ────────────────────────────────

def slp_full(h_init, max_rounds=50, time_limit=600):
    """SLP with all near-maximal lags and analytical Jacobian."""
    print("\n=== Approach 3: SLP with Full Jacobian ===")
    h = h_init.copy()
    n = len(h)
    best_h = h.copy()
    best_score = score(h)
    t0 = time.time()

    print(f"  Start: score={best_score:.16f}, n={n}")

    for round_idx in range(max_rounds):
        if time.time() - t0 > time_limit:
            break

        # Normalize
        h = project(h)

        # Correlation and active lags
        corr = correlation_vector(h)
        max_corr = np.max(corr)

        # Select active lags: within 0.01 of max in correlation space
        threshold = max_corr - max_corr * 0.001
        active_idx = np.where(corr >= threshold)[0]
        if len(active_idx) > 500:
            active_idx = np.argsort(corr)[-500:]
        n_active = len(active_idx)

        # Numerical Jacobian
        eps = 1e-8
        G = np.zeros((n_active, n))
        for i in range(n):
            hp = h.copy()
            hp[i] += eps
            corr_p = fftconvolve(hp, (1.0 - hp)[::-1], mode="full")
            G[:, i] = (corr_p[active_idx] - corr[active_idx]) / eps

        # Try multiple trust region sizes
        for delta in [0.1, 0.05, 0.02, 0.01, 0.005, 0.001, 0.0005, 0.0001]:
            # LP: minimize t s.t. corr0 + G @ d <= t, constraints
            c_obj = np.zeros(n + 1)
            c_obj[-1] = 1.0

            A_ub = np.zeros((n_active, n + 1))
            A_ub[:, :n] = G
            A_ub[:, -1] = -1.0
            b_ub = -corr[active_idx]

            bounds = [(max(-delta, -h[i]), min(delta, 1.0 - h[i])) for i in range(n)]
            bounds.append((None, None))

            A_eq = np.zeros((1, n + 1))
            A_eq[0, :n] = 1.0
            b_eq = np.array([0.0])

            try:
                result = linprog(c_obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                               bounds=bounds, method='highs', options={'time_limit': 30})

                if result.success:
                    d = result.x[:n]
                    h_new = project(h + d)
                    new_score = score(h_new)

                    if new_score < best_score - 1e-16:
                        imp = best_score - new_score
                        best_score = new_score
                        best_h = h_new.copy()
                        h = h_new
                        print(f"    round {round_idx}, delta={delta}: score={best_score:.16f} (imp={imp:.2e})")
                        break
            except Exception:
                continue

        if time.time() - t0 > time_limit:
            break

    print(f"  SLP done: best={best_score:.16f}")
    return best_h, best_score


# ─── Approach 4: Population-Based Search ───────────────────────────────

def population_search(h_init, pop_size=50, time_limit=600, seed=42):
    """Population-based search with crossover and mutation."""
    print("\n=== Approach 4: Population-Based Search ===")
    rng = np.random.default_rng(seed)
    n = len(h_init)
    t0 = time.time()

    # Initialize population from SOTA + perturbations
    pop = np.zeros((pop_size, n))
    pop[0] = h_init.copy()
    for i in range(1, pop_size):
        noise = rng.standard_normal(n) * rng.choice([1e-3, 1e-4, 1e-5, 1e-6])
        pop[i] = project(h_init + noise)

    scores = np.array([score(pop[i]) for i in range(pop_size)])
    best_idx = np.argmin(scores)
    best_h = pop[best_idx].copy()
    best_score = scores[best_idx]

    print(f"  Initial pop: best={best_score:.16f}")

    gen = 0
    while time.time() - t0 < time_limit:
        gen += 1

        # Tournament selection
        idx1, idx2 = rng.choice(pop_size, size=2, replace=False)
        parent1 = pop[idx1] if scores[idx1] < scores[idx2] else pop[idx2]

        idx3, idx4 = rng.choice(pop_size, size=2, replace=False)
        parent2 = pop[idx3] if scores[idx3] < scores[idx4] else pop[idx4]

        # Crossover: blend
        alpha = rng.uniform(0.2, 0.8)
        child = alpha * parent1 + (1 - alpha) * parent2

        # Mutation: multi-scale
        scale = rng.choice([1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2])
        n_mutate = rng.integers(2, min(50, n))
        mut_idx = rng.choice(n, size=n_mutate, replace=False)
        mutation = rng.standard_normal(n_mutate) * scale
        mutation -= mutation.mean()
        child[mut_idx] += mutation

        child = project(child)
        child_score = score(child)

        # Replace worst
        worst_idx = np.argmax(scores)
        if child_score < scores[worst_idx]:
            pop[worst_idx] = child
            scores[worst_idx] = child_score

            if child_score < best_score:
                best_score = child_score
                best_h = child.copy()

        if gen % 50000 == 0:
            elapsed = time.time() - t0
            print(f"    gen {gen}: best={best_score:.16f} mean={np.mean(scores):.12f} [{elapsed:.0f}s]")

    print(f"  Pop search done: best={best_score:.16f}")
    return best_h, best_score


# ─── Approach 5: Haugland-style Constructions ──────────────────────────

def haugland_constructions(n=600):
    """Systematic piecewise linear constructions inspired by Haugland (2016).

    Haugland's key insight: use piecewise constant functions with breakpoints
    at rational positions. The optimal function has a specific structure with
    ~51 pieces.
    """
    print("\n=== Approach 5: Haugland-style Constructions ===")
    best_score = float("inf")
    best_h = None

    x = np.linspace(0, 2, n, endpoint=False)

    # Strategy: parameterize h as piecewise constant with K pieces
    for K in [20, 30, 40, 51, 60, 75, 95, 120, 150, 200]:
        for seed in range(20):
            rng = np.random.default_rng(seed * 1000 + K)

            # Random breakpoints
            breaks = np.sort(rng.uniform(0, 2, K - 1))
            breaks = np.concatenate([[0], breaks, [2]])

            # Random heights
            heights = rng.uniform(0, 1, K)

            # Build h
            h = np.zeros(n)
            for i in range(K):
                mask = (x >= breaks[i]) & (x < breaks[i + 1])
                h[mask] = heights[i]

            h = project(h)

            # Optimize heights with Nelder-Mead
            def obj(params):
                hh = np.zeros(n)
                for i in range(K):
                    mask = (x >= breaks[i]) & (x < breaks[i + 1])
                    hh[mask] = params[i]
                hh = project(hh)
                return score(hh)

            result = minimize(obj, heights, method='Nelder-Mead',
                            options={'maxiter': 3000, 'xatol': 1e-12, 'fatol': 1e-14})

            s = result.fun
            if s < best_score:
                best_score = s
                # Reconstruct h from optimized params
                for i in range(K):
                    mask = (x >= breaks[i]) & (x < breaks[i + 1])
                    h[mask] = result.x[i]
                best_h = project(h)

        print(f"  K={K:3d}: best={best_score:.12f} (gap={best_score - SOTA_SCORE:+.2e})")

    print(f"\n  Best piecewise: {best_score:.16f}")
    return best_h, best_score


# ─── Approach 6: Coordinate descent on near-max lags ───────────────────

def targeted_coordinate_descent(h_init, time_limit=600, seed=42):
    """Target perturbations that reduce the max lag specifically."""
    print("\n=== Approach 6: Targeted Coordinate Descent ===")
    rng = np.random.default_rng(seed)
    h = h_init.copy()
    n = len(h)
    best_h = h.copy()
    best_score = score(h)
    t0 = time.time()
    improved = 0

    print(f"  Start: score={best_score:.16f}")

    iters = 0
    while time.time() - t0 < time_limit:
        # Compute correlation to find the argmax lag
        corr = correlation_vector(h)
        argmax_lag = np.argmax(corr)
        max_corr = corr[argmax_lag]

        # The derivative of corr[j] w.r.t. h[i] tells us which indices to move
        # d corr[j] / d h[i] = (1 - h[n-1-j+i]) - h[i-n+1+j]
        # For the argmax lag, compute gradient
        grad = np.zeros(n)
        for i in range(n):
            idx1 = n - 1 - argmax_lag + i
            idx2 = i - n + 1 + argmax_lag
            if 0 <= idx1 < n:
                grad[i] += 1.0 - h[idx1]
            if 0 <= idx2 < n:
                grad[i] -= h[idx2]

        # Move in negative gradient direction (reduce max corr)
        grad -= np.mean(grad)  # sum-preserving

        # Try multiple step sizes
        for lr in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]:
            h_new = h - lr * grad
            h_new = np.clip(h_new, 0.0, 1.0)
            h_new = project(h_new)
            new_score = score(h_new)

            if new_score < best_score:
                best_score = new_score
                best_h = h_new.copy()
                h = h_new
                improved += 1
                break

        # Also try random perturbation
        for _ in range(1000):
            n_pts = rng.choice([2, 3, 4, 5])
            idx = rng.choice(n, size=n_pts, replace=False)
            delta = rng.standard_normal(n_pts) * rng.choice([1e-6, 1e-7, 1e-8])
            delta -= delta.mean()

            old = h[idx].copy()
            new = old + delta
            if np.any(new < 0) or np.any(new > 1):
                continue

            h[idx] = new
            s = score(h)
            if s < best_score:
                best_score = s
                best_h = h.copy()
                improved += 1
            else:
                h[idx] = old

        iters += 1
        if iters % 10 == 0:
            elapsed = time.time() - t0
            print(f"    round {iters}: best={best_score:.16f} improved={improved} [{elapsed:.0f}s]")

    print(f"  TCD done: best={best_score:.16f}, improved={improved}")
    return best_h, best_score


# ─── Approach 7: Symmetrized construction ──────────────────────────────

def symmetrized_search(h_init, time_limit=300, seed=42):
    """Enforce approximate symmetry h(x) ≈ h(2-x) and optimize."""
    print("\n=== Approach 7: Symmetrized Search ===")
    rng = np.random.default_rng(seed)
    h = h_init.copy()
    n = len(h)

    # Symmetrize
    h_sym = (h + h[::-1]) / 2.0
    h_sym = project(h_sym)
    s_sym = score(h_sym)
    print(f"  Symmetrized from SOTA: {s_sym:.16f}")

    # Polish the symmetrized version
    best_h = h_sym.copy()
    best_score = s_sym
    t0 = time.time()

    half = n // 2
    iters = 0
    while time.time() - t0 < time_limit:
        # Perturb first half, mirror to second half
        n_pts = rng.choice([2, 3, 4, 5])
        idx = rng.choice(half, size=n_pts, replace=False)
        delta = rng.standard_normal(n_pts) * rng.choice([1e-6, 1e-7, 1e-5])
        delta -= delta.mean()

        mirror_idx = n - 1 - idx

        old_vals = h_sym[idx].copy()
        old_mirror = h_sym[mirror_idx].copy()

        h_sym[idx] = np.clip(old_vals + delta, 0, 1)
        h_sym[mirror_idx] = h_sym[idx]  # enforce symmetry

        # Fix sum
        excess = np.sum(h_sym) - n / 2.0
        if abs(excess) > 1e-12:
            h_sym[0] -= excess / 2
            h_sym[-1] -= excess / 2
            h_sym = np.clip(h_sym, 0, 1)

        s = score(h_sym)
        if s < best_score:
            best_score = s
            best_h = h_sym.copy()
        else:
            h_sym[idx] = old_vals
            h_sym[mirror_idx] = old_mirror

        iters += 1
        if iters % 500000 == 0:
            elapsed = time.time() - t0
            print(f"    iter {iters}: best={best_score:.16f} [{elapsed:.0f}s]")

    print(f"  Symmetrized done: best={best_score:.16f}")
    return best_h, best_score


# ─── Approach 8: Different n values with deep polish ───────────────────

def deep_resolution_search(sota_h, n_values=None, polish_time=120):
    """Try key n values with much deeper polishing."""
    if n_values is None:
        # Focus on n values near 600 and some special ones
        n_values = [300, 400, 500, 550, 575, 600, 625, 650, 700, 800, 900, 1000, 1200]

    print("\n=== Approach 8: Deep Resolution Search ===")
    best_score = float("inf")
    best_h = None

    for n in n_values:
        t0 = time.time()
        h = resample(sota_h, n)
        s0 = score(h)

        # Deep SA at this resolution
        h_sa, s_sa = mini_sa(h, time_limit=polish_time, seed=n)

        gap = s_sa - SOTA_SCORE
        marker = " ***" if s_sa < SOTA_SCORE else ""
        print(f"  n={n:5d}: start={s0:.12f} SA={s_sa:.12f} (gap={gap:+.2e}){marker} [{time.time()-t0:.0f}s]")

        if s_sa < best_score:
            best_score = s_sa
            best_h = h_sa.copy()
            save_solution(h_sa, f"deepres_n{n}", s_sa)

    return best_h, best_score


def mini_sa(h, time_limit=60, seed=42):
    """Mini simulated annealing."""
    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    current_score = score(h)
    best_h = h.copy()
    best_score = current_score
    T = 1e-5
    t0 = time.time()

    while time.time() - t0 < time_limit:
        T *= 0.999999
        n_pts = rng.choice([2, 3, 4, 5])
        idx = rng.choice(n, size=n_pts, replace=False)
        scale = rng.choice([1e-8, 1e-7, 1e-6, 1e-5, 1e-4])
        delta = rng.standard_normal(n_pts) * scale
        delta -= delta.mean()

        old = h[idx].copy()
        new = old + delta
        if np.any(new < 0) or np.any(new > 1):
            continue

        h[idx] = new
        new_score = score(h)

        d = new_score - current_score
        if d < 0 or (T > 0 and rng.random() < np.exp(-d / T)):
            current_score = new_score
            if new_score < best_score:
                best_score = new_score
                best_h = h.copy()
        else:
            h[idx] = old

    return best_h, best_score


# ─── Main ──────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("Erdős Minimum Overlap — Multi-Approach Solver")
    print("=" * 70)
    print(f"SOTA:   {SOTA_SCORE:.16f}")
    print(f"Target: {TARGET:.16f} (improvement >= 1e-6)")
    print()

    t_total = time.time()

    # Load SOTA
    with open("/tmp/sota_p1.json") as f:
        sota = json.load(f)
    h_sota = np.array(sota["values"], dtype=np.float64)
    s_verify, match = triple_verify(h_sota, "SOTA verify")

    all_results = []

    # Approach 1: Resolution sweep (quick, ~5 min)
    h1, s1 = resolution_sweep(h_sota, polish_iters=100000)
    all_results.append(("Resolution sweep", s1, h1))
    save_solution(h1, "resweep", s1)

    # Approach 2: Simulated annealing from SOTA (10 min)
    h2, s2 = simulated_annealing(h_sota.copy(), time_limit=600, seed=42)
    all_results.append(("Simulated annealing", s2, h2))
    save_solution(h2, "sa", s2)

    # Approach 6: Targeted coordinate descent (10 min)
    h6, s6 = targeted_coordinate_descent(h_sota.copy(), time_limit=600, seed=42)
    all_results.append(("Targeted CD", s6, h6))
    save_solution(h6, "tcd", s6)

    # Approach 7: Symmetrized search (5 min)
    h7, s7 = symmetrized_search(h_sota.copy(), time_limit=300, seed=42)
    all_results.append(("Symmetrized", s7, h7))
    save_solution(h7, "sym", s7)

    # Approach 8: Deep resolution search (15 min)
    h8, s8 = deep_resolution_search(h_sota, polish_time=60)
    all_results.append(("Deep resolution", s8, h8))
    save_solution(h8, "deepres", s8)

    # Summary
    all_results.sort(key=lambda r: r[1])
    elapsed = time.time() - t_total

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for name, s, h in all_results:
        gap = s - SOTA_SCORE
        marker = " *** BEATS SOTA! ***" if s < TARGET else ""
        print(f"  {name:25s}: {s:.16f} (gap={gap:+.2e}){marker}")

    print(f"\nTotal time: {elapsed:.0f}s")

    # Verify best
    best_name, best_s, best_h = all_results[0]
    s_verified, match = triple_verify(best_h, f"Best ({best_name})")

    if s_verified < TARGET:
        print(f"\n*** SUBMISSION CANDIDATE: {s_verified:.16f} ***")
        save_solution(best_h, "CANDIDATE", s_verified)
    else:
        print(f"\nNo solution beats SOTA by >= 1e-6")

    return best_h, s_verified


if __name__ == "__main__":
    main()
