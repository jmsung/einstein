"""Submit Lean proof for Problem 21 — Sum Formula.

Prove: 2 * ∑ i ∈ Finset.range(n+1), i = n * (n + 1)

Usage:
  uv run python scripts/lean_proof/submit_p21.py                # dry run
  uv run python scripts/lean_proof/submit_p21.py --submit       # actual submission
"""

import argparse
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from check_submission import API_URL, load_api_key, load_agent_name, check_leaderboard, print_leaderboard

PROBLEM_ID = 21

LEAN_PROOF = r"""import FormalConjectures.Util.ProblemImports
theorem sum_formula (n : ℕ) :
    2 * ∑ i ∈ Finset.range (n + 1), i = answer(n * (n + 1)) := by
  show 2 * ∑ i ∈ Finset.range (n + 1), i = n * (n + 1)
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, mul_add, ih]
    ring""".strip()


def submit(api_key: str) -> dict:
    url = f"{API_URL}/solutions"
    payload = {
        "problem_id": PROBLEM_ID,
        "solution": {"lean_code": LEAN_PROOF},
    }
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def main():
    parser = argparse.ArgumentParser(description="Submit Lean proof for P21")
    parser.add_argument("--submit", action="store_true", help="Actually submit")
    args = parser.parse_args()

    agent_name = load_agent_name()

    print("=" * 60)
    print("Problem 21 — Lean Test: Sum Formula")
    print("=" * 60)
    print(f"\nLean proof ({len(LEAN_PROOF)} chars):")
    print(LEAN_PROOF)
    print()

    # Show current leaderboard
    print("Current leaderboard:")
    lb = check_leaderboard(PROBLEM_ID)
    print_leaderboard(lb, agent_name)
    on_board = any(e["agentName"] == agent_name for e in lb)
    if on_board:
        print(f"\n{agent_name} already on leaderboard — no submission needed.")
        return

    if not args.submit:
        print("\nDRY RUN — add --submit to actually submit")
        return

    api_key = load_api_key()
    print(f"\nSubmitting as {agent_name}...")
    resp = submit(api_key)
    print(f"Response: {json.dumps(resp, indent=2)}")
    print("\nPoll leaderboard with:")
    print(f"  uv run python scripts/check_submission.py --problem {PROBLEM_ID}")


if __name__ == "__main__":
    main()
