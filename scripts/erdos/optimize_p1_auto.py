"""Auto-solve optimization for Erdős Minimum Overlap (Problem 1).

CPU-only, no torch. Runs spectral search + basin hopping + multi-n.
"""

import json
import sys
import time
from pathlib import Path
from functools import partial

import numpy as np
from scipy.signal import fftconvolve

print = partial(print, flush=True)

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

RESULTS_DIR = Path("results/problem-1-erdos-overlap")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
ARENA_SOTA = 0.3808703105862199
TARGET = ARENA_SOTA - 1e-6


def load_sota():
    """Load SOTA solution."""
    p = RESULTS_DIR / "sota_together_ai.json"
    with open(p) as f:
        sol = json.load(f)
    raw = sol.get("data", sol)
    return np.array(raw["values"] if isinstance(raw, dict) else raw, dtype=np.float64)


def polish(h, n_iters=200_000, delta_scale=1e-7, seed=42, label=""):
    """Zero-sum multi-point mass transport."""
    rng = np.random.default_rng(seed)
    n = len(h)
    h = np.clip(h.copy(), 0, 1)
    target = n / 2.0
    s = np.sum(h)
    if s > 0:
        h *= target / s
    h = np.clip(h, 0, 1)

    best = fast_evaluate(h)
    improved = 0
    t0 = time.time()

    for trial in range(n_iters):
        k = rng.choice([2, 3, 4, 5])
        idx = rng.choice(n, size=k, replace=False)
        delta = rng.standard_normal(k) * delta_scale
        delta -= delta.mean()
        old = h[idx].copy()
        new_vals = old + delta
        if np.any(new_vals < 0) or np.any(new_vals > 1):
            continue
        h[idx] = new_vals
        s = fast_evaluate(h)
        if s < best:
            best = s
            improved += 1
        else:
            h[idx] = old

        if (trial + 1) % 100_000 == 0:
            print(f"    {label} iter {trial+1}: C={best:.13f} imp={improved} "
                  f"t={time.time()-t0:.0f}s")

    return h, best


def approach_spectral(h_sota, n=600):
    """Spectral phase/magnitude random walk from SOTA."""
    print("\n[1/3] Spectral search")
    print("-" * 40)

    H = np.fft.rfft(h_sota)
    mags = np.abs(H)
    phases = np.angle(H)
    n_freq = len(H)

    best = ARENA_SOTA
    best_h = None
    rng = np.random.default_rng(42)

    # Phase perturbation search
    for trial in range(500):
        perturb = rng.normal(0, 0.01, n_freq)
        perturb[0] = 0
        new_phases = phases + perturb
        H_new = mags * np.exp(1j * new_phases)
        H_new[0] = n / 2.0
        h_new = np.fft.irfft(H_new, n=n)
        h_new = np.clip(h_new, 0, 1)
        target = n / 2.0
        s = np.sum(h_new)
        if s > 0:
            h_new *= target / s
        h_new = np.clip(h_new, 0, 1)
        s = fast_evaluate(h_new)
        if s < best:
            best = s
            best_h = h_new.copy()
            phases = new_phases.copy()
    print(f"  Phase search (500): {best:.13f}")

    # Magnitude perturbation
    for trial in range(500):
        perturb = rng.normal(0, 0.1, n_freq)
        perturb[0] = 0
        new_mags = np.maximum(0, mags + perturb)
        H_new = new_mags * np.exp(1j * phases)
        H_new[0] = n / 2.0
        h_new = np.fft.irfft(H_new, n=n)
        h_new = np.clip(h_new, 0, 1)
        target = n / 2.0
        s = np.sum(h_new)
        if s > 0:
            h_new *= target / s
        h_new = np.clip(h_new, 0, 1)
        s = fast_evaluate(h_new)
        if s < best:
            best = s
            best_h = h_new.copy()
            mags = new_mags.copy()
    print(f"  Mag search (500): {best:.13f}")

    # Single-frequency random walk
    for trial in range(2000):
        k = rng.integers(1, n_freq)
        pd = rng.normal(0, 0.005)
        md = rng.normal(0, 0.05)
        old_mag, old_phase = mags[k], phases[k]
        mags[k] = max(0, mags[k] + md)
        phases[k] += pd
        H_new = mags * np.exp(1j * phases)
        H_new[0] = n / 2.0
        h_new = np.fft.irfft(H_new, n=n)
        h_new = np.clip(h_new, 0, 1)
        target = n / 2.0
        sn = np.sum(h_new)
        if sn > 0:
            h_new *= target / sn
        h_new = np.clip(h_new, 0, 1)
        s = fast_evaluate(h_new)
        if s < best:
            best = s
            best_h = h_new.copy()
        else:
            mags[k], phases[k] = old_mag, old_phase
    print(f"  Single-freq walk (2000): {best:.13f}")

    print(f"  RESULT: {best:.13f} (diff={best - ARENA_SOTA:+.2e})")
    return best_h, best


