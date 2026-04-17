"""SOCP / White-constraint optimizer for Erdős Minimum Overlap (Problem 1).

Exploits White (2022) insight: the overlap function M(x) has all even cosine
Fourier coefficients nonpositive (A_{2m} <= 0). This constrains the feasible
region and should help optimization converge to better minima.

Approaches:
  1. Low-frequency cosine parameterization with various K
  2. Warm-start from SOTA solution via Fourier decomposition
  3. SLSQP with explicit White constraints
  4. Multi-scale annealing with aggressive local polishing

Usage (from project root):
    uv run python3 scripts/erdos/socp_white.py
"""

import json
import sys
import time
import warnings
from pathlib import Path

import numpy as np
from scipy.optimize import minimize as scipy_minimize
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.fast import fast_evaluate
from einstein.erdos.evaluator import compute_upper_bound

warnings.filterwarnings("ignore")

SOTA_PATH = Path(".mb/knowledge/problem-1-erdos-overlap/solutions/solution-best.json")
RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH = Path("/tmp/p1_socp_white_best.json")

SOTA_SCORE = 0.3808703105862199
TARGET_SCORE = 0.3808693  # need at least 1e-6 lower

N = 600  # discretization
TIME_LIMIT = 1500  # 25 minutes total (leave margin from 30)


# ---------------------------------------------------------------------------
# Core utilities
# ---------------------------------------------------------------------------

def normalize(h: np.ndarray) -> np.ndarray:
    """Project h onto [0,1] with sum = n/2."""
    h = np.clip(h, 0.0, 1.0)
    n = len(h)
    for _ in range(20):
        s = np.sum(h)
        if s == 0:
            h = np.full(n, 0.5)
            break
        h = h * (n / 2.0 / s)
        if np.all(h <= 1.0) and np.all(h >= 0.0):
            break
        h = np.clip(h, 0.0, 1.0)
    return h


def fast_eval(h: np.ndarray) -> float:
    """Compute C = max(correlate(h, 1-h, 'full')) * 2/n."""
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    if n == 0:
        return float("inf")
    h_c = np.clip(h, 0, 1)
    s = np.sum(h_c)
    if s == 0:
        return float("inf")
    h_c = h_c * (n / 2.0 / s)
    if np.any(h_c > 1.0):
        return float("inf")
    corr = fftconvolve(h_c, (1.0 - h_c)[::-1], mode="full")
    return float(np.max(corr)) / n * 2


def correlation_profile(h: np.ndarray) -> np.ndarray:
    """Return full correlation array correlate(h, 1-h, 'full')."""
    return fftconvolve(h, (1.0 - h)[::-1], mode="full")


def logsumexp_max(arr: np.ndarray, beta: float = 100.0) -> float:
    """Smooth approximation of max via LogSumExp."""
    m = np.max(arr)
    return m + np.log(np.sum(np.exp(beta * (arr - m)))) / beta


def compute_overlap_fourier_coeffs(h: np.ndarray) -> np.ndarray:
    """Compute the Fourier coefficients of the overlap function.

    The overlap function M(k) = correlate(h, 1-h) at each lag.
    Returns FFT of the full correlation profile.
    """
    corr = correlation_profile(h)
    return np.fft.rfft(corr)


def white_constraint_violation(h: np.ndarray) -> float:
    """Compute total violation of White constraint: A_{2m} <= 0.

    Returns sum of max(0, Re(A_{2m})) for even-indexed coefficients.
    """
    corr = correlation_profile(h)
    coeffs = np.fft.rfft(corr)
    # Even indices: 0, 2, 4, ...
    even_coeffs = coeffs[::2]
    violations = np.maximum(0, even_coeffs.real)
    return float(np.sum(violations))


def save_solution(h: np.ndarray, score: float, tag: str) -> None:
    """Save solution."""
    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": len(h),
        "score": float(score),
        "values": h.tolist(),
        "source": f"socp_white/{tag}",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"erdos_n{len(h)}_{score:.10f}_{tag}.json"
    with open(fname, "w") as f:
        json.dump(result, f)
    print(f"  Saved: {fname}")


def load_sota() -> np.ndarray:
    """Load the SOTA solution."""
    with open(SOTA_PATH) as f:
        data = json.load(f)
    return np.array(data["data"]["values"], dtype=np.float64)


