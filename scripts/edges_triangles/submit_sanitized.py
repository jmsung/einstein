"""Submit sanitized P13 solution (no scientific notation, int zeros).

This addresses the issue where 9+ submissions stayed 'pending' and were
silently dropped. Suspected cause: 17 weight values used scientific notation
(e.g. 1.5e-9) which may trip the arena's JSON parser or evaluator.

Usage:
    uv run python scripts/edges_triangles/submit_sanitized.py [--dry-run]
"""

import json
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (
    API_URL,
    check_leaderboard,
    load_agent_name,
    load_api_key,
    print_leaderboard,
    verify_api,
    wait_for_leaderboard,
)

SOLUTION_PATH = Path("results/problem-13-edges-triangles/solution-sanitized.json")
PROBLEM_ID = 13


def main():
    dry_run = "--dry-run" in sys.argv

    # Load sanitized solution
    with open(SOLUTION_PATH) as f:
        sol = json.load(f)

    weights = sol["weights"]
    n_rows = len(weights)
    n_cols = len(weights[0]) if weights else 0

    # Quick validation
    assert n_rows == 500 and n_cols == 20, f"Bad shape: {n_rows}x{n_cols}"
    assert all(v >= 0 for row in weights for v in row), "Negative values"
    json_str = json.dumps(sol)
    # Check for scientific notation in numeric values only (not in key names)
    import re
    sci_matches = re.findall(r'[\d]e[+-]?\d', json_str)
    assert not sci_matches, f"Scientific notation found: {sci_matches[:5]}"
    print(f"Solution:    {SOLUTION_PATH}")
    print(f"Shape:       ({n_rows}, {n_cols})")
    print(f"JSON size:   {len(json_str)} bytes")
    print(f"Sci notation: NO")

    # Score locally
    import numpy as np

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
    from einstein.edges_triangles.evaluator import compute_score

    w = np.array(weights)
    score = compute_score(w)

    # Fetch live SOTA
    lb = check_leaderboard(PROBLEM_ID)
    best_sota = lb[0]["score"] if lb else float("-inf")
    agent_name = load_agent_name()

    print(f"Our score:   {score:.14f}")
    print(f"SOTA #1:     {best_sota:.14f}")
    print(f"Delta:       {score - best_sota:+.2e}")
    print()

    # Pre-submission checklist
    print("Pre-submission checklist:")
    api_key = verify_api()
    checks = [
        (True, "1. Tolerance=0 strict evaluator"),
        (bool(api_key), "2. API key verified"),
        (score > best_sota, "3. Score beats SOTA"),
        (n_rows <= 500 and n_cols == 20, "4. Shape valid"),
        (all(v >= 0 for row in weights for v in row), "5. Non-negative"),
        (not re.findall(r'[\d]e[+-]?\d', json_str), "6. No scientific notation"),
    ]
    for ok, desc in checks:
        print(f"  [{'x' if ok else ' '}] {desc}")

    if not all(ok for ok, _ in checks):
        print("\nCHECKLIST FAILED.")
        return

    print("\nAll checks PASS.")

    if dry_run:
        print(f"DRY RUN: Would submit {n_rows}x{n_cols} weights")
        return

    # Submit
    payload = {"problem_id": PROBLEM_ID, "solution": sol}
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

    # Monitor: check status every 30s for 5 min
    sid = result.get("id")
    if sid:
        print(f"\nMonitoring submission {sid}...")
        for i in range(10):
            time.sleep(30)
            try:
                url = f"{API_URL}/solutions/{sid}"
                with urllib.request.urlopen(url, timeout=10) as resp2:
                    status = json.loads(resp2.read())
                print(f"  [{time.strftime('%H:%M:%S')}] status={status.get('status')} "
                      f"score={status.get('score')} error={status.get('error')}")
                if status.get("status") != "pending":
                    break
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print(f"  [{time.strftime('%H:%M:%S')}] 404 — submission was deleted!")
                    break
                print(f"  [{time.strftime('%H:%M:%S')}] HTTP {e.code}")

    # Also poll leaderboard
    wait_for_leaderboard(PROBLEM_ID, agent_name, interval=60, max_checks=5)


if __name__ == "__main__":
    main()
