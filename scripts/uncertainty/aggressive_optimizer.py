"""Aggressive multi-strategy optimizer to beat RhizomeAgent's 0.318221.

Strategies:
1. CMA-ES with multiple restarts and varying sigma
2. Nelder-Mead from many random perturbations
3. Basin hopping with cluster-aware perturbations
4. Systematic k=14 search (cold-start, not just adding root)
5. Different cluster structure exploration (2+5+6, 4+5+4, etc.)
6. High-precision gradient descent with sign-change tracking
"""
import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from scipy.optimize import minimize, basinhopping, differential_evolution
from einstein.uncertainty.fast import fast_evaluate, solve_coefficients_mp

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

TARGET = 0.318221  # RhizomeAgent's score

BEST_ROOTS_K13 = [
    3.0886658942606733, 4.435156861236376, 6.034127890108831,
    30.945538933257353, 36.84167838791129, 42.20424571337132,
    47.682624801878234, 51.92315504790176, 57.58188043903107,
    100.7501292924569, 115.43881608340484, 123.02406833559513,
    140.04812478845042,
]

# Global best tracking
global_best_score = fast_evaluate(BEST_ROOTS_K13)
global_best_roots = list(BEST_ROOTS_K13)


def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def obj(x, dps=30):
    """Objective function for optimizers."""
    r = sorted(x)
    if any(z <= 0 or z > 300 for z in r):
        return 1e6
    if any(r[i+1] - r[i] < 0.01 for i in range(len(r)-1)):
        return 1e6
    s = fast_evaluate(r, dps=dps)
    return s if np.isfinite(s) else 1e6


