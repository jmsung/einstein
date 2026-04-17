"""Multi-n discretization optimizer for Erdos Minimum Overlap (Problem 1).

Explores whether different discretization sizes n can beat the n=600 SOTA.

Strategy:
  1. Interpolate SOTA (n=600) to each target n using cubic interpolation
  2. Re-normalize and polish with mass-transport local search
  3. For the best n, run a longer polishing session
  4. Try round-trip: optimize at other n, then downsample back to n=600

Usage:
    cd /Users/jmsung/projects/einstein/cb-feat-auto-p1
    uv run python3 scripts/erdos/multi_n_optimizer.py
"""

import json
import sys
import time

import numpy as np
from scipy.interpolate import interp1d

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

SOTA_PATH = "/tmp/p1_sota.json"
OUTPUT_PATH = "/tmp/p1_multi_n_best.json"

# Target discretization sizes to explore
TARGET_NS = [
    400, 500, 550, 580, 590, 595, 598, 599,
    600,
    601, 602, 605, 610, 620, 650, 700, 800, 1000, 1200,
]


def load_sota() -> tuple[np.ndarray, float]:
    """Load the SOTA solution (n=600) from disk."""
    with open(SOTA_PATH) as f:
        data = json.load(f)
    h = np.array(data["values"], dtype=np.float64)
    score = fast_evaluate(h)
    print(f"SOTA loaded: n={len(h)}, score={score:.16f}")
    return h, score


def project_to_feasible(h: np.ndarray) -> np.ndarray:
    """Project h onto the feasible set: h in [0,1], sum(h) = n/2.

    Uses iterative clipping + redistribution to ensure both box constraints
    and the sum constraint are satisfied simultaneously. This is essentially
    a Dykstra-style alternating projection.
    """
    n = len(h)
    target = n / 2.0
    h = h.copy()

    for _ in range(100):  # converges in a few iterations
        h = np.clip(h, 0.0, 1.0)
        current_sum = np.sum(h)
        if current_sum == 0:
            h[:] = 0.5
            return h

        deficit = target - current_sum
        if abs(deficit) < 1e-14:
            break

        # Distribute deficit among indices that have room
        if deficit > 0:
            # Need to increase: only increase values below 1
            free = h < 1.0
            n_free = np.sum(free)
            if n_free == 0:
                break
            room = 1.0 - h[free]
            total_room = np.sum(room)
            if total_room <= deficit:
                h[free] = 1.0
            else:
                h[free] += deficit * (room / total_room)
        else:
            # Need to decrease: only decrease values above 0
            free = h > 0.0
            n_free = np.sum(free)
            if n_free == 0:
                break
            room = h[free]
            total_room = np.sum(room)
            if total_room <= -deficit:
                h[free] = 0.0
            else:
                h[free] += deficit * (room / total_room)

    return h


def interpolate_to_n(h_source: np.ndarray, target_n: int) -> np.ndarray:
    """Interpolate a solution to a new discretization size using cubic splines.

    Uses scipy.interpolate.interp1d with cubic method for high-quality
    resampling, then projects onto the feasible set [0,1] with sum = n/2.
    """
    source_n = len(h_source)
    if source_n == target_n:
        return h_source.copy()

    # Map to [0, 1] domain
    x_source = np.linspace(0, 1, source_n)
    x_target = np.linspace(0, 1, target_n)

    # Cubic interpolation (fill_value="extrapolate" for edge robustness)
    interp_func = interp1d(x_source, h_source, kind="cubic", fill_value="extrapolate")
    h_new = interp_func(x_target)

    # Project onto feasible set using iterative clipping + redistribution
    h_new = project_to_feasible(h_new)

    return h_new