def approach_basin_hop(h_sota, n=600, n_hops=30):
    """Large perturbations from SOTA + local polish."""
    print("\n[2/3] Basin hopping from SOTA")
    print("-" * 40)

    best = ARENA_SOTA
    best_h = None
    x = np.linspace(0, 1, n, endpoint=False)

    for hop in range(n_hops):
        rng = np.random.default_rng(hop * 31 + 7)
        h = h_sota.copy()

        ptype = hop % 6
        if ptype == 0:
            start = rng.integers(0, n - 80)
            length = rng.integers(20, 80)
            seg = h[start:start+length].copy()
            rng.shuffle(seg)
            h[start:start+length] = seg
        elif ptype == 1:
            k = rng.integers(1, 50)
            amp = rng.uniform(0.05, 0.3)
            phase = rng.uniform(0, 2 * np.pi)
            h += amp * np.cos(2 * np.pi * k * x + phase)
        elif ptype == 2:
            start = rng.integers(0, n - 40)
            length = rng.integers(10, 40)
            h[start:start+length] = 1.0 - h[start:start+length]
        elif ptype == 3:
            h += rng.normal(0, 0.15, n)
        elif ptype == 4:
            s1, s2 = rng.integers(0, n - 40, 2)
            L = rng.integers(10, 40)
            seg1, seg2 = h[s1:s1+L].copy(), h[s2:s2+L].copy()
            h[s1:s1+L], h[s2:s2+L] = seg2, seg1
        elif ptype == 5:
            noise = rng.normal(0, 0.2, n)
            H = np.fft.rfft(noise)
            H[10:] = 0
            h += np.fft.irfft(H, n=n)

        h = np.clip(h, 0, 1)
        target = n / 2.0
        s = np.sum(h)
        if s > 0:
            h *= target / s
        h = np.clip(h, 0, 1)
        s = np.sum(h)
        if s > 0:
            h *= target / s

        perturbed = fast_evaluate(h)
        h, final = polish(h, n_iters=100_000, delta_scale=1e-6, seed=hop, label=f"hop{hop}")
        print(f"  hop {hop} (type={ptype}): {perturbed:.6f} -> {final:.10f}")

        if final < best:
            best = final
            best_h = h

    print(f"  RESULT: {best:.13f} (diff={best - ARENA_SOTA:+.2e})")
    return best_h, best


def approach_cold_start_polish(n=600, n_starts=8):
    """Diverse cold starts + aggressive polishing."""
    print("\n[3/3] Cold-start + polish (L-BFGS-B + local search)")
    print("-" * 40)

    from scipy.optimize import minimize as sp_minimize

    best = ARENA_SOTA
    best_h = None
    x = np.linspace(0, 1, n, endpoint=False)

    for i in range(n_starts):
        rng = np.random.default_rng(i * 17 + 3)

        if i == 0:
            alpha = 1.5
            h = np.maximum(0, 1 - np.abs(2 * x - 1) ** alpha)
        elif i == 1:
            alpha = 2.0
            h = np.maximum(0, 1 - np.abs(2 * x - 1) ** alpha)
        elif i < 4:
            h = np.full(n, 0.5)
            K = [10, 20][i - 2]
            for k in range(1, K + 1):
                amp = rng.uniform(-0.3, 0.3) / np.sqrt(k)
                phase = rng.uniform(0, 2 * np.pi)
                h += amp * np.cos(2 * np.pi * k * x + phase)
        elif i < 6:
            n_bumps = [5, 8][i - 4]
            h = np.zeros(n)
            for _ in range(n_bumps):
                c = rng.uniform(0.1, 0.9)
                w = rng.uniform(0.03, 0.12)
                a = rng.uniform(0.5, 1.0)
                h += a * np.exp(-0.5 * ((x - c) / w) ** 2)
        else:
            h = rng.random(n)
            H = np.fft.rfft(h)
            H[20 + i * 5:] = 0
            h = np.fft.irfft(H, n=n)

        h = np.clip(h, 0, 1)
        target = n / 2.0
        s = np.sum(h)
        if s > 0:
            h *= target / s
        h = np.clip(h, 0, 1)
        if np.sum(h) <= 0:
            print(f"  start {i}: invalid (skip)")
            continue

        init = fast_evaluate(h)

        # L-BFGS-B polish
        def obj(x_flat):
            xc = np.clip(x_flat, 0, 1)
            s = np.sum(xc)
            if s > 0:
                xc = xc * (target / s)
            xc = np.clip(xc, 0, 1)
            return fast_evaluate(xc)

        result = sp_minimize(obj, h, method='L-BFGS-B',
                           bounds=[(0, 1)] * n,
                           options={'maxiter': 1000, 'ftol': 1e-15})
        h_opt = np.clip(result.x, 0, 1)
        s = np.sum(h_opt)
        if s > 0:
            h_opt *= target / s
        h_opt = np.clip(h_opt, 0, 1)

        lbfgs_score = fast_evaluate(h_opt)

        # Then mass-transport polish
        h_opt, final = polish(h_opt, n_iters=200_000, delta_scale=1e-6, seed=i, label=f"cs{i}")
        print(f"  start {i}: {init:.6f} -> lbfgs={lbfgs_score:.8f} -> polish={final:.10f}")

        if final < best:
            best = final
            best_h = h_opt

    print(f"  RESULT: {best:.13f} (diff={best - ARENA_SOTA:+.2e})")
    return best_h, best


