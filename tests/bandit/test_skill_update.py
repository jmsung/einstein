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


# ---------------- Goal 3 (js/feat/parallel-attempts): per-pull ledger ----------------


def test_update_counts_pull_index_distinguishes_same_cycle(tmp_path: Path) -> None:
    """Two pulls of the same arm within one cycle both apply.

    K-pull Thompson (Goal 0 research note) lets the same arm be drawn K
    times. Each draw is a trial; the bandit's tried-counter should reflect
    that. Pre-Goal-3, the ledger key `(cycle, technique)` deduped both pulls;
    `pull_index` distinguishes them."""
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    r0 = update_counts(
        lib,
        "tech-A",
        reached_top3=True,
        cycle_id=5,
        pull_index=0,
        ledger_path=ledger,
    )
    r1 = update_counts(
        lib,
        "tech-A",
        reached_top3=False,
        cycle_id=5,
        pull_index=1,
        ledger_path=ledger,
    )
    assert r0.applied and r1.applied
    # Two pulls × tech-A → tried += 2 (4 → 6), top3 += 1 (only pull 0 won)
    assert r1.tried == 6 and r1.top3 == 3


def test_update_counts_pull_index_backward_compat(tmp_path: Path) -> None:
    """An old-format ledger entry (pre-Goal-3) still dedupes a None-pull call.

    Migration safety: pre-existing entries in `mb/logs/skill-bandit-updates.tsv`
    were written without pull_index. A subsequent call with `pull_index=None`
    (the single-attempt path) must still see them as 'already applied'."""
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    # Simulate an old-format entry
    ledger.parent.mkdir(parents=True, exist_ok=True)
    ledger.write_text("5\ttech-A\n")
    r = update_counts(lib, "tech-A", reached_top3=True, cycle_id=5, ledger_path=ledger)
    assert not r.applied
    assert "idempotent" in r.reason


def test_update_counts_pull_index_idempotent_within_pull(tmp_path: Path) -> None:
    """Same (cycle, pull_index, technique) called twice → second call deduped."""
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    r0 = update_counts(
        lib,
        "tech-A",
        reached_top3=True,
        cycle_id=5,
        pull_index=0,
        ledger_path=ledger,
    )
    r1 = update_counts(
        lib,
        "tech-A",
        reached_top3=True,
        cycle_id=5,
        pull_index=0,
        ledger_path=ledger,
    )
    assert r0.applied and not r1.applied
    assert "idempotent" in r1.reason


def test_update_counts_pull_index_namespace_distinct_from_none(tmp_path: Path) -> None:
    """`pull_index=None` (single-attempt) and `pull_index=0` (fanout pull 0)
    are DIFFERENT keys — both should apply.

    Protects against a regex like `^5\\t` accidentally matching
    `5\\tP0\\ttech-A` and skipping it as already-applied."""
    lib = _lib(tmp_path)
    ledger = tmp_path / "ledger.tsv"
    r_none = update_counts(
        lib,
        "tech-A",
        reached_top3=True,
        cycle_id=5,
        ledger_path=ledger,
    )
    r_p0 = update_counts(
        lib,
        "tech-A",
        reached_top3=False,
        cycle_id=5,
        pull_index=0,
        ledger_path=ledger,
    )
    assert r_none.applied and r_p0.applied
