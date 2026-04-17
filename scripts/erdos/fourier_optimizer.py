"""Fourier-constrained optimizer for Erdős Minimum Overlap (Problem 1).

Inspired by White (2022) (arXiv:2201.05704): the even Fourier coefficients
of the overlap function are nonpositive, providing additional constraints.

Three approaches:
  A. Fourier parametrization with LogSumExp smooth max + L-BFGS-B
  B. Iterative projection (POCS) exploiting Fourier constraints
  C. Direct CVXPY formulation (autocorrelation LP + spectral factorization)

Problem: minimize C = max_k correlate(h, 1-h, k) * 2/n
         subject to h in [0,1]^n, sum(h) = n/2

Usage:
    cd /Users/jmsung/projects/einstein/cb-feat-auto-p1
    uv run python3 scripts/erdos/fourier_optimizer.py
"""

import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np
from scipy.optimize import minimize as scipy_minimize, differential_evolution
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

warnings.filterwarnings("ignore", category=FutureWarning)

OUTPUT_PATH = Path("/tmp/p1_fourier_best.json")
RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Shared utilities
# ---------------------------------------------------------------------------


def normalize(h: np.ndarray) -> np.ndarray:
    """Project h onto [0,1] with sum = n/2.

    Iterates clip-then-scale to handle cases where scaling pushes values > 1.
    """
    h = np.clip(h, 0, 1)
    n = len(h)
    for _ in range(10):
        s = np.sum(h)
        if s == 0:
            h = np.full(n, 0.5)
            break
        h = h * (n / 2.0 / s)
        if np.all(h <= 1.0) and np.all(h >= 0.0):
            break
        h = np.clip(h, 0, 1)
    return h


def fast_eval(h: np.ndarray) -> float:
    """Compute C = max(correlate(h, 1-h, 'full')) * 2/n."""
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


def correlation_profile(h: np.ndarray) -> np.ndarray:
    """Return full correlation array correlate(h, 1-h, 'full')."""
    return fftconvolve(h, (1.0 - h)[::-1], mode="full")


def save_solution(h: np.ndarray, score: float, tag: str) -> None:
    """Save solution to results directory."""
    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": len(h),
        "score": float(score),
        "values": h.tolist(),
        "source": f"fourier_optimizer/{tag}",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"erdos_n{len(h)}_{score:.10f}_{tag}.json"
    with open(fname, "w") as f:
        json.dump(result, f)
    print(f"  Saved: {fname}")


# ---------------------------------------------------------------------------
# Approach A: Fourier parametrization
# ---------------------------------------------------------------------------


def fourier_to_h(coeffs: np.ndarray, n: int) -> np.ndarray:
    """Build h(x) = 0.5 + sum_k a_k cos(pi*k*x/L) on [0,2), then normalize.

    The period L=2 matches the problem domain [0,2].
    """
    K = len(coeffs)
    x = np.linspace(0, 2, n, endpoint=False)
    h = np.full(n, 0.5)
    for k in range(K):
        h += coeffs[k] * np.cos(np.pi * (k + 1) * x / 2.0)
    return normalize(h)


def fourier_to_h_sincos(coeffs: np.ndarray, n: int) -> np.ndarray:
    """Build h(x) = 0.5 + sum_k [a_k cos + b_k sin](pi*k*x/2).

    Uses both cosine and sine terms for more flexibility.
    coeffs = [a_1, b_1, a_2, b_2, ...] length 2K.
    """
    K = len(coeffs) // 2
    x = np.linspace(0, 2, n, endpoint=False)
    h = np.full(n, 0.5)
    for k in range(K):
        freq = np.pi * (k + 1) * x / 2.0
        h += coeffs[2 * k] * np.cos(freq) + coeffs[2 * k + 1] * np.sin(freq)
    return normalize(h)


def logsumexp_max(arr: np.ndarray, beta: float = 50.0) -> float:
    """Smooth approximation of max via LogSumExp."""
    m = np.max(arr)
    return m + np.log(np.sum(np.exp(beta * (arr - m)))) / beta


def approach_a_objective(coeffs, n, beta):
    """Objective for Approach A: LogSumExp smooth max of overlap."""
    h = fourier_to_h(coeffs, n)
    corr = correlation_profile(h)
    return logsumexp_max(corr, beta=beta) / n * 2


def approach_a_sincos_objective(coeffs, n, beta):
    """Objective with sin+cos parametrization."""
    h = fourier_to_h_sincos(coeffs, n)
    corr = correlation_profile(h)
    return logsumexp_max(corr, beta=beta) / n * 2


