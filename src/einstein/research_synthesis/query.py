"""qmd subprocess wrapper for the synthesis step.

Parses `qmd query` / `qmd vsearch` output into typed `Hit` objects. Hides the
subprocess machinery behind a `runner` callable so tests don't shell out.
"""

from __future__ import annotations

import logging
import os
import re
import shutil
import subprocess
from collections.abc import Callable
from dataclasses import dataclass

from einstein.research_synthesis.schema import Hit

log = logging.getLogger("research_synthesis.query")


@dataclass
class RunnerResult:
    """Subprocess result shape used by the injectable runner."""

    returncode: int
    stdout: str = ""
    stderr: str = ""


Runner = Callable[[list[str], dict[str, str]], RunnerResult]


def _default_runner(cmd: list[str], env: dict[str, str]) -> RunnerResult:
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=60)
    return RunnerResult(
        returncode=proc.returncode, stdout=proc.stdout or "", stderr=proc.stderr or ""
    )


# qmd result block looks like:
#   qmd://<collection>/<path>:<line> #<hash>
#   Title: <title>
#   Score:  <pct>%
#   <blank>
#   @@ -<a>,<b> @@ (<x> before, <y> after)
#   <snippet lines>
#   <blank>
#   <blank>
# Multiple blocks separated by blank lines.

_QMD_PREFIX = re.compile(r"^qmd://(?P<collection>[^/]+)/(?P<path>[^\s:]+)(:\d+)?\s+#[0-9a-f]+\s*$")
_SCORE_LINE = re.compile(r"^Score:\s+(?P<pct>\d+)%\s*$")
_SNIPPET_HEADER = re.compile(r"^@@ ")


def parse_qmd_output(text: str, default_collection: str = "") -> list[Hit]:
    """Parse `qmd query` / `qmd vsearch` plain stdout into a list of `Hit`.

    Robust to extra leading lines (warnings, qmd preamble) and missing snippets.
    Returns an empty list if no blocks parse.
    """
    hits: list[Hit] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = _QMD_PREFIX.match(lines[i])
        if not m:
            i += 1
            continue
        path = m.group("path")
        collection = m.group("collection") or default_collection
        score_pct = 0
        snippet_parts: list[str] = []
        # Scan forward to the next blank-blank boundary (or next prefix)
        j = i + 1
        while j < len(lines):
            line = lines[j]
            if _QMD_PREFIX.match(line):
                break
            sm = _SCORE_LINE.match(line)
            if sm:
                score_pct = int(sm.group("pct"))
            elif _SNIPPET_HEADER.match(line):
                # Snippet header — capture following non-empty lines until blank-blank
                k = j + 1
                while k < len(lines) and lines[k].strip() != "":
                    snippet_parts.append(lines[k].strip())
                    k += 1
                j = k
                continue
            j += 1
        snippet = " ".join(snippet_parts)[:240]  # cap for readability
        hits.append(
            Hit(
                path=path,
                score=score_pct / 100.0,
                snippet=snippet,
                collection=collection,
            )
        )
        i = j
    return hits


def query_qmd(
    text: str,
    *,
    collection: str,
    n: int = 5,
    qmd_bin: str = "qmd",
    runner: Runner | None = None,
    env: dict[str, str] | None = None,
) -> list[Hit]:
    """Run `qmd query <text> -c <collection> -n <n>` and parse hits.

    Sets `QMD_FORCE_CPU=1` in the environment to avoid the Darwin Metal
    finalizer SIGABRT (see docs/wiki/findings/qmd-metal-embed-fix.md).
    """
    runner_fn: Runner = runner or _default_runner
    if runner is None and shutil.which(qmd_bin) is None:
        log.warning("qmd binary %r not on PATH; returning empty hits", qmd_bin)
        return []
    merged_env = dict(os.environ)
    merged_env["QMD_FORCE_CPU"] = "1"
    if env:
        merged_env.update(env)
    cmd = [qmd_bin, "query", text, "-c", collection, "-n", str(n)]
    result = runner_fn(cmd, merged_env)
    if result.returncode != 0:
        log.warning("qmd query failed (rc=%s): %s", result.returncode, (result.stderr or "")[-200:])
        return []
    return parse_qmd_output(result.stdout, default_collection=collection)


def gather(
    queries: list[str],
    *,
    source_collection: str = "einstein-wiki-source",
    wiki_collection: str = "einstein-wiki",
    n_per_query: int = 10,
    top_k_source: int = 50,
    top_k_wiki: int = 20,
    runner: Runner | None = None,
    qmd_bin: str = "qmd",
) -> tuple[list[Hit], list[Hit]]:
    """Run multiple queries against both collections; dedupe by path; top-K each.

    Returns ``(source_hits, wiki_hits)`` sorted descending by score.
    """
    source_by_path: dict[str, Hit] = {}
    wiki_by_path: dict[str, Hit] = {}
    for q in queries:
        for h in query_qmd(
            q, collection=source_collection, n=n_per_query, runner=runner, qmd_bin=qmd_bin
        ):
            prior = source_by_path.get(h.path)
            if prior is None or h.score > prior.score:
                source_by_path[h.path] = h
        for h in query_qmd(
            q, collection=wiki_collection, n=n_per_query, runner=runner, qmd_bin=qmd_bin
        ):
            prior = wiki_by_path.get(h.path)
            if prior is None or h.score > prior.score:
                wiki_by_path[h.path] = h
    source_hits = sorted(source_by_path.values(), key=lambda h: h.score, reverse=True)[
        :top_k_source
    ]
    wiki_hits = sorted(wiki_by_path.values(), key=lambda h: h.score, reverse=True)[:top_k_wiki]
    return source_hits, wiki_hits
