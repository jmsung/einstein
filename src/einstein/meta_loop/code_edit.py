"""meta_loop.code_edit — Goal 2 draft-writer for code_edit proposals.

Reads a `ToolGap` (from `tool_gaps.detect_recurring_tool_gaps`) and emits a
`Proposal` of type `code_edit` whose `proposed_diff` is the full body of a
new `scripts/proposed/<tool>.py` draft (signature + docstring + cite block +
`NotImplementedError` body).

Design rationale: `tool-autosynthesis-design.md`. The proposer drafts the
*contract* (path, signature, citation block) and refuses to hallucinate
the body — matching SkillClaw's "skip > speculative edit" guardrail. The
shadow A/B's B-arm (Goal 4) is what gets the chance to flesh the body out
from inside a real cycle, or the human writes it during human-approval.

Why a Python-side helper rather than an LLM call: the gap-detector already
produced a structured `ToolGap`. Synthesizing the draft body from that
structure is deterministic — no token spend needed for the boilerplate.
A future variant could ask an LLM to fill the body, but `_default_proposer`
in `propose.py` is already the LLM surface; this module deliberately stays
LLM-free for the boilerplate stage.
"""

from __future__ import annotations

import datetime as dt
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from .code_edit_context import CodeEditContext
from .proposals import (
    Confidence,
    Proposal,
    ProposalType,
    ProposalValidationError,
    make_proposal_id,
)
from .tool_gaps import ToolGap

log = logging.getLogger("meta_loop.code_edit")

PROPOSER_ID = "tool-autosynthesis-v0"

# Provenance tag when the body was filled by the LLM body-writer (Goal 2/3),
# distinct from the stub proposer above. The audit trail keeps them separate.
BODY_WRITER_PROPOSER_ID = "tool-autosynthesis-body-writer-v1"

# The body-writer system prompt lives in a file so it can be A/B'd and
# shadow-compared without a code edit (mirrors propose.DEFAULT_PROMPT_PATH).
# cb root = parents[3] (src/einstein/meta_loop/code_edit.py).
_REPO = Path(__file__).resolve().parents[3]
BODY_WRITER_PROMPT_PATH = _REPO / "docs" / "agent" / "proposer_prompts" / "body-writer-v1.md"

# Sentinel the LLM emits when it cannot honestly write a body.
ABSTAIN = "ABSTAIN"

# Where drafts live (repo-relative). `apply_proposal_to_worktree` in
# `shadow.py` writes the file here in the arm worktree.
DRAFT_DIR = "scripts/proposed"


# ---------------- slug → identifier ----------------


_KEBAB_RE = re.compile(r"[^a-z0-9_\-]")


def _normalize_slug(slug: str) -> str:
    """Lowercase, restrict to [a-z0-9_-], collapse repeats."""
    s = _KEBAB_RE.sub("-", slug.lower())
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "unnamed-tool"


def _slug_for_gap(gap: ToolGap) -> str:
    """Pick the canonical slug for the gap's proposed tool.

    Preferred: `gap.suggested_tool` (extracted from "not yet wired"
    patterns). Fallback for fungible markers: synthesize from the
    pattern + problem list ("dispatch-fallback-p1-p9-p14").
    """
    if gap.suggested_tool:
        return _normalize_slug(gap.suggested_tool)
    problems = "-".join(p.lower() for p in sorted(set(gap.problem_ids))[:4])
    base = gap.pattern.replace("_", "-")
    return _normalize_slug(f"{base}-{problems}")


def _python_identifier(slug: str) -> str:
    """Convert a kebab slug to a snake_case Python identifier."""
    return slug.replace("-", "_")


# ---------------- draft body ----------------


