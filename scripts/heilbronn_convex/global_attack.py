"""Global attack on Heilbronn Convex (P16) — find a new basin.

Uses fundamentally different global optimizers beyond multistart SLSQP:

1. scipy.optimize.differential_evolution — population-based global search
2. scipy.optimize.dual_annealing — simulated annealing with local search
3. Non-10+4 hull structures (9+5, 11+3, 8+6)
4. Crossover between known basins

Usage:
    uv run python scripts/heilbronn_convex/global_attack.py --time 1800 --seed 42
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, dual_annealing
from scipy.spatial import ConvexHull

from einstein.heilbronn_convex import arena_score, fast_score, active_triples, hull_vertex_indices
from einstein.heilbronn_convex.optimizer import polish_slsqp, random_convex_init

RESULTS_DIR = Path("results/problem-16-heilbronn-convex")

# Targets
ARENA_BEST = 0.02783558051755368259
OUR_PREV = 0.02783558045993943589
MIN_IMPROVEMENT = 1e-9
SUBMIT_THRESHOLD = OUR_PREV + MIN_IMPROVEMENT


def load_all_solutions():
    """Load all saved leaderboard solutions."""
    solutions = {}
    for f in RESULTS_DIR.glob("*.json"):
        try:
            data = json.loads(f.read_text())
            pts = np.array(data["points"], dtype=np.float64)
            if pts.shape == (14, 2):
                sc = fast_score(pts)
                solutions[f.stem] = (pts, sc)
        except Exception:
            continue
    return solutions


def neg_score_flat(x):
    """Negative arena score for a flat 28-vector. For minimization."""
    pts = x.reshape(14, 2)
    sc = fast_score(pts)
    if not np.isfinite(sc) or sc < 0:
        return 1e10
    return -sc


def neg_score_arena(x):
    """Negative arena_score (exact) for a flat 28-vector."""
    pts = x.reshape(14, 2)
    sc = arena_score(pts)
    if not np.isfinite(sc) or sc < 0:
        return 1e10
    return -sc


def run_differential_evolution(seed, maxiter=2000, popsize=60, tol=1e-18):
    """Run scipy DE on full 28-dim space."""
    bounds = [(-2.0, 2.0)] * 28
    result = differential_evolution(
        neg_score_flat,
        bounds,
        seed=seed,
        maxiter=maxiter,
        popsize=popsize,
        tol=tol,
        mutation=(0.5, 1.5),
        recombination=0.9,
        strategy="best1bin",
        polish=False,  # we'll polish with SLSQP ourselves
    )
    pts = result.x.reshape(14, 2)
    return pts, -result.fun


def run_dual_annealing(seed, maxiter=5000):
    """Run scipy dual annealing on full 28-dim space."""
    bounds = [(-2.0, 2.0)] * 28
    result = dual_annealing(
        neg_score_flat,
        bounds,
        seed=seed,
        maxiter=maxiter,
        initial_temp=5230.0,
        restart_temp_ratio=2e-5,
        visit=2.62,
        no_local_search=True,  # skip local search, we'll polish ourselves
    )
    pts = result.x.reshape(14, 2)
    return pts, -result.fun


def crossover_solutions(pts_a, pts_b, rng, mode="hull_swap"):
    """Create a crossover offspring from two solutions.

    Modes:
    - hull_swap: take hull from A, interior from B
    - random_mix: randomly assign each point from A or B
    - interpolate: weighted average of A and B
    - interior_swap: take interior from A, hull from B
    """
    hv_a = set(hull_vertex_indices(pts_a))
    hv_b = set(hull_vertex_indices(pts_b))

    if mode == "hull_swap":
        # Hull from A, interior from B
        child = pts_a.copy()
        for i in range(14):
            if i not in hv_a:
                # Map to nearest non-hull point in B
                non_hull_b = [j for j in range(14) if j not in hv_b]
                if non_hull_b:
                    j = rng.choice(non_hull_b)
                    child[i] = pts_b[j]
        return child
    elif mode == "interior_swap":
        child = pts_b.copy()
        for i in range(14):
            if i not in hv_b:
                non_hull_a = [j for j in range(14) if j not in hv_a]
                if non_hull_a:
                    j = rng.choice(non_hull_a)
                    child[i] = pts_a[j]
        return child
    elif mode == "random_mix":
        mask = rng.random(14) > 0.5
        child = np.where(mask[:, None], pts_a, pts_b)
        return child
    elif mode == "interpolate":
        alpha = rng.uniform(0.1, 0.9)
        return alpha * pts_a + (1 - alpha) * pts_b
    return pts_a.copy()


def make_non_standard_init(rng, n_hull):
    """Create initial configs with non-standard hull sizes (not 10+4)."""
    n_int = 14 - n_hull
    # Hull: evenly spaced on unit circle with random perturbation
    angles = np.sort(rng.uniform(0, 2 * np.pi, n_hull))
    radii = rng.uniform(0.85, 1.15, n_hull)
    hull = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])

    # Interior: random within the hull
    if n_int > 0:
        r_int = np.sqrt(rng.uniform(0, 1, n_int)) * 0.6
        theta_int = rng.uniform(0, 2 * np.pi, n_int)
        interior = np.column_stack([r_int * np.cos(theta_int), r_int * np.sin(theta_int)])
        pts = np.vstack([hull, interior])
    else:
        pts = hull

    # Break symmetry
    pts += rng.normal(0, 0.01, pts.shape)
    return pts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=float, default=1800.0, help="Wall time budget (s)")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=str, default="/tmp/heilbronn_global_attack.json")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    start = time.time()

    print(f"Target: {SUBMIT_THRESHOLD:.20f} (our prev + minImprovement)")
    print(f"Arena #1: {ARENA_BEST:.20f}")
    print(f"Need: {SUBMIT_THRESHOLD - ARENA_BEST:.3e} above arena #1")
    print()

    # Load all known solutions for crossover
    solutions = load_all_solutions()
    print(f"Loaded {len(solutions)} reference solutions")
    all_pts = [(name, pts, sc) for name, (pts, sc) in solutions.items()]
    all_pts.sort(key=lambda x: -x[2])
    for name, pts, sc in all_pts[:5]:
        print(f"  {sc:.16f}  {name}")

    best_score = ARENA_BEST
    best_pts = None
    discovered_basins = {}  # binned by score at 1e-10
    phase_stats = {}

    def record(pts, score, phase):
        nonlocal best_score, best_pts
        if not np.isfinite(score) or score < 0.02:
            return
        key = int(round(score * 1e10))
        if key not in discovered_basins or score > discovered_basins[key][0]:
            discovered_basins[key] = (score, pts.copy(), phase)
        if score > best_score:
            best_score = score
            best_pts = pts.copy()
            at = active_triples(pts, rel_tol=1e-9)
            hv = hull_vertex_indices(pts)
            delta = score - ARENA_BEST
            print(f"\n*** NEW BEST! {score:.20f}  delta={delta:+.3e}  "
                  f"hull={len(hv)}+{14-len(hv)}  active={len(at)}  phase={phase}")
            if score > SUBMIT_THRESHOLD:
                print(f"*** ABOVE SUBMIT THRESHOLD! ***")
                # Save immediately
                out = {"points": pts.tolist(), "score": score, "phase": phase}
                Path("/tmp/heilbronn_candidate.json").write_text(json.dumps(out, indent=2))

    # ============================================================
    # Phase 1: Differential Evolution (broad global search)
    # ============================================================
    phase = "DE"
    phase_stats[phase] = 0
    budget_de = min(args.time * 0.3, 600)  # 30% of budget or 10 min max
    print(f"\n{'='*60}")
    print(f"Phase 1: Differential Evolution ({budget_de:.0f}s budget)")
    print(f"{'='*60}")

    de_seeds = rng.integers(0, 2**31, size=20)
    for i, de_seed in enumerate(de_seeds):
        if time.time() - start > budget_de:
            break
        pts_de, score_de = run_differential_evolution(
            seed=int(de_seed), maxiter=1000, popsize=50
        )
        polished, score_pol = polish_slsqp(pts_de, max_iter=500)
        record(polished, score_pol, f"DE-{i}")
        phase_stats[phase] = i + 1
        if (i + 1) % 2 == 0:
            elapsed = time.time() - start
            print(f"  DE round {i+1}: raw={score_de:.10f} polished={score_pol:.16f}  [{elapsed:.0f}s]")

    # ============================================================
    # Phase 2: Dual Annealing (simulated annealing + local search)
    # ============================================================
    phase = "DA"
    phase_stats[phase] = 0
    budget_da = min(args.time * 0.2, 400)
    print(f"\n{'='*60}")
    print(f"Phase 2: Dual Annealing ({budget_da:.0f}s budget)")
    print(f"{'='*60}")

    da_seeds = rng.integers(0, 2**31, size=10)
    for i, da_seed in enumerate(da_seeds):
        if time.time() - start > budget_de + budget_da:
            break
        pts_da, score_da = run_dual_annealing(seed=int(da_seed), maxiter=3000)
        polished, score_pol = polish_slsqp(pts_da, max_iter=500)
        record(polished, score_pol, f"DA-{i}")
        phase_stats[phase] = i + 1
        elapsed = time.time() - start
        print(f"  DA round {i+1}: raw={score_da:.10f} polished={score_pol:.16f}  [{elapsed:.0f}s]")

    # ============================================================
    # Phase 3: Non-standard hull structures (9+5, 11+3, 8+6, etc.)
    # ============================================================
    phase = "non-std-hull"
    phase_stats[phase] = 0
    budget_hull = min(args.time * 0.15, 300)
    print(f"\n{'='*60}")
    print(f"Phase 3: Non-standard hull structures ({budget_hull:.0f}s budget)")
    print(f"{'='*60}")

    hull_sizes = [7, 8, 9, 11, 12, 13, 14]
    trial_count = 0
    for n_hull in hull_sizes:
        n_int = 14 - n_hull
        if time.time() - start > budget_de + budget_da + budget_hull:
            break
        best_for_hull = -np.inf
        for j in range(200):
            if time.time() - start > budget_de + budget_da + budget_hull:
                break
            pts0 = make_non_standard_init(rng, n_hull)
            polished, score_pol = polish_slsqp(pts0, max_iter=400)
            record(polished, score_pol, f"hull-{n_hull}+{n_int}")
            trial_count += 1
            if score_pol > best_for_hull:
                best_for_hull = score_pol
        phase_stats[phase] = trial_count
        print(f"  hull={n_hull}+{n_int}: best={best_for_hull:.16f}")

    # ============================================================
    # Phase 4: Crossover between known basins
    # ============================================================
    phase = "crossover"
    phase_stats[phase] = 0
    budget_xo = min(args.time * 0.1, 200)
    print(f"\n{'='*60}")
    print(f"Phase 4: Crossover between basins ({budget_xo:.0f}s budget)")
    print(f"{'='*60}")

    xo_count = 0
    top_solutions = [(pts, sc) for _, (pts, sc) in solutions.items()]
    top_solutions.sort(key=lambda x: -x[1])
    top_solutions = top_solutions[:10]
    modes = ["hull_swap", "interior_swap", "random_mix", "interpolate"]

    for _ in range(5000):
        if time.time() - start > budget_de + budget_da + budget_hull + budget_xo:
            break
        ia = rng.integers(0, len(top_solutions))
        ib = rng.integers(0, len(top_solutions))
        if ia == ib:
            continue
        mode = rng.choice(modes)
        child = crossover_solutions(top_solutions[ia][0], top_solutions[ib][0], rng, mode)
        # Add small perturbation
        child += rng.normal(0, rng.choice([1e-4, 1e-3, 5e-3, 1e-2]), child.shape)
        polished, score_pol = polish_slsqp(child, max_iter=400)
        record(polished, score_pol, f"xo-{mode}")
        xo_count += 1
    phase_stats[phase] = xo_count
    print(f"  Crossover trials: {xo_count}")

    # ============================================================
    # Phase 5: Massive multistart with truly random starts
    # ============================================================
    phase = "massive-random"
    phase_stats[phase] = 0
    remaining = args.time - (time.time() - start)
    print(f"\n{'='*60}")
    print(f"Phase 5: Massive random multistart ({remaining:.0f}s remaining)")
    print(f"{'='*60}")

    shapes = ["disk", "square", "10p4"]
    random_count = 0
    while time.time() - start < args.time:
        shape = rng.choice(shapes)
        pts0 = random_convex_init(rng, shape=shape)
        polished, score_pol = polish_slsqp(pts0, max_iter=400)
        record(polished, score_pol, f"random-{shape}")
        random_count += 1
        if random_count % 500 == 0:
            elapsed = time.time() - start
            n_basins = len(discovered_basins)
            print(f"  [{random_count:6d}] {elapsed:.0f}s  basins={n_basins}  best={best_score:.16f}")
    phase_stats[phase] = random_count

    # ============================================================
    # Summary
    # ============================================================
    elapsed = time.time() - start
    print(f"\n{'='*60}")
    print(f"SUMMARY after {elapsed:.1f}s")
    print(f"{'='*60}")
    print(f"Best score: {best_score:.20f}")
    print(f"Arena #1:   {ARENA_BEST:.20f}")
    print(f"Threshold:  {SUBMIT_THRESHOLD:.20f}")
    if best_score > ARENA_BEST:
        print(f"Delta vs arena #1: {best_score - ARENA_BEST:+.3e}")
    if best_score > SUBMIT_THRESHOLD:
        print(f"*** ABOVE SUBMIT THRESHOLD! CANDIDATE SAVED TO /tmp/heilbronn_candidate.json ***")
    else:
        print(f"Gap to threshold: {SUBMIT_THRESHOLD - best_score:.3e}")
    print(f"\nPhase stats: {phase_stats}")
    print(f"Discovered basins: {len(discovered_basins)}")

    # Top 10 basins
    sorted_basins = sorted(discovered_basins.values(), key=lambda x: -x[0])[:10]
    print(f"\nTop 10 basins:")
    for i, (sc, pts, ph) in enumerate(sorted_basins):
        hv = hull_vertex_indices(pts)
        at = active_triples(pts, rel_tol=1e-9)
        print(f"  #{i+1}: {sc:.16f}  hull={len(hv)}+{14-len(hv)}  active={len(at)}  phase={ph}")

    # Save results
    out = {
        "best_score": best_score,
        "best_pts": best_pts.tolist() if best_pts is not None else None,
        "arena_best": ARENA_BEST,
        "submit_threshold": SUBMIT_THRESHOLD,
        "above_threshold": best_score > SUBMIT_THRESHOLD,
        "basins_top10": [
            {"score": sc, "points": pts.tolist(), "phase": ph,
             "n_hull": len(hull_vertex_indices(pts)),
             "active_triples": len(active_triples(pts, rel_tol=1e-9))}
            for sc, pts, ph in sorted_basins
        ],
        "stats": phase_stats,
        "elapsed_s": elapsed,
    }
    Path(args.out).write_text(json.dumps(out, indent=2))
    print(f"\nResults saved to {args.out}")


if __name__ == "__main__":
    main()
