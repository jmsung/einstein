"""Local status dashboard for the autonomous loop — single self-contained HTML.

Reads the ledgers the loop already writes (no new data sources) and renders one
auto-refreshing page: live loop status, today's cost/budget, per-problem records
(our score vs arena #1 + headroom), recent cycles, and auto-submit decisions.

    uv run python docs/tools/dashboard.py            # write mb/logs/dashboard.html
    uv run python docs/tools/dashboard.py --open      # write + open in browser
    uv run python docs/tools/dashboard.py --serve 8787 # serve at localhost:8787

Regenerated each cycle by `docs/tools/cycle_runner.sh`. Open the file directly
(file://) — the `<meta refresh>` keeps it current; or use --serve for http://.

Pure aggregation lives in the `*_summary` / `parse_*` functions (tested in
tests/tools/test_dashboard.py); `render_html` is the only presentation seam.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import signal
import subprocess
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
_REPO = _TOOLS.parent.parent  # cb/
_MB = _REPO.parent / "mb"
_LOGS = _MB / "logs"

DEFAULT_OUT = _LOGS / "dashboard.html"
TELEMETRY = _LOGS / "inner-agent-telemetry.jsonl"
CYCLE_LOG = _REPO / "docs" / "agent" / "cycle-log.md"
RUN_LEDGER = _LOGS / "scheduler-runs.log"
BUDGET = _LOGS / "inner-agent-budget.md"
AUTO_SUBMIT = _LOGS / "auto-submit.md"
HEADROOM_CACHE = _LOGS / "headroom-cache.json"
RANK1_JSON = _LOGS / "status" / "our_rank1_problems.json"
SENTINEL = _MB / ".inner-agent-disabled"
LOCKFILE = _REPO / ".autonomous-loop.lock"

DAILY_TOKEN_BUDGET = 5_000_000  # axioms.md / precheck hard ceiling
REFRESH_S = 30


# ----------------------------- parsing -----------------------------


def _read_text(p: Path) -> str:
    try:
        return p.read_text()
    except OSError:
        return ""


def parse_telemetry(path: Path = TELEMETRY) -> list[dict]:
    """All telemetry rows (one completed claude -p call each), oldest first."""
    rows = []
    for line in _read_text(path).splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            continue
    return rows


_CYCLE_RE = re.compile(r"^\|\s*(\d+)\s*\|")


def parse_cycle_log(path: Path = CYCLE_LOG) -> list[dict]:
    """Parse the pipe-table cycle rows → dicts. Tolerant of column drift."""
    rows = []
    for line in _read_text(path).splitlines():
        if not _CYCLE_RE.match(line.strip()):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 11 or not cells[0].isdigit():
            continue
        rows.append(
            {
                "cycle_id": int(cells[0]),
                "problem": cells[1],
                "score": cells[2],
                "hours": cells[3],
                "compute": cells[4],
                "findings_added": cells[6],
                "outcome": cells[9],
                "notes": cells[10],
            }
        )
    return rows


def parse_strategy(notes: str) -> dict:
    """Pull strategy/technique/llm-move/category out of a cycle-log notes cell.

    Notes are semicolon-ish key=value soup, e.g.
    `... strategy=thompson-bandit; ... technique=warm-self-pruning-compact-support.md
     prior=Beta(3,3) sampled_θ=0.58; llm-strategy=skip-execution-converged-... ;`
    """

    def grab(pat, default=""):
        m = re.search(pat, notes)
        return m.group(1).strip() if m else default

    return {
        "strategy": grab(r"strategy=([^;]+)"),
        "technique": grab(r"technique=(\S+?\.md)").removesuffix(".md"),
        "llm_move": grab(r"llm-strategy=([^;]+)"),
        "category": grab(r"category=([^;]+)"),
        "theta": grab(r"sampled_θ=([\d.]+)"),
    }


def recent_attempts(cycle_rows: list[dict], label: str, n: int = 6) -> list[dict]:
    """Last n cycles for one problem, newest first, with strategy parsed."""
    mine = [r for r in cycle_rows if r["problem"] == label][-n:][::-1]
    return [{**r, **parse_strategy(r.get("notes", ""))} for r in mine]


def parse_headroom_cache(path: Path = HEADROOM_CACHE) -> dict[int, float]:
    try:
        data = json.loads(_read_text(path) or "{}")
        return {int(k): float(v["arena1"]) for k, v in data.items() if v.get("arena1") is not None}
    except (ValueError, KeyError, TypeError):
        return {}


def parse_rank1(path: Path = RANK1_JSON) -> set[int]:
    try:
        return set(json.loads(_read_text(path) or "[]"))
    except ValueError:
        return set()


_STATUS_DIR = _LOGS / "status"


def parse_rank1_agents(status_dir: Path = _STATUS_DIR) -> tuple[dict[int, str], str]:
    """{problem_id: arena-#1 agent name} from the latest status_*.md snapshot.

    Source: `scripts/update_status.py` writes blocks like
        ## Problem 4: Third Autocorrelation ...
        - **#1**: OrganonAgent (1.4523...)
    Returns ({}, "") if no snapshot exists. Also returns the snapshot date.
    """
    try:
        latest = max(status_dir.glob("status_*.md"), key=lambda p: p.name, default=None)
    except OSError:
        latest = None
    if latest is None:
        return {}, ""
    text = _read_text(latest)
    agents: dict[int, str] = {}
    cur: int | None = None
    for line in text.splitlines():
        m = re.match(r"##\s*Problem\s+(\d+)\s*:", line)
        if m:
            cur = int(m.group(1))
            continue
        m = re.match(r"-\s*\*\*#1\*\*:\s*([^(]+?)\s*\(", line)
        if m and cur is not None:
            agents[cur] = m.group(1).strip()
            cur = None
    return agents, latest.stem.replace("status_", "")


# ----------------------------- summaries -----------------------------


def today_summary(telemetry: list[dict], *, today: str) -> dict:
    """Today's cycle count, cost, tokens, fallback count from telemetry."""
    rows = [r for r in telemetry if str(r.get("ts", "")).startswith(today)]
    n = len(rows)
    cost = sum(r.get("cost_usd", 0) or 0 for r in rows)
    tokens = sum((r.get("input_tokens", 0) or 0) + (r.get("output_tokens", 0) or 0) for r in rows)
    fb = sum(1 for r in rows if r.get("path_taken") != "llm")
    return {
        "cycles": n,
        "cost": cost,
        "tokens": tokens,
        "fallback": fb,
        "budget_pct": (100 * tokens / DAILY_TOKEN_BUDGET) if DAILY_TOKEN_BUDGET else 0,
    }


def loop_status(
    *, lockfile: Path = LOCKFILE, sentinel: Path = SENTINEL, ledger: Path = RUN_LEDGER
) -> dict:
    """Is the loop running / killed, and when did it last run?"""
    last_run = ""
    led = _read_text(ledger).splitlines()
    if led:
        last_run = led[-1]
    return {
        "running": lockfile.exists(),
        "killed": sentinel.exists(),
        "last_run": last_run,
    }


def relative_headroom(
    our: float | None, arena1: float | None, minimize: bool | None
) -> float | None:
    if our is None or arena1 is None or minimize is None:
        return None
    gap = (our - arena1) if minimize else (arena1 - our)
    return max(gap, 0.0) / max(abs(arena1), 1e-12)


def per_problem_records(
    problems,
    headroom: dict[int, float],
    rank1: set[int],
    cycle_rows: list[dict],
    minimize_map: dict[int, bool],
    priority_scorer=None,
    rank1_agents: dict[int, str] | None = None,
) -> list[dict]:
    """One record per problem: our score, arena #1, headroom %, rank1, activity.

    `priority_scorer(rec) -> float | None` ranks the queue exactly as the loop's
    picker does (headroom × hit-rate × staleness). When None, falls back to raw
    headroom so the function stays usable standalone.
    """
    # cycle activity by problem label
    last_cycle: dict[str, int] = {}
    count: dict[str, int] = {}
    for r in cycle_rows:
        lbl = r["problem"]
        count[lbl] = count.get(lbl, 0) + 1
        last_cycle[lbl] = max(last_cycle.get(lbl, 0), r["cycle_id"])
    recs = []
    for p in problems:
        pid = p.problem_id
        lbl = f"P{pid}-{p.slug}"
        arena1 = headroom.get(pid)
        minz = minimize_map.get(pid)
        hr = relative_headroom(p.score_current, arena1, minz)
        recs.append(
            {
                "pid": pid,
                "label": lbl,
                "name": getattr(p, "name", p.slug),
                "tier": p.tier,
                "status": p.status,
                "ours": p.score_current,
                "arena1": arena1,
                "arena1_agent": (rank1_agents or {}).get(pid, ""),
                "headroom": hr,
                "rank1": pid in rank1,
                "last_cycle": last_cycle.get(lbl, 0),
                "cycles": count.get(lbl, 0),
            }
        )
    for r in recs:
        r["priority"] = priority_scorer(r) if priority_scorer else r["headroom"]
    # highest priority first; unknowns (None) last; ties by id
    recs.sort(key=lambda r: (r["priority"] is None, -(r["priority"] or 0), r["pid"]))
    return recs


def current_problem(
    cycle_rows: list[dict], telemetry: list[dict], records: list[dict], *, running: bool
) -> dict | None:
    """The problem the loop is on right now (running) or up next (idle).

    Running → the latest cycle-log row's problem. Idle → the highest-headroom
    record (what --by-priority would pick next). Enriches with the latest
    telemetry attempt (path/cost/ts) and the matched per-problem record.
    """
    by_label = {r["label"]: r for r in records}
    latest_row = max(cycle_rows, key=lambda r: r["cycle_id"]) if cycle_rows else {}
    if running and latest_row:
        rec = by_label.get(latest_row["problem"])
        mode = "running"
    elif records:
        rec = records[0]
        mode = "next"
    else:
        return None
    if rec is None:
        return None
    last = telemetry[-1] if telemetry else {}
    strat = parse_strategy(latest_row.get("notes", "")) if mode == "running" else {}
    return {
        "mode": mode,
        "label": rec["label"],
        "name": rec["name"],
        "tier": rec["tier"],
        "status": rec["status"],
        "ours": rec["ours"],
        "arena1": rec["arena1"],
        "headroom": rec["headroom"],
        "attempt": last.get("attempt_index"),
        "path": last.get("path_taken"),
        "cost": last.get("cost_usd"),
        "ts": last.get("ts", ""),
        "strategy": strat.get("strategy", ""),
        "technique": strat.get("technique", ""),
        "llm_move": strat.get("llm_move", ""),
        "theta": strat.get("theta", ""),
    }


# ----------------------------- control actions (--serve only) -----------------------------

_SCHED_LOG = _LOGS / "scheduler.log"
CONTROL_LOG = _LOGS / "dashboard-control.log"
LAUNCHD_LABEL = "com.einstein.autonomous-loop"
FINDINGS_DIR = _REPO / "docs" / "wiki" / "findings"

# Allowlisted log files the viewer may render (name → path). No arbitrary reads.
LOG_FILES = {
    "cycle-log": CYCLE_LOG,
    "scheduler": _SCHED_LOG,
    "scheduler-err": _LOGS / "scheduler.err.log",
    "auto-submit": AUTO_SUBMIT,
    "budget": BUDGET,
    "telemetry": TELEMETRY,
    "control": CONTROL_LOG,
}


def _audit(action: str, result: str) -> None:
    try:
        CONTROL_LOG.parent.mkdir(parents=True, exist_ok=True)
        with CONTROL_LOG.open("a") as f:
            f.write(f"{dt.datetime.now(dt.timezone.utc).isoformat()} {action} → {result}\n")
    except OSError:
        pass


def action_start(pid: int) -> str:
    """Spawn a detached one-problem loop run for problem `pid`."""
    cmd = [
        sys.executable,
        str(_REPO / "scripts" / "autonomous_loop.py"),
        "--one-problem",
        "--by-priority",
        "--problem-id",
        str(pid),
    ]
    try:
        out = _SCHED_LOG.open("a")
        subprocess.Popen(  # noqa: S603 — fixed argv, local control plane
            cmd, cwd=str(_REPO), stdout=out, stderr=subprocess.STDOUT, start_new_session=True
        )
        res = f"spawned loop for P{pid} (pid-detached)"
    except OSError as e:
        res = f"start failed: {e}"
    _audit(f"start P{pid}", res)
    return res


def action_stop(lockfile: Path = LOCKFILE) -> str:
    """SIGTERM the running loop via its lockfile pid (graceful)."""
    try:
        m = re.search(r"pid=(\d+)", lockfile.read_text())
    except OSError:
        m = None
    if not m:
        res = "no running loop (no lockfile)"
    else:
        pid = int(m.group(1))
        try:
            os.kill(pid, signal.SIGTERM)
            res = f"SIGTERM → pid {pid}"
        except ProcessLookupError:
            res = f"pid {pid} already gone (stale lockfile)"
        except OSError as e:
            res = f"stop failed: {e}"
    _audit("stop", res)
    return res


def action_auto(on: bool) -> str:
    """Toggle the launchd schedule (real auto-mode on/off)."""
    uid = os.getuid()
    plist = Path.home() / "Library" / "LaunchAgents" / f"{LAUNCHD_LABEL}.plist"
    if on:
        cmd = ["launchctl", "bootstrap", f"gui/{uid}", str(plist)]
    else:
        cmd = ["launchctl", "bootout", f"gui/{uid}/{LAUNCHD_LABEL}"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=15)  # noqa: S603
        res = f"auto {'ON' if on else 'OFF'} (launchctl rc={r.returncode})"
    except (OSError, subprocess.SubprocessError) as e:
        res = f"auto toggle failed: {e}"
    _audit(f"auto {'on' if on else 'off'}", res)
    return res


def action_kill(on: bool, sentinel: Path = SENTINEL) -> str:
    """Toggle the kill-switch sentinel (pause/resume everything)."""
    try:
        if on:
            sentinel.parent.mkdir(parents=True, exist_ok=True)
            sentinel.write_text("disabled via dashboard\n")
            res = "kill switch ON (loop paused)"
        else:
            sentinel.unlink(missing_ok=True)
            res = "kill switch OFF (loop re-enabled)"
    except OSError as e:
        res = f"kill toggle failed: {e}"
    _audit(f"kill {'on' if on else 'off'}", res)
    return res


def read_log(name: str, *, tail: int = 200) -> tuple[str, str]:
    """Return (title, last-`tail`-lines) for an allowlisted log or a finding.

    `name` is either a LOG_FILES key, or 'finding:<slug>' restricted to
    docs/wiki/findings/ (path-traversal guarded). Returns an error string in
    the body for unknown/unsafe names — never reads outside the allowlist.
    """
    if name.startswith("finding:"):
        slug = name.split(":", 1)[1]
        path = (FINDINGS_DIR / f"{slug}.md").resolve()
        if FINDINGS_DIR.resolve() not in path.parents:
            return (name, "refused: path escapes findings/")
        title = f"finding · {slug}"
    elif name in LOG_FILES:
        path = LOG_FILES[name]
        title = f"log · {name}"
    else:
        return (name, f"refused: '{name}' not in the allowlist")
    lines = _read_text(path).splitlines()
    body = "\n".join(lines[-tail:]) if lines else "(empty)"
    return (title, body)


# ----------------------------- render -----------------------------


def _fmt(x, nd=6):
    if x is None:
        return "—"
    if isinstance(x, float):
        return f"{x:.{nd}g}"
    return str(x)


def _hr_badge(hr):
    if hr is None:
        return '<span class="b gray">n/a</span>'
    if hr <= 0:
        return '<span class="b green">SOTA</span>'
    return f'<span class="b amber">{hr*100:.3g}%</span>'


def render_html(
    *,
    status: dict,
    today: dict,
    current: dict | None,
    attempts: list[dict],
    records: list[dict],
    recent_cycles: list[dict],
    submits: list[str],
    health: str,
    generated: str,
    controls: bool = False,
) -> str:
    rows_problems = "\n".join(
        f"<tr class='{'r1' if r['rank1'] else ''}'>"
        f"<td class='num'>{i}</td>"
        f"<td>P{r['pid']}</td><td class='nm'>{r['name']}</td>"
        f"<td>{r['tier']}</td><td class='st'>{r['status']}</td>"
        f"<td class='num'>{_fmt(r['ours'])}</td><td class='num'>{_fmt(r['arena1'])}</td>"
        f"<td class='ag'>{r.get('arena1_agent') or '—'}</td>"
        f"<td>{_hr_badge(r['headroom'])}</td>"
        f"<td class='num'>{_fmt(r.get('priority'), 3) if r.get('priority') is not None else '—'}</td>"
        f"<td>{'★' if r['rank1'] else ''}</td>"
        f"<td class='num'>{r['cycles']}</td><td class='num'>#{r['last_cycle'] or '—'}</td>"
        + (
            f"<td><form method=post action=/start style=margin:0>"
            f"<input type=hidden name=pid value={r['pid']}>"
            f"<button class=run title='start one cycle on P{r['pid']}'>▶</button></form></td>"
            if controls
            else ""
        )
        + "</tr>"
        for i, r in enumerate(records, 1)
    )
    rows_cycles = "\n".join(
        f"<tr><td class='num'>#{c['cycle_id']}</td><td class='nm'>{c['problem']}</td>"
        f"<td class='num'>{c['score']}</td><td>{c['outcome']}</td>"
        f"<td class='num'>{c.get('cost','')}</td></tr>"
        for c in recent_cycles
    )
    rows_submit = "\n".join(f"<li><code>{s}</code></li>" for s in submits) or "<li>none today</li>"
    run_state = (
        "🟢 RUNNING"
        if status["running"]
        else (
            "🛑 KILLED (sentinel)" if status["killed"] else "⚪ idle (waiting for next 30-min slot)"
        )
    )
    health_cls = "green" if health.startswith("HEALTHY") else "amber"
    budget_cls = "amber" if today["budget_pct"] > 80 else "green"
    if current is None:
        hero = ""
    else:
        verb = "🟢 working on" if current["mode"] == "running" else "⏭ up next (highest headroom)"
        att = (
            f" · attempt {current['attempt']} · {current['path']} · ${current['cost']:.2f}"
            if current.get("attempt") is not None and current["mode"] == "running"
            else ""
        )
        strat_line = ""
        if current["mode"] == "running" and current.get("technique"):
            th = f" · θ={current['theta']}" if current.get("theta") else ""
            mv = (
                f" → <span class=mv>{current['llm_move']}</span>" if current.get("llm_move") else ""
            )
            strat_line = (
                f"<div class=hs>strategy <b>{current['strategy'] or '—'}</b>{th} · "
                f"technique <b>{current['technique']}</b>{mv}</div>"
            )
        hero = f"""<div class=hero>
 <div class=k>{verb}</div>
 <div class=hp>{current['label']} <span class=ht>{current['name']}</span></div>
 <div class=hm>tier {current['tier']} · {current['status']} · ours {_fmt(current['ours'])} ·
   arena #1 {_fmt(current['arena1'])} · headroom {_hr_badge(current['headroom'])}{att}</div>
 {strat_line}
</div>"""
    rows_attempts = "\n".join(
        f"<tr><td class='num'>#{a['cycle_id']}</td><td class='nm'>{a.get('technique') or '—'}</td>"
        f"<td>{a.get('llm_move') or a['outcome']}</td><td class='num'>{a['score']}</td>"
        f"<td>{a['outcome']}</td></tr>"
        for a in attempts
    )
    attempts_block = (
        f"<h2>Recent attempts on {current['label']} — what was tried</h2>"
        f"<table><tr><th>cycle</th><th>technique</th><th>move</th><th>score</th><th>outcome</th></tr>{rows_attempts}</table>"
        if (current and attempts)
        else ""
    )
    if controls:
        killed = status["killed"]
        control_bar = (
            "<div class=ctl>"
            "<form method=post action=/stop><button class=warn>⏹ Stop loop</button></form>"
            "<form method=post action=/auto/on><button>▶ Auto on</button></form>"
            "<form method=post action=/auto/off><button class=warn>⏸ Auto off</button></form>"
            + (
                "<form method=post action=/kill/off><button>✅ Resume (clear kill)</button></form>"
                if killed
                else "<form method=post action=/kill/on><button class=danger>🛑 Kill switch</button></form>"
            )
            + "</div>"
        )
        links = "".join(f"<a href='/log?name={n}'>{n}</a>" for n in LOG_FILES)
        log_links = f"<h2>Logs</h2><div class=links>{links}</div>"
        start_th = "<th>start</th>"
    else:
        control_bar = log_links = start_th = ""
    return f"""<!doctype html><html><head><meta charset=utf-8>
<meta http-equiv=refresh content={REFRESH_S}>
<title>einstein · autonomous loop</title>
<style>
 :root{{--bg:#0d1117;--card:#161b22;--bd:#30363d;--fg:#c9d1d9;--mut:#8b949e}}
 *{{box-sizing:border-box}} body{{margin:0;background:var(--bg);color:var(--fg);
   font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace}}
 .wrap{{max-width:1180px;margin:0 auto;padding:20px}}
 h1{{font-size:17px;margin:0 0 2px}} .sub{{color:var(--mut);font-size:11px;margin-bottom:16px}}
 .cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-bottom:18px}}
 .card{{background:var(--card);border:1px solid var(--bd);border-radius:8px;padding:12px}}
 .card .k{{color:var(--mut);font-size:10px;text-transform:uppercase;letter-spacing:.05em}}
 .card .v{{font-size:20px;margin-top:4px}}
 h2{{font-size:12px;color:var(--mut);text-transform:uppercase;letter-spacing:.06em;
   border-bottom:1px solid var(--bd);padding-bottom:6px;margin:22px 0 8px}}
 table{{width:100%;border-collapse:collapse}} th,td{{text-align:left;padding:5px 8px;border-bottom:1px solid var(--bd)}}
 th{{color:var(--mut);font-weight:400;font-size:10px;text-transform:uppercase}}
 td.num{{text-align:right;font-variant-numeric:tabular-nums}} td.nm{{color:#79c0ff}}
 td.st{{color:var(--mut);font-size:11px}} tr.r1 td.nm{{color:#7ee787}}
 td.ag{{color:#d2a8ff;font-size:11px}}
 .b{{padding:1px 6px;border-radius:10px;font-size:11px}}
 .green{{background:#1b3a26;color:#7ee787}} .amber{{background:#3a341b;color:#e3b341}} .gray{{background:#21262d;color:#8b949e}}
 code{{color:var(--mut);font-size:11px}} ul{{margin:6px 0;padding-left:18px}}
 .state{{font-size:15px}}
 .hero{{background:linear-gradient(135deg,#161b22,#1b2530);border:1px solid #2d4a3a;
   border-radius:10px;padding:16px 18px;margin-bottom:18px}}
 .hero .k{{color:var(--mut);font-size:10px;text-transform:uppercase;letter-spacing:.06em}}
 .hp{{font-size:24px;color:#7ee787;margin:4px 0}} .hp .ht{{color:var(--mut);font-size:14px}}
 .hm{{color:var(--fg);font-size:12px}}
 .hs{{margin-top:8px;font-size:12px;color:var(--fg)}} .hs b{{color:#79c0ff;font-weight:600}}
 .mv{{color:#e3b341}}
 .ctl{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px}}
 .ctl form{{margin:0}}
 button{{background:#21304a;color:#c9d1d9;border:1px solid #30557d;border-radius:6px;
   padding:6px 12px;font:inherit;font-size:12px;cursor:pointer}}
 button:hover{{background:#2b4a6e}}
 button.warn{{background:#3a341b;border-color:#6e5b1f}} button.danger{{background:#3a1b1b;border-color:#7d3030}}
 button.run{{padding:2px 8px;font-size:12px}}
 .links a{{color:#79c0ff;margin-right:14px;font-size:12px}}
</style></head><body><div class=wrap>
<h1>einstein · autonomous loop</h1>
<div class=sub>generated {generated} · auto-refresh {REFRESH_S}s · <span class=state>{run_state}</span></div>
{control_bar}
{hero}

<div class=cards>
 <div class=card><div class=k>health</div><div class="v {health_cls}">{health.split(' ')[0]}</div><div class=sub>{health}</div></div>
 <div class=card><div class=k>cycles today</div><div class=v>{today['cycles']}</div></div>
 <div class=card><div class=k>spend today</div><div class=v>${today['cost']:.2f}</div></div>
 <div class=card><div class=k>tokens today</div><div class="v {budget_cls}">{today['tokens']:,}</div><div class=sub>{today['budget_pct']:.1f}% of 5M</div></div>
 <div class=card><div class=k>fallbacks today</div><div class=v>{today['fallback']}</div></div>
 <div class=card><div class=k>last run</div><div class=sub style=margin-top:6px>{status['last_run'] or '—'}</div></div>
</div>

{attempts_block}

<h2>Per-problem records — ranked by picker priority (headroom × hit-rate × staleness)</h2>
<table><tr><th>#</th><th>id</th><th>problem</th><th>tier</th><th>status</th><th>ours</th><th>arena #1</th><th>#1 agent</th><th>headroom</th><th>priority</th><th>we&nbsp;#1?</th><th>cycles</th><th>last</th>{start_th}</tr>
{rows_problems}
</table>

<h2>Recent cycles</h2>
<table><tr><th>cycle</th><th>problem</th><th>score</th><th>outcome</th><th>cost</th></tr>
{rows_cycles}
</table>

<h2>Auto-submit decisions (today)</h2>
<ul>{rows_submit}</ul>
{log_links}
</div></body></html>"""


# ----------------------------- assembly -----------------------------


def build(*, today: str | None = None, generated: str | None = None, controls: bool = False) -> str:
    now = dt.datetime.now(dt.timezone.utc)
    today = today or now.strftime("%Y-%m-%d")
    generated = generated or now.strftime("%Y-%m-%d %H:%M:%SZ")

    telemetry = parse_telemetry()
    cycle_rows = parse_cycle_log()
    headroom = parse_headroom_cache()
    rank1 = parse_rank1()
    rank1_agents, rank1_asof = parse_rank1_agents()
    status = loop_status()
    today_s = today_summary(telemetry, today=today)

    # problems + direction map via the loop's own loaders (single source of truth)
    problems, minimize_map, scorer = [], {}, None
    try:
        sys.path.insert(0, str(_REPO / "scripts"))
        sys.path.insert(0, str(_REPO / "src"))
        sys.path.insert(0, str(_TOOLS))
        from autonomous_loop import (
            DEFAULT_CYCLE_LOG,
            DEFAULT_PROBLEMS_DIR,
            DEFAULT_SKILL_LIBRARY,
            load_problems,
        )

        from einstein.auto_submit import PROBLEM_MINIMIZE

        problems = load_problems(DEFAULT_PROBLEMS_DIR)
        minimize_map = dict(PROBLEM_MINIMIZE)

        # Rank exactly as the picker does: headroom × hit-rate × staleness.
        import problem_priority as pp
        import strategy_picker as sp

        def scorer(rec):  # noqa: E306 — closure over the loaded modules
            hr = rec["headroom"]
            if hr is None:
                return None
            cat = sp.category_for(rec["pid"])
            hit = pp.category_hit_rate(cat, DEFAULT_SKILL_LIBRARY)
            if hit is None:
                hit = pp.overall_hit_rate(DEFAULT_SKILL_LIBRARY)
            stale = pp.staleness(rec["label"], DEFAULT_CYCLE_LOG)
            return pp.problem_priority(hr, hit, stale)
    except Exception as e:  # noqa: BLE001 — dashboard degrades to ledger-only view
        print(f"warn: problem loader unavailable ({e}); rendering ledger-only", file=sys.stderr)

    records = per_problem_records(
        problems, headroom, rank1, cycle_rows, minimize_map, scorer, rank1_agents
    )

    # cost per recent cycle: join telemetry cost onto the last cycle rows by order
    cost_by_idx = {i: r.get("cost_usd") for i, r in enumerate(telemetry)}
    recent = cycle_rows[-20:][::-1]
    # attach today's costs to recent cycles where the problem matches the latest telemetry
    tele_cost = {r.get("problem_id"): r.get("cost_usd") for r in telemetry[-20:]}
    for c in recent:
        m = re.match(r"P(\d+)-", c["problem"])
        c["cost"] = (
            f"${tele_cost[int(m.group(1))]:.2f}" if (m and int(m.group(1)) in tele_cost) else ""
        )

    submits = [ln.strip() for ln in _read_text(AUTO_SUBMIT).splitlines() if today in ln][-10:]

    # health: reuse scheduler_health's exact checks (single source of truth)
    health = "HEALTHY"
    try:
        sys.path.insert(0, str(_TOOLS))
        import scheduler_health as sh

        issues = (
            sh.check_runs(
                RUN_LEDGER,
                now_iso=now.isoformat(),
                max_age_hours=sh.DEFAULT_MAX_AGE_HOURS,
                max_consecutive_failures=sh.DEFAULT_MAX_CONSECUTIVE_FAILURES,
            )
            + sh.check_telemetry(
                TELEMETRY,
                window=sh.DEFAULT_TELEMETRY_WINDOW,
                max_fallback_rate=sh.DEFAULT_MAX_FALLBACK_RATE,
                max_cost_usd=sh.DEFAULT_MAX_COST_USD,
            )
            + sh.check_sentinel(SENTINEL)
        )
        health = "HEALTHY" if not issues else f"UNHEALTHY: {issues[0]}"
    except Exception as e:  # noqa: BLE001 — health card degrades, page still renders
        health = f"HEALTHY (health-check unavailable: {e})"

    current = current_problem(cycle_rows, telemetry, records, running=status["running"])
    attempts = recent_attempts(cycle_rows, current["label"]) if current else []

    return render_html(
        status=status,
        today=today_s,
        current=current,
        attempts=attempts,
        records=records,
        recent_cycles=recent,
        submits=submits,
        health=health,
        generated=generated,
        controls=controls,
    )


def _log_page(name: str) -> str:
    """A minimal HTML page rendering one allowlisted log/finding (--serve)."""
    title, body = read_log(name)
    esc = body.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (
        "<!doctype html><meta charset=utf-8>"
        "<style>body{background:#0d1117;color:#c9d1d9;font:12px ui-monospace,Menlo,monospace;"
        "margin:0;padding:20px}a{color:#79c0ff}pre{white-space:pre-wrap;word-break:break-word}"
        "h1{font-size:15px}</style>"
        f"<h1>{title}</h1><p><a href='/'>← back to dashboard</a></p><pre>{esc}</pre>"
    )


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--open", action="store_true", help="open the file in the default browser")
    ap.add_argument(
        "--serve",
        type=int,
        metavar="PORT",
        help="serve on localhost:PORT (regenerates per request)",
    )
    args = ap.parse_args(argv)

    if args.serve:
        import http.server
        import socketserver
        from urllib.parse import parse_qs, urlparse

        def _send(h, body: str, code: int = 200):
            data = body.encode()
            h.send_response(code)
            h.send_header("Content-Type", "text/html; charset=utf-8")
            h.send_header("Content-Length", str(len(data)))
            h.end_headers()
            h.wfile.write(data)

        def _redirect(h):
            h.send_response(303)
            h.send_header("Location", "/")
            h.end_headers()

        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(self):  # noqa: N802
                u = urlparse(self.path)
                if u.path == "/log":
                    name = parse_qs(u.query).get("name", [""])[0]
                    _send(self, _log_page(name))
                elif u.path in ("/", "/index.html"):
                    _send(self, build(controls=True))
                else:
                    _send(self, "not found", 404)

            def do_POST(self):  # noqa: N802
                u = urlparse(self.path)
                length = int(self.headers.get("Content-Length", 0) or 0)
                form = parse_qs(self.rfile.read(length).decode()) if length else {}
                qs = parse_qs(u.query)
                if u.path == "/start":
                    pid = (form.get("pid") or qs.get("pid") or ["0"])[0]
                    action_start(int(pid)) if pid.isdigit() else None
                elif u.path == "/stop":
                    action_stop()
                elif u.path == "/auto/on":
                    action_auto(True)
                elif u.path == "/auto/off":
                    action_auto(False)
                elif u.path == "/kill/on":
                    action_kill(True)
                elif u.path == "/kill/off":
                    action_kill(False)
                _redirect(self)

            def log_message(self, *a):  # silence
                pass

        with socketserver.TCPServer(("127.0.0.1", args.serve), H) as srv:
            print(f"dashboard → http://localhost:{args.serve}  (Ctrl-C to stop)")
            srv.serve_forever()
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(build())
    print(f"dashboard → {args.out}")
    if args.open:
        import webbrowser

        webbrowser.open(args.out.as_uri())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
