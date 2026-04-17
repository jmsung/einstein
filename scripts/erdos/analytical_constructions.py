"""Analytical/construction-based approaches for Erdos Minimum Overlap (P1).

Instead of pure numerical optimization, these approaches build solutions
from mathematical structure, then polish.

Constructions:
  1. Haugland's piecewise step function (2016)
  2. Chebyshev equioscillation via Remez-style exchange
  3. Flat-spectrum spectral construction
  4. B-spline parametrization with scipy.optimize
  5. Sigmoid network with gradient descent
  6. Torch minimax with logsumexp annealing

Usage:
    cd /Users/jmsung/projects/einstein/cb-feat-auto-p1
    uv run python3 scripts/erdos/analytical_constructions.py
"""

import json
import sys
import time

import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import minimize
from scipy.signal import fftconvolve

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

N = 600
SOTA = 0.3808703105862199
OUTPUT_PATH = "/tmp/p1_analytical_best.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalize_h(h: np.ndarray) -> np.ndarray:
    """Clamp to [0,1] and rescale so sum = n/2."""
    h = np.clip(h, 0.0, 1.0)
    s = h.sum()
    if s > 0:
        h = h * (len(h) / 2.0 / s)
    h = np.clip(h, 0.0, 1.0)
    return h


def correlation_vector(h: np.ndarray) -> np.ndarray:
    """Compute full cross-correlation vector: correlate(h, 1-h, 'full') * 2/n."""
    h = normalize_h(h)
    n = len(h)
    one_minus_h = 1.0 - h
    corr = fftconvolve(h, one_minus_h[::-1], mode="full")
    return corr * 2.0 / n


def hillclimb_polish(h: np.ndarray, n_iters: int = 200_000,
                     time_limit: float = 60.0, tag: str = "") -> tuple[np.ndarray, float]:
    """Zero-sum pairwise hill climbing to polish a solution."""
    rng = np.random.default_rng(42)
    h = normalize_h(h.copy())
    n = len(h)
    best = fast_evaluate(h)
    best_h = h.copy()
    improved = 0
    t0 = time.time()

    for trial in range(n_iters):
        if time.time() - t0 > time_limit:
            break

        i, j = rng.choice(n, size=2, replace=False)
        delta = rng.uniform(1e-10, 5e-5)
        sign = rng.choice([-1, 1])
        old_i, old_j = h[i], h[j]
        new_i = old_i + sign * delta
        new_j = old_j - sign * delta

        if new_i < 0 or new_i > 1 or new_j < 0 or new_j > 1:
            continue

        h[i], h[j] = new_i, new_j
        s = fast_evaluate(h)
        if s < best:
            best = s
            best_h = h.copy()
            improved += 1
        else:
            h[i], h[j] = old_i, old_j

        if (trial + 1) % 50_000 == 0:
            elapsed = time.time() - t0
            print(f"    [{tag}] polish iter {trial+1}: C={best:.13f}, "
                  f"improved={improved}, {elapsed:.0f}s")

    return best_h, best


def save_best(h: np.ndarray, score_val: float, tag: str = ""):
    """Save result to output path."""
    exact = exact_evaluate({"values": h.tolist()})
    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": len(h),
        "score": float(exact),
        "values": h.tolist(),
        "tag": tag,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f)
    print(f"  Saved: {OUTPUT_PATH} (exact C={exact:.13f})")
    return exact


# ---------------------------------------------------------------------------
# Construction 1: Haugland's piecewise step function (2016)
# ---------------------------------------------------------------------------

