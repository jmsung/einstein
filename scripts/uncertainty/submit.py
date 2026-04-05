"""Submit solution to Einstein Arena.

Usage:
  uv run python scripts/uncertainty/submit.py                # dry run (default)
  uv run python scripts/uncertainty/submit.py --submit       # actual submission
  uv run python scripts/uncertainty/submit.py --check-known  # submit known-good first
"""
import sys
sys.path.insert(0, "src")

import argparse
import json
import time
import requests
from pathlib import Path
from einstein.uncertainty.fast import fast_evaluate
from einstein.uncertainty.hybrid import hybrid_evaluate

PROBLEM_ID = 9
MIN_IMPROVEMENT = 0.0001

# k=14 champion — triple-verified
CHAMPION_ROOTS = [
    3.094256883022448, 4.452995541910148, 6.052155208644422,
    30.648342984268222, 35.919848028666856, 40.93501224771374,
    46.21091466253731, 51.80523203960438, 57.18224335263326,
    103.32764758852369, 112.22936409660696, 116.43440789402486,
    125.33838702606033, 143.31745266272625,
]
CHAMPION_SCORE = 0.3181691600963948  # exact sympy verified


def load_api_key():
    cred_path = Path.home() / ".config" / "einsteinarena" / "credentials.json"
    if not cred_path.exists():
        raise FileNotFoundError(f"No credentials at {cred_path}")
    with open(cred_path) as f:
        return json.load(f)["api_key"]


def submit_solution(roots, api_key, problem_id=PROBLEM_ID):
    """Submit to arena API. Returns response dict."""
    url = "https://einsteinarena.com/api/solutions"
    payload = {
        "problem_id": problem_id,
        "solution": {"laguerre_double_roots": roots},
    }
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true", help="Actually submit")
    parser.add_argument("--check-known", action="store_true",
                       help="Submit known-good solution first to verify parity")
    args = parser.parse_args()

    print("="*60)
    print("SUBMISSION CHECKLIST — Problem 9 (Uncertainty Principle)")
    print("="*60)

    # 1. Verify score locally
    print("\n1. Local verification (strict tol=0):")
    fast = fast_evaluate(CHAMPION_ROOTS)
    print(f"   Fast score:  {fast:.16f}")
    print(f"   Expected:    {CHAMPION_SCORE:.16f}")
    print(f"   Match:       {'PASS' if abs(fast - CHAMPION_SCORE) < 1e-10 else 'FAIL'}")

    # 2. Check vs leaderboard
    print("\n2. Score comparison:")
    rhizome = 0.318221
    our_prev = 0.318353  # our previous #1 submission (now #2)
    print(f"   Our score:         {CHAMPION_SCORE:.10f}")
    print(f"   RhizomeAgent #1:   {rhizome:.10f}")
    print(f"   Our previous best: {our_prev:.10f}")
    print(f"   Margin vs #1:      {rhizome - CHAMPION_SCORE:.10f}")
    print(f"   Margin vs prev:    {our_prev - CHAMPION_SCORE:.10f}")
    print(f"   minImprovement:    {MIN_IMPROVEMENT}")
    beats_1 = CHAMPION_SCORE < rhizome
    beats_min = (our_prev - CHAMPION_SCORE) > MIN_IMPROVEMENT
    print(f"   Beats #1:          {'PASS' if beats_1 else 'FAIL'}")
    print(f"   Beats minImprove:  {'PASS' if beats_min else 'FAIL'} ({our_prev - CHAMPION_SCORE:.6f} > {MIN_IMPROVEMENT})")

    # 3. Solution format
    print("\n3. Solution format:")
    solution = {"laguerre_double_roots": CHAMPION_ROOTS}
    k = len(CHAMPION_ROOTS)
    print(f"   k={k} roots, all positive: {all(r > 0 for r in CHAMPION_ROOTS)}")
    print(f"   All ≤ 300: {all(r <= 300 for r in CHAMPION_ROOTS)}")
    print(f"   Format: {json.dumps(solution)[:80]}...")

    if not args.submit and not args.check_known:
        print("\n" + "="*60)
        print("DRY RUN — add --submit to actually submit")
        print("="*60)
        return

    # Load API key
    try:
        api_key = load_api_key()
        print(f"\n4. API key loaded: {api_key[:10]}...")
    except FileNotFoundError as e:
        print(f"\n4. ERROR: {e}")
        return

    if args.check_known:
        print("\n5. Submitting known-good solution first...")
        # Use our previous k=13 #1 solution
        known_roots = [
            3.0886658942606733, 4.435156861236376, 6.034127890108831,
            30.945538933257353, 36.84167838791129, 42.20424571337132,
            47.682624801878234, 51.92315504790176, 57.58188043903107,
            100.7501292924569, 115.43881608340484, 123.02406833559513,
            140.04812478845042,
        ]
        try:
            resp = submit_solution(known_roots, api_key)
            print(f"   Response: {resp}")
        except Exception as e:
            print(f"   ERROR: {e}")
            print("   Arena may be offline. Aborting.")
            return

    if args.submit:
        print(f"\n{'='*60}")
        print("SUBMITTING k=14 CHAMPION SOLUTION")
        print(f"{'='*60}")
        try:
            resp = submit_solution(CHAMPION_ROOTS, api_key)
            print(f"Response: {resp}")
            print("SUBMITTED!")
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
