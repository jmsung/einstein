"""Live arena standings sweep — fetch every active problem's leaderboard and
report one agent's rank across all of them, with a tally of rank-1/2/3 and a
UTC timestamp.

The arena `/api/problems` and `/api/solutions/best` endpoints are public (no key
needed). `/solutions/best` returns many submissions (not best-per-agent), so we
reduce to each agent's best, then rank.

Tiebreak matters: the arena ranks **strictly**, and on exactly-equal scores the
**earliest submission wins** (verified on P1 — Together-AI, JSAgent, and
alpha_omega_agents all scored 0.3808703105862199; the arena ranked them by
createdAt ascending). So rank = sort by (score per scoring direction, then
createdAt ascending), positional.

Usage:
    uv run python scripts/leaderboard_standings.py [--agent JSAgent]
"""

import argparse
import datetime
import json
import urllib.request

BASE = "https://einsteinarena.com/api"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "einstein-standings"})
    return json.load(urllib.request.urlopen(req, timeout=60))


def best_per_agent(lb, scoring):
    """Reduce raw submissions to each agent's best (score, then earliest time)."""
    best = {}
    for e in lb:
        a, s, t = e.get("agentName"), e.get("score"), e.get("createdAt")
        if a is None or s is None:
            continue
        if a not in best:
            best[a] = e
            continue
        cur = best[a]
        better = s > cur["score"] if scoring == "maximize" else s < cur["score"]
        same = s == cur["score"] and (t or "") < (cur.get("createdAt") or "")
        if better or same:
            best[a] = e
    return list(best.values())


def rank_board(entries, scoring):
    """Strict arena ranking: score primary, earliest createdAt breaks ties."""
    return sorted(
        entries,
        key=lambda e: (
            -e["score"] if scoring == "maximize" else e["score"],
            e.get("createdAt") or "",
        ),
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--agent", default="JSAgent")
    args = ap.parse_args()
    agent = args.agent

    ts = datetime.datetime.now(datetime.timezone.utc).astimezone()
    probs = sorted(get(f"{BASE}/problems"), key=lambda p: p["id"])

    rows = []
    tally = {1: 0, 2: 0, 3: 0}
    top3 = 0
    for p in probs:
        pid, slug, scoring = p["id"], p["slug"], p["scoring"]
        try:
            lb = get(f"{BASE}/solutions/best?problem_id={pid}&limit=500")
        except Exception as e:
            rows.append((pid, slug, "ERR", None, None, None, str(e)[:40], False))
            continue
        ordered = rank_board(best_per_agent(lb, scoring), scoring)
        rank = myscore = mydate = None
        for i, e in enumerate(ordered):
            if e["agentName"] == agent:
                rank, myscore, mydate = i + 1, e["score"], (e.get("createdAt") or "")[:10]
                break
        leader = (ordered[0]["agentName"], ordered[0]["score"]) if ordered else None
        # tie flag: does someone share my exact score?
        tied = myscore is not None and sum(1 for e in ordered if e["score"] == myscore) > 1
        if rank in (1, 2, 3):
            tally[rank] += 1
        if rank and rank <= 3:
            top3 += 1
        rows.append((pid, slug, scoring, rank, len(ordered), myscore, leader, mydate, tied))

    print(f"# Live arena standings for agent '{agent}'")
    print(f"# Fetched: {ts.isoformat()}")
    print(f"# Active problems: {len(probs)}  (strict rank; earliest-submission breaks score ties)")
    print()
    hdr = f"{'PID':>3} | {'slug':<26} | {'my score':<11} | {'rank':>5} | {'/N':>3} | {'leader (agent / score)':<32} | tie?"
    print(hdr)
    print("-" * len(hdr))
    for pid, slug, scoring, rank, n, myscore, leader, mydate, tied in rows:
        if scoring == "ERR":
            print(f"{pid:>3} | {slug[:26]:<26} | {'ERR':<11} | {'-':>5} | {'-':>3} | {'-':<32} | -")
            continue
        rk = f"#{rank}" if rank else "—"
        ms = f"{myscore:.10g}" if isinstance(myscore, (int, float)) else "—"
        ld = f"{leader[0][:18]} {leader[1]:.7g}" if leader else "—"
        print(
            f"{pid:>3} | {slug[:26]:<26} | {ms:<11} | {rk:>5} | {n:>3} | {ld:<32} | {'yes' if tied else ''}"
        )

    present = [r for r in rows if isinstance(r[3], int)]
    absent = [r for r in rows if r[3] is None and r[2] != "ERR"]
    print()
    print(f"## Summary (as of {ts.isoformat()})")
    print(f"On the board: {len(present)} / {len(probs)} problems")
    print(
        f"  Rank #1: {tally[1]}   Rank #2: {tally[2]}   Rank #3: {tally[3]}   (top-3 total: {top3})"
    )
    for r_ in (1, 2, 3):
        names = [f"P{r[0]}({r[1]})" + ("*" if r[8] else "") for r in present if r[3] == r_]
        if names:
            print(f"  Rank-#{r_}: " + ", ".join(names))
    if absent:
        print("  Not on board: " + ", ".join(f"P{r[0]}({r[1]})" for r in absent))
    print(
        "  (* = shares exact score with another agent; rank held via earlier submission or lost to it)"
    )


if __name__ == "__main__":
    main()
