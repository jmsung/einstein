"""Tests for src/einstein/meta_loop/propose.py — agentic proposer harness.

The LLM call is injected so unit tests don't shell out. The real `_default_proposer`
path is covered manually.
"""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import propose  # noqa: E402
from einstein.meta_loop.proposals import ProposalStore, ProposalType  # noqa: E402

UTC = dt.timezone.utc


def _now() -> dt.datetime:
    return dt.datetime(2026, 5, 25, 12, 0, 0, tzinfo=UTC)


@pytest.fixture
def fake_repo(tmp_path: Path) -> dict[str, Path]:
    """Lay down enough structure for propose.run() to call diagnose.run()."""
    cycle_log = tmp_path / "agent" / "cycle-log.md"
    skill_library = tmp_path / "agent" / "skill-library.md"
    findings_dir = tmp_path / "wiki" / "findings"
    questions_dir = tmp_path / "wiki" / "questions"
    for d in (cycle_log.parent, findings_dir, questions_dir):
        d.mkdir(parents=True, exist_ok=True)
    # Minimum viable cycle-log so diagnose.run doesn't choke
    cycle_log.write_text(
        "# cycle log\n\n"
        "| # | problem | start → end score | hours | compute | wiki cites "
        "| findings+ | concepts+ | author mix | outcome | notes |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
        "| 49 | P14 | 2.6 (no Δ) | 0 | local | 0 | 1 | 0 | a:1 | dead-end "
        "| manifest-blocked / strict-tol-unsafe |\n"
    )
    skill_library.write_text(
        "# skill\n\n| technique | category | tried | top3 | finding | last_used | hit_rate |\n"
        "|---|---|---|---|---|---|---|\n"
        "| `slsqp.md` | packing | 6 | 4 | 1 | 2026-04-12 | 0.67 |\n"
    )
    return {
        "cycle_log": cycle_log,
        "skill_library": skill_library,
        "findings_dir": findings_dir,
        "questions_dir": questions_dir,
        "mb_logs_dir": tmp_path / "mb-logs",
        "proposals_root": tmp_path / "proposals",
        "output": tmp_path / "mb-logs" / "meta-loop-report.md",
    }


# ---------------- _extract_json_array ----------------


def test_extract_json_fenced() -> None:
    text = 'Some prose.\n\n```json\n[{"type": "rule_edit"}]\n```\nMore prose.\n'
    out = propose._extract_json_array(text)
    assert out == [{"type": "rule_edit"}]


def test_extract_json_unfenced_fallback() -> None:
    text = '[{"type": "new_question"}]'
    out = propose._extract_json_array(text)
    assert out == [{"type": "new_question"}]


def test_extract_json_empty_on_garbage() -> None:
    assert propose._extract_json_array("not json at all") == []
    assert propose._extract_json_array("") == []


def test_extract_json_empty_on_non_array() -> None:
    # Single object, not array → reject
    assert propose._extract_json_array('{"type": "rule_edit"}') == []


# ---------------- propose.run with injected proposer ----------------


def test_run_writes_proposals_via_stub(fake_repo: dict[str, Path]) -> None:
    """Inject a stub proposer that emits one valid new_question proposal."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        # Sanity-check the input contract — proposer should see the diagnostic
        assert "manifest" in inp.report_text or "Cycles summary" in inp.report_text
        return [
            {
                "type": ProposalType.NEW_QUESTION.value,
                "target_path": "docs/wiki/questions/2026-05-25-test-q.md",
                "proposed_diff": (
                    "---\ntype: question\nauthor: agent\n"
                    "drafted: 2026-05-25\nstatus: open\n---\n\n"
                    "test question body\n"
                ),
                "evidence_cycles": [49],
                "expected_metric_delta": {},
                "predicted_regressions": ["none — read-only"],
                "confidence": "low",
                "requires_shadow": False,
                "rationale": "From the P14 manifest regression",
            }
        ]

    out = propose.run(
        proposer=stub,
        now=_now(),
        **fake_repo,
    )
    assert out.proposer_error is None
    assert len(out.written) == 1
    assert len(out.rejected_raw) == 0
    # Diagnostic was refreshed
    assert fake_repo["output"].exists()
    # Pending dir contains exactly one proposal
    store = ProposalStore(fake_repo["proposals_root"])
    pending = store.list_pending()
    assert len(pending) == 1
    assert pending[0].type == ProposalType.NEW_QUESTION.value


def test_run_rejects_malformed_proposals(fake_repo: dict[str, Path]) -> None:
    """Stub emits one valid + two malformed proposals — only the valid one lands."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        return [
            # Valid
            {
                "type": ProposalType.NEW_QUESTION.value,
                "target_path": "docs/wiki/questions/2026-05-25-ok.md",
                "proposed_diff": "---\nbody\n---\n",
                "evidence_cycles": [49],
                "predicted_regressions": ["none"],
                "confidence": "low",
            },
            # Bad — disallowed type
            {
                "type": "code_edit",
                "target_path": "src/foo.py",
                "proposed_diff": "diff",
            },
            # Bad — target_path policy mismatch
            {
                "type": ProposalType.RULE_EDIT.value,
                "target_path": "src/einstein/optimizer.py",
                "proposed_diff": "diff",
                "predicted_regressions": ["x"],
            },
        ]

    out = propose.run(proposer=stub, now=_now(), **fake_repo)
    assert len(out.written) == 1
    assert len(out.rejected_raw) == 2


