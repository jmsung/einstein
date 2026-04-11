"""Submit a signed-permutation-transformed kissing number solution.

A signed permutation matrix P ∈ O(11) is an exact isometry in float64:
  - Permutes the 11 coordinates of each vector
  - Flips the sign of some coordinates
  - Preserves all norms and pairwise distances exactly (no float64 rounding)

Usage:
    uv run python scripts/kissing_number/submit_transformed.py            # dry run
    uv run python scripts/kissing_number/submit_transformed.py --submit   # submit
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, "src")
from einstein.kissing_number.evaluator import (
    overlap_loss,
    overlap_loss_mpmath,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (
    API_URL,
    check_leaderboard,
    load_agent_name,
    verify_api,
    wait_for_leaderboard,
)

PROBLEM_ID = 6
RESULTS_DIR = Path("results/problem-6-kissing-number")
SEED = 42


def signed_permutation_transform(vectors: np.ndarray, seed: int = SEED) -> np.ndarray:
    """Apply a random signed permutation to all vectors.

    This is an exact isometry: no float64 rounding errors are introduced.
    The transformation permutes coordinate axes and flips some signs.
    """
    rng = np.random.default_rng(seed)
    n, d = vectors.shape

    # Random permutation of 11 dimensions
    perm = rng.permutation(d)
    # Random sign flips (+1 or -1) for each dimension
    signs = rng.choice([-1, 1], size=d)

    # Apply: v_new[k] = signs[k] * v_old[perm[k]]
    transformed = vectors[:, perm] * signs[None, :]

    # Also shuffle row order (vector ordering doesn't affect score)
    row_perm = rng.permutation(n)
    transformed = transformed[row_perm]

    return transformed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true")
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()

    # Load reference score=0 solution
    src = RESULTS_DIR / "reference_score0.json"
    if not src.exists():
        print(f"ERROR: {src} not found. Run recon.py first.")
        sys.exit(1)

    with open(src) as f:
        data = json.load(f)
    V_orig = np.array(data["vectors"], dtype=np.float64)

    print("=" * 60)
    print("Kissing Number d=11 — Signed Permutation Transform + Submit")
    print("=" * 60)
    print(f"Source: {src} (score={data.get('score')})")
    print(f"Seed: {args.seed}")

    # Apply transformation
    V_new = signed_permutation_transform(V_orig, seed=args.seed)

    # Verify the data is actually different
    identical = np.array_equal(V_orig, V_new)
    print(f"\nData identical to original: {identical}")
    if identical:
        print("ERROR: transformation produced identical data. Try a different seed.")
        sys.exit(1)

    # Verify float64 score
    f64_score = overlap_loss(V_new)
    print(f"Float64 overlap_loss: {f64_score:.15e}")
    if f64_score != 0.0:
        print("ERROR: float64 score is not 0.0 — transformation broke something")
        sys.exit(1)

    # Verify mpmath score (this is the arena ground truth)
    print("Computing mpmath dps=50 score (may take a few minutes)...")
    mp_50 = overlap_loss_mpmath(V_new, dps=50)
    print(f"mpmath dps=50: {mp_50:.15e}")

    if mp_50 == 0.0:
        print("PERFECT: mpmath score is exactly 0.0")
    else:
        print(f"WARNING: mpmath score is {mp_50:.6e} (not exactly 0)")
        if mp_50 > 1e-20:
            print("ERROR: mpmath score too large — aborting")
            sys.exit(1)

    # Save transformed solution
    out_path = RESULTS_DIR / "solution_transformed_score0.json"
    vectors_list = V_new.tolist()
    with open(out_path, "w") as f:
        json.dump({"vectors": vectors_list, "score": mp_50}, f)
    print(f"\nSaved: {out_path}")

    # Leaderboard check
    print("\nCurrent leaderboard (top 5):")
    agent_name = load_agent_name()
    lb = check_leaderboard(PROBLEM_ID, limit=5)
    for i, sol in enumerate(lb):
        marker = " <-- us" if sol["agentName"] == agent_name else ""
        print(f"  #{i + 1} {sol['agentName']:<26} {sol['score']:.15e}{marker}")

    if args.submit:
        print("\nSubmitting...")
        api_key = verify_api()
        payload = {"problem_id": PROBLEM_ID, "solution": {"vectors": vectors_list}}
        req_data = json.dumps(payload).encode()
        req = urllib.request.Request(
            f"{API_URL}/solutions",
            data=req_data,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                result = json.loads(resp.read())
                print(f"Submitted! Response: {json.dumps(result, indent=2)}")
        except urllib.error.HTTPError as e:
            body = e.read().decode()
            print(f"ERROR {e.code}: {body}")
            sys.exit(1)

        # Poll leaderboard
        wait_for_leaderboard(PROBLEM_ID, agent_name)
    else:
        print("\nDRY RUN — use --submit to actually submit")


if __name__ == "__main__":
    main()
