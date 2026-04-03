"""RALPH-style adaptive optimization loop.

Runs autonomously (overnight). Each iteration:
  1. Load best verified result from results/
  2. Read learnings from progress.txt → adapt strategy weights
  3. Pick strategies weighted by past success
  4. Validate best candidate with exact SymPy verifier (quality gate)
  5. Record what worked/failed → smarter next iteration

State persisted between iterations (survives restart):
  - results/*.json: verified best solutions
  - logs/progress.txt: structured learnings (strategy outcomes)
  - logs/optimize_loop.log: detailed execution log

Usage: PYTHONUNBUFFERED=1 nohup python scripts/optimize_loop.py &
"""

import os
import sys
sys.path.insert(0, "src")

import json
import re
import time
import numpy as np
import cma
from collections import defaultdict
from scipy.optimize import minimize, basinhopping
from pathlib import Path
from einstein.uncertainty.fast import fast_evaluate
from einstein.uncertainty.verifier import evaluate as exact_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / "optimize_loop.log"
PROGRESS_FILE = LOGS_DIR / "progress.txt"
PID_FILE = LOGS_DIR / "loop.pid"

# Reference solution for benchmarking (loaded from results/ at runtime)
REFERENCE_ROOTS = None
REFERENCE_SCORE = None

# Strategy names (must match function names below)
STRATEGY_NAMES = ["hillclimb", "lbfgsb", "cma", "basin_hop", "perturb",
                  "pairwise", "nelder_mead", "differential_evolution"]


def log(msg):
    ts = time.strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def record_learning(msg):
    """Append structured learning to progress.txt."""
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(PROGRESS_FILE, "a") as f:
        f.write(f"[{ts}] {msg}\n")


def read_strategy_stats():
    """Parse progress.txt to compute per-strategy performance stats.

    Tracks every strategy's outcome every iteration:
      - RESULT lines: score, rank, delta vs best for every strategy
      - VERIFIED/REJECTED lines: verification outcomes for winning candidate
      - WINNER lines: which strategy won each iteration

    Returns dict: {strategy_name: {
        "wins": N,       # times this strategy had the best score
        "top3": N,       # times in top 3
        "rejected": N,   # times verified and rejected (fake result)
        "improved": N,   # times it led to a verified improvement
        "runs": N,       # total runs
        "avg_rank": float,  # average rank across iterations
    }}
    """
    stats = defaultdict(lambda: {
        "wins": 0, "top3": 0, "rejected": 0, "improved": 0,
        "runs": 0, "ranks": [], "times": [],
    })
    if not PROGRESS_FILE.exists():
        return stats
    for line in PROGRESS_FILE.read_text().splitlines():
        # Per-strategy result: RESULT strategy=X rank=N score=Y delta=Z time=Ts
        m = re.search(r"RESULT strategy=(\w+) rank=(\d+).*time=(\d+)s", line)
        if m:
            name, rank, t = m.group(1), int(m.group(2)), int(m.group(3))
            stats[name]["runs"] += 1
            stats[name]["ranks"].append(rank)
            stats[name]["times"].append(t)
            if rank == 1:
                stats[name]["wins"] += 1
            if rank <= 3:
                stats[name]["top3"] += 1
        # Verification outcomes
        m2 = re.search(r"strategy=(\w+)\s+(IMPROVED|REJECTED)", line)
        if m2:
            name, outcome = m2.group(1), m2.group(2)
            if outcome == "IMPROVED":
                stats[name]["improved"] += 1
            elif outcome == "REJECTED":
                stats[name]["rejected"] += 1
    return stats


def pick_strategies(stats, rng):
    """Pick strategies for next iteration. Adaptive selection:
    - First iteration: run all (explore)
    - After that: keep top 3 + drop 2 worst + random 2 from rest
    Performance > speed, but consistently slow losers get dropped.
    """
    total_runs = sum(s["runs"] for s in stats.values())
    if total_runs == 0:
        return list(STRATEGY_NAMES)  # first iteration: try all

    # Score each strategy: performance-weighted, with time penalty for losers
    scores = {}
    for name in STRATEGY_NAMES:
        s = stats[name]
        if s["runs"] == 0:
            scores[name] = 5.0  # unexplored → high priority
            continue
        avg_rank = sum(s["ranks"]) / len(s["ranks"])
        avg_time = sum(s["times"]) / len(s["times"]) if s["times"] else 300
        # Core score: rank performance + verified improvements
        perf = (s["improved"] * 10 + s["wins"] * 3 + s["top3"] * 1
                - s["rejected"] * 5)
        rank_score = max(0, 9.0 - avg_rank)  # rank 1 → 8, rank 8 → 1
        # Time penalty only for bad performers (slow + bad rank)
        time_penalty = 0
        if avg_rank > 5 and avg_time > 500:
            time_penalty = 2  # slow AND bad → penalize
        scores[name] = perf + rank_score - time_penalty

    # Sort by score
    ranked = sorted(STRATEGY_NAMES, key=lambda n: scores[n], reverse=True)
    top3 = ranked[:3]
    rest = ranked[3:]
    # Random 2 from the rest (exploration)
    n_random = min(2, len(rest))
    random_picks = list(rng.choice(rest, n_random, replace=False))
    chosen = top3 + random_picks
    return chosen


