"""Download leaderboard solutions for Problem 2 and verify scores locally.

Saves each solution to results/problem-2-first-autocorrelation/sol-{rank}-{agent}.json
with the full payload, then re-scores via the local evaluator and prints a comparison
table to confirm parity with the arena server.
"""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

from einstein.first_autocorrelation.evaluator import verify_and_compute

REPO = Path(__file__).resolve().parents[2]
RESULTS = REPO / "results" / "problem-2-first-autocorrelation"
RESULTS.mkdir(parents=True, exist_ok=True)

CRED = json.loads((Path.home() / ".config/einsteinarena/credentials.json").read_text())
API_KEY = CRED["api_key"]
BASE = "https://www.einsteinarena.com"


def fetch(url: str) -> dict | list:
    req = urllib.request.Request(BASE + url, headers={"Authorization": f"Bearer {API_KEY}"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def safe_filename(s: str) -> str:
    return "".join(c if c.isalnum() or c in "-_." else "_" for c in s)[:60]


def main() -> None:
    data = fetch("/api/solutions/best?problem_id=2&limit=20")
    print(f"Fetched {len(data)} entries")
    print(f"{'rank':>4} {'sub_id':>6} {'agent':<32} {'reported':<22} {'local':<22} {'n':>7} {'delta':>14}")
    rows = []
    for rank, sol in enumerate(data, 1):
        agent = sol.get("agentName") or sol.get("agent") or "unknown"
        sub_id = sol.get("id") or sol.get("submissionId")
        reported = sol.get("score")
        sol_data = sol.get("data") or sol.get("solution") or sol.get("payload")
        if isinstance(sol_data, str):
            sol_data = json.loads(sol_data)
        values = sol_data.get("values") if isinstance(sol_data, dict) else None
        if values is None:
            print(f"{rank:>4} {sub_id!s:>6} {agent!r:<32} {reported!s:<22} -- no values --")
            continue
        try:
            local = verify_and_compute(values)
        except Exception as e:
            print(f"{rank:>4} {sub_id!s:>6} {agent!r:<32} verify err: {e}")
            continue
        delta = local - float(reported) if reported is not None else float("nan")
        n = len(values)
        print(f"{rank:>4} {sub_id!s:>6} {agent!r:<32} {reported!s:<22} {local:<22.16g} {n:>7} {delta:>+14.3e}")
        out = {
            "rank": rank,
            "submission_id": sub_id,
            "agent": agent,
            "reported_score": reported,
            "local_score": local,
            "n_points": n,
            "values": values,
        }
        fname = f"sol-{rank:02d}-{safe_filename(str(agent))}-{sub_id}.json"
        (RESULTS / fname).write_text(json.dumps(out))
        rows.append((rank, agent, reported, local, n))

    print("\n=== summary of n_points distribution ===")
    ns = sorted({r[4] for r in rows})
    for n in ns:
        agents = [r[1] for r in rows if r[4] == n]
        print(f"  n={n}: {len(agents)} solutions ({agents[:5]}...)")


if __name__ == "__main__":
    main()
