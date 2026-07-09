"""Tests for src/einstein/research_synthesis/shadow.py (Goal 6 of js/feat/research-synthesis)."""

from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from einstein.meta_loop.proposals import Proposal, ProposalType
from einstein.research_synthesis import shadow

# ---------------- cycles_with_citations ----------------


CYCLE_LOG_FIXTURE = textwrap.dedent("""\
    # Cycle log

    ## Cycles

    | # | problem | start → end | hours | compute | wiki cites | findings+ | concepts+ | mix | outcome | notes | cites_src |
    |---|---|---|---|---|---|---|---|---|---|---|---|
    | 10 | P14-x | 1.0 → 1.0 | 0.1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | smoke | 2 |
    | 11 | P14-x | 1.0 → 1.0 | 0.1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | smoke | 0 |
    | 12 | P14-x | 1.0 → 1.0 | 0.1 | local-cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | smoke | 3 |
""")


def test_cycles_with_citations_counts_nonzero_cites_src(tmp_path: Path) -> None:
    p = tmp_path / "cycle-log.md"
    p.write_text(CYCLE_LOG_FIXTURE)
    assert shadow.cycles_with_citations(p) == 2  # rows 10 and 12 have cites_src > 0


def test_cycles_with_citations_since_filter(tmp_path: Path) -> None:
    """since_cycle_id=10 excludes cycle 10."""
    p = tmp_path / "cycle-log.md"
    p.write_text(CYCLE_LOG_FIXTURE)
    # cycle_id > 10 → only 12 qualifies (11 has 0 cites)
    assert shadow.cycles_with_citations(p, since_cycle_id=10) == 1


def test_cycles_with_citations_missing_file_returns_zero(tmp_path: Path) -> None:
    assert shadow.cycles_with_citations(tmp_path / "missing.md") == 0


def test_cycles_with_citations_from_sidecar_counts_arm_records(tmp_path: Path) -> None:
    """G9: sidecar reader counts records with arm=<arm> + non-empty cited_sources."""
    sidecar = tmp_path / "cited-sources.jsonl"
    sidecar.write_text(
        '{"cycle_id": 1, "problem": "P14", "cited_sources": ["knowledge/source/X.md"], "ts": "2026-05-25T10:00:00+00:00", "arm": "A"}\n'
        '{"cycle_id": 2, "problem": "P14", "cited_sources": [], "ts": "2026-05-25T10:01:00+00:00", "arm": "A"}\n'
        '{"cycle_id": 3, "problem": "P19", "cited_sources": ["knowledge/source/Y.md"], "ts": "2026-05-25T10:02:00+00:00", "arm": "A"}\n'
        '{"cycle_id": 1, "problem": "P14", "cited_sources": ["knowledge/source/Z.md"], "ts": "2026-05-25T10:03:00+00:00", "arm": "B"}\n'
    )
    assert shadow.cycles_with_citations_from_sidecar(sidecar, arm="A") == 2  # cycles 1, 3
    assert shadow.cycles_with_citations_from_sidecar(sidecar, arm="B") == 1


def test_cycles_with_citations_from_sidecar_since_ts_filter(tmp_path: Path) -> None:
    """since_ts excludes records at/before the cutoff."""
    sidecar = tmp_path / "cited-sources.jsonl"
    sidecar.write_text(
        '{"cycle_id": 1, "cited_sources": ["X"], "ts": "2026-05-25T10:00:00+00:00", "arm": "A"}\n'
        '{"cycle_id": 2, "cited_sources": ["Y"], "ts": "2026-05-25T11:00:00+00:00", "arm": "A"}\n'
    )
    # since_ts cuts off everything at or before 10:30
    n = shadow.cycles_with_citations_from_sidecar(
        sidecar, arm="A", since_ts="2026-05-25T10:30:00+00:00"
    )
    assert n == 1


def test_cycles_with_citations_from_sidecar_missing_file_returns_zero(tmp_path: Path) -> None:
    assert shadow.cycles_with_citations_from_sidecar(tmp_path / "missing.jsonl", arm="A") == 0


def test_cycles_with_citations_from_sidecar_ignores_arm_mismatch(tmp_path: Path) -> None:
    """Records without arm field, or with different arm, don't count."""
    sidecar = tmp_path / "cited-sources.jsonl"
    sidecar.write_text(
        # No arm field — pre-G9 record
        '{"cycle_id": 1, "cited_sources": ["X"], "ts": "2026-05-25T10:00:00+00:00"}\n'
        # arm=B
        '{"cycle_id": 2, "cited_sources": ["Y"], "ts": "2026-05-25T10:01:00+00:00", "arm": "B"}\n'
    )
    assert shadow.cycles_with_citations_from_sidecar(sidecar, arm="A") == 0


def test_cycles_with_citations_from_sidecar_skips_malformed(tmp_path: Path) -> None:
    sidecar = tmp_path / "cited-sources.jsonl"
    sidecar.write_text('not json\n{"cycle_id": 1, "cited_sources": ["X"], "arm": "A"}\n')
    assert shadow.cycles_with_citations_from_sidecar(sidecar, arm="A") == 1


def test_cycles_with_citations_no_trailing_column(tmp_path: Path) -> None:
    """Pre-G4 rows (no cites_src column) don't match the regex → 0 counted."""
    p = tmp_path / "cycle-log.md"
    p.write_text("| 1 | P | 1→1 | 0.1 | cpu | 0 | 0 | 0 | a:1/h:0/hyb:0 | no-change | smoke |\n")
    assert shadow.cycles_with_citations(p) == 0


# ---------------- synthesis_promotion_decision ----------------


