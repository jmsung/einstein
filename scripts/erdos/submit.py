"""Submit Erdős Minimum Overlap solution to Einstein Arena.

Usage:
    uv run python scripts/erdos/submit.py            # dry run
    uv run python scripts/erdos/submit.py --submit   # actual submission
"""

import argparse
import json
import sys
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, "src")
from einstein.erdos.evaluator import evaluate as exact_evaluate
from einstein.erdos.fast import fast_evaluate

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (  # noqa: E402
    check_leaderboard,
    load_agent_name,
    verify_api,
    wait_for_leaderboard,
    API_URL,
)

PROBLEM_ID = 1
MIN_IMPROVEMENT = 1e-6
RESULTS_DIR = Path("results/problem-1-erdos-overlap")


def load_best_solution():
    """Load best solution from results directory."""
    candidates = [
        p for p in RESULTS_DIR.glob("erdos_n*.json")
        if not p.name.startswith("sota_")
    ]
    if not candidates:
        raise FileNotFoundError(f"No solution files in {RESULTS_DIR}")
    best_score = float("inf")
    best_data, best_path = None, None
    for p in candidates:
        with open(p) as f:
            data = json.load(f)
        score = data.get("score", float("inf"))
        if score < best_score:
            best_score = score
            best_data = data
            best_path = p
    return best_data, best_path


def submit_solution(values, dry_run=False):
    """Submit to arena."""
    submit_url = f"{API_URL}/solutions"
    payload = {"problem_id": PROBLEM_ID, "solution": {"values": values}}

    if dry_run:
        print(f"DRY RUN: Would submit n={len(values)} values to {submit_url}")
        return None

    api_key = verify_api()

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        submit_url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
            print(f"Submitted! Response: {json.dumps(result, indent=2)}")
            return result
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"ERROR {e.code}: {body}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true",
                        help="Actually submit (default: dry run)")
    args = parser.parse_args()

    data, path = load_best_solution()
    values = data["values"]
    stored = data.get("score")

    h = np.array(values, dtype=np.float64)
    exact = exact_evaluate({"values": values})
    fast = fast_evaluate(h)

    print("=" * 60)
    print("Erdős Minimum Overlap — Submission")
    print("=" * 60)
    print(f"File:           {path}")
    print(f"n:              {len(values)}")
    print(f"Stored score:   {stored}")
    print(f"Exact eval:     {exact:.13f}")
    print(f"Fast eval:      {fast:.13f}")
    print(f"Eval match:     {abs(exact - fast) < 1e-10}")

    print("\nCurrent leaderboard:")
    lb = check_leaderboard(PROBLEM_ID, limit=5)
    for i, sol in enumerate(lb):
        marker = " <-- us" if sol["agentName"] == load_agent_name() else ""
        print(f"  #{i+1} {sol['agentName']:<20} {sol['score']:.13f}{marker}")

    our_prev = next((s["score"] for s in lb if s["agentName"] == load_agent_name()), None)
    rank3 = lb[2]["score"] if len(lb) >= 3 else None

    print("\nPre-submission checklist:")
    c1 = abs(exact - fast) < 1e-10
    print(f"  [{'x' if c1 else ' '}] Evaluator tolerance=0 (exact match)")
    c2 = abs(exact - stored) < 1e-12
    print(f"  [{'x' if c2 else ' '}] Score independently verified")
    c3 = rank3 is not None and exact < rank3 - MIN_IMPROVEMENT
    print(f"  [{'x' if c3 else ' '}] Score < #3 - minImprovement")
    c4 = our_prev is None or exact < our_prev - MIN_IMPROVEMENT
    print(f"  [{'x' if c4 else ' '}] Improves on our previous best by > minImprovement")

    all_pass = c1 and c2 and c3 and c4
    print(f"\n  All checks: {'PASS' if all_pass else 'FAIL'}")

    if args.submit:
        if not all_pass:
            print("  WARNING: Submitting despite failed checks!")
        result = submit_solution(values, dry_run=False)
        if result:
            wait_for_leaderboard(PROBLEM_ID, load_agent_name())
    else:
        submit_solution(values, dry_run=True)


if __name__ == "__main__":
    main()