def mass_transport_polish(
    h: np.ndarray,
    n_iters: int,
    seed: int = 42,
    delta_scale: float = 1e-7,
    report_every: int = 10_000,
    label: str = "",
) -> tuple[np.ndarray, float]:
    """Polish a solution with zero-sum mass-transport perturbations.

    Picks random pairs/triples of indices, applies zero-sum perturbations,
    and keeps the move only if the fast_evaluate score improves.
    """
    rng = np.random.default_rng(seed)
    h = h.copy()
    n = len(h)
    best_score = fast_evaluate(h)
    best_h = h.copy()
    improved = 0
    t0 = time.time()

    n_points_choices = np.array([2, 3, 4])

    for trial in range(n_iters):
        n_pts = rng.choice(n_points_choices)
        idx = rng.choice(n, size=n_pts, replace=False)
        delta = rng.standard_normal(n_pts) * delta_scale
        delta -= delta.mean()  # zero-sum constraint

        old = h[idx].copy()
        new = old + delta
        if np.any(new < 0) or np.any(new > 1):
            continue

        h[idx] = new
        score = fast_evaluate(h)
        if score < best_score:
            best_score = score
            best_h = h.copy()
            improved += 1
        else:
            h[idx] = old

        if report_every > 0 and (trial + 1) % report_every == 0:
            elapsed = time.time() - t0
            prefix = f"  [{label}] " if label else "  "
            print(
                f"{prefix}iter {trial+1:>8d}/{n_iters}: "
                f"C={best_score:.16f}, improved={improved}, "
                f"time={elapsed:.1f}s"
            )

    return best_h, best_score


def phase1_survey(h_sota: np.ndarray) -> dict:
    """Phase 1: Survey all target n values with short polishing runs.

    Returns dict mapping n -> (best_h, best_score, interpolated_score).
    """
    print("\n" + "=" * 70)
    print("PHASE 1: Survey all discretization sizes (100k iters each)")
    print("=" * 70)

    results = {}
    sota_n = len(h_sota)

    for target_n in TARGET_NS:
        print(f"\n--- n={target_n} ---")
        t0 = time.time()

        # Interpolate
        h_interp = interpolate_to_n(h_sota, target_n)
        interp_score = fast_evaluate(h_interp)
        print(f"  After interpolation: C={interp_score:.16f}")

        if interp_score == float("inf"):
            print(f"  SKIP: invalid after interpolation")
            continue

        # Polish with 100k iterations
        h_polished, polished_score = mass_transport_polish(
            h_interp,
            n_iters=100_000,
            seed=42,
            label=f"n={target_n}",
            report_every=50_000,
        )

        # Verify with exact evaluator
        exact_score = exact_evaluate({"values": h_polished.tolist()})

        elapsed = time.time() - t0
        improvement = interp_score - polished_score
        print(
            f"  Final: C={exact_score:.16f} "
            f"(improvement={improvement:.2e}, time={elapsed:.1f}s)"
        )

        results[target_n] = {
            "h": h_polished,
            "score": exact_score,
            "interp_score": interp_score,
        }

    return results


def phase2_deep_polish(results: dict) -> tuple[int, np.ndarray, float]:
    """Phase 2: Take the best n and run a longer polishing session (500k iters)."""
    print("\n" + "=" * 70)
    print("PHASE 2: Deep polish on the best n (500k iters)")
    print("=" * 70)

    # Find best n
    best_n = min(results, key=lambda n: results[n]["score"])
    best_entry = results[best_n]
    print(f"\nBest n from survey: n={best_n}, C={best_entry['score']:.16f}")

    # Also polish the top 3 to be thorough
    sorted_ns = sorted(results, key=lambda n: results[n]["score"])[:3]
    print(f"Top 3 candidates: {[(n, results[n]['score']) for n in sorted_ns]}")

    overall_best_n = best_n
    overall_best_h = best_entry["h"]
    overall_best_score = best_entry["score"]

    for target_n in sorted_ns:
        entry = results[target_n]
        print(f"\n--- Deep polish n={target_n} (start C={entry['score']:.16f}) ---")

        h_deep, deep_score = mass_transport_polish(
            entry["h"],
            n_iters=500_000,
            seed=123,
            delta_scale=5e-8,
            label=f"deep-n={target_n}",
            report_every=100_000,
        )

        # Verify
        exact_deep = exact_evaluate({"values": h_deep.tolist()})
        print(f"  Deep polish final: C={exact_deep:.16f}")

        if exact_deep < overall_best_score:
            overall_best_score = exact_deep
            overall_best_h = h_deep
            overall_best_n = target_n
            print(f"  ** NEW OVERALL BEST: n={target_n}, C={exact_deep:.16f}")

        # Update results
        results[target_n]["h"] = h_deep
        results[target_n]["score"] = exact_deep

    return overall_best_n, overall_best_h, overall_best_score


