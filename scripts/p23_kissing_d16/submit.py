"""Submit P23 (kissing d=16) solution to Einstein Arena.

Usage:
    uv run python scripts/p23_kissing_d16/submit.py PATH            # dry run
    uv run python scripts/p23_kissing_d16/submit.py PATH --submit   # actual submission
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, "src")
from einstein.p23_kissing_d16.evaluator import (  # noqa: E402
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

PROBLEM_ID = 23
PROBLEM_SLUG = "kissing-number-d16"


def fetch_min_improvement() -> float:
    url = f"{API_URL}/problems"
    with urllib.request.urlopen(url, timeout=15) as resp:
        problems = json.loads(resp.read())
    for p in problems:
        if p["id"] == PROBLEM_ID:
            return float(p["minImprovement"])
    raise ValueError(f"Problem {PROBLEM_ID} not found in /api/problems")


def fetch_leaderboard_top() -> list:
    url = f"{API_URL}/solutions/best?problem_id={PROBLEM_ID}&limit=20"
    with urllib.request.urlopen(url, timeout=15) as resp:
        return json.loads(resp.read())


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
        with urllib.request.urlopen(req, timeout=300) as resp:
            result = json.loads(resp.read())
            print(f"Submitted! Response: {json.dumps(result, indent=2)}")
            return result
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"ERROR {e.code}: {body}")
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Path to candidate JSON {vectors: [[...]]}")
    parser.add_argument("--submit", action="store_true", help="Actually submit")
    parser.add_argument("--skip-mpmath100", action="store_true",
                        help="Skip mpmath100 triple-check (fast path only)")
    args = parser.parse_args()

    path = Path(args.path)
    with open(path) as f:
        data = json.load(f)
    vectors = data["vectors"]

    V = np.array(vectors, dtype=np.float64)
    print("=" * 70)
    print("P23 Kissing Number d=16 (n=4321) — Submission")
    print("=" * 70)
    print(f"File:            {path}")
    print(f"shape:           {V.shape}")
    if V.shape != (4321, 16):
        print(f"ERROR: expected (4321, 16), got {V.shape}")
        sys.exit(1)

    print("\nTriple verification (arena parity = mpmath):")
    t0 = time.time(); s_fast = overlap_loss_fast(V); t_fast = time.time() - t0
    print(f"  fast (dot products):   {s_fast:.15e}  ({t_fast:.1f}s)  [sanity]")
    t0 = time.time(); s_full = overlap_loss(V); t_full = time.time() - t0
    print(f"  full O(n^2) f64:       {s_full:.15e}  ({t_full:.1f}s)  [sanity]")
    t0 = time.time(); s_mp50 = overlap_loss_mpmath(V, dps=50); t_50 = time.time() - t0
    print(f"  mpmath dps=50:         {s_mp50:.15e}  ({t_50:.1f}s)  [arena parity]")
    if not args.skip_mpmath100:
        t0 = time.time(); s_mp100 = overlap_loss_mpmath(V, dps=100); t_100 = time.time() - t0
        print(f"  mpmath dps=100:        {s_mp100:.15e}  ({t_100:.1f}s)  [triple-check]")
        stable = abs(s_mp50 - s_mp100) < 1e-20
        print(f"  mpmath stable:         {stable}")
        if not stable:
            print("  WARNING: mpmath dps=50 vs 100 disagree — score is not stable")
    else:
        s_mp100 = s_mp50

    print("\nLeaderboard context:")
    lb = fetch_leaderboard_top()
    for i, s in enumerate(lb[:5]):
        marker = " <-- best to beat" if i == 0 else ""
        print(f"  rank {i+1}: {s.get('agentName','?'):<25} score={s.get('score')}{marker}")

    min_imp = fetch_min_improvement()
    print(f"\nminImprovement: {min_imp}")
    sota_score = float(lb[0]["score"]) if lb else float("inf")
    second_score = float(lb[1]["score"]) if len(lb) > 1 else float("inf")

    print(f"\nOur score (mpmath50): {s_mp50:.15e}")
    if s_mp50 < sota_score - min_imp:
        print(f"  -> would be RANK #1 (beats {sota_score} by {sota_score - s_mp50:.6e})")
    elif s_mp50 == sota_score:
        print(f"  -> EXACT TIE with rank #1 (server may reject as copy-paste)")
    elif s_mp50 < second_score:
        print(f"  -> would be RANK #2 (between {sota_score} and {second_score})")
    else:
        print(f"  -> would be RANK #{1 + sum(1 for s in lb if float(s['score']) < s_mp50)}")

    if args.submit:
        print("\nPRE-FLIGHT API CHECK")
        verify_api()
        print("\nSUBMITTING...")
        submit_solution(vectors, dry_run=False)
        print("\nWaiting for leaderboard update...")
        agent_name = load_agent_name()
        wait_for_leaderboard(PROBLEM_ID, agent_name, expected_score=s_mp50)
    else:
        print("\nDRY RUN — pass --submit to actually POST")


if __name__ == "__main__":
    main()
