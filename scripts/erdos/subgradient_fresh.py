"""Projected subgradient descent for Erdős Minimum Overlap.

The SOTA (0.38087) at n=600 is a near-binary step function that's already
extremely well optimized (440+ equioscillation constraints). Subgradient
from SOTA makes no progress.

New strategy: optimize at n=600 from diverse starts with aggressive methods.
The solution is known to be nearly binary (0/1 indicator with smooth edges).
We parametrize using:
1. Step-function families with different widths and positions
2. Smooth approximations that we gradually sharpen
3. Direct search on the transition region indices

Also try various n to find grids where the minimum is structurally lower.
"""

import json
import os
import time
import numpy as np
from scipy.signal import fftconvolve


def score_h(h):
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    target = n / 2.0
    s = np.sum(h)
    if s != target:
        h = h * (target / s)
    conv = np.correlate(h, 1 - h, mode='full')
    return float(np.max(conv)) / n * 2


def score_fft(h):
    h = np.asarray(h, dtype=np.float64)
    n = len(h)
    target = n / 2.0
    s = np.sum(h)
    if s != target:
        h = h * (target / s)
    conv = fftconvolve(h, (1 - h)[::-1], mode='full')
    return float(np.max(conv)) / n * 2


def compute_corr(h):
    n = len(h)
    return fftconvolve(h, (1 - h)[::-1], mode='full') * (2.0 / n)


def compute_subgradient(h, active_lags):
    n = len(h)
    dx = 2.0 / n
    grad = np.zeros(n)
    for s in active_lags:
        shift = s - (n - 1)
        g = np.zeros(n)
        if shift >= 0:
            end1 = n - shift
            g[:end1] += 1.0 - h[shift:shift + end1]
        else:
            start1 = -shift
            g[start1:] += 1.0 - h[:n - start1]
        if shift >= 0:
            g[shift:] -= h[:n - shift]
        else:
            end2 = n + shift
            g[:end2] -= h[-shift:-shift + end2]
        grad += g
    grad *= dx / len(active_lags)
    return grad


def get_active_lags(corr, tol=1e-10):
    max_c = np.max(corr)
    return np.where(corr >= max_c - tol)[0].tolist()


def project(h):
    n = len(h)
    target = n / 2.0
    lo, hi = float(np.min(h)) - 2.0, float(np.max(h)) + 2.0
    for _ in range(80):
        mu = (lo + hi) / 2.0
        s = np.sum(np.clip(h - mu, 0.0, 1.0))
        if s > target:
            lo = mu
        else:
            hi = mu
    return np.clip(h - (lo + hi) / 2.0, 0.0, 1.0)


def upsample(h, new_n):
    x_old = np.linspace(0, 1, len(h))
    x_new = np.linspace(0, 1, new_n)
    return project(np.interp(x_new, x_old, h))


# ---------------------------------------------------------------------------
# Subgradient with multiple step strategies
# ---------------------------------------------------------------------------

