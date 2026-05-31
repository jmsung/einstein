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
import re
from pathlib import Path

from .proposals import (
    Confidence,
    Proposal,
    ProposalType,
    ProposalValidationError,
    make_proposal_id,
)
from .tool_gaps import ToolGap

PROPOSER_ID = "tool-autosynthesis-v0"

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


# ---------------- proposal helpers ----------------


def make_code_edit_proposal(
    gap: ToolGap,
    *,
    now: dt.datetime | None = None,
    confidence: str = Confidence.LOW.value,
) -> Proposal:
    """Build a `code_edit` Proposal from a threshold-passing ToolGap.

    Returns a Proposal whose `proposed_diff` is the full draft body.
    `apply_proposal_to_worktree` (in `shadow.py`) writes the body to
    `scripts/proposed/<slug>.py` and commits in the arm worktree.

    Raises `ProposalValidationError` if the gap doesn't actually clear the
    recurrence threshold (≥3 cycles, ≥2 problems) — the proposer should
    not fire on noise.
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
        expected_metric_delta={"tool_invoked_cycles_b": 1.0},
        predicted_regressions=[
            "draft body raises NotImplementedError — strategy_picker that "
            "selects it before promotion will dispatch-fail",
        ],
        confidence=confidence,
        requires_shadow=True,
        rationale=(
            f"tool gap {gap.canonical!r} recurred across "
            f"{gap.cycle_count} cycles / {gap.problem_count} problems; "
            f"manifest doesn't wire a {slug} script."
        ),
        proposer_id=PROPOSER_ID,
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
    "DRAFT_DIR",
    "PROPOSER_ID",
    "apply_code_edit_to_worktree",
    "make_code_edit_proposal",
]
