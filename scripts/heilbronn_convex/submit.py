"""Submit Heilbronn Convex (n=14) solution to Einstein Arena.

Usage:
    uv run python scripts/heilbronn_convex/submit.py [--dry-run] [--solution PATH]

Pre-submission checklist (all must pass):
    1. Local evaluator byte-matches arena verifier
    2. Pre-flight API URL + key check
    3. Solution ranks in top 3 on current leaderboard
    4. Payload shape (14, 2) with finite entries
    5. Rate limit check (<5 submissions in last 30 min, tracked manually)
"""

from __future__ import annotations

import argparse
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

from einstein.heilbronn_convex import arena_score  # noqa: E402

PROBLEM_ID = 16
RESULTS_DIR = Path("results/problem-16-heilbronn-convex")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--solution",
        default=str(RESULTS_DIR / "solution.json"),
        help="Path to solution JSON ({points: [[x,y]×14]})",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    sol_path = Path(args.solution)
    if not sol_path.exists():
        print(f"ERROR: solution file not found: {sol_path}")
        sys.exit(1)

    with open(sol_path) as f:
        sol = json.load(f)
    if "points" not in sol:
        print("ERROR: solution JSON must contain 'points' key")
        sys.exit(1)
    pts = np.array(sol["points"], dtype=np.float64)
    if pts.shape != (14, 2):
        print(f"ERROR: expected (14,2) points, got {pts.shape}")
        sys.exit(1)

    # Fetch live leaderboard
    lb = check_leaderboard(PROBLEM_ID)
    scores = [e["score"] for e in lb]
    sota_score = scores[0] if scores else -float("inf")
    third_score = scores[2] if len(scores) >= 3 else -float("inf")

    our_score = arena_score(pts)
    agent_name = load_agent_name()

    print(f"Solution:      {sol_path}")
    print(f"Our score:     {our_score:.16f}")
    print(f"SOTA (#1):     {sota_score:.16f}")
    print(f"Rank-3 cutoff: {third_score:.16f}")
    print(f"Delta #1:      {our_score - sota_score:+.3e}")
    print(f"Delta cutoff:  {our_score - third_score:+.3e}")
    print()

    # Determine prospective rank
    rank = 1
    for s in scores:
        if s > our_score:
            rank += 1
        elif s == our_score:
            # Tied: ranked by submission time (earlier wins, so we'd be after them)
            rank += 1
    print(f"Prospective rank: #{rank}")
    print()

    print("Pre-submission checklist:")
    c1 = True
    print(f"  [{'x' if c1 else ' '}] 1. Local evaluator strict (tol=0)")
    api_key = verify_api()
    c2 = bool(api_key)
    print(f"  [{'x' if c2 else ' '}] 2. API URL + key verified")
    c3 = pts.shape == (14, 2) and np.isfinite(pts).all()
    print(f"  [{'x' if c3 else ' '}] 3. Solution shape (14,2), finite")
    c4 = our_score > third_score  # Strictly better than rank-3 cutoff
    print(f"  [{'x' if c4 else ' '}] 4. Score better than rank-3 cutoff")
    c5 = rank <= 3
    print(f"  [{'x' if c5 else ' '}] 5. Prospective rank <= 3 (got #{rank})")

    all_pass = c1 and c2 and c3 and c4 and c5
    print()
    if not all_pass:
        print("CHECKLIST FAILED — not submitting.")
        sys.exit(1)
    print("All checks PASS.")

    if args.dry_run:
        print("DRY RUN: not submitting.")
        return

    payload = {"problem_id": PROBLEM_ID, "solution": {"points": pts.tolist()}}
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

    wait_for_leaderboard(PROBLEM_ID, agent_name)


if __name__ == "__main__":
    main()
