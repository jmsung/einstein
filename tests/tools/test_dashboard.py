"""Tests for the dashboard's pure aggregation seam (docs/tools/dashboard.py)."""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parents[2] / "docs" / "tools"
spec = importlib.util.spec_from_file_location("dashboard", _TOOLS / "dashboard.py")
dashboard = importlib.util.module_from_spec(spec)
sys.modules["dashboard"] = dashboard
spec.loader.exec_module(dashboard)


def test_today_summary_sums_cost_tokens_and_fallback():
    tele = [
        {
            "ts": "2026-06-11T07:00:00Z",
            "path_taken": "llm",
            "cost_usd": 0.6,
            "input_tokens": 5,
            "output_tokens": 100,
        },
        {
            "ts": "2026-06-11T08:00:00Z",
            "path_taken": "fallback",
            "cost_usd": 0.0,
            "input_tokens": 0,
            "output_tokens": 0,
        },
        {
            "ts": "2026-06-10T23:00:00Z",
            "path_taken": "llm",
            "cost_usd": 9.9,
            "input_tokens": 1,
            "output_tokens": 1,
        },
    ]
    s = dashboard.today_summary(tele, today="2026-06-11")
    assert s["cycles"] == 2  # the 06-10 row excluded
    assert abs(s["cost"] - 0.6) < 1e-9
    assert s["tokens"] == 105
    assert s["fallback"] == 1


def test_relative_headroom_direction_and_floor():
    # minimise: lower is better → ours above arena1 = positive headroom
    assert abs(dashboard.relative_headroom(1.10, 1.00, True) - 0.10) < 1e-9
    # minimise but we already lead → clamped to 0 (SOTA)
    assert dashboard.relative_headroom(0.90, 1.00, True) == 0.0
    # maximise: higher is better
    assert abs(dashboard.relative_headroom(0.90, 1.00, False) - 0.10) < 1e-9
    # missing data → None
    assert dashboard.relative_headroom(None, 1.0, True) is None
    assert dashboard.relative_headroom(1.0, 1.0, None) is None


def test_per_problem_records_sorts_by_headroom_then_unknowns_last():
    class P:
        def __init__(self, pid, slug, score):
            self.problem_id, self.slug, self.name = pid, slug, slug
            self.tier, self.status, self.score_current = "A", "active", score

    problems = [P(1, "a", 1.20), P(2, "b", 1.01), P(3, "c", None)]
    headroom = {1: 1.00, 2: 1.00, 3: 1.00}
    recs = dashboard.per_problem_records(
        problems,
        headroom,
        rank1={2},
        cycle_rows=[{"problem": "P2-b", "cycle_id": 7}],
        minimize_map={1: True, 2: True, 3: True},
    )
    assert [r["pid"] for r in recs] == [1, 2, 3]  # P1 biggest headroom; P3 (None) last
    assert recs[0]["headroom"] > recs[1]["headroom"]
    assert recs[2]["headroom"] is None
    p2 = next(r for r in recs if r["pid"] == 2)
    assert p2["rank1"] is True and p2["last_cycle"] == 7 and p2["cycles"] == 1


def test_per_problem_records_priority_scorer_reorders():
    class P:
        def __init__(self, pid, slug, score):
            self.problem_id, self.slug, self.name = pid, slug, slug
            self.tier, self.status, self.score_current = "A", "active", score

    problems = [P(1, "a", 2.0), P(2, "b", 1.5)]  # P1 has bigger raw headroom
    headroom = {1: 1.0, 2: 1.0}
    # scorer inverts: reward P2 over P1 (e.g. hit-rate/staleness favours P2)
    recs = dashboard.per_problem_records(
        problems,
        headroom,
        rank1=set(),
        cycle_rows=[],
        minimize_map={1: True, 2: True},
        priority_scorer=lambda r: {1: 0.1, 2: 0.9}[r["pid"]],
    )
    assert [r["pid"] for r in recs] == [2, 1]  # picker priority wins, not raw headroom
    assert recs[0]["priority"] == 0.9


def test_parse_strategy_extracts_technique_and_move():
    notes = (
        "autonomous_loop LLM cycle — category=autocorrelation; strategy=thompson-bandit; "
        "technique=warm-self-pruning-compact-support.md prior=Beta(3,3) sampled_θ=0.58; "
        "llm-strategy=skip-execution-converged-honest-zero; tokens=..."
    )
    s = dashboard.parse_strategy(notes)
    assert s["strategy"] == "thompson-bandit"
    assert s["technique"] == "warm-self-pruning-compact-support"  # .md stripped
    assert s["llm_move"] == "skip-execution-converged-honest-zero"
    assert s["theta"] == "0.58"


