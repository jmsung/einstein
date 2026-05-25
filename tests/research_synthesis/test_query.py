"""Tests for the qmd subprocess wrapper + gather()."""

from __future__ import annotations

import textwrap

import pytest

from einstein.research_synthesis import query as Q
from einstein.research_synthesis.query import RunnerResult

# A real-shape stdout block captured from `qmd query "X" -c einstein-wiki-source -n 2`
FIXTURE_QMD_STDOUT = textwrap.dedent("""\
    qmd://einstein-wiki-source/2026-lee-meta-harness-end-to-end-optimization-model.md:4 #b84ed0
    Title: Meta-Harness: End-to-End Optimization of Model Harnesses
    Score:  88%

    @@ -3,4 @@ (2 before, 37 after)
    kind: paper
    title: Meta-Harness
    authors: Yoonho Lee et al
    year: 2026


    qmd://einstein-wiki-source/2024-baek-researchagent-iterative-research-idea.md #b30a33
    Title: ResearchAgent
    Score:  92%

    @@ -3,4 @@ (2 before, 34 after)
    kind: paper
    title: ResearchAgent
    authors: Baek et al
    year: 2024


""")


def _stub_runner(stdout: str = "", stderr: str = "", returncode: int = 0):
    """Build a stub runner that returns the given fixture regardless of cmd."""

    def runner(cmd, env):
        return RunnerResult(returncode=returncode, stdout=stdout, stderr=stderr)

    return runner


def test_parse_qmd_output_parses_two_hits() -> None:
    hits = Q.parse_qmd_output(FIXTURE_QMD_STDOUT)
    assert len(hits) == 2
    paths = [h.path for h in hits]
    assert "2026-lee-meta-harness-end-to-end-optimization-model.md" in paths
    assert "2024-baek-researchagent-iterative-research-idea.md" in paths
    by_path = {h.path: h for h in hits}
    assert by_path["2026-lee-meta-harness-end-to-end-optimization-model.md"].score == 0.88
    assert by_path["2024-baek-researchagent-iterative-research-idea.md"].score == 0.92
    # Collection extracted from prefix
    assert all(h.collection == "einstein-wiki-source" for h in hits)
    # Snippet has body content
    assert (
        "Meta-Harness" in by_path["2026-lee-meta-harness-end-to-end-optimization-model.md"].snippet
    )


def test_parse_qmd_output_empty_returns_empty() -> None:
    assert Q.parse_qmd_output("") == []
    assert Q.parse_qmd_output("just stderr noise\nno blocks here") == []


def test_query_qmd_happy_path() -> None:
    runner = _stub_runner(stdout=FIXTURE_QMD_STDOUT)
    hits = Q.query_qmd("anything", collection="einstein-wiki-source", n=5, runner=runner)
    assert len(hits) == 2


def test_query_qmd_nonzero_returns_empty(caplog) -> None:
    runner = _stub_runner(stdout="", stderr="qmd: collection not found", returncode=2)
    hits = Q.query_qmd("X", collection="nonexistent", runner=runner)
    assert hits == []


def test_query_qmd_sets_force_cpu_env() -> None:
    seen_env: dict = {}

    def capturing_runner(cmd, env):
        seen_env.update(env)
        return RunnerResult(returncode=0, stdout="")

    Q.query_qmd("X", collection="einstein-wiki", runner=capturing_runner)
    assert seen_env.get("QMD_FORCE_CPU") == "1"


def test_gather_dedupes_by_path_keeping_highest_score() -> None:
    """Same path returned twice → keep the higher score."""
    # First query returns the hit with score 50%
    stdout_low = textwrap.dedent("""\
        qmd://einstein-wiki-source/A.md #aaaaaa
        Title: A
        Score:  50%

        @@ -1,1 @@ (0 before, 1 after)
        body A1

    """)
    # Second query returns the same path with score 90%
    stdout_high = textwrap.dedent("""\
        qmd://einstein-wiki-source/A.md #aaaaaa
        Title: A
        Score:  90%

        @@ -1,1 @@ (0 before, 1 after)
        body A2

    """)
    call_count = {"n": 0}

    def runner(cmd, env):
        # First two calls are source-collection (queries[0]+wiki), then queries[1]
        call_count["n"] += 1
        # Even calls hit source, odd calls hit wiki (per gather() order)
        if "einstein-wiki-source" in cmd:
            return RunnerResult(
                returncode=0,
                stdout=stdout_low if call_count["n"] == 1 else stdout_high,
            )
        return RunnerResult(returncode=0, stdout="")

    src, wiki = Q.gather(
        ["q1", "q2"],
        n_per_query=5,
        top_k_source=10,
        top_k_wiki=10,
        runner=runner,
    )
    # Deduped to 1 hit; kept the higher score
    assert len(src) == 1
    assert src[0].score == pytest.approx(0.90)


def test_gather_sorts_by_score_descending() -> None:
    stdout = textwrap.dedent("""\
        qmd://einstein-wiki-source/A.md #aaaaaa
        Title: A
        Score:  40%

        @@ -1,1 @@ (0 before, 1 after)
        body


        qmd://einstein-wiki-source/B.md #bbbbbb
        Title: B
        Score:  80%

        @@ -1,1 @@ (0 before, 1 after)
        body


        qmd://einstein-wiki-source/C.md #cccccc
        Title: C
        Score:  60%

        @@ -1,1 @@ (0 before, 1 after)
        body

    """)

    def runner(cmd, env):
        if "einstein-wiki-source" in cmd:
            return RunnerResult(returncode=0, stdout=stdout)
        return RunnerResult(returncode=0, stdout="")

    src, _ = Q.gather(["q"], runner=runner)
    assert [h.path for h in src] == ["B.md", "C.md", "A.md"]


def test_gather_top_k_respected() -> None:
    blocks = []
    hashes = ["aaaaaa", "bbbbbb", "cccccc", "dddddd", "eeeeee"]
    for (letter, pct), h in zip(
        [("A", 40), ("B", 80), ("C", 60), ("D", 30), ("E", 90)], hashes, strict=True
    ):
        blocks.append(
            textwrap.dedent(f"""\
                qmd://einstein-wiki-source/{letter}.md #{h}
                Title: {letter}
                Score:  {pct}%

                @@ -1,1 @@ (0 before, 1 after)
                body {letter}

            """)
        )

    def runner(cmd, env):
        if "einstein-wiki-source" in cmd:
            return RunnerResult(returncode=0, stdout="\n".join(blocks))
        return RunnerResult(returncode=0, stdout="")

    src, _ = Q.gather(["q"], top_k_source=2, runner=runner)
    assert [h.path for h in src] == ["E.md", "B.md"]
