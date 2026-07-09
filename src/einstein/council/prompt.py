"""Citation-enriched council prompt builder.

Extends the demo prompt in scripts/council_demo.py with a "Relevant ingested
literature" block populated by qmd hits matching the persona's trigger
categories (or the problem category if the persona has no triggers). The
question-not-solution rule from .claude/rules/council-dispatch.md is enforced
in the task block, and each question is required to cite ≥1 specific path.

Anchored in knowledge/wiki/findings/research-synthesis-design.md Patterns C
(citation provenance as signal) and D (pre-cycle synthesis as distinct step).
"""

from __future__ import annotations

import logging
from collections.abc import Callable

from einstein.council.personas import Persona
from einstein.research_synthesis.query import query_qmd
from einstein.research_synthesis.schema import Hit

log = logging.getLogger("council.prompt")


def _hits_query(persona: Persona, problem_category: str) -> str:
    """Choose the qmd query text for this persona on this problem.

    Bench personas have trigger_categories; query those + persona expertise.
    Core personas (empty triggers) fall back to the problem_category arg.
    """
    if persona.trigger_categories:
        cats = " ".join(sorted(persona.trigger_categories))
        return f"{cats} {persona.expertise}"
    return f"{problem_category} {persona.expertise}"


def _fetch_hits(
    persona: Persona,
    problem_category: str,
    *,
    qmd_runner: Callable | None,
    n_hits: int,
    collection: str,
) -> list[Hit]:
    """Run a single qmd query for this persona; return empty on any error."""
    query = _hits_query(persona, problem_category)
    try:
        return query_qmd(
            query,
            collection=collection,
            n=n_hits,
            runner=qmd_runner,
        )
    except Exception as e:  # noqa: BLE001 — graceful degradation by design
        log.warning("council.prompt: qmd query failed (%s); proceeding without hits", e)
        return []


def _format_hits(hits: list[Hit], n_hits: int) -> str:
    if not hits:
        return "(no relevant hits)"
    lines: list[str] = []
    for h in hits[:n_hits]:
        pct = int(round(h.score * 100))
        lines.append(f"- [{pct}%] {h.path} — {h.snippet}")
    return "\n".join(lines)


def build_enriched_prompt(
    persona: Persona,
    problem_id: int,
    problem_category: str,
    *,
    hits: list[Hit] | None = None,
    qmd_runner: Callable | None = None,
    n_hits: int = 5,
    collection: str = "einstein-wiki-source",
) -> str:
    """Persona prompt enriched with top-k qmd hits + question-not-solution task block.

    Either pre-gather ``hits`` and pass them in (for batch dispatch with cached
    queries) or pass a ``qmd_runner`` and let the function call qmd internally.
    On qmd error the function degrades gracefully — the prompt is still
    well-formed, just with ``(no relevant hits)`` in the literature block.
    """
    if hits is None:
        hits = _fetch_hits(
            persona,
            problem_category,
            qmd_runner=qmd_runner,
            n_hits=n_hits,
            collection=collection,
        )
    lit_block = _format_hits(hits, n_hits)
    return (
        f"You are channelling {persona.name} ({persona.perspective}).\n"
        "\n"
        f"Problem P{problem_id} (category: {problem_category}).\n"
        "\n"
        f"Real expertise: {persona.expertise}\n"
        f"Approach: {persona.prompt_seed}\n"
        f"Recommended literature: {persona.literature}\n"
        f"Worked example: {persona.example_insight}\n"
        "\n"
        "## Relevant ingested literature\n"
        "\n"
        f"Query: {_hits_query(persona, problem_category)}\n"
        "\n"
        f"{lit_block}\n"
        "\n"
        "## Task — questions, not solutions\n"
        "\n"
        "Write 2–3 questions in your characteristic perspective. Each question MUST:\n"
        "\n"
        "1. Cite at least one specific path from the literature above\n"
        "   (or explicitly note the absence if no relevant hit exists).\n"
        "2. Name an unknown precisely (falsifiable answer — you would recognize\n"
        "   the right answer if you saw it).\n"
        "3. Not presuppose its conclusion.\n"
        "\n"
        "Do NOT propose solutions, code, or methods. Questions only. Per\n"
        f".claude/rules/council-dispatch.md, {persona.name}'s contribution\n"
        "is the question Tao-style framing — not a guess at the answer.\n"
        "\n"
        "Output format: numbered questions only. No preamble.\n"
    )