def subgradient_run(h0, max_iters, step_mode="polyak",
                    f_lower=0.379, max_step=0.01, step0=0.001,
                    label="", log_every=50000, verbose=True):
    h = h0.copy()
    best_score = score_fft(h)
    best_h = h.copy()
    h_avg = h.copy()
    avg_count = 0
    t0 = time.time()
    improved = 0
    stall = 0

    for it in range(max_iters):
        corr = compute_corr(h)
        f_cur = float(np.max(corr))
        active = get_active_lags(corr, tol=1e-10)
        g = compute_subgradient(h, active)
        gnorm2 = np.dot(g, g)

        if step_mode == "polyak" and gnorm2 > 1e-30:
            step = max(f_cur - f_lower, 1e-15) / gnorm2
            step = min(step, max_step)
        elif step_mode == "normalized":
            gnorm = np.sqrt(gnorm2) if gnorm2 > 1e-30 else 1.0
            step = step0 / np.sqrt(1.0 + it)
            g = g / gnorm  # normalize direction
        elif step_mode == "diminishing":
            step = step0 / np.sqrt(1.0 + it)
        else:
            step = step0

        h = project(h - step * g)
        sc = score_fft(h)
        if sc < best_score:
            best_score = sc
            best_h = h.copy()
            improved += 1
            stall = 0
        else:
            stall += 1

        avg_count += 1
        h_avg += (h - h_avg) / avg_count

        if (it + 1) % 10000 == 0:
            sc_avg = score_fft(project(h_avg))
            if sc_avg < best_score:
                best_score = sc_avg
                best_h = project(h_avg.copy())
                improved += 1
                stall = 0

        if verbose and (it + 1) % log_every == 0:
            el = time.time() - t0
            print(f"  [{label:40s}] {it+1:>7d}: f={f_cur:.12f} best={best_score:.14f} "
                  f"act={len(active):>3d} t={el:.0f}s", flush=True)

        if stall > min(max_iters // 2, 100000) and it > 50000:
            break

    el = time.time() - t0
    if verbose:
        print(f"  [{label:40s}] DONE best={best_score:.14f} improv={improved} t={el:.0f}s",
              flush=True)
    return best_score, best_h


# ---------------------------------------------------------------------------
# Parametric step-function family
# ---------------------------------------------------------------------------

def make_step_function(n, left_start, right_end, transition_width=0):
    """Create indicator of [left_start, right_end] on [0,2) with smooth edges.

    left_start, right_end in [0, 2).
    transition_width: width of smooth sigmoid transition (0 = sharp).
    """
    x = np.linspace(0, 2, n, endpoint=False)
    if transition_width < 1e-10:
        h = ((x >= left_start) & (x < right_end)).astype(float)
    else:
        # Sigmoid transitions
        h = (1 / (1 + np.exp(-(x - left_start) / transition_width)) *
             1 / (1 + np.exp((x - right_end) / transition_width)))
    return project(h)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    T0 = time.time()
    print("=" * 70, flush=True)
    print("Erdős Minimum Overlap — Multi-strategy Optimization", flush=True)
    print("=" * 70, flush=True)

    SOTA = 0.3808703105862199
    print(f"SOTA:   {SOTA:.16f}", flush=True)
    print(f"Target: {SOTA - 1e-6:.16f}", flush=True)

    # Load SOTA
    sota_path = "/Users/jmsung/projects/einstein/cb/results/problem-1-erdos-overlap/sota_jsagent_n600.json"
    with open(sota_path) as f:
        h_sota = np.array(json.load(f)["values"])
    sc_sota = score_fft(h_sota)
    print(f"SOTA: n={len(h_sota)}, score={sc_sota:.16f}", flush=True)

    overall_best = sc_sota
    overall_best_h = h_sota.copy()

    # ===================================================================
    # Phase 1: Parametric search over step functions at n=600
    # ===================================================================
    n = 600
    print(f"\n=== Phase 1: Parametric step functions at n={n} ===", flush=True)

    # The SOTA is roughly h=1 for [~0.42, ~1.58] with smooth edges
    # Search over (left_start, right_end, transition_width) triples

    best_param = None
    for ls in np.arange(0.05, 0.70, 0.02):
        re = 2.0 - ls  # Symmetric
        for tw in [0, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2]:
            h = make_step_function(n, ls, re, tw)
            sc = score_fft(h)
            if sc < overall_best:
                overall_best = sc
                overall_best_h = h.copy()
                best_param = (ls, re, tw)
                print(f"  NEW BEST: {sc:.14f} ls={ls:.2f} re={re:.2f} tw={tw:.2f}",
                      flush=True)

    # Also try asymmetric
    for ls in np.arange(0.10, 0.60, 0.05):
        for re in np.arange(1.40, 1.90, 0.05):
            for tw in [0, 0.05, 0.1, 0.2]:
                h = make_step_function(n, ls, re, tw)
                sc = score_fft(h)
                if sc < overall_best:
                    overall_best = sc
                    overall_best_h = h.copy()
                    best_param = (ls, re, tw)
                    print(f"  NEW BEST: {sc:.14f} ls={ls:.2f} re={re:.2f} tw={tw:.2f}",
                          flush=True)

    print(f"Phase 1 best: {overall_best:.14f} params={best_param}", flush=True)

    # ===================================================================
    # Phase 2: Refine best parametric with subgradient at n=600
    # ===================================================================
    print(f"\n=== Phase 2: Subgradient refinement at n={n} ===", flush=True)

    configs = [
        ("polyak", dict(f_lower=0.379, max_step=0.001)),
        ("polyak", dict(f_lower=0.379, max_step=0.01)),
        ("polyak", dict(f_lower=0.375, max_step=0.01)),
        ("polyak", dict(f_lower=0.38, max_step=0.001)),
        ("normalized", dict(step0=0.01)),
        ("normalized", dict(step0=0.001)),
        ("diminishing", dict(step0=0.01)),
        ("diminishing", dict(step0=0.001)),
    ]

    for mode, params in configs:
        label = f"refine600/{mode}/{list(params.values())[0]}"
        sc, h = subgradient_run(
            overall_best_h, max_iters=200000, step_mode=mode,
            label=label, log_every=50000, **params,
        )
        if sc < overall_best:
            overall_best = sc
            overall_best_h = h.copy()
            print(f"  *** NEW BEST: {overall_best:.14f} ***", flush=True)

    print(f"Phase 2 best: {overall_best:.14f}", flush=True)

    # ===================================================================
    # Phase 3: Search over many n values with subgradient
    # ===================================================================
    print(f"\n=== Phase 3: Search over n values ===", flush=True)

    # For each n, create the best parametric start and optimize
    for n_try in [300, 400, 500, 550, 580, 590, 595, 598, 600, 602, 605,
                  610, 620, 650, 700, 800, 900, 1000, 1200]:
        # Grid search for best parametric start at this n
        best_n = float('inf')
        best_h_n = None
        for ls in np.arange(0.10, 0.60, 0.05):
            re = 2.0 - ls
            for tw in [0, 0.05, 0.1, 0.2]:
                h = make_step_function(n_try, ls, re, tw)
                sc = score_fft(h)
                if sc < best_n:
                    best_n = sc
                    best_h_n = h.copy()

        print(f"  n={n_try:5d}: param_best={best_n:.14f}", flush=True, end="")

        # Subgradient refinement
        sc, h = subgradient_run(
            best_h_n, max_iters=200000, step_mode="polyak",
            f_lower=0.379, max_step=0.01,
            label=f"n{n_try}", log_every=100000, verbose=False,
        )
        print(f" -> refined={sc:.14f}", flush=True)

        if sc < overall_best:
            overall_best = sc
            overall_best_h = h.copy()
            print(f"  *** NEW BEST: {overall_best:.14f} at n={n_try} ***", flush=True)

    print(f"Phase 3 best: {overall_best:.14f}", flush=True)

    # ===================================================================
    # Phase 4: Extended subgradient from multiple starts at best n
    # ===================================================================
    n_best = len(overall_best_h)
    print(f"\n=== Phase 4: Extended runs at best n={n_best} ===", flush=True)

    # Try more starting points at the best n
    rng = np.random.default_rng(42)
    for trial in range(20):
        # Random start
        h0 = project(rng.random(n_best))
        sc0 = score_fft(h0)

        sc, h = subgradient_run(
            h0, max_iters=300000, step_mode="polyak",
            f_lower=0.379, max_step=0.01,
            label=f"rand_trial{trial}/n{n_best}", log_every=100000,
        )
        if sc < overall_best:
            overall_best = sc
            overall_best_h = h.copy()
            print(f"  *** NEW BEST: {overall_best:.14f} ***", flush=True)

    # Step function starts with variations
    for ls_offset in np.arange(-0.05, 0.06, 0.01):
        for tw in [0, 0.03, 0.07, 0.12, 0.18]:
            ls = 0.42 + ls_offset
            re = 2.0 - ls
            h0 = make_step_function(n_best, ls, re, tw)
            sc, h = subgradient_run(
                h0, max_iters=200000, step_mode="polyak",
                f_lower=0.379, max_step=0.01,
                label=f"step_ls{ls:.2f}_tw{tw}/n{n_best}",
                log_every=100000, verbose=False,
            )
            if sc < overall_best:
                overall_best = sc
                overall_best_h = h.copy()
                print(f"  *** NEW BEST: {overall_best:.14f} "
                      f"ls={ls:.2f} tw={tw} ***", flush=True)

    print(f"Phase 4 best: {overall_best:.14f}", flush=True)

    # ===================================================================
    # Phase 5: Very long subgradient runs from best
    # ===================================================================
    print(f"\n=== Phase 5: Very long runs from best ===", flush=True)

    for mode, params in [
        ("polyak", dict(f_lower=0.3805, max_step=0.001)),
        ("polyak", dict(f_lower=0.38, max_step=0.001)),
        ("normalized", dict(step0=0.001)),
        ("diminishing", dict(step0=0.001)),
    ]:
        label = f"long/{mode}/{list(params.values())[0]}"
        sc, h = subgradient_run(
            overall_best_h, max_iters=500000, step_mode=mode,
            label=label, log_every=100000, **params,
        )
        if sc < overall_best:
            overall_best = sc
            overall_best_h = h.copy()
            print(f"  *** NEW BEST: {overall_best:.14f} ***", flush=True)

    # ===================================================================
    # Final
    # ===================================================================
    print(f"\n{'='*70}", flush=True)
    print("FINAL RESULTS", flush=True)
    print(f"{'='*70}", flush=True)

    exact = score_h(overall_best_h)
    print(f"Best (FFT):   {overall_best:.16f}", flush=True)
    print(f"Best (exact): {exact:.16f}", flush=True)
    print(f"SOTA:         {SOTA:.16f}", flush=True)
    print(f"Improvement:  {SOTA - exact:.2e}", flush=True)
    print(f"Solution n:   {len(overall_best_h)}", flush=True)
    print(f"Total time:   {time.time() - T0:.0f}s", flush=True)

    out_dir = "/Users/jmsung/projects/einstein/cb/results"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "subgradient_best.json")
    with open(out_path, 'w') as f:
        json.dump({"values": overall_best_h.tolist()}, f)
    print(f"Saved to {out_path}", flush=True)

    if exact < SOTA - 1e-6:
        print("\n>>> SUCCESS: Beat SOTA by >= 1e-6! <<<", flush=True)
    else:
        print("\nDid not beat SOTA by 1e-6.", flush=True)


if __name__ == "__main__":
    main()
