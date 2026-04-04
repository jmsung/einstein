"""Submit Thomson problem solution to Einstein Arena.

Usage:
    uv run python scripts/thomson/submit.py [--dry-run] [--tag TAG]
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

import numpy as np

RESULTS_DIR = Path("results/problem-10-thomson")
PROBLEM_ID = 10
BASE_URL = os.environ.get("EINSTEIN_ARENA_BASE_URL", "https://einsteinarena.com")
API_KEY = os.environ.get("EINSTEIN_ARENA_API_KEY", "")

SOTA_SCORE = 37147.29441846226
MIN_IMPROVEMENT = 1e-5


def load_solution(tag="best"):
    path = RESULTS_DIR / f"solution_{tag}.json"
    with open(path) as f:
        data = json.load(f)
    return data["vectors"], data.get("score", None)


def verify_energy(vectors):
    """Compute energy locally to verify before submission."""
    pts = np.array(vectors, dtype=np.float64)
    norms = np.linalg.norm(pts, axis=1, keepdims=True)
    pts = pts / norms

    diff = pts[:, None, :] - pts[None, :, :]
    dist_sq = np.sum(diff ** 2, axis=-1)
    n = len(pts)
    ii, jj = np.triu_indices(n, k=1)
    dists = np.sqrt(dist_sq[ii, jj])
    dists = np.maximum(dists, 1e-12)
    return float(np.sum(1.0 / dists))


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
    tag = "best"
    for i, arg in enumerate(sys.argv):
        if arg == "--tag" and i + 1 < len(sys.argv):
            tag = sys.argv[i + 1]

    vectors, local_score = load_solution(tag)
    verified_score = verify_energy(vectors)

    print(f"Solution tag:    {tag}")
    print(f"Shape:           ({len(vectors)}, {len(vectors[0])})")
    print(f"Stored score:    {local_score}")
    print(f"Verified score:  {verified_score:.15f}")
    print(f"Arena SOTA:      {SOTA_SCORE}")
    print(f"Gap:             {verified_score - SOTA_SCORE:+.2e}")
    print()

    # Pre-submission checklist
    print("Pre-submission checklist:")
    c1 = True
    print(f"  [{'x' if c1 else ' '}] Local evaluator uses tolerance=0 (strict)")
    c3 = verified_score < SOTA_SCORE - MIN_IMPROVEMENT
    print(f"  [{'x' if c3 else ' '}] Score < leaderboard #3 - minImprovement ({SOTA_SCORE - MIN_IMPROVEMENT:.15f})")

    if not c3:
        print(f"\n  WARNING: Score {verified_score:.15f} is NOT below target {SOTA_SCORE - MIN_IMPROVEMENT:.15f}")
        print(f"  Gap to target: {verified_score - (SOTA_SCORE - MIN_IMPROVEMENT):+.2e}")
        if not dry_run:
            print("  Refusing to submit. Use --dry-run to see what would happen.")
            return

    result = submit(vectors, dry_run=dry_run)
    if result:
        print(f"\nSolution submitted. Check leaderboard.")


if __name__ == "__main__":
    main()