def haugland_construction() -> tuple[np.ndarray, float]:
    """Haugland (2016) achieved ~0.380927 with a piecewise constant function.

    We parametrize as a K-piece step function and optimize the breakpoints
    and values using scipy.optimize.
    """
    print("\n" + "=" * 60)
    print("Construction 1: Haugland piecewise step function")
    print("=" * 60)

    n = N
    best_h = None
    best_score = float("inf")

    for K in [21, 31, 41, 51]:
        t0 = time.time()
        best_local = float("inf")
        best_local_h = None

        for seed in range(5):
            rng = np.random.default_rng(seed + 100)

            def _params_to_h(params, k=K, _n=n):
                # First k params: breakpoint gaps via softmax (k pieces => k gaps)
                gap_logits = params[:k]
                gaps = np.exp(gap_logits - np.max(gap_logits))
                gaps = gaps / gaps.sum()
                breakpoints = np.concatenate([[0.0], np.cumsum(gaps)])
                # breakpoints has k+1 entries: [0, ..., 1]

                # Next k params: values via sigmoid
                val_logits = params[k:2 * k]
                values = 1.0 / (1.0 + np.exp(-np.clip(val_logits, -20, 20)))

                # Build h on grid
                x = np.linspace(0, 1, _n, endpoint=False)
                h = np.zeros(_n)
                for i in range(k):
                    mask = (x >= breakpoints[i]) & (x < breakpoints[i + 1])
                    h[mask] = values[i]
                # Handle last boundary
                h[x >= breakpoints[-1]] = values[-1]
                return normalize_h(h)

            def _objective(params, k=K):
                h = _params_to_h(params, k=k)
                s = fast_evaluate(h)
                return s if s != float("inf") else 1.0

            # Initialize: alternate high/low values with equal spacing
            gap_logits = np.zeros(K)  # equal spacing
            val_logits = np.zeros(K)
            for i in range(K):
                val_logits[i] = 3.0 if i % 2 == 0 else -3.0
            val_logits += rng.standard_normal(K) * 0.5
            gap_logits += rng.standard_normal(K) * 0.3

            p0 = np.concatenate([gap_logits, val_logits])

            res = minimize(_objective, p0, method="Nelder-Mead",
                           options={"maxiter": 8000, "xatol": 1e-10,
                                    "fatol": 1e-12, "adaptive": True})

            s = res.fun
            if s < best_local:
                best_local = s
                best_local_h = _params_to_h(res.x, k=K)

        elapsed = time.time() - t0
        print(f"  K={K}: C={best_local:.10f} ({elapsed:.1f}s)")

        if best_local < best_score:
            best_score = best_local
            best_h = best_local_h.copy()

    print(f"  Best piecewise: C={best_score:.10f}")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Construction 2: Chebyshev equioscillation via Remez exchange
# ---------------------------------------------------------------------------

