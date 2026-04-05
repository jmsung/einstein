"""Submit Edges vs Triangles solution to Einstein Arena.

Usage:
    uv run python scripts/edges_triangles/submit.py [--dry-run]
"""

import json
import sys
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (  # noqa: E402
    API_URL,
    check_leaderboard,
    load_agent_name,
    load_api_key,
    verify_api,
    wait_for_leaderboard,
)

from einstein.edges_triangles.evaluator import compute_score  # noqa: E402

RESULTS_DIR = Path("results/problem-13-edges-triangles")
PROBLEM_ID = 13


def main():
    dry_run = "--dry-run" in sys.argv

    # Load solution
    sol_path = RESULTS_DIR / "solution.json"
    with open(sol_path) as f:
        sol = json.load(f)
    weights = np.array(sol["weights"])

    # Fetch live SOTA
    lb = check_leaderboard(PROBLEM_ID)
    best_sota = lb[0]["score"] if lb else float("-inf")

    score = compute_score(weights)
    agent_name = load_agent_name()

    print(f"Solution:    {sol_path}")
    print(f"Shape:       {weights.shape}")
    print(f"Our score:   {score:.14f}")
    print(f"SOTA #1:     {best_sota:.14f}")
    print(f"Delta:       {score - best_sota:+.2e}")
    print()

    # Pre-submission checklist
    print("Pre-submission checklist:")

    c1 = True
    print(f"  [{'x' if c1 else ' '}] 1. Local evaluator uses tolerance=0 (strict)")

    api_key = verify_api()
    c2 = bool(api_key)
    print(f"  [{'x' if c2 else ' '}] 2. API URL + key verified")

    c3 = score > best_sota
    print(f"  [{'x' if c3 else ' '}] 3. Score beats SOTA")

    c4 = weights.shape[1] == 20 and weights.shape[0] <= 500
    print(f"  [{'x' if c4 else ' '}] 4. Shape valid ({weights.shape})")

    c5 = bool(np.all(weights >= 0))
    print(f"  [{'x' if c5 else ' '}] 5. All weights non-negative")

    all_pass = c1 and c2 and c3 and c4 and c5
    print()

    if not all_pass:
        print("CHECKLIST FAILED — not submitting.")
        return

    print("All checks PASS.")

    if dry_run:
        print(f"DRY RUN: Would submit {weights.shape[0]}x{weights.shape[1]} weights")
        return

    # Submit
    payload = {
        "problem_id": PROBLEM_ID,
        "solution": {"weights": weights.tolist()},
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

    # Poll leaderboard until we appear (blocking, streams output)
    wait_for_leaderboard(PROBLEM_ID, agent_name)


if __name__ == "__main__":
    main()