def _render_draft_body(gap: ToolGap, *, slug: str, drafted: str) -> str:
    """Render the `scripts/proposed/<slug>.py` body for the given gap.

    The body is a runnable Python file with:
    - A docstring naming the gap, citing cycles + problems + questions.
    - A `main()` stub that raises NotImplementedError.
    - A `__main__` guard so the file is dispatch-callable but always
      exits non-zero until the body is written.
    """
    qpaths = [str(p) for p in gap.open_questions]
    questions_block = "\n".join(f"- {q}" for q in qpaths) if qpaths else "(none filed yet)"
    py_id = _python_identifier(slug)
    return f'''"""scripts/proposed/{slug}.py — autosynthesized draft.

Source: tool-autosynthesis (proposer {PROPOSER_ID}, drafted {drafted}).
Promotion gate: ANY use of this script must clear the
`tool_autosynthesis_promotion_decision` chain (validator + shadow A/B +
human approval). See `docs/wiki/findings/tool-autosynthesis-design.md`.

DO NOT IMPORT THIS MODULE FROM PRODUCTION CODE. It lives under
`scripts/proposed/` precisely because it is unverified; promotion to
`scripts/` happens via `apply_proposal_to_worktree` in `shadow.py`.

## Citation block (immutable — promotion gate verifies these)

- canonical gap: {gap.canonical}
- pattern: {gap.pattern}
- suggested tool slug: {gap.suggested_tool or "(synthesized)"}
- missing manifest entry: {gap.missing_manifest_entry or "(n/a)"}
- evidence cycles: {gap.citing_cycles}
- problems: {sorted(set(gap.problem_ids))}
- originating open questions:

{questions_block}
"""

from __future__ import annotations


def {py_id}(*args, **kwargs):
    """TODO(autosynth): implement {slug}.

    The gap recurred across {gap.cycle_count} cycles and {gap.problem_count} problems
    ({sorted(set(gap.problem_ids))}); the inner agent kept selecting this
    technique but the manifest never wired it. Either flesh the body out
    here, or write a {slug}-specific question and let the council propose
    a different shape.
    """
    raise NotImplementedError(
        "{slug} is an autosynthesized draft from tool-autosynthesis. "
        "It needs a real body before any dispatcher should pick it up."
    )


if __name__ == "__main__":
    {py_id}()
'''


# ---------------- LLM body-writer (Goal 2) ----------------


class BodyWriterError(RuntimeError):
    """The body-writer LLM call failed (auth/quota/timeout/non-zero)."""


@dataclass
class BodyWriterInput:
    """Context handed to a body-writer proposer callable."""

    gap: ToolGap
    context: CodeEditContext
    stub_body: str  # the full stub file (docstring + NotImplementedError body)
    py_identifier: str
    prompt_path: Path = BODY_WRITER_PROMPT_PATH


# A swappable proposer: takes a BodyWriterInput, returns the raw LLM text
# (a ```python fenced body, or the ABSTAIN sentinel). Tests inject a stub.
BodyWriterProposer = Callable[["BodyWriterInput"], str]


# The leading module docstring is the first triple-quoted string. We splice
# the LLM body AFTER it so the cite block stays byte-for-byte (the promotion
# gate parses `- problems: [...]` from it). See code-edit-body-writer-design.md.
def _split_module_docstring(stub: str) -> tuple[str, str]:
    """Return (docstring_block, remainder).

    `docstring_block` is the leading triple-quoted module docstring including
    its closing quotes and the trailing newline. `remainder` is everything
    after — the part the body-writer replaces. Raises ValueError if the stub
    doesn't open with a module docstring (it always does, by
    `_render_draft_body` construction).
    """
    if not stub.startswith('"""'):
        raise ValueError("stub does not open with a module docstring")
    close = stub.find('"""', 3)
    if close == -1:
        raise ValueError("unterminated module docstring in stub")
    end = close + 3
    # Include the trailing newline after the closing quotes, if present.
    if end < len(stub) and stub[end] == "\n":
        end += 1
    return stub[:end], stub[end:]


_PY_FENCE_RE = re.compile(r"```(?:python)?\s*\n(.*?)\n```", re.DOTALL)


def _extract_code_block(text: str) -> str | None:
    """Pull the post-docstring body out of the LLM response.

    Returns None if the model abstained (`ABSTAIN` sentinel) or emitted
    nothing usable. Prefers a fenced ```python block; falls back to the whole
    response when no fence is present (some models drop it).
    """
    if not text:
        return None
    if text.strip() == ABSTAIN:
        return None
    m = _PY_FENCE_RE.search(text)
    body = (m.group(1) if m else text).strip()
    if not body or body == ABSTAIN:
        return None
    return body


