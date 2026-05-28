"""Tests for the bandit vs manifest shadow A/B harness (Goal 5)."""

from __future__ import annotations

import datetime as dt
from pathlib import Path

from einstein.bandit import shadow_ab
from einstein.meta_loop import diagnose


def _row(cid: int, problem: str, findings: int, notes: str, outcome: str = "new-finding") -> str:
    return (
        f"| {cid} | {problem} | 1.0 → 1.0 | 0 | local-cpu | 0 | {findings} | 0 "
        f"| a:1/h:0/hyb:0 | {outcome} | {notes} | 0 |"
    )


def _cycle_log(tmp_path: Path, name: str, rows: list[str]) -> Path:
    p = tmp_path / name
    header = (
        "| cycle | problem | score | hrs | compute | cit | findings | concepts "
        "| authors | outcome | notes | cites |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
    )
    p.write_text(header + "\n".join(rows) + "\n")
    return p


# ---------------- cross-problem rediscovery ----------------


def test_cross_problem_rediscovery_counts_multi_problem_techniques(tmp_path: Path) -> None:
    log = _cycle_log(
        tmp_path,
        "a.md",
        [
            _row(
                0,
                "P1-erdos",
                1,
                "strategy=thompson-bandit; technique=warm-start.md prior=Beta(3,2) sampled_θ=0.6",
            ),
            _row(
                1,
                "P9-func",
                1,
                "strategy=thompson-bandit; technique=warm-start.md prior=Beta(4,2) sampled_θ=0.7",
            ),
            _row(
                2,
                "P14-pack",
                0,
                "strategy=thompson-bandit; technique=slsqp.md prior=Beta(2,2) sampled_θ=0.5",
            ),
        ],
    )
    rows = diagnose.parse_cycle_log(log)
    # warm-start.md appears on P1 + P9 → 1 rediscovery; slsqp.md only P14 → 0
    assert shadow_ab.count_cross_problem_rediscoveries(rows) == 1


def test_no_rediscovery_when_each_technique_single_problem(tmp_path: Path) -> None:
    log = _cycle_log(
        tmp_path,
        "a.md",
        [
            _row(0, "P1-erdos", 1, "technique=a.md prior=Beta(2,2) sampled_θ=0.5"),
            _row(1, "P9-func", 1, "technique=b.md prior=Beta(2,2) sampled_θ=0.5"),
        ],
    )
    rows = diagnose.parse_cycle_log(log)
    assert shadow_ab.count_cross_problem_rediscoveries(rows) == 0


# ---------------- decide (the G5 gate) ----------------


def test_decide_promotes_when_non_worse_and_rediscovery(tmp_path: Path) -> None:
    a = diagnose.parse_cycle_log(
        _cycle_log(
            tmp_path,
            "a.md",
            [
                _row(0, "P1-x", 1, "technique=t.md prior=Beta(2,2) sampled_θ=0.5"),
                _row(1, "P9-y", 1, "technique=t.md prior=Beta(3,2) sampled_θ=0.6"),
            ],
        )
    )
    b = diagnose.parse_cycle_log(
        _cycle_log(
            tmp_path,
            "b.md",
            [_row(0, "P1-x", 1, "prior=t.md(0.5)"), _row(1, "P9-y", 0, "prior=t.md(0.5)")],
        )
    )
    v = shadow_ab.decide(a, b)
    # A findings/cyc = 1.0, B = 0.5 → non-worse; rediscovery = 1 → promote
    assert v.promote is True
    assert v.cross_problem_rediscoveries == 1


def test_decide_blocks_when_findings_worse(tmp_path: Path) -> None:
    a = diagnose.parse_cycle_log(
        _cycle_log(
            tmp_path,
            "a.md",
            [
                _row(0, "P1-x", 0, "technique=t.md prior=Beta(2,2) sampled_θ=0.5"),
                _row(1, "P9-y", 0, "technique=t.md prior=Beta(2,2) sampled_θ=0.5"),
            ],
        )
    )
    b = diagnose.parse_cycle_log(
        _cycle_log(
            tmp_path,
            "b.md",
            [_row(0, "P1-x", 1, "prior=t.md(0.5)"), _row(1, "P9-y", 1, "prior=t.md(0.5)")],
        )
    )
    v = shadow_ab.decide(a, b)
    assert v.promote is False  # A findings/cyc 0.0 < B 1.0


def test_decide_blocks_without_rediscovery(tmp_path: Path) -> None:
    a = diagnose.parse_cycle_log(
        _cycle_log(
            tmp_path,
            "a.md",
            [
                _row(0, "P1-x", 1, "technique=t1.md prior=Beta(2,2) sampled_θ=0.5"),
                _row(1, "P9-y", 1, "technique=t2.md prior=Beta(2,2) sampled_θ=0.5"),
            ],
        )
    )
    b = diagnose.parse_cycle_log(_cycle_log(tmp_path, "b.md", [_row(0, "P1-x", 0, "prior=x")]))
    v = shadow_ab.decide(a, b)
    # findings non-worse, but no technique on >=2 problems → block
    assert v.cross_problem_rediscoveries == 0
    assert v.promote is False


# ---------------- verdict log ----------------


def test_append_run_writes_header_and_row(tmp_path: Path) -> None:
    log = tmp_path / "meta-shadow-runs.md"
    v = shadow_ab.Verdict(
        promote=True,
        reason="findings/cyc A=1.000 >= B=0.500; cross-problem rediscoveries=1 (need >=1)",
        a_findings_per_cycle=1.0,
        b_findings_per_cycle=0.5,
        cross_problem_rediscoveries=1,
        a_cycles=2,
        b_cycles=2,
    )
    shadow_ab.append_run(
        log,
        timestamp=dt.datetime(2026, 5, 27, tzinfo=dt.timezone.utc),
        mode="wiring-validation",
        n_cycles=2,
        problems=[1, 9],
        verdict=v,
    )
    text = log.read_text()
    assert "meta-shadow runs" in text  # header
    assert "human-gated" in text
    assert "| 2026-05-27T00:00:00Z | wiring-validation | 2 | P1,P9 |" in text
    assert "| yes |" in text


# ---------------- orchestration (injected runner) ----------------


def test_run_shadow_ab_with_stub_runner(tmp_path: Path) -> None:
    """End-to-end metric→verdict→log with a stub arm runner (no live cycles)."""

    def stub_runner(arm, bandit, problems, n_cycles, cycle_log):
        if bandit:
            rows = [
                _row(0, "P1-x", 1, "technique=warm.md prior=Beta(3,2) sampled_θ=0.6"),
                _row(1, "P9-y", 1, "technique=warm.md prior=Beta(4,2) sampled_θ=0.7"),
            ]
        else:
            rows = [
                _row(0, "P1-x", 0, "prior=warm.md(0.5)"),
                _row(1, "P9-y", 1, "prior=warm.md(0.5)"),
            ]
        _cycle_log(tmp_path, cycle_log.name, rows)

    res = shadow_ab.run_shadow_ab(
        [1, 9],
        2,
        arm_a_log=tmp_path / "armA.md",
        arm_b_log=tmp_path / "armB.md",
        arm_runner=stub_runner,
        shadow_log=tmp_path / "shadow.md",
        mode="wiring-validation",
        now=dt.datetime(2026, 5, 27, tzinfo=dt.timezone.utc),
    )
    assert res.verdict.promote is True
    assert res.verdict.cross_problem_rediscoveries == 1
    assert (tmp_path / "shadow.md").read_text().count("wiring-validation") == 1
