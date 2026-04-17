"""Novel optimization approaches for Erdős Minimum Overlap (Problem 1).

Tries approaches NOT attempted in previous work:
1. LP relaxation with cutting planes
2. Analytical coordinate descent using exact gradients
3. Large-basin escape via structured perturbations
4. Fourier-parameterized Adam with float64
5. CVXPY SOCP relaxation

Current SOTA: 0.3808703105862199 at n=600
Target: beat by >= 1e-6 (need < 0.3808693105862199)
"""

import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from scipy.signal import fftconvolve
from scipy.optimize import linprog, minimize

from einstein.erdos.evaluator import compute_upper_bound
from einstein.erdos.fast import fast_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Global best tracking
global_best_score = float("inf")
global_best_h = None


def load_sota():
    """Load SOTA solution."""
    with open(RESULTS_DIR / "sota_together_ai_n600.json") as f:
        data = json.load(f)
    return np.array(data["values"], dtype=np.float64)


def save_if_best(h, score, tag):
    """Save solution if it improves global best."""
    global global_best_score, global_best_h
    if score < global_best_score:
        global_best_score = score
        global_best_h = h.copy()
        result = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(h),
            "score": float(score),
            "values": h.tolist(),
            "tag": tag,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"novel_{tag}_{score:.13f}.json"
        with open(fname, "w") as f:
            json.dump(result, f)
        print(f"  ** NEW BEST: {score:.16f} (tag={tag}) saved to {fname}")
        return True
    return False


def overlap_at_shift(h, k):
    """Compute overlap at a specific shift k."""
    n = len(h)
    if k >= 0:
        return np.sum(h[:n-k] * (1 - h[k:]))
    else:
        return np.sum(h[-k:] * (1 - h[:n+k]))


def all_overlaps(h):
    """Compute overlap at all shifts using FFT."""
    corr = fftconvolve(h, (1 - h)[::-1], mode="full")
    return corr


def gradient_at_shift(h, k):
    """Compute gradient of overlap(k) w.r.t. h."""
    n = len(h)
    grad = np.zeros(n)
    # d/dh_j [sum_i h_i (1-h_{i+k})] = (1-h_{j+k}) if j+k < n, minus h_{j-k} if j-k >= 0
    if k >= 0:
        grad[:n-k] += (1 - h[k:])
        grad[k:] -= h[:n-k]
    else:
        kk = -k
        grad[kk:] += (1 - h[:n-kk])
        grad[:n-kk] -= h[kk:]
    return grad


# ============================================================
# Approach 1: Analytical steepest descent with exact subgradient
# ============================================================
def approach_steepest_descent(h_init, n_iters=100000, lr_init=1e-8):
    """Steepest descent using exact subgradient of max overlap."""
    print("\n=== Approach 1: Analytical Steepest Descent ===")
    h = h_init.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    best_h = h.copy()
    improved = 0

    for it in range(n_iters):
        # Find active shift(s)
        corr = all_overlaps(h)
        max_val = np.max(corr)
        C = max_val / n * 2

        # Get shifts within 1e-8 of max
        threshold = max_val - 1e-8
        active = np.where(corr >= threshold)[0]
        active_shifts = active - (n - 1)

        # Subgradient = average of gradients at active shifts
        grad = np.zeros(n)
        for k in active_shifts:
            grad += gradient_at_shift(h, k)
        grad /= len(active_shifts)

        # Project gradient onto sum-preserving subspace
        grad -= grad.mean()

        # Adaptive learning rate
        lr = lr_init / (1 + it * 1e-5)

        # Take step
        h_new = h - lr * grad
        h_new = np.clip(h_new, 0, 1)
        # Re-normalize sum
        s = h_new.sum()
        if s > 0:
            h_new *= (n / 2.0) / s
            h_new = np.clip(h_new, 0, 1)

        new_score = fast_evaluate(h_new)
        if new_score < best_score:
            best_score = new_score
            best_h = h_new.copy()
            h = h_new
            improved += 1
        # Don't revert - continue exploring with momentum

        if (it + 1) % 10000 == 0:
            print(f"  iter {it+1}: C={best_score:.16f}, improved={improved}, "
                  f"active={len(active_shifts)}, lr={lr:.2e}")

    print(f"  Final: C={best_score:.16f}, improved={improved}")
    save_if_best(best_h, best_score, "steepest")
    return best_h, best_score


