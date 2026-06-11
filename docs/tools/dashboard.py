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
import re
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
) -> list[dict]:
    """One record per problem: our score, arena #1, headroom %, rank1, activity."""
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
                "headroom": hr,
                "rank1": pid in rank1,
                "last_cycle": last_cycle.get(lbl, 0),
                "cycles": count.get(lbl, 0),
            }
        )
    # highest headroom first; unknowns (None) last; ties by id
    recs.sort(key=lambda r: (r["headroom"] is None, -(r["headroom"] or 0), r["pid"]))
    return recs


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
    records: list[dict],
    recent_cycles: list[dict],
    submits: list[str],
    health: str,
    generated: str,
) -> str:
    rows_problems = "\n".join(
        f"<tr class='{'r1' if r['rank1'] else ''}'>"
        f"<td>P{r['pid']}</td><td class='nm'>{r['name']}</td>"
        f"<td>{r['tier']}</td><td class='st'>{r['status']}</td>"
        f"<td class='num'>{_fmt(r['ours'])}</td><td class='num'>{_fmt(r['arena1'])}</td>"
        f"<td>{_hr_badge(r['headroom'])}</td>"
        f"<td>{'★' if r['rank1'] else ''}</td>"
        f"<td class='num'>{r['cycles']}</td><td class='num'>#{r['last_cycle'] or '—'}</td></tr>"
        for r in records
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
 .b{{padding:1px 6px;border-radius:10px;font-size:11px}}
 .green{{background:#1b3a26;color:#7ee787}} .amber{{background:#3a341b;color:#e3b341}} .gray{{background:#21262d;color:#8b949e}}
 code{{color:var(--mut);font-size:11px}} ul{{margin:6px 0;padding-left:18px}}
 .state{{font-size:15px}}
</style></head><body><div class=wrap>
<h1>einstein · autonomous loop</h1>
<div class=sub>generated {generated} · auto-refresh {REFRESH_S}s · <span class=state>{run_state}</span></div>

<div class=cards>
 <div class=card><div class=k>health</div><div class="v {health_cls}">{health.split(' ')[0]}</div><div class=sub>{health}</div></div>
 <div class=card><div class=k>cycles today</div><div class=v>{today['cycles']}</div></div>
 <div class=card><div class=k>spend today</div><div class=v>${today['cost']:.2f}</div></div>
 <div class=card><div class=k>tokens today</div><div class="v {budget_cls}">{today['tokens']:,}</div><div class=sub>{today['budget_pct']:.1f}% of 5M</div></div>
 <div class=card><div class=k>fallbacks today</div><div class=v>{today['fallback']}</div></div>
 <div class=card><div class=k>last run</div><div class=sub style=margin-top:6px>{status['last_run'] or '—'}</div></div>
</div>

<h2>Per-problem records (our score vs arena #1)</h2>
<table><tr><th>id</th><th>problem</th><th>tier</th><th>status</th><th>ours</th><th>arena #1</th><th>headroom</th><th>#1?</th><th>cycles</th><th>last</th></tr>
{rows_problems}
</table>

<h2>Recent cycles</h2>
<table><tr><th>cycle</th><th>problem</th><th>score</th><th>outcome</th><th>cost</th></tr>
{rows_cycles}
</table>

<h2>Auto-submit decisions (today)</h2>
<ul>{rows_submit}</ul>
</div></body></html>"""


# ----------------------------- assembly -----------------------------


def build(*, today: str | None = None, generated: str | None = None) -> str:
    now = dt.datetime.now(dt.timezone.utc)
    today = today or now.strftime("%Y-%m-%d")
    generated = generated or now.strftime("%Y-%m-%d %H:%M:%SZ")

    telemetry = parse_telemetry()
    cycle_rows = parse_cycle_log()
    headroom = parse_headroom_cache()
    rank1 = parse_rank1()
    status = loop_status()
    today_s = today_summary(telemetry, today=today)

    # problems + direction map via the loop's own loaders (single source of truth)
    problems, minimize_map = [], {}
    try:
        sys.path.insert(0, str(_REPO / "scripts"))
        sys.path.insert(0, str(_REPO / "src"))
        from autonomous_loop import DEFAULT_PROBLEMS_DIR, load_problems

        from einstein.auto_submit import PROBLEM_MINIMIZE

        problems = load_problems(DEFAULT_PROBLEMS_DIR)
        minimize_map = dict(PROBLEM_MINIMIZE)
    except Exception as e:  # noqa: BLE001 — dashboard degrades to ledger-only view
        print(f"warn: problem loader unavailable ({e}); rendering ledger-only", file=sys.stderr)

    records = per_problem_records(problems, headroom, rank1, cycle_rows, minimize_map)

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

    return render_html(
        status=status,
        today=today_s,
        records=records,
        recent_cycles=recent,
        submits=submits,
        health=health,
        generated=generated,
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

        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(self):  # noqa: N802
                body = build().encode()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

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