def update_best(roots, score, tag):
    global global_best_score, global_best_roots
    if score < global_best_score:
        global_best_score = score
        global_best_roots = list(roots)
        result = {
            "problem": "uncertainty-principle",
            "k": len(roots),
            "score": score,
            "laguerre_double_roots": list(roots),
            "tag": tag,
            "verified": False,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        fname = RESULTS_DIR / f"up_k{len(roots)}_{score:.10f}_{tag}.json"
        with open(fname, "w") as f:
            json.dump(result, f, indent=2)
        log(f"  *** NEW BEST: {score:.16f} ({tag}) ***")
        return True
    return False


def strategy_cmaes_restart(roots, n_restarts=5, max_fevals=2000):
    """CMA-ES with multiple restarts at varying sigma."""
    import cma
    best_score = fast_evaluate(roots)
    best_roots = list(roots)

    for restart in range(n_restarts):
        sigma = np.random.choice([0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5])
        trial = list(roots)
        # Small random perturbation
        for i in range(len(trial)):
            trial[i] += np.random.randn() * sigma * 0.3
        trial.sort()

        k = len(trial)
        opts = cma.CMAOptions()
        opts["maxfevals"] = max_fevals
        opts["tolfun"] = 1e-16
        opts["tolx"] = 1e-14
        opts["verbose"] = -1
        opts["bounds"] = [[0.01]*k, [300.0]*k]
        opts["seed"] = int(time.time() * 1000) % 100000 + restart

        try:
            es = cma.CMAEvolutionStrategy(trial, sigma, opts)
            es.optimize(obj)
            score = es.result.fbest
            if score < best_score:
                best_score = score
                best_roots = sorted(es.result.xbest)
                log(f"    CMA restart {restart}: σ={sigma:.3f} → {score:.16f}")
        except Exception as e:
            log(f"    CMA restart {restart}: FAILED ({e})")

    return best_roots, best_score


def strategy_nelder_mead_multi(roots, n_trials=20):
    """Nelder-Mead from many random perturbations."""
    best_score = fast_evaluate(roots)
    best_roots = list(roots)

    for trial_idx in range(n_trials):
        sigma = np.random.choice([0.001, 0.005, 0.01, 0.05, 0.1])
        trial = [r + np.random.randn() * sigma for r in roots]
        trial.sort()

        if any(z <= 0 or z > 300 for z in trial):
            continue

        res = minimize(obj, trial, method="Nelder-Mead",
                      options={"maxiter": 5000, "xatol": 1e-14, "fatol": 1e-16})
        score = res.fun
        if score < best_score:
            best_score = score
            best_roots = sorted(res.x)
            log(f"    NM trial {trial_idx}: σ={sigma:.3f} → {score:.16f}")

    return best_roots, best_score


def strategy_fine_hillclimb(roots, n_rounds=200):
    """Ultra-fine coordinate hillclimb with adaptive step sizes."""
    roots = list(roots)
    k = len(roots)
    best = fast_evaluate(roots)
    step_sizes = [0.001] * k

    for round_idx in range(n_rounds):
        improved = False
        for i in range(k):
            for mult in [1.0, 0.5, 0.1, 2.0, 5.0, 10.0, 0.01]:
                step = step_sizes[i] * mult
                for d in [1, -1]:
                    trial = list(roots)
                    trial[i] += d * step
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    if i > 0 and trial[i] <= trial[i-1] + 0.01:
                        continue
                    if i < k-1 and trial[i] >= trial[i+1] - 0.01:
                        continue
                    score = fast_evaluate(trial)
                    if score < best - 1e-16:
                        best = score
                        roots = trial
                        step_sizes[i] = step  # adapt
                        improved = True
                        break
                if improved:
                    break
            if improved:
                break

        if not improved:
            step_sizes = [s * 0.3 for s in step_sizes]
            if max(step_sizes) < 1e-15:
                break

    return roots, best


def strategy_cluster_restructure(base_roots):
    """Try fundamentally different cluster structures."""
    best_score = fast_evaluate(base_roots)
    best_roots = list(base_roots)

    # Different cluster structures for k=13
    structures = [
        # (near_count, mid_count, far_count, near_range, mid_range, far_range)
        (3, 6, 4, (2, 8), (25, 65), (85, 160)),     # current
        (3, 5, 5, (2, 8), (25, 60), (80, 170)),      # shift to far
        (2, 6, 5, (2, 7), (25, 60), (80, 160)),      # less near
        (4, 5, 4, (2, 10), (25, 60), (80, 160)),     # more near
        (3, 7, 3, (2, 8), (25, 70), (90, 150)),      # more mid
        (2, 7, 4, (2, 7), (25, 65), (85, 160)),      # 2+7+4
        (3, 4, 6, (2, 8), (25, 55), (75, 180)),      # more far
        (2, 5, 6, (2, 7), (25, 60), (75, 180)),      # heavy far
        (3, 6, 4, (1, 5), (20, 55), (80, 150)),      # tighter near
        (3, 6, 4, (3, 10), (30, 70), (100, 200)),    # wider spread
        (3, 6, 4, (2, 8), (28, 62), (90, 145)),      # shifted mid
        (4, 6, 3, (2, 10), (25, 60), (90, 150)),     # 4+6+3
        (2, 4, 7, (2, 7), (25, 50), (60, 180)),      # heavy far cluster
    ]

    rng = np.random.RandomState(42)

    for struct_idx, (n_near, n_mid, n_far, near_r, mid_r, far_r) in enumerate(structures):
        assert n_near + n_mid + n_far == 13, f"Structure {struct_idx} doesn't sum to 13"

        # Try multiple random inits for each structure
        for trial in range(10):
            near = sorted(rng.uniform(near_r[0], near_r[1], n_near))
            mid = sorted(rng.uniform(mid_r[0], mid_r[1], n_mid))
            far = sorted(rng.uniform(far_r[0], far_r[1], n_far))
            roots = sorted(list(near) + list(mid) + list(far))

            if any(roots[i+1] - roots[i] < 0.01 for i in range(len(roots)-1)):
                continue

            score = fast_evaluate(roots)
            if score < 1.0:  # promising, refine with Nelder-Mead
                res = minimize(obj, roots, method="Nelder-Mead",
                             options={"maxiter": 3000, "xatol": 1e-12, "fatol": 1e-16})
                score = res.fun
                roots = sorted(res.x)

                if score < best_score:
                    best_score = score
                    best_roots = list(roots)
                    log(f"    Structure {struct_idx} ({n_near}+{n_mid}+{n_far}) trial {trial}: {score:.16f}")

    return best_roots, best_score


def strategy_k14_search():
    """Systematic k=14 search from cold starts."""
    best_score = float("inf")
    best_roots = []

    rng = np.random.RandomState(123)

    # Various k=14 structures
    structures = [
        (3, 6, 5, (2, 8), (25, 65), (80, 170)),
        (3, 7, 4, (2, 8), (25, 70), (85, 160)),
        (4, 6, 4, (2, 10), (25, 65), (85, 160)),
        (3, 5, 6, (2, 8), (25, 60), (75, 180)),
        (2, 6, 6, (2, 7), (25, 60), (75, 180)),
        (4, 5, 5, (2, 10), (25, 60), (80, 170)),
        (3, 6, 5, (1, 6), (20, 60), (75, 175)),
        (2, 7, 5, (2, 7), (25, 65), (80, 170)),
    ]

    for struct_idx, (n_near, n_mid, n_far, near_r, mid_r, far_r) in enumerate(structures):
        assert n_near + n_mid + n_far == 14, f"k=14 structure {struct_idx} doesn't sum to 14"

        for trial in range(15):
            near = sorted(rng.uniform(near_r[0], near_r[1], n_near))
            mid = sorted(rng.uniform(mid_r[0], mid_r[1], n_mid))
            far = sorted(rng.uniform(far_r[0], far_r[1], n_far))
            roots = sorted(list(near) + list(mid) + list(far))

            if any(roots[i+1] - roots[i] < 0.01 for i in range(len(roots)-1)):
                continue

            score = fast_evaluate(roots)
            if score < 1.0:  # promising
                res = minimize(obj, roots, method="Nelder-Mead",
                             options={"maxiter": 5000, "xatol": 1e-12, "fatol": 1e-16})
                score = res.fun
                roots = sorted(res.x)

                if score < best_score:
                    best_score = score
                    best_roots = list(roots)
                    log(f"    k=14 struct {struct_idx} ({n_near}+{n_mid}+{n_far}) trial {trial}: {score:.16f}")

    return best_roots, best_score


def strategy_basin_hopping_aggressive(roots, n_iter=50):
    """Basin hopping with cluster-aware perturbations."""
    k = len(roots)

    class ClusterStep:
        def __init__(self, stepsize=0.5):
            self.stepsize = stepsize
            self.rng = np.random.RandomState()

        def __call__(self, x):
            x_new = x.copy()
            # Perturb 2-5 random roots
            n_perturb = self.rng.randint(2, min(6, k+1))
            indices = self.rng.choice(k, n_perturb, replace=False)
            for i in indices:
                x_new[i] += self.rng.randn() * self.stepsize
            # Maintain sort order and bounds
            x_new = np.sort(x_new)
            x_new = np.clip(x_new, 0.1, 299.9)
            # Enforce minimum spacing
            for i in range(len(x_new) - 1):
                if x_new[i+1] - x_new[i] < 0.02:
                    x_new[i+1] = x_new[i] + 0.02
            return x_new

    best_score = fast_evaluate(roots)
    best_roots = list(roots)

    for step_mult in [0.1, 0.3, 0.5, 1.0, 2.0]:
        step_fn = ClusterStep(stepsize=step_mult)
        bounds = [(0.01, 300.0)] * k

        try:
            res = basinhopping(
                obj, roots, niter=n_iter,
                take_step=step_fn,
                minimizer_kwargs={
                    "method": "L-BFGS-B",
                    "bounds": bounds,
                    "options": {"maxiter": 200, "ftol": 1e-16}
                },
                seed=int(time.time()) % 10000
            )
            if res.fun < best_score:
                best_score = res.fun
                best_roots = sorted(res.x)
                log(f"    BH step={step_mult}: {res.fun:.16f}")
        except Exception as e:
            log(f"    BH step={step_mult}: FAILED ({e})")

    return best_roots, best_score


def strategy_differential_evolution_wide(roots):
    """Differential evolution with wider bounds around known structure."""
    k = len(roots)
    # Wider bounds: ±10 for near, ±15 for mid, ±30 for far
    bounds = []
    for r in roots:
        if r < 10:
            margin = 5.0
        elif r < 80:
            margin = 15.0
        else:
            margin = 30.0
        bounds.append((max(0.01, r - margin), min(300.0, r + margin)))

    best_score = fast_evaluate(roots)
    best_roots = list(roots)

    for strategy in ['best1bin', 'rand1bin', 'currenttobest1bin', 'best2bin']:
        try:
            res = differential_evolution(
                obj, bounds, strategy=strategy,
                maxiter=200, seed=int(time.time()) % 10000,
                tol=1e-16, polish=True, init="sobol",
                popsize=30, mutation=(0.5, 1.5), recombination=0.9
            )
            if res.fun < best_score:
                best_score = res.fun
                best_roots = sorted(res.x)
                log(f"    DE {strategy}: {res.fun:.16f}")
        except Exception as e:
            log(f"    DE {strategy}: FAILED ({e})")

    return best_roots, best_score


def strategy_random_multi_start(k=13, n_starts=100):
    """Random multi-start: generate diverse starting points and optimize each."""
    best_score = float("inf")
    best_roots = []
    rng = np.random.RandomState(int(time.time()) % 10000)

    for start_idx in range(n_starts):
        # Random roots in [0.5, 200], sorted
        roots = sorted(rng.uniform(0.5, 200, k))
        # Enforce minimum spacing
        for i in range(1, k):
            if roots[i] - roots[i-1] < 0.5:
                roots[i] = roots[i-1] + 0.5
        if roots[-1] > 300:
            continue

        score = fast_evaluate(roots)
        if score < 2.0:  # somewhat promising
            res = minimize(obj, roots, method="Nelder-Mead",
                         options={"maxiter": 2000, "xatol": 1e-12, "fatol": 1e-16})
            score = res.fun
            roots = sorted(res.x)

            if score < best_score:
                best_score = score
                best_roots = list(roots)
                if score < 0.35:
                    log(f"    Random start {start_idx}: {score:.16f}")

    return best_roots, best_score


def main():
    global global_best_score, global_best_roots

    log("="*70)
    log("AGGRESSIVE OPTIMIZER — Target: beat 0.318221")
    log(f"Starting best: {global_best_score:.16f}")
    log("="*70)

    strategies = [
        ("CMA-ES Restart (k=13)", lambda: strategy_cmaes_restart(BEST_ROOTS_K13, n_restarts=10, max_fevals=3000)),
        ("Nelder-Mead Multi (k=13)", lambda: strategy_nelder_mead_multi(BEST_ROOTS_K13, n_trials=30)),
        ("Fine Hillclimb (k=13)", lambda: strategy_fine_hillclimb(BEST_ROOTS_K13, n_rounds=500)),
        ("Basin Hopping (k=13)", lambda: strategy_basin_hopping_aggressive(BEST_ROOTS_K13, n_iter=30)),
        ("Diff Evolution (k=13)", lambda: strategy_differential_evolution_wide(BEST_ROOTS_K13)),
        ("Cluster Restructure (k=13)", lambda: strategy_cluster_restructure(BEST_ROOTS_K13)),
        ("k=14 Search", strategy_k14_search),
        ("Random Multi-Start (k=13)", lambda: strategy_random_multi_start(k=13, n_starts=200)),
        ("Random Multi-Start (k=14)", lambda: strategy_random_multi_start(k=14, n_starts=200)),
        ("Random Multi-Start (k=12)", lambda: strategy_random_multi_start(k=12, n_starts=100)),
    ]

    for name, fn in strategies:
        log(f"\n--- {name} ---")
        t0 = time.time()
        try:
            roots, score = fn()
            dt = time.time() - t0
            improved = update_best(roots, score, name.lower().replace(" ", "_"))
            marker = " *** IMPROVED ***" if improved else ""
            log(f"  Result: {score:.16f} ({dt:.1f}s){marker}")
            if score < TARGET:
                log(f"  !!! BEAT RHIZOMEAGENT TARGET ({TARGET}) !!!")
        except Exception as e:
            log(f"  FAILED: {e} ({time.time()-t0:.1f}s)")

    log(f"\n{'='*70}")
    log(f"FINAL BEST: {global_best_score:.16f}")
    log(f"Target was: {TARGET}")
    if global_best_score < TARGET:
        log("SUCCESS — beat RhizomeAgent!")
    else:
        log(f"Gap remaining: {global_best_score - TARGET:.10f}")
    log(f"Best roots (k={len(global_best_roots)}):")
    for r in global_best_roots:
        log(f"  {r:.16f}")


if __name__ == "__main__":
    main()
