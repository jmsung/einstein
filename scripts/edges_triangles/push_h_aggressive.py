"""P13 push: Aggressive BH with diverse perturbation strategies.

Strategies:
  A. Log-gap noise (what we've been using)
  B. Block-shuffle: randomly permute gaps in a contiguous window
  C. Scallop-local redistribution: uniformly redistribute within one scallop
  D. Add/remove+re-insert random points
  E. Adjacent-pair swap

Runs many seeds (60+) with all 5 strategies. Uses bounded L-BFGS as local minimizer.
"""

import json
import shutil
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from push_d_torch_lbfgs import load_xs_from_solution  # noqa: E402
from push_g_bounded import lbfgs_polish_bounded, save_solution, true_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")
X_LO, X_HI = 0.5, 0.95


def perturb_log_gaps(multi_xs, noise, rng):
    gaps = np.empty(len(multi_xs) + 1)
    gaps[0] = multi_xs[0] - X_LO
    gaps[1:-1] = np.diff(multi_xs)
    gaps[-1] = X_HI - multi_xs[-1]
    gaps = np.maximum(gaps, 1e-15)
    log_gaps = np.log(gaps) + rng.normal(0, noise, size=len(gaps))
    new_gaps = np.exp(log_gaps)
    new_gaps = new_gaps / new_gaps.sum() * (X_HI - X_LO)
    new_multi = X_LO + np.cumsum(new_gaps[:-1])
    return np.sort(np.clip(new_multi, X_LO + 1e-14, X_HI - 1e-14))


def perturb_block_shuffle(multi_xs, win_size, rng):
    """Shuffle gaps within a random window of size win_size."""
    m = len(multi_xs)
    if win_size >= m - 2:
        return multi_xs.copy()
    start = rng.integers(1, m - win_size - 1)
    gaps = np.diff(np.concatenate([[X_LO], multi_xs, [X_HI]]))
    # Shuffle the gaps in window [start, start+win_size]
    window_gaps = gaps[start:start + win_size].copy()
    rng.shuffle(window_gaps)
    new_gaps = gaps.copy()
    new_gaps[start:start + win_size] = window_gaps
    new_multi = X_LO + np.cumsum(new_gaps[:-1])
    return np.sort(np.clip(new_multi, X_LO + 1e-14, X_HI - 1e-14))


def perturb_scallop_redistribute(multi_xs, scallop_k, rng, noise=0.3):
    """Randomly redistribute points within a specific scallop."""
    k = scallop_k
    lo, hi = 1 - 1/k + 1e-10, 1 - 1/(k+1) - 1e-10
    mask = (multi_xs >= lo) & (multi_xs <= hi)
    n_in = mask.sum()
    if n_in < 2:
        return multi_xs.copy()
    # Generate new xs uniformly in [lo, hi] with noise
    new_xs = rng.uniform(lo, hi, size=n_in)
    # Perturb to favor clustering by sorting
    new_xs.sort()
    result = multi_xs.copy()
    result[mask] = new_xs
    return np.sort(result)


def perturb_point_move(multi_xs, n_moves, rng):
    """Move n_moves random points to new positions in a nearby scallop or far region."""
    result = multi_xs.copy()
    for _ in range(n_moves):
        idx = rng.integers(0, len(result))
        # Move to a random position in [0.5, 0.95]
        result[idx] = rng.uniform(X_LO + 1e-10, X_HI - 1e-10)
    return np.sort(result)


def perturb_adjacent_pair_swap_or_replace(multi_xs, n_swaps, rng):
    """Pick a random pair, replace with two points spanning their midpoint."""
    result = multi_xs.copy()
    for _ in range(n_swaps):
        i = rng.integers(0, len(result) - 1)
        mid = (result[i] + result[i+1]) / 2
        spread = (result[i+1] - result[i]) * 0.4
        result[i] = mid - spread
        result[i+1] = mid + spread
    return np.sort(np.clip(result, X_LO + 1e-14, X_HI - 1e-14))