def test_current_problem_running_picks_latest_cycle():
    records = [
        {
            "label": "P4-c",
            "name": "c",
            "tier": "S",
            "status": "x",
            "ours": 1.0,
            "arena1": 1.0,
            "headroom": 0.0,
        },
        {
            "label": "P10-t",
            "name": "t",
            "tier": "B",
            "status": "y",
            "ours": 2.0,
            "arena1": 1.0,
            "headroom": 0.5,
        },
    ]
    cycle_rows = [{"problem": "P4-c", "cycle_id": 308}, {"problem": "P10-t", "cycle_id": 312}]
    tele = [
        {"problem_id": 10, "attempt_index": 2, "path_taken": "llm", "cost_usd": 0.38, "ts": "t"}
    ]
    cur = dashboard.current_problem(cycle_rows, tele, records, running=True)
    assert (
        cur["mode"] == "running" and cur["label"] == "P10-t"
    )  # latest cycle, not highest headroom
    assert cur["attempt"] == 2 and cur["path"] == "llm"


def test_current_problem_running_prefers_active_pid_over_cycle_log():
    # cycle-log + telemetry both still say P4 (last completed), but the live
    # process is on P5 (active_pid) → hero must show P5, not the stale P4.
    records = [
        {
            "pid": 4,
            "label": "P4-c",
            "name": "c",
            "tier": "S",
            "status": "x",
            "ours": 1.0,
            "arena1": 1.0,
            "headroom": 0.0,
        },
        {
            "pid": 5,
            "label": "P5-d",
            "name": "d",
            "tier": "B",
            "status": "y",
            "ours": 2.0,
            "arena1": 1.0,
            "headroom": 0.5,
        },
    ]
    cycle_rows = [{"problem": "P4-c", "cycle_id": 308, "notes": ""}]
    tele = [{"problem_id": 4, "attempt_index": 1, "path_taken": "llm", "ts": "t"}]
    cur = dashboard.current_problem(cycle_rows, tele, records, running=True, active_pid=5)
    assert cur["label"] == "P5-d"  # active process wins over stale cycle/telemetry


def test_current_problem_idle_picks_highest_headroom():
    records = [
        {
            "label": "P4-c",
            "name": "c",
            "tier": "S",
            "status": "x",
            "ours": 1.0,
            "arena1": 1.0,
            "headroom": 0.5,
        }
    ]
    cur = dashboard.current_problem(
        [{"problem": "P9-z", "cycle_id": 9}], [], records, running=False
    )
    assert cur["mode"] == "next" and cur["label"] == "P4-c"  # records[0], ignores cycle history


def test_parse_rank1_agents_reads_latest_snapshot(tmp_path):
    (tmp_path / "status_2026-06-09.md").write_text("## Problem 4:\n- **#1**: OldAgent (1.0)\n")
    (tmp_path / "status_2026-06-10.md").write_text(
        "# Arena Status\n"
        "## Problem 2: First Autocorrelation\n"
        "- **#1**: JSAgent (1.5028506180033636)\n"
        "- **Top 3**: #1 JSAgent, #2 OrganonAgent\n"
        "## Problem 4: Third Autocorrelation\n"
        "- **#1**: OrganonAgent (1.4523043331831582)\n"
    )
    agents, asof = dashboard.parse_rank1_agents(tmp_path)
    assert agents == {2: "JSAgent", 4: "OrganonAgent"}  # latest file wins (2026-06-10)
    assert asof == "2026-06-10"


def test_parse_arena_urls_reads_frontmatter(tmp_path):
    (tmp_path / "4-third.md").write_text(
        "---\nproblem_id: 4\narena_url: https://einsteinarena.com/problems/third-autocorrelation\n---\n# x\n"
    )
    (tmp_path / "10-thom.md").write_text(
        "---\nproblem_id: 10\narena_url: https://einsteinarena.com/problems/thomson\n---\n"
    )
    (tmp_path / "nourl.md").write_text("---\nproblem_id: 99\n---\n")  # no arena_url → skipped
    urls = dashboard.parse_arena_urls(tmp_path)
    assert urls[4].endswith("/third-autocorrelation")
    assert urls[10].endswith("/thomson")  # arena slug ≠ our slug
    assert 99 not in urls


