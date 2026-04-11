"""Continuous optimizer for P16 Heilbronn Convex — designed for cron execution.

Each invocation runs for a fixed time budget, saves the best result,
and optionally submits if it beats the threshold.

Usage:
    # Single run (10 min):
    uv run python scripts/heilbronn_convex/continuous_optimize.py --time 600

    # With auto-submit:
    uv run python scripts/heilbronn_convex/continuous_optimize.py --time 600 --auto-submit
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

import numpy as np

from einstein.heilbronn_convex import arena_score, fast_score, active_triples, hull_vertex_indices
from einstein.heilbronn_convex.optimizer import polish_slsqp, random_convex_init

RESULTS = Path("results/problem-16-heilbronn-convex")


def load_reference():
    """Load reference solution from results directory."""
    data = json.loads((RESULTS / "reference_solution.json").read_text())
    return np.array(data["points"], dtype=np.float64)


def fetch_our_best():
    """Fetch our best submitted score from the arena API."""
    import urllib.request
    try:
        req = urllib.request.Request(
            "https://einsteinarena.com/api/solutions/best?problem_id=16&limit=20"
        )
        resp = urllib.request.urlopen(req, timeout=10)
        sols = json.loads(resp.read())
        # Find JSAgent's best (we look for our submission ID pattern)
        # For now, return the known value
        return None
    except Exception:
        return None


def fetch_min_improvement():
    """Fetch per-problem minImprovement from API."""
    import urllib.request
    try:
        req = urllib.request.Request("https://einsteinarena.com/api/problems")
        resp = urllib.request.urlopen(req, timeout=10)
        problems = json.loads(resp.read())
        for p in problems:
            if p["id"] == 16:
                return p.get("minImprovement", 1e-9)
    except Exception:
        pass
    return 1e-9


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--time", type=float, default=600.0, help="Wall time budget (s)")
    parser.add_argument("--seed", type=int, default=None, help="RNG seed (default: time-based)")
    parser.add_argument("--auto-submit", action="store_true", help="Auto-submit if above threshold")
    args = parser.parse_args()

    if args.seed is None:
        args.seed = int(time.time()) % (2**31)

    rng = np.random.default_rng(args.seed)
    start = time.time()

    # Fetch current state
    our_best = fetch_our_best()
    min_imp = fetch_min_improvement()
    threshold = our_best + min_imp

    ref_pts = load_reference()
    ref_score = arena_score(ref_pts)

    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] P16 Continuous Optimizer")
    print(f"  Seed: {args.seed}")
    print(f"  Our best: {our_best}")
    print(f"  Reference: {ref_score:.20f}")
    print(f"  Threshold: {threshold}")
    print(f"  Budget: {args.time}s")
    print()

    best_score = ref_score
    best_pts = ref_pts.copy()
    trials = 0

    while time.time() - start < args.time:
        r = rng.random()
        if r < 0.2:
            # Perturb reference solution
            scale = rng.choice([1e-3, 5e-3, 1e-2, 5e-2, 0.1, 0.3])
            pts0 = ref_pts + rng.normal(0, scale, ref_pts.shape)
        elif r < 0.4:
            pts0 = random_convex_init(rng, shape="10p4")
        elif r < 0.55:
            # 9+5 or 11+3
            n_hull = rng.choice([9, 11])
            angles = np.sort(rng.uniform(0, 2 * np.pi, n_hull))
            radii = rng.uniform(0.7, 1.3, n_hull)
            hull = np.column_stack([radii * np.cos(angles), radii * np.sin(angles)])
            n_int = 14 - n_hull
            interior = rng.uniform(-0.5, 0.5, (n_int, 2))
            pts0 = np.vstack([hull, interior])
        elif r < 0.7:
            pts0 = random_convex_init(rng, shape="disk")
        elif r < 0.85:
            pts0 = random_convex_init(rng, shape="square")
        else:
            pts0 = rng.uniform(-1.5, 1.5, (14, 2))

        polished, score = polish_slsqp(pts0, max_iter=400)
        trials += 1

        if score > best_score:
            best_score = score
            best_pts = polished.copy()
            at = active_triples(polished, rel_tol=1e-9)
            hv = hull_vertex_indices(polished)
            delta = score - ref_score
            print(f"  [{trials:5d}] NEW BEST! {score:.20f}  "
                  f"delta={delta:+.3e}  hull={len(hv)}+{14-len(hv)}  active={len(at)}")

            # Save immediately
            RESULTS.mkdir(parents=True, exist_ok=True)
            fn = RESULTS / f"cron_best_{score:.10f}.json"
            with open(fn, "w") as f:
                json.dump({"points": polished.tolist(), "score": float(score)}, f, indent=2)

            if score > threshold:
                print(f"\n*** ABOVE SUBMIT THRESHOLD! score={score:.20f} ***")
                # Save candidate
                candidate = RESULTS / "submit_candidate.json"
                with open(candidate, "w") as f:
                    json.dump({"points": polished.tolist(), "score": float(score)}, f, indent=2)
                print(f"Candidate saved to {candidate}")

                if args.auto_submit:
                    print("Auto-submit enabled — would submit here")
                    # TODO: integrate with submit.py

        if trials % 500 == 0:
            elapsed = time.time() - start
            print(f"  [{trials:5d}] {elapsed:.0f}s  best={best_score:.16f}")

    elapsed = time.time() - start
    print(f"\nDone: {trials} trials in {elapsed:.1f}s")
    print(f"Best: {best_score:.20f}")
    if best_score > threshold:
        print("*** SUBMITTABLE ***")
    else:
        print(f"Gap to threshold: {threshold - best_score:.3e}")


if __name__ == "__main__":
    main()