def try_perturbation(
    multi, bi_xs, strategy: str, params: dict, rng,
) -> tuple[np.ndarray, float] | None:
    if strategy == "log_gap":
        pert = perturb_log_gaps(multi, params["noise"], rng)
    elif strategy == "block_shuffle":
        pert = perturb_block_shuffle(multi, params["win"], rng)
    elif strategy == "scallop_redist":
        pert = perturb_scallop_redistribute(multi, params["k"], rng)
    elif strategy == "point_move":
        pert = perturb_point_move(multi, params["n"], rng)
    elif strategy == "pair_swap":
        pert = perturb_adjacent_pair_swap_or_replace(multi, params["n"], rng)
    else:
        return None
    try:
        polished, _ = lbfgs_polish_bounded(pert, bi_xs, max_rounds=30)
        sc = true_score(bi_xs, polished)
        return polished, sc
    except Exception:
        return None


def main():
    bi_xs, multi_xs = load_xs_from_solution(RESULTS / "solution.json")
    init_score = true_score(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f}")

    best_multi = multi_xs.copy()
    best_score = init_score

    # Initial polish
    polished, _ = lbfgs_polish_bounded(multi_xs, bi_xs, max_rounds=60)
    psc = true_score(bi_xs, polished)
    print(f"Polish : {psc:.14f}  delta={psc-init_score:+.2e}")
    if psc > best_score:
        best_multi = polished.copy()
        best_score = psc

    # Diverse perturbations
    strategies = []
    # A: wide range of log-gap noise
    for noise in [0.5, 0.35, 0.25, 0.18, 0.13, 0.1, 0.07, 0.05, 0.03, 0.02, 0.015, 0.01]:
        strategies.append(("log_gap", {"noise": noise}))
    # B: block shuffle various window sizes
    for w in [3, 5, 10, 20, 40]:
        strategies.append(("block_shuffle", {"win": w}))
    # C: scallop-local redistribution
    for k in [2, 3, 4, 5, 6, 8, 12]:
        strategies.append(("scallop_redist", {"k": k}))
    # D: point move
    for n in [1, 3, 5, 10]:
        strategies.append(("point_move", {"n": n}))
    # E: pair swap
    for n in [1, 5, 10, 25]:
        strategies.append(("pair_swap", {"n": n}))

    print(f"\n=== Aggressive BH ({len(strategies)} strategies) ===")

    N_SEEDS = 40
    t0 = time.time()
    n_improvements = 0
    improvements = []

    for seed in range(N_SEEDS):
        rng = np.random.default_rng(seed * 91 + 17)
        for strategy, params in strategies:
            if time.time() - t0 > 900:
                print(f"\n[time limit] break at seed={seed}")
                break
            res = try_perturbation(best_multi, bi_xs, strategy, params, rng)
            if res is None:
                continue
            new_multi, sc = res
            if sc > best_score + 1e-13:
                best_multi = new_multi.copy()
                best_score = sc
                n_improvements += 1
                improvements.append((strategy, params, sc))
                print(f"  seed={seed:2d} {strategy:<15} {params}: {sc:.14f} (+{sc-init_score:.3e})")
        else:
            continue
        break

    elapsed = time.time() - t0
    print(f"\nDone. {n_improvements} improvements in {elapsed:.0f}s")
    print(f"Initial: {init_score:.14f}")
    print(f"Final  : {best_score:.14f}")
    print(f"Gain   : {best_score - init_score:+.3e}")

    # Strategy effectiveness
    if improvements:
        from collections import Counter
        strat_counts = Counter(s for s, _, _ in improvements)
        print("\nStrategy win counts:")
        for s, c in strat_counts.most_common():
            print(f"  {s}: {c}")

    if best_score > init_score + 1e-12:
        save_solution(bi_xs, best_multi, "push-h-final")
        print("\n** IMPROVED — saved")


if __name__ == "__main__":
    main()
