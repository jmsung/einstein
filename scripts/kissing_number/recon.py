"""Goal-1 recon for Problem 6 (Kissing Number).

Fetches:
- Live problem spec (authoritative minImprovement)
- Top-20 leaderboard
- Each solution payload (to see if vectors are returned for non-owner agents)

Outputs:
- results/problem-6-kissing-number/leaderboard_<UTC>.json   (raw recon dump)
- results/problem-6-kissing-number/sota_<agent>_<rank>.json (per-rank, if vectors returned)
- Console digest

Read-only against the arena. No mutations, no submissions.
"""

from __future__ import annotations

import datetime as _dt
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

PROBLEM_ID = 6
LIMIT = 20
BASE_URL = "https://einsteinarena.com/api"
RESULTS_DIR = Path("results/problem-6-kissing-number")


def fetch_json(path: str) -> dict | list:
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_problem_spec(pid: int) -> dict:
    problems = fetch_json("/problems")
    for p in problems:
        if p["id"] == pid:
            return p
    raise SystemExit(f"Problem {pid} not found in /problems")


def fetch_leaderboard(pid: int, limit: int) -> list[dict]:
    return fetch_json(f"/solutions/best?problem_id={pid}&limit={limit}")


def fetch_solution(sol_id: int) -> dict | None:
    """Try the per-solution endpoint. Returns None if not accessible."""
    try:
        return fetch_json(f"/solutions/{sol_id}")
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}", "_body": e.read().decode(errors="replace")[:200]}
    except Exception as e:  # pragma: no cover
        return {"_error": str(e)}


def main() -> int:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = _dt.datetime.now(_dt.UTC).strftime("%Y%m%dT%H%M%SZ")

    print(f"=== P6 Kissing Number recon — {ts} ===\n")

    spec = fetch_problem_spec(PROBLEM_ID)
    min_improvement = spec["minImprovement"]
    scoring = spec["scoring"]
    print(f"Problem: {spec['title']}  (id={spec['id']}, slug={spec['slug']})")
    print(f"Scoring: {scoring}")
    print(f"minImprovement (LIVE): {min_improvement!r}")
    print()

    lb = fetch_leaderboard(PROBLEM_ID, LIMIT)
    print(f"Top {len(lb)} leaderboard entries:")
    print(f"  {'#':>2} {'agent':<28} {'score':<22} {'id':>8} createdAt")
    for i, sol in enumerate(lb, start=1):
        print(
            f"  {i:>2} {sol.get('agentName', '?'):<28} "
            f"{sol.get('score'):<22.15f} {sol.get('id', -1):>8} "
            f"{sol.get('createdAt', '')}"
        )
    print()

    # Try per-solution endpoint on top 3 to see what payload comes back
    print("Probing /api/solutions/<id> on top 3...")
    payloads = []
    for rank, sol in enumerate(lb[:3], start=1):
        sid = sol["id"]
        agent = sol.get("agentName", "agent")
        body = fetch_solution(sid)
        if body is None:
            print(f"  rank {rank} (id={sid}, {agent}): no body")
            payloads.append(None)
            continue
        if "_error" in body:
            print(f"  rank {rank} (id={sid}, {agent}): {body['_error']} {body.get('_body', '')}")
            payloads.append(body)
            continue
        # Did we get vectors?
        sol_body = body.get("solution") if isinstance(body, dict) else None
        has_vectors = isinstance(sol_body, dict) and isinstance(sol_body.get("vectors"), list)
        keys = list(body.keys()) if isinstance(body, dict) else type(body).__name__
        print(f"  rank {rank} (id={sid}, {agent}): keys={keys}  vectors={'YES' if has_vectors else 'NO'}")
        payloads.append(body)

        if has_vectors:
            out = RESULTS_DIR / f"sota_{agent.lower()}_rank{rank}_id{sid}.json"
            with open(out, "w") as f:
                json.dump(sol_body, f)
            print(f"    saved → {out}")

    # Save raw dump
    dump_path = RESULTS_DIR / f"leaderboard_{ts}.json"
    with open(dump_path, "w") as f:
        json.dump(
            {
                "fetched_at": ts,
                "problem_spec": spec,
                "leaderboard": lb,
                "solution_probes": payloads,
            },
            f,
            indent=2,
        )
    print(f"\nRaw dump → {dump_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
