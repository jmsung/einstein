"""High-resolution discretization optimizer for Erdős Minimum Overlap (P1).

Interpolates the SOTA n=600 solution to various resolutions (higher and lower)
and runs dyadic mass transport optimization at each resolution.

Approach:
  - Higher n (1200, 2400, 4800): finer grids may unlock smoother optimization basins
  - Lower n (100, 200, 300): coarser grids may have different local optima
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import fftconvolve

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))
from einstein.erdos.fast import fast_evaluate

SOLUTION_PATH = (
    PROJECT_ROOT
    / ".mb/knowledge/problem-1-erdos-overlap/solutions/solution-best.json"
)
RESULTS_DIR = PROJECT_ROOT / "results/problem-1-erdos-overlap"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

SOTA_SCORE = 0.3808703105862199
TARGET_RESOLUTIONS = [100, 200, 300, 1200, 2400, 4800]
TIME_PER_N = 300  # 5 minutes per resolution
TOTAL_TIMEOUT = 30 * 60  # 30 minutes total


def load_sota() -> np.ndarray:
    """Load the SOTA n=600 solution."""
    with open(SOLUTION_PATH) as f:
        data = json.load(f)
    return np.array(data["data"]["values"], dtype=np.float64)


def interpolate_to_n(h_src: np.ndarray, target_n: int) -> np.ndarray:
    """Interpolate solution to a different resolution."""
    src_n = len(h_src)
    # Map to [0, 1] parameter space
    x_src = np.linspace(0, 1, src_n, endpoint=False) + 0.5 / src_n
    x_tgt = np.linspace(0, 1, target_n, endpoint=False) + 0.5 / target_n

    # Use cubic interpolation for upsampling, linear for downsampling
    kind = "cubic" if target_n > src_n else "linear"
    interp_func = interp1d(x_src, h_src, kind=kind, fill_value="extrapolate")
    h_new = interp_func(x_tgt)

    # Iterative clip-and-normalize to ensure all values in [0, 1] with sum = n/2.
    # After clipping, the sum changes, so re-normalize. Repeat until stable.
    target_sum = target_n / 2.0
    for _ in range(100):
        h_new = np.clip(h_new, 0.0, 1.0)
        current_sum = np.sum(h_new)
        if current_sum == 0:
            break
        h_new *= target_sum / current_sum
        # Check convergence: all in [0,1] and sum correct
        if np.all(h_new >= 0) and np.all(h_new <= 1.0):
            break
    # Final safety clip — distribute excess uniformly across non-saturated entries
    h_new = np.clip(h_new, 0.0, 1.0)
    deficit = target_sum - np.sum(h_new)
    if abs(deficit) > 1e-12:
        # Add deficit uniformly to entries that have room
        room = 1.0 - h_new
        total_room = np.sum(room)
        if total_room > abs(deficit):
            h_new += deficit * (room / total_room)
            h_new = np.clip(h_new, 0.0, 1.0)

    return h_new


def dyadic_mass_transport(
    h: np.ndarray, time_limit: float, seed: int = 42
) -> tuple[np.ndarray, float]:
    """Dyadic pairwise mass transport optimization.

    Pick random pairs (i, j), try h[i] += step, h[j] -= step (sum preserved),
    accept if score improves. Step size = 2^-32.
    """
    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    improved_count = 0
    total_iters = 0
    step = 2**-32  # ~2.3e-10

    t0 = time.time()
    last_report = t0

    while time.time() - t0 < time_limit:
        # Batch of iterations
        for _ in range(10_000):
            total_iters += 1
            i = rng.integers(n)
            j = rng.integers(n)
            if i == j:
                continue

            # Try +step on i, -step on j
            new_i = h[i] + step
            new_j = h[j] - step
            if new_i > 1.0 or new_j < 0.0:
                # Try reverse direction
                new_i = h[i] - step
                new_j = h[j] + step
                if new_i < 0.0 or new_j > 1.0:
                    continue

            old_i, old_j = h[i], h[j]
            h[i], h[j] = new_i, new_j
            score = fast_evaluate(h)
            if score < best_score:
                best_score = score
                improved_count += 1
            else:
                h[i], h[j] = old_i, old_j

        # Progress report every 30s
        now = time.time()
        if now - last_report > 30:
            elapsed = now - t0
            print(
                f"    [{elapsed:.0f}s] iters={total_iters}, "
                f"best={best_score:.16f}, improvements={improved_count}"
            )
            last_report = now

    return h, best_score


def four_point_transport(
    h: np.ndarray, time_limit: float, seed: int = 123
) -> tuple[np.ndarray, float]:
    """4-point coordinated mass transport.

    Pick 4 random indices, redistribute small amounts among them
    while keeping the sum fixed.
    """
    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    improved_count = 0
    total_iters = 0
    step = 2**-32

    t0 = time.time()
    last_report = t0

    while time.time() - t0 < time_limit:
        for _ in range(5_000):
            total_iters += 1
            idx = rng.choice(n, size=4, replace=False)
            # Random zero-sum perturbation
            delta = rng.standard_normal(4)
            delta -= delta.mean()
            delta *= step / max(abs(delta.max()), abs(delta.min()), 1e-30)

            old_vals = h[idx].copy()
            new_vals = old_vals + delta
            if np.any(new_vals < 0) or np.any(new_vals > 1):
                continue

            h[idx] = new_vals
            score = fast_evaluate(h)
            if score < best_score:
                best_score = score
                improved_count += 1
            else:
                h[idx] = old_vals

        now = time.time()
        if now - last_report > 30:
            elapsed = now - t0
            print(
                f"    [{elapsed:.0f}s] iters={total_iters}, "
                f"best={best_score:.16f}, improvements={improved_count}"
            )
            last_report = now

    return h, best_score


def multi_scale_search(
    h: np.ndarray, time_limit: float, seed: int = 77
) -> tuple[np.ndarray, float]:
    """Multi-scale random local search with varying step sizes."""
    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    improved_count = 0
    total_iters = 0

    # Multiple step scales
    scales = [2**-k for k in range(20, 40)]  # 2^-20 to 2^-39

    t0 = time.time()
    last_report = t0

    while time.time() - t0 < time_limit:
        for _ in range(5_000):
            total_iters += 1
            scale = rng.choice(scales)
            n_pts = rng.choice([2, 3, 4])
            idx = rng.choice(n, size=n_pts, replace=False)
            delta = rng.standard_normal(n_pts) * scale
            delta -= delta.mean()  # zero-sum

            old_vals = h[idx].copy()
            new_vals = old_vals + delta
            if np.any(new_vals < 0) or np.any(new_vals > 1):
                continue

            h[idx] = new_vals
            score = fast_evaluate(h)
            if score < best_score:
                best_score = score
                improved_count += 1
            else:
                h[idx] = old_vals

        now = time.time()
        if now - last_report > 30:
            elapsed = now - t0
            print(
                f"    [{elapsed:.0f}s] iters={total_iters}, "
                f"best={best_score:.16f}, improvements={improved_count}"
            )
            last_report = now

    return h, best_score


def save_solution(h: np.ndarray, score: float, tag: str):
    """Save solution to results directory."""
    out = {
        "values": h.tolist(),
        "score": score,
        "n": len(h),
        "tag": tag,
    }
    path = RESULTS_DIR / f"high_res_{tag}_n{len(h)}.json"
    with open(path, "w") as f:
        json.dump(out, f)
    print(f"  Saved to {path}")


def main():
    global_start = time.time()
    print("=" * 70)
    print("High-Resolution Discretization Optimizer for Erdős Minimum Overlap")
    print(f"SOTA score: {SOTA_SCORE:.16f} (n=600)")
    print(f"Target: beat by at least 1e-6 -> need < {SOTA_SCORE - 1e-6:.16f}")
    print("=" * 70)

    # Load SOTA
    h_sota = load_sota()
    verify_score = fast_evaluate(h_sota)
    print(f"\nVerified SOTA score: {verify_score:.16f}")

    results = {}

    for target_n in TARGET_RESOLUTIONS:
        elapsed = time.time() - global_start
        if elapsed > TOTAL_TIMEOUT - 60:
            print(f"\nGlobal timeout approaching, skipping n={target_n}")
            break

        remaining_global = TOTAL_TIMEOUT - elapsed
        time_budget = min(TIME_PER_N, remaining_global - 30)
        if time_budget < 30:
            print(f"\nNot enough time for n={target_n}, skipping")
            break

        print(f"\n{'='*70}")
        print(f"Resolution n={target_n} (time budget: {time_budget:.0f}s)")
        print("=" * 70)

        # Interpolate
        h_interp = interpolate_to_n(h_sota, target_n)
        interp_score = fast_evaluate(h_interp)
        print(f"  Interpolated score: {interp_score:.16f}")

        if interp_score == float("inf"):
            print("  ERROR: Invalid interpolation, skipping")
            results[target_n] = {"interp": float("inf"), "best": float("inf")}
            continue

        best_h = h_interp.copy()
        best_score = interp_score

        # Allocate time: 40% dyadic, 30% four-point, 30% multi-scale
        t_dyadic = time_budget * 0.4
        t_four = time_budget * 0.3
        t_multi = time_budget * 0.3

        # 1. Dyadic mass transport
        print(f"\n  [1/3] Dyadic mass transport ({t_dyadic:.0f}s)...")
        h_opt, score = dyadic_mass_transport(h_interp.copy(), t_dyadic, seed=42)
        if score < best_score:
            best_score = score
            best_h = h_opt
            print(f"  -> Improved to {best_score:.16f}")

        # 2. Four-point transport (start from best so far)
        print(f"\n  [2/3] Four-point transport ({t_four:.0f}s)...")
        h_opt, score = four_point_transport(best_h.copy(), t_four, seed=123)
        if score < best_score:
            best_score = score
            best_h = h_opt
            print(f"  -> Improved to {best_score:.16f}")

        # 3. Multi-scale search (start from best so far)
        print(f"\n  [3/3] Multi-scale search ({t_multi:.0f}s)...")
        h_opt, score = multi_scale_search(best_h.copy(), t_multi, seed=77)
        if score < best_score:
            best_score = score
            best_h = h_opt
            print(f"  -> Improved to {best_score:.16f}")

        results[target_n] = {
            "interp": interp_score,
            "best": best_score,
            "delta_from_sota": best_score - SOTA_SCORE,
        }

        # Save if this is an improvement
        save_solution(best_h, best_score, f"opt")
        print(f"\n  Final for n={target_n}: {best_score:.16f} "
              f"(delta from SOTA: {best_score - SOTA_SCORE:+.2e})")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'n':>6} | {'Interpolated':>20} | {'Optimized':>20} | {'Delta from SOTA':>16}")
    print("-" * 70)
    for n, r in sorted(results.items()):
        interp_str = f"{r['interp']:.16f}" if r['interp'] != float('inf') else "inf"
        best_str = f"{r['best']:.16f}" if r['best'] != float('inf') else "inf"
        delta_str = f"{r.get('delta_from_sota', float('inf')):+.2e}"
        print(f"{n:>6} | {interp_str:>20} | {best_str:>20} | {delta_str:>16}")

    print(f"\nSOTA reference: {SOTA_SCORE:.16f}")
    beat_threshold = SOTA_SCORE - 1e-6
    any_beat = any(
        r["best"] < beat_threshold
        for r in results.values()
        if r["best"] != float("inf")
    )
    if any_beat:
        print("*** FOUND SOLUTION THAT BEATS SOTA! ***")
    else:
        print("No resolution beat SOTA by the required margin.")

    total_time = time.time() - global_start
    print(f"\nTotal time: {total_time:.0f}s")


if __name__ == "__main__":
    main()
