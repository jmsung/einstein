#!/usr/bin/env python3
"""llm_distill.py — Claude Code-headless distillation of extracted papers.

The wiki contract says `knowledge/source/*.md` should hold LLM-distilled summaries,
not raw extractions. This module shells out to `claude -p` (Claude Code's
headless mode) per paper to produce a Karpathy-llm-wiki-style structured
summary: title, one-line, key claim, method, why-it-matters, connections,
key terms.

Uses the user's Claude Code subscription — no API key required, no
per-paper $/token charge.

Each `claude -p` invocation:
  - cold start ~3-5 sec
  - Haiku generation ~2-5 sec per paper
  - Total ~5-10 sec/paper, parallelizable across CPUs via concurrent.futures.

For batch use: invoked from `seed_ingest.apply()` between PDF→md extraction
and source/ write. Also a standalone CLI for retroactively distilling
oversized source/ entries.

Usage:
    uv run python docs/tools/llm_distill.py --input extracted.md --slug 2024-foo
    uv run python docs/tools/llm_distill.py --shrink knowledge/source/2007-saliola.md
"""

from __future__ import annotations

import argparse
import concurrent.futures
import logging
import re
import sys
from pathlib import Path

# claude_headless lives alongside this module under docs/tools/.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import claude_headless  # noqa: E402

log = logging.getLogger("llm_distill")

# Hard cap on body chars handed to claude -p — keeps the prompt within a single
# invocation's reasonable size. Papers larger than this get a head + tail
# excerpt (intro + conclusion are usually the highest-signal parts).
_BODY_CHAR_LIMIT = 60_000


class DistillError(RuntimeError):
    """Raised when a claude -p invocation fails."""


# ---------------- prompt ----------------

# Karpathy llm-wiki style: short, fielded, opinionated. Output is markdown
# with stable section headers so qmd can chunk on them.
_PROMPT_TEMPLATE = """\
You are an expert mathematician summarizing a research paper for a wiki
indexed by vector search. The wiki feeds an autonomous-loop agent solving
Einstein Arena problems (sphere packing, autocorrelation inequalities,
discrete combinatorics, extremal graph theory, kissing numbers, sieve
theory, functional inequalities).

Given the extracted text of a paper, produce a concise distillation
following EXACTLY this structure (Markdown). Be specific, no padding.
Keep math notation ($...$). If a field can't be determined, write "—".

----- PAPER METADATA -----
Title: {title}
Authors: {authors}
Year: {year}
Source: {source_url}

----- PAPER TEXT -----
{body}

----- OUTPUT (return only the markdown below, no preamble, no code-fence) -----

# {title}

**Authors:** {authors}  ·  **Year:** {year}  ·  **Source:** {source_url}

## One-line
<single sentence: what this paper does, in plain language>

## Key claim
<the headline result, with the specific numerical bound / theorem if any>

## Method
<2-3 sentences on the technique used — LP / SDP / Lovász local lemma / Cohn-Elkies magic function / Remez exchange / etc.>

## Result
<2-3 sentences on the specific bound, theorem, or value established. Include numbers where applicable.>

## Why it matters here
<1-2 sentences anchoring this paper to the Einstein Arena agent's work — which concept(s) it informs, which problem(s) it relates to, what it adds vs prior wiki content. If unclear, write "general background; no direct arena tie".>

## Open questions / connections
<2-3 bullets on follow-up questions raised, prior work it extends, or open problems it leaves. Just bullets.>

## Key terms
<8-12 comma-separated terms for vector-search retrieval — concept names, technique names, mathematician surnames, problem keywords>
"""


