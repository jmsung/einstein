"""Submit Prime Number Theorem (P7) solution to Einstein Arena.

Usage:
    uv run python scripts/prime/submit.py                         # dry run
    uv run python scripts/prime/submit.py --submit                # submit
    uv run python scripts/prime/submit.py --file path/to/sol.json # custom file
"""

import argparse
import json
import math
import sys
import urllib.request
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import (
    API_URL,
    check_leaderboard,
    load_agent_name,
    load_api_key,
    verify_api,
    wait_for_leaderboard,
)

PROBLEM_ID = 7
RESULTS_DIR = Path("results/problem-7-prime")


def fetch_min_improvement():
    url = f"{API_URL}/problems"
    with urllib.request.urlopen(url, timeout=15) as resp:
        problems = json.loads(resp.read())
    for p in problems:
        if p["id"] == PROBLEM_ID:
            return float(p["minImprovement"])
    return 1e-5


def mc_verify(pf, n_samples=10_000_000, seed=42, arena_tol=1e-4):
    """MC constraint check with arena tolerance."""
    pf = dict(pf)
    keys = sorted(pf.keys())
    sum_fk = sum(pf[k] / k for k in keys if k != 1)
    pf[1] = max(-10.0, min(10.0, -sum_fk))
    keys = sorted(pf.keys())

    ka = np.array(keys, dtype=np.int64)
    va = np.array([pf[k] for k in keys], dtype=np.float64)
    max_key = max(k for k in keys if k > 1)

    rng = np.random.RandomState(seed)
    x_samples = rng.uniform(1.0, 10.0 * max_key, size=n_samples)
    chunk_size = max(1, 100_000_000 // len(keys))
    worst = -1e10
    for start in range(0, n_samples, chunk_size):
        end = min(start + chunk_size, n_samples)
        floors = np.floor(x_samples[start:end, None] / ka[None, :].astype(np.float64))
        G = floors @ va
        mx = float(np.max(G))
        if mx > worst:
            worst = mx
        if mx > 1.0 + arena_tol:
            return False, worst
    return True, worst


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--submit", action="store_true", help="Actually submit")
    parser.add_argument("--file", type=str, default=None, help="Solution file")
    args = parser.parse_args()

    # Load solution
    if args.file:
        sol_path = Path(args.file)
    else:
        # Try best files in order of preference
        candidates = [
            RESULTS_DIR / "best_solve_scale.json",
            RESULTS_DIR / "best_v3.json",
            RESULTS_DIR / "best_colgen.json",
            RESULTS_DIR / "best.json",
        ]
        sol_path = None
        for c in candidates:
            if c.exists():
                sol_path = c
                break
        if sol_path is None:
            print("ERROR: No solution file found. Run optimizer first.")
            sys.exit(1)

    print(f"Loading: {sol_path}")
    with open(sol_path) as f:
        sol = json.load(f)

    pf = {int(k): float(v) for k, v in sol["partial_function"].items()}
    keys = sorted(k for k in pf if k > 1)
    n_keys = len(keys)

    # Compute analytical score
    pf_norm = dict(pf)
    sum_fk = sum(pf_norm[k] / k for k in keys if k != 1)
    pf_norm[1] = max(-10.0, min(10.0, -sum_fk))
    score = -sum(pf_norm[k] * math.log(k) / k for k in sorted(pf_norm) if k >= 2)

    print(f"Keys: {n_keys} (range [{min(keys)}, {max(keys)}])")
    print(f"Analytical score: {score:.15f}")

    # Fetch current SOTA
    print("\nFetching leaderboard...")
    api_key = load_api_key()
    verify_api(api_key)
    board = check_leaderboard(PROBLEM_ID)
    if board:
        print(f"  #1: {board[0]['agentName']} — {board[0]['score']:.15f}")
        sota = board[0]["score"]
        agent = load_agent_name()
        my_entry = next((e for e in board if agent in e["agentName"]), None)
        if my_entry:
            idx = board.index(my_entry) + 1
            print(f"  #{idx}: {my_entry['agentName']} — {my_entry['score']:.15f}")
    else:
        sota = 0

    min_imp = fetch_min_improvement()
    print(f"\nminImprovement: {min_imp}")
    print(f"Need score > {sota + min_imp:.15f}")
    print(f"Our score:      {score:.15f}")
    print(f"Margin:         {score - (sota + min_imp):+.2e}")

    if score <= sota + min_imp:
        print("\nWARNING: Score doesn't beat SOTA + minImprovement!")

    # MC verification
    print("\nMC verification (arena tolerance 1e-4)...")
    passed, worst = mc_verify(pf, 10_000_000, 42, 1e-4)
    print(f"  MC(10M, seed=42):  worst={worst:.12f} {'PASS' if passed else 'FAIL'}")
    if passed:
        passed2, worst2 = mc_verify(pf, 10_000_000, 123, 1e-4)
        print(f"  MC(10M, seed=123): worst={worst2:.12f} {'PASS' if passed2 else 'FAIL'}")
        if not passed2:
            print("WARNING: Failed cross-seed MC!")

    if not args.submit:
        print("\nDry run. Use --submit to actually submit.")
        return

    if not passed:
        print("ABORT: MC verification failed!")
        sys.exit(1)

    # Submit
    print("\nSubmitting...")
    # Build submission: exclude key 1 (server normalizes it)
    submit_data = {"partial_function": {str(k): v for k, v in pf.items() if k != 1}}
    payload = json.dumps({"problem_id": PROBLEM_ID, "solution": submit_data}).encode()
    req = urllib.request.Request(
        f"{API_URL}/solutions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
        print(f"  Response: {json.dumps(result, indent=2)}")
    except Exception as e:
        print(f"  ERROR: {e}")
        sys.exit(1)

    # Poll leaderboard
    print("\nWaiting for evaluation...")
    wait_for_leaderboard(PROBLEM_ID)


if __name__ == "__main__":
    main()
