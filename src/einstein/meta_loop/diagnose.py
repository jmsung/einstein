"""meta_loop.diagnose — read-only diagnostic over cycle-log + skill-library.

The inner loop (`scripts/autonomous_loop.py`) runs *cycles*; this module reads
the artifacts those cycles leave behind and writes a structured report.

Goal 1 in `mb/active/js-feat-meta-loop.md`. Read-only by construction — no
proposals, no edits, no env mutation. Builds the substrate Goal 2's agentic
proposer feeds on.

Filesystem-as-feedback principle (MetaHarness, Lee et al. 2026):

    Raw rows + raw finding/dead-end markdown beat compressed summaries by
    ~15 pts in their ablation. This module's report is for the human and
    surfaces patterns — it does NOT replace the raw filesystem the agentic
    proposer (Goal 2) reads.

See `knowledge/wiki/findings/meta-loop-design-from-literature.md`.
"""

from __future__ import annotations

import datetime as dt
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

# ---------------- cycle-log parsing ----------------


# Match a data row in the markdown table: starts with `| <int> |` after the header.
_CYCLE_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")


@dataclass(frozen=True)
class CycleRow:
    """One row from `docs/agent/cycle-log.md`."""

    cycle_id: int
    problem: str
    score_field: str  # raw "start → end" string; parsing is lossy, keep raw
    hours: str
    compute: str
    wiki_citations: str
    findings_added: str
    concepts_added: str
    author_mix: str
    outcome: str
    notes: str

    @property
    def score_changed(self) -> bool:
        """True iff start_score and end_score appear to differ in the raw field.

        Conservative — only returns True when we can unambiguously read two
        distinct numbers separated by an arrow.
        """
        m = re.search(r"([\d.eE+\-]+)\s*→\s*([\d.eE+\-]+)", self.score_field)
        if not m:
            return False
        try:
            start = float(m.group(1))
            end = float(m.group(2))
        except ValueError:
            return False
        return start != end


def parse_cycle_log(path: Path) -> list[CycleRow]:
    """Parse the cycle-log markdown table into typed rows.

    Robust to header lines, blank lines, and trailing prose — only lines
    matching `| <int> | ...` with at least 11 pipe-separated columns count.
    """
    if not path.is_file():
        return []
    rows: list[CycleRow] = []
    for line in path.read_text().splitlines():
        if not _CYCLE_ROW_RE.match(line):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 11:
            continue
        try:
            cid = int(parts[0])
        except ValueError:
            continue
        rows.append(
            CycleRow(
                cycle_id=cid,
                problem=parts[1],
                score_field=parts[2],
                hours=parts[3],
                compute=parts[4],
                wiki_citations=parts[5],
                findings_added=parts[6],
                concepts_added=parts[7],
                author_mix=parts[8],
                outcome=parts[9],
                notes="|".join(parts[10:]),  # rejoin any pipes inside notes
            )
        )
    return rows


# ---------------- skill-library parsing ----------------


@dataclass(frozen=True)
class SkillRow:
    technique: str
    category: str
    tried: int
    top3: int
    finding: int
    last_used: str
    hit_rate: str  # raw string — may be "(n/a)" for meta entries


_SKILL_ROW_RE = re.compile(r"^\|\s*`[^`]+\.md`\s*\|")


def parse_skill_library(path: Path) -> list[SkillRow]:
    if not path.is_file():
        return []
    rows: list[SkillRow] = []
    for line in path.read_text().splitlines():
        if not _SKILL_ROW_RE.match(line):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 7:
            continue

        def _as_int(s: str) -> int:
            try:
                return int(s)
            except ValueError:
                return 0

        rows.append(
            SkillRow(
                technique=parts[0].strip("`"),
                category=parts[1],
                tried=_as_int(parts[2]),
                top3=_as_int(parts[3]),
                finding=_as_int(parts[4]),
                last_used=parts[5],
                hit_rate=parts[6],
            )
        )
    return rows


# ---------------- pattern detectors ----------------


@dataclass
class Stagnation:
    """A problem stuck across multiple consecutive cycles with no score change."""

    problem: str
    cycle_ids: list[int]
    outcomes: list[str]
    last_notes: str  # raw notes from the most recent cycle, for the human

    def is_flagged(self) -> bool:
        """A stagnation pattern is flagged when there's *evidence of dead-end*
        — not just any 3-cycle no-Δ run (e.g. cold scaffolds don't count as
        regressions, they're known gaps to fill)."""
        return any(
            tag in o.lower()
            for o in self.outcomes
            for tag in ("dead-end", "dispatch-failed", "converged")
        )


