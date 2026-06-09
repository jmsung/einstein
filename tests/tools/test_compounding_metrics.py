"""Tests for docs/tools/compounding_metrics.py (Phase 4 of meta-learning-automation)."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import compounding_metrics as cm  # noqa: E402

# A minimal cycle-log: 12-column schema (id|problem|score|hours|compute|cites|
# findings|concepts|authormix|outcome|notes|cites_src).
_LOG = """# Cycle log

| # | problem | start → end | hours | compute | wiki cites | findings+ | concepts+ | author mix | outcome | notes | cites_src |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | P2-x | a → b | 1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | n | 0 |
| 1 | P2-x | a → b | 1 | local-cpu | 1 | 0 | 0 | a:1/h:0/hyb:0 | no-change | n | 1 |
| 2 | P2-x | a → c | 1 | local-cpu | 1 | 1 | 0 | a:1/h:0/hyb:0 | improved-and-submitted | record | 2 |
| 3 | P9-y | a → a | 1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | conquered | win | 0 |
"""

_SKILL = """# skill library

| technique | category | tried | top3 | finding | last_used | hit_rate |
|---|---|---|---|---|---|---|
| `parallel-tempering-sa.md` | kissing | 5 | 3 | 2 | 2026-04-25 | 0.60 |
| `slsqp-active-pair-polish.md` | packing | 25 | 6 | 1 | 2026-06-03 | 0.24 |
"""


def test_parse_cycle_rows_skips_headers() -> None:
    rows = cm.parse_cycle_rows(_LOG)
    assert [r.cycle_id for r in rows] == [0, 1, 2, 3]
    assert rows[2].outcome == "improved-and-submitted"
    assert rows[3].outcome == "conquered"


def test_time_to_record_counts_attempts_to_first_record() -> None:
    ttr = cm.time_to_record(cm.parse_cycle_rows(_LOG))
    # P2-x: 3rd attempt was the record → 3 cycles. P9-y: 1st attempt → 1.
    assert ttr == {"P2-x": 3, "P9-y": 1}


def test_technique_hit_rate_positional_parse() -> None:
    hr = cm.technique_hit_rate(_SKILL)
    assert hr["parallel-tempering-sa.md"] == (3, 5)  # (top3, tried)
    assert hr["slsqp-active-pair-polish.md"] == (6, 25)
    # overall = (3+6)/(5+25) = 9/30 = 0.30
    assert abs(cm.overall_hit_rate(hr) - 0.30) < 1e-9


def test_cite_reuse_rate() -> None:
    records = [
        {"cited_sources": ["docs/source/x.md"]},  # baseline (first citing)
        {"cited_sources": ["docs/source/x.md"]},  # reuse → counts
        {"cited_sources": ["docs/source/y.md"]},  # new → eligible, not reuse
        {"cited_sources": []},  # skipped (cites nothing)
        {"cited_sources": ["docs/source/y.md"]},  # reuse
    ]
    rate, reuse, eligible = cm.cite_reuse_rate(records)
    assert (reuse, eligible) == (2, 3)
    assert abs(rate - 2 / 3) < 1e-9


def test_cite_reuse_rate_none_when_no_eligible() -> None:
    rate, reuse, eligible = cm.cite_reuse_rate([{"cited_sources": ["a"]}])
    assert rate is None and reuse == 0 and eligible == 0


def test_render_block_has_markers_and_metrics(tmp_path: Path) -> None:
    log = tmp_path / "cycle-log.md"
    log.write_text(_LOG)
    skill = tmp_path / "skill.md"
    skill.write_text(_SKILL)
    cited = tmp_path / "cited.jsonl"
    cited.write_text('{"cited_sources": ["a"]}\n{"cited_sources": ["a"]}\n')
    block = cm.render_block(cycle_log=log, skill_library=skill, cited_sources=cited)
    assert cm.START_MARKER in block and cm.END_MARKER in block
    assert "Records achieved | 2" in block
    assert "30%" in block  # hit-rate
    assert "needs instrumentation" in block  # honest n/a, not faked


def test_write_block_is_idempotent(tmp_path: Path) -> None:
    metrics = tmp_path / "metrics.md"
    metrics.write_text("# Metrics\n\nexisting content\n")
    block1 = "<!-- compounding:start -->\nA\n<!-- compounding:end -->"
    cm.write_block(metrics, block1)
    assert "existing content" in metrics.read_text()
    assert metrics.read_text().count(cm.START_MARKER) == 1
    block2 = "<!-- compounding:start -->\nB\n<!-- compounding:end -->"
    cm.write_block(metrics, block2)
    text = metrics.read_text()
    assert text.count(cm.START_MARKER) == 1  # replaced, not appended
    assert "B" in text and "\nA\n" not in text
