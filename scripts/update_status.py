"""Fetch arena leaderboard and update README status section.

Saves a timestamped log to logs/status/ and updates README.md.

Usage:
    uv run python scripts/update_status.py
"""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_URL = "https://einsteinarena.com/api"
AGENT_NAME = "JSAgent"
ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs" / "status"
README = ROOT / "README.md"

# Track ALL problems
TRACKED_PROBLEMS: dict[int, str] = {}  # populated dynamically from API


def fetch_json(path: str) -> list | dict:
    req = urllib.request.Request(f"{BASE_URL}{path}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def get_problem_status(problem_id: int, title: str) -> dict:
    """Get rank 1 and our status for a problem."""
    lb = fetch_json(f"/solutions/best?problem_id={problem_id}&limit=100")

    rank1 = lb[0] if lb else None
    ours = None
    our_rank = None
    for i, entry in enumerate(lb, 1):
        if entry.get("agentName") == AGENT_NAME:
            ours = entry
            our_rank = i
            break

    return {
        "problem_id": problem_id,
        "title": title,
        "rank1_agent": rank1["agentName"] if rank1 else "N/A",
        "rank1_score": rank1["score"] if rank1 else None,
        "our_score": ours["score"] if ours else None,
        "our_rank": our_rank,
        "total_entries": len(lb),
    }


def generate_status_table(statuses: list[dict], timestamp: str) -> str:
    """Generate markdown status table."""
    lines = [
        "## Arena Status",
        "",
        f"*Last updated: {timestamp}*",
        "",
        "| # | Problem | #1 Agent | #1 Score | JSAgent Score | JSAgent Rank |",
        "|---|---------|----------|----------|---------------|--------------|",
    ]

    for s in statuses:
        r1_score = f"{s['rank1_score']:.6f}" if s["rank1_score"] else "N/A"
        our_score = f"{s['our_score']:.6f}" if s["our_score"] else "—"
        our_rank = f"#{s['our_rank']}/{s['total_entries']}" if s["our_rank"] else "—"
        is_r1 = " **#1**" if s["our_rank"] == 1 else ""
        lines.append(
            f"| {s['problem_id']} | {s['title']} | {s['rank1_agent']} | "
            f"{r1_score} | {our_score}{is_r1} | {our_rank} |"
        )

    lines.append("")
    return "\n".join(lines)


def save_log(statuses: list[dict], timestamp: str) -> Path:
    """Save timestamped log."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_path = LOG_DIR / f"status_{date_str}.md"

    content = f"# Arena Status — {timestamp}\n\n"
    for s in statuses:
        content += f"## Problem {s['problem_id']}: {s['title']}\n"
        content += f"- **#1**: {s['rank1_agent']} ({s['rank1_score']})\n"
        if s["our_score"]:
            content += f"- **JSAgent**: {s['our_score']} (rank #{s['our_rank']}/{s['total_entries']})\n"
        else:
            content += "- **JSAgent**: not attempted\n"
        content += "\n"

    log_path.write_text(content)
    return log_path


def update_readme(status_table: str) -> None:
    """Update README.md with status table between markers."""
    marker_start = "<!-- ARENA_STATUS_START -->"
    marker_end = "<!-- ARENA_STATUS_END -->"

    if not README.exists():
        return

    text = README.read_text()

    if marker_start in text and marker_end in text:
        before = text[: text.index(marker_start)]
        after = text[text.index(marker_end) + len(marker_end) :]
        text = f"{before}{marker_start}\n{status_table}\n{marker_end}{after}"
    else:
        # Append markers + table at the end
        text += f"\n{marker_start}\n{status_table}\n{marker_end}\n"

    README.write_text(text)


def main() -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"Fetching arena status at {timestamp}")

    # Fetch all problems from API
    problems = fetch_json("/problems")

    statuses = []
    for p in sorted(problems, key=lambda x: x["id"]):
        pid, title = p["id"], p["title"]
        print(f"  Problem {pid}: {title}...")
        status = get_problem_status(pid, title)
        statuses.append(status)
        r1 = f"{status['rank1_agent']} ({status['rank1_score']:.6f})"
        ours = f"#{status['our_rank']}" if status["our_rank"] else "—"
        print(f"    #1: {r1}, JSAgent: {ours}")

    # Generate outputs
    status_table = generate_status_table(statuses, timestamp)
    log_path = save_log(statuses, timestamp)
    update_readme(status_table)

    print(f"\nLog saved: {log_path}")
    print(f"README updated with {len(statuses)} problems")
    print("\n" + status_table)


if __name__ == "__main__":
    main()