def detect_stagnations(rows: list[CycleRow], *, min_run: int = 3) -> list[Stagnation]:
    """Find runs of ≥ `min_run` consecutive cycles on the same problem
    with no score change.

    The list is ordered by last cycle_id ascending. Each run is the *longest*
    such consecutive sub-sequence for a given problem (we don't emit
    overlapping runs).
    """
    if not rows:
        return []
    out: list[Stagnation] = []
    i = 0
    while i < len(rows):
        j = i + 1
        while (
            j < len(rows)
            and rows[j].problem == rows[i].problem
            and not rows[j].score_changed
            and not rows[i].score_changed
        ):
            j += 1
        if j - i >= min_run:
            chunk = rows[i:j]
            out.append(
                Stagnation(
                    problem=rows[i].problem,
                    cycle_ids=[r.cycle_id for r in chunk],
                    outcomes=[r.outcome for r in chunk],
                    last_notes=chunk[-1].notes,
                )
            )
            i = j
        else:
            i += 1
    return out


_MANIFEST_TOKEN_RE = re.compile(
    # Two arms:
    #   1. strict[- ]?tol followed by any hyphen-suffix (-unsafe, -locked, -failing, -loss)
    #   2. `manifest` followed by up to ~40 hyphen/word chars and then a trigger
    #      verb (block / wir(e|ing) / fix / default). Non-greedy so we don't
    #      sweep across unrelated sentences.
    r"(strict[- ]?tol[\w-]*"
    r"|manifest[\w\- ]{0,40}?(?:block(?:ed|er)?|wir(?:e|ing)|fix|default))",
    re.IGNORECASE,
)


@dataclass
class ManifestRegression:
    """A cycle whose notes mention manifest/strict-tol — flag for human review."""

    cycle_id: int
    problem: str
    outcome: str
    matched: str  # the substring that triggered the match
    notes: str


def detect_manifest_regressions(rows: list[CycleRow]) -> list[ManifestRegression]:
    """Surface cycles whose notes mention manifest-blocking / strict-tol issues.

    This is the regression pattern the P14 cycle 49–51 case exposed:
    manifest defaults are strict-tol-unsafe, so dispatch produces a
    `dead-end` and subsequent cycles converge without an attempt.
    """
    out: list[ManifestRegression] = []
    for r in rows:
        m = _MANIFEST_TOKEN_RE.search(r.notes)
        if not m:
            continue
        out.append(
            ManifestRegression(
                cycle_id=r.cycle_id,
                problem=r.problem,
                outcome=r.outcome,
                matched=m.group(0),
                notes=r.notes,
            )
        )
    return out


# ---------------- technique heat map ----------------


@dataclass(frozen=True)
class TechniqueRanking:
    """Promote/demote/watchlist call for one technique."""

    technique: str
    category: str
    tried: int
    top3: int
    finding: int
    hit_rate: float | None  # None for "(n/a)" meta entries
    bucket: str  # "promote" | "demote" | "watchlist" | "ok" | "meta"


def rank_techniques(rows: list[SkillRow]) -> list[TechniqueRanking]:
    """Apply skill-library.md's promote/demote/watchlist rules."""
    out: list[TechniqueRanking] = []
    for s in rows:
        if s.hit_rate.lower() in {"(n/a)", "n/a", "—", "-"}:
            out.append(
                TechniqueRanking(
                    technique=s.technique,
                    category=s.category,
                    tried=s.tried,
                    top3=s.top3,
                    finding=s.finding,
                    hit_rate=None,
                    bucket="meta",
                )
            )
            continue
        try:
            hr = float(s.hit_rate)
        except ValueError:
            hr = float("nan")
        if s.tried < 3:
            bucket = "watchlist"
        elif s.tried >= 5 and hr < 0.2:
            bucket = "demote"
        elif s.tried >= 5 and hr >= 0.5:
            bucket = "promote"
        else:
            bucket = "ok"
        out.append(
            TechniqueRanking(
                technique=s.technique,
                category=s.category,
                tried=s.tried,
                top3=s.top3,
                finding=s.finding,
                hit_rate=hr,
                bucket=bucket,
            )
        )
    return out


# ---------------- wiki file counts ----------------


@dataclass(frozen=True)
class WikiCounts:
    findings_total: int
    dead_ends_total: int
    findings_recent: int
    questions_open: int
    questions_answered: int
    questions_total: int


