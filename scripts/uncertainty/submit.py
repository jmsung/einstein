"""Submit best verified solution to Einstein Arena.

Usage:
  uv run python scripts/uncertainty/submit.py                # dry run (default)
  uv run python scripts/uncertainty/submit.py --submit       # actual submission
"""
import sys
sys.path.insert(0, "src")

import argparse
import json
from pathlib import Path
from einstein.uncertainty.fast import fast_evaluate

PROBLEM_ID = 9
MIN_IMPROVEMENT = 0.0001
RESULTS_DIR = Path("results")


def load_best_verified():
    """Load best verified result from results/ (gitignored)."""
    best_score = float("inf")
    best_roots = None
    for p in RESULTS_DIR.glob("up_k*.json"):
        with open(p) as f:
            d = json.load(f)
        if d.get("verified") and d["score"] < best_score:
            best_score = d["score"]
            best_roots = d["laguerre_double_roots"]
    if best_roots is None:
        raise FileNotFoundError("No verified result in results/")
    return best_roots, best_score


def load_api_key():
    cred_path = Path.home() / ".config" / "einsteinarena" / "credentials.json"
    if not cred_path.exists():
        raise FileNotFoundError(f"No credentials at {cred_path}")
    with open(cred_path) as f:
        return json.load(f)["api_key"]


def submit_solution(roots, api_key, problem_id=PROBLEM_ID):
    """Submit to arena API. Returns response dict."""
    import requests
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
    args = parser.parse_args()

    roots, score = load_best_verified()
    fast = fast_evaluate(roots)

    print("="*60)
    print(f"Best verified: S={score:.10f} (k={len(roots)})")
    print(f"Fast check:    S={fast:.10f}")
    print(f"Match: {'PASS' if abs(fast - score) < 1e-8 else 'FAIL'}")
    print(f"Roots valid: {all(0 < r <= 300 for r in roots)}")
    print("="*60)

    if not args.submit:
        print("DRY RUN — add --submit to actually submit")
        return

    api_key = load_api_key()
    print("API key loaded. Submitting...")
    resp = submit_solution(roots, api_key)
    print(f"Response: {resp}")


if __name__ == "__main__":
    main()