def test_run_handles_proposer_exception(fake_repo: dict[str, Path]) -> None:
    """If the proposer raises, the harness reports the error in proposer_error."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        raise RuntimeError("simulated LLM unavailable")

    out = propose.run(proposer=stub, now=_now(), **fake_repo)
    assert out.written == []
    assert out.proposer_error is not None
    assert "simulated LLM unavailable" in out.proposer_error


def test_run_empty_proposer_output_is_fine(fake_repo: dict[str, Path]) -> None:
    """Honest answer of `[]` is the expected default — should not error."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        return []

    out = propose.run(proposer=stub, now=_now(), **fake_repo)
    assert out.written == []
    assert out.rejected_raw == []
    assert out.proposer_error is None


def test_default_regressions_backfilled_when_missing(fake_repo: dict[str, Path]) -> None:
    """If proposer forgets predicted_regressions, harness backfills "(none stated)"."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        return [
            {
                "type": ProposalType.NEW_QUESTION.value,
                "target_path": "docs/wiki/questions/2026-05-25-no-reg.md",
                "proposed_diff": "---\nbody\n---\n",
                "evidence_cycles": [49],
                "confidence": "low",
            },
        ]

    out = propose.run(proposer=stub, now=_now(), **fake_repo)
    assert len(out.written) == 1
    text = out.written[0].read_text()
    assert "none stated" in text  # the placeholder shows up in the audit


def test_default_proposer_id_tagged_on_llm_path(fake_repo: dict[str, Path]) -> None:
    """A raw proposal without proposer_id is tagged metaharness-llm-v1 (the LLM path)."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        return [
            {
                "type": ProposalType.NEW_QUESTION.value,
                "target_path": "docs/wiki/questions/2026-05-25-prov.md",
                "proposed_diff": "---\nbody\n---\n",
                "evidence_cycles": [49],
                "predicted_regressions": ["none"],
                "confidence": "low",
            },
        ]

    out = propose.run(proposer=stub, now=_now(), **fake_repo)
    assert len(out.written) == 1
    assert f"proposer_id: {propose.DEFAULT_PROPOSER_ID}" in out.written[0].read_text()


def test_explicit_proposer_id_survives(fake_repo: dict[str, Path]) -> None:
    """A raw proposal carrying proposer_id keeps it — a non-LLM proposer's tag wins."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        return [
            {
                "type": ProposalType.NEW_QUESTION.value,
                "target_path": "docs/wiki/questions/2026-05-25-bandit.md",
                "proposed_diff": "---\nbody\n---\n",
                "evidence_cycles": [49],
                "predicted_regressions": ["none"],
                "confidence": "low",
                "proposer_id": "thompson-bandit-v0",
            },
        ]

    out = propose.run(proposer=stub, now=_now(), **fake_repo)
    assert len(out.written) == 1
    assert "proposer_id: thompson-bandit-v0" in out.written[0].read_text()


def test_proposer_can_override_requires_shadow_default(fake_repo: dict[str, Path]) -> None:
    """Proposer can set requires_shadow explicitly for any type."""

    def stub(inp: propose.ProposerInput) -> list[dict]:
        return [
            {
                "type": ProposalType.RULE_EDIT.value,
                "target_path": ".claude/rules/agent-stance.md",
                "proposed_diff": "--- a/r\n+++ b/r\n+x\n",
                "evidence_cycles": [49],
                "predicted_regressions": ["might slow recon"],
                "confidence": "medium",
                "requires_shadow": False,  # explicitly opt out
            },
        ]

    out = propose.run(proposer=stub, now=_now(), **fake_repo)
    assert len(out.written) == 1
    text = out.written[0].read_text()
    # `requires_shadow: false` survived round-trip via the markdown frontmatter
    body = text.split("---\n")[1] if "---" in text else text
    assert "requires_shadow: false" in body