def _count_files(path: Path, *, predicate=lambda p: True) -> int:
    if not path.is_dir():
        return 0
    return sum(1 for p in path.iterdir() if p.is_file() and p.suffix == ".md" and predicate(p))


def _status_open(path: Path) -> bool:
    """A question is open if its frontmatter has `status: open` (or no status:)."""
    try:
        text = path.read_text()
    except OSError:
        return False
    m = re.search(r"^status:\s*(\S+)", text, re.MULTILINE)
    if not m:
        return False  # unknown — don't count as open
    return m.group(1).lower() == "open"


def _status_answered(path: Path) -> bool:
    try:
        text = path.read_text()
    except OSError:
        return False
    m = re.search(r"^status:\s*(\S+)", text, re.MULTILINE)
    if not m:
        return False
    return m.group(1).lower() == "answered"


def count_wiki(
    findings_dir: Path,
    questions_dir: Path,
    *,
    recent_window_days: int = 30,
    now: dt.date | None = None,
) -> WikiCounts:
    """Count wiki files; `findings_recent` uses the `drafted:` frontmatter date."""
    today = now or dt.date.today()
    cutoff = today - dt.timedelta(days=recent_window_days)

    def _is_recent(p: Path) -> bool:
        try:
            text = p.read_text()
        except OSError:
            return False
        m = re.search(r"^drafted:\s*(\d{4}-\d{2}-\d{2})", text, re.MULTILINE)
        if not m:
            return False
        try:
            return dt.date.fromisoformat(m.group(1)) >= cutoff
        except ValueError:
            return False

    findings_all = (
        [p for p in findings_dir.iterdir() if p.is_file() and p.suffix == ".md"]
        if findings_dir.is_dir()
        else []
    )
    dead_ends = [p for p in findings_all if p.stem.startswith("dead-end-")]
    findings_recent = sum(1 for p in findings_all if _is_recent(p))

    questions_all = (
        [p for p in questions_dir.iterdir() if p.is_file() and p.suffix == ".md"]
        if questions_dir.is_dir()
        else []
    )
    open_q = sum(1 for p in questions_all if _status_open(p))
    answered_q = sum(1 for p in questions_all if _status_answered(p))

    return WikiCounts(
        findings_total=len(findings_all),
        dead_ends_total=len(dead_ends),
        findings_recent=findings_recent,
        questions_open=open_q,
        questions_answered=answered_q,
        questions_total=len(questions_all),
    )


# ---------------- report writer ----------------


REPORT_HEADER = "# meta-loop diagnostic report\n\n"


