"""Tests for src/einstein/meta_loop/meta_budget.py — separate token ledger."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import meta_budget  # noqa: E402


def test_read_today_zero_when_no_file(tmp_path: Path) -> None:
    row = meta_budget.read_today(tmp_path / "nope.md", today=dt.date(2026, 5, 25))
    assert row.input == 0
    assert row.output == 0
    assert row.runs == 0


def test_record_creates_file_and_row(tmp_path: Path) -> None:
    path = tmp_path / "budget.md"
    row = meta_budget.record(path, input_tokens=100, output_tokens=20, today=dt.date(2026, 5, 25))
    assert path.is_file()
    assert row.input == 100
    assert row.output == 20
    assert row.total == 120
    assert row.runs == 1
    text = path.read_text()
    assert "2026-05-25 | 100 | 20 | 120 | 1" in text


def test_record_accumulates_within_day(tmp_path: Path) -> None:
    path = tmp_path / "budget.md"
    meta_budget.record(path, input_tokens=100, output_tokens=20, today=dt.date(2026, 5, 25))
    row = meta_budget.record(path, input_tokens=50, output_tokens=10, today=dt.date(2026, 5, 25))
    assert row.input == 150
    assert row.output == 30
    assert row.runs == 2


def test_record_separate_rows_per_day(tmp_path: Path) -> None:
    path = tmp_path / "budget.md"
    meta_budget.record(path, input_tokens=100, output_tokens=20, today=dt.date(2026, 5, 25))
    meta_budget.record(path, input_tokens=200, output_tokens=40, today=dt.date(2026, 5, 26))
    all_rows = meta_budget.read_all(path)
    assert len(all_rows) == 2
    by_date = {r.date: r for r in all_rows}
    assert by_date[dt.date(2026, 5, 25)].total == 120
    assert by_date[dt.date(2026, 5, 26)].total == 240


def test_negative_tokens_rejected(tmp_path: Path) -> None:
    path = tmp_path / "budget.md"
    with pytest.raises(ValueError):
        meta_budget.record(path, input_tokens=-1, output_tokens=0)


def test_read_today_returns_existing(tmp_path: Path) -> None:
    path = tmp_path / "budget.md"
    meta_budget.record(path, input_tokens=100, output_tokens=20, today=dt.date(2026, 5, 25))
    row = meta_budget.read_today(path, today=dt.date(2026, 5, 25))
    assert row.input == 100
    assert row.runs == 1
