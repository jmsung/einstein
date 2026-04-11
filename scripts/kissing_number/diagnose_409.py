"""Diagnose why P6 submissions return 409.

Tests three hypotheses:
1. Problem-level block (retry P6)
2. Agent-specific block (try P6 with minimal data)
3. Arena-wide block (try a different problem)

Usage:
    uv run python scripts/kissing_number/diagnose_409.py
"""

import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


def load_api_key():
    cred = Path.home() / ".config" / "einsteinarena" / "credentials.json"
    with open(cred) as f:
        return json.load(f)


def try_submit(problem_id, solution_data, label):
    """Attempt a submission and report the result."""
    creds = load_api_key()
    payload = json.dumps({
        "problem_id": problem_id,
        "solution": solution_data,
    }).encode()
    req = urllib.request.Request(
        "https://einsteinarena.com/api/solutions",
        data=payload,
        headers={
            "Authorization": f"Bearer {creds['api_key']}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode()
            print(f"  {label}: HTTP {resp.status} — {body[:300]}")
            return resp.status, body
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  {label}: HTTP {e.code} — {body[:300]}")
        return e.code, body


def main():
    print("=" * 60)
    print("P6 Submission 409 Diagnostic")
    print("=" * 60)

    # Test 1: Retry P6 with a deliberately invalid/minimal solution
    # This tests if P6 is blocked at the problem level (before validation)
    print("\nTest 1: P6 with 1 vector (invalid, should fail validation if submissions open)")
    code1, body1 = try_submit(6, {"vectors": [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]}, "P6-minimal")

    if code1 == 409:
        print("  → P6 is blocked (409 before validation)")
    elif code1 == 400:
        print("  → P6 accepts submissions! 400 = validation error (expected for 1 vector)")
    elif code1 == 200:
        print("  → P6 accepted (unexpected for invalid data)")

    # Test 2: Try a different problem (P17 Hexagon) with invalid data
    # This tests if the block is arena-wide or P6-specific
    print("\nTest 2: P17 with invalid data (tests arena-wide vs P6-specific)")
    code2, body2 = try_submit(17, {"hexagons": [[0, 0]]}, "P17-minimal")

    if code2 == 409:
        print("  → Arena-wide block!")
    elif code2 in (400, 422):
        print("  → P17 accepts submissions — block is P6-specific")
    elif code2 == 200:
        print("  → P17 accepted (unexpected)")

    # Test 3: Try P6 with the transformed solution (the real one)
    print("\nTest 3: P6 with real transformed score=0 solution")
    sol_path = Path("results/problem-6-kissing-number/solution_transformed_score0.json")
    if sol_path.exists():
        with open(sol_path) as f:
            sol = json.load(f)
        code3, body3 = try_submit(6, {"vectors": sol["vectors"]}, "P6-transformed")
        if code3 == 409:
            print("  → P6 still blocked for real submissions")
        elif code3 == 200:
            print("  → SUBMITTED SUCCESSFULLY!")
        else:
            print(f"  → Unexpected: {code3}")
    else:
        print("  → Skipped (no transformed solution file)")

    print("\n" + "=" * 60)
    print("Summary:")
    if code1 == 409 and code2 != 409:
        print("  P6 specifically blocked. Other problems accept submissions.")
        print("  Likely cause: arena disabled P6 after score=0 achieved (problem solved).")
    elif code1 == 409 and code2 == 409:
        print("  Arena-wide submission block. All problems affected.")
    elif code1 != 409:
        print("  P6 is NOT blocked! The 409 may have been temporary.")
    print("=" * 60)


if __name__ == "__main__":
    main()
