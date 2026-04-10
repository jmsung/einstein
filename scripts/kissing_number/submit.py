"""Submit kissing number solution to Einstein Arena.

Usage:
    uv run python scripts/kissing_number/submit.py            # dry run
    uv run python scripts/kissing_number/submit.py --submit   # actual submission
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
from einstein.kissing_number.evaluator import (  # noqa: E402
    overlap_loss,
    overlap_loss_fast,
    overlap_loss_mpmath,
)

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (  # noqa: E402
    API_URL,
    check_leaderboard,
    load_agent_name,
    verify_api,
    wait_for_leaderboard,
)

PROBLEM_ID = 6
RESULTS_DIR = Path("results/problem-6-kissing-number")


def fetch_min_improvement() -> float:
    url = f"{API_URL}/problems"
    with urllib.request.urlopen(url, timeout=15) as resp:
        problems = json.loads(resp.read())
    for p in problems:
        if p["id"] == PROBLEM_ID:
            return float(p["minImprovement"])
    raise ValueError(f"Problem {PROBLEM_ID} not found in /api/problems")


def load_best_solution():
    """Prefer the mpmath-polished solution if available."""
    mpmath_path = RESULTS_DIR / "solution_best_mpmath.json"
    if mpmath_path.exists():
        with open(mpmath_path) as f:
            return json.load(f), mpmath_path
    path = RESULTS_DIR / "solution_best.json"
    with open(path) as f:
        data = json.load(f)
    return data, path


def submit_solution(vectors, dry_run: bool = False):
    submit_url = f"{API_URL}/solutions"
    payload = {"problem_id": PROBLEM_ID, "solution": {"vectors": vectors}}

    if dry_run:
        print(f"DRY RUN: Would POST {len(vectors)} vectors to {submit_url}")
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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true", help="Actually submit")
    args = parser.parse_args()

    data, path = load_best_solution()
    vectors = data["vectors"]
    stored = data.get("score")

    V = np.array(vectors, dtype=np.float64)
    # The arena verifier uses high-precision (mpmath) arithmetic. The float64
    # paths are kept only as a sanity print; the mpmath result is the ground truth.
    f64_slow = overlap_loss(V)
    f64_fast = overlap_loss_fast(V)
    mp_50 = overlap_loss_mpmath(V, dps=50)
    mp_80 = overlap_loss_mpmath(V, dps=80)

    print("=" * 60)
    print("Kissing Number d=11 — Submission")
    print("=" * 60)
    print(f"File:            {path}")
    print(f"n_vectors:       {len(vectors)}")
    print(f"Stored score:    {stored}")
    print(f"f64 slow eval:   {f64_slow:.15e}  (sanity check)")
    print(f"f64 fast eval:   {f64_fast:.15e}  (sanity check)")
    print(f"mpmath dps=50:   {mp_50:.15e}  (arena parity)")
    print(f"mpmath dps=80:   {mp_80:.15e}  (triple-check)")
    print(f"mpmath stable:   {abs(mp_50 - mp_80) < 1e-20}")

    min_improvement = fetch_min_improvement()
    print(f"minImprovement:  {min_improvement}")

    print("\nCurrent leaderboard (top 5):")
    agent_name = load_agent_name()
    lb = check_leaderboard(PROBLEM_ID, limit=5)
    for i, sol in enumerate(lb):
        marker = " <-- us" if sol["agentName"] == agent_name else ""
        print(f"  #{i+1} {sol['agentName']:<26} {sol['score']:.15e}{marker}")

    our_prev = next((s["score"] for s in lb if s["agentName"] == agent_name), None)
    rank3 = lb[2]["score"] if len(lb) >= 3 else None
    leader = lb[0]["score"] if lb else None

    print("\nPre-submission checklist:")
    c1 = abs(mp_50 - mp_80) < 1e-20
    print(f"  [{'x' if c1 else ' '}] mpmath dps=50 ≡ dps=80 (stable across precision)")
    c2 = stored is not None and abs(mp_50 - float(stored)) < 1e-16
    print(f"  [{'x' if c2 else ' '}] Score matches stored value")
    c3 = rank3 is not None and mp_50 <= rank3
    print(f"  [{'x' if c3 else ' '}] Score ranks top 3 (<= #3)")
    c4 = our_prev is None or (mp_50 < our_prev - min_improvement)
    print(f"  [{'x' if c4 else ' '}] Improves on our previous best by > minImprovement")
    c5 = leader is None or mp_50 < leader
    print(f"  [{'x' if c5 else ' '}] Strictly beats current leader (rank-1 candidate)")

    all_pass = c1 and c2 and c3 and c4 and c5
    print(f"\n  All checks: {'PASS' if all_pass else 'FAIL'}")

    if args.submit:
        if not all_pass:
            print("  ERROR: not submitting — failed checks")
            sys.exit(1)
        result = submit_solution(vectors, dry_run=False)
        if result:
            wait_for_leaderboard(PROBLEM_ID, load_agent_name())
    else:
        submit_solution(vectors, dry_run=True)


if __name__ == "__main__":
    main()