@dataclass
class DiagnosticReport:
    """Structured report — render() produces the markdown file."""

    generated_at: dt.datetime
    cycles_total: int
    outcome_counts: dict[str, int]
    score_changed_cycles: list[int]
    stagnations: list[Stagnation]
    manifest_regressions: list[ManifestRegression]
    techniques: list[TechniqueRanking]
    wiki: WikiCounts
    cycle_log_path: Path
    skill_library_path: Path
    findings_dir: Path
    questions_dir: Path

    def render(self) -> str:
        lines: list[str] = [REPORT_HEADER]
        lines.append(f"_Generated: {self.generated_at.strftime('%Y-%m-%dT%H:%M:%SZ')}_\n")
        lines.append(
            "Read-only diagnostic — see `knowledge/wiki/findings/meta-loop-design-from-literature.md`.\n"
        )
        lines.append("## Sources\n")
        lines.append(f"- cycle-log: `{self.cycle_log_path}`")
        lines.append(f"- skill-library: `{self.skill_library_path}`")
        lines.append(f"- findings: `{self.findings_dir}`")
        lines.append(f"- questions: `{self.questions_dir}`\n")

        lines.append("## Cycles summary\n")
        lines.append(f"- total cycles: **{self.cycles_total}**")
        lines.append(f"- cycles that changed score: **{len(self.score_changed_cycles)}**")
        if self.outcome_counts:
            lines.append("\n| outcome | count |")
            lines.append("|---|---|")
            for outcome, count in sorted(self.outcome_counts.items(), key=lambda kv: -kv[1]):
                lines.append(f"| {outcome} | {count} |")
        lines.append("")

        lines.append("## Surfaced regressions\n")
        if self.manifest_regressions:
            lines.append(
                f"**{len(self.manifest_regressions)} cycle(s) mention manifest "
                "or strict-tol issues** — likely manifest-default needs revisiting.\n"
            )
            lines.append("| cycle | problem | outcome | matched | notes |")
            lines.append("|---|---|---|---|---|")
            for m in self.manifest_regressions:
                notes_short = (m.notes[:120] + "…") if len(m.notes) > 120 else m.notes
                notes_safe = notes_short.replace("|", "\\|")
                lines.append(
                    f"| {m.cycle_id} | {m.problem} | {m.outcome} "
                    f"| `{m.matched}` | {notes_safe} |"
                )
        else:
            lines.append("_No manifest/strict-tol regressions detected._\n")
        lines.append("")

        lines.append("## Stagnation patterns (no-Δ runs of length ≥ 3)\n")
        if self.stagnations:
            flagged = [s for s in self.stagnations if s.is_flagged()]
            lines.append(
                f"**{len(self.stagnations)} stagnation run(s), "
                f"{len(flagged)} flagged** (dead-end / dispatch-failed / converged "
                "outcomes present — those are not just cold-scaffold gaps).\n"
            )
            lines.append("| problem | cycles | length | outcomes | flagged |")
            lines.append("|---|---|---|---|---|")
            for s in self.stagnations:
                cycles_s = ",".join(str(c) for c in s.cycle_ids)
                outcomes_s = ", ".join(sorted(set(s.outcomes)))
                lines.append(
                    f"| {s.problem} | {cycles_s} | {len(s.cycle_ids)} "
                    f"| {outcomes_s} | {'yes' if s.is_flagged() else 'no'} |"
                )
        else:
            lines.append("_No stagnation runs of length ≥ 3._\n")
        lines.append("")

        lines.append("## Technique heat map\n")
        if self.techniques:
            buckets = defaultdict(list)
            for t in self.techniques:
                buckets[t.bucket].append(t)
            for bucket_name in ("demote", "promote", "watchlist", "ok", "meta"):
                techs = buckets.get(bucket_name, [])
                if not techs:
                    continue
                lines.append(f"### {bucket_name} ({len(techs)})\n")
                lines.append("| technique | category | tried | top3 | finding | hit_rate |")
                lines.append("|---|---|---|---|---|---|")
                for t in sorted(techs, key=lambda x: -(x.hit_rate or -1)):
                    hr_s = "n/a" if t.hit_rate is None else f"{t.hit_rate:.2f}"
                    lines.append(
                        f"| `{t.technique}` | {t.category} | {t.tried} | {t.top3} "
                        f"| {t.finding} | {hr_s} |"
                    )
                lines.append("")
        else:
            lines.append("_No technique rows parsed._\n")

        lines.append("## Wiki state\n")
        lines.append(
            f"- findings: {self.wiki.findings_total} total, "
            f"{self.wiki.dead_ends_total} dead-ends, "
            f"{self.wiki.findings_recent} drafted in last window"
        )
        lines.append(
            f"- questions: {self.wiki.questions_total} total — "
            f"{self.wiki.questions_open} open, "
            f"{self.wiki.questions_answered} answered"
        )
        lines.append("")

        return "\n".join(lines)


def run(
    *,
    cycle_log: Path,
    skill_library: Path,
    findings_dir: Path,
    questions_dir: Path,
    output: Path,
    now: dt.datetime | None = None,
) -> DiagnosticReport:
    """Read all sources, build the report, write it. Returns the report object."""
    now = now or dt.datetime.now(dt.timezone.utc)

    cycles = parse_cycle_log(cycle_log)
    outcome_counts = Counter(r.outcome for r in cycles)
    score_changed = [r.cycle_id for r in cycles if r.score_changed]
    stagnations = detect_stagnations(cycles)
    manifest_regs = detect_manifest_regressions(cycles)

    skills = parse_skill_library(skill_library)
    technique_ranks = rank_techniques(skills)

    wiki = count_wiki(findings_dir, questions_dir, now=now.date())

    report = DiagnosticReport(
        generated_at=now,
        cycles_total=len(cycles),
        outcome_counts=dict(outcome_counts),
        score_changed_cycles=score_changed,
        stagnations=stagnations,
        manifest_regressions=manifest_regs,
        techniques=technique_ranks,
        wiki=wiki,
        cycle_log_path=cycle_log,
        skill_library_path=skill_library,
        findings_dir=findings_dir,
        questions_dir=questions_dir,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report.render())
    return report


__all__ = [
    "CycleRow",
    "DiagnosticReport",
    "ManifestRegression",
    "SkillRow",
    "Stagnation",
    "TechniqueRanking",
    "WikiCounts",
    "count_wiki",
    "detect_manifest_regressions",
    "detect_stagnations",
    "parse_cycle_log",
    "parse_skill_library",
    "rank_techniques",
    "run",
]