def equioscillation_construction() -> tuple[np.ndarray, float]:
    """Build h so C(k) is as equal as possible across all shifts.

    Uses vectorized gradient computation for efficiency.
    """
    print("\n" + "=" * 60)
    print("Construction 2: Chebyshev equioscillation (Remez-style)")
    print("=" * 60)

    n = N
    best_h = None
    best_score = float("inf")

    for trial_seed in range(4):
        rng = np.random.default_rng(trial_seed + 200)

        # Initialize with structured patterns
        x = np.linspace(0, 1, n, endpoint=False)
        if trial_seed == 0:
            h = 0.5 + 0.45 * np.cos(2 * np.pi * x)
        elif trial_seed == 1:
            # Triangle wave
            h = 0.5 + 0.45 * (2 * np.abs(2 * (x - np.floor(x + 0.5))) - 1)
        elif trial_seed == 2:
            # Alternating blocks of ~10 samples
            block = 10
            h = np.zeros(n)
            for i in range(n // block):
                h[i * block:(i + 1) * block] = 0.95 if i % 2 == 0 else 0.05
        else:
            # Random smooth via Fourier
            h = 0.5 * np.ones(n)
            for k in range(1, 30):
                h += rng.standard_normal() * 0.03 * np.cos(2 * np.pi * k * x)
                h += rng.standard_normal() * 0.03 * np.sin(2 * np.pi * k * x)

        h = normalize_h(h)
        current_score = fast_evaluate(h)
        print(f"  Trial {trial_seed}: init C={current_score:.10f}")

        # Vectorized Remez-style iteration
        lr = 0.005
        best_trial_score = current_score
        best_trial_h = h.copy()

        for iteration in range(500):
            cv = correlation_vector(h)
            c_max = cv.max()

            # Find hot shifts (within 0.5% of max)
            threshold = c_max * 0.995
            hot_idx = np.where(cv > threshold)[0]
            lags = hot_idx - (n - 1)

            # Vectorized gradient: for each hot lag k, C(k) = sum_j h[j]*(1-h[j-k])*2/n
            # dC(k)/dh[j] = (1-h[j-k])*2/n  (if j-k in bounds)
            #             - h[j+k]*2/n        (if j+k in bounds)
            grad = np.zeros(n)
            one_minus_h = 1.0 - h

            for k in lags:
                # Contribution from h[j] * (1-h[j-k]):
                # partial wrt h[j] = (1-h[j-k]) where j-k in [0,n-1]
                if k >= 0:
                    j_start, j_end = k, n
                    grad[j_start:j_end] += one_minus_h[:n - k] * 2.0 / n
                else:
                    j_start, j_end = 0, n + k
                    grad[j_start:j_end] += one_minus_h[-k:n] * 2.0 / n

                # Contribution from h[m+k] appearing as (1-h[m]) in C(k):
                # -h[j+k] at index j means: for j+k in [0,n-1]
                if k >= 0:
                    j_start, j_end = 0, n - k
                    grad[j_start:j_end] -= h[k:n] * 2.0 / n
                else:
                    j_start, j_end = -k, n
                    grad[j_start:j_end] -= h[:n + k] * 2.0 / n

            # Normalize and project (zero-mean to preserve sum constraint)
            grad -= grad.mean()
            gn = np.linalg.norm(grad)
            if gn > 0:
                grad /= gn

            # Line search
            improved = False
            for alpha in [lr, lr * 0.5, lr * 0.2, lr * 0.1]:
                h_new = h - alpha * grad
                h_new = normalize_h(h_new)
                new_score = fast_evaluate(h_new)
                if new_score < current_score:
                    h = h_new
                    current_score = new_score
                    improved = True
                    break

            if not improved:
                lr *= 0.95

            if current_score < best_trial_score:
                best_trial_score = current_score
                best_trial_h = h.copy()

            if lr < 1e-8:
                break

            if (iteration + 1) % 100 == 0:
                print(f"    iter {iteration+1}: C={current_score:.10f}, "
                      f"lr={lr:.6f}, hot={len(hot_idx)}")

        print(f"  Trial {trial_seed} final: C={best_trial_score:.10f}")

        if best_trial_score < best_score:
            best_score = best_trial_score
            best_h = best_trial_h.copy()

    print(f"  Best equioscillation: C={best_score:.10f}")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Construction 3: Flat-spectrum spectral construction
# ---------------------------------------------------------------------------

def spectral_construction() -> tuple[np.ndarray, float]:
    """Design h so |DFT(h)|^2 is as flat as possible.

    C(k) = (sum(h) - R(k)) * 2/n. Maximizing min R(k) = flat autocorrelation
    = flat power spectrum.
    """
    print("\n" + "=" * 60)
    print("Construction 3: Flat-spectrum spectral construction")
    print("=" * 60)

    n = N
    n_freq = n // 2 + 1
    best_h = None
    best_score = float("inf")

    # Strategy 1: Optimize phases with fixed flat magnitude
    print("  Phase-only optimization (flat |H|)...")
    for trial_seed in range(5):
        rng = np.random.default_rng(trial_seed + 300)
        t0 = time.time()

        magnitudes = np.ones(n_freq) * np.sqrt(n / 4.0)
        magnitudes[0] = n / 2.0
        phases = rng.uniform(0, 2 * np.pi, n_freq)
        phases[0] = 0.0

        # Optimize all phases at once using Powell (better than NM for moderate dim)
        n_opt = min(100, n_freq - 1)

        def _obj_phases(ph_sub, _mag=magnitudes, _n=n, _nf=n_freq, _base_ph=phases):
            ph = _base_ph.copy()
            ph[1:n_opt + 1] = ph_sub
            H = _mag * np.exp(1j * ph)
            H[0] = _n / 2.0
            h = np.fft.irfft(H, n=_n)
            h = normalize_h(h)
            s = fast_evaluate(h)
            return s if s != float("inf") else 1.0

        p0 = phases[1:n_opt + 1].copy()
        res = minimize(_obj_phases, p0, method="Powell",
                       options={"maxiter": 5000, "ftol": 1e-12})

        phases[1:n_opt + 1] = res.x
        H = magnitudes * np.exp(1j * phases)
        H[0] = n / 2.0
        h = np.fft.irfft(H, n=n)
        h = normalize_h(h)
        s = fast_evaluate(h)

        elapsed = time.time() - t0
        print(f"    trial {trial_seed}: C={s:.10f} ({elapsed:.1f}s)")

        if s < best_score:
            best_score = s
            best_h = h.copy()

    # Strategy 2: Optimize magnitudes + phases jointly
    print("  Magnitude+phase optimization...")
    n_opt = 60

    for seed in range(3):
        rng2 = np.random.default_rng(seed + 400)
        t0 = time.time()

        base_mag = np.sqrt(n / 4.0)

        def _obj_mag_ph(params, _n=n, _nf=n_freq):
            mag_raw = params[:n_opt]
            ph_raw = params[n_opt:]
            mag = np.ones(_nf) * base_mag
            mag[0] = _n / 2.0
            mag[1:n_opt + 1] = np.abs(mag_raw) + 0.1
            ph = np.zeros(_nf)
            ph[1:n_opt + 1] = ph_raw
            H = mag * np.exp(1j * ph)
            H[0] = _n / 2.0
            h = np.fft.irfft(H, n=_n)
            h = normalize_h(h)
            s = fast_evaluate(h)
            return s if s != float("inf") else 1.0

        p0 = np.concatenate([
            np.ones(n_opt) * base_mag + rng2.standard_normal(n_opt) * 1.0,
            rng2.uniform(0, 2 * np.pi, n_opt)
        ])
        res = minimize(_obj_mag_ph, p0, method="Powell",
                       options={"maxiter": 8000, "ftol": 1e-12})

        mag_params = res.x[:n_opt]
        ph_params = res.x[n_opt:]
        mag = np.ones(n_freq) * base_mag
        mag[0] = n / 2.0
        mag[1:n_opt + 1] = np.abs(mag_params) + 0.1
        ph = np.zeros(n_freq)
        ph[1:n_opt + 1] = ph_params
        H = mag * np.exp(1j * ph)
        H[0] = n / 2.0
        h = np.fft.irfft(H, n=n)
        h = normalize_h(h)
        s = fast_evaluate(h)
        elapsed = time.time() - t0
        print(f"    mag+ph seed {seed}: C={s:.10f} ({elapsed:.1f}s)")

        if s < best_score:
            best_score = s
            best_h = h.copy()

    print(f"  Best spectral: C={best_score:.10f}")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Construction 4: B-spline parametrization
# ---------------------------------------------------------------------------

def bspline_construction() -> tuple[np.ndarray, float]:
    """Represent h as a B-spline with K control points, optimize with scipy."""
    print("\n" + "=" * 60)
    print("Construction 4: B-spline parametrization")
    print("=" * 60)

    n = N
    best_h = None
    best_score = float("inf")

    for K in [30, 50, 80, 120]:
        for trial_seed in range(3):
            rng = np.random.default_rng(trial_seed + K * 10 + 500)
            t0 = time.time()

            degree = 3
            knots = np.concatenate([
                np.zeros(degree),
                np.linspace(0, 1, K - degree + 1),
                np.ones(degree),
            ])

            x_eval = np.linspace(0, 1, n, endpoint=False)

            # Precompute basis matrix
            basis_matrix = np.zeros((n, K))
            for i in range(K):
                coeffs = np.zeros(K)
                coeffs[i] = 1.0
                spl = BSpline(knots, coeffs, degree, extrapolate=False)
                basis_matrix[:, i] = spl(x_eval)
            basis_matrix = np.nan_to_num(basis_matrix, nan=0.0)

            def _coeffs_to_h(c, bm=basis_matrix):
                vals = 1.0 / (1.0 + np.exp(-np.clip(c, -20, 20)))
                h = bm @ vals
                return normalize_h(h)

            def _objective(c):
                h = _coeffs_to_h(c)
                s = fast_evaluate(h)
                return s if s != float("inf") else 1.0

            # Initialize: alternating pattern
            c0 = np.zeros(K)
            for i in range(K):
                c0[i] = 3.0 if i % 2 == 0 else -3.0
            c0 += rng.standard_normal(K) * 0.5

            res = minimize(_objective, c0, method="Powell",
                           options={"maxiter": 10000, "ftol": 1e-12})

            h = _coeffs_to_h(res.x)
            s = fast_evaluate(h)
            elapsed = time.time() - t0
            print(f"  K={K}, seed={trial_seed}: C={s:.10f} ({elapsed:.1f}s)")

            if s < best_score:
                best_score = s
                best_h = h.copy()

    print(f"  Best B-spline: C={best_score:.10f}")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Construction 5: Sigmoid network
# ---------------------------------------------------------------------------

def sigmoid_network_construction() -> tuple[np.ndarray, float]:
    """Parametrize h as a sum of sigmoids and optimize with torch.

    h(x) = sigmoid(bias + sum_k w_k * sigmoid(a_k * (x - b_k)))
    Uses CPU with float64 for precision (MPS doesn't support float64).
    """
    print("\n" + "=" * 60)
    print("Construction 5: Sigmoid network (torch)")
    print("=" * 60)

    import torch

    n = N
    # Always use CPU for float64 precision
    device = "cpu"
    dtype = torch.float64

    best_h = None
    best_score = float("inf")

    for n_sigmoids in [20, 40, 80]:
        for trial_seed in range(3):
            torch.manual_seed(trial_seed + n_sigmoids * 100 + 600)
            t0 = time.time()

            K = n_sigmoids
            x_t = torch.linspace(0, 1, n, device=device, dtype=dtype)

            w = torch.randn(K, device=device, dtype=dtype) * 0.3
            a = torch.randn(K, device=device, dtype=dtype) * 5.0
            b = torch.linspace(0.05, 0.95, K, device=device, dtype=dtype).clone()
            b = b + torch.randn(K, device=device, dtype=dtype) * 0.05
            bias = torch.zeros(1, device=device, dtype=dtype)

            w.requires_grad_(True)
            a.requires_grad_(True)
            b.requires_grad_(True)
            bias.requires_grad_(True)

            optimizer = torch.optim.Adam([w, a, b, bias], lr=0.01)
            scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=4000)

            nc = 2 * n - 1
            nfft = 1
            while nfft < nc:
                nfft <<= 1

            local_best = float("inf")
            local_best_h = None

            for step in range(4000):
                optimizer.zero_grad()

                inner = a.unsqueeze(1) * (x_t.unsqueeze(0) - b.unsqueeze(1))
                sig_inner = torch.sigmoid(inner)
                raw = bias + (w.unsqueeze(1) * sig_inner).sum(dim=0)
                h_t = torch.sigmoid(raw)

                s = h_t.sum()
                h_t = h_t * (n / 2.0) / (s + 1e-30)
                h_t = torch.clamp(h_t, 0.0, 1.0)

                one_minus_h = 1.0 - h_t
                H_fft = torch.fft.rfft(h_t, n=nfft)
                G_fft = torch.fft.rfft(one_minus_h.flip(0), n=nfft)
                corr = torch.fft.irfft(H_fft * G_fft, n=nfft)[:nc]
                C = corr.max() * 2.0 / n

                C.backward()
                optimizer.step()
                scheduler.step()

                if (step + 1) % 500 == 0:
                    c_val = C.item()
                    if c_val < local_best and c_val > 0:
                        local_best = c_val
                        local_best_h = h_t.detach().cpu().numpy().copy()

            # Final eval with numpy precision
            with torch.no_grad():
                inner = a.unsqueeze(1) * (x_t.unsqueeze(0) - b.unsqueeze(1))
                sig_inner = torch.sigmoid(inner)
                raw = bias + (w.unsqueeze(1) * sig_inner).sum(dim=0)
                h_t = torch.sigmoid(raw)
                s = h_t.sum()
                h_t = h_t * (n / 2.0) / (s + 1e-30)
                h_t = torch.clamp(h_t, 0.0, 1.0)

            h_np = h_t.cpu().numpy()
            s = fast_evaluate(h_np)
            if s < local_best:
                local_best = s
                local_best_h = h_np.copy()

            elapsed = time.time() - t0
            print(f"  K={K}, seed={trial_seed}: C={local_best:.10f} ({elapsed:.1f}s)")

            if local_best < best_score:
                best_score = local_best
                best_h = local_best_h.copy()

    print(f"  Best sigmoid network: C={best_score:.10f}")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Construction 6: Direct minimax with torch + logsumexp annealing
