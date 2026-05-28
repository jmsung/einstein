"""Tests for the bandit skill-library counter updater (Goal 3)."""

from __future__ import annotations

from pathlib import Path

from einstein.bandit.skill_update import update_counts


def _lib(tmp_path: Path) -> Path:
    p = tmp_path / "skill-library.md"
    p.write_text(
        "| technique | category | tried | top3 | finding | last_used | hit_rate |\n"
        "|---|---|---|---|---|---|---|\n"
        "| `tech-A` | packing | 4 | 2 | 1 | 2026-01-01 | 0.50 |\n"
        "| `tech-B` | kissing | 3 | 0 | 2 | 2026-02-01 | 0.00 |\n"
    )
    return p


def _row_for(lib: Path, technique: str) -> str:
    return next(line for line in lib.read_text().splitlines() if f"`{technique}`" in line)


def test_tried_always_increments_top3_on_reward(tmp_path: Path) -> None:
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    r = update_counts(
        lib, "tech-A", reached_top3=True, cycle_id=10, ledger_path=ledger, today="2026-05-27"
    )
    assert r.applied
    assert (r.tried, r.top3, r.finding) == (5, 3, 1)
    assert r.hit_rate == 0.6
    row = _row_for(lib, "tech-A")
    assert "| 5 | 3 | 1 |" in row
    assert "2026-05-27" in row
    assert "0.60" in row


def test_top3_not_incremented_without_reward(tmp_path: Path) -> None:
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    r = update_counts(lib, "tech-B", reached_top3=False, cycle_id=1, ledger_path=ledger)
    assert (r.tried, r.top3) == (4, 0)
    assert r.hit_rate == 0.0


def test_produced_finding_increments_finding(tmp_path: Path) -> None:
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    r = update_counts(
        lib, "tech-B", reached_top3=False, cycle_id=2, ledger_path=ledger, produced_finding=True
    )
    assert r.finding == 3


def test_idempotent_same_cycle_is_noop(tmp_path: Path) -> None:
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    first = update_counts(lib, "tech-A", reached_top3=True, cycle_id=7, ledger_path=ledger)
    assert first.applied
    snapshot = lib.read_text()
    second = update_counts(lib, "tech-A", reached_top3=True, cycle_id=7, ledger_path=ledger)
    assert not second.applied
    assert "idempotent" in second.reason
    assert lib.read_text() == snapshot  # file untouched


def test_different_cycle_applies_again(tmp_path: Path) -> None:
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    update_counts(lib, "tech-A", reached_top3=False, cycle_id=1, ledger_path=ledger)
    r2 = update_counts(lib, "tech-A", reached_top3=False, cycle_id=2, ledger_path=ledger)
    assert r2.applied
    assert r2.tried == 6  # 4 → 5 → 6 across two distinct cycles


def test_technique_not_in_library(tmp_path: Path) -> None:
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    r = update_counts(lib, "nope.md", reached_top3=True, cycle_id=1, ledger_path=ledger)
    assert not r.applied
    assert "not in library" in r.reason


def test_header_and_separator_rows_untouched(tmp_path: Path) -> None:
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    update_counts(lib, "tech-A", reached_top3=True, cycle_id=1, ledger_path=ledger)
    text = lib.read_text()
    assert "| technique | category | tried |" in text  # header intact
    assert "|---|---|---|---|---|---|---|" in text  # separator intact
    # tech-B (not chosen) unchanged
    assert "| `tech-B` | kissing | 3 | 0 | 2 | 2026-02-01 | 0.00 |" in text
