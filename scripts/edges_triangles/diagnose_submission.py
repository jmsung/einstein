"""Diagnose P13 submission issues.

9+ submissions have all stayed 'pending' and been silently deleted.
This script runs 3 diagnostic tests to identify the root cause:

Test 1: Submit arena #1's exact data (FeynmanAgent) as our own
  → If pending: account/API issue on P13
  → If accepted: our solution data has a problem

Test 2: Submit our sanitized solution (no sci notation, int zeros)
  → Tests whether JSON format was the issue

Test 3: Submit a minimal 50-row solution (guaranteed small payload)
  → Tests whether solution size/complexity is the issue

Usage:
    uv run python scripts/edges_triangles/diagnose_submission.py --test 1
    uv run python scripts/edges_triangles/diagnose_submission.py --test 2
    uv run python scripts/edges_triangles/diagnose_submission.py --test 3
    uv run python scripts/edges_triangles/diagnose_submission.py --all
"""

import argparse
import json
import math
import sys
import time
import urllib.request
from pathlib import Path

API_URL = "https://einsteinarena.com/api"
PROBLEM_ID = 13


def load_api_key():
    cred = Path.home() / ".config" / "einsteinarena" / "credentials.json"
    with open(cred) as f:
        return json.load(f)["api_key"]


def submit_and_monitor(payload, label, timeout_s=300):
    """Submit and monitor for up to timeout_s seconds."""
    api_key = load_api_key()
    data = json.dumps(payload).encode()
    print(f"\n{'='*60}")
    print(f"TEST: {label}")
    print(f"Payload size: {len(data)} bytes")
    print(f"{'='*60}")

    # Check for scientific notation
    payload_str = json.dumps(payload["solution"])
    import re
    sci = re.findall(r'\d[eE][+-]?\d', payload_str)
    print(f"Scientific notation in payload: {'YES: ' + str(sci[:3]) if sci else 'NO'}")

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
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read())
        print(f"Submitted! Response: {json.dumps(result)}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"HTTP Error {e.code}: {body}")
        return

    sid = result.get("id")
    if not sid:
        print("No submission ID returned!")
        return

    # Monitor
    print(f"\nMonitoring submission {sid}...")
    checks = int(timeout_s / 15)
    for i in range(checks):
        time.sleep(15)
        try:
            url = f"{API_URL}/solutions/{sid}"
            with urllib.request.urlopen(url, timeout=10) as resp2:
                status = json.loads(resp2.read())
            s = status.get("status")
            score = status.get("score")
            error = status.get("error")
            evaluated = status.get("evaluatedAt")
            print(f"  [{time.strftime('%H:%M:%S')}] status={s} score={score} "
                  f"error={error} evaluated={evaluated}")
            if s != "pending":
                if s == "completed":
                    print(f"\n✓ SUBMISSION ACCEPTED! Score: {score}")
                elif s == "failed":
                    print(f"\n✗ SUBMISSION FAILED! Error: {error}")
                return
        except urllib.error.HTTPError as e:
            if e.code == 404:
                print(f"  [{time.strftime('%H:%M:%S')}] 404 — SUBMISSION DELETED!")
                print(f"\n✗ Submission was silently deleted (same as previous failures)")
                return
            print(f"  [{time.strftime('%H:%M:%S')}] HTTP {e.code}")

    print(f"\nTimed out after {timeout_s}s — still pending")


def test1_arena_exact():
    """Submit arena #1's exact data."""
    url = f"{API_URL}/solutions/best?problem_id={PROBLEM_ID}&limit=1"
    with urllib.request.urlopen(url, timeout=30) as resp:
        lb = json.loads(resp.read())
    arena_data = lb[0]["data"]
    payload = {"problem_id": PROBLEM_ID, "solution": arena_data}
    submit_and_monitor(payload, "Arena #1 exact data (FeynmanAgent)")


def test2_sanitized():
    """Submit our sanitized solution."""
    path = Path("results/problem-13-edges-triangles/solution-sanitized.json")
    with open(path) as f:
        sol = json.load(f)
    payload = {"problem_id": PROBLEM_ID, "solution": sol}
    submit_and_monitor(payload, "Our sanitized solution (no sci notation)")


def test3_minimal():
    """Submit a minimal 50-row solution."""
    weights = []
    for i in range(50):
        x = 0.01 + 0.019 * i  # 50 points in [0.01, 0.95]
        p = [0.0] * 20
        if x <= 0.5:
            a = 0.5 * (1.0 - math.sqrt(max(0, 1.0 - 2.0 * x)))
            p[0] = a
            p[1] = 1.0 - a
        else:
            k = int(1.0 / (1.0 - x) + 1e-10)
            k = max(k, 2)
            k = min(k, 20)
            if k >= 20:
                p = [1.0 / 20] * 20
            else:
                disc = 4 * k ** 2 - 4 * k * (k + 1) * x
                if disc < 0:
                    for j in range(k + 1):
                        p[j] = 1.0 / (k + 1)
                else:
                    c = (2 * k + math.sqrt(disc)) / (2 * k * (k + 1))
                    c = max(1.0 / (k + 1), min(c, 1.0 / k))
                    r = max(0, 1.0 - k * c)
                    for j in range(k):
                        p[j] = c
                    p[k] = r
        # Convert 0.0 to 0
        weights.append([0 if v == 0.0 else v for v in p])

    sol = {"weights": weights}
    payload = {"problem_id": PROBLEM_ID, "solution": sol}
    submit_and_monitor(payload, f"Minimal {len(weights)}-row solution")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=int, choices=[1, 2, 3])
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.all:
        test1_arena_exact()
        test2_sanitized()
        test3_minimal()
    elif args.test == 1:
        test1_arena_exact()
    elif args.test == 2:
        test2_sanitized()
    elif args.test == 3:
        test3_minimal()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