# ---------------------------------------------------------------------------
# Approach 1: Cosine parameterization h(x) = clip(0.5 + sum a_k cos(...), 0, 1)
# ---------------------------------------------------------------------------

def cosine_to_h(coeffs: np.ndarray, n: int) -> np.ndarray:
    """Build h(x) = 0.5 + sum_{k=1}^{K} a_k * cos(2*pi*k*x/2) on [0,2).

    The period is 2, matching the domain [0, 2].
    cos(2*pi*k*x/2) = cos(pi*k*x).
    """
    K = len(coeffs)
    x = np.linspace(0, 2, n, endpoint=False)  # x in [0, 2)
    # Precompute all cosines as matrix multiply
    k_vals = np.arange(1, K + 1)
    # cos(pi * k * x) for each k and x
    cos_matrix = np.cos(np.pi * k_vals[np.newaxis, :] * x[:, np.newaxis])
    h = 0.5 + cos_matrix @ coeffs
    return normalize(h)


def cosine_objective(coeffs: np.ndarray, n: int, beta: float,
                     white_penalty: float = 0.0) -> float:
    """Objective: LogSumExp smooth max + optional White constraint penalty."""
    h = cosine_to_h(coeffs, n)
    corr = correlation_profile(h)
    obj = logsumexp_max(corr, beta=beta) / n * 2

    if white_penalty > 0:
        violation = white_constraint_violation(h)
        obj += white_penalty * violation

    return obj


def cosine_objective_with_white(coeffs: np.ndarray, n: int, beta: float) -> float:
    """Objective with built-in White constraint penalty (adaptive)."""
    h = cosine_to_h(coeffs, n)
    corr = correlation_profile(h)
    obj = logsumexp_max(corr, beta=beta) / n * 2

    # White constraint: even Fourier coefficients of overlap <= 0
    fft_corr = np.fft.rfft(corr)
    even_violations = np.maximum(0, fft_corr[::2].real)
    penalty = float(np.sum(even_violations ** 2))
    obj += 10.0 * penalty / (n ** 2)

    return obj


