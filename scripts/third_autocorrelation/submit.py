"""Submit Third Autocorrelation Inequality solution to Einstein Arena.

Usage:
    uv run python scripts/third_autocorrelation/submit.py            # dry run
    uv run python scripts/third_autocorrelation/submit.py --submit   # actual
"""

import argparse
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, "src")
from einstein.third_autocorrelation.evaluator import verify_and_compute

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (  # noqa: E402
    API_URL,
    check_leaderboard,
    load_agent_name,
    verify_api,
    wait_for_leaderboard,
)

PROBLEM_ID = 4
RESULTS_DIR = Path("results/problem-4-third-autocorrelation")


def fetch_min_improvement():
    url = f"{API_URL}/problems"
    with urllib.request.urlopen(url, timeout=15) as resp:
        problems = json.loads(resp.read())
    for p in problems:
        if p["id"] == PROBLEM_ID:
            return float(p["minImprovement"])
    raise ValueError(f"Problem {PROBLEM_ID} not found in /api/problems")


def load_best_solution():
    """Load best local solution from results directory."""
    candidates = sorted(RESULTS_DIR.glob("*.json"))
    if not candidates:
        raise FileNotFoundError(f"No solution files in {RESULTS_DIR}")
    best_path, best_score = None, float("inf")
    for p in candidates:
        with open(p) as f:
            data = json.load(f)
        if "values" not in data:
            continue
        s = verify_and_compute(data["values"])
        if s < best_score:
            best_score = s
            best_path = p
    if best_path is None:
        raise FileNotFoundError(f"No usable solution files in {RESULTS_DIR}")
    with open(best_path) as f:
        return json.load(f), best_path


def submit_solution(values, dry_run=False):
    submit_url = f"{API_URL}/solutions"
    payload = {"problem_id": PROBLEM_ID, "solution": {"values": values}}
    if dry_run:
        print(f"DRY RUN: would POST n={len(values)} values to {submit_url}")
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
        with urllib.request.urlopen(req, timeout=120) as resp:
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
    parser.add_argument("--file", type=str, default=None,
                        help="Specific solution file")
    args = parser.parse_args()

    if args.file:
        with open(args.file) as f:
            data = json.load(f)
        path = Path(args.file)
    else:
        data, path = load_best_solution()
    values = data["values"]
    stored = data.get("score")
    exact_score = verify_and_compute(values)

    print("=" * 60)
    print("Third Autocorrelation Inequality — Submission")
    print("=" * 60)
    print(f"File:           {path}")
    print(f"n:              {len(values)}")
    print(f"Stored score:   {stored}")
    print(f"Exact eval:     {exact_score:.18g}")

    min_improvement = fetch_min_improvement()
    print(f"minImprovement: {min_improvement}")

    print("\nCurrent leaderboard (top 5):")
    agent_name = load_agent_name()
    lb = check_leaderboard(PROBLEM_ID, limit=5)
    for i, sol in enumerate(lb):
        marker = " <-- us" if sol["agentName"] == agent_name else ""
        print(f"  #{i+1} {sol['agentName']:<28} {sol['score']:.18g}{marker}")

    sota = lb[0]["score"]
    print(f"\nDelta vs SOTA: {sota - exact_score:+.6e}")
    print(f"  (need >= +{min_improvement:.0e} to beat #1 by minImprovement)")

    print("\nPre-submission checklist:")
    print("  [x] Evaluator tolerance=0 (matches arena verifier)")
    print("  [x] Score verified independently (in-process)")
    rank3_pass = len(lb) >= 3 and exact_score < lb[2]["score"]
    print(f"  [{'x' if rank3_pass else ' '}] Score beats current top 3")
    beat_min_imp = exact_score < sota - min_improvement
    print(f"  [{'x' if beat_min_imp else ' '}] Beats current #1 by minImprovement")

    if args.submit:
        if not beat_min_imp:
            print("\nABORT: score does not beat SOTA by minImprovement — rejection risk.")
            sys.exit(2)
        result = submit_solution(values, dry_run=False)
        if result:
            wait_for_leaderboard(PROBLEM_ID, agent_name)
    else:
        submit_solution(values, dry_run=True)


if __name__ == "__main__":
    main()