def main():
    t_start = time.time()

    print("=" * 60)
    print("Erdős Minimum Overlap — Auto-Solve Optimization")
    print(f"SOTA: {ARENA_SOTA:.16f}")
    print(f"TARGET (beat by 1e-6): {TARGET:.16f}")
    print(f"Start: {time.strftime('%H:%M:%S')}")
    print("=" * 60)

    h_sota = load_sota()
    print(f"Loaded SOTA: n={len(h_sota)}, sum={np.sum(h_sota):.10f}")
    print(f"Verified score: {fast_evaluate(h_sota):.16f}")

    results = {}

    t0 = time.time()
    h1, s1 = approach_spectral(h_sota)
    results["spectral"] = (s1, time.time() - t0)

    t0 = time.time()
    h2, s2 = approach_basin_hop(h_sota)
    results["basin_hop"] = (s2, time.time() - t0)

    t0 = time.time()
    h3, s3 = approach_cold_start_polish()
    results["cold_start"] = (s3, time.time() - t0)

    # Summary
    elapsed = time.time() - t_start
    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print(f"{'Approach':<20} {'Score':<22} {'vs SOTA':<15} {'Time':<10}")
    print("-" * 67)
    for name, (s, t) in sorted(results.items(), key=lambda x: x[1][0]):
        diff = s - ARENA_SOTA
        status = "BEATS!" if s < TARGET else ""
        print(f"{name:<20} {s:.16f}  {diff:+.2e}  {t:>6.0f}s  {status}")

    best_name = min(results, key=lambda k: results[k][0])
    best_score = results[best_name][0]

    print(f"\nOverall best: {best_name} = {best_score:.16f}")
    print(f"SOTA:         {ARENA_SOTA:.16f}")
    print(f"Difference:   {best_score - ARENA_SOTA:+.2e}")
    print(f"Beats SOTA by 1e-6? {'YES' if best_score < TARGET else 'NO'}")
    print(f"Total elapsed: {elapsed:.0f}s ({elapsed/60:.1f} min)")

    # Save best
    all_h = [h1, h2, h3]
    all_s = [s1, s2, s3]
    best_idx = min(range(3), key=lambda i: all_s[i] if all_h[i] is not None else float("inf"))
    bh, bs = all_h[best_idx], all_s[best_idx]

    if bh is not None:
        exact = exact_evaluate({"values": bh.tolist()})
        fast = fast_evaluate(bh)
        print(f"\nTriple verification:")
        print(f"  Fast:  {fast:.16f}")
        print(f"  Exact: {exact:.16f}")
        print(f"  Match: {abs(fast - exact) < 1e-10}")

        out = {
            "values": bh.tolist(),
            "score": float(exact),
            "approach": best_name,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"auto_best_{exact:.13f}.json"
        with open(fname, "w") as f:
            json.dump(out, f)
        print(f"Saved: {fname}")


if __name__ == "__main__":
    main()
