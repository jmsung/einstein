"""Tests for docs/tools/inner_agent_telemetry.py (Phase 2 Goal 1).

Covers the pure record/read/summarize API: round-trip append, tolerant
reading, and the R2–R5 readiness-criteria folds in `summarize`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import inner_agent_telemetry as iat  # noqa: E402

# ---------------- record + read round-trip ----------------


def test_record_cycle_appends_one_json_line(tmp_path: Path) -> None:
    p = tmp_path / "tele.jsonl"
    rec = iat.record_cycle(
        p,
        problem_id=2,
        attempt_index=1,
        path_taken="llm",
        parse_ok=True,
        wall_clock_s=45.2,
        input_tokens=6000,
        output_tokens=300,
    )
    assert rec.problem_id == 2
    assert rec.total_tokens == 6300
    assert rec.ts  # auto-stamped
    lines = p.read_text().strip().splitlines()
    assert len(lines) == 1
    d = json.loads(lines[0])
    assert d["path_taken"] == "llm"
    assert d["parse_ok"] is True


def test_record_cycle_creates_parent_dir(tmp_path: Path) -> None:
    p = tmp_path / "nested" / "logs" / "tele.jsonl"
    iat.record_cycle(p, problem_id=1, attempt_index=1, path_taken="fallback")
    assert p.is_file()


def test_record_cycle_explicit_ts_is_preserved(tmp_path: Path) -> None:
    p = tmp_path / "tele.jsonl"
    rec = iat.record_cycle(
        p, problem_id=1, attempt_index=1, path_taken="llm", ts="2026-06-09T00:00:00+00:00"
    )
    assert rec.ts == "2026-06-09T00:00:00+00:00"


def test_read_records_absent_file_is_empty(tmp_path: Path) -> None:
    assert iat.read_records(tmp_path / "missing.jsonl") == []


def test_read_records_skips_malformed_and_partial_lines(tmp_path: Path) -> None:
    p = tmp_path / "tele.jsonl"
    iat.record_cycle(p, problem_id=1, attempt_index=1, path_taken="llm", parse_ok=True)
    # Simulate an interrupted append + a non-telemetry line.
    with p.open("a") as f:
        f.write('{"path_taken": "llm", "problem_id": 9, "attempt_in')  # truncated
        f.write("\n")
        f.write('{"unrelated": true}\n')  # valid JSON, not a telemetry record
        f.write("\n")  # blank
    recs = iat.read_records(p)
    assert len(recs) == 1
    assert recs[0].problem_id == 1


def test_read_records_ignores_unknown_keys(tmp_path: Path) -> None:
    p = tmp_path / "tele.jsonl"
    with p.open("w") as f:
        f.write(json.dumps({"path_taken": "llm", "problem_id": 3, "future_field": 1}) + "\n")
    recs = iat.read_records(p)
    assert len(recs) == 1
    assert recs[0].problem_id == 3


# ---------------- summarize: the readiness folds ----------------


def _rec(**kw):
    base = dict(problem_id=1, attempt_index=1, path_taken="llm")
    base.update(kw)
    return iat.CycleTelemetry(**base)


def test_summarize_empty_is_safe_defaults() -> None:
    s = iat.summarize([])
    assert s.cycles == 0
    assert s.fallback_rate == 0.0
    assert s.parse_success_rate == 1.0  # vacuous
    assert s.timeout_rate == 0.0
    assert s.mean_tokens_per_llm_cycle == 0.0


def test_summarize_fallback_rate_excludes_environmental() -> None:
    # 2 llm, 1 parse-error fallback (counts), 1 unavailable fallback (env, excluded).
    recs = [
        _rec(path_taken="llm", parse_ok=True),
        _rec(path_taken="llm", parse_ok=True),
        _rec(path_taken="fallback", llm_error_kind="parse-error"),
        _rec(path_taken="fallback", llm_error_kind="unavailable"),
    ]
    s = iat.summarize(recs)
    assert s.cycles == 4
    assert s.llm_cycles == 2
    assert s.fallback_cycles == 2
    assert s.environmental_fallbacks == 1
    # denominator = 4 - 1 env = 3 decided; non-env fallbacks = 2 - 1 = 1 → 1/3
    assert abs(s.fallback_rate - (1 / 3)) < 1e-9


def test_summarize_parse_success_counts_only_attempted() -> None:
    # parse attempted on: 2 llm successes + 1 parse-error. unavailable doesn't count.
    recs = [
        _rec(path_taken="llm", parse_ok=True),
        _rec(path_taken="llm", parse_ok=True),
        _rec(path_taken="fallback", llm_error_kind="parse-error", parse_ok=False),
        _rec(path_taken="fallback", llm_error_kind="unavailable"),
    ]
    s = iat.summarize(recs)
    assert s.parse_attempts == 3
    assert s.parse_ok == 2
    assert abs(s.parse_success_rate - (2 / 3)) < 1e-9


def test_summarize_timeout_rate_and_error_kinds() -> None:
    recs = [
        _rec(path_taken="llm", parse_ok=True),
        _rec(path_taken="fallback", llm_error_kind="timeout"),
        _rec(path_taken="fallback", llm_error_kind="timeout"),
    ]
    s = iat.summarize(recs)
    assert s.timeouts == 2
    assert abs(s.timeout_rate - (2 / 3)) < 1e-9
    assert s.error_kind_counts == {"timeout": 2}


def test_summarize_mean_tokens_only_over_llm_cycles() -> None:
    recs = [
        _rec(path_taken="llm", parse_ok=True, input_tokens=5000, output_tokens=1000),
        _rec(path_taken="llm", parse_ok=True, input_tokens=7000, output_tokens=1000),
        _rec(path_taken="fallback", llm_error_kind="timeout"),  # excluded from token mean
    ]
    s = iat.summarize(recs)
    assert s.total_tokens == 14000
    assert s.mean_tokens_per_llm_cycle == 7000.0


def test_summarize_cost_only_over_exact_cost_cycles() -> None:
    """$/cycle averages only cycles that carry an exact cost (>0); estimate-only
    cycles (cost_usd=0) don't dilute the mean."""
    recs = [
        _rec(path_taken="llm", parse_ok=True, token_source="exact", cost_usd=0.04),
        _rec(path_taken="llm", parse_ok=True, token_source="exact", cost_usd=0.06),
        _rec(path_taken="llm", parse_ok=True, token_source="estimate", cost_usd=0.0),
    ]
    s = iat.summarize(recs)
    assert s.exact_cost_cycles == 2
    assert abs(s.total_cost_usd - 0.10) < 1e-9
    assert abs(s.mean_cost_per_llm_cycle - 0.05) < 1e-9


def test_summarize_cost_zero_when_no_exact_cost() -> None:
    s = iat.summarize([_rec(path_taken="llm", parse_ok=True, cost_usd=0.0)])
    assert s.exact_cost_cycles == 0
    assert s.mean_cost_per_llm_cycle == 0.0


def test_record_cycle_round_trips_cost_and_source(tmp_path: Path) -> None:
    p = tmp_path / "tele.jsonl"
    iat.record_cycle(
        p,
        problem_id=2,
        attempt_index=1,
        path_taken="llm",
        parse_ok=True,
        token_source="exact",
        cost_usd=0.0421,
    )
    rec = iat.read_records(p)[0]
    assert rec.token_source == "exact"
    assert rec.cost_usd == 0.0421
