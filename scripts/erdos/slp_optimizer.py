"""Sequential Linear Programming (SLP) optimizer for Erdos Minimum Overlap.

Linearizes the bilinear objective around the current h, solves an LP to find
a descent direction, and takes a trust-region step with line search. Repeats.

Problem: Minimize C = max_k (sum_j h[j]*(1-h[j+k])) * 2/n
         subject to h in [0,1]^n, sum(h) = n/2.

Usage:
    cd cb-feat-auto-p1 && uv run python3 scripts/erdos/slp_optimizer.py
"""

import json
import sys
import time

import numpy as np
from scipy.optimize import linprog
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

EPS = 1e-10


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def project_to_feasible(h: np.ndarray) -> np.ndarray:
    """Project h to [EPS, 1-EPS]^n with sum = n/2."""
    h = np.clip(h, EPS, 1.0 - EPS)
    n = len(h)
    target = n / 2.0
    for _ in range(20):
        s = np.sum(h)
        if abs(s - target) < 1e-12:
            break
        diff = s - target
        adjustable = (h > EPS) if diff > 0 else (h < 1.0 - EPS)
        n_adj = np.sum(adjustable)
        if n_adj == 0:
            break
        h[adjustable] -= diff / n_adj
        h = np.clip(h, EPS, 1.0 - EPS)
    return h


