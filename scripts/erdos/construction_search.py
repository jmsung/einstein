"""Construction-based search for Erdős Minimum Overlap.

Instead of gradient-based optimization, try structured mathematical constructions.
The idea: the SOTA was found by gradient methods and is at a local optimum.
A completely different construction might land in a better basin.

Constructions to try:
1. Sigmoid of trigonometric polynomials with optimized coefficients
2. Legendre-symbol-based constructions
3. Piecewise optimal (optimize each piece independently)
4. Smoothed binary (start from 0/1, gradually smooth)
5. Haar wavelet representation
"""

import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from scipy.signal import fftconvolve

from einstein.erdos.fast import fast_evaluate
from einstein.erdos.evaluator import evaluate as exact_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
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


def construction_trig_sigmoid(n=600, n_terms=50, n_trials=5000, seed=0):
    """h(x) = sigmoid(sum of trig terms with random coefficients).

    This is a smooth function that naturally satisfies [0,1] bounds.
    Explore many random coefficient sets.
    """
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 2, n, endpoint=False)
    best_score = float("inf")
    best_h = None

    for trial in range(n_trials):
        # Random coefficients
        a = rng.standard_normal(n_terms) * np.sqrt(2.0 / n_terms)
        b = rng.standard_normal(n_terms) * np.sqrt(2.0 / n_terms)

        # Build function
        f = np.zeros(n)
        for k in range(n_terms):
            freq = (k + 1) * np.pi
            f += a[k] * np.cos(freq * x) + b[k] * np.sin(freq * x)

        # Sigmoid to [0, 1]
        h = 1.0 / (1.0 + np.exp(-f))
        h = normalize(h)
        score = fast_eval(h)

        if score < best_score:
            best_score = score
            best_h = h.copy()
            if trial % 500 == 0:
                print(f"  trial {trial}: NEW BEST = {best_score:.10f}")

    return best_h, best_score


def construction_legendre(n=600, seed=0):
    """Use Legendre-symbol-like constructions.

    For prime p, the Legendre symbol χ(a) = (a/p) takes values {-1, 0, 1}.
    Map to [0,1]: h = (χ + 1) / 2.
    These sequences have known autocorrelation properties.
    """
    rng = np.random.default_rng(seed)
    best_score = float("inf")
    best_h = None

    # Find primes near n
    def is_prime(x):
        if x < 2:
            return False
        for d in range(2, int(x**0.5) + 1):
            if x % d == 0:
                return False
        return True

    primes = [p for p in range(max(n - 50, 100), n + 50) if is_prime(p)]

    for p in primes:
        # Legendre symbol
        chi = np.zeros(p)
        for a in range(1, p):
            # Compute a^((p-1)/2) mod p
            val = pow(a, (p - 1) // 2, p)
            chi[a] = 1 if val == 1 else -1

        # Map to [0, 1]: (chi + 1) / 2
        h = (chi + 1.0) / 2.0  # values in {0, 0.5, 1}

        # Resize to n
        if len(h) != n:
            h = np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(h)), h)

        h = normalize(h)
        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()

        # Also try shifted versions
        for shift in range(0, p, p // 10):
            h_shifted = np.roll(chi, shift)
            h_s = (h_shifted + 1.0) / 2.0
            if len(h_s) != n:
                h_s = np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(h_s)), h_s)
            h_s = normalize(h_s)
            score = fast_eval(h_s)
            if score < best_score:
                best_score = score
                best_h = h_s.copy()

    print(f"  Legendre: best={best_score:.10f} (tested {len(primes)} primes)")

    # Also try quadratic residue based constructions
    for p in primes[:5]:
        qr = set()
        for a in range(1, p):
            qr.add((a * a) % p)

        h = np.array([1.0 if i % p in qr else 0.0 for i in range(n)])
        h = normalize(h)
        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()

    return best_h, best_score


def construction_smooth_binary(n=600, n_trials=200, kernel_size=10,
                                time_limit=120, seed=0):
    """Start from binary (0/1) solutions, smooth with Gaussian kernel.

    The smoothing may give better continuous solutions.
    """
    rng = np.random.default_rng(seed)
    best_score = float("inf")
    best_h = None
    t0 = time.time()

    from scipy.ndimage import gaussian_filter1d

    for trial in range(n_trials):
        if time.time() - t0 > time_limit:
            break

        # Random binary vector with ~n/2 ones
        h_bin = (rng.random(n) < 0.5).astype(np.float64)

        # Try different smoothing levels
        for sigma in [1, 2, 3, 5, 8, 10, 15, 20, 30, 50]:
            h_smooth = gaussian_filter1d(h_bin, sigma, mode='wrap')
            h_smooth = normalize(h_smooth)
            score = fast_eval(h_smooth)
            if score < best_score:
                best_score = score
                best_h = h_smooth.copy()

        if (trial + 1) % 50 == 0:
            print(f"  trial {trial+1}: best={best_score:.10f}")

    return best_h, best_score