# ---------------------------------------------------------------------------

def torch_minimax_construction() -> tuple[np.ndarray, float]:
    """Direct minimax: minimize logsumexp(C(k)/temp) with temp annealing.

    Operates in logit space h = sigmoid(z) for unconstrained optimization.
    Uses CPU for float64 precision.
    """
    print("\n" + "=" * 60)
    print("Construction 6: Torch minimax with logsumexp annealing")
    print("=" * 60)

    import torch

    n = N
    device = "cpu"
    dtype = torch.float64

    best_h = None
    best_score = float("inf")

    nc = 2 * n - 1
    nfft = 1
    while nfft < nc:
        nfft <<= 1

    for trial_seed in range(6):
        torch.manual_seed(trial_seed + 700)
        rng = np.random.default_rng(trial_seed + 700)
        t0 = time.time()

        x = np.linspace(0, 1, n, endpoint=False)
        if trial_seed == 0:
            h_init = 0.5 + 0.45 * np.cos(2 * np.pi * x)
        elif trial_seed == 1:
            # Square wave with smooth edges
            h_init = 0.5 + 0.45 * np.tanh(10 * np.cos(2 * np.pi * x))
        elif trial_seed == 2:
            # Alternating blocks of ~20
            block = 20
            h_init = np.zeros(n)
            for i in range(n // block + 1):
                s, e = i * block, min((i + 1) * block, n)
                h_init[s:e] = 0.95 if i % 2 == 0 else 0.05
        elif trial_seed == 3:
            # Smooth random via Fourier
            raw = rng.standard_normal(n)
            H_raw = np.fft.rfft(raw)
            freqs = np.arange(len(H_raw))
            H_raw *= np.exp(-freqs**2 / (2 * 30**2))
            h_init = np.fft.irfft(H_raw, n=n)
            h_init = (h_init - h_init.min()) / (h_init.max() - h_init.min() + 1e-10)
        elif trial_seed == 4:
            # Two-frequency cosine
            h_init = 0.5 + 0.3 * np.cos(2 * np.pi * x) + 0.15 * np.cos(4 * np.pi * x)
        else:
            h_init = rng.random(n)

        h_init = normalize_h(h_init)
        h_init = np.clip(h_init, 1e-4, 1 - 1e-4)
        z_init = np.log(h_init / (1 - h_init))
        z = torch.tensor(z_init, device=device, dtype=dtype, requires_grad=True)

        optimizer = torch.optim.Adam([z], lr=0.003)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=8000)

        local_best = float("inf")
        local_best_h = None

        n_steps = 8000
        temp_start = 0.01
        temp_end = 0.0005

        for step in range(n_steps):
            optimizer.zero_grad()

            temp = temp_start * (temp_end / temp_start) ** (step / n_steps)

            h_t = torch.sigmoid(z)
            s = h_t.sum()
            h_t = h_t * (n / 2.0) / (s + 1e-30)
            h_t = torch.clamp(h_t, 0.0, 1.0)

            one_minus_h = 1.0 - h_t
            H_fft = torch.fft.rfft(h_t, n=nfft)
            G_fft = torch.fft.rfft(one_minus_h.flip(0), n=nfft)
            corr = torch.fft.irfft(H_fft * G_fft, n=nfft)[:nc]
            corr_scaled = corr * 2.0 / n

            loss = temp * torch.logsumexp(corr_scaled / temp, dim=0)

            loss.backward()
            optimizer.step()
            scheduler.step()

            if (step + 1) % 1000 == 0:
                with torch.no_grad():
                    h_np = torch.sigmoid(z).cpu().numpy()
                    h_np = normalize_h(h_np)
                    c_val = fast_evaluate(h_np)
                    if c_val < local_best and c_val > 0:
                        local_best = c_val
                        local_best_h = h_np.copy()

        # Final extraction
        with torch.no_grad():
            h_np = torch.sigmoid(z).cpu().numpy()
            h_np = normalize_h(h_np)
            c_val = fast_evaluate(h_np)
            if c_val < local_best and c_val > 0:
                local_best = c_val
                local_best_h = h_np.copy()

        elapsed = time.time() - t0
        print(f"  Trial {trial_seed}: C={local_best:.10f} ({elapsed:.1f}s)")

        if local_best < best_score:
            best_score = local_best
            best_h = local_best_h.copy()

    print(f"  Best minimax: C={best_score:.10f}")
    return best_h, best_score


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("  Erdos Minimum Overlap -- Analytical Constructions")
    print(f"  n={N}, SOTA={SOTA}")
    print("=" * 70)

    global_best_h = None
    global_best_score = float("inf")
    t_total = time.time()

    results = {}

    constructions = [
        ("Haugland piecewise", haugland_construction),
        ("Equioscillation", equioscillation_construction),
        ("Spectral", spectral_construction),
        ("B-spline", bspline_construction),
        ("Sigmoid network", sigmoid_network_construction),
        ("Torch minimax", torch_minimax_construction),
    ]

    for name, func in constructions:
        try:
            h, s = func()
            results[name] = s

            if s < global_best_score:
                global_best_score = s
                global_best_h = h.copy()
                print(f"\n  >>> New global best: {name} -> C={s:.13f}")

        except Exception as e:
            print(f"\n  !!! {name} failed: {e}")
            import traceback
            traceback.print_exc()

    # Polish the best result
    if global_best_h is not None:
        print("\n" + "=" * 60)
        print("Final polishing of best construction...")
        print(f"Starting from C={global_best_score:.13f}")
        print("=" * 60)

        remaining = max(120.0, 600.0 - (time.time() - t_total))
        polished_h, polished_score = hillclimb_polish(
            global_best_h, n_iters=1_000_000,
            time_limit=min(remaining, 180.0),
            tag="final"
        )

        if polished_score < global_best_score:
            global_best_score = polished_score
            global_best_h = polished_h.copy()
            print(f"  Polish improved to: C={polished_score:.13f}")

        save_best(global_best_h, global_best_score, "analytical_best")

    # Summary
    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)
    for name, s in sorted(results.items(), key=lambda x: x[1]):
        marker = " *" if s <= global_best_score + 1e-12 else ""
        print(f"  {name:30s}: C={s:.13f}{marker}")

    if global_best_h is not None:
        exact = exact_evaluate({"values": global_best_h.tolist()})
        print(f"\n  Global best (exact): C={exact:.13f}")
        print(f"  SOTA:                C={SOTA:.13f}")
        gap = exact - SOTA
        print(f"  Gap:                 {gap:+.2e}")
        if exact < SOTA:
            print("  *** BEATS SOTA! ***")

    elapsed = time.time() - t_total
    print(f"\n  Total time: {elapsed:.0f}s")
    print("=" * 70)


if __name__ == "__main__":
    main()