def score(h: np.ndarray) -> float:
    """Compute overlap score robustly (never returns inf)."""
    h = np.clip(h, 0.0, 1.0)
    n = len(h)
    s = np.sum(h)
    if s == 0:
        return 1e10
    target = n / 2.0
    if abs(s - target) > 1e-8:
        h = h * (target / s)
    h = np.clip(h, 0.0, 1.0)
    corr = fftconvolve(h, (1.0 - h)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


# ---------------------------------------------------------------------------
# SLP core
# ---------------------------------------------------------------------------

def slp_step(h0: np.ndarray, trust_radius: float,
             n_active_lags: int = 100) -> np.ndarray | None:
    """One SLP step: linearize around h0, solve LP in delta-space."""
    n = len(h0)
    dx = 2.0 / n

    corr = fftconvolve(h0, (1.0 - h0)[::-1], mode="full")
    active_lag_indices = np.argsort(corr)[::-1][:n_active_lags]

    n_vars = n + 1  # [delta_0 .. delta_{n-1}, t]
    c_obj = np.zeros(n_vars)
    c_obj[n] = 1.0

    A_ub_rows = []
    b_ub_rows = []

    for L in active_lag_indices:
        k = L - (n - 1)
        ak = abs(k)
        if ak >= n:
            continue

        m = n - ak
        grad = np.zeros(n)
        jr = np.arange(m)

        if k >= 0:
            grad[jr] += 1.0 - h0[jr + k]
            np.add.at(grad, jr + k, -h0[jr])
            const = np.dot(h0[:m], h0[k:k + m])
        else:
            grad[jr + ak] += 1.0 - h0[jr]
            np.add.at(grad, jr, -h0[jr + ak])
            const = np.dot(h0[ak:ak + m], h0[:m])

        lin_at_h0 = np.dot(grad, h0) + const

        row = np.zeros(n_vars)
        row[:n] = grad * dx
        row[n] = -1.0
        A_ub_rows.append(row)
        b_ub_rows.append(-lin_at_h0 * dx)

    if not A_ub_rows:
        return None

    A_ub = np.array(A_ub_rows)
    b_ub = np.array(b_ub_rows)

    A_eq = np.zeros((1, n_vars))
    A_eq[0, :n] = 1.0
    b_eq = np.array([0.0])

    delta_lb = np.maximum(-trust_radius, EPS - h0)
    delta_ub = np.minimum(trust_radius, (1.0 - EPS) - h0)
    bounds = [(delta_lb[i], delta_ub[i]) for i in range(n)]
    bounds.append((None, None))

    try:
        result = linprog(c_obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                         bounds=bounds, method='highs',
                         options={'presolve': True, 'time_limit': 30.0})
        if result.success:
            return h0 + result.x[:n]
        return None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# SLP main loop
# ---------------------------------------------------------------------------

def slp_optimize(h_init: np.ndarray, max_iters: int = 500,
                 trust_radius_init: float = 0.05,
                 trust_radius_min: float = 1e-8,
                 trust_radius_max: float = 0.2,
                 n_active_lags: int = 200,
                 time_limit: float = 120.0,
                 label: str = "SLP") -> tuple[np.ndarray, float]:
    """Run the SLP loop with adaptive trust region, line search, and time limit."""
    n = len(h_init)
    h = project_to_feasible(h_init.copy())
    best_score = score(h)
    h_best = h.copy()
    tr = trust_radius_init
    no_improve_count = 0
    line_search_alphas = [1.0, 0.5, 0.25, 0.1, 0.05, 0.02, 0.01]

    print(f"\n  {label}: n={n}, init_score={best_score:.13f}")
    print(f"  tr={trust_radius_init}, lags={n_active_lags}, time_limit={time_limit:.0f}s")

    t0 = time.time()
    total_improvements = 0

    for it in range(max_iters):
        if time.time() - t0 > time_limit:
            print(f"  iter {it+1}: time limit reached.")
            break

        h_lp = slp_step(h, trust_radius=tr, n_active_lags=n_active_lags)

        if h_lp is None:
            tr *= 0.5
            if tr < trust_radius_min:
                print(f"  iter {it+1}: trust radius below minimum. Stopping.")
                break
            continue

        # Line search
        direction = h_lp - h
        found_better = False
        best_alpha = 0.0
        best_ls_score = best_score

        for alpha in line_search_alphas:
            h_cand = project_to_feasible(h + alpha * direction)
            sc = score(h_cand)
            if sc < best_ls_score:
                best_ls_score = sc
                best_alpha = alpha
                found_better = True

        if found_better:
            h = project_to_feasible(h + best_alpha * direction)
            improvement = best_score - best_ls_score
            best_score = best_ls_score
            h_best = h.copy()
            no_improve_count = 0
            total_improvements += 1
            tr = min(tr * 1.3, trust_radius_max)

            if total_improvements <= 3 or improvement > 1e-6 or (it + 1) % 50 == 0:
                elapsed = time.time() - t0
                print(f"  iter {it+1:4d}: C={best_score:.13f}  "
                      f"impr={improvement:.2e}  a={best_alpha:.3f}  "
                      f"tr={tr:.5f}  t={elapsed:.1f}s")
        else:
            no_improve_count += 1
            tr *= 0.6
            if tr < trust_radius_min:
                print(f"  iter {it+1}: trust radius below minimum. Stopping.")
                break
            if no_improve_count >= 10:
                n_active_lags = min(n_active_lags + 50, 2 * n - 2)
                no_improve_count = 0
                tr = max(tr * 5, trust_radius_init * 0.1)

        if (it + 1) % 100 == 0:
            elapsed = time.time() - t0
            print(f"  iter {it+1:4d}: C={best_score:.13f}  "
                  f"tr={tr:.2e}  lags={n_active_lags}  t={elapsed:.1f}s")

    elapsed = time.time() - t0
    print(f"  {label} DONE: C={best_score:.13f} in {elapsed:.1f}s "
          f"({total_improvements} improvements)")
    return h_best, best_score


# ---------------------------------------------------------------------------
# Starting points
# ---------------------------------------------------------------------------

def make_fourier_start(n: int, seed: int = 42) -> np.ndarray:
    """Construct a starting point from low-frequency Fourier components."""
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 2 * np.pi, n, endpoint=False)
    h = np.full(n, 0.5)
    for freq in range(1, 31):
        amp = rng.uniform(-0.4, 0.4) / np.sqrt(freq)
        phase = rng.uniform(0, 2 * np.pi)
        h += amp * np.cos(freq * x + phase)
    return project_to_feasible(h)


