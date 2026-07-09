"""meta_loop.tool_gaps — Goal 1 detector for recurring tool gaps.

Scans `docs/agent/cycle-log.md` notes for the canonical markers that show up
when the inner agent could have dispatched but couldn't, then clusters them
into `ToolGap` records keyed by *suggested tool slug* (preferred) or
*marker pattern* (fallback). Joined with open `knowledge/wiki/questions/*.md`
tagged `tool-gap` so a long-running question can also seed a gap.

Read-only; mirrors the shape of `diagnose.py`. The downstream proposer
(Goal 2) reads these records and decides whether to draft a
`scripts/proposed/<tool>.py`.

Threshold: ≥3 cycles AND ≥2 distinct problem ids (rationale in
`knowledge/wiki/findings/tool-autosynthesis-design.md`). The ≥2 distinct
problems constraint is what prevents one-stuck-problem from masquerading
as recurrence.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from . import diagnose

# ---------------- patterns ----------------

# `P{id}-...` or `P{id} ...` — pull the leading problem id token.
_PROBLEM_ID_RE = re.compile(r"^(P\d+)\b")

# A slug looks like `kebab-case-words`. Match conservatively: 2+ words joined
# by `-`, lowercased, ≥1 letter each segment. Excludes single bare words
# like "newton_max" (those are existing manifest entries we DON'T treat as
# suggested tools — they're the *gap*, not the proposed fill).
_SLUG_RE = re.compile(r"\b([a-z][a-z0-9]+(?:-[a-z0-9]+){1,4})\b")

# The phrases that anchor a "novel tool name in flight, manifest doesn't
# wire it" signal. Each phrase tells us the slug appeared somewhere LEFT
# of the phrase; we walk back through the preceding ~60 chars to find the
# closest slug-shaped token.
_WIRING_PHRASES = (
    "not yet wired",
    "picked novel but unwired",
)

# Slug shape: kebab-case, ≥2 segments, ≥1 alphanumeric char each.
_SLUG_TOKEN_RE = re.compile(r"\b([a-z][a-z0-9]+(?:-[a-z0-9]+){1,4})\b")

# Slugs that look kebab-cased but are state descriptions, not tool names.
_NON_TOOL_SLUGS = {
    "strict-tol-failing",
    "strict-tol-unsafe",
    "strict-tol-trap",
    "tol-failing",
    "no-manifest-entry",
    "manifest-only",
    "manifest-blocker",
    "manifest-wire-fix",
    "manifest-wiring",
    "rank-2-frozen",
    "rank-3-frozen",
    "float64-ceiling",
    "float64-ceiling-locked",
    "no-execute-structural-converged-manifest-blocker",
    "file-missing-artifacts-from-cycles-49-50-no-dispatch",
    "no-attempt-problem-closed",
    "council-needed",
    "per-exp-log",
    "exp-log",
}

# Markers that don't extract a tool slug — bucketed by pattern.
_MARKER_PATTERNS: dict[str, re.Pattern[str]] = {
    "dispatch_failed": re.compile(r"\bdispatch-failed\b", re.IGNORECASE),
    "no_manifest_entry": re.compile(r"dispatch:\s*no-manifest-entry", re.IGNORECASE),
    "no_library_match": re.compile(r"no library matches\s*—\s*council needed", re.IGNORECASE),
    "manifest_gap": re.compile(r"manifest only exposes\b", re.IGNORECASE),
}

# These markers all reflect the same root cause (no script reachable from
# the manifest). When they coexist without an extractable tool slug, the
# clusterer merges them into a single "manifest_or_dispatch_gap" cluster so
# 1+1+1 across distinct problems passes the threshold.
_FUNGIBLE_MARKERS = {"dispatch_failed", "no_manifest_entry", "no_library_match"}
_FUNGIBLE_CLUSTER_KEY = "manifest_or_dispatch_gap"


# ---------------- signals ----------------


@dataclass(frozen=True)
class _Signal:
    """One extracted-from-one-row tool-gap signal. Internal."""

    cycle_id: int
    problem_id: str
    pattern: str
    suggested_tool: str | None
    missing_manifest_entry: str | None


def _problem_id(raw: str) -> str | None:
    m = _PROBLEM_ID_RE.match(raw.strip())
    return m.group(1) if m else None


def _extract_suggested_tool(notes: str) -> str | None:
    """Pull the suggested tool slug out of the notes column, if any.

    Anchors on a `_WIRING_PHRASES` occurrence and walks LEFT through the
    preceding ~60 chars to find the closest slug-shaped token that isn't in
    `_NON_TOOL_SLUGS`. Returns None if no plausible slug is in flight.
    """
    low = notes.lower()
    for phrase in _WIRING_PHRASES:
        idx = low.find(phrase)
        while idx != -1:
            window_start = max(0, idx - 80)
            window = notes[window_start:idx]
            # Find ALL slug tokens in the window; prefer the rightmost
            # (closest to the wiring phrase).
            tokens = _SLUG_TOKEN_RE.findall(window)
            for tok in reversed(tokens):
                slug = tok.lower()
                if slug in _NON_TOOL_SLUGS:
                    continue
                return slug
            idx = low.find(phrase, idx + 1)
    return None


def _extract_missing_manifest_entry(notes: str) -> str | None:
    """If the notes say `manifest only exposes <X>`, pull <X>."""
    m = re.search(r"manifest only exposes\s+([a-z_][a-z0-9_]*)", notes, re.IGNORECASE)
    return m.group(1) if m else None


def _extract_signal(row: diagnose.CycleRow) -> _Signal | None:
    """Build a _Signal from a single cycle-log row, or None if no marker fires."""
    notes = row.notes or ""
    pid = _problem_id(row.problem)
    if pid is None:
        return None
    suggested = _extract_suggested_tool(notes)
    missing = _extract_missing_manifest_entry(notes)

    if suggested is not None:
        # The "not yet wired" / "picked novel but unwired" construct dominates
        # any coexisting marker — it's the most informative.
        return _Signal(
            cycle_id=row.cycle_id,
            problem_id=pid,
            pattern="manifest_gap",
            suggested_tool=suggested,
            missing_manifest_entry=missing,
        )
    # Bare manifest_gap (no novel tool extracted) is rare but possible
    if missing is not None:
        return _Signal(
            cycle_id=row.cycle_id,
            problem_id=pid,
            pattern="manifest_gap",
            suggested_tool=None,
            missing_manifest_entry=missing,
        )
    # Otherwise check the marker patterns
    for pat_name, pat_re in _MARKER_PATTERNS.items():
        if pat_re.search(notes):
            return _Signal(
                cycle_id=row.cycle_id,
                problem_id=pid,
                pattern=pat_name,
                suggested_tool=None,
                missing_manifest_entry=None,
            )
    return None


# ---------------- gaps ----------------


@dataclass(frozen=True)
class ToolGap:
    """One clustered tool gap — the unit the proposer reads."""

    canonical: str
    pattern: str
    suggested_tool: str | None
    missing_manifest_entry: str | None
    citing_cycles: list[int] = field(default_factory=list)
    problem_ids: list[str] = field(default_factory=list)
    open_questions: list[Path] = field(default_factory=list)

    @property
    def cycle_count(self) -> int:
        return len(self.citing_cycles)

    @property
    def problem_count(self) -> int:
        return len(set(self.problem_ids))

    def meets_threshold(self, *, min_cycles: int = 3, min_problems: int = 2) -> bool:
        return self.cycle_count >= min_cycles and self.problem_count >= min_problems


def _canonical_for(signal: _Signal) -> str:
    if signal.suggested_tool:
        return f"manifest_gap:{signal.suggested_tool}"
    if signal.pattern in _FUNGIBLE_MARKERS:
        # Bucket fungible "you cannot dispatch" markers together so 1+1+1
        # across 3 distinct problems sums to one threshold-passing gap.
        return _FUNGIBLE_CLUSTER_KEY
    if signal.missing_manifest_entry:
        return f"manifest_gap:missing:{signal.missing_manifest_entry}"
    return f"{signal.pattern}"


# ---------------- questions ----------------


def _scan_tool_gap_questions(questions_dir: Path) -> list[Path]:
    """Open questions tagged `tool-gap` — paths only, parsing is shallow."""
    if not questions_dir.is_dir():
        return []
    out: list[Path] = []
    for p in sorted(questions_dir.glob("*.md")):
        try:
            text = p.read_text()
        except OSError:
            continue
        # Cheap frontmatter scan — look for `tool-gap` in a tags: line, and
        # status: open (or absent).
        m = re.search(r"^tags:\s*\[(.+?)\]", text, re.MULTILINE)
        if not m:
            continue
        tags = {t.strip() for t in m.group(1).split(",")}
        if "tool-gap" not in tags:
            continue
        status_m = re.search(r"^status:\s*(\w+)", text, re.MULTILINE)
        if status_m and status_m.group(1).lower() != "open":
            continue
        out.append(p)
    return out


def _link_questions_to_gaps(gaps: list[ToolGap], questions: list[Path]) -> list[ToolGap]:
    """Attach each tool-gap question to the gap whose problem_ids it mentions.

    Cheap heuristic: scan the filename for `pXX` tokens; attach to any gap
    whose problem_ids overlap. A question can attach to multiple gaps.
    Returns a new list with `open_questions` populated.
    """
    if not questions:
        return gaps
    by_qpid: dict[Path, set[str]] = {}
    for q in questions:
        # Filename like `2026-05-24-p14-strict-tol-manifest-wiring.md` →
        # extract `p14` and normalize to `P14`.
        by_qpid[q] = {f"P{p}" for p in re.findall(r"\bp(\d+)\b", q.stem.lower())}
    out: list[ToolGap] = []
    for g in gaps:
        linked = [q for q, pids in by_qpid.items() if pids & set(g.problem_ids)]
        if linked:
            out.append(
                ToolGap(
                    canonical=g.canonical,
                    pattern=g.pattern,
                    suggested_tool=g.suggested_tool,
                    missing_manifest_entry=g.missing_manifest_entry,
                    citing_cycles=g.citing_cycles,
                    problem_ids=g.problem_ids,
                    open_questions=linked,
                )
            )
        else:
            out.append(g)
    return out


# ---------------- public entry point ----------------


def detect_recurring_tool_gaps(
    cycle_log_path: Path,
    questions_dir: Path | None = None,
    *,
    min_cycles: int = 3,
    min_problems: int = 2,
) -> list[ToolGap]:
    """Parse cycle-log + optional questions dir; return threshold-passing gaps.

    Sorted by (cycle_count desc, problem_count desc). Read-only.
    """
    rows = diagnose.parse_cycle_log(cycle_log_path)
    if not rows:
        return []
    signals: list[_Signal] = [s for s in (_extract_signal(r) for r in rows) if s is not None]
    if not signals:
        return []

    by_canon: dict[str, list[_Signal]] = defaultdict(list)
    for s in signals:
        by_canon[_canonical_for(s)].append(s)

    gaps: list[ToolGap] = []
    for canon, sigs in by_canon.items():
        # Pick the representative pattern (manifest_gap if any signal has it,
        # else the most common). Suggested tool: first non-None.
        suggested = next((s.suggested_tool for s in sigs if s.suggested_tool), None)
        missing = next((s.missing_manifest_entry for s in sigs if s.missing_manifest_entry), None)
        pattern = (
            "manifest_gap" if any(s.pattern == "manifest_gap" for s in sigs) else sigs[0].pattern
        )
        # For the fungible cluster, prefer the umbrella pattern name.
        if canon == _FUNGIBLE_CLUSTER_KEY:
            pattern = _FUNGIBLE_CLUSTER_KEY
        gap = ToolGap(
            canonical=canon,
            pattern=pattern,
            suggested_tool=suggested,
            missing_manifest_entry=missing,
            citing_cycles=sorted({s.cycle_id for s in sigs}),
            problem_ids=sorted({s.problem_id for s in sigs}),
        )
        if gap.meets_threshold(min_cycles=min_cycles, min_problems=min_problems):
            gaps.append(gap)

    if questions_dir is not None:
        gaps = _link_questions_to_gaps(gaps, _scan_tool_gap_questions(questions_dir))

    gaps.sort(key=lambda g: (-g.cycle_count, -g.problem_count, g.canonical))
    return gaps


__all__ = [
    "ToolGap",
    "detect_recurring_tool_gaps",
]
