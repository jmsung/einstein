"""Submit kissing number solution to Einstein Arena.

Usage:
    uv run python scripts/kissing_number/submit.py [--dry-run]
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

RESULTS_DIR = Path("results/problem-6-kissing-number")
PROBLEM_ID = 6
BASE_URL = os.environ.get("EINSTEIN_ARENA_BASE_URL", "https://einsteinarena.com")
API_KEY = os.environ.get("EINSTEIN_ARENA_API_KEY", "")


def load_solution(tag="best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    with open(path) as f:
        data = json.load(f)
    return data["vectors"], data.get("score", None)


def submit(vectors, dry_run=False):
    if not API_KEY:
        print("ERROR: EINSTEIN_ARENA_API_KEY not set")
        sys.exit(1)

    payload = {
        "problem_id": PROBLEM_ID,
        "solution": {"vectors": vectors},
    }

    if dry_run:
        print(f"DRY RUN: Would submit {len(vectors)} vectors to {BASE_URL}/api/solutions")
        print(f"  Shape: ({len(vectors)}, {len(vectors[0])})")
        return None

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        f"{BASE_URL}/api/solutions",
        data=data,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())
            print(f"Submitted! Response: {json.dumps(result, indent=2)}")
            return result
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"ERROR {e.code}: {body}")
        sys.exit(1)


def main():
    dry_run = "--dry-run" in sys.argv

    vectors, local_score = load_solution()
    print(f"Solution: {len(vectors)} vectors x {len(vectors[0])} dims")
    print(f"Local score: {local_score:.15f}")
    print()

    result = submit(vectors, dry_run=dry_run)
    if result:
        print(f"\nSolution submitted. Check leaderboard in ~15 minutes.")


if __name__ == "__main__":
    main()