def construction_haar_wavelet(n=600, n_trials=2000, seed=0):
    """Parameterize h using Haar wavelet coefficients.

    h = mean + sum of Haar wavelets at different scales.
    Only optimize the wavelet coefficients.
    """
    rng = np.random.default_rng(seed)
    best_score = float("inf")
    best_h = None

    # Haar wavelet basis for length n
    # We'll use a simplified version: scale-j wavelets at positions
    max_j = int(np.log2(n))

    for trial in range(n_trials):
        h = np.ones(n) * 0.5  # start from mean

        # Add random Haar wavelets
        n_wavelets = rng.integers(5, max_j * 3)
        for _ in range(n_wavelets):
            j = rng.integers(1, max_j + 1)  # scale
            block_size = n // (2 ** j)
            if block_size < 1:
                continue
            pos = rng.integers(0, n - block_size + 1)
            amp = rng.uniform(-0.3, 0.3)
            h[pos:pos + block_size] += amp

        h = normalize(h)
        score = fast_eval(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()

        if (trial + 1) % 500 == 0:
            print(f"  trial {trial+1}: best={best_score:.10f}")

    return best_h, best_score


def massive_random_search(n=600, n_trials=50000, time_limit=300, seed=0):
    """Try a LOT of random functions and keep the best.

    Also try: random + local refinement.
    """
    rng = np.random.default_rng(seed)
    best_score = float("inf")
    best_h = None
    t0 = time.time()
    pool = []  # keep top 10

    for trial in range(n_trials):
        if time.time() - t0 > time_limit:
            break

        # Random function generation
        method = trial % 5
        if method == 0:
            # Uniform random
            h = rng.random(n)
        elif method == 1:
            # Beta distribution
            a, b = rng.uniform(0.5, 5), rng.uniform(0.5, 5)
            h = rng.beta(a, b, n)
        elif method == 2:
            # Smooth random (low-pass filtered noise)
            noise = rng.standard_normal(n)
            k_cutoff = rng.integers(5, n // 2)
            H = np.fft.rfft(noise)
            H[k_cutoff:] = 0
            h = np.fft.irfft(H, n=n)
            h = (h - h.min()) / (h.max() - h.min() + 1e-30)
        elif method == 3:
            # Piecewise constant with random pieces
            n_pieces = rng.integers(5, 200)
            breaks = np.sort(rng.choice(n, n_pieces - 1, replace=False))
            breaks = np.concatenate([[0], breaks, [n]])
            heights = rng.random(n_pieces)
            h = np.zeros(n)
            for i in range(n_pieces):
                h[breaks[i]:breaks[i + 1]] = heights[i]
        else:
            # Sigmoid of polynomial
            x = np.linspace(-3, 3, n)
            deg = rng.integers(3, 20)
            coeffs = rng.standard_normal(deg + 1) * 0.3
            poly = np.polyval(coeffs, x)
            h = 1.0 / (1.0 + np.exp(-poly))

        h = normalize(h)
        score = fast_eval(h)

        if score < best_score:
            best_score = score
            best_h = h.copy()

        # Track top 10
        pool.append((score, h.copy()))
        pool.sort(key=lambda x: x[0])
        pool = pool[:10]

        if (trial + 1) % 10000 == 0:
            elapsed = time.time() - t0
            print(f"  trial {trial+1}: best={best_score:.10f} ({elapsed:.0f}s)")

    print(f"\nTop 10 random scores:")
    for i, (s, _) in enumerate(pool):
        print(f"  #{i+1}: {s:.10f}")

    return best_h, best_score


def main():
    print("=" * 70)
    print("CONSTRUCTION SEARCH: Erdős Minimum Overlap")
    print("=" * 70)
    t_global = time.time()
    results = {}

    # 1. Trig sigmoid
    print("\n--- Trig Sigmoid Construction ---")
    t0 = time.time()
    h, s = construction_trig_sigmoid(600, n_terms=50, n_trials=10000, seed=42)
    print(f"  Result: {s:.10f} ({time.time()-t0:.0f}s)")
    results["trig_sigmoid"] = (h, s)

    # 2. Legendre
    print("\n--- Legendre Symbol Construction ---")
    t0 = time.time()
    h, s = construction_legendre(600, seed=42)
    results["legendre"] = (h, s)

    # 3. Smooth binary
    print("\n--- Smooth Binary Construction ---")
    t0 = time.time()
    h, s = construction_smooth_binary(600, n_trials=500, time_limit=120, seed=42)
    print(f"  Result: {s:.10f} ({time.time()-t0:.0f}s)")
    results["smooth_binary"] = (h, s)

    # 4. Haar wavelet
    print("\n--- Haar Wavelet Construction ---")
    t0 = time.time()
    h, s = construction_haar_wavelet(600, n_trials=5000, seed=42)
    print(f"  Result: {s:.10f} ({time.time()-t0:.0f}s)")
    results["haar"] = (h, s)

    # 5. Massive random search
    print("\n--- Massive Random Search ---")
    t0 = time.time()
    h, s = massive_random_search(600, n_trials=100000, time_limit=300, seed=42)
    print(f"  Result: {s:.10f} ({time.time()-t0:.0f}s)")
    results["random_search"] = (h, s)

    # Summary
    print("\n" + "=" * 70)
    print(f"SUMMARY (SOTA = {SOTA_SCORE:.10f})")
    print("=" * 70)
    for name, (h, s) in sorted(results.items(), key=lambda x: x[1][1]):
        delta = SOTA_SCORE - s
        print(f"  {name:20s}: {s:.10f}  improve={delta:.2e}")

    # Save best
    best_name = min(results, key=lambda k: results[k][1])
    best_h, best_score = results[best_name]

    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": len(best_h), "score": float(best_score),
        "values": [round(float(v), 14) for v in best_h],
        "tag": f"construction_{best_name}",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"construction_best_{best_score:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f)
    print(f"\nSaved: {fname}")
    print(f"Total time: {time.time()-t_global:.0f}s")


if __name__ == "__main__":
    main()