# ============================================================
# Approach 2: LP cutting plane method
# ============================================================
def approach_lp_cutting_plane(h_init, n_iters=50):
    """LP relaxation with cutting planes for the minimax problem.

    Linearize around current point, solve LP, take step.
    """
    print("\n=== Approach 2: LP Cutting Plane ===")
    h = h_init.copy()
    n = len(h)
    best_score = fast_evaluate(h)

    for it in range(n_iters):
        corr = all_overlaps(h)
        max_val = np.max(corr)
        C = max_val / n * 2

        # Find top-K shifts (cutting planes)
        top_k = min(50, 2*n-1)
        top_shifts_idx = np.argsort(corr)[::-1][:top_k]
        top_shifts = top_shifts_idx - (n - 1)

        # LP: minimize t subject to:
        #   overlap(k) linearized <= t * n/2 for each active k
        #   0 <= h_i <= 1
        #   sum(h) = n/2
        #
        # Let delta = h_new - h (decision variable)
        # overlap(k, h+delta) ≈ overlap(k, h) + grad_k . delta
        # We want: overlap(k, h) + grad_k . delta <= t * n/2
        #
        # Variables: [delta_0, ..., delta_{n-1}, t]  (n+1 variables)
        # minimize t (last variable)
        c_obj = np.zeros(n + 1)
        c_obj[-1] = 1.0  # minimize t

        # Inequality constraints: overlap(k,h) + grad_k . delta <= t * n/2
        # => grad_k . delta - t * n/2 <= -overlap(k,h)
        A_ub = np.zeros((top_k, n + 1))
        b_ub = np.zeros(top_k)
        for i, k in enumerate(top_shifts):
            g = gradient_at_shift(h, k)
            A_ub[i, :n] = g
            A_ub[i, n] = -n / 2.0  # -t * n/2
            b_ub[i] = -overlap_at_shift(h, k)

        # Equality: sum(delta) = 0 (preserve sum)
        A_eq = np.zeros((1, n + 1))
        A_eq[0, :n] = 1.0
        b_eq = np.array([0.0])

        # Bounds: -h_i <= delta_i <= 1 - h_i, t >= 0
        bounds = [(-h[i], 1 - h[i]) for i in range(n)] + [(0, None)]

        try:
            res = linprog(c_obj, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                         bounds=bounds, method='highs')
            if res.success:
                delta = res.x[:n]
                t_opt = res.x[n]
                # Line search along delta direction
                best_alpha = 0
                for alpha in [1.0, 0.5, 0.25, 0.1, 0.05, 0.01, 0.001]:
                    h_try = h + alpha * delta
                    h_try = np.clip(h_try, 0, 1)
                    s = h_try.sum()
                    if s > 0:
                        h_try *= (n / 2.0) / s
                        h_try = np.clip(h_try, 0, 1)
                    score = fast_evaluate(h_try)
                    if score < best_score:
                        best_score = score
                        best_alpha = alpha
                        h = h_try

                if best_alpha > 0:
                    print(f"  LP iter {it+1}: C={best_score:.16f}, alpha={best_alpha}, "
                          f"LP_t={t_opt*2/n:.16f}")
                else:
                    print(f"  LP iter {it+1}: no improvement (LP_t={t_opt*2/n:.16f}, "
                          f"current C={C:.16f})")
            else:
                print(f"  LP iter {it+1}: solver failed: {res.message}")
        except Exception as e:
            print(f"  LP iter {it+1}: error: {e}")

    save_if_best(h, best_score, "lp_cutting")
    return h, best_score


