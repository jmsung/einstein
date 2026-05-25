"""Tests for docs/tools/inner_agent_budget.py (Goal 7.8d CLI)."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "docs" / "tools"))

import inner_agent_budget as iab  # noqa: E402
import inner_agent_gates as iag  # noqa: E402

# ---------------- show ----------------


def test_show_today_on_empty_ledger_prints_zero_row(tmp_path, capsys):
    p = tmp_path / "budget.md"
    rc = iab.main(["--path", str(p), "show"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "in=         0" in out
    assert "out=         0" in out
    # Date column present
    assert dt.date.today().isoformat() in out


def test_show_today_pct_column_when_cap_specified(tmp_path, capsys):
    p = tmp_path / "budget.md"
    iag.record_token_usage(
        p,
        input_tokens=300,
        output_tokens=200,
        today=dt.date.today(),
    )
    rc = iab.main(["--path", str(p), "--cap", "1000", "show"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "50.0% of 1000" in out


def test_show_all_lists_every_row_sorted(tmp_path, capsys):
    p = tmp_path / "budget.md"
    iag.record_token_usage(
        p,
        input_tokens=100,
        output_tokens=20,
        today=dt.date(2026, 5, 23),
    )
    iag.record_token_usage(
        p,
        input_tokens=50,
        output_tokens=10,
        today=dt.date(2026, 5, 24),
    )
    iag.record_token_usage(
        p,
        input_tokens=200,
        output_tokens=40,
        today=dt.date(2026, 5, 22),
    )
    rc = iab.main(["--path", str(p), "show", "--all"])
    assert rc == 0
    out = capsys.readouterr().out
    lines = [line for line in out.splitlines() if line.strip()]
    # Sorted ascending — 2026-05-22 first
    assert "2026-05-22" in lines[0]
    assert "2026-05-23" in lines[1]
    assert "2026-05-24" in lines[2]


def test_show_all_empty_ledger_prints_marker(tmp_path, capsys):
    p = tmp_path / "missing.md"
    rc = iab.main(["--path", str(p), "show", "--all"])
    assert rc == 0
    assert "no ledger" in capsys.readouterr().out


# ---------------- record ----------------


def test_record_appends_and_prints_new_row(tmp_path, capsys):
    p = tmp_path / "budget.md"
    rc = iab.main(
        [
            "--path",
            str(p),
            "record",
            "--input",
            "1000",
            "--output",
            "200",
        ]
    )
    assert rc == 0
    out = capsys.readouterr().out
    assert "in=      1000" in out
    assert "total=      1200" in out
    # Real ledger was updated
    text = p.read_text()
    assert "| 1000 | 200 | 1200 | 1 |" in text


def test_record_rejects_negative(tmp_path, capsys):
    p = tmp_path / "budget.md"
    rc = iab.main(
        [
            "--path",
            str(p),
            "record",
            "--input",
            "-1",
            "--output",
            "10",
        ]
    )
    assert rc == 2
    err = capsys.readouterr().err
    assert "non-negative" in err


# ---------------- reset ----------------


def test_reset_zeros_a_specific_day(tmp_path, capsys):
    p = tmp_path / "budget.md"
    iag.record_token_usage(
        p,
        input_tokens=5000,
        output_tokens=1000,
        today=dt.date(2026, 5, 24),
    )
    iag.record_token_usage(
        p,
        input_tokens=2000,
        output_tokens=400,
        today=dt.date(2026, 5, 23),
    )
    rc = iab.main(["--path", str(p), "reset", "2026-05-24"])
    assert rc == 0
    assert "reset 2026-05-24" in capsys.readouterr().out
    text = p.read_text()
    # 2026-05-24 zeroed
    assert "| 2026-05-24 | 0 | 0 | 0 | 0 |" in text
    # 2026-05-23 preserved
    assert "| 2026-05-23 | 2000 | 400 | 2400 | 1 |" in text


def test_reset_rejects_malformed_date(tmp_path, capsys):
    p = tmp_path / "budget.md"
    rc = iab.main(["--path", str(p), "reset", "yesterday"])
    assert rc == 2
    assert "YYYY-MM-DD" in capsys.readouterr().err


def test_reset_no_row_for_date_is_noop(tmp_path, capsys):
    p = tmp_path / "budget.md"
    iag.record_token_usage(
        p,
        input_tokens=100,
        output_tokens=20,
        today=dt.date(2026, 5, 24),
    )
    rc = iab.main(["--path", str(p), "reset", "2099-12-31"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "nothing to reset" in out


def test_reset_no_ledger_is_noop(tmp_path, capsys):
    rc = iab.main(["--path", str(tmp_path / "missing.md"), "reset", "2026-05-24"])
    assert rc == 0
    assert "nothing to reset" in capsys.readouterr().out


def test_subcommand_required(tmp_path, capsys):
    """argparse should reject calls without a subcommand."""
    import pytest

    with pytest.raises(SystemExit):
        iab.main(["--path", str(tmp_path / "x.md")])
