"""Backfill historical team rankings from arena API and generate trend chart.

Reconstructs daily leaderboards by filtering each agent's best score
by submission date, then computes Olympic-style team rankings per day.

Saves:
  - logs/status/rankings_history.json  — daily rankings data
  - logs/status/rankings_chart.png     — score trend chart (top agents)

Usage:
    uv run python scripts/backfill_rankings.py
"""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE_URL = "https://einsteinarena.com/api"
ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs" / "status"
HISTORY_PATH = LOG_DIR / "rankings_history.json"
CHART_PATH = LOG_DIR / "rankings_chart.png"

MEDAL_POINTS = {1: 3, 2: 2, 3: 1}


def fetch_json(path: str) -> list | dict:
    req = urllib.request.Request(f"{BASE_URL}{path}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def fetch_all_data() -> tuple[list[dict], dict[int, list[dict]]]:
    """Fetch all problems and their leaderboards."""
    problems = fetch_json("/problems")
    leaderboards: dict[int, list[dict]] = {}
    for p in sorted(problems, key=lambda x: x["id"]):
        pid = p["id"]
        lb = fetch_json(f"/solutions/best?problem_id={pid}&limit=100")
        leaderboards[pid] = lb
    return problems, leaderboards


def leaderboard_at_date(
    solutions: list[dict], scoring: str, date_str: str,
) -> list[dict]:
    """Filter solutions to those submitted on or before date, then rank."""
    filtered = [s for s in solutions if s["createdAt"][:10] <= date_str]
    reverse = scoring == "maximize"
    filtered.sort(key=lambda s: s["score"], reverse=reverse)
    return filtered


def compute_rankings_for_date(
    problems: list[dict],
    leaderboards: dict[int, list[dict]],
    date_str: str,
) -> dict[str, dict]:
    """Compute team scores for a given date."""
    scores: dict[str, dict] = {}
    for p in problems:
        pid = p["id"]
        lb = leaderboard_at_date(leaderboards[pid], p["scoring"], date_str)
        top3 = [s["agentName"] for s in lb[:3]]
        for rank_idx, agent in enumerate(top3):
            rank = rank_idx + 1
            if agent not in scores:
                scores[agent] = {"score": 0, "gold": 0, "silver": 0, "bronze": 0}
            scores[agent]["score"] += MEDAL_POINTS[rank]
            if rank == 1:
                scores[agent]["gold"] += 1
            elif rank == 2:
                scores[agent]["silver"] += 1
            else:
                scores[agent]["bronze"] += 1
    return scores


def generate_chart(history: list[dict], top_n: int = 8) -> None:
    """Generate score-over-time line chart for top agents."""
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    # Find top agents by latest score
    latest = history[-1]["rankings"]
    top_agents_sorted = sorted(
        latest.items(), key=lambda x: (x[1]["score"], x[1]["gold"]), reverse=True,
    )[:top_n]
    top_agents = [a for a, _ in top_agents_sorted]

    dates = [datetime.strptime(h["date"], "%Y-%m-%d") for h in history]

    fig, ax = plt.subplots(figsize=(10, 5))

    for agent in top_agents:
        scores = []
        for h in history:
            r = h["rankings"].get(agent)
            scores.append(r["score"] if r else 0)
        ax.plot(dates, scores, marker="o", markersize=4, linewidth=2, label=agent)

    ax.set_xlabel("Date")
    ax.set_ylabel("Score (3/2/1 for rank 1/2/3)")
    ax.set_title("Einstein Arena — Team Rankings Over Time")
    ax.legend(loc="upper left", fontsize=8)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(CHART_PATH, dpi=150)
    plt.close(fig)
    print(f"Chart saved: {CHART_PATH}")


def main() -> None:
    print("Fetching arena data...")
    problems, leaderboards = fetch_all_data()
    print(f"Fetched {len(problems)} problems")

    # Find date range from all solutions
    all_dates: list[str] = []
    for lb in leaderboards.values():
        for s in lb:
            all_dates.append(s["createdAt"][:10])

    start_date = datetime.strptime(min(all_dates), "%Y-%m-%d")
    end_date = datetime.strptime(max(all_dates), "%Y-%m-%d")

    # Compute rankings for each day
    history: list[dict] = []
    current = start_date
    while current <= end_date:
        date_str = current.strftime("%Y-%m-%d")
        rankings = compute_rankings_for_date(problems, leaderboards, date_str)
        if rankings:  # skip days with no data
            history.append({"date": date_str, "rankings": rankings})
            # Print top 3 for this day
            top = sorted(
                rankings.items(),
                key=lambda x: (x[1]["score"], x[1]["gold"]),
                reverse=True,
            )[:3]
            top_str = ", ".join(f"{a}={d['score']}" for a, d in top)
            print(f"  {date_str}: {top_str}")
        current += timedelta(days=1)

    # Save history
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_PATH.write_text(json.dumps(history, indent=2))
    print(f"\nHistory saved: {HISTORY_PATH} ({len(history)} days)")

    # Generate chart
    generate_chart(history)


if __name__ == "__main__":
    main()
