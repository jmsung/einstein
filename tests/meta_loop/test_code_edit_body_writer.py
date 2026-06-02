"""Tests for the Goal 2 LLM body-writer in meta_loop/code_edit.py."""

from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO / "src"))

from einstein.meta_loop import code_edit  # noqa: E402
from einstein.meta_loop.code_edit import (  # noqa: E402
    ABSTAIN,
    BodyWriterError,
    BodyWriterInput,
    _extract_code_block,
    _split_module_docstring,
    make_code_edit_proposal,
    write_body_llm,
)
from einstein.meta_loop.code_edit_context import CodeEditContext  # noqa: E402
from einstein.meta_loop.tool_gaps import ToolGap  # noqa: E402

UTC = dt.timezone.utc


def _now() -> dt.datetime:
    return dt.datetime(2026, 6, 2, 12, 0, 0, tzinfo=UTC)


def _gap() -> ToolGap:
    return ToolGap(
        canonical="manifest_gap:mpmath-ulp-polish",
        pattern="manifest_gap",
        suggested_tool="mpmath-ulp-polish",
        missing_manifest_entry=None,
        citing_cycles=[49, 50, 70],
        problem_ids=["P14", "P11"],
        open_questions=[],
    )


def _ctx() -> CodeEditContext:
    return CodeEditContext(
        gap_canonical="manifest_gap:mpmath-ulp-polish",
        suggested_tool="mpmath-ulp-polish",
        py_identifier="mpmath_ulp_polish",
    )


def _stub() -> str:
    return make_code_edit_proposal(_gap(), now=_now()).proposed_diff


# ---------------- helpers ----------------


def test_split_module_docstring_preserves_cite_block() -> None:
    stub = _stub()
    docstring, remainder = _split_module_docstring(stub)
    # The cite block lives in the docstring half.
    assert "## Citation block" in docstring
    assert "- problems:" in docstring
    # The NotImplementedError body lives in the remainder.
    assert "NotImplementedError" in remainder
    assert "NotImplementedError" not in docstring


def test_extract_code_block_prefers_fence() -> None:
    text = "Here you go:\n```python\ndef f():\n    return 1\n```\nDone."
    assert _extract_code_block(text) == "def f():\n    return 1"


def test_extract_code_block_falls_back_to_whole_text() -> None:
    text = "def f():\n    return 1"
    assert _extract_code_block(text) == "def f():\n    return 1"


def test_extract_code_block_abstain_returns_none() -> None:
    assert _extract_code_block(ABSTAIN) is None
    assert _extract_code_block("  ABSTAIN \n") is None
    assert _extract_code_block("") is None


# ---------------- write_body_llm ----------------


def test_write_body_llm_splices_body_onto_docstring() -> None:
    stub = _stub()

    def fake(inp: BodyWriterInput) -> str:
        assert inp.py_identifier == "mpmath_ulp_polish"
        return (
            "```python\n"
            "def mpmath_ulp_polish(*args, **kwargs):\n"
            "    return 0.123\n\n\n"
            'if __name__ == "__main__":\n'
            "    print(mpmath_ulp_polish())\n"
            "```"
        )

    out = write_body_llm(_gap(), _ctx(), stub_body=stub, proposer=fake)
    assert out is not None
    # Docstring + cite block preserved verbatim.
    assert "## Citation block" in out
    assert "- problems:" in out
    # Stub body gone; real body present.
    assert "NotImplementedError" not in out
    assert "return 0.123" in out
    assert "def mpmath_ulp_polish(" in out


def test_write_body_llm_abstain_returns_none() -> None:
    out = write_body_llm(_gap(), _ctx(), stub_body=_stub(), proposer=lambda inp: ABSTAIN)
    assert out is None


def test_write_body_llm_passes_context_to_proposer() -> None:
    seen = {}

    def fake(inp: BodyWriterInput) -> str:
        seen["canonical"] = inp.context.gap_canonical
        seen["has_stub"] = "NotImplementedError" in inp.stub_body
        return "```python\ndef mpmath_ulp_polish():\n    return 1.0\n```"

    write_body_llm(_gap(), _ctx(), stub_body=_stub(), proposer=fake)
    assert seen["canonical"] == "manifest_gap:mpmath-ulp-polish"
    assert seen["has_stub"] is True


