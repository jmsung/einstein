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


def fetch_json(path: str) -> list | dict:
    req = urllib.request.Request(f"{BASE_URL}{path}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def get_problem_status(problem_id: int, title: str, slug: str) -> dict:
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

    top3 = [
        entry.get("agentName", "?") for entry in lb[:3]
    ]

    # Detect tied scores: #1 tied with #2, or JSAgent tied with adjacent rank
    rank1_tied = (
        len(lb) >= 2
        and lb[0]["score"] == lb[1]["score"]
    )
    our_rank_tied = False
    if ours and our_rank:
        our_score = ours["score"]
        # Tied with rank above
        if our_rank > 1 and lb[our_rank - 2]["score"] == our_score:
            our_rank_tied = True
        # Tied with rank below
        if our_rank < len(lb) and lb[our_rank]["score"] == our_score:
            our_rank_tied = True

    return {
        "problem_id": problem_id,
        "title": title,
        "slug": slug,
        "rank1_agent": rank1["agentName"] if rank1 else "N/A",
        "rank1_score": rank1["score"] if rank1 else None,
        "rank1_tied": rank1_tied,
        "our_score": ours["score"] if ours else None,
        "our_rank": our_rank,
        "our_rank_tied": our_rank_tied,
        "total_entries": len(lb),
        "top3": top3,
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

    has_ties = False
    for s in statuses:
        r1_score = f"{s['rank1_score']:.6f}" if s["rank1_score"] else "N/A"
        our_score = f"{s['our_score']:.6f}" if s["our_score"] else "—"
        our_rank = f"#{s['our_rank']}/{s['total_entries']}" if s["our_rank"] else "—"
        # Mark tied rankings with *
        r1_agent = s["rank1_agent"]
        if s.get("rank1_tied"):
            r1_agent += " \\*"
            has_ties = True
        if s.get("our_rank_tied") and s["our_rank"]:
            our_rank += " \\*"
            has_ties = True
        problem_link = f"[{s['title']}](https://einsteinarena.com/problems/{s['slug']})"
        lines.append(
            f"| {s['problem_id']} | {problem_link} | {r1_agent} | "
            f"{r1_score} | {our_score} | {our_rank} |"
        )

    lines.append("")
    if has_ties:
        lines.append(
            "*\\* Tied score — rank order depends on submission timestamp "
            "and may differ from the leaderboard page.*"
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
        top3_str = ", ".join(
            f"#{i+1} {a}" for i, a in enumerate(s["top3"])
        )
        content += f"- **Top 3**: {top3_str}\n"
        if s["our_score"]:
            content += f"- **JSAgent**: {s['our_score']} (rank #{s['our_rank']}/{s['total_entries']})\n"
        else:
            content += "- **JSAgent**: not attempted\n"
        content += "\n"

    log_path.write_text(content)
    return log_path


def _replace_section(text: str, marker_start: str, marker_end: str, content: str) -> str:
    """Replace content between markers, or append if markers don't exist."""
    if marker_start in text and marker_end in text:
        before = text[: text.index(marker_start)]
        after = text[text.index(marker_end) + len(marker_end) :]
        return f"{before}{marker_start}\n{content}\n{marker_end}{after}"
    return text + f"\n{marker_start}\n{content}\n{marker_end}\n"


def update_readme(status_table: str) -> None:
    """Update README.md with status table."""
    if not README.exists():
        return

    text = README.read_text()
    text = _replace_section(
        text, "<!-- ARENA_STATUS_START -->", "<!-- ARENA_STATUS_END -->", status_table,
    )
    README.write_text(text)


def _load_json_set(path: Path) -> set[int]:
    """Load a JSON list of ints as a set, or empty set if missing."""
    if path.exists():
        return set(json.loads(path.read_text()))
    return set()


def check_alerts(statuses: list[dict]) -> list[str]:
    """Check for new problems and #1 position changes since last run."""
    alerts: list[str] = []
    titles = {s["problem_id"]: s["title"] for s in statuses}

    # New problems
    current_ids = {s["problem_id"] for s in statuses}
    known_ids_path = LOG_DIR / "known_problem_ids.json"
    prev_ids = _load_json_set(known_ids_path)
    for pid in sorted(current_ids - prev_ids):
        if prev_ids:  # only alert after first run
            alerts.append(f"NEW PROBLEM: #{pid} — {titles[pid]}")
    known_ids_path.write_text(json.dumps(sorted(current_ids)))

    # Lost / gained #1 positions
    curr_r1 = {s["problem_id"] for s in statuses if s["our_rank"] == 1}
    r1_path = LOG_DIR / "our_rank1_problems.json"
    prev_r1 = _load_json_set(r1_path)
    if prev_r1:  # only alert after first run
        for pid in sorted(prev_r1 - curr_r1):
            r1_agent = next(s["rank1_agent"] for s in statuses if s["problem_id"] == pid)
            alerts.append(f"LOST #1 on {titles[pid]}! New #1: {r1_agent}")
        for pid in sorted(curr_r1 - prev_r1):
            alerts.append(f"GAINED #1 on {titles[pid]}!")
    r1_path.write_text(json.dumps(sorted(curr_r1)))

    return alerts


def main() -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    print(f"Fetching arena status at {timestamp}")

    # Fetch all problems from API
    problems = fetch_json("/problems")

    statuses = []
    for p in sorted(problems, key=lambda x: x["id"]):
        pid, title, slug = p["id"], p["title"], p["slug"]
        print(f"  Problem {pid}: {title}...")
        status = get_problem_status(pid, title, slug)
        statuses.append(status)
        r1 = f"{status['rank1_agent']} ({status['rank1_score']:.6f})"
        ours = f"#{status['our_rank']}" if status["our_rank"] else "—"
        print(f"    #1: {r1}, JSAgent: {ours}")

    # Generate outputs
    status_table = generate_status_table(statuses, timestamp)
    log_path = save_log(statuses, timestamp)
    update_readme(status_table)

    # --- Alerts ---
    alerts = check_alerts(statuses)

    # Print results
    print(f"\nLog saved: {log_path}")
    print(f"README updated with {len(statuses)} problems")

    if alerts:
        print("\n--- ALERTS ---")
        for a in alerts:
            print(f"  {a}")
        print()

    print(status_table)

    # Alerts are informational only — do NOT exit with error code,
    # otherwise the CI commit step is skipped and the update never lands.


if __name__ == "__main__":
    main()