def test_loop_running_true_for_live_pid(tmp_path):
    lf = tmp_path / "l.lock"
    lf.write_text(f"pid={os.getpid()} started=now\n")  # this process is alive
    assert dashboard.loop_running(lf) is True


def test_loop_running_false_for_dead_pid_and_missing(tmp_path):
    lf = tmp_path / "l.lock"
    lf.write_text("pid=999999 started=2020-01-01\n")  # dead
    assert dashboard.loop_running(lf) is False
    assert dashboard.loop_running(tmp_path / "absent.lock") is False


def test_action_start_refused_while_running(monkeypatch):
    monkeypatch.setattr(dashboard, "loop_running", lambda *a, **k: True)
    res = dashboard.action_start(11)
    assert "refused" in res and "Stop it first" in res


def test_action_auto_on_refused_while_running(monkeypatch):
    monkeypatch.setattr(dashboard, "loop_running", lambda *a, **k: True)
    assert "refused" in dashboard.action_auto(True)


def test_action_kill_toggles_sentinel(tmp_path):
    s = tmp_path / ".inner-agent-disabled"
    dashboard.action_kill(True, sentinel=s)
    assert s.exists()
    dashboard.action_kill(False, sentinel=s)
    assert not s.exists()


def test_action_stop_parses_lockfile_pid(tmp_path, monkeypatch):
    lock = tmp_path / "loop.lock"
    lock.write_text("pid=999999 started=2026-06-11T00:00:00\n")
    killed = {}
    monkeypatch.setattr(dashboard.os, "kill", lambda pid, sig: killed.update(pid=pid, sig=sig))
    res = dashboard.action_stop(lockfile=lock)
    assert killed["pid"] == 999999 and "SIGTERM" in res


def test_action_stop_no_lockfile(tmp_path):
    assert "no running loop" in dashboard.action_stop(lockfile=tmp_path / "absent.lock")


def test_read_log_allowlist_and_traversal(tmp_path, monkeypatch):
    # unknown name refused
    _, body, _ = dashboard.read_log("../../etc/passwd")
    assert "refused" in body
    # path-traversal finding refused
    _, body, _ = dashboard.read_log("finding:../../../etc/passwd")
    assert "refused" in body
    # allowlisted log reads, newest-first, not markdown
    title, _, is_md = dashboard.read_log("cycle-log")
    assert title.startswith("log · cycle-log") and is_md is False


def test_read_log_newest_first(tmp_path, monkeypatch):
    log = tmp_path / "x.log"
    log.write_text("first\nsecond\nthird\n")
    monkeypatch.setitem(dashboard.LOG_FILES, "x", log)
    _, body, _ = dashboard.read_log("x")
    assert body.splitlines()[0] == "third"  # newest at top


def test_render_markdown_basics():
    md = "---\ntype: finding\n---\n# Title\n\nA **bold** and `code` and [[wl]].\n\n- one\n- two\n"
    html = dashboard.render_markdown(md)
    assert "<div class=fm>" in html  # frontmatter block
    assert "<h2>Title</h2>" in html  # # → h2
    assert "<b>bold</b>" in html and "<code>code</code>" in html
    assert "<span class=wl>wl</span>" in html
    assert html.count("<li>") == 2


def test_parse_cycle_log_tolerates_pipe_rows(tmp_path):
    log = tmp_path / "cycle-log.md"
    log.write_text(
        "## Cycles\n"
        "| # | problem | start → end | hours | compute | cites | f+ | c+ | mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 306 | P3-autocorrelation | none | 0.02 | local-cpu+llm | 0 | 0 | 0 | a:1 | converged | gloss |\n"
    )
    rows = dashboard.parse_cycle_log(log)
    assert len(rows) == 1
    assert rows[0]["cycle_id"] == 306 and rows[0]["problem"] == "P3-autocorrelation"
    assert rows[0]["outcome"] == "converged"


def test_rank1_leaderboard_counts_orders_and_lists_problems():
    agents = {1: "Together-AI", 2: "JSAgent", 5: "Together-AI", 9: "JSAgent", 4: "OrganonAgent"}
    lb = dashboard.rank1_leaderboard(agents)
    # (agent, count, sorted pids); ties (2 each) broken by name asc
    assert lb[0] == ("JSAgent", 2, [2, 9])
    assert lb[1] == ("Together-AI", 2, [1, 5])
    assert lb[2] == ("OrganonAgent", 1, [4])