def approach_a(n: int = 600, K_values: list[int] | None = None,
               time_limit: float = 900.0) -> tuple[np.ndarray | None, float]:
    """Approach A: Fourier parametrization with L-BFGS-B.

    Parametrize h as Fourier series. Optimize coefficients to minimize C
    using smooth LogSumExp max. Try multiple K values, beta schedules,
    and random initializations. Cascade best results between K values.
    """
    if K_values is None:
        K_values = [20, 50, 100, 200]

    print("\n" + "=" * 70)
    print("APPROACH A: Fourier Parametrization + L-BFGS-B")
    print("=" * 70)

    best_h = None
    best_score = float("inf")
    best_coeffs = None
    t0 = time.time()

    for K in K_values:
        if time.time() - t0 > time_limit:
            print(f"  Time limit reached, skipping K={K}")
            break

        print(f"\n  --- K={K} Fourier modes (cosine) ---")
        trial_best = float("inf")
        trial_h = None
        trial_coeffs = None

        # Generate diverse initializations
        inits = []
        for seed in range(4):
            rng = np.random.default_rng(seed + K * 100)
            # Amplitude decays with frequency
            x0 = rng.standard_normal(K) * 0.15 / np.sqrt(np.arange(1, K + 1))
            inits.append((f"rand_s{seed}", x0))

        # Warm-start from best at previous K if available
        if best_coeffs is not None:
            prev_K = len(best_coeffs)
            if K > prev_K:
                x0_warm = np.zeros(K)
                x0_warm[:prev_K] = best_coeffs
                inits.insert(0, ("warm_prev", x0_warm))
            elif K == prev_K:
                inits.insert(0, ("warm_prev", best_coeffs.copy()))

        # Beta schedule: start smooth, then sharpen
        beta_schedule = [10.0, 50.0, 200.0, 500.0]

        for name, x0 in inits:
            if time.time() - t0 > time_limit:
                break

            current_x = x0.copy()
            for beta in beta_schedule:
                if time.time() - t0 > time_limit:
                    break

                try:
                    result = scipy_minimize(
                        approach_a_objective,
                        current_x,
                        args=(n, beta),
                        method="L-BFGS-B",
                        options={"maxiter": 3000, "ftol": 1e-15, "gtol": 1e-12},
                    )
                    h = fourier_to_h(result.x, n)
                    score = fast_eval(h)

                    if score < trial_best:
                        trial_best = score
                        trial_h = h.copy()
                        trial_coeffs = result.x.copy()
                        current_x = result.x.copy()  # warm-start next beta
                    else:
                        current_x = result.x.copy()

                except Exception as e:
                    print(f"    {name}, beta={beta:.0f}: error - {e}")
                    continue

            if trial_best < float("inf"):
                print(f"    {name}: C = {trial_best:.13f}")

        # Also try sin+cos parametrization
        print(f"\n  --- K={K} Fourier modes (sin+cos) ---")
        for seed in range(2):
            if time.time() - t0 > time_limit:
                break

            rng = np.random.default_rng(seed + K * 200 + 1000)
            x0 = rng.standard_normal(2 * K) * 0.1 / np.sqrt(
                np.repeat(np.arange(1, K + 1), 2))

            current_x = x0.copy()
            for beta in [30.0, 100.0, 300.0]:
                if time.time() - t0 > time_limit:
                    break

                try:
                    result = scipy_minimize(
                        approach_a_sincos_objective,
                        current_x,
                        args=(n, beta),
                        method="L-BFGS-B",
                        options={"maxiter": 3000, "ftol": 1e-15, "gtol": 1e-12},
                    )
                    h = fourier_to_h_sincos(result.x, n)
                    score = fast_eval(h)

                    if score < trial_best:
                        trial_best = score
                        trial_h = h.copy()
                        # Don't set trial_coeffs for sincos (different basis)
                    current_x = result.x.copy()

                except Exception:
                    continue

            print(f"    sincos s{seed}: C = {trial_best:.13f}")

        # Refinement: re-fit Fourier coefficients to current best
        if trial_h is not None:
            x = np.linspace(0, 2, n, endpoint=False)
            A = np.zeros((n, K))
            for k in range(K):
                A[:, k] = np.cos(np.pi * (k + 1) * x / 2.0)
            coeffs_fit, _, _, _ = np.linalg.lstsq(A, trial_h - 0.5, rcond=None)

            for beta in [300.0, 1000.0]:
                if time.time() - t0 > time_limit:
                    break
                result = scipy_minimize(
                    approach_a_objective,
                    coeffs_fit,
                    args=(n, beta),
                    method="L-BFGS-B",
                    options={"maxiter": 5000, "ftol": 1e-15, "gtol": 1e-12},
                )
                h = fourier_to_h(result.x, n)
                score = fast_eval(h)
                if score < trial_best:
                    trial_best = score
                    trial_h = h.copy()
                    trial_coeffs = result.x.copy()

            print(f"  K={K} final: C = {trial_best:.13f}")

        if trial_h is not None and trial_best < best_score:
            best_score = trial_best
            best_h = trial_h.copy()
            if trial_coeffs is not None:
                best_coeffs = trial_coeffs.copy()
            print(f"  >>> NEW GLOBAL BEST: C = {best_score:.13f}")

    elapsed = time.time() - t0
    print(f"\n  Approach A complete: best C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Approach A2: Direct optimization on h values
# ---------------------------------------------------------------------------


def direct_h_objective(h_flat, n, beta):
    """Objective for direct optimization on h values."""
    h = normalize(h_flat.copy())
    corr = correlation_profile(h)
    return logsumexp_max(corr, beta=beta) / n * 2


def approach_a2_direct(n: int = 600, time_limit: float = 600.0,
                       warm_h: np.ndarray | None = None
                       ) -> tuple[np.ndarray | None, float]:
    """Direct L-BFGS-B optimization on all n values of h.

    Uses LogSumExp smooth max with annealing beta schedule.
    This is more flexible than Fourier parametrization but higher dimensional.
    """
    print("\n" + "=" * 70)
    print("APPROACH A2: Direct L-BFGS-B on h values")
    print("=" * 70)

    best_h = None
    best_score = float("inf")
    t0 = time.time()

    inits = []

    # Fourier-based diverse initializations
    for K in [10, 20, 50, 100]:
        for seed in range(3):
            rng = np.random.default_rng(seed + K * 37)
            coeffs = rng.standard_normal(K) * 0.15 / np.sqrt(np.arange(1, K + 1))
            h = fourier_to_h(coeffs, n)
            inits.append((f"fourier_K{K}_s{seed}", h))

    if warm_h is not None:
        inits.insert(0, ("warm_start", warm_h.copy()))

    bounds = [(0.0, 1.0)] * n

    for name, h0 in inits:
        if time.time() - t0 > time_limit:
            break

        current_h = h0.copy()
        for beta in [10.0, 50.0, 200.0, 500.0]:
            if time.time() - t0 > time_limit:
                break

            try:
                result = scipy_minimize(
                    direct_h_objective,
                    current_h,
                    args=(n, beta),
                    method="L-BFGS-B",
                    bounds=bounds,
                    options={"maxiter": 2000, "ftol": 1e-15, "gtol": 1e-12},
                )
                h = normalize(result.x)
                score = fast_eval(h)
                if score < best_score:
                    best_score = score
                    best_h = h.copy()
                    print(f"  {name}, beta={beta:.0f}: C = {score:.13f} ***")
                current_h = result.x.copy()
            except Exception as e:
                print(f"  {name}, beta={beta:.0f}: error - {e}")

        # Print progress for each init
        print(f"  {name} done, best so far: C = {best_score:.13f}")

    elapsed = time.time() - t0
    print(f"\n  Approach A2 complete: best C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Approach B: Iterative Projection (POCS)
# ---------------------------------------------------------------------------


def gradient_wrt_max_lag(h: np.ndarray) -> np.ndarray:
    """Compute gradient of max overlap C w.r.t. h.

    C = max_k corr(k) * 2/n
    corr(k) = sum_j h[j] * (1 - h[j-k])  (for the argmax lag k)

    d corr(k)/dh[j] = (1 - h[j-k]) - h[j+k]  (where indices are valid)
    """
    n = len(h)
    corr = correlation_profile(h)
    max_idx = np.argmax(corr)
    lag = max_idx - (n - 1)  # correlation index to lag

    grad = np.zeros(n)
    for j in range(n):
        # d/dh[j] of sum_m h[m]*(1 - h[m - lag])
        # = (1 - h[j - lag]) when m = j, plus -h[j + lag] when m - lag = j
        j_minus_lag = j - lag
        j_plus_lag = j + lag
        if 0 <= j_minus_lag < n:
            grad[j] += (1.0 - h[j_minus_lag])
        if 0 <= j_plus_lag < n:
            grad[j] -= h[j_plus_lag]

    return grad * 2.0 / n


def approach_b(n: int = 600, time_limit: float = 900.0,
               warm_h: np.ndarray | None = None
               ) -> tuple[np.ndarray | None, float]:
    """Approach B: Iterative Projection (POCS).

    Variant B1: Gradient descent with Fourier constraint projection.
    Variant B2: Power spectrum shaping.
    Variant B3: Projected gradient descent (long run).
    """
    print("\n" + "=" * 70)
    print("APPROACH B: Iterative Projection (POCS)")
    print("=" * 70)

    best_h = None
    best_score = float("inf")
    t0 = time.time()

    # --- B1: Gradient descent with projection ---
    print("\n  --- B1: Gradient descent + Fourier projection ---")

    for seed in range(6):
        if time.time() - t0 > time_limit * 0.25:
            break

        rng = np.random.default_rng(seed)

        if warm_h is not None and seed == 0:
            h = warm_h.copy()
        else:
            K = 20 + seed * 15
            coeffs = rng.standard_normal(K) * 0.15 / np.sqrt(np.arange(1, K + 1))
            h = fourier_to_h(coeffs, n)

        score = fast_eval(h)
        print(f"    seed {seed}: init C = {score:.13f}")

        lr = 5e-4
        for iteration in range(5000):
            if time.time() - t0 > time_limit * 0.25:
                break

            # Gradient step
            grad = gradient_wrt_max_lag(h)
            grad -= grad.mean()  # preserve sum
            h -= lr * grad
            h = normalize(h)

            # Every 100 steps, project Fourier constraint:
            # force even Fourier coefficients of overlap to be nonpositive
            if (iteration + 1) % 100 == 0:
                corr = correlation_profile(h)
                nc = len(corr)
                C_hat = np.fft.fft(corr)
                # Project: zero out positive real parts of even indices
                for k in range(0, nc, 2):
                    if C_hat[k].real > 0:
                        C_hat[k] = C_hat[k].imag * 1j
                corr_proj = np.fft.ifft(C_hat).real
                # Use projected correlation to guide h update
                # (reduce h where projected overlap increased, etc.)
                diff = corr_proj - corr
                if np.abs(diff).max() > 1e-10:
                    # Apply a small correction based on the projection residual
                    max_proj_idx = np.argmax(corr_proj)
                    lag = max_proj_idx - (n - 1)
                    correction = np.zeros(n)
                    for j in range(n):
                        j_plus = j + lag
                        if 0 <= j_plus < n:
                            correction[j] += diff[max_proj_idx] * 0.001
                    correction -= correction.mean()
                    h -= correction
                    h = normalize(h)

            # Adaptive learning rate
            if (iteration + 1) % 1000 == 0:
                lr *= 0.8

        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()
        print(f"    seed {seed} final: C = {score:.13f} (best: {best_score:.13f})")

    # --- B2: Power spectrum shaping with gradient ---
    print("\n  --- B2: Power spectrum shaping ---")

    for seed in range(8):
        if time.time() - t0 > time_limit * 0.5:
            break

        rng = np.random.default_rng(seed + 200)

        if warm_h is not None and seed == 0:
            h = warm_h.copy()
        elif best_h is not None and seed == 1:
            h = best_h.copy()
        else:
            K = 30 + seed * 20
            coeffs = rng.standard_normal(min(K, 200)) * 0.12 / np.sqrt(
                np.arange(1, min(K, 200) + 1))
            h = fourier_to_h(coeffs, n)

        for iteration in range(1000):
            if time.time() - t0 > time_limit * 0.5:
                break

            # Compute power spectrum
            H = np.fft.rfft(h)
            power = np.abs(H) ** 2
            phases = np.angle(H)

            # Flatten the power spectrum to make autocorrelation more uniform
            mean_power = np.mean(power[1:])
            alpha = 0.05 / (1 + iteration * 0.01)
            power_new = power.copy()
            power_new[1:] = (1 - alpha) * power[1:] + alpha * mean_power

            H_new = np.sqrt(np.maximum(power_new, 0)) * np.exp(1j * phases)
            h_new = np.fft.irfft(H_new, n=n)
            h_new = normalize(h_new)

            # Accept if improved
            if fast_eval(h_new) < fast_eval(h):
                h = h_new

        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()

        if (seed + 1) % 2 == 0:
            print(f"    seed {seed}: C = {score:.13f} (best: {best_score:.13f})")

    # --- B3: Long projected gradient descent ---
    print("\n  --- B3: Long projected gradient descent ---")

    if best_h is not None:
        h = best_h.copy()
    elif warm_h is not None:
        h = warm_h.copy()
    else:
        h = normalize(np.random.default_rng(42).random(n))

    print(f"    Starting from C = {fast_eval(h):.13f}")

    lr = 2e-4
    stale_count = 0
    prev_score = fast_eval(h)

    for iteration in range(20000):
        if time.time() - t0 > time_limit:
            break

        grad = gradient_wrt_max_lag(h)
        grad -= grad.mean()
        h -= lr * grad
        h = normalize(h)

        if (iteration + 1) % 1000 == 0:
            score = fast_eval(h)
            improved = score < prev_score - 1e-14
            if improved:
                stale_count = 0
                if score < best_score:
                    best_score = score
                    best_h = h.copy()
            else:
                stale_count += 1
                if stale_count > 3:
                    lr *= 0.5
                    stale_count = 0

            prev_score = score
            print(f"    iter {iteration+1}: C = {score:.13f} lr={lr:.2e} "
                  f"(best: {best_score:.13f})")

    elapsed = time.time() - t0
    print(f"\n  Approach B complete: best C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Approach C: CVXPY formulation
# ---------------------------------------------------------------------------


def approach_c(n_values: list[int] | None = None,
               time_limit: float = 900.0
               ) -> tuple[np.ndarray | None, float]:
    """Approach C: CVXPY-based optimization.

    C1: Autocorrelation LP relaxation — finds a lower bound and
        constructs h via spectral factorization.
    C2: Direct QCQP at small n — linearize around current best,
        solve LP subproblem, iterate (convex-concave procedure).
    C3: SDP at small n with tighter constraints.
    """
    if n_values is None:
        n_values = [20, 40, 60, 80, 100]

    print("\n" + "=" * 70)
    print("APPROACH C: CVXPY Formulations")
    print("=" * 70)

    try:
        import cvxpy as cp
    except ImportError:
        print("  cvxpy not available, skipping Approach C")
        return None, float("inf")

    best_h = None
    best_score = float("inf")
    t0 = time.time()

    # --- C1: Autocorrelation LP relaxation ---
    print("\n  --- C1: Autocorrelation LP relaxation ---")

    for n_lp in [50, 100, 200, 300]:
        if time.time() - t0 > time_limit * 0.3:
            break

        print(f"\n    LP at n={n_lp}...")
        t_start = time.time()

        try:
            r = cp.Variable(n_lp)
            alpha = cp.Variable()

            constraints = []

            # r(k) >= alpha for all k (maximize min autocorrelation)
            for k in range(n_lp):
                constraints.append(r[k] >= alpha)

            # Toeplitz PSD via DFT: power spectrum >= 0
            # For real symmetric r: spectrum[m] = r[0] + 2*sum r[k]*cos(2pi*k*m/n)
            for m in range(n_lp):
                cos_vals = np.zeros(n_lp)
                cos_vals[0] = 1.0
                for k in range(1, n_lp):
                    cos_vals[k] = 2.0 * np.cos(2.0 * np.pi * k * m / n_lp)
                constraints.append(cos_vals @ r >= 0)

            # r(0) = sum(h^2), which is in [n/4, n/2] for h in [0,1] with sum=n/2
            constraints.append(r[0] >= n_lp / 4.0)
            constraints.append(r[0] <= n_lp / 2.0)

            # r(k) >= 0 and r(k) <= r(0)
            for k in range(n_lp):
                constraints.append(r[k] >= 0)
                constraints.append(r[k] <= r[0])

            # sum of autocorrelation at all lags = (sum h)^2 = n^2/4
            # Actually sum_{k=-(n-1)}^{n-1} r(|k|) = (sum h)^2
            # = r(0) + 2*sum_{k=1}^{n-1} r(k) = n^2/4
            sum_r_all = r[0] + 2 * cp.sum(r[1:])
            constraints.append(sum_r_all == n_lp ** 2 / 4.0)

            prob = cp.Problem(cp.Maximize(alpha), constraints)
            prob.solve(solver=cp.SCS, max_iters=20000, verbose=False,
                       eps_abs=1e-9, eps_rel=1e-9)

            if prob.status in ["optimal", "optimal_inaccurate"]:
                alpha_val = alpha.value
                r_val = r.value
                C_bound = 1.0 - 2.0 * alpha_val / n_lp
                print(f"    LP bound: C >= {C_bound:.10f}")

                # Construct h via spectral factorization
                # Build full autocorrelation (symmetric)
                r_full = np.concatenate([r_val, r_val[-2:0:-1]])
                power = np.fft.fft(r_full).real
                power = np.maximum(power, 0)

                # Try many random phases (Griffin-Lim style)
                rng = np.random.default_rng(42)
                for trial in range(50):
                    phases = rng.uniform(-np.pi, np.pi, len(power))
                    phases[0] = 0
                    if len(power) % 2 == 0:
                        phases[len(power) // 2] = 0
                    H = np.sqrt(power) * np.exp(1j * phases)
                    h_recon = np.fft.ifft(H).real[:n_lp]
                    h_recon = normalize(h_recon)
                    score_small = fast_eval(h_recon)

                    # Upsample to 600
                    h_up = np.interp(
                        np.linspace(0, 1, 600),
                        np.linspace(0, 1, n_lp),
                        h_recon,
                    )
                    h_up = normalize(h_up)
                    score_up = fast_eval(h_up)

                    if score_up < best_score:
                        best_score = score_up
                        best_h = h_up.copy()
                        if trial < 10 or score_up < best_score + 0.001:
                            print(f"    trial {trial}: small={score_small:.10f} "
                                  f"up={score_up:.10f} ***")

            else:
                print(f"    LP status: {prob.status}")

        except Exception as e:
            print(f"    LP error at n={n_lp}: {e}")

        print(f"    Time: {time.time() - t_start:.1f}s")

    # --- C2: Convex-concave procedure at small n ---
    print("\n  --- C2: Convex-concave procedure ---")

    for n_cc in [30, 50, 80]:
        if time.time() - t0 > time_limit * 0.65:
            break

        print(f"\n    CCP at n={n_cc}...")
        t_start = time.time()

        try:
            # Start with best available init for this n
            if best_h is not None and len(best_h) != n_cc:
                h_init = np.interp(
                    np.linspace(0, 1, n_cc),
                    np.linspace(0, 1, len(best_h)),
                    best_h,
                )
            else:
                h_init = np.full(n_cc, 0.5)
            h_init = normalize(h_init)

            h_current = h_init.copy()

            for ccp_iter in range(20):
                if time.time() - t0 > time_limit * 0.65:
                    break

                # Linearize quadratic terms around h_current:
                # h[i]*h[j] ~ h_current[i]*h[j] + h[i]*h_current[j] - h_current[i]*h_current[j]

                h_var = cp.Variable(n_cc, nonneg=True)
                t_var = cp.Variable()

                constraints = [
                    h_var <= 1,
                    cp.sum(h_var) == n_cc / 2.0,
                ]

                # For each lag k, overlap = sum_i h[i](1 - h[i+k]) * 2/n
                # = (sum_valid h[i] - sum_valid h[i]*h[i+k]) * 2/n
                # Linearize h[i]*h[i+k]:
                #   ~ h_current[i]*h_var[i+k] + h_var[i]*h_current[i+k] - h_current[i]*h_current[i+k]
                for k in range(n_cc):
                    valid = n_cc - k if k > 0 else n_cc
                    h_sum = cp.sum(h_var[:n_cc - k]) if k > 0 else cp.sum(h_var)

                    quad_approx = 0
                    for i in range(n_cc - k):
                        j = i + k
                        quad_approx += (
                            h_current[i] * h_var[j]
                            + h_var[i] * h_current[j]
                            - h_current[i] * h_current[j]
                        )

                    overlap_k = (h_sum - quad_approx) * 2.0 / n_cc
                    constraints.append(overlap_k <= t_var)

                # Negative lags
                for k in range(1, n_cc):
                    h_sum = cp.sum(h_var[k:])
                    quad_approx = 0
                    for i in range(n_cc - k):
                        j = i + k
                        quad_approx += (
                            h_current[j] * h_var[i]
                            + h_var[j] * h_current[i]
                            - h_current[j] * h_current[i]
                        )
                    overlap_k = (h_sum - quad_approx) * 2.0 / n_cc
                    constraints.append(overlap_k <= t_var)

                prob = cp.Problem(cp.Minimize(t_var), constraints)
                prob.solve(solver=cp.SCS, max_iters=10000, verbose=False)

                if prob.status in ["optimal", "optimal_inaccurate"]:
                    h_new = normalize(np.clip(h_var.value, 0, 1))
                    score_new = fast_eval(h_new)

                    # Damped update
                    alpha = 0.5
                    h_current = alpha * h_new + (1 - alpha) * h_current
                    h_current = normalize(h_current)

                    if (ccp_iter + 1) % 5 == 0:
                        print(f"    CCP iter {ccp_iter+1}: "
                              f"C={score_new:.10f} bound={t_var.value:.10f}")
                else:
                    print(f"    CCP iter {ccp_iter+1}: {prob.status}")
                    break

            # Final score
            score_cc = fast_eval(h_current)
            print(f"    CCP n={n_cc} final: C = {score_cc:.10f}")

            # Upsample
            h_up = np.interp(
                np.linspace(0, 1, 600),
                np.linspace(0, 1, n_cc),
                h_current,
            )
            h_up = normalize(h_up)
            score_up = fast_eval(h_up)
            print(f"    Upsampled to 600: C = {score_up:.10f}")

            if score_up < best_score:
                best_score = score_up
                best_h = h_up.copy()
                print(f"    >>> NEW BEST: C = {best_score:.13f}")

        except Exception as e:
            print(f"    CCP error at n={n_cc}: {e}")

        print(f"    Time: {time.time() - t_start:.1f}s")

    # --- C3: SDP with tighter constraints at small n ---
    print("\n  --- C3: SDP with rank-1 encouragement ---")

    for n_sdp in [20, 30, 50]:
        if time.time() - t0 > time_limit:
            break

        print(f"\n    SDP at n={n_sdp}...")
        t_start = time.time()

        try:
            h_var = cp.Variable(n_sdp, nonneg=True)
            X = cp.Variable((n_sdp, n_sdp), symmetric=True)
            t_var = cp.Variable()

            constraints = [
                X >> 0,
                h_var <= 1,
                cp.sum(h_var) == n_sdp / 2.0,
                X >= 0,
            ]

            # Schur complement: [[X, h], [h^T, 1]] >> 0
            Y = cp.bmat([
                [X, cp.reshape(h_var, (n_sdp, 1), order='C')],
                [cp.reshape(h_var, (1, n_sdp), order='C'), np.ones((1, 1))]
            ])
            constraints.append(Y >> 0)

            # X[i,i] <= h[i]
            for i in range(n_sdp):
                constraints.append(X[i, i] <= h_var[i])

            # Tighter: X[i,i] >= 2*h[i] - 1 (from h^2 >= 2h-1 for h in [0,1])
            # Actually h^2 >= 2h-1 only when h >= 1 (not useful). Instead:
            # X[i,i] >= 0 (already by X >= 0)

            # Trace constraint: tr(X) = sum(h^2) >= n/4 (Cauchy-Schwarz)
            constraints.append(cp.trace(X) >= n_sdp / 4.0)

            # Nuclear norm regularization to encourage rank-1:
            # Minimize t + lambda * (trace(X) - ||h||^2_approx)
            # But this makes it non-convex. Use trace penalty instead.

            # Overlap constraints
            for k in range(n_sdp):
                h_sum = cp.sum(h_var[:n_sdp - k]) if k > 0 else cp.sum(h_var)
                x_sum = cp.sum([X[i, i + k] for i in range(n_sdp - k)])
                constraints.append((h_sum - x_sum) * 2.0 / n_sdp <= t_var)

            for k in range(1, n_sdp):
                h_sum = cp.sum(h_var[k:])
                x_sum = cp.sum([X[i + k, i] for i in range(n_sdp - k)])
                constraints.append((h_sum - x_sum) * 2.0 / n_sdp <= t_var)

            prob = cp.Problem(cp.Minimize(t_var), constraints)
            prob.solve(solver=cp.SCS, max_iters=20000, verbose=False,
                       eps_abs=1e-9, eps_rel=1e-9)

            if prob.status in ["optimal", "optimal_inaccurate"]:
                print(f"    SDP bound: {t_var.value:.10f}")

                h_val = normalize(np.clip(h_var.value, 0, 1))
                score_small = fast_eval(h_val)
                print(f"    Rounded at n={n_sdp}: C = {score_small:.10f}")

                # Upsample and refine
                h_up = np.interp(
                    np.linspace(0, 1, 600),
                    np.linspace(0, 1, n_sdp),
                    h_val,
                )
                h_up = normalize(h_up)

                # Refine upsampled solution with L-BFGS-B
                result = scipy_minimize(
                    direct_h_objective,
                    h_up,
                    args=(600, 100.0),
                    method="L-BFGS-B",
                    bounds=[(0, 1)] * 600,
                    options={"maxiter": 2000, "ftol": 1e-15},
                )
                h_refined = normalize(result.x)
                score_refined = fast_eval(h_refined)
                print(f"    Refined at 600: C = {score_refined:.10f}")

                if score_refined < best_score:
                    best_score = score_refined
                    best_h = h_refined.copy()
                    print(f"    >>> NEW BEST: C = {best_score:.13f}")
            else:
                print(f"    SDP status: {prob.status}")

        except Exception as e:
            print(f"    SDP error at n={n_sdp}: {e}")

        print(f"    Time: {time.time() - t_start:.1f}s")

    elapsed = time.time() - t0
    print(f"\n  Approach C complete: best C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Local polishing
# ---------------------------------------------------------------------------


def local_polish(h: np.ndarray, n_iters: int = 2_000_000,
                 time_limit: float = 300.0, seed: int = 0
                 ) -> tuple[np.ndarray, float]:
    """Polish a solution with random zero-sum perturbations."""
    print("\n" + "=" * 70)
    print("LOCAL POLISHING")
    print("=" * 70)

    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    best = fast_eval(h)
    best_h = h.copy()
    improved = 0
    t0 = time.time()

    print(f"  Starting C = {best:.13f}, n = {n}")

    for trial in range(n_iters):
        if time.time() - t0 > time_limit:
            break

        n_pts = rng.choice([2, 3, 4])
        idx = rng.choice(n, size=n_pts, replace=False)

        # Multi-scale delta
        if trial < n_iters // 4:
            scale = 1e-4
        elif trial < n_iters // 2:
            scale = 1e-5
        elif trial < 3 * n_iters // 4:
            scale = 1e-6
        else:
            scale = 1e-7

        delta = rng.standard_normal(n_pts) * scale
        delta -= delta.mean()

        old = h[idx].copy()
        new = old + delta
        if np.any(new < 0) or np.any(new > 1):
            continue

        h[idx] = new
        score = fast_eval(h)
        if score < best:
            best = score
            best_h = h.copy()
            improved += 1
        else:
            h[idx] = old

        if (trial + 1) % 500_000 == 0:
            elapsed = time.time() - t0
            print(f"    iter {trial+1}: C = {best:.13f}, "
                  f"improved = {improved}, time = {elapsed:.0f}s")

    elapsed = time.time() - t0
    print(f"  Polish done: C = {best:.13f}, improved = {improved} ({elapsed:.0f}s)")
    return best_h, best


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    print("=" * 70)
    print("FOURIER-CONSTRAINED OPTIMIZER: Erdős Minimum Overlap (Problem 1)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    n = 600
    global_best_h = None
    global_best_score = float("inf")
    t_global = time.time()

    # Check for existing warm-start solutions
    warm_h = None
    for candidate in sorted(RESULTS_DIR.glob("erdos_n*.json")):
        try:
            with open(candidate) as f:
                data = json.load(f)
            vals = np.array(data["values"], dtype=np.float64)
            score = fast_eval(vals)
            if score < global_best_score:
                global_best_score = score
                global_best_h = vals.copy()
                warm_h = vals.copy()
                print(f"  Loaded warm-start: {candidate.name}, C = {score:.13f}")
        except Exception:
            pass

    if warm_h is not None:
        print(f"  Warm-start best: C = {global_best_score:.13f}")
    else:
        print("  No warm-start found, starting from scratch.")

    results = {}

    # ===== Approach A: Fourier parametrization =====
    h_a, s_a = approach_a(n=n, K_values=[20, 50, 100, 200], time_limit=300)
    results["A_fourier_param"] = s_a
    if h_a is not None and s_a < global_best_score:
        global_best_score = s_a
        global_best_h = h_a.copy()
        print(f"\n  >>> New global best from Approach A: C = {s_a:.13f}")

    # ===== Approach A2: Direct L-BFGS-B =====
    h_a2, s_a2 = approach_a2_direct(
        n=n, time_limit=180, warm_h=global_best_h)
    results["A2_direct_lbfgsb"] = s_a2
    if h_a2 is not None and s_a2 < global_best_score:
        global_best_score = s_a2
        global_best_h = h_a2.copy()
        print(f"\n  >>> New global best from Approach A2: C = {s_a2:.13f}")

    # ===== Approach B: Iterative projection =====
    h_b, s_b = approach_b(n=n, time_limit=180, warm_h=global_best_h)
    results["B_iterative_proj"] = s_b
    if h_b is not None and s_b < global_best_score:
        global_best_score = s_b
        global_best_h = h_b.copy()
        print(f"\n  >>> New global best from Approach B: C = {s_b:.13f}")

    # ===== Approach C: CVXPY =====
    h_c, s_c = approach_c(n_values=[20, 40, 60, 80], time_limit=180)
    results["C_cvxpy"] = s_c
    if h_c is not None and s_c < global_best_score:
        global_best_score = s_c
        global_best_h = h_c.copy()
        print(f"\n  >>> New global best from Approach C: C = {s_c:.13f}")

    # ===== Local polishing on global best =====
    if global_best_h is not None:
        remaining = max(0, 1800 - (time.time() - t_global))
        if remaining > 30:
            h_pol, s_pol = local_polish(
                global_best_h, n_iters=5_000_000,
                time_limit=min(remaining, 300))
            results["polish"] = s_pol
            if s_pol < global_best_score:
                global_best_score = s_pol
                global_best_h = h_pol.copy()

    # ===== Final verification =====
    print("\n" + "=" * 70)
    print("FINAL VERIFICATION")
    print("=" * 70)

    if global_best_h is not None:
        exact_score = exact_evaluate({"values": global_best_h.tolist()})
        fast_score = fast_evaluate(global_best_h)
        print(f"  Fast eval:  C = {fast_score:.13f}")
        print(f"  Exact eval: C = {exact_score:.13f}")
        print(f"  Match: {abs(fast_score - exact_score) < 1e-10}")

        # Save to /tmp
        output = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(global_best_h),
            "score": float(exact_score),
            "values": global_best_h.tolist(),
            "source": "fourier_optimizer",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        with open(OUTPUT_PATH, "w") as f:
            json.dump(output, f)
        print(f"  Saved best to: {OUTPUT_PATH}")

        # Also save to results dir
        save_solution(global_best_h, exact_score, "fourier_best")

    # ===== Summary =====
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for name, score in sorted(results.items(), key=lambda x: x[1]):
        print(f"  {name:25s}: C = {score:.13f}")

    if global_best_h is not None:
        print(f"\n  GLOBAL BEST: C = {global_best_score:.13f}")
    else:
        print("\n  No valid solution found.")

    total_time = time.time() - t_global
    print(f"  Total time: {total_time:.0f}s ({total_time/60:.1f}min)")
    print("=" * 70)


if __name__ == "__main__":
    main()