def test_write_body_llm_propagates_proposer_error() -> None:
    def boom(inp: BodyWriterInput) -> str:
        raise BodyWriterError("auth")

    with pytest.raises(BodyWriterError, match="auth"):
        write_body_llm(_gap(), _ctx(), stub_body=_stub(), proposer=boom)


def test_render_body_writer_prompt_includes_sections() -> None:
    inp = BodyWriterInput(
        gap=_gap(),
        context=_ctx(),
        stub_body=_stub(),
        py_identifier="mpmath_ulp_polish",
    )
    prompt = code_edit._render_body_writer_prompt(inp)
    assert "body-writer" in prompt.lower()
    assert "EXISTING DRAFT" in prompt
    assert "mpmath_ulp_polish" in prompt


def test_body_writer_prompt_file_exists() -> None:
    assert code_edit.BODY_WRITER_PROMPT_PATH.is_file()
    text = code_edit.BODY_WRITER_PROMPT_PATH.read_text()
    assert "ABSTAIN" in text
    assert "citation block" in text.lower()


# ---------------- Goal 3: make_code_edit_proposal(write_body=True) ----------------

from einstein.meta_loop.proposals import (  # noqa: E402
    ProposalStore,
    ProposalType,
)
from einstein.meta_loop.shadow import _parse_problem_ids_from_body  # noqa: E402


def _real_body_proposer(inp: BodyWriterInput) -> str:
    return (
        "```python\n"
        "import json\n\n\n"
        f"def {inp.py_identifier}(*args, **kwargs):\n"
        "    return 0.5\n\n\n"
        'if __name__ == "__main__":\n'
        f"    print(json.dumps({{'score': {inp.py_identifier}()}}))\n"
        "```"
    )


def test_make_proposal_write_body_replaces_stub(tmp_path: Path) -> None:
    p = make_code_edit_proposal(
        _gap(),
        now=_now(),
        write_body=True,
        repo_root=tmp_path,  # empty repo → no examples, but the proposer is stubbed
        body_proposer=_real_body_proposer,
    )
    assert "NotImplementedError" not in p.proposed_diff
    assert "return 0.5" in p.proposed_diff
    assert p.proposer_id == code_edit.BODY_WRITER_PROPOSER_ID
    # The regression prediction reflects the body-written risk, not the stub's.
    assert any("wrong score" in r for r in p.predicted_regressions)
    p._validate()


def test_make_proposal_write_body_preserves_cite_block(tmp_path: Path) -> None:
    """The spliced body must keep the cite block graduation parses."""
    p = make_code_edit_proposal(
        _gap(),
        now=_now(),
        write_body=True,
        repo_root=tmp_path,
        body_proposer=_real_body_proposer,
    )
    pids = _parse_problem_ids_from_body(p.proposed_diff)
    assert pids == ["P11", "P14"]  # sorted, from the cite block


def test_make_proposal_write_body_abstain_keeps_stub(tmp_path: Path) -> None:
    p = make_code_edit_proposal(
        _gap(),
        now=_now(),
        write_body=True,
        repo_root=tmp_path,
        body_proposer=lambda inp: ABSTAIN,
    )
    assert "NotImplementedError" in p.proposed_diff
    assert p.proposer_id == code_edit.PROPOSER_ID


def test_make_proposal_write_body_requires_repo_root() -> None:
    with pytest.raises(ValueError, match="repo_root"):
        make_code_edit_proposal(_gap(), now=_now(), write_body=True)


def test_make_proposal_default_still_stub(tmp_path: Path) -> None:
    p = make_code_edit_proposal(_gap(), now=_now())
    assert "NotImplementedError" in p.proposed_diff
    assert p.proposer_id == code_edit.PROPOSER_ID


def test_write_body_proposal_store_round_trip(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    p = make_code_edit_proposal(
        _gap(),
        now=_now(),
        write_body=True,
        repo_root=repo,
        body_proposer=_real_body_proposer,
    )
    store = ProposalStore(tmp_path / "proposals")
    path = store.write_pending(p)
    assert path.is_file()
    rt = store.list_pending()[0]
    assert rt.id == p.id
    assert rt.type == ProposalType.CODE_EDIT.value
    assert rt.proposer_id == code_edit.BODY_WRITER_PROPOSER_ID
    assert "return 0.5" in rt.proposed_diff
    assert "NotImplementedError" not in rt.proposed_diff
