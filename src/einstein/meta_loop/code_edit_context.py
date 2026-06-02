"""meta_loop.code_edit_context — Goal 1 pattern extractor for the body-writer.

`gather_context(gap)` assembles the in-context evidence an LLM needs to write
a *real* body for a `code_edit` draft (instead of the `NotImplementedError`
stub). It reads three sources, all repo-relative:

1. **Rank-current optimizer bodies** for every cited problem — the manifest's
   wired `script:` paths under `scripts/<problem>/`. These are the structural
   examples the body-writer learns from (SkillClaw's "evolve from evidence,
   not from nothing" — see `code-edit-body-writer-design.md`).
2. **The technique page** `docs/wiki/techniques/<gap.suggested_tool>.md`, if it
   exists — the prose framing for the technique the gap is asking for.
3. **The originating open questions** attached to the gap.

Read-only. Every source is head-truncated to a char budget so a fat
`scripts/<problem>/` dir can't blow the ~30K-input-token cap. The result
renders to a prompt block via `CodeEditContext.render_prompt_context()`.

Reusable beyond the body-writer: any proposer that wants sibling-problem
context (e.g. a future `manifest_tweak` that reads sibling manifest entries)
can call `gather_context` and ignore the fields it doesn't need.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .. import optimizer_dispatch
from .tool_gaps import ToolGap

# Char budgets. ~4 chars/token, ~30K input tokens → ~120K chars total. Leave
# headroom for the static prompt + cite block: cap examples at 8 × 4K = 32K,
# technique page at 8K, each question at 3K.
MAX_EXAMPLES = 8
MAX_SCRIPT_CHARS = 4000
MAX_TECHNIQUE_CHARS = 8000
MAX_QUESTION_CHARS = 3000

_PROBLEM_ID_INT_RE = re.compile(r"^P(\d+)$")

# A manifest `script:` path that has a problem subdir, e.g.
# `scripts/circle_packing_square/slsqp_polish.py`. Shared top-level scripts
# (`scripts/verify_seed.py`) are NOT technique exemplars — skip them.
_PROBLEM_SCRIPT_RE = re.compile(r"^scripts/[^/]+/[^/]+\.py$")


def _problem_id_int(pid: str) -> int | None:
    m = _PROBLEM_ID_INT_RE.match(pid)
    return int(m.group(1)) if m else None


def _head(text: str, max_chars: int) -> str:
    """Line-aware head truncation. Appends a `… (truncated)` marker."""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars]
    # Don't slice mid-line — back off to the last newline if there is one.
    nl = cut.rfind("\n")
    if nl > max_chars // 2:
        cut = cut[:nl]
    return cut + "\n# … (truncated for prompt budget)\n"


@dataclass
class ExampleScript:
    """One rank-current optimizer body, as a body-writer example."""

    path: str  # repo-relative
    problem_id: str  # "P14"
    optimizer: str  # manifest optimizer key, e.g. "mpmath_ulp_polish"
    source: str  # head-truncated file body


@dataclass
class CodeEditContext:
    """Structured prompt context for `write_body_llm`."""

    gap_canonical: str
    suggested_tool: str | None
    py_identifier: str
    example_scripts: list[ExampleScript] = field(default_factory=list)
    technique_page_path: str | None = None
    technique_page: str | None = None
    open_questions: list[tuple[str, str]] = field(default_factory=list)  # (path, text)

    def render_prompt_context(self) -> str:
        """Render the gathered evidence as a single prompt block.

        Ordering: examples first (the structural seed), then the technique
        page (the prose framing), then the open questions (the unknown).
        """
        parts: list[str] = []
        parts.append(f"## Gap\n\ncanonical: `{self.gap_canonical}`")
        if self.suggested_tool:
            parts.append(f"suggested tool slug: `{self.suggested_tool}`")
        parts.append(f"target function name: `{self.py_identifier}`")

        if self.example_scripts:
            parts.append(
                "\n## Rank-current optimizer bodies (structural examples)\n\n"
                "These are the wired, working optimizer scripts for the cited "
                "problems. Match their structure, imports, and result-file "
                "conventions. They are the evidence; do not copy verbatim."
            )
            for ex in self.example_scripts:
                parts.append(
                    f"\n### `{ex.path}` (problem {ex.problem_id}, "
                    f"optimizer `{ex.optimizer}`)\n\n```python\n{ex.source}\n```"
                )
        else:
            parts.append(
                "\n## Rank-current optimizer bodies\n\n"
                "(none wired for the cited problems — write from the technique "
                "page + question alone, conservatively.)"
            )

        if self.technique_page:
            parts.append(
                f"\n## Technique page `{self.technique_page_path}`\n\n" f"{self.technique_page}"
            )

        if self.open_questions:
            parts.append("\n## Originating open questions")
            for qpath, qtext in self.open_questions:
                parts.append(f"\n### `{qpath}`\n\n{qtext}")

        return "\n\n".join(parts)


def _gather_example_scripts(
    gap: ToolGap,
    repo_root: Path,
    manifest: dict,
) -> list[ExampleScript]:
    """Collect head-truncated manifest optimizer bodies for cited problems.

    Skips shared top-level scripts (e.g. `scripts/verify_seed.py`) and the
    gap's own suggested tool (no point feeding the body-writer a stub of the
    thing it's about to write). Dedups by path; caps at MAX_EXAMPLES.
    """
    seen: set[str] = set()
    out: list[ExampleScript] = []
    for pid in gap.problem_ids:
        n = _problem_id_int(pid)
        if n is None:
            continue
        entry = manifest.get(n)
        if not entry:
            continue
        optimizers = entry.get("optimizers") or {}
        for opt_name, block in optimizers.items():
            if not isinstance(block, dict):
                continue
            rel = block.get("script")
            if not isinstance(rel, str):
                continue
            if not _PROBLEM_SCRIPT_RE.match(rel):
                continue  # shared / non-problem script — not a technique exemplar
            if gap.suggested_tool and Path(rel).stem == gap.suggested_tool.replace("-", "_"):
                continue  # don't feed the body-writer its own (likely stub) target
            if rel in seen:
                continue
            abspath = repo_root / rel
            if not abspath.is_file():
                continue
            seen.add(rel)
            out.append(
                ExampleScript(
                    path=rel,
                    problem_id=pid,
                    optimizer=str(opt_name),
                    source=_head(abspath.read_text(), MAX_SCRIPT_CHARS),
                )
            )
            if len(out) >= MAX_EXAMPLES:
                return out
    return out


def gather_context(
    gap: ToolGap,
    *,
    repo_root: Path,
    manifest_path: Path | None = None,
) -> CodeEditContext:
    """Assemble the body-writer's in-context evidence for `gap`.

    Args:
        gap: the threshold-passing ToolGap to write a body for.
        repo_root: cb root (worktree root). All sources resolve relative to it.
        manifest_path: optimizer manifest override; defaults to the repo's
            `src/einstein/optimizer_manifest.yaml` via `load_manifest`.

    Read-only. Returns a `CodeEditContext` whose `render_prompt_context()` is
    the prompt body for `write_body_llm`.
    """
    manifest = optimizer_dispatch.load_manifest(manifest_path)
    py_id = (gap.suggested_tool or gap.pattern).replace("-", "_")

    examples = _gather_example_scripts(gap, repo_root, manifest)

    technique_page = None
    technique_page_path = None
    if gap.suggested_tool:
        rel = f"docs/wiki/techniques/{gap.suggested_tool}.md"
        tp = repo_root / rel
        if tp.is_file():
            technique_page_path = rel
            technique_page = _head(tp.read_text(), MAX_TECHNIQUE_CHARS)

    open_questions: list[tuple[str, str]] = []
    for q in gap.open_questions:
        qpath = Path(q)
        abspath = qpath if qpath.is_absolute() else repo_root / qpath
        if not abspath.is_file():
            continue
        rel = str(qpath if not qpath.is_absolute() else abspath.relative_to(repo_root))
        open_questions.append((rel, _head(abspath.read_text(), MAX_QUESTION_CHARS)))

    return CodeEditContext(
        gap_canonical=gap.canonical,
        suggested_tool=gap.suggested_tool,
        py_identifier=py_id,
        example_scripts=examples,
        technique_page_path=technique_page_path,
        technique_page=technique_page,
        open_questions=open_questions,
    )


__all__ = [
    "CodeEditContext",
    "ExampleScript",
    "gather_context",
]
