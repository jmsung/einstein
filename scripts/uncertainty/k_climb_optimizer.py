"""k-climbing optimizer: increase k to find better solutions.

Strategy (simplest first):
1. Start from verified k=13 best
2. Add a k+1'th root at candidate positions
3. Optimize with CMA-ES (gap reparameterization)
4. Verify EVERY improvement with hybrid verifier (not fast evaluator)
5. If improved, continue to k+2, k+3, ...

Gap reparameterization: optimize gaps g_i = z_{i+1} - z_i instead of
root positions directly. This eliminates the ordering constraint and
minimum separation constraint, converting to simple box constraints.
"""
import sys
sys.path.insert(0, "src")

import json
import time
import numpy as np
from pathlib import Path
from scipy.optimize import minimize
from einstein.uncertainty.fast import fast_evaluate
from einstein.uncertainty.hybrid import hybrid_evaluate

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

def _load_best():
    """Load best verified roots from results/ (gitignored)."""
    best_score = float("inf")
    best_roots = None
    for p in RESULTS_DIR.glob("up_k*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("verified") and d["score"] < best_score:
            best_score = d["score"]
            best_roots = d["laguerre_double_roots"]
    return best_roots, best_score


BEST_K13, _ = _load_best() or ([], float("inf"))


def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


# ── Gap reparameterization ──────────────────────────────────────────────────

def roots_to_gaps(roots):
    """Convert sorted root positions to gaps: [z0, z1-z0, z2-z1, ...]."""
    roots = sorted(roots)
    return [roots[0]] + [roots[i] - roots[i-1] for i in range(1, len(roots))]


def gaps_to_roots(gaps):
    """Convert gaps back to sorted root positions (cumulative sum)."""
    return list(np.cumsum(gaps))


def obj_gaps(gaps, dps=30):
    """Objective in gap space. All gaps must be > 0.01, last root ≤ 300."""
    if any(g < 0.01 for g in gaps):
        return 1e6
    roots = gaps_to_roots(gaps)
    if roots[-1] > 300 or roots[0] <= 0:
        return 1e6
    s = fast_evaluate(roots, dps=dps)
    return s if np.isfinite(s) else 1e6


# ── k+1 root insertion candidates ──────────────────────────────────────────

def generate_k14_candidates(base_roots):
    """Generate starting points for k=14 by inserting a root into k=13."""
    candidates = []

    # Strategy 1: Insert in far cluster (research says best position)
    far_positions = [85, 90, 95, 100, 105, 108, 110, 115, 120, 125, 130, 135, 145, 150]
    for pos in far_positions:
        roots = sorted(base_roots + [pos])
        # Ensure minimum spacing
        valid = True
        for i in range(len(roots) - 1):
            if roots[i+1] - roots[i] < 0.5:
                valid = False
                break
        if valid:
            candidates.append((roots, f"far_{pos}"))

    # Strategy 2: Insert between mid and far clusters (gap at 58-100)
    gap_positions = [60, 65, 70, 75, 80]
    for pos in gap_positions:
        roots = sorted(base_roots + [pos])
        valid = all(roots[i+1] - roots[i] >= 0.5 for i in range(len(roots)-1))
        if valid:
            candidates.append((roots, f"gap_{pos}"))

    # Strategy 3: Extend near cluster
    near_positions = [1.5, 2.0, 2.5, 7.5, 8.0, 9.0]
    for pos in near_positions:
        roots = sorted(base_roots + [pos])
        valid = all(roots[i+1] - roots[i] >= 0.5 for i in range(len(roots)-1))
        if valid and roots[0] > 0:
            candidates.append((roots, f"near_{pos}"))

    # Strategy 4: Insert in mid cluster
    mid_positions = [25, 28, 33, 45, 55]
    for pos in mid_positions:
        roots = sorted(base_roots + [pos])
        valid = all(roots[i+1] - roots[i] >= 0.5 for i in range(len(roots)-1))
        if valid:
            candidates.append((roots, f"mid_{pos}"))

    return candidates


# ── Optimization ────────────────────────────────────────────────────────────

def optimize_from_start(roots, tag, max_nm_iter=3000, max_hc_rounds=100):
    """Optimize roots using NM in gap space + hillclimb, with hybrid verification."""
    k = len(roots)
    log(f"  Optimizing k={k} from {tag}...")

    # Phase 1: Nelder-Mead in gap space
    gaps = roots_to_gaps(roots)
    res = minimize(obj_gaps, gaps, method="Nelder-Mead",
                  options={"maxiter": max_nm_iter, "xatol": 1e-14, "fatol": 1e-16,
                           "adaptive": True})
    nm_roots = gaps_to_roots(sorted(res.x) if res.x[0] > 0 else list(res.x))
    nm_score = res.fun
    log(f"    NM: {nm_score:.14f}")

    # Phase 2: Hillclimb refinement
    roots = list(nm_roots) if nm_score < 1e5 else list(roots)
    best = fast_evaluate(roots)
    step = 0.01
    for _ in range(max_hc_rounds):
        improved = False
        for i in range(k):
            for d in [1, -1]:
                for s in [step, step*0.5, step*0.1, step*2, step*5]:
                    trial = list(roots)
                    trial[i] += d * s
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
                        improved = True
                        break
                if improved:
                    break
            if improved:
                break
        if not improved:
            step *= 0.3
            if step < 1e-13:
                break

    log(f"    HC: {best:.14f}")
    return roots, best


def verify_and_save(roots, fast_score, tag):
    """Verify with hybrid evaluator and save if valid."""
    log(f"  Verifying {tag} (fast={fast_score:.14f})...")
    t0 = time.time()
    try:
        hybrid_score = hybrid_evaluate(roots)
    except Exception as e:
        log(f"    Hybrid FAILED: {e}")
        return None

    dt = time.time() - t0
    diff = abs(fast_score - hybrid_score)
    log(f"    Hybrid: {hybrid_score:.14f} ({dt:.1f}s), diff={diff:.2e}")

    if diff > 1e-4:
        log(f"    REJECTED — far sign change (hybrid={hybrid_score:.4f})")
        return None

    # Save verified result
    result = {
        "problem": "uncertainty-principle",
        "k": len(roots),
        "score": hybrid_score,
        "score_fast": fast_score,
        "laguerre_double_roots": list(roots),
        "tag": tag,
        "verified": True,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }
    fname = RESULTS_DIR / f"up_k{len(roots)}_{hybrid_score:.10f}.json"
    with open(fname, "w") as f:
        json.dump(result, f, indent=2)
    log(f"    SAVED: {fname.name}")
    return hybrid_score


def main():
    log("="*70)
    log("K-CLIMBING OPTIMIZER")
    log(f"Starting: k=13, S={fast_evaluate(BEST_K13):.16f}")
    log(f"Target: {TARGET}")
    log("="*70)

    best_score = fast_evaluate(BEST_K13)
    best_roots = list(BEST_K13)
    best_k = 13

    # Try k=14
    log(f"\n{'='*50}")
    log("Phase 1: k=14 — insert 14th root into k=13 best")
    log(f"{'='*50}")

    candidates = generate_k14_candidates(BEST_K13)
    log(f"Generated {len(candidates)} starting configurations")

    # Quick screen all candidates
    screened = []
    for roots, tag in candidates:
        score = fast_evaluate(roots)
        if np.isfinite(score) and score < 5.0:
            screened.append((score, roots, tag))
    screened.sort(key=lambda x: x[0])
    log(f"Viable: {len(screened)}. Top 5: {[(f'{s[0]:.6f}', s[2]) for s in screened[:5]]}")

    # Optimize top candidates
    k14_results = []
    for raw_score, roots, tag in screened[:10]:
        opt_roots, opt_score = optimize_from_start(roots, tag)
        k14_results.append((opt_score, opt_roots, tag))

        if opt_score < 0.32:
            verified = verify_and_save(opt_roots, opt_score, f"k14_{tag}")
            if verified is not None:
                log(f"    Verified k=14: {verified:.14f}")
                if verified < best_score:
                    best_score = verified
                    best_roots = list(opt_roots)
                    best_k = 14
                    log(f"    *** NEW BEST: k=14, S={verified:.14f} ***")
                if verified < TARGET:
                    log(f"    !!! BEAT TARGET !!!")

    k14_results.sort(key=lambda x: x[0])
    log(f"\nBest k=14 (fast): {k14_results[0][0]:.14f} ({k14_results[0][2]})")

    # If k=14 improved, try k=15
    if best_k == 14:
        log(f"\n{'='*50}")
        log("Phase 2: k=15 — insert 15th root into k=14 best")
        log(f"{'='*50}")
        # Similar logic...

    log(f"\n{'='*70}")
    log(f"FINAL: k={best_k}, S={best_score:.16f}")
    if best_score < TARGET:
        log("SUCCESS!")
    else:
        log(f"Gap: {best_score - TARGET:.10f}")
    log(f"Roots: {best_roots}")


if __name__ == "__main__":
    main()