def _render_body_writer_prompt(inp: BodyWriterInput) -> str:
    system = Path(inp.prompt_path).read_text().rstrip()
    return (
        system
        + "\n\n--- GAP + EVIDENCE ---\n"
        + inp.context.render_prompt_context()
        + "\n\n--- EXISTING DRAFT (docstring is immutable; replace the body below it) ---\n"
        + f"```python\n{inp.stub_body}\n```\n"
        + f"\nEmit the post-docstring body that defines `{inp.py_identifier}`.\n"
    )


def _default_body_writer(inp: BodyWriterInput) -> str:
    """Shell out via `claude_headless` to fill the body. Lazy-imports the tool.

    Token budget is capped at the wrapper's default; the context gatherer
    already truncates inputs to the ~30K-token envelope.
    """
    import importlib.util as _ilu
    import sys as _sys

    tools_dir = _REPO / "docs" / "tools"
    if str(tools_dir) not in _sys.path:
        _sys.path.insert(0, str(tools_dir))
    spec = _ilu.find_spec("claude_headless")
    if spec is None or spec.loader is None:
        raise BodyWriterError(f"claude_headless not importable from {tools_dir}")
    claude_headless = _ilu.module_from_spec(spec)
    spec.loader.exec_module(claude_headless)

    result = claude_headless.run(
        prompt=_render_body_writer_prompt(inp),
        allowed_tools=["Read", "Grep", "Glob"],
        output_format="text",
        timeout_seconds=600,
        add_dirs=[_REPO / "docs", _REPO / "scripts", _REPO / "src"],
    )
    if not result.ok:
        raise BodyWriterError(
            f"body-writer LLM call failed: kind={result.error_kind} "
            f"message={result.error_message!r}"
        )
    return result.stdout


def write_body_llm(
    gap: ToolGap,
    context: CodeEditContext,
    *,
    stub_body: str,
    proposer: BodyWriterProposer | None = None,
    prompt_path: Path | None = None,
) -> str | None:
    """Ask the body-writer to replace the stub's body, preserving the docstring.

    Splices the LLM-generated post-docstring body onto the stub's leading
    module docstring (which carries the immutable cite block). Returns the
    full new file body, or None if the LLM abstained / emitted nothing usable
    (caller keeps the stub).

    Args:
        gap: the gap the draft is for (provenance + threshold already checked).
        context: gathered evidence from `code_edit_context.gather_context`.
        stub_body: the full stub file from `_render_draft_body`.
        proposer: injectable callable for tests; defaults to the claude_headless
            body-writer.
        prompt_path: system-prompt override (A/B without code edit).

    Raises:
        BodyWriterError: the LLM call itself failed (distinct from abstain).
    """
    proposer = proposer or _default_body_writer
    docstring_block, _ = _split_module_docstring(stub_body)
    inp = BodyWriterInput(
        gap=gap,
        context=context,
        stub_body=stub_body,
        py_identifier=context.py_identifier,
        prompt_path=prompt_path or BODY_WRITER_PROMPT_PATH,
    )
    raw = proposer(inp)
    body = _extract_code_block(raw)
    if body is None:
        log.info("body-writer abstained for gap %r — keeping stub", gap.canonical)
        return None
    return docstring_block + "\n" + body + "\n"


# ---------------- proposal helpers ----------------


