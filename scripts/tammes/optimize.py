"""Tammes (n=50) optimizer — produces a submission-quality solution.

Warm-starts from a seed JSON (50 unit vectors on S²) and refines via
iterated constrained polishing until the result converges to a local
maximum of the min-pairwise-distance objective.

Reads the seed file from `--source` (absolute path or relative to the
directory given by the `EINSTEIN_TAMMES_SEEDS` environment variable).
Fetches the live leaderboard from the arena API for ranking context;
nothing is hardcoded.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import check_leaderboard  # noqa: E402

from einstein.tammes.evaluator import evaluate  # noqa: E402
from einstein.tammes.polish import slsqp_polish, normalize, min_dist  # noqa: E402


REPO_ROOT = Path(__file__).resolve().parents[2]
RESULTS_DIR = REPO_ROOT / "results" / "problem-11-tammes"
PROBLEM_ID = 11


def live_rank(score: float) -> str:
    """Report the projected rank against the live leaderboard."""
    try:
        lb = check_leaderboard(PROBLEM_ID, limit=10)
    except Exception as e:
        return f"(leaderboard fetch failed: {e})"
    higher = sum(1 for e in lb if e["score"] > score)
    equal = sum(1 for e in lb if e["score"] == score)
    projected = higher + 1 + equal  # ties: newer entries rank after older
    return f"rank {projected} (of {len(lb)} visible)"


def iterated_polish(P: np.ndarray, n_iters: int, perturb_sigma: float,
                    seed: int, verbose: bool = False) -> np.ndarray:
    """Run the SLSQP polish ``n_iters`` times, with a tiny tangent-space
    perturbation between iterations to break symmetric stagnation.
    Returns the configuration with the highest observed min distance.
    """
    rng = np.random.default_rng(seed)
    best_md = min_dist(P)
    best_P = P.copy()
    for i in range(n_iters):
        P, _ = slsqp_polish(P, max_pairs=300, tol_active=1e-3, verbose=False)
        md = min_dist(P)
        if md > best_md:
            best_md = md
            best_P = P.copy()
        if verbose:
            print(f"  iter {i:2d}: min_dist={md:.16f}  best={best_md:.16f}")
        # Tangent-space perturbation (preserves unit-sphere constraint)
        g = rng.standard_normal(P.shape) * perturb_sigma
        g = g - (g * P).sum(axis=1, keepdims=True) * P
        P = normalize(P + g)
    return best_P


def _resolve_seed(source: str) -> Path:
    """Resolve a seed path from ``--source``.

    Accepts an absolute path, or a filename relative to ``$EINSTEIN_TAMMES_SEEDS``
    if that env var is set, otherwise relative to the current working directory.
    """
    p = Path(source).expanduser()
    if p.is_absolute() and p.exists():
        return p
    seeds_root = os.environ.get("EINSTEIN_TAMMES_SEEDS")
    if seeds_root:
        candidate = Path(seeds_root).expanduser() / source
        if candidate.exists():
            return candidate
    if p.exists():
        return p
    raise FileNotFoundError(
        f"Seed file not found: {source}. Provide an absolute path or set "
        f"EINSTEIN_TAMMES_SEEDS to the directory containing the seed file."
    )


def main():
    parser = argparse.ArgumentParser(description="Tammes (n=50) optimizer")
    parser.add_argument("--source", type=str, required=True,
                        help="Seed JSON (absolute path, or filename under "
                             "$EINSTEIN_TAMMES_SEEDS)")
    parser.add_argument("--polish-iters", type=int, default=30)
    parser.add_argument("--perturb-sigma", type=float, default=1e-13)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--out", type=str, default=None)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    src = _resolve_seed(args.source)
    print(f"Source: {src}")
    with open(src) as f:
        data = json.load(f)
    P = normalize(np.array(data["vectors"], dtype=np.float64))

    s0 = evaluate({"vectors": P.tolist()})
    print(f"Initial score: {s0:.16f}")
    print(f"Initial rank:  {live_rank(s0)}")

    print(f"\n[Phase] Iterated SLSQP polish ({args.polish_iters} iters)...")
    t = time.time()
    P = iterated_polish(
        P,
        n_iters=args.polish_iters,
        perturb_sigma=args.perturb_sigma,
        seed=args.seed,
        verbose=args.verbose,
    )
    s1 = evaluate({"vectors": P.tolist()})
    print(f"  After polish: {s1:.16f}  ({time.time() - t:.0f}s)")
    print(f"  Rank: {live_rank(s1)}")

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else RESULTS_DIR / "solution.json"
    with open(out_path, "w") as f:
        json.dump({"vectors": P.tolist()}, f)
    print(f"\nSaved → {out_path}")
    print(f"Final score: {s1:.16f}")


if __name__ == "__main__":
    main()
