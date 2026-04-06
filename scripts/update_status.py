"""Fetch arena leaderboard and update README status section.

Saves a timestamped log to logs/status/ and updates README.md.
Also updates historical rankings data and trend chart.

Usage:
    uv run python scripts/update_status.py
"""

from __future__ import annotations

import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE_URL = "https://einsteinarena.com/api"
AGENT_NAME = "JSAgent"
ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = ROOT / "logs" / "status"
README = ROOT / "README.md"
HISTORY_PATH = LOG_DIR / "rankings_history.json"
CHART_PATH_DARK = LOG_DIR / "rankings_chart_dark.png"
CHART_PATH_LIGHT = LOG_DIR / "rankings_chart_light.png"
DASHBOARD_PATH = ROOT / "docs" / "dashboard.html"


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

    # Top 3 agents for medal scoring
    top3 = [
        entry.get("agentName", "?") for entry in lb[:3]
    ]

    return {
        "problem_id": problem_id,
        "title": title,
        "slug": slug,
        "rank1_agent": rank1["agentName"] if rank1 else "N/A",
        "rank1_score": rank1["score"] if rank1 else None,
        "our_score": ours["score"] if ours else None,
        "our_rank": our_rank,
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

    for s in statuses:
        r1_score = f"{s['rank1_score']:.6f}" if s["rank1_score"] else "N/A"
        our_score = f"{s['our_score']:.6f}" if s["our_score"] else "—"
        our_rank = f"#{s['our_rank']}/{s['total_entries']}" if s["our_rank"] else "—"
        is_r1 = " **#1**" if s["our_rank"] == 1 else ""
        problem_link = f"[{s['title']}](https://einsteinarena.com/problems/{s['slug']})"
        lines.append(
            f"| {s['problem_id']} | {problem_link} | {s['rank1_agent']} | "
            f"{r1_score} | {our_score}{is_r1} | {our_rank} |"
        )

    lines.append("")
    return "\n".join(lines)


MEDAL_POINTS = {1: 3, 2: 2, 3: 1}  # rank → points


def compute_team_rankings(statuses: list[dict]) -> list[dict]:
    """Compute Olympic-style team rankings: rank 1/2/3 = 3/2/1 pts."""
    scores: dict[str, dict] = {}  # agent → {score, gold, silver, bronze}
    for s in statuses:
        for rank_idx, agent in enumerate(s["top3"]):
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

    # Sort by score desc, then gold desc, then silver desc
    ranked = sorted(
        scores.items(),
        key=lambda x: (x[1]["score"], x[1]["gold"], x[1]["silver"]),
        reverse=True,
    )
    return [
        {"agent": agent, **data, "rank": i + 1}
        for i, (agent, data) in enumerate(ranked)
    ]


def generate_rankings_table(rankings: list[dict], top_n: int = 10) -> str:
    """Generate markdown team rankings table with chart."""
    lines = [
        "## Team Rankings",
        "",
        "Olympic-style scoring: #1 = 3 pts, #2 = 2 pts, #3 = 1 pt, summed across all problems.",
        "",
        "| Rank | Agent | Score | #1 | #2 | #3 |",
        "|------|-------|-------|----|----|----|",
    ]
    for r in rankings[:top_n]:
        agent = f"**{r['agent']}**" if r["rank"] == 1 else r["agent"]
        lines.append(
            f"| {r['rank']} | {agent} | {r['score']} | "
            f"{r['gold']} | {r['silver']} | {r['bronze']} |"
        )
    lines.append("")
    lines.append('<picture>')
    lines.append('  <source media="(prefers-color-scheme: dark)" srcset="logs/status/rankings_chart_dark.png">')
    lines.append('  <source media="(prefers-color-scheme: light)" srcset="logs/status/rankings_chart_light.png">')
    lines.append('  <img alt="Team Rankings Over Time" src="logs/status/rankings_chart_dark.png">')
    lines.append('</picture>')
    lines.append("")
    lines.append('*<a href="https://jmsung.github.io/einstein/dashboard.html" target="_blank">View interactive dashboard</a>*')
    lines.append("")
    return "\n".join(lines)


def save_log(
    statuses: list[dict], rankings: list[dict], timestamp: str,
) -> Path:
    """Save timestamped log."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log_path = LOG_DIR / f"status_{date_str}.md"

    content = f"# Arena Status — {timestamp}\n\n"

    # Team rankings
    content += "## Team Rankings\n\n"
    content += "| Rank | Agent | Score | #1 | #2 | #3 |\n"
    content += "|------|-------|-------|----|----|----|"
    for r in rankings:
        content += (
            f"\n| {r['rank']} | {r['agent']} | {r['score']} | "
            f"{r['gold']} | {r['silver']} | {r['bronze']} |"
        )
    content += "\n\n"

    # Per-problem status
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


def update_readme(status_table: str, rankings_table: str) -> None:
    """Update README.md with status and rankings tables."""
    if not README.exists():
        return

    text = README.read_text()
    text = _replace_section(
        text, "<!-- ARENA_STATUS_START -->", "<!-- ARENA_STATUS_END -->", status_table,
    )
    text = _replace_section(
        text, "<!-- TEAM_RANKINGS_START -->", "<!-- TEAM_RANKINGS_END -->", rankings_table,
    )
    README.write_text(text)


def update_rankings_history(rankings: list[dict]) -> list[dict]:
    """Append today's rankings to history file and return full history."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Load existing history
    history: list[dict] = []
    if HISTORY_PATH.exists():
        history = json.loads(HISTORY_PATH.read_text())

    # Convert rankings list to dict for storage
    rankings_dict = {
        r["agent"]: {"score": r["score"], "gold": r["gold"], "silver": r["silver"], "bronze": r["bronze"]}
        for r in rankings
    }

    # Update or append today's entry
    updated = False
    for entry in history:
        if entry["date"] == today:
            entry["rankings"] = rankings_dict
            updated = True
            break
    if not updated:
        history.append({"date": today, "rankings": rankings_dict})

    history.sort(key=lambda h: h["date"])
    HISTORY_PATH.write_text(json.dumps(history, indent=2))
    return history


def _get_top_agents(history: list[dict], top_n: int = 8) -> list[str]:
    """Get top N agents by latest score."""
    latest = history[-1]["rankings"]
    top_sorted = sorted(
        latest.items(), key=lambda x: (x[1]["score"], x[1]["gold"]), reverse=True,
    )[:top_n]
    return [a for a, _ in top_sorted]


def _extract_series(history: list[dict], agents: list[str]) -> tuple[list[str], dict[str, list[int]]]:
    """Extract date strings and score series per agent."""
    dates = [h["date"] for h in history]
    series: dict[str, list[int]] = {}
    for agent in agents:
        series[agent] = [
            h["rankings"].get(agent, {}).get("score", 0) for h in history
        ]
    return dates, series


# Rank-based rainbow palette: red → orange → yellow → green → blue.
# Rank 1 gets red for maximum attention.
RANK_COLORS = [
    "#e63946",  # #1 — red
    "#ff7f0e",  # #2 — orange
    "#e7b416",  # #3 — gold (darker yellow for visibility on white bg)
    "#2ca02c",  # #4 — green
    "#1f77b4",  # #5 — blue
]
RANK_WIDTHS = [3.2, 2.8, 2.4, 2.0, 1.8]
RANK_ALPHAS = [1.0, 0.95, 0.9, 0.85, 0.8]


def _render_chart(history: list[dict], path: Path, top_n: int,
                   bg: str, text: str, grid: str) -> None:
    """Render a single chart variant."""
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt
    import numpy as np

    agents = _get_top_agents(history, top_n)
    date_strs, series = _extract_series(history, agents)
    dates = [datetime.strptime(d, "%Y-%m-%d") for d in date_strs]
    latest = history[-1]["rankings"]

    fig, ax = plt.subplots(figsize=(10, 5), facecolor=bg)
    ax.set_facecolor(bg)
    date_nums = mdates.date2num(dates)

    for i, agent in enumerate(agents):
        scores = np.array(series[agent], dtype=float)
        score = latest.get(agent, {}).get("score", 0)
        label = f"#{i+1} {agent} ({score}pts)"
        color = RANK_COLORS[i] if i < len(RANK_COLORS) else "#444444"
        width = RANK_WIDTHS[i] if i < len(RANK_WIDTHS) else 1.2
        alpha = RANK_ALPHAS[i] if i < len(RANK_ALPHAS) else 0.4
        if len(dates) >= 3:
            from scipy.interpolate import PchipInterpolator
            x_smooth = np.linspace(date_nums[0], date_nums[-1], 300)
            pchip = PchipInterpolator(date_nums, scores)
            y_smooth = pchip(x_smooth)
            ax.plot(mdates.num2date(x_smooth), y_smooth, linewidth=width,
                    solid_capstyle="round", label=label,
                    color=color, alpha=alpha)
        else:
            ax.plot(dates, scores, linewidth=width, label=label,
                    color=color, alpha=alpha)
        ax.scatter(dates, scores, s=24, zorder=5, color=color, alpha=alpha)

    ax.set_xlabel("Date", color=text)
    ax.set_ylabel("Score (3/2/1 for rank 1/2/3)", color=text)
    ax.set_title("Einstein Arena — Team Rankings Over Time", color=text)
    ax.legend(loc="upper left", fontsize=8, facecolor=bg, edgecolor=grid,
              labelcolor=text)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax.tick_params(colors=text)
    ax.grid(True, alpha=0.3, color=grid)
    for spine in ax.spines.values():
        spine.set_color(grid)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(path, dpi=150, facecolor=bg)
    plt.close(fig)


def generate_chart(history: list[dict], top_n: int = 5) -> None:
    """Generate dark and light chart PNGs for README."""
    _render_chart(history, CHART_PATH_DARK, top_n,
                  bg="#0d1117", text="#c9d1d9", grid="#21262d")
    _render_chart(history, CHART_PATH_LIGHT, top_n,
                  bg="#ffffff", text="#1f2328", grid="#d1d9e0")
    print(f"Charts saved: {CHART_PATH_DARK}, {CHART_PATH_LIGHT}")


def generate_dashboard(history: list[dict], top_n: int = 5) -> None:
    """Generate interactive HTML dashboard with Plotly.js."""
    agents = _get_top_agents(history, top_n)
    date_strs, series = _extract_series(history, agents)

    # Build Plotly traces as JSON
    latest = history[-1]["rankings"]
    traces = []
    for i, agent in enumerate(agents):
        score = latest.get(agent, {}).get("score", 0)
        color = RANK_COLORS[i] if i < len(RANK_COLORS) else "#444444"
        width = RANK_WIDTHS[i] if i < len(RANK_WIDTHS) else 1.2
        traces.append({
            "x": date_strs,
            "y": series[agent],
            "name": f"#{i+1} {agent} ({score}pts)",
            "mode": "lines+markers",
            "line": {"shape": "spline", "smoothing": 1.0, "width": width,
                     "color": color},
            "marker": {"size": 6, "color": color},
        })

    traces_json = json.dumps(traces)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Einstein Arena — Team Rankings Dashboard</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    margin: 0; padding: 20px; background: #0d1117; color: #c9d1d9;
  }}
  h1 {{ text-align: center; margin-bottom: 4px; }}
  .subtitle {{ text-align: center; color: #8b949e; margin-bottom: 20px; font-size: 14px; }}
  .chart-container {{ max-width: 1000px; margin: 0 auto; }}
  .range-buttons {{
    display: flex; justify-content: center; gap: 8px; margin-bottom: 16px;
  }}
  .range-buttons button {{
    padding: 8px 20px; border: 1px solid #30363d; border-radius: 6px;
    background: #21262d; color: #c9d1d9; cursor: pointer; font-size: 14px;
  }}
  .range-buttons button:hover {{ background: #30363d; }}
  .range-buttons button.active {{
    background: #1f6feb; border-color: #1f6feb; color: #fff;
  }}
  .home-link {{
    position: absolute; top: 16px; left: 20px;
    color: #58a6ff; text-decoration: none; font-size: 14px;
  }}
  .home-link:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<a class="home-link" href="https://github.com/jmsung/einstein">&larr; Back to repo</a>
<h1>Einstein Arena — Team Rankings</h1>
<p class="subtitle">Olympic scoring: #1 = 3 pts, #2 = 2 pts, #3 = 1 pt per problem</p>
<div class="chart-container">
  <div class="range-buttons">
    <button onclick="setRange(7)" id="btn-7d">Last 7 days</button>
    <button onclick="setRange(30)" id="btn-30d">Last 30 days</button>
    <button onclick="setRange(90)" id="btn-90d">Last 90 days</button>
    <button onclick="setRange(0)" id="btn-all" class="active">All time</button>
  </div>
  <div id="chart"></div>
</div>
<script>
const allTraces = {traces_json};
const allDates = {json.dumps(date_strs)};

const layout = {{
  paper_bgcolor: '#0d1117',
  plot_bgcolor: '#0d1117',
  font: {{ color: '#c9d1d9' }},
  xaxis: {{
    gridcolor: '#21262d',
    tickformat: '%m-%d',
  }},
  yaxis: {{
    title: 'Score',
    gridcolor: '#21262d',
  }},
  legend: {{
    bgcolor: 'rgba(0,0,0,0)',
    font: {{ size: 11 }},
  }},
  margin: {{ t: 20, b: 50, l: 60, r: 20 }},
  hovermode: 'x unified',
}};

const config = {{ responsive: true, displayModeBar: false }};

Plotly.newPlot('chart', allTraces, layout, config);

function setRange(days) {{
  document.querySelectorAll('.range-buttons button').forEach(b => b.classList.remove('active'));
  if (days === 7) document.getElementById('btn-7d').classList.add('active');
  else if (days === 30) document.getElementById('btn-30d').classList.add('active');
  else if (days === 90) document.getElementById('btn-90d').classList.add('active');
  else document.getElementById('btn-all').classList.add('active');

  if (days === 0) {{
    Plotly.relayout('chart', {{ 'xaxis.range': [allDates[0], allDates[allDates.length - 1]] }});
  }} else {{
    const end = new Date(allDates[allDates.length - 1]);
    const start = new Date(end);
    start.setDate(start.getDate() - days);
    Plotly.relayout('chart', {{
      'xaxis.range': [start.toISOString().slice(0, 10), end.toISOString().slice(0, 10)]
    }});
  }}
}}
</script>
</body>
</html>"""

    DASHBOARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    DASHBOARD_PATH.write_text(html)
    print(f"Dashboard saved: {DASHBOARD_PATH}")


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

    # Compute team rankings
    rankings = compute_team_rankings(statuses)

    # Generate outputs
    status_table = generate_status_table(statuses, timestamp)
    rankings_table = generate_rankings_table(rankings)
    log_path = save_log(statuses, rankings, timestamp)
    update_readme(status_table, rankings_table)

    # Update history, generate chart and dashboard
    history = update_rankings_history(rankings)
    generate_chart(history)
    generate_dashboard(history)

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
    print()
    print(rankings_table)

    # Non-zero exit if there are alerts (useful for cron notifications)
    if alerts:
        sys.exit(1)


if __name__ == "__main__":
    main()