def make_code_edit_proposal(
    gap: ToolGap,
    *,
    now: dt.datetime | None = None,
    confidence: str = Confidence.LOW.value,
    write_body: bool = False,
    repo_root: Path | None = None,
    manifest_path: Path | None = None,
    body_proposer: "BodyWriterProposer | None" = None,
    prompt_path: Path | None = None,
) -> Proposal:
    """Build a `code_edit` Proposal from a threshold-passing ToolGap.

    Returns a Proposal whose `proposed_diff` is the full draft body.
    `apply_proposal_to_worktree` (in `shadow.py`) writes the body to
    `scripts/proposed/<slug>.py` and commits in the arm worktree.

    By default the body is the `NotImplementedError` stub (the safe Phase-1
    contract). With `write_body=True` the LLM body-writer (Goal 2) replaces
    the stub with a real body, gathering context from the cited problems'
    rank-current scripts. `repo_root` is required in that mode (it's where
    `gather_context` reads the examples). If the body-writer abstains, the
    stub is kept and the proposer_id stays `tool-autosynthesis-v0`.

    Raises `ProposalValidationError` if the gap doesn't actually clear the
    recurrence threshold (≥3 cycles, ≥2 problems) — the proposer should
    not fire on noise. Raises `ValueError` if `write_body=True` without a
    `repo_root`. Propagates `BodyWriterError` if the LLM call itself fails.
    """
    if not gap.meets_threshold():
        raise ProposalValidationError(
            f"gap {gap.canonical!r} below threshold: "
            f"{gap.cycle_count} cycles across {gap.problem_count} problems"
        )
    now = now or dt.datetime.now(dt.timezone.utc)
    slug = _slug_for_gap(gap)
    target = f"{DRAFT_DIR}/{slug}.py"
    body = _render_draft_body(gap, slug=slug, drafted=now.strftime("%Y-%m-%d"))

    proposer_id = PROPOSER_ID
    predicted_regressions = [
        "draft body raises NotImplementedError — strategy_picker that "
        "selects it before promotion will dispatch-fail",
    ]
    if write_body:
        if repo_root is None:
            raise ValueError("write_body=True requires repo_root (for gather_context)")
        # Lazy import to keep the module-level import graph identical to Phase 1.
        from . import code_edit_context

        ctx = code_edit_context.gather_context(
            gap, repo_root=repo_root, manifest_path=manifest_path
        )
        new_body = write_body_llm(
            gap,
            ctx,
            stub_body=body,
            proposer=body_proposer,
            prompt_path=prompt_path,
        )
        if new_body is not None:
            body = new_body
            proposer_id = BODY_WRITER_PROPOSER_ID
            predicted_regressions = [
                "LLM-written body may compute a wrong score — caught by shadow "
                "A/B (no finding produced) + triple-verify before any submission",
            ]

    pid = make_proposal_id(
        proposal_type=ProposalType.CODE_EDIT.value,
        target_path=target,
        now=now,
    )
    return Proposal(
        id=pid,
        type=ProposalType.CODE_EDIT.value,
        target_path=target,
        proposed_diff=body,
        evidence_cycles=list(gap.citing_cycles),
        expected_metric_delta={"tool_invoked_cycles_a": 1.0},
        predicted_regressions=predicted_regressions,
        confidence=confidence,
        requires_shadow=True,
        rationale=(
            f"tool gap {gap.canonical!r} recurred across "
            f"{gap.cycle_count} cycles / {gap.problem_count} problems; "
            f"manifest doesn't wire a {slug} script."
        ),
        proposer_id=proposer_id,
        created_at=now,
    )


def apply_code_edit_to_worktree(
    proposal: Proposal,
    worktree: Path,
) -> Path:
    """Write the draft to `<worktree>/scripts/proposed/<slug>.py`.

    Refuses to overwrite an existing `scripts/<slug>.py` OR
    `scripts/proposed/<slug>.py`. Returns the written path.

    This is the *raw* apply step — no git add/commit. The shadow harness's
    `apply_proposal_to_worktree` adds the commit; this helper exists for
    callers that want the file write without the git plumbing (e.g.
    unit-test fixtures, the Goal 3 sandbox validator).
    """
    if proposal.type != ProposalType.CODE_EDIT.value:
        raise ValueError(f"expected code_edit, got {proposal.type!r}")
    slug = Path(proposal.target_path).stem
    proposed = worktree / "scripts" / "proposed" / f"{slug}.py"
    graduated = worktree / "scripts" / f"{slug}.py"
    if graduated.exists():
        raise FileExistsError(
            f"refusing to draft {slug!r}: scripts/{slug}.py already exists "
            "(promotion is the only path to scripts/<slug>.py)"
        )
    if proposed.exists():
        raise FileExistsError(f"draft already exists at {proposed}; remove or rename first")
    proposed.parent.mkdir(parents=True, exist_ok=True)
    proposed.write_text(proposal.proposed_diff)
    return proposed


__all__ = [
    "ABSTAIN",
    "BODY_WRITER_PROMPT_PATH",
    "BODY_WRITER_PROPOSER_ID",
    "DRAFT_DIR",
    "PROPOSER_ID",
    "BodyWriterError",
    "BodyWriterInput",
    "apply_code_edit_to_worktree",
    "make_code_edit_proposal",
    "write_body_llm",
]
