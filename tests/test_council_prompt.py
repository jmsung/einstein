"""Tests for council.prompt.build_enriched_prompt (Goal 3 of js/feat/research-synthesis).

Build verifies the persona-prompt enrichment with qmd hits while preserving
the questions-not-solutions invariant from .claude/rules/council-dispatch.md.
"""

from __future__ import annotations

import textwrap

from einstein.council import Persona
from einstein.council.prompt import build_enriched_prompt
from einstein.research_synthesis.query import RunnerResult
from einstein.research_synthesis.schema import Hit


def _viazovska() -> Persona:
    return Persona(
        name="Viazovska",
        perspective="Sphere packing optimality proofs",
        tier="bench",
        expertise="E8, Leech magic functions",
        prompt_seed="Viazovska-style optimality proof?",
        literature="Viazovska 2016",
        example_insight="P6 LP gap",
        trigger_categories=frozenset({"sphere_packing", "kissing_number"}),
    )


def _gauss() -> Persona:
    return Persona(
        name="Gauss",
        perspective="Number theory, algebraic constructions",
        tier="core",
        expertise="CRT, character sums",
        prompt_seed="Approach as algebraic construction.",
        literature="Ireland-Rosen",
        example_insight="P7 LP over squarefree integers.",
        trigger_categories=frozenset(),
    )


def _hit(path: str, score: float = 0.8, snippet: str = "snippet") -> Hit:
    return Hit(path=path, score=score, snippet=snippet, collection="einstein-wiki-source")


def test_includes_persona_fields() -> None:
    p = _viazovska()
    out = build_enriched_prompt(p, problem_id=6, problem_category="sphere_packing", hits=[])
    assert "Viazovska" in out
    assert "Sphere packing optimality proofs" in out
    assert "E8, Leech magic functions" in out
    assert "Viazovska-style optimality proof?" in out
    assert "Viazovska 2016" in out
    assert "P6 LP gap" in out


def test_with_provided_hits_lists_them() -> None:
    hits = [
        _hit("knowledge/source/2016-viazovska-sphere-packing-d8.md", 0.92, "magic function for E8"),
        _hit("knowledge/source/2017-cohn-viazovska-leech-24.md", 0.88, "Leech lattice density"),
        _hit("knowledge/source/2024-cohn-formal-d8-verification.md", 0.81, "formal verification of d=8"),
    ]
    out = build_enriched_prompt(
        _viazovska(), problem_id=6, problem_category="sphere_packing", hits=hits
    )
    assert "2016-viazovska-sphere-packing-d8.md" in out
    assert "2017-cohn-viazovska-leech-24.md" in out
    assert "2024-cohn-formal-d8-verification.md" in out
    assert "magic function for E8" in out


def test_bench_query_uses_trigger_categories_not_unrelated() -> None:
    """Viazovska on sphere_packing → query mentions sphere_packing, not autocorrelation."""
    seen_cmds: list[list[str]] = []

    def runner(cmd, env):
        seen_cmds.append(list(cmd))
        return RunnerResult(returncode=0, stdout="")

    build_enriched_prompt(
        _viazovska(),
        problem_id=6,
        problem_category="sphere_packing",
        qmd_runner=runner,
    )
    assert seen_cmds, "expected at least one qmd query call"
    flat = " ".join(" ".join(c) for c in seen_cmds)
    # Must include the trigger categories
    assert "sphere_packing" in flat or "sphere packing" in flat
    # Must NOT include an unrelated trigger
    assert "autocorrelation" not in flat


def test_core_query_uses_problem_category_when_no_triggers() -> None:
    """Gauss (core, empty triggers) → query falls back to problem_category arg."""
    seen_cmds: list[list[str]] = []

    def runner(cmd, env):
        seen_cmds.append(list(cmd))
        return RunnerResult(returncode=0, stdout="")

    build_enriched_prompt(
        _gauss(),
        problem_id=7,
        problem_category="sieve",
        qmd_runner=runner,
    )
    flat = " ".join(" ".join(c) for c in seen_cmds)
    assert "sieve" in flat


def test_empty_hits_still_well_formed() -> None:
    out = build_enriched_prompt(
        _viazovska(), problem_id=6, problem_category="sphere_packing", hits=[]
    )
    assert "Relevant ingested literature" in out
    assert "(no relevant hits)" in out
    # Still asks for questions
    assert "questions" in out.lower()


def test_includes_questions_not_solutions_instruction() -> None:
    out = build_enriched_prompt(_viazovska(), 6, "sphere_packing", hits=[])
    low = out.lower()
    # Must instruct: questions, with cited paths, falsifiable, in persona's voice
    assert "questions, not solutions" in low or "not solutions" in low
    assert "cite" in low
    # And no anti-pattern wording
    assert "implement the solution" not in low
    assert "write the code" not in low


def test_n_hits_cap_respected() -> None:
    """qmd_runner returns 10 hits, n_hits=3 → only 3 listed in output."""
    stdout = ""
    for i in range(10):
        stdout += textwrap.dedent(f"""\
            qmd://einstein-wiki-source/source-{i:02d}.md #{i:06x}
            Title: Source {i}
            Score:  {90 - i}%

            @@ -1,1 @@ (0 before, 1 after)
            body {i}


        """)

    def runner(cmd, env):
        return RunnerResult(returncode=0, stdout=stdout)

    out = build_enriched_prompt(_viazovska(), 6, "sphere_packing", qmd_runner=runner, n_hits=3)
    # Top 3 by score should be source-00, source-01, source-02
    assert "source-00.md" in out
    assert "source-01.md" in out
    assert "source-02.md" in out
    # source-09 (lowest score) must NOT be present
    assert "source-09.md" not in out


def test_runner_failure_is_graceful() -> None:
    """A runner that raises is caught; prompt still produced with empty-hits block."""

    def runner(cmd, env):
        raise RuntimeError("qmd not on PATH")

    out = build_enriched_prompt(_viazovska(), 6, "sphere_packing", qmd_runner=runner)
    assert "(no relevant hits)" in out
    # No traceback bled into the prompt
    assert "Traceback" not in out
    assert "RuntimeError" not in out


def test_prompt_cites_problem_id_and_category() -> None:
    out = build_enriched_prompt(_gauss(), problem_id=7, problem_category="sieve", hits=[])
    assert "P7" in out
    assert "sieve" in out