def approach_1_cosine_param(time_limit: float = 400.0) -> tuple[np.ndarray | None, float]:
    """Approach 1: Low-frequency cosine parameterization for various K."""
    print("\n" + "=" * 70)
    print("APPROACH 1: Cosine Parameterization h = 0.5 + sum a_k cos(pi*k*x)")
    print("=" * 70)

    best_h = None
    best_score = float("inf")
    best_coeffs = None
    t0 = time.time()

    K_values = [10, 20, 50, 100]

    for K in K_values:
        if time.time() - t0 > time_limit:
            break

        print(f"\n  --- K = {K} ---")
        trial_best = float("inf")
        trial_h = None
        trial_coeffs = None

        # Multiple initializations
        inits = []

        # Random inits with 1/k decay
        for seed in range(6):
            rng = np.random.default_rng(seed + K * 100)
            x0 = rng.standard_normal(K) * 0.2 / np.sqrt(np.arange(1, K + 1))
            inits.append((f"rand_s{seed}", x0))

        # Warm-start from previous K
        if best_coeffs is not None:
            prev_K = len(best_coeffs)
            x0_warm = np.zeros(K)
            x0_warm[:min(K, prev_K)] = best_coeffs[:min(K, prev_K)]
            inits.insert(0, ("warm_prev", x0_warm))

        # Beta annealing schedule: start smooth, end sharp
        beta_schedules = [
            [10, 30, 100, 300, 1000],
            [5, 20, 80, 200, 500],
        ]

        for name, x0 in inits:
            if time.time() - t0 > time_limit:
                break

            for schedule_idx, betas in enumerate(beta_schedules):
                if time.time() - t0 > time_limit:
                    break

                current_x = x0.copy()
                for beta in betas:
                    if time.time() - t0 > time_limit:
                        break

                    # Without White penalty
                    try:
                        result = scipy_minimize(
                            cosine_objective,
                            current_x,
                            args=(N, beta, 0.0),
                            method="L-BFGS-B",
                            options={"maxiter": 5000, "ftol": 1e-16, "gtol": 1e-13},
                        )
                        h = cosine_to_h(result.x, N)
                        score = fast_eval(h)
                        if score < trial_best:
                            trial_best = score
                            trial_h = h.copy()
                            trial_coeffs = result.x.copy()
                        current_x = result.x.copy()
                    except Exception:
                        pass

                    # With White penalty
                    try:
                        result = scipy_minimize(
                            cosine_objective_with_white,
                            current_x,
                            args=(N, beta),
                            method="L-BFGS-B",
                            options={"maxiter": 3000, "ftol": 1e-16, "gtol": 1e-13},
                        )
                        h = cosine_to_h(result.x, N)
                        score = fast_eval(h)
                        if score < trial_best:
                            trial_best = score
                            trial_h = h.copy()
                            trial_coeffs = result.x.copy()
                        current_x = result.x.copy()
                    except Exception:
                        pass

                if schedule_idx == 0:
                    # Only run first schedule for most inits to save time
                    break

            print(f"    {name}: C = {trial_best:.13f}")

        if trial_h is not None and trial_best < best_score:
            best_score = trial_best
            best_h = trial_h.copy()
            best_coeffs = trial_coeffs.copy() if trial_coeffs is not None else None
            print(f"  >>> K={K} NEW BEST: C = {best_score:.13f}")

    elapsed = time.time() - t0
    print(f"\n  Approach 1 complete: C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Approach 2: Warm-start from SOTA, optimize in Fourier space
# ---------------------------------------------------------------------------

def extract_fourier_coeffs(h: np.ndarray, K: int) -> np.ndarray:
    """Extract cosine Fourier coefficients from h by least-squares projection.

    h(x) ~ 0.5 + sum_{k=1}^K a_k cos(pi*k*x) on x in [0, 2).
    """
    n = len(h)
    x = np.linspace(0, 2, n, endpoint=False)
    k_vals = np.arange(1, K + 1)
    cos_matrix = np.cos(np.pi * k_vals[np.newaxis, :] * x[:, np.newaxis])
    # Solve: cos_matrix @ coeffs ~ h - 0.5
    residual = h - 0.5
    coeffs, _, _, _ = np.linalg.lstsq(cos_matrix, residual, rcond=None)
    return coeffs


def approach_2_warmstart(time_limit: float = 400.0) -> tuple[np.ndarray | None, float]:
    """Approach 2: Warm-start from SOTA, optimize in Fourier space."""
    print("\n" + "=" * 70)
    print("APPROACH 2: Warm-start from SOTA in Fourier space")
    print("=" * 70)

    sota_h = load_sota()
    sota_score = fast_eval(sota_h)
    print(f"  SOTA score: {sota_score:.13f}")

    best_h = sota_h.copy()
    best_score = sota_score
    t0 = time.time()

    # Extract Fourier coefficients at various truncation levels
    K_values = [10, 20, 50, 100, 150, 200, 300]

    for K in K_values:
        if time.time() - t0 > time_limit:
            break

        print(f"\n  --- K = {K} Fourier warm-start ---")

        # Extract coefficients from SOTA
        coeffs = extract_fourier_coeffs(sota_h, K)
        h_recon = cosine_to_h(coeffs, N)
        recon_score = fast_eval(h_recon)
        print(f"    Reconstructed: C = {recon_score:.13f}")

        # Now optimize from these coefficients
        current_x = coeffs.copy()

        # Try different beta schedules
        for beta in [30, 100, 300, 1000, 3000]:
            if time.time() - t0 > time_limit:
                break

            # Plain objective
            try:
                result = scipy_minimize(
                    cosine_objective,
                    current_x,
                    args=(N, beta, 0.0),
                    method="L-BFGS-B",
                    options={"maxiter": 8000, "ftol": 1e-16, "gtol": 1e-14},
                )
                h = cosine_to_h(result.x, N)
                score = fast_eval(h)
                if score < best_score:
                    best_score = score
                    best_h = h.copy()
                    print(f"    beta={beta}: C = {score:.13f} *** NEW BEST")
                current_x = result.x.copy()
            except Exception as e:
                print(f"    beta={beta}: error {e}")

            # With White penalty
            try:
                result = scipy_minimize(
                    cosine_objective_with_white,
                    current_x,
                    args=(N, beta),
                    method="L-BFGS-B",
                    options={"maxiter": 5000, "ftol": 1e-16, "gtol": 1e-14},
                )
                h = cosine_to_h(result.x, N)
                score = fast_eval(h)
                if score < best_score:
                    best_score = score
                    best_h = h.copy()
                    print(f"    beta={beta}+White: C = {score:.13f} *** NEW BEST")
                current_x = result.x.copy()
            except Exception:
                pass

        print(f"    K={K} best: C = {best_score:.13f}")

    # Also try SLSQP with explicit White constraints at moderate K
    print("\n  --- SLSQP with explicit White constraints ---")
    for K in [20, 50, 100]:
        if time.time() - t0 > time_limit:
            break

        coeffs = extract_fourier_coeffs(best_h, K)

        def white_constraints(c, n=N):
            """Return array of -A_{2m} (must be >= 0 for feasibility)."""
            h = cosine_to_h(c, n)
            corr = correlation_profile(h)
            fft_c = np.fft.rfft(corr)
            # Even indices: A_{2m} <= 0, i.e., -A_{2m} >= 0
            return -fft_c[::2].real

        for beta in [100, 500, 2000]:
            if time.time() - t0 > time_limit:
                break

            try:
                result = scipy_minimize(
                    cosine_objective,
                    coeffs,
                    args=(N, beta, 0.0),
                    method="SLSQP",
                    constraints={"type": "ineq", "fun": white_constraints},
                    options={"maxiter": 3000, "ftol": 1e-16},
                )
                h = cosine_to_h(result.x, N)
                score = fast_eval(h)
                if score < best_score:
                    best_score = score
                    best_h = h.copy()
                    print(f"    SLSQP K={K} beta={beta}: C = {score:.13f} *** NEW BEST")
                coeffs = result.x.copy()
            except Exception as e:
                print(f"    SLSQP K={K} beta={beta}: {e}")

    elapsed = time.time() - t0
    print(f"\n  Approach 2 complete: C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Approach 3: Direct optimization on h values with White-projected gradient
# ---------------------------------------------------------------------------

def gradient_wrt_max_lag(h: np.ndarray) -> np.ndarray:
    """Compute gradient of max overlap C w.r.t. h at the argmax lag."""
    n = len(h)
    corr = correlation_profile(h)
    max_idx = np.argmax(corr)
    lag = max_idx - (n - 1)

    grad = np.zeros(n)
    for j in range(n):
        j_minus_lag = j - lag
        j_plus_lag = j + lag
        if 0 <= j_minus_lag < n:
            grad[j] += (1.0 - h[j_minus_lag])
        if 0 <= j_plus_lag < n:
            grad[j] -= h[j_plus_lag]
    return grad * 2.0 / n


def project_white(h: np.ndarray, strength: float = 0.1) -> np.ndarray:
    """Project h to better satisfy White constraint by modifying overlap spectrum.

    Damp positive even Fourier coefficients of the overlap function,
    then reconstruct h via an approximate inverse.
    """
    n = len(h)
    corr = correlation_profile(h)
    nc = len(corr)
    C_hat = np.fft.fft(corr)

    # Dampen positive real parts of even-indexed coefficients
    modified = False
    for k in range(0, nc, 2):
        if C_hat[k].real > 0:
            C_hat[k] = (1 - strength) * C_hat[k].real * 1 + C_hat[k].imag * 1j
            if C_hat[k].real > 0:
                C_hat[k] = C_hat[k].imag * 1j
            modified = True

    if not modified:
        return h

    corr_new = np.fft.ifft(C_hat).real

    # The overlap is correlate(h, 1-h). Changing the overlap doesn't directly
    # give us h back. Instead, use the spectral modification as a hint:
    # apply a small correction to h based on the change in the argmax lag.
    max_old = np.argmax(corr)
    max_new = np.argmax(corr_new)
    diff = corr_new[max_old] - corr[max_old]

    if abs(diff) < 1e-15:
        return h

    # Scale correction
    lag = max_old - (n - 1)
    correction = np.zeros(n)
    for j in range(n):
        j_plus_lag = j + lag
        if 0 <= j_plus_lag < n:
            correction[j] = diff * 0.01

    correction -= correction.mean()
    h_new = h - correction
    return normalize(h_new)


def approach_3_direct_white(time_limit: float = 400.0,
                            warm_h: np.ndarray | None = None
                            ) -> tuple[np.ndarray | None, float]:
    """Approach 3: Direct gradient descent with White constraint projection."""
    print("\n" + "=" * 70)
    print("APPROACH 3: Direct gradient + White projection")
    print("=" * 70)

    best_h = None
    best_score = float("inf")
    t0 = time.time()

    # Initialize from SOTA or warm start
    if warm_h is not None:
        h_init = warm_h.copy()
    else:
        h_init = load_sota()

    init_score = fast_eval(h_init)
    print(f"  Starting score: {init_score:.13f}")

    # Run multiple configurations
    configs = [
        {"lr": 5e-4, "project_every": 50, "name": "fast_lr"},
        {"lr": 1e-4, "project_every": 100, "name": "slow_lr"},
        {"lr": 2e-4, "project_every": 20, "name": "freq_proj"},
        {"lr": 1e-3, "project_every": 200, "name": "aggr_lr"},
    ]

    for cfg in configs:
        if time.time() - t0 > time_limit:
            break

        h = h_init.copy()
        lr = cfg["lr"]
        proj_every = cfg["project_every"]
        name = cfg["name"]
        stale = 0
        prev = fast_eval(h)

        print(f"\n  --- Config: {name} (lr={lr}, proj_every={proj_every}) ---")

        for it in range(30000):
            if time.time() - t0 > time_limit:
                break

            # Gradient step
            grad = gradient_wrt_max_lag(h)
            grad -= grad.mean()
            h -= lr * grad
            h = normalize(h)

            # White projection
            if (it + 1) % proj_every == 0:
                h = project_white(h, strength=0.2)

            # Evaluation and adaptive LR
            if (it + 1) % 2000 == 0:
                score = fast_eval(h)
                if score < prev - 1e-14:
                    stale = 0
                    if score < best_score:
                        best_score = score
                        best_h = h.copy()
                else:
                    stale += 1
                    if stale > 3:
                        lr *= 0.5
                        stale = 0
                prev = score

                if (it + 1) % 10000 == 0:
                    wv = white_constraint_violation(h)
                    print(f"    iter {it+1}: C={score:.13f} lr={lr:.2e} "
                          f"white_viol={wv:.6f} best={best_score:.13f}")

        final = fast_eval(h)
        if final < best_score:
            best_score = final
            best_h = h.copy()
        print(f"    {name} final: C={final:.13f} (best={best_score:.13f})")

    elapsed = time.time() - t0
    print(f"\n  Approach 3 complete: C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Approach 4: Multi-scale + aggressive local polishing
# ---------------------------------------------------------------------------

def approach_4_multiscale(time_limit: float = 300.0,
                          warm_h: np.ndarray | None = None
                          ) -> tuple[np.ndarray | None, float]:
    """Approach 4: Multi-resolution + local polishing."""
    print("\n" + "=" * 70)
    print("APPROACH 4: Multi-resolution + local polishing")
    print("=" * 70)

    best_h = None
    best_score = float("inf")
    t0 = time.time()

    # Start at low resolution, optimize, upsample, refine
    if warm_h is not None:
        base_h = warm_h.copy()
        best_score = fast_eval(base_h)
        best_h = base_h.copy()
        print(f"  Warm-start: C = {best_score:.13f}")

    resolutions = [100, 200, 400, 600]

    for n_res in resolutions:
        if time.time() - t0 > time_limit * 0.5:
            break

        print(f"\n  --- Resolution n = {n_res} ---")

        if best_h is not None:
            # Downsample/upsample
            h0 = np.interp(
                np.linspace(0, 1, n_res),
                np.linspace(0, 1, len(best_h)),
                best_h,
            )
            h0 = normalize(h0)
        else:
            rng = np.random.default_rng(42)
            K = min(50, n_res // 2)
            coeffs = rng.standard_normal(K) * 0.15 / np.sqrt(np.arange(1, K + 1))
            h0 = cosine_to_h(coeffs, n_res)

        # Optimize at this resolution
        def obj_res(h_flat, beta=200):
            h = normalize(h_flat.copy())
            corr = correlation_profile(h)
            return logsumexp_max(corr, beta=beta) / n_res * 2

        current = h0.copy()
        for beta in [30, 100, 300, 1000]:
            if time.time() - t0 > time_limit * 0.5:
                break
            try:
                result = scipy_minimize(
                    obj_res,
                    current,
                    args=(beta,),
                    method="L-BFGS-B",
                    bounds=[(0, 1)] * n_res,
                    options={"maxiter": 3000, "ftol": 1e-16, "gtol": 1e-13},
                )
                current = normalize(result.x)
            except Exception:
                pass

        score_res = fast_eval(current)
        print(f"    Optimized at n={n_res}: C = {score_res:.13f}")

        # Upsample to 600
        if n_res < N:
            h_up = np.interp(
                np.linspace(0, 1, N),
                np.linspace(0, 1, n_res),
                current,
            )
            h_up = normalize(h_up)
        else:
            h_up = current

        score_up = fast_eval(h_up)
        if score_up < best_score:
            best_score = score_up
            best_h = h_up.copy()
            print(f"    Upsampled: C = {score_up:.13f} *** NEW BEST")

    # Aggressive local polishing on the best solution
    if best_h is not None:
        remaining = max(0, time_limit - (time.time() - t0))
        if remaining > 30:
            print(f"\n  --- Local polishing ({remaining:.0f}s remaining) ---")
            h = best_h.copy()
            rng = np.random.default_rng(0)
            improved = 0
            polish_t0 = time.time()
            n = len(h)
            current_best = fast_eval(h)

            # Phase 1: larger perturbations
            for trial in range(3_000_000):
                elapsed = time.time() - polish_t0
                if elapsed > remaining:
                    break

                # Adaptive scale
                if trial < 500_000:
                    scale = 5e-4
                    n_pts = rng.choice([2, 3, 4, 5])
                elif trial < 1_500_000:
                    scale = 5e-5
                    n_pts = rng.choice([2, 3, 4])
                else:
                    scale = 5e-6
                    n_pts = rng.choice([2, 3])

                idx = rng.choice(n, size=n_pts, replace=False)
                delta = rng.standard_normal(n_pts) * scale
                delta -= delta.mean()

                old = h[idx].copy()
                new = old + delta
                if np.any(new < 0) or np.any(new > 1):
                    continue

                h[idx] = new
                score = fast_eval(h)
                if score < current_best:
                    current_best = score
                    improved += 1
                    if current_best < best_score:
                        best_score = current_best
                        best_h = h.copy()
                else:
                    h[idx] = old

                if (trial + 1) % 500_000 == 0:
                    print(f"    polish iter {trial+1}: C = {current_best:.13f} "
                          f"improved={improved}")

            print(f"  Polish done: C = {current_best:.13f}, improved={improved}")

    elapsed = time.time() - t0
    print(f"\n  Approach 4 complete: C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Approach 5: Hybrid — Fourier warm-start + SLSQP + direct polishing
# ---------------------------------------------------------------------------

def approach_5_hybrid(time_limit: float = 300.0,
                      warm_h: np.ndarray | None = None
                      ) -> tuple[np.ndarray | None, float]:
    """Approach 5: Combine Fourier parameterization with direct optimization.

    1. Start from best Fourier parameterization
    2. Switch to direct h-space L-BFGS-B
    3. Polish with random perturbations
    """
    print("\n" + "=" * 70)
    print("APPROACH 5: Hybrid Fourier + Direct + Polish")
    print("=" * 70)

    if warm_h is None:
        warm_h = load_sota()

    best_h = warm_h.copy()
    best_score = fast_eval(warm_h)
    t0 = time.time()
    print(f"  Starting: C = {best_score:.13f}")

    # Step 1: Fourier refinement at multiple K
    print("\n  Step 1: Fourier refinement...")
    for K in [50, 100, 150, 200, 300]:
        if time.time() - t0 > time_limit * 0.3:
            break

        coeffs = extract_fourier_coeffs(best_h, K)
        h_test = cosine_to_h(coeffs, N)
        recon_score = fast_eval(h_test)

        for beta in [200, 1000, 5000]:
            if time.time() - t0 > time_limit * 0.3:
                break

            try:
                result = scipy_minimize(
                    cosine_objective,
                    coeffs,
                    args=(N, beta, 0.0),
                    method="L-BFGS-B",
                    options={"maxiter": 8000, "ftol": 1e-16, "gtol": 1e-14},
                )
                h = cosine_to_h(result.x, N)
                score = fast_eval(h)
                if score < best_score:
                    best_score = score
                    best_h = h.copy()
                    print(f"    K={K} beta={beta}: C = {score:.13f} ***")
                coeffs = result.x.copy()
            except Exception:
                pass

    # Step 2: Direct L-BFGS-B on h values
    print(f"\n  Step 2: Direct L-BFGS-B (from C = {best_score:.13f})...")

    def direct_obj(h_flat, beta):
        h = normalize(h_flat.copy())
        corr = correlation_profile(h)
        return logsumexp_max(corr, beta=beta) / N * 2

    current = best_h.copy()
    for beta in [50, 200, 1000, 5000]:
        if time.time() - t0 > time_limit * 0.6:
            break

        try:
            result = scipy_minimize(
                direct_obj,
                current,
                args=(beta,),
                method="L-BFGS-B",
                bounds=[(0, 1)] * N,
                options={"maxiter": 5000, "ftol": 1e-16, "gtol": 1e-14},
            )
            h = normalize(result.x)
            score = fast_eval(h)
            if score < best_score:
                best_score = score
                best_h = h.copy()
                print(f"    Direct beta={beta}: C = {score:.13f} ***")
            current = result.x.copy()
        except Exception:
            pass

    # Step 3: Polish
    remaining = max(0, time_limit - (time.time() - t0))
    if remaining > 20 and best_h is not None:
        print(f"\n  Step 3: Polish ({remaining:.0f}s)...")
        h = best_h.copy()
        rng = np.random.default_rng(42)
        n = len(h)
        current_best = best_score
        improved = 0

        for trial in range(5_000_000):
            if time.time() - t0 > time_limit:
                break

            scale = max(1e-7, 1e-4 * (0.999 ** (trial // 1000)))
            n_pts = rng.choice([2, 3, 4])
            idx = rng.choice(n, size=n_pts, replace=False)
            delta = rng.standard_normal(n_pts) * scale
            delta -= delta.mean()

            old = h[idx].copy()
            new = old + delta
            if np.any(new < 0) or np.any(new > 1):
                continue

            h[idx] = new
            score = fast_eval(h)
            if score < current_best:
                current_best = score
                improved += 1
                if current_best < best_score:
                    best_score = current_best
                    best_h = h.copy()
            else:
                h[idx] = old

            if (trial + 1) % 1_000_000 == 0:
                print(f"    polish {trial+1}: C = {current_best:.13f} imp={improved}")

        print(f"  Polish: C = {current_best:.13f}, improved={improved}")

    elapsed = time.time() - t0
    print(f"\n  Approach 5 complete: C = {best_score:.13f} ({elapsed:.0f}s)")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("SOCP / WHITE-CONSTRAINT OPTIMIZER: Erdős Minimum Overlap")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"SOTA score: {SOTA_SCORE}")
    print(f"Target:     {TARGET_SCORE} (need 1e-6 improvement)")
    print("=" * 70)

    t_global = time.time()
    global_best_h = None
    global_best_score = float("inf")

    # Load SOTA as baseline
    sota_h = load_sota()
    sota_score = fast_eval(sota_h)
    print(f"\nSOTA verification: C = {sota_score:.13f}")
    global_best_h = sota_h.copy()
    global_best_score = sota_score

    # Also check for any existing results
    for candidate in sorted(RESULTS_DIR.glob("erdos_n*.json")):
        try:
            with open(candidate) as f:
                data = json.load(f)
            vals = np.array(data["values"], dtype=np.float64)
            score = fast_eval(vals)
            if score < global_best_score:
                global_best_score = score
                global_best_h = vals.copy()
                print(f"  Found better: {candidate.name}, C = {score:.13f}")
        except Exception:
            pass

    results = {}

    # ===== Approach 1: Cosine parameterization =====
    remaining = max(0, TIME_LIMIT - (time.time() - t_global))
    h1, s1 = approach_1_cosine_param(time_limit=min(remaining * 0.25, 400))
    results["1_cosine_param"] = s1
    if h1 is not None and s1 < global_best_score:
        global_best_score = s1
        global_best_h = h1.copy()
        print(f"\n>>> Global best from Approach 1: C = {s1:.13f}")

    # ===== Approach 2: Warm-start from SOTA =====
    remaining = max(0, TIME_LIMIT - (time.time() - t_global))
    h2, s2 = approach_2_warmstart(time_limit=min(remaining * 0.3, 400))
    results["2_warmstart_fourier"] = s2
    if h2 is not None and s2 < global_best_score:
        global_best_score = s2
        global_best_h = h2.copy()
        print(f"\n>>> Global best from Approach 2: C = {s2:.13f}")

    # ===== Approach 3: Direct + White projection =====
    remaining = max(0, TIME_LIMIT - (time.time() - t_global))
    h3, s3 = approach_3_direct_white(time_limit=min(remaining * 0.35, 400),
                                      warm_h=global_best_h)
    results["3_direct_white"] = s3
    if h3 is not None and s3 < global_best_score:
        global_best_score = s3
        global_best_h = h3.copy()
        print(f"\n>>> Global best from Approach 3: C = {s3:.13f}")

    # ===== Approach 5: Hybrid =====
    remaining = max(0, TIME_LIMIT - (time.time() - t_global))
    if remaining > 60:
        h5, s5 = approach_5_hybrid(time_limit=min(remaining * 0.5, 400),
                                    warm_h=global_best_h)
        results["5_hybrid"] = s5
        if h5 is not None and s5 < global_best_score:
            global_best_score = s5
            global_best_h = h5.copy()
            print(f"\n>>> Global best from Approach 5: C = {s5:.13f}")

    # ===== Approach 4: Multi-scale + polish (uses remaining time) =====
    remaining = max(0, TIME_LIMIT - (time.time() - t_global))
    if remaining > 60:
        h4, s4 = approach_4_multiscale(time_limit=remaining - 30,
                                        warm_h=global_best_h)
        results["4_multiscale_polish"] = s4
        if h4 is not None and s4 < global_best_score:
            global_best_score = s4
            global_best_h = h4.copy()
            print(f"\n>>> Global best from Approach 4: C = {s4:.13f}")

    # ===== Final verification =====
    print("\n" + "=" * 70)
    print("FINAL VERIFICATION")
    print("=" * 70)

    if global_best_h is not None:
        fast_score = fast_evaluate(global_best_h)
        exact_score = compute_upper_bound(global_best_h.tolist())
        print(f"  Fast eval:  C = {fast_score:.15f}")
        print(f"  Exact eval: C = {exact_score:.15f}")
        print(f"  SOTA:       C = {SOTA_SCORE:.15f}")
        print(f"  Difference: {SOTA_SCORE - exact_score:.2e}")
        print(f"  Match fast/exact: {abs(fast_score - exact_score) < 1e-10}")

        if exact_score < SOTA_SCORE:
            print(f"\n  *** IMPROVEMENT FOUND: {SOTA_SCORE - exact_score:.2e} ***")
            if exact_score < TARGET_SCORE:
                print(f"  *** MEETS TARGET (need >= 1e-6 improvement) ***")
            else:
                print(f"  *** Does NOT meet 1e-6 target yet ***")
        else:
            print(f"\n  No improvement over SOTA.")

        # Save
        output = {
            "problem": "erdos-minimum-overlap",
            "n_points": len(global_best_h),
            "score": float(exact_score),
            "values": global_best_h.tolist(),
            "source": "socp_white",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        with open(OUTPUT_PATH, "w") as f:
            json.dump(output, f)
        print(f"  Saved: {OUTPUT_PATH}")
        save_solution(global_best_h, exact_score, "socp_white_best")

    # ===== Summary =====
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for name, score in sorted(results.items(), key=lambda x: x[1]):
        marker = " ***" if score < SOTA_SCORE else ""
        print(f"  {name:25s}: C = {score:.13f}{marker}")

    if global_best_h is not None:
        print(f"\n  GLOBAL BEST: C = {global_best_score:.13f}")
    else:
        print("\n  No valid solution found.")

    total_time = time.time() - t_global
    print(f"  Total time: {total_time:.0f}s ({total_time/60:.1f}min)")
    print("=" * 70)


if __name__ == "__main__":
    main()
