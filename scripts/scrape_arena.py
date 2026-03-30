"""Fetch problem specs and leaderboard data from Einstein Arena API.

Usage:
    uv run python scripts/scrape_arena.py          # print summary table
    uv run python scripts/scrape_arena.py --json    # dump raw JSON to stdout
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request

BASE_URL = "https://einsteinarena.com/api"


def fetch_json(path: str) -> list | dict:
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_problems() -> list[dict]:
    return fetch_json("/problems")


def fetch_leaderboard(problem_id: int, limit: int = 5) -> list[dict]:
    return fetch_json(f"/solutions/best?problem_id={problem_id}&limit={limit}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scrape Einstein Arena problems and leaderboards")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    parser.add_argument("--limit", type=int, default=5, help="Top N per leaderboard")
    args = parser.parse_args()

    problems = fetch_problems()
    results = []

    for p in sorted(problems, key=lambda x: x["id"]):
        pid = p["id"]
        lb = fetch_leaderboard(pid, args.limit)
        entry = {
            "id": pid,
            "slug": p["slug"],
            "title": p["title"],
            "scoring": p["scoring"],
            "minImprovement": p["minImprovement"],
            "leaderboard": [
                {"agent": s.get("agentName", "?"), "score": s.get("score")}
                for s in lb
            ],
        }
        results.append(entry)

    if args.json:
        json.dump(results, sys.stdout, indent=2)
        print()
        return

    # Print summary table
    print(f"{'ID':>3}  {'Dir':>3}  {'SOTA':>14}  {'#1 Agent':<30}  Title")
    print("-" * 90)
    for r in results:
        sota = r["leaderboard"][0]["score"] if r["leaderboard"] else "N/A"
        agent = r["leaderboard"][0]["agent"] if r["leaderboard"] else "N/A"
        direction = "max" if r["scoring"] == "maximize" else "min"
        if isinstance(sota, float):
            sota_str = f"{sota:.6f}"
        else:
            sota_str = str(sota)
        print(f"{r['id']:>3}  {direction:>3}  {sota_str:>14}  {agent:<30}  {r['title']}")


if __name__ == "__main__":
    main()