def _build_prompt(*, extracted_md: str, metadata: dict) -> str:
    """Compose the full claude -p prompt with paper text + structured output schema."""
    body = extracted_md
    if len(body) > _BODY_CHAR_LIMIT:
        # Head + tail strategy: keep intro + conclusion-shaped chunks.
        head = body[: _BODY_CHAR_LIMIT // 2]
        tail = body[-_BODY_CHAR_LIMIT // 2 :]
        body = f"{head}\n\n[... middle of paper omitted for length ...]\n\n{tail}"
    return _PROMPT_TEMPLATE.format(
        title=metadata.get("title", "(no title)"),
        authors=metadata.get("authors", ""),
        year=metadata.get("year", ""),
        source_url=metadata.get("source_url", ""),
        body=body,
    )


# ---------------- one-shot distill ----------------


_FENCE_RE = re.compile(r"^```(?:markdown|md)?\s*\n(.*?)\n```\s*$", re.DOTALL)
_REQUIRED_HEADINGS = (
    "## One-line",
    "## Key claim",
    "## Method",
    "## Why it matters here",
    "## Open questions / connections",
    "## Key terms",
)


def _strip_fence(text: str) -> str:
    """If the output is wrapped in a ```markdown\n...\n``` fence, unwrap it."""
    m = _FENCE_RE.match(text.strip())
    return m.group(1) if m else text


def _validate_summary(text: str) -> None:
    """Reject malformed distill outputs (missing structural headings).

    Auth/quota detection moved to `claude_headless._is_unavailable`. This
    function now only enforces the distill-specific output schema.
    """
    missing = [heading for heading in _REQUIRED_HEADINGS if heading not in text]
    if missing:
        raise DistillError("claude output missing required headings: " + ", ".join(missing))


def distill_via_claude_code(
    *, extracted_md: str, metadata: dict, model: str = "claude-opus-4-7[1m]", timeout: int = 180
) -> str:
    """Distill one paper via `claude -p`. Returns the markdown summary."""
    prompt = _build_prompt(extracted_md=extracted_md, metadata=metadata)
    result = claude_headless.run(
        prompt,
        model=model,
        timeout_seconds=timeout,
    )
    if not result.ok:
        if result.error_kind == "unavailable":
            raise DistillError("Claude Code unavailable: auth/session-limit response")
        raise DistillError(result.error_message)
    summary = _strip_fence(result.stdout).strip()
    _validate_summary(summary)
    return summary + "\n"


# ---------------- batch ----------------


def distill_batch(
    items: list[dict],
    *,
    model: str = "claude-opus-4-7[1m]",
    max_workers: int = 4,
    timeout: int = 180,
    delay_seconds: float = 0,
) -> list[dict]:
    """Distill N papers concurrently. Each item: {slug, extracted_md, metadata}.

    Returns a list of {slug, ok, summary | error} dicts in the same order
    as `items`. Failures are isolated — one bad paper doesn't sink the batch.

    `delay_seconds` introduces a sleep BEFORE each task submission, throttling
    the rate of Claude Code calls to avoid burning the session-token budget too
    fast. With max_workers=1 + delay=180, runs one paper every ~3 minutes.
    """
    import time as _time

    results: list[dict | None] = [None] * len(items)

    def _one(idx: int, item: dict) -> tuple[int, dict]:
        try:
            summary = distill_via_claude_code(
                extracted_md=item["extracted_md"],
                metadata=item["metadata"],
                model=model,
                timeout=timeout,
            )
            return (idx, {"slug": item["slug"], "ok": True, "summary": summary})
        except Exception as e:
            return (idx, {"slug": item["slug"], "ok": False, "error": str(e)})

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = []
        for i, item in enumerate(items):
            if i > 0 and delay_seconds > 0:
                _time.sleep(delay_seconds)
            futures.append(ex.submit(_one, i, item))
        for fut in concurrent.futures.as_completed(futures):
            idx, payload = fut.result()
            results[idx] = payload

    return [r for r in results if r is not None]


# ---------------- retroactive shrink ----------------


_FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip("\"'")
    return fm, text[m.end() :]


def shrink_source_entry(
    path: Path,
    *,
    model: str = "claude-opus-4-7[1m]",
    timeout: int = 180,
    min_size_bytes: int = 8000,
) -> bool:
    """Replace the body of a source/<slug>.md with an LLM-distilled summary.

    Skipped if the file is already small (< min_size_bytes — already
    distilled by an earlier /wiki-ingest pass). Avoids burning Opus
    calls on entries that don't need re-curation.

    Returns True if the file was rewritten; False if it had no frontmatter,
    was already small, or the new summary isn't materially smaller.
    """
    if path.stat().st_size < min_size_bytes:
        log.info("skip %s — already small (%d bytes)", path.name, path.stat().st_size)
        return False
    text = path.read_text()
    fm, body = _parse_frontmatter(text)
    if not fm:
        log.warning("no frontmatter — skipping %s", path.name)
        return False

    try:
        summary = distill_via_claude_code(
            extracted_md=body, metadata=fm, model=model, timeout=timeout
        )
    except DistillError as e:
        log.error("distill failed for %s: %s", path.name, e)
        return False

    # Recompose: keep original frontmatter, replace body with summary
    new_text = "---\n"
    for k, v in fm.items():
        new_text += f"{k}: {v}\n"
    new_text += "---\n\n" + summary

    if len(new_text) >= len(text) * 0.85:
        return False
    path.write_text(new_text)
    return True


# ---------------- CLI ----------------


def main(argv: list[str] | None = None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--input", type=Path, help="Path to an extracted markdown file to distill.")
    g.add_argument("--shrink", type=Path, help="Shrink one knowledge/source/<slug>.md in place.")
    g.add_argument("--shrink-all", type=Path, help="Shrink every *.md in the given directory.")
    p.add_argument(
        "--slug", type=str, help="Filename stem for --input output (required with --input)."
    )
    p.add_argument(
        "--out-dir",
        type=Path,
        default=Path("knowledge/source"),
        help="Destination dir for --input mode.",
    )
    p.add_argument(
        "--model",
        default="claude-opus-4-7[1m]",
        help="claude -p --model. Default: claude-opus-4-7[1m] "
        "(Opus 4.7 with 1M context — highest quality + "
        "handles long papers). One-time-per-paper distill, "
        "so quality > speed.",
    )
    p.add_argument(
        "--workers", type=int, default=4, help="Parallel workers for --shrink-all (default 4)."
    )
    args = p.parse_args(argv)

    if args.input:
        if not args.slug:
            p.error("--slug required with --input")
        text = args.input.read_text()
        fm, body = _parse_frontmatter(text)
        if not fm:
            log.error("no frontmatter on %s", args.input)
            return 1
        summary = distill_via_claude_code(
            extracted_md=body,
            metadata=fm,
            model=args.model,
        )
        out = args.out_dir / f"{args.slug}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        new_text = "---\n" + "".join(f"{k}: {v}\n" for k, v in fm.items()) + "---\n\n" + summary
        out.write_text(new_text)
        log.info("wrote %s", out)
        return 0

    if args.shrink:
        ok = shrink_source_entry(args.shrink, model=args.model)
        log.info("%s %s", "shrunk" if ok else "no-op", args.shrink)
        return 0

    targets = sorted(
        [t for t in args.shrink_all.glob("*.md") if t.name not in ("INDEX.md", "README.md")]
    )
    log.info(
        "shrinking %d files with %d workers (model %s)", len(targets), args.workers, args.model
    )
    total_before = sum(t.stat().st_size for t in targets)

    def _one(t: Path) -> tuple[Path, bool]:
        return (t, shrink_source_entry(t, model=args.model))

    n_shrunk = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for t, ok in ex.map(_one, targets):
            if ok:
                n_shrunk += 1
                log.info("✓ %s", t.name)
            else:
                log.info("·  %s (no-op)", t.name)

    total_after = sum(t.stat().st_size for t in targets)
    log.info(
        "shrunk %d/%d entries; %d → %d KB (%.1f%% reduction)",
        n_shrunk,
        len(targets),
        total_before // 1024,
        total_after // 1024,
        100 * (1 - total_after / max(total_before, 1)),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
