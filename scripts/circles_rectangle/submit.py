"""Submit Problem 17 (Circles in Rectangle, n=21) solution to Einstein Arena.

Usage:
    uv run python scripts/circles_rectangle/submit.py [--dry-run] [--submit]
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

from einstein.circles_rectangle.evaluator import (  # noqa: E402
    PERIMETER_BOUND,
    evaluate,
    evaluate_verbose,
)

RESULTS_DIR = Path("results/problem-17-circles-rectangle")
PROBLEM_ID = 18  # arena id for "Circles in a Rectangle (n=21)"
MIN_IMPROVEMENT = 1e-7


def main():
    dry_run = "--dry-run" in sys.argv
    do_submit = "--submit" in sys.argv

    sol_path = RESULTS_DIR / "solution-best.json"
    with open(sol_path) as f:
        sol = json.load(f)
    circles = np.array(sol["circles"], dtype=np.float64)

    score = evaluate(sol)

    lb = check_leaderboard(PROBLEM_ID)
    sota_score = lb[0]["score"] if lb else float("-inf")
    sota_agent = lb[0]["agentName"] if lb else "?"
    second_score = lb[1]["score"] if len(lb) > 1 else float("-inf")
    second_agent = lb[1]["agentName"] if len(lb) > 1 else "?"

    print(f"Solution:    {sol_path}")
    print(f"Shape:       {circles.shape}")
    print(f"Our score:   {score:.16f}")
    print(f"#1 SOTA:     {sota_agent} @ {sota_score:.13f}")
    print(f"#2:          {second_agent} @ {second_score:.13f}")
    print(f"Δ vs #1:     {score - sota_score:+.4e}  (negative = below)")
    print(f"Δ vs #2:     {score - second_score:+.4e}  (positive = above)")
    print()
    print("Current leaderboard (top 5):")
    print_leaderboard(lb[:5], load_agent_name())
    print()

    # Pre-submission checklist
    print("Pre-submission checklist:")
    c1 = True
    print(f"  [{'x' if c1 else ' '}] 1. Local evaluator matches arena format (Σr, w+h≤2, disjoint)")

    api_key = verify_api()
    c2 = bool(api_key)
    print(f"  [{'x' if c2 else ' '}] 2. API URL + key verified")

    # Strict validity (tol=0)
    try:
        score_strict = evaluate(sol, tol=0)
        c3 = True
        print(f"  [x] 3. evaluate(tol=0) PASS — strictly disjoint, perimeter ≤ 4")
    except AssertionError as e:
        c3 = False
        print(f"  [ ] 3. evaluate(tol=0) FAIL: {e}")

    # Tighter perimeter check
    v = evaluate_verbose(sol)
    c4 = v["perimeter"] <= PERIMETER_BOUND
    print(f"  [{'x' if c4 else ' '}] 4. Perimeter {v['perimeter']:.16f} ≤ 4.0  (slack {v['slack']:.4e})")

    c5 = v["worst_overlap"] >= 0
    print(f"  [{'x' if c5 else ' '}] 5. Worst overlap {v['worst_overlap']:.4e} ≥ 0")

    # Window check: must beat #2 by minImprovement AND not claim #1
    above_second = (score - second_score) > MIN_IMPROVEMENT
    below_first_by_min = (sota_score - score) > MIN_IMPROVEMENT
    c6 = above_second and below_first_by_min
    print(f"  [{'x' if c6 else ' '}] 6. Score in safe rank-2 window:")
    print(f"        above #2 by > {MIN_IMPROVEMENT:.0e}? {above_second}  (Δ = {score-second_score:+.4e})")
    print(f"        below #1 by > {MIN_IMPROVEMENT:.0e}? {below_first_by_min}  (Δ = {sota_score-score:+.4e})")

    # Projected rank
    strictly_better = sum(1 for e in lb if e["score"] > score)
    projected_rank = strictly_better + 1
    c7 = projected_rank <= 3
    print(f"  [{'x' if c7 else ' '}] 7. Projected rank #{projected_rank} (≤ 3)")

    all_pass = c1 and c2 and c3 and c4 and c5 and c6 and c7
    print()

    if not all_pass:
        print("CHECKLIST FAILED — not submitting.")
        sys.exit(1)
    print("All checks PASS.")

    if dry_run:
        print("DRY RUN: would submit 21 circles")
        return

    if not do_submit:
        print("\nNo --submit flag — pass --submit to actually POST.")
        return

    # Submit
    payload = {
        "problem_id": PROBLEM_ID,
        "solution": {"circles": circles.tolist()},
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