def test_promotion_decision_a_wins_when_all_gates_pass() -> None:
    d = shadow.synthesis_promotion_decision(
        findings_delta=0.5,
        score_changed_delta=0.1,
        cycles_with_citations_a=3,
        cycles_with_citations_b=0,
    )
    assert d.a_wins is True
    assert "a_wins=true" in d.reason


def test_promotion_decision_negative_findings_delta_fails() -> None:
    d = shadow.synthesis_promotion_decision(
        findings_delta=-0.5,
        score_changed_delta=0.0,
        cycles_with_citations_a=5,
        cycles_with_citations_b=0,
    )
    assert d.a_wins is False
    assert "findings_delta" in d.reason


def test_promotion_decision_score_regression_fails() -> None:
    d = shadow.synthesis_promotion_decision(
        findings_delta=0.5,
        score_changed_delta=-0.1,
        cycles_with_citations_a=5,
        cycles_with_citations_b=0,
    )
    assert d.a_wins is False
    assert "score_changed_delta" in d.reason


def test_promotion_decision_zero_citation_cycles_fails() -> None:
    """The citation-grounded requirement — without it, A is just expensive noise."""
    d = shadow.synthesis_promotion_decision(
        findings_delta=0.5,
        score_changed_delta=0.5,
        cycles_with_citations_a=0,
        cycles_with_citations_b=0,
    )
    assert d.a_wins is False
    assert "zero citation-grounded" in d.reason


def test_promotion_decision_carries_arm_counts() -> None:
    d = shadow.synthesis_promotion_decision(
        findings_delta=0.0,
        score_changed_delta=0.0,
        cycles_with_citations_a=4,
        cycles_with_citations_b=1,
    )
    assert d.cycles_with_citations_a == 4
    assert d.cycles_with_citations_b == 1


# ---------------- make_synthesis_proposal ----------------


def test_make_synthesis_proposal_validates() -> None:
    """Proposal.__post_init__ validates; if our diff/target/id are wrong, this throws."""
    p = shadow.make_synthesis_proposal()
    assert isinstance(p, Proposal)
    assert p.type == ProposalType.RULE_EDIT.value
    assert p.target_path == ".claude/rules/cycle-discipline.md"
    assert p.requires_shadow is True
    assert p.confidence == "low"
    assert p.predicted_regressions  # non-empty
    assert "synthesis" in p.rationale.lower()


def test_make_synthesis_proposal_evidence_cycles_threaded() -> None:
    p = shadow.make_synthesis_proposal(evidence_cycles=[10, 11, 12])
    assert p.evidence_cycles == [10, 11, 12]


def test_make_synthesis_proposal_serializes_round_trip() -> None:
    """The Proposal can be written and read back via meta_loop.proposals helpers."""
    p = shadow.make_synthesis_proposal()
    md = p.to_markdown()
    restored = Proposal.from_markdown(md)
    assert restored.id == p.id
    assert restored.type == p.type
    assert restored.target_path == p.target_path
    assert restored.requires_shadow is True


def test_make_synthesis_proposal_rejects_bad_id() -> None:
    """Proposal.__post_init__ rejects ids that don't match the pattern."""
    with pytest.raises(Exception):
        shadow.make_synthesis_proposal(proposal_id="X")  # too short


def test_synthesis_rule_diff_applies_cleanly_against_live_file() -> None:
    """Regression guard: `git apply --check` on the diff against the live
    .claude/rules/cycle-discipline.md must succeed. Without this, --execute
    fails at apply-to-A and the whole shadow run aborts (we hit this in the
    first --execute attempt: hand-crafted hunk header was wrong).
    """
    import subprocess

    proc = subprocess.run(
        ["git", "apply", "--check", "-"],
        input=shadow.SYNTHESIS_RULE_DIFF,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"SYNTHESIS_RULE_DIFF doesn't apply cleanly: stderr={proc.stderr}"


# ---------------- CLI orchestrator ----------------


def test_cli_dry_run_prints_proposal_summary(tmp_path: Path) -> None:
    """--dry-run prints the proposal + plan; no side effects."""
    import io
    import sys as _sys

    _sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
    import research_synthesis_shadow as script

    out = io.StringIO()
    rc = script.run_cli(
        n_cycles=5,
        proposal_id="rs-shadow-test",
        evidence_cycles=[10, 11, 12],
        dry_run=True,
        execute=False,
        out_stream=out,
    )
    assert rc == 0
    s = out.getvalue()
    assert "Proposal" in s
    assert "rs-shadow-test" in s
    assert "n_cycles per arm: 5" in s
    assert "citation-grounded" in s


def test_cli_execute_without_runner_uses_stub_for_smoke(tmp_path: Path, monkeypatch) -> None:
    """With a stub cycle_runner that returns empty rows, the CLI surfaces 'no delta'."""
    import io
    import sys as _sys

    _sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
    import research_synthesis_shadow as script

    from einstein.meta_loop import shadow as ml_shadow

    # Stub out the heavy run_shadow with a controlled fake.
    fake_called: dict = {}

    class _FakeResult:
        delta = None
        a_wins = False
        error = None
        proposal_id = "x"
        n_cycles = 1

    def fake_run_shadow(proposal, **kwargs):
        fake_called["proposal_id"] = proposal.id
        return _FakeResult()

    monkeypatch.setattr(ml_shadow, "run_shadow", fake_run_shadow)
    monkeypatch.setattr(script.ml_shadow, "run_shadow", fake_run_shadow)

    out = io.StringIO()
    rc = script.run_cli(
        n_cycles=1,
        proposal_id="rs-shadow-test",
        dry_run=False,
        execute=True,
        shadow_log=tmp_path / "shadow.md",
        out_stream=out,
        cycle_runner=lambda arm_path, n: [],
    )
    assert rc == 1
    assert fake_called.get("proposal_id") == "rs-shadow-test"
    assert "no delta" in out.getvalue()