def load_best_verified():
    """Load best verified result from results directory."""
    best_score = float("inf")
    best_roots = []
    for path in RESULTS_DIR.glob("up_k*.json"):
        with open(path) as f:
            data = json.load(f)
        if data.get("verified") and data["score"] < best_score:
            best_score = data["score"]
            best_roots = data["laguerre_double_roots"]
    return best_roots, best_score


def save_verified(roots, fast_score, exact_score, tag, iteration):
    result = {
        "problem": "uncertainty-principle",
        "k": len(roots),
        "score": exact_score,
        "score_fast": fast_score,
        "laguerre_double_roots": list(roots),
        "tag": f"iter{iteration}_{tag}",
        "verified": True,
        "iteration": iteration,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"up_k{len(roots)}_{exact_score:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    log(f"  SAVED: {fname.name}")


def obj(x, dps=30):
    r = sorted(x)
    if any(z <= 0 or z > 300 for z in r):
        return 1e6
    if any(r[i+1] - r[i] < 0.01 for i in range(len(r)-1)):
        return 1e6
    s = fast_evaluate(r, dps=dps)
    return s if np.isfinite(s) else 1e6


# ── Strategies ──────────────────────────────────────────────────────────────

def strategy_hillclimb(roots, rng):
    """Coordinate hillclimb with adaptive step sizes."""
    roots = list(roots)
    k = len(roots)
    step = rng.choice([0.5, 0.1, 0.01, 0.001])
    step_sizes = [step] * k
    best = fast_evaluate(roots)
    for _ in range(60):
        improved = False
        for i in range(k):
            for d in [1, -1]:
                for s in [1.0, 0.5, 0.1, 2.0]:
                    trial = list(roots)
                    trial[i] += d * step_sizes[i] * s
                    if trial[i] <= 0 or trial[i] > 300:
                        continue
                    if i > 0 and trial[i] <= trial[i-1] + 0.01:
                        continue
                    if i < k-1 and trial[i] >= trial[i+1] - 0.01:
                        continue
                    score = fast_evaluate(trial)
                    if score < best - 1e-15:
                        best = score
                        roots = trial
                        improved = True
                        break
                if improved:
                    break
        if not improved:
            step_sizes = [s * 0.5 for s in step_sizes]
            if max(step_sizes) < 1e-13:
                break
    return roots, best


def strategy_pairwise(roots, rng):
    """Move pairs of roots together — exploits correlations."""
    roots = list(roots)
    k = len(roots)
    best = fast_evaluate(roots)
    for _ in range(40):
        improved = False
        pairs = [(i, j) for i in range(k) for j in range(i+1, k)]
        rng.shuffle(pairs)
        for i, j in pairs[:20]:  # sample subset for speed
            for di, dj in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                for s in [0.01, 0.05, 0.1, 0.5]:
                    trial = list(roots)
                    trial[i] += di * s
                    trial[j] += dj * s
                    trial_s = sorted(trial)
                    if any(z <= 0 or z > 300 for z in trial_s):
                        continue
                    if any(trial_s[m+1] - trial_s[m] < 0.01 for m in range(k-1)):
                        continue
                    score = fast_evaluate(trial_s)
                    if score < best - 1e-15:
                        best = score
                        roots = trial_s
                        improved = True
                        break
                if improved:
                    break
            if improved:
                break
        if not improved:
            break
    return roots, best


def strategy_lbfgsb(roots, rng):
    """L-BFGS-B with small random perturbation."""
    trial = list(roots)
    for i in range(len(trial)):
        trial[i] += rng.randn() * 0.1
    trial.sort()
    if any(z <= 0 or z > 300 for z in trial):
        return roots, fast_evaluate(roots)
    k = len(trial)
    bounds = [(0.01, 300.0)] * k
    res = minimize(obj, trial, method="L-BFGS-B", bounds=bounds,
                   options={"maxiter": 300, "ftol": 1e-16})
    return sorted(res.x), res.fun


def strategy_nelder_mead(roots, rng):
    """Nelder-Mead (simplex) — good for non-smooth landscapes."""
    trial = list(roots)
    for i in range(len(trial)):
        trial[i] += rng.randn() * 0.05
    trial.sort()
    res = minimize(obj, trial, method="Nelder-Mead",
                   options={"maxiter": 2000, "xatol": 1e-12, "fatol": 1e-16})
    return sorted(res.x), res.fun


def strategy_cma(roots, rng):
    """CMA-ES with random sigma."""
    sigma = rng.choice([0.01, 0.05, 0.1, 0.2])
    k = len(roots)
    trial = list(roots)
    for i in range(k):
        trial[i] += rng.randn() * sigma * 0.3
    trial.sort()
    opts = cma.CMAOptions()
    opts["maxfevals"] = 800
    opts["tolfun"] = 1e-16
    opts["verbose"] = -1
    opts["bounds"] = [[0.01]*k, [300.0]*k]
    try:
        es = cma.CMAEvolutionStrategy(trial, sigma, opts)
        es.optimize(obj)
        return sorted(es.result.xbest), es.result.fbest
    except Exception:
        return roots, fast_evaluate(roots)


def strategy_basin_hop(roots, rng):
    """Basin-hopping with random step size."""
    step = rng.choice([0.1, 0.3, 0.5, 1.0])
    k = len(roots)
    bounds = [(0.01, 300.0)] * k
    res = basinhopping(obj, roots, niter=5, stepsize=step,
                       minimizer_kwargs={"method": "L-BFGS-B", "bounds": bounds,
                                         "options": {"maxiter": 100, "ftol": 1e-16}},
                       seed=int(rng.randint(0, 10000)))
    return sorted(res.x), res.fun


def strategy_perturb(roots, rng):
    """Big perturbation + hillclimb refinement."""
    k = len(roots)
    trial = list(roots)
    n_perturb = rng.randint(2, min(6, k+1))
    indices = rng.choice(k, n_perturb, replace=False)
    sigma = rng.choice([0.3, 0.5, 1.0, 2.0])
    for i in indices:
        trial[i] += rng.randn() * sigma
    trial.sort()
    if any(z <= 0 or z > 300 for z in trial):
        return roots, fast_evaluate(roots)
    if any(trial[i+1] - trial[i] < 0.01 for i in range(k-1)):
        return roots, fast_evaluate(roots)
    return strategy_hillclimb(trial, rng)


def strategy_differential_evolution(roots, rng):
    """Differential evolution — population-based global optimizer."""
    from scipy.optimize import differential_evolution as de
    k = len(roots)
    # Tight bounds around current best
    margin = 3.0
    bounds = [(max(0.01, r - margin), min(300.0, r + margin)) for r in roots]
    res = de(obj, bounds, maxiter=50, seed=int(rng.randint(0, 10000)),
             tol=1e-16, polish=True, init="sobol")
    return sorted(res.x), res.fun


STRATEGY_MAP = {
    "hillclimb": strategy_hillclimb,
    "lbfgsb": strategy_lbfgsb,
    "cma": strategy_cma,
    "basin_hop": strategy_basin_hop,
    "perturb": strategy_perturb,
    "pairwise": strategy_pairwise,
    "nelder_mead": strategy_nelder_mead,
    "differential_evolution": strategy_differential_evolution,
}


# ── Main loop ───────────────────────────────────────────────────────────────

def main():
    # Write PID for easy kill
    PID_FILE.write_text(str(os.getpid()))

    log("=" * 60)
    log("RALPH-style Adaptive Optimization Loop")
    log(f"PID: {os.getpid()}")
    log("=" * 60)

    best_roots, best_score = load_best_verified()
    log(f"Starting best: {best_score:.16f} (k={len(best_roots)})")
    log(f"Target: improve on current best")

    iteration = 0
    total_improvements = 0

    while True:
        iteration += 1
        log(f"\n{'='*60}")
        log(f"--- Iteration {iteration} ---")

        # ── RALPH: read learnings and adapt ──
        stats = read_strategy_stats()
        iter_rng = np.random.RandomState(iteration * 31 + int(time.time()) % 10000)
        chosen = pick_strategies(stats, iter_rng)

        total_runs = sum(s['runs'] for s in stats.values())
        log(f"  Stats ({total_runs} past runs):")
        for name in STRATEGY_NAMES:
            s = stats[name]
            avg_r = f"{sum(s['ranks'])/len(s['ranks']):.1f}" if s['ranks'] else "-"
            avg_t = f"{sum(s['times'])/len(s['times']):.0f}s" if s['times'] else "-"
            picked = " <<<" if name in chosen else ""
            log(f"    {name:25s}: runs={s['runs']}, wins={s['wins']}, top3={s['top3']}, "
                f"rej={s['rejected']}, avg_rank={avg_r}, avg_time={avg_t}{picked}")

        log(f"  Running {len(chosen)} strategies sequentially: {', '.join(chosen)}")

        # ── Run strategies sequentially (reliable, no deadlock) ──
        candidates = []
        t_iter = time.time()
        for name in chosen:
            strategy_fn = STRATEGY_MAP[name]
            seed = iteration * 31 + hash(name) % 10000 + int(time.time()) % 10000
            rng = np.random.RandomState(seed)
            try:
                t0 = time.time()
                r, s = strategy_fn(list(best_roots), rng)
                dt = time.time() - t0
                candidates.append((name, r, s, dt))
                marker = " <-- improvement!" if s < best_score - 1e-15 else ""
                log(f"  {name:25s}: {s:.16f} ({dt:.1f}s){marker}")
            except Exception as e:
                log(f"  {name:25s}: FAILED ({e})")
                record_learning(f"iter={iteration} strategy={name} CRASHED: {e}")
        log(f"  Total wall time: {time.time() - t_iter:.1f}s")

        if not candidates:
            log("  No candidates produced")
            record_learning(f"iter={iteration} NO_CANDIDATES")
            continue

        # Sort by score and record EVERY strategy's outcome
        candidates.sort(key=lambda x: x[2])
        for rank, (name, r, s, dt) in enumerate(candidates, 1):
            delta = s - best_score
            record_learning(
                f"iter={iteration} RESULT strategy={name} rank={rank}/{len(candidates)} "
                f"score={s:.10f} delta={delta:+.2e} time={dt:.0f}s"
            )

        cand_name, cand_roots, cand_score, cand_time = candidates[0]

        if cand_score >= best_score - 1e-15:
            log(f"  No improvement this iteration (best: {cand_name} = {cand_score:.16f})")
            record_learning(f"iter={iteration} NO_IMPROVEMENT: best_candidate={cand_score:.10f} from {cand_name}, current_best={best_score:.10f}")
            continue

        # ── QUALITY GATE: exact SymPy verification ──
        log(f"  Verifying {cand_name} candidate ({cand_score:.16f})...")
        try:
            exact_score = exact_evaluate({"laguerre_double_roots": list(cand_roots)})
        except Exception as e:
            log(f"  Exact verifier FAILED: {e}")
            record_learning(f"iter={iteration} strategy={cand_name} VERIFY_FAILED: {e}")
            continue

        diff = abs(cand_score - exact_score)
        log(f"  Fast:  {cand_score:.16f}")
        log(f"  Exact: {exact_score:.16f}")
        log(f"  Diff:  {diff:.2e}")

        if diff > 1e-4:
            log(f"  REJECTED — fast/exact disagree (far sign change)")
            record_learning(f"iter={iteration} strategy={cand_name} REJECTED: fast={cand_score:.10f} exact={exact_score:.4f}")
            continue

        if exact_score < best_score - 1e-15:
            old_best = best_score
            best_score = exact_score
            best_roots = list(cand_roots)
            total_improvements += 1
            save_verified(cand_roots, cand_score, exact_score, cand_name, iteration)
            log(f"  *** VERIFIED IMPROVEMENT #{total_improvements}: {exact_score:.16f} ***")
            record_learning(f"iter={iteration} strategy={cand_name} IMPROVED: {old_best:.10f} -> {exact_score:.10f} (Δ={old_best - exact_score:.2e})")
        else:
            log(f"  Exact score not better than current best")
            record_learning(f"iter={iteration} strategy={cand_name} verified but not better: {exact_score:.10f} vs best {best_score:.10f}")

        log(f"  Current best: {best_score:.16f} (k={len(best_roots)})")
        log(f"  Total improvements: {total_improvements}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nStopped by user.")
    finally:
        roots, score = load_best_verified()
        print(f"\nFinal best: {score:.16f}")
        if PROGRESS_FILE.exists():
            lines = PROGRESS_FILE.read_text().splitlines()
            print(f"Total learnings recorded: {len(lines)}")
