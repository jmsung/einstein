"""Submit Problem 14 (Circle Packing in a Square, n=26) solution to Einstein Arena.

Usage:
    uv run python scripts/circle_packing_square/submit.py [--dry-run] [--submit]
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

from einstein.circle_packing_square.evaluator import (  # noqa: E402
    N_CIRCLES,
    evaluate,
    evaluate_verbose,
)

RESULTS_DIR = Path("results/problem-14-circle-packing-square")
PROBLEM_ID = 14  # arena id for "Circle Packing in a Square"
ARENA_PAIR_TOL = 1e-9  # arena accepts pair overlaps up to ~1e-9


def fetch_min_improvement(problem_id: int) -> float:
    with urllib.request.urlopen(f"{API_URL}/problems", timeout=10) as resp:
        problems = json.loads(resp.read())
    for p in problems:
        if p.get("id") == problem_id:
            return float(p["minImprovement"])
    raise ValueError(f"Problem {problem_id} not found in /api/problems")


def main():
    dry_run = "--dry-run" in sys.argv
    do_submit = "--submit" in sys.argv

    sol_path = RESULTS_DIR / "solution-best.json"
    with open(sol_path) as f:
        sol = json.load(f)
    circles = np.array(sol["circles"], dtype=np.float64)

    # Score under arena tolerance (1e-9)
    score = evaluate(sol, tol=ARENA_PAIR_TOL)

    min_improvement = fetch_min_improvement(PROBLEM_ID)
    print(f"minImprovement (from API): {min_improvement:.0e}")

    lb = check_leaderboard(PROBLEM_ID)
    me = load_agent_name()
    own = next((e for e in lb if e["agentName"] == me), None)
    others = [e for e in lb if e["agentName"] != me]
    sota_score = others[0]["score"] if others else float("-inf")
    sota_agent = others[0]["agentName"] if others else "?"

    print(f"Solution:    {sol_path}")
    print(f"Shape:       {circles.shape}")
    print(f"Our score:   {score:.16f}")
    print(f"#1 SOTA:     {sota_agent} @ {sota_score:.13f}")
    print(f"Δ vs #1:     {score - sota_score:+.4e}  (positive = beats #1)")
    print()
    print("Current leaderboard (top 5):")
    print_leaderboard(lb[:5], me)
    print()

    # Pre-submission checklist
    print("Pre-submission checklist:")

    c1 = circles.shape == (N_CIRCLES, 3)
    print(f"  [{'x' if c1 else ' '}] 1. Shape ({N_CIRCLES}, 3)")

    api_key = verify_api()
    c2 = bool(api_key)
    print(f"  [{'x' if c2 else ' '}] 2. API URL + key verified")

    # Diagnostics
    diag = evaluate_verbose(sol)
    cx, cy, r = circles[:, 0], circles[:, 1], circles[:, 2]
    walls = np.concatenate([cx - r, 1.0 - cx - r, cy - r, 1.0 - cy - r])
    wmin = float(walls.min())
    pmin = float(diag["worst_overlap"])

    c3 = wmin >= 0
    print(f"  [{'x' if c3 else ' '}] 3. min wall slack {wmin:+.4e} ≥ 0")

    c4 = pmin >= -ARENA_PAIR_TOL
    print(f"  [{'x' if c4 else ' '}] 4. min pair gap {pmin:+.4e} ≥ -{ARENA_PAIR_TOL:.0e} (arena tol)")

    margin = pmin - (-ARENA_PAIR_TOL)
    # FeynmanAgent #9 was accepted with margin 1.69e-13. We require ≥1e-12 margin
    # (~6× safer than Feynman's known accepted minimum).
    MIN_MARGIN = 1e-12
    c5 = margin >= MIN_MARGIN
    print(f"  [{'x' if c5 else ' '}] 5. pair gap margin ≥ {MIN_MARGIN:.0e} (got +{margin:.3e})")
    print(f"        FeynmanAgent #9 (accepted) had margin 1.69e-13; ours is {margin/1.69e-13:.0f}× safer")

    # Improvement gates
    if own:
        own_score = own["score"]
        improvement = score - own_score
        c6 = improvement > min_improvement
        print(f"  [{'x' if c6 else ' '}] 6. improvement vs own ({own_score:.13f}): "
              f"{improvement:+.3e} > {min_improvement:.0e}")
    else:
        c6 = True
        print(f"  [x] 6. no prior submission — first submission gate auto-passes")

    # Projected rank — accept top 3
    strictly_better = sum(1 for e in lb if e["score"] > score)
    projected_rank = strictly_better + 1
    c7 = projected_rank <= 3
    print(f"  [{'x' if c7 else ' '}] 7. projected rank #{projected_rank} ≤ 3")

    all_pass = all([c1, c2, c3, c4, c5, c6, c7])
    print()

    if not all_pass:
        print("CHECKLIST FAILED — not submitting.")
        sys.exit(1)
    print("All checks PASS.")

    if dry_run:
        print("DRY RUN: would submit 26 circles")
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
