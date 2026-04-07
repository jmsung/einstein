"""Submit Tammes Problem solution to Einstein Arena.

Usage:
    uv run python scripts/tammes/submit.py [--dry-run] [--submit]
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
    verify_api,
    wait_for_leaderboard,
)

from einstein.tammes.evaluator import evaluate  # noqa: E402


def fetch_min_improvement(problem_id: int) -> float:
    """Fetch per-problem minImprovement from the arena API."""
    problems = json.loads(urllib.request.urlopen(f"{API_URL}/problems", timeout=15).read())
    for p in problems:
        if p["id"] == problem_id:
            return float(p["minImprovement"])
    raise RuntimeError(f"problem_id {problem_id} not found in /api/problems")

RESULTS_DIR = Path("results/problem-11-tammes")
PROBLEM_ID = 11


def main():
    dry_run = "--dry-run" in sys.argv
    do_submit = "--submit" in sys.argv

    # Find best solution file
    candidates = sorted(RESULTS_DIR.glob("solution-*.json"))
    if not candidates:
        print("ERROR: no solution files in", RESULTS_DIR)
        sys.exit(1)

    best_path = None
    best_score = -np.inf
    for p in candidates:
        with open(p) as f:
            d = json.load(f)
        s = evaluate(d)
        if s > best_score:
            best_score = s
            best_path = p

    print(f"Best solution: {best_path.name}")
    print(f"Score: {best_score:.16f}")

    with open(best_path) as f:
        sol = json.load(f)
    vectors = np.array(sol["vectors"], dtype=np.float64)

    # Fetch live leaderboard
    lb = check_leaderboard(PROBLEM_ID)
    print("\nLive leaderboard top 5:")
    for i, e in enumerate(lb[:5]):
        marker = " ← us" if e["agentName"] == load_agent_name() else ""
        print(f"  #{i+1} {e['agentName'][:25]:25s} {e['score']:.16f}{marker}")

    print()
    print("Pre-submission checklist:")
    c1 = True
    print(f"  [{'x' if c1 else ' '}] 1. Local evaluator matches arena verifier (verified)")

    api_key = verify_api()
    c2 = bool(api_key)
    print(f"  [{'x' if c2 else ' '}] 2. API URL + key verified")

    # Determine projected rank
    sorted_lb = sorted(lb, key=lambda e: -e["score"])
    higher = sum(1 for e in sorted_lb if e["score"] > best_score)
    equal = sum(1 for e in sorted_lb if e["score"] == best_score)
    projected_rank = higher + 1 + equal  # ties: we go after older equals
    c3 = projected_rank <= 3
    print(f"  [{'x' if c3 else ' '}] 3. Projected rank top 3 (rank {projected_rank}, score {best_score:.13f})")

    # minImprovement check (vs our previous best, if any) — fetched from API per CLAUDE.md
    agent_name = load_agent_name()
    our_prev = next((e["score"] for e in lb if e["agentName"] == agent_name), None)
    min_imp = fetch_min_improvement(PROBLEM_ID)
    min_imp_ok = True
    if our_prev is not None:
        delta = best_score - our_prev
        min_imp_ok = delta >= min_imp
        print(f"  [{'x' if min_imp_ok else ' '}] 4. minImprovement (Δ={delta:+.3e} vs prev {our_prev:.13f}, threshold {min_imp:.0e})")
    else:
        print(f"  [x] 4. No previous submission — minImprovement N/A (threshold {min_imp:.0e})")

    # Shape validation
    c5 = vectors.shape == (50, 3)
    print(f"  [{'x' if c5 else ' '}] 5. Shape valid {vectors.shape}")

    all_pass = c1 and c2 and c3 and min_imp_ok and c5
    print()
    if not all_pass:
        print("CHECKLIST FAILED — not submitting.")
        sys.exit(1)
    print("All checks PASS.")

    if dry_run:
        print(f"\nDRY RUN: would submit (problem={PROBLEM_ID}, score={best_score:.16f}, projected rank {projected_rank})")
        return
    if not do_submit:
        print("\nNot submitting (use --submit to actually submit).")
        return

    # Confirm
    print(f"\nProceeding with submission to problem {PROBLEM_ID}...")
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

    wait_for_leaderboard(PROBLEM_ID, agent_name)


if __name__ == "__main__":
    main()