def make_perturbed_start(h_base: np.ndarray, noise_scale: float = 0.05,
                         seed: int = 123) -> np.ndarray:
    """Perturb a base solution with Gaussian noise and re-project."""
    rng = np.random.default_rng(seed)
    return project_to_feasible(h_base.copy() + rng.standard_normal(len(h_base)) * noise_scale)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("SLP OPTIMIZER: Erdos Minimum Overlap (Problem 1)")
    print("=" * 70)

    # Load SOTA
    try:
        with open("/tmp/p1_sota.json") as f:
            sota_data = json.load(f)
        h_sota = np.array(sota_data["values"], dtype=np.float64)
        n = len(h_sota)
        sota_score = fast_evaluate(h_sota)
        print(f"\nLoaded SOTA: n={n}, score={sota_score:.13f}")
    except FileNotFoundError:
        print("ERROR: /tmp/p1_sota.json not found. Using uniform start.")
        n = 600
        h_sota = np.full(n, 0.5)
        sota_score = fast_evaluate(h_sota)

    global_best_h = h_sota.copy()
    global_best_score = sota_score

    # --- (a): Polish the SOTA ---
    print("\n" + "#" * 70)
    print("# (a) SOTA starting point")
    print("#" * 70)
    h_a, score_a = slp_optimize(
        h_sota,
        max_iters=500,
        trust_radius_init=0.005,
        trust_radius_max=0.05,
        n_active_lags=300,
        time_limit=90.0,
        label="SLP-SOTA",
    )
    if score_a < global_best_score:
        global_best_score = score_a
        global_best_h = h_a.copy()
        print(f"  >>> New global best: {global_best_score:.13f}")

    # --- (b): Perturbed SOTA ---
    print("\n" + "#" * 70)
    print("# (b) Perturbed SOTA")
    print("#" * 70)
    h_perturbed = make_perturbed_start(h_sota, noise_scale=0.03, seed=777)
    print(f"  Perturbed start score: {score(h_perturbed):.13f}")
    h_b, score_b = slp_optimize(
        h_perturbed,
        max_iters=500,
        trust_radius_init=0.03,
        trust_radius_max=0.15,
        n_active_lags=200,
        time_limit=120.0,
        label="SLP-Perturbed",
    )
    if score_b < global_best_score:
        global_best_score = score_b
        global_best_h = h_b.copy()
        print(f"  >>> New global best: {global_best_score:.13f}")

    # --- (c): Fourier ---
    print("\n" + "#" * 70)
    print("# (c) Fourier starting point")
    print("#" * 70)
    h_fourier = make_fourier_start(n, seed=42)
    print(f"  Fourier start score: {score(h_fourier):.13f}")
    h_c, score_c = slp_optimize(
        h_fourier,
        max_iters=1000,
        trust_radius_init=0.10,
        trust_radius_max=0.30,
        n_active_lags=200,
        time_limit=180.0,
        label="SLP-Fourier",
    )
    if score_c < global_best_score:
        global_best_score = score_c
        global_best_h = h_c.copy()
        print(f"  >>> New global best: {global_best_score:.13f}")

    # --- Final verification ---
    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)

    exact_score = exact_evaluate({"values": global_best_h.tolist()})
    fast_score = fast_evaluate(global_best_h)

    print(f"  Original SOTA:  {sota_score:.13f}")
    print(f"  Best found:     {global_best_score:.13f}")
    print(f"  Exact verify:   {exact_score:.13f}")
    print(f"  Fast verify:    {fast_score:.13f}")
    print(f"  Improvement:    {sota_score - global_best_score:.2e}")
    print(f"  From (a) SOTA:      {score_a:.13f}")
    print(f"  From (b) Perturbed: {score_b:.13f}")
    print(f"  From (c) Fourier:   {score_c:.13f}")

    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": n,
        "score": float(exact_score),
        "values": global_best_h.tolist(),
        "method": "SLP optimizer",
        "sota_score": float(sota_score),
        "improvement": float(sota_score - exact_score),
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    out_path = "/tmp/p1_slp_best.json"
    with open(out_path, "w") as f:
        json.dump(result, f)
    print(f"\n  Saved best solution to {out_path}")
    print("=" * 70)


if __name__ == "__main__":
    main()
