"""Shared arena submission utilities: pre-flight check, leaderboard polling.

The arena has no per-submission status endpoint. After POSTing, the only
way to confirm is to poll the leaderboard until the agent's score appears.

Provides:
    verify_api()              — pre-flight URL + auth check (call before POST)
    load_api_key()            — load API key from credentials or env
    check_leaderboard()       — fetch current leaderboard for a problem
    wait_for_leaderboard()    — poll until agent appears (blocking, streams output)

Usage (CLI — poll leaderboard for agent):
    uv run python scripts/check_submission.py --problem 13
    uv run python scripts/check_submission.py --problem 13 --once

Usage (import from any submit.py):
    from scripts.check_submission import verify_api, wait_for_leaderboard, load_api_key
"""

import json
import os
import sys
import time
import urllib.request
from pathlib import Path

BASE_URL = os.environ.get("EINSTEIN_ARENA_BASE_URL", "https://einsteinarena.com")
API_URL = f"{BASE_URL}/api"


def load_api_key():
    """Load API key from ~/.config/einsteinarena/credentials.json or env."""
    cred = Path.home() / ".config" / "einsteinarena" / "credentials.json"
    if cred.exists():
        with open(cred) as f:
            return json.load(f)["api_key"]
    return os.environ.get("EINSTEIN_ARENA_API_KEY", "")


def load_agent_name():
    """Load agent name from credentials."""
    cred = Path.home() / ".config" / "einsteinarena" / "credentials.json"
    if cred.exists():
        with open(cred) as f:
            return json.load(f).get("agent_name", "JSAgent")
    return "JSAgent"


def verify_api(api_key=None):
    """Pre-flight check: confirm API URL is reachable and key is valid.

    Exits with error if URL is wrong or auth fails. Call before any POST.
    """
    url = f"{API_URL}/problems"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            data = json.loads(resp.read())
        if not isinstance(data, list) or len(data) == 0:
            print(f"ERROR: {url} returned unexpected data")
            sys.exit(1)
        print(f"  API reachable: {url} ({len(data)} problems)")
    except Exception as e:
        print(f"ERROR: Cannot reach API at {url}: {e}")
        print(f"  Check BASE_URL={BASE_URL}")
        sys.exit(1)

    key = api_key or load_api_key()
    if not key:
        print("ERROR: No API key found (set EINSTEIN_ARENA_API_KEY or "
              "~/.config/einsteinarena/credentials.json)")
        sys.exit(1)
    print(f"  API key: ...{key[-8:]}")

    return key


def check_leaderboard(problem_id, limit=10):
    """Fetch current leaderboard for a problem."""
    url = f"{API_URL}/solutions/best?problem_id={problem_id}&limit={limit}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read())


def print_leaderboard(lb, agent_name="JSAgent"):
    """Print leaderboard, marking our agent."""
    for i, sol in enumerate(lb):
        marker = " <<<" if sol["agentName"] == agent_name else ""
        print(f"  #{i+1} {sol['agentName']:<20} {sol['score']:.13f}{marker}",
              flush=True)


def wait_for_leaderboard(problem_id, agent_name="JSAgent",
                         interval=300, max_checks=12):
    """Poll leaderboard until agent appears. Blocking, streams output.

    Args:
        problem_id: Arena problem ID.
        agent_name: Our agent name to look for.
        interval: Seconds between checks (default 5 min).
        max_checks: Max number of polls (default 12 = 60 min).

    Returns:
        dict with agent's leaderboard entry, or None if timed out.
    """
    print(f"\nPolling leaderboard for {agent_name} on problem {problem_id}")
    print(f"  Interval: {interval}s, max checks: {max_checks}", flush=True)

    for check in range(1, max_checks + 1):
        if check > 1:
            print(f"\n... waiting {interval // 60} min (check {check}/{max_checks}) ...",
                  flush=True)
            time.sleep(interval)

        try:
            lb = check_leaderboard(problem_id)
        except Exception as e:
            print(f"  [Error: {e}]", flush=True)
            continue

        ts = time.strftime("%H:%M:%S")
        print(f"\n[{ts}] Leaderboard:", flush=True)
        print_leaderboard(lb, agent_name)

        for entry in lb:
            if entry["agentName"] == agent_name:
                print(f"\n=== {agent_name} found on leaderboard! ===", flush=True)
                return entry

    print(f"\nTimed out after {max_checks} checks. {agent_name} not on leaderboard.")
    print(f"Check manually: uv run python scripts/check_submission.py --problem {problem_id} --once")
    return None


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Poll arena leaderboard")
    parser.add_argument("--problem", type=int, required=True, help="Problem ID")
    parser.add_argument("--once", action="store_true", help="Single check only")
    parser.add_argument("--interval", type=int, default=300, help="Poll interval (s)")
    parser.add_argument("--max-checks", type=int, default=12, help="Max polls")
    args = parser.parse_args()

    agent_name = load_agent_name()

    if args.once:
        lb = check_leaderboard(args.problem)
        ts = time.strftime("%H:%M:%S")
        print(f"[{ts}] Leaderboard (problem {args.problem}):")
        print_leaderboard(lb, agent_name)
        found = any(e["agentName"] == agent_name for e in lb)
        print(f"\n{agent_name}: {'FOUND' if found else 'not on board'}")
        return

    wait_for_leaderboard(args.problem, agent_name,
                         interval=args.interval, max_checks=args.max_checks)


if __name__ == "__main__":
    main()
