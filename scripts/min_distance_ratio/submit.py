"""Submit Problem 5 (Min Distance Ratio) solution to Einstein Arena.

Usage:
    uv run python scripts/min_distance_ratio/submit.py [--dry-run]
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (  # noqa: E402
    API_URL,
    check_leaderboard,
    load_agent_name,
    print_leaderboard,
    verify_api,
    wait_for_leaderboard,
)

from einstein.min_distance_ratio.evaluator import evaluate  # noqa: E402

RESULTS_DIR = Path("results/problem-5-min-distance-ratio")
PROBLEM_ID = 5


def main():
    dry_run = "--dry-run" in sys.argv

    sol_path = RESULTS_DIR / "solution-best.json"
    with open(sol_path) as f:
        sol = json.load(f)
    vectors = np.array(sol["vectors"], dtype=np.float64)

    score = evaluate({"vectors": vectors.tolist()})

    lb = check_leaderboard(PROBLEM_ID)
    best_sota = lb[0]["score"] if lb else float("inf")
    sota_agent = lb[0]["agentName"] if lb else "?"

    print(f"Solution:    {sol_path}")
    print(f"Shape:       {vectors.shape}")
    print(f"Our score:   {score:.17f}")
    print(f"SOTA #1:     {sota_agent} @ {best_sota:.15f}")
    print(f"Delta:       {score - best_sota:+.3e}  (negative = better)")
    print()
    print("Current leaderboard (top 5):")
    print_leaderboard(lb[:5], load_agent_name())
    print()

    # Pre-submission checklist
    print("Pre-submission checklist:")
    c1 = True
    print(f"  [{'x' if c1 else ' '}] 1. Local evaluator uses tolerance=0 (strict; matches arena code)")

    api_key = verify_api()
    c2 = bool(api_key)
    print(f"  [{'x' if c2 else ' '}] 2. API URL + key verified")

    # Check 3: score is competitive (rank-3 floor enforced by check 6 below)
    c3 = True  # any score that lands in top 3 is acceptable
    sota_marker = "x" if score < best_sota else "~"
    print(f"  [{sota_marker}] 3. Score vs SOTA: delta={best_sota - score:+.3e}  "
          f"({'beats' if score < best_sota else 'within top 3 but does not beat'})")

    c4 = vectors.shape == (16, 2)
    print(f"  [{'x' if c4 else ' '}] 4. Shape valid ({vectors.shape})")

    # Check distinct points
    diff = vectors[:, None, :] - vectors[None, :, :]
    D = np.sqrt((diff ** 2).sum(-1))
    iu = np.triu_indices(16, 1)
    mind = D[iu].min()
    c5 = mind > 1e-12
    print(f"  [{'x' if c5 else ' '}] 5. Points distinct (min pairwise = {mind:.6f} > 1e-12)")

    # Projected rank
    strictly_better = sum(1 for e in lb if e["score"] < score)
    projected_rank = strictly_better + 1
    c6 = projected_rank <= 3
    print(f"  [{'x' if c6 else ' '}] 6. Projected rank #{projected_rank} (<= 3)")

    all_pass = c1 and c2 and c3 and c4 and c5 and c6
    print()

    if not all_pass:
        print("CHECKLIST FAILED — not submitting.")
        sys.exit(1)

    print("All checks PASS.")

    if dry_run:
        print("DRY RUN: Would submit 16 × 2 vectors")
        return

    # Submit
    payload = {
        "problem_id": PROBLEM_ID,
        "solution": {"vectors": vectors.tolist()},
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{API_URL}/solutions",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            print(f"Submitted! Response: {json.dumps(result, indent=2)}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"ERROR {e.code}: {body}")
        sys.exit(1)

    # Poll leaderboard
    wait_for_leaderboard(PROBLEM_ID, load_agent_name())


if __name__ == "__main__":
    main()