# ============================================================
# Approach 3: Structured large perturbations (basin escape)
# ============================================================
def approach_basin_escape(h_init, n_trials=200, time_limit=600):
    """Try large structured perturbations to escape current basin.

    Uses mathematical structures: sine waves, step functions,
    block swaps, and combinations.
    """
    print("\n=== Approach 3: Basin Escape ===")
    n = len(h_init)
    best_score = fast_evaluate(h_init)
    best_h = h_init.copy()
    t0 = time.time()

    perturbation_types = [
        "sine_wave", "step_swap", "block_rotate", "fourier_random",
        "gradient_escape", "mirror_blend", "random_reinit_partial",
        "golden_ratio", "binary_snap", "smooth_blend"
    ]

    for trial in range(n_trials):
        if time.time() - t0 > time_limit:
            print(f"  Time limit reached at trial {trial}")
            break

        ptype = perturbation_types[trial % len(perturbation_types)]
        rng = np.random.default_rng(trial * 137 + 42)

        h_try = h_init.copy()

        if ptype == "sine_wave":
            # Add a sine wave perturbation at random frequency/phase
            freq = rng.integers(1, 50)
            phase = rng.uniform(0, 2 * np.pi)
            amp = rng.uniform(0.001, 0.1)
            x = np.linspace(0, 2 * np.pi * freq, n)
            h_try += amp * np.sin(x + phase)

        elif ptype == "step_swap":
            # Swap two random blocks
            block_size = rng.integers(10, n // 4)
            i1 = rng.integers(0, n - block_size)
            i2 = rng.integers(0, n - block_size)
            h_try[i1:i1+block_size], h_try[i2:i2+block_size] = \
                h_try[i2:i2+block_size].copy(), h_try[i1:i1+block_size].copy()

        elif ptype == "block_rotate":
            # Circular shift a block
            block_size = rng.integers(20, n // 2)
            start = rng.integers(0, n - block_size)
            shift = rng.integers(1, block_size)
            block = h_try[start:start+block_size].copy()
            h_try[start:start+block_size] = np.roll(block, shift)

        elif ptype == "fourier_random":
            # Perturb Fourier coefficients
            from scipy.fft import rfft, irfft
            H = rfft(h_try)
            n_modes = rng.integers(5, 30)
            modes = rng.choice(len(H), n_modes, replace=False)
            for m in modes:
                H[m] *= (1 + rng.uniform(-0.1, 0.1))
                H[m] *= np.exp(1j * rng.uniform(-0.1, 0.1))
            h_try = irfft(H, n=n)

        elif ptype == "gradient_escape":
            # Move UPHILL along gradient (escape local minimum)
            corr = all_overlaps(h_try)
            k_max = np.argmax(corr) - (n - 1)
            grad = gradient_at_shift(h_try, k_max)
            grad -= grad.mean()
            step = rng.uniform(0.01, 0.1)
            h_try = h_try + step * grad  # uphill!

        elif ptype == "mirror_blend":
            # Blend with mirror image
            alpha = rng.uniform(0.05, 0.5)
            h_try = (1 - alpha) * h_try + alpha * h_try[::-1]

        elif ptype == "random_reinit_partial":
            # Reinitialize a random region
            region_size = rng.integers(50, 200)
            start = rng.integers(0, n - region_size)
            h_try[start:start+region_size] = rng.uniform(0, 1, region_size)

        elif ptype == "golden_ratio":
            # Golden ratio modulated perturbation
            phi = (1 + np.sqrt(5)) / 2
            x = np.arange(n) * phi % 1
            amp = rng.uniform(0.01, 0.1)
            h_try += amp * (x - 0.5)

        elif ptype == "binary_snap":
            # Snap to binary (0/1) based on threshold
            threshold = rng.uniform(0.3, 0.7)
            h_try = np.where(h_try > threshold, 1.0, 0.0).astype(np.float64)
            # Add small random noise to break ties
            h_try += rng.uniform(-0.01, 0.01, n)

        elif ptype == "smooth_blend":
            # Blend with a smooth curve (e.g., sigmoid)
            center = rng.uniform(0.2, 0.8) * n
            width = rng.uniform(10, 100)
            sigmoid = 1.0 / (1.0 + np.exp(-(np.arange(n) - center) / width))
            alpha = rng.uniform(0.05, 0.3)
            h_try = (1 - alpha) * h_try + alpha * sigmoid

        # Project to feasible set
        h_try = np.clip(h_try, 0, 1)
        s = h_try.sum()
        if s > 0:
            h_try *= (n / 2.0) / s
            h_try = np.clip(h_try, 0, 1)
            # May need iterative normalization
            for _ in range(10):
                s = h_try.sum()
                if abs(s - n/2) < 1e-10:
                    break
                h_try *= (n / 2.0) / s
                h_try = np.clip(h_try, 0, 1)

        score_perturbed = fast_evaluate(h_try)

        # Now polish with local search (short)
        h_polished, score_polished = quick_polish(h_try, n_iters=50000)

        if score_polished < best_score:
            best_score = score_polished
            best_h = h_polished.copy()
            print(f"  Trial {trial} ({ptype}): IMPROVED to {best_score:.16f}")
        elif (trial + 1) % 20 == 0:
            print(f"  Trial {trial+1}: best={best_score:.16f}, "
                  f"this={score_polished:.10f} ({ptype})")

    save_if_best(best_h, best_score, "basin_escape")
    return best_h, best_score


def quick_polish(h, n_iters=50000):
    """Quick random local search polish."""
    rng = np.random.default_rng(42)
    h = np.clip(h.copy(), 0, 1)
    n = len(h)
    best = fast_evaluate(h)

    for _ in range(n_iters):
        n_pts = rng.choice([2, 3, 4])
        idx = rng.choice(n, size=n_pts, replace=False)
        delta = rng.standard_normal(n_pts) * 1e-5
        delta -= delta.mean()

        old = h[idx].copy()
        new = old + delta
        if np.any(new < 0) or np.any(new > 1):
            continue

        h[idx] = new
        score = fast_evaluate(h)
        if score < best:
            best = score
        else:
            h[idx] = old

    return h, best


# ============================================================
# Approach 4: Fourier-parameterized optimization (float64)
# ============================================================
def approach_fourier_adam(n=600, n_modes=100, n_iters=50000, lr=1e-4, seed=0):
    """Optimize in Fourier space with Adam (float64, CPU).

    Parameterize h = IDFT(coefficients), optimize coefficients.
    """
    print(f"\n=== Approach 4: Fourier Adam (modes={n_modes}) ===")
    from scipy.fft import rfft, irfft

    # Initialize from SOTA's Fourier coefficients
    h_sota = load_sota()
    H_sota = rfft(h_sota)

    # Only optimize first n_modes coefficients
    rng = np.random.default_rng(seed)
    coeffs_real = np.real(H_sota[:n_modes+1]).copy()
    coeffs_imag = np.imag(H_sota[:n_modes+1]).copy()

    best_score = fast_evaluate(h_sota)
    best_h = h_sota.copy()
    best_coeffs_real = coeffs_real.copy()
    best_coeffs_imag = coeffs_imag.copy()

    # Adam state
    m_r = np.zeros_like(coeffs_real)
    v_r = np.zeros_like(coeffs_real)
    m_i = np.zeros_like(coeffs_imag)
    v_i = np.zeros_like(coeffs_imag)
    beta1, beta2, eps = 0.9, 0.999, 1e-8

    for it in range(n_iters):
        # Reconstruct h from coefficients
        H_full = H_sota.copy()
        H_full[:n_modes+1] = coeffs_real + 1j * coeffs_imag
        h = irfft(H_full, n=n)

        # Project
        h = np.clip(h, 0, 1)
        s = h.sum()
        if s > 0:
            h *= (n / 2.0) / s
            h = np.clip(h, 0, 1)

        score = fast_evaluate(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()
            best_coeffs_real = coeffs_real.copy()
            best_coeffs_imag = coeffs_imag.copy()

        # Numerical gradient via finite differences
        grad_r = np.zeros_like(coeffs_real)
        grad_i = np.zeros_like(coeffs_imag)
        eps_fd = 1e-10
        for m in range(min(n_modes+1, 30)):  # Only compute gradient for top modes
            # Real part
            coeffs_real[m] += eps_fd
            H_full[:n_modes+1] = coeffs_real + 1j * coeffs_imag
            h_plus = np.clip(irfft(H_full, n=n), 0, 1)
            s = h_plus.sum()
            if s > 0: h_plus *= (n/2.0)/s; h_plus = np.clip(h_plus, 0, 1)
            coeffs_real[m] -= 2 * eps_fd
            H_full[:n_modes+1] = coeffs_real + 1j * coeffs_imag
            h_minus = np.clip(irfft(H_full, n=n), 0, 1)
            s = h_minus.sum()
            if s > 0: h_minus *= (n/2.0)/s; h_minus = np.clip(h_minus, 0, 1)
            coeffs_real[m] += eps_fd  # restore
            grad_r[m] = (fast_evaluate(h_plus) - fast_evaluate(h_minus)) / (2 * eps_fd)

            # Imaginary part
            coeffs_imag[m] += eps_fd
            H_full[:n_modes+1] = coeffs_real + 1j * coeffs_imag
            h_plus = np.clip(irfft(H_full, n=n), 0, 1)
            s = h_plus.sum()
            if s > 0: h_plus *= (n/2.0)/s; h_plus = np.clip(h_plus, 0, 1)
            coeffs_imag[m] -= 2 * eps_fd
            H_full[:n_modes+1] = coeffs_real + 1j * coeffs_imag
            h_minus = np.clip(irfft(H_full, n=n), 0, 1)
            s = h_minus.sum()
            if s > 0: h_minus *= (n/2.0)/s; h_minus = np.clip(h_minus, 0, 1)
            coeffs_imag[m] += eps_fd  # restore
            grad_i[m] = (fast_evaluate(h_plus) - fast_evaluate(h_minus)) / (2 * eps_fd)

        # Adam update
        t = it + 1
        m_r = beta1 * m_r + (1 - beta1) * grad_r
        v_r = beta2 * v_r + (1 - beta2) * grad_r**2
        m_i = beta1 * m_i + (1 - beta1) * grad_i
        v_i = beta2 * v_i + (1 - beta2) * grad_i**2

        m_r_hat = m_r / (1 - beta1**t)
        v_r_hat = v_r / (1 - beta2**t)
        m_i_hat = m_i / (1 - beta1**t)
        v_i_hat = v_i / (1 - beta2**t)

        coeffs_real -= lr * m_r_hat / (np.sqrt(v_r_hat) + eps)
        coeffs_imag -= lr * m_i_hat / (np.sqrt(v_i_hat) + eps)

        if (it + 1) % 5000 == 0:
            print(f"  iter {it+1}: C={best_score:.16f}, |grad|={np.linalg.norm(grad_r):.2e}")

    save_if_best(best_h, best_score, "fourier_adam")
    return best_h, best_score


# ============================================================
# Approach 5: CVXPY SOCP/SDP relaxation
# ============================================================
def approach_cvxpy_relaxation(h_init):
    """Solve LP relaxation using CVXPY."""
    print("\n=== Approach 5: CVXPY LP Relaxation ===")
    try:
        import cvxpy as cp
    except ImportError:
        print("  CVXPY not available, skipping")
        return h_init, fast_evaluate(h_init)

    n = len(h_init)

    # Decision variable
    h = cp.Variable(n)
    t = cp.Variable()  # upper bound on overlap

    constraints = [
        h >= 0,
        h <= 1,
        cp.sum(h) == n / 2.0,
        t >= 0,
    ]

    # For each shift k, overlap(k) = h^T M_k (1 - h) where M_k is a shift matrix
    # This is bilinear, so we can't use LP directly.
    # Instead, linearize around h_init:
    # overlap(k, h) ≈ overlap(k, h0) + grad_k^T (h - h0)
    h0 = h_init

    # Add cutting planes for top shifts
    corr = all_overlaps(h0)
    top_indices = np.argsort(corr)[::-1][:100]

    for idx in top_indices:
        k = idx - (n - 1)
        g = gradient_at_shift(h0, k)
        ov0 = overlap_at_shift(h0, k)
        # overlap(k) ≈ ov0 + g^T (h - h0) <= t * n/2
        constraints.append(ov0 + g @ (h - h0) <= t * n / 2.0)

    prob = cp.Problem(cp.Minimize(t), constraints)
    try:
        prob.solve(solver=cp.CLARABEL, verbose=False, max_iter=10000)
        if prob.status == "optimal":
            h_opt = h.value
            t_opt = t.value
            print(f"  LP bound: t = {t_opt:.16f} (C = {t_opt * 2/n:.16f})")
            print(f"  Current C = {fast_evaluate(h0):.16f}")

            # Polish the LP solution
            h_clipped = np.clip(h_opt, 0, 1)
            s = h_clipped.sum()
            if s > 0:
                h_clipped *= (n / 2.0) / s
                h_clipped = np.clip(h_clipped, 0, 1)
            lp_score = fast_evaluate(h_clipped)
            print(f"  LP solution score: {lp_score:.16f}")

            # Polish further
            h_polished, score_polished = quick_polish(h_clipped, n_iters=200000)
            print(f"  After polish: {score_polished:.16f}")

            save_if_best(h_polished, score_polished, "cvxpy_lp")
            return h_polished, score_polished
        else:
            print(f"  CVXPY status: {prob.status}")
    except Exception as e:
        print(f"  CVXPY error: {e}")

    return h_init, fast_evaluate(h_init)


# ============================================================
# Approach 6: scipy.optimize.minimize with L-BFGS-B
# ============================================================
def approach_lbfgsb(h_init, max_iter=1000):
    """L-BFGS-B on a smooth approximation of the max overlap."""
    print("\n=== Approach 6: L-BFGS-B (LogSumExp smooth max) ===")
    n = len(h_init)

    # Use LogSumExp to smooth the max
    for beta in [100, 500, 1000, 5000, 10000]:
        def objective(h_flat):
            h = h_flat.copy()
            h = np.clip(h, 0, 1)
            s = h.sum()
            if s > 0:
                h *= (n / 2.0) / s
                h = np.clip(h, 0, 1)
            corr = fftconvolve(h, (1 - h)[::-1], mode="full")
            # LogSumExp approximation of max
            shifted = beta * (corr - corr.max())
            lse = corr.max() + np.log(np.sum(np.exp(shifted))) / beta
            return lse / n * 2

        bounds = [(0, 1)] * n
        result = minimize(objective, h_init, method='L-BFGS-B', bounds=bounds,
                         options={'maxiter': max_iter, 'ftol': 1e-15, 'gtol': 1e-12})

        h_opt = np.clip(result.x, 0, 1)
        s = h_opt.sum()
        if s > 0:
            h_opt *= (n / 2.0) / s
            h_opt = np.clip(h_opt, 0, 1)

        score = fast_evaluate(h_opt)
        exact = compute_upper_bound(h_opt.tolist())
        print(f"  beta={beta}: C={exact:.16f} (fast={score:.16f}), "
              f"converged={result.success}")

        save_if_best(h_opt, exact, f"lbfgsb_b{beta}")

    return h_opt, exact


# ============================================================
# Approach 7: Population-based diverse start
# ============================================================
def approach_diverse_population(n=600, n_candidates=50, polish_iters=500000,
                                 time_limit=1200):
    """Start from diverse mathematical constructions, polish each."""
    print("\n=== Approach 7: Diverse Population ===")
    t0 = time.time()
    best_score = float("inf")
    best_h = None

    candidates = []

    # 1. SOTA
    candidates.append(("sota", load_sota()))

    # 2. Random uniform
    for seed in range(5):
        rng = np.random.default_rng(seed)
        h = rng.uniform(0, 1, n)
        h *= (n/2) / h.sum()
        h = np.clip(h, 0, 1)
        candidates.append((f"random_{seed}", h))

    # 3. Binary patterns (characteristic functions)
    for seed in range(5):
        rng = np.random.default_rng(seed + 100)
        h = np.zeros(n)
        # Randomly select n/2 indices to be 1
        indices = rng.choice(n, n//2, replace=False)
        h[indices] = 1.0
        candidates.append((f"binary_{seed}", h))

    # 4. Haugland-style piecewise constant (few pieces)
    for n_pieces in [10, 20, 30, 51, 80]:
        rng = np.random.default_rng(n_pieces)
        breakpoints = np.sort(rng.choice(n, n_pieces - 1, replace=False))
        breakpoints = np.concatenate([[0], breakpoints, [n]])
        h = np.zeros(n)
        for i in range(len(breakpoints) - 1):
            h[breakpoints[i]:breakpoints[i+1]] = rng.uniform(0, 1)
        h *= (n/2) / h.sum()
        h = np.clip(h, 0, 1)
        candidates.append((f"piecewise_{n_pieces}", h))

    # 5. Fourier-based construction
    for n_modes in [5, 10, 20, 50]:
        rng = np.random.default_rng(n_modes + 200)
        from scipy.fft import irfft
        H = np.zeros(n // 2 + 1, dtype=complex)
        H[0] = n / 2  # DC component for sum = n/2
        for m in range(1, n_modes + 1):
            H[m] = rng.standard_normal() * (10 / m) + 1j * rng.standard_normal() * (10 / m)
        h = irfft(H, n=n)
        h = np.clip(h, 0, 1)
        h *= (n/2) / h.sum()
        h = np.clip(h, 0, 1)
        candidates.append((f"fourier_{n_modes}", h))

    # 6. Sigmoid-based
    for center_frac in [0.3, 0.4, 0.5, 0.6, 0.7]:
        center = center_frac * n
        h = 1.0 / (1 + np.exp(-(np.arange(n) - center) / 20))
        h *= (n/2) / h.sum()
        h = np.clip(h, 0, 1)
        candidates.append((f"sigmoid_{center_frac}", h))

    # 7. SOTA with large random perturbation
    h_sota = load_sota()
    for amp in [0.01, 0.05, 0.1, 0.2, 0.5]:
        rng = np.random.default_rng(int(amp * 1000))
        h = h_sota + amp * rng.standard_normal(n)
        h = np.clip(h, 0, 1)
        h *= (n/2) / h.sum()
        h = np.clip(h, 0, 1)
        candidates.append((f"sota_perturb_{amp}", h))

    print(f"  Total candidates: {len(candidates)}")

    for i, (name, h) in enumerate(candidates):
        if time.time() - t0 > time_limit:
            print(f"  Time limit at candidate {i}")
            break

        raw_score = fast_evaluate(h)
        h_polished, score = quick_polish(h, n_iters=min(polish_iters, 100000))

        if score < best_score:
            best_score = score
            best_h = h_polished.copy()
            print(f"  #{i} {name}: {raw_score:.10f} -> {score:.16f} ** BEST **")
        elif (i + 1) % 5 == 0:
            print(f"  #{i} {name}: {raw_score:.10f} -> {score:.10f}")

    if best_h is not None:
        # Final heavy polish on the best
        print(f"\n  Final heavy polish on best (C={best_score:.16f})...")
        best_h, best_score = quick_polish(best_h, n_iters=500000)
        print(f"  After heavy polish: {best_score:.16f}")
        save_if_best(best_h, best_score, "diverse_pop")

    return best_h, best_score


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 70)
    print("Erdős Minimum Overlap — Novel Optimization Approaches")
    print("=" * 70)
    t_start = time.time()

    h_sota = load_sota()
    sota_score = fast_evaluate(h_sota)
    exact_sota = compute_upper_bound(h_sota.tolist())
    print(f"SOTA: {exact_sota:.16f} (fast: {sota_score:.16f})")
    print(f"Target: < {exact_sota - 1e-6:.16f}")
    global global_best_score, global_best_h
    global_best_score = exact_sota
    global_best_h = h_sota.copy()

    # Run approaches
    # 1. Steepest descent (fast, low overhead)
    approach_steepest_descent(h_sota, n_iters=50000, lr_init=1e-9)
    print(f"\n>>> Global best after Approach 1: {global_best_score:.16f}")

    # 2. LP cutting plane
    approach_lp_cutting_plane(h_sota, n_iters=30)
    print(f"\n>>> Global best after Approach 2: {global_best_score:.16f}")

    # 3. Basin escape
    approach_basin_escape(h_sota, n_trials=100, time_limit=300)
    print(f"\n>>> Global best after Approach 3: {global_best_score:.16f}")

    # 4. Fourier Adam (only if still have time)
    elapsed = time.time() - t_start
    if elapsed < 3600:
        approach_fourier_adam(n=600, n_modes=50, n_iters=20000, lr=1e-5)
        print(f"\n>>> Global best after Approach 4: {global_best_score:.16f}")

    # 5. CVXPY relaxation
    elapsed = time.time() - t_start
    if elapsed < 5400:
        approach_cvxpy_relaxation(h_sota)
        print(f"\n>>> Global best after Approach 5: {global_best_score:.16f}")

    # 6. L-BFGS-B
    elapsed = time.time() - t_start
    if elapsed < 7200:
        approach_lbfgsb(h_sota, max_iter=500)
        print(f"\n>>> Global best after Approach 6: {global_best_score:.16f}")

    # 7. Diverse population
    elapsed = time.time() - t_start
    remaining = max(600, 10800 - elapsed)
    if elapsed < 9000:
        approach_diverse_population(n=600, n_candidates=50,
                                    polish_iters=200000, time_limit=remaining)
        print(f"\n>>> Global best after Approach 7: {global_best_score:.16f}")

    # Final verification
    print(f"\n{'=' * 70}")
    print(f"FINAL RESULTS")
    print(f"{'=' * 70}")
    if global_best_h is not None:
        exact_final = compute_upper_bound(global_best_h.tolist())
        fast_final = fast_evaluate(global_best_h)
        print(f"Best score (exact):  {exact_final:.16f}")
        print(f"Best score (fast):   {fast_final:.16f}")
        print(f"SOTA score:          {exact_sota:.16f}")
        print(f"Improvement:         {exact_sota - exact_final:.2e}")
        print(f"Needed improvement:  1.0e-06")
        print(f"Sufficient:          {exact_sota - exact_final >= 1e-6}")

        # Save final best
        result = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(global_best_h),
            "score": float(exact_final),
            "values": global_best_h.tolist(),
            "tag": "novel_final",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"novel_FINAL_{exact_final:.13f}.json"
        with open(fname, "w") as f:
            json.dump(result, f)
        print(f"Saved to {fname}")
    else:
        print("No improvement found.")

    total = time.time() - t_start
    print(f"\nTotal time: {total:.0f}s ({total/60:.1f}min)")


if __name__ == "__main__":
    main()
