"""Goal-1 recon for Problem 22 (Kissing Number, d=12, n=841).

Fetches:
- Live problem spec (authoritative minImprovement, slug, scoring)
- Top-20 leaderboard
- Each solution payload for rank 1..3 (to capture SOTA vectors)
- Discussion threads for the problem slug

Outputs:
- results/p22_kissing_d12/leaderboard_<UTC>.json            (raw recon dump)
- results/p22_kissing_d12/sota_<agent>_rank<r>_id<id>.json  (per-rank, if vectors returned)
- results/p22_kissing_d12/threads_<UTC>.json                (arena discussion threads)
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

PROBLEM_ID = 22
LIMIT = 20
BASE_URL = "https://einsteinarena.com/api"
RESULTS_DIR = Path("results/p22_kissing_d12")


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
    try:
        return fetch_json(f"/solutions/{sol_id}")
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}", "_body": e.read().decode(errors="replace")[:200]}
    except Exception as e:  # pragma: no cover
        return {"_error": str(e)}


def fetch_threads(slug: str) -> list | dict:
    try:
        return fetch_json(f"/problems/{slug}/threads")
    except urllib.error.HTTPError as e:
        return {"_error": f"HTTP {e.code}", "_body": e.read().decode(errors="replace")[:400]}
    except Exception as e:  # pragma: no cover
        return {"_error": str(e)}


def main() -> int:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    ts = _dt.datetime.now(_dt.UTC).strftime("%Y%m%dT%H%M%SZ")

    print(f"=== P22 Kissing Number d=12 recon — {ts} ===\n")

    spec = fetch_problem_spec(PROBLEM_ID)
    min_improvement = spec["minImprovement"]
    scoring = spec["scoring"]
    slug = spec["slug"]
    print(f"Problem: {spec['title']}  (id={spec['id']}, slug={slug})")
    print(f"Scoring: {scoring}")
    print(f"minImprovement (LIVE): {min_improvement!r}")
    print()

    lb = fetch_leaderboard(PROBLEM_ID, LIMIT)
    print(f"Top {len(lb)} leaderboard entries:")
    print(f"  {'#':>2} {'agent':<28} {'score':<22} {'id':>8} createdAt")
    for i, sol in enumerate(lb, start=1):
        score = sol.get("score")
        score_str = f"{score:.15f}" if isinstance(score, (int, float)) else str(score)
        print(
            f"  {i:>2} {sol.get('agentName', '?'):<28} "
            f"{score_str:<22} {sol.get('id', -1):>8} "
            f"{sol.get('createdAt', '')}"
        )
    print()

    print("Probing /api/solutions/<id> on top 3 for vector payloads...")
    payloads = []
    for rank, sol in enumerate(lb[:3], start=1):
        sid = sol["id"]
        agent = sol.get("agentName", "agent")
        body = fetch_solution(sid)
        if body is None:
            print(f"  rank {rank} (id={sid}, {agent}): no body")
            payloads.append(None)
            continue
        if isinstance(body, dict) and "_error" in body:
            print(f"  rank {rank} (id={sid}, {agent}): {body['_error']} {body.get('_body', '')}")
            payloads.append(body)
            continue
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

    # /solutions/best already includes the full data field per CLAUDE.md; save that too
    for rank, sol in enumerate(lb[:3], start=1):
        data = sol.get("data")
        if isinstance(data, dict) and "vectors" in data:
            agent = sol.get("agentName", "agent")
            sid = sol.get("id", -1)
            out = RESULTS_DIR / f"sota_best_{agent.lower()}_rank{rank}_id{sid}.json"
            with open(out, "w") as f:
                json.dump(data, f)
            print(f"    (from /best) saved → {out}")

    print("\nFetching discussion threads...")
    threads = fetch_threads(slug)
    threads_path = RESULTS_DIR / f"threads_{ts}.json"
    with open(threads_path, "w") as f:
        json.dump(threads, f, indent=2)
    if isinstance(threads, list):
        print(f"  {len(threads)} threads → {threads_path}")
        for t in threads[:10]:
            title = t.get("title", "?") if isinstance(t, dict) else str(t)[:80]
            print(f"    - {title}")
    else:
        print(f"  threads payload (non-list): {str(threads)[:200]}")

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
