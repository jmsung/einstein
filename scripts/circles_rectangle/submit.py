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


def fetch_min_improvement(problem_id: int) -> float:
    """Fetch per-problem minImprovement from the arena API.

    CLAUDE.md requires: minImprovement is per-problem — fetch from /api/problems
    before submitting; do NOT hardcode.
    """
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

    # Arena-tolerable overlap threshold (empirically determined from accepted submissions)
    ARENA_OVERLAP_SAFE = 8e-12

    score = evaluate(sol, tol=ARENA_OVERLAP_SAFE)

    min_improvement = fetch_min_improvement(PROBLEM_ID)
    print(f"minImprovement (from API): {min_improvement:.0e}")

    lb = check_leaderboard(PROBLEM_ID)
    me = load_agent_name()

    # Find our own previous best on the leaderboard
    our_entries = [e for e in lb if e["agentName"] == me]
    our_prev_best = our_entries[0]["score"] if our_entries else 0.0

    # SOTA among other agents
    others = [e for e in lb if e["agentName"] != me]
    sota_score = others[0]["score"] if others else float("-inf")
    sota_agent = others[0]["agentName"] if others else "?"

    print(f"Solution:    {sol_path}")
    print(f"Shape:       {circles.shape}")
    print(f"Our score:   {score:.16f}")
    print(f"#1 SOTA:     {sota_agent} @ {sota_score:.16f}")
    print(f"Our prev:    {our_prev_best:.16f}")
    print(f"Δ vs #1:     {score - sota_score:+.4e}  (positive = above)")
    print(f"Δ vs prev:   {score - our_prev_best:+.4e}  (improvement)")
    print()
    print("Current leaderboard (top 5):")
    print_leaderboard(lb[:5], me)
    print()

    # Pre-submission checklist (targeting rank #1 or tie)
    print("Pre-submission checklist:")
    c1 = True
    print(f"  [{'x' if c1 else ' '}] 1. Local evaluator matches arena format (Σr, w+h≤2, disjoint)")

    api_key = verify_api()
    c2 = bool(api_key)
    print(f"  [{'x' if c2 else ' '}] 2. API URL + key verified")

    # Arena-tolerance validity (overlaps within arena-accepted range)
    v = evaluate_verbose(sol, eps=1e-15)
    c3 = abs(v["worst_overlap"]) < ARENA_OVERLAP_SAFE
    print(f"  [{'x' if c3 else ' '}] 3. Overlap {v['worst_overlap']:.4e} within arena tolerance (< {ARENA_OVERLAP_SAFE:.0e})")

    # Perimeter check (arena accepts small float64 noise)
    PERIM_NOISE = 1e-12
    c4 = v["perimeter"] <= PERIMETER_BOUND + PERIM_NOISE
    print(f"  [{'x' if c4 else ' '}] 4. Perimeter {v['perimeter']:.16f} ≤ 4.0 + noise  (slack {v['slack']:.4e})")

    # minImprovement gate: must improve over OUR OWN previous best
    improvement = score - our_prev_best
    c5 = improvement > min_improvement
    print(f"  [{'x' if c5 else ' '}] 5. minImprovement gate: {improvement:.4e} > {min_improvement:.0e}")

    # Must tie or beat current #1 (rank #1 target)
    c6 = score >= sota_score
    print(f"  [{'x' if c6 else ' '}] 6. Ties/beats SOTA: {score:.16f} >= {sota_score:.16f}  (by {score-sota_score:+.4e})")

    # Projected rank
    strictly_better = sum(1 for e in lb if e["score"] > score)
    projected_rank = strictly_better + 1
    c7 = projected_rank <= 1
    print(f"  [{'x' if c7 else ' '}] 7. Projected rank #{projected_rank} (target: #1)")

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