def phase3_roundtrip(results: dict, h_sota: np.ndarray) -> tuple[np.ndarray, float]:
    """Phase 3: Try round-trip optimization.

    Optimize at other n values, then downsample back to n=600 and polish.
    This tests whether optimizing at a different resolution and then coming
    back yields a better n=600 solution.
    """
    print("\n" + "=" * 70)
    print("PHASE 3: Round-trip optimization (optimize at n!=600, downsample to 600)")
    print("=" * 70)

    # Pick interesting n values to round-trip through
    roundtrip_ns = [500, 700, 800, 1000, 1200]
    best_rt_h = h_sota.copy()
    best_rt_score = fast_evaluate(h_sota)
    print(f"Starting n=600 score: {best_rt_score:.16f}")

    for src_n in roundtrip_ns:
        if src_n not in results:
            continue

        entry = results[src_n]
        print(f"\n--- Round-trip via n={src_n} (polished C={entry['score']:.16f}) ---")

        # Downsample the polished n=src_n solution back to n=600
        h_back = interpolate_to_n(entry["h"], 600)
        back_score = fast_evaluate(h_back)
        print(f"  After downsample to 600: C={back_score:.16f}")

        if back_score == float("inf"):
            print(f"  SKIP: invalid after downsample")
            continue

        # Polish the downsampled solution
        h_rt_polished, rt_polished_score = mass_transport_polish(
            h_back,
            n_iters=200_000,
            seed=456,
            label=f"rt-from-{src_n}",
            report_every=100_000,
        )

        exact_rt = exact_evaluate({"values": h_rt_polished.tolist()})
        print(f"  After polish: C={exact_rt:.16f}")

        if exact_rt < best_rt_score:
            best_rt_score = exact_rt
            best_rt_h = h_rt_polished
            print(f"  ** NEW BEST n=600 via round-trip: C={exact_rt:.16f}")

    return best_rt_h, best_rt_score


def print_summary(results: dict, best_n: int, best_score: float,
                   best_rt_score: float, sota_score: float):
    """Print a summary table of all results."""
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"{'n':>6} | {'Interp Score':>20} | {'Polished Score':>20} | {'vs SOTA':>12}")
    print("-" * 70)

    for n in sorted(results.keys()):
        entry = results[n]
        diff = entry["score"] - sota_score
        marker = " <-- BEST" if n == best_n else ""
        print(
            f"{n:>6} | {entry['interp_score']:>20.16f} | "
            f"{entry['score']:>20.16f} | {diff:>+12.2e}{marker}"
        )

    print("-" * 70)
    print(f"SOTA (n=600):        {sota_score:.16f}")
    print(f"Best any-n:          {best_score:.16f} (n={best_n})")
    print(f"Best round-trip n=600: {best_rt_score:.16f}")
    print(f"Overall best:        {min(best_score, best_rt_score):.16f}")

    if min(best_score, best_rt_score) < sota_score:
        improvement = sota_score - min(best_score, best_rt_score)
        print(f"\n*** IMPROVEMENT FOUND: {improvement:.2e} ***")
    else:
        print(f"\nNo improvement over SOTA found.")


def main():
    print("=" * 70)
    print("Erdos Minimum Overlap — Multi-n Discretization Explorer")
    print("=" * 70)
    t_start = time.time()

    # Load SOTA
    h_sota, sota_score = load_sota()

    # Phase 1: Survey all n values
    results = phase1_survey(h_sota)

    # Phase 2: Deep polish best candidates
    best_n, best_h, best_score = phase2_deep_polish(results)

    # Phase 3: Round-trip optimization
    best_rt_h, best_rt_score = phase3_roundtrip(results, h_sota)

    # Summary
    print_summary(results, best_n, best_score, best_rt_score, sota_score)

    # Save overall best to JSON
    if best_score <= best_rt_score:
        save_h = best_h
        save_score = best_score
        save_n = best_n
        save_source = f"multi-n survey, n={best_n}"
    else:
        save_h = best_rt_h
        save_score = best_rt_score
        save_n = 600
        save_source = "round-trip optimization to n=600"

    result = {
        "problem": "erdos-minimum-overlap",
        "n_points": save_n,
        "score": float(save_score),
        "values": save_h.tolist(),
        "source": save_source,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "sota_score": sota_score,
        "all_results": {
            str(n): {
                "interp_score": entry["interp_score"],
                "polished_score": entry["score"],
            }
            for n, entry in results.items()
        },
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved best result to {OUTPUT_PATH}")

    elapsed = time.time() - t_start
    print(f"Total time: {elapsed:.0f}s ({elapsed/60:.1f}min)")


if __name__ == "__main__":
    main()
