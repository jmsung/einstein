"""research_synthesis.shadow — wire pre-cycle synthesis to meta_loop's A/B harness.

Goal 6 of `js/feat/research-synthesis`. The shadow primitive (worktree fork +
arm metrics + delta + log) is `src/einstein/meta_loop/shadow.py` (merged via
PR #104). This module is the first consumer:

- A `rule_edit` Proposal that flips on the pre-cycle synthesis step at
  cycle-start in `.claude/rules/cycle-discipline.md`.
- A citation-aware promotion gate: A wins iff
  `findings_delta >= 0` AND at least one cycle in arm A declared
  ``cited_sources != []`` (the citation-grounded improvement requirement
  from the branch G6 plan).
- A metric extractor that pulls citation counts from the cycle-log's
  trailing `cites_src` column (the column my G4 added).

Caller is `scripts/research_synthesis_shadow.py`; tests live alongside.
"""

from __future__ import annotations

import datetime as _dt
import re
from dataclasses import dataclass
from pathlib import Path

from einstein.meta_loop.proposals import Confidence, Proposal, ProposalType

# Cycle-log rows my G4 emits look like::
#
#     | 42 | P19-difference-bases | ... | a:1/h:0/hyb:0 | no-change | smoke | 3 |
#
# Trailing column is the cited_sources count. This pattern grabs the leading
# cycle_id and trailing count for fast scans without re-parsing the full row.
_CITES_TRAILING_RE = re.compile(r"^\|\s*(\d+)\s*\|.*\|\s*(\d+)\s*\|\s*$")

DEFAULT_SHADOW_RULE_PATH = ".claude/rules/cycle-discipline.md"


# ---------------- metric: cycles with non-empty cited_sources ----------------


def cycles_with_citations(cycle_log_path: Path, *, since_cycle_id: int = 0) -> int:
    """Count cycle-log rows whose trailing `cites_src` column is > 0.

    `since_cycle_id`: only count cycles with `cycle_id > since_cycle_id`.
    The shadow arms each start at a known max-cycle baseline; pass that here
    to scope the count to cycles produced by the arm's run.

    Returns 0 if the file is missing or empty.
    """
    if not cycle_log_path.is_file():
        return 0
    n = 0
    for line in cycle_log_path.read_text(encoding="utf-8").splitlines():
        m = _CITES_TRAILING_RE.match(line.strip())
        if not m:
            continue
        cid = int(m.group(1))
        cites = int(m.group(2))
        if cid > since_cycle_id and cites > 0:
            n += 1
    return n


# ---------------- promotion decision ----------------


@dataclass(frozen=True)
class SynthesisPromotionDecision:
    """Tri-tuple for the synthesis A/B gate."""

    a_wins: bool
    reason: str
    cycles_with_citations_a: int
    cycles_with_citations_b: int


def synthesis_promotion_decision(
    *,
    findings_delta: float,
    score_changed_delta: float,
    cycles_with_citations_a: int,
    cycles_with_citations_b: int,
    min_findings_delta: float = 0.0,
    min_score_delta: float = 0.0,
) -> SynthesisPromotionDecision:
    """G6 promotion gate.

    A wins iff:
      1. findings_delta >= min_findings_delta (A authored ≥ B's per-cycle findings)
      2. score_changed_delta >= min_score_delta (A didn't regress on score moves)
      3. cycles_with_citations_a >= 1 — at least one cycle in arm A produced
         a citation-grounded attempt. Without this, "research synthesis on"
         is just adding tokens without proving the synthesis step paid off.

    The third gate is the branch G6 plan's requirement: "≥1
    attempt-derived-from-citation appears in synthesis arm".
    """
    reasons: list[str] = []
    if findings_delta < min_findings_delta:
        reasons.append(f"findings_delta {findings_delta:.3f} < {min_findings_delta}")
    if score_changed_delta < min_score_delta:
        reasons.append(f"score_changed_delta {score_changed_delta:.3f} < {min_score_delta}")
    if cycles_with_citations_a < 1:
        reasons.append("arm A produced zero citation-grounded cycles")
    a_wins = not reasons
    reason = (
        f"a_wins=true (Δfindings={findings_delta:.3f}, "
        f"Δscore_chg={score_changed_delta:.3f}, "
        f"cited_A={cycles_with_citations_a}, cited_B={cycles_with_citations_b})"
        if a_wins
        else "a_wins=false: " + "; ".join(reasons)
    )
    return SynthesisPromotionDecision(
        a_wins=a_wins,
        reason=reason,
        cycles_with_citations_a=cycles_with_citations_a,
        cycles_with_citations_b=cycles_with_citations_b,
    )


# ---------------- proposal builder ----------------


SYNTHESIS_RULE_DIFF = """--- a/.claude/rules/cycle-discipline.md
+++ b/.claude/rules/cycle-discipline.md
@@ -1,3 +1,8 @@
 # Cycle discipline — every cycle logged, no cherry-picking
+
+## Pre-cycle (Goal 5 of js/feat/research-synthesis; A/B-promoted)
+
+0a. **Pre-cycle synthesis (research_synthesis):** before step 0 (qmd query),
+    run `cb/scripts/research_synthesis.py --problem-id N` which writes
+    `mb/problems/<id>-<slug>/literature-synthesis-<date>.md` for the
+    inner agent to consume. Citations land in `cited_sources` of the
+    cycle-log row + `mb/logs/cited-sources.jsonl` sidecar.
"""


def make_synthesis_proposal(
    *,
    proposal_id: str = "rs-shadow-enable-synthesis",
    evidence_cycles: list[int] | None = None,
    created_at: _dt.datetime | None = None,
) -> Proposal:
    """Construct the rule_edit Proposal that toggles synthesis on at cycle-start.

    Validated by Proposal.__post_init__ (target_path matches the rule_edit
    pattern; diff is non-empty). Used as the "treatment" in the shadow A/B.
    """
    return Proposal(
        id=proposal_id,
        type=ProposalType.RULE_EDIT.value,
        target_path=DEFAULT_SHADOW_RULE_PATH,
        proposed_diff=SYNTHESIS_RULE_DIFF,
        evidence_cycles=evidence_cycles or [],
        expected_metric_delta={
            "findings_added_per_cycle": 0.1,
            "cycles_with_citations": 1.0,
        },
        predicted_regressions=[
            "synthesis step may add ~30s/cycle wall-clock",
            "synthesis step may consume ~30K tokens/cycle",
            "if cited_sources field is wrong, downstream promotion_candidates noise",
        ],
        confidence=Confidence.LOW.value,
        requires_shadow=True,
        rationale=(
            "Goal 6 of js/feat/research-synthesis. Validates whether enabling "
            "pre-cycle synthesis (Goals 0–5 of this branch) actually improves "
            "the inner loop's outcomes vs. control. Promotion gate requires "
            "citation-grounded improvement: at least one cycle in arm A must "
            "have non-empty cited_sources, in addition to non-negative "
            "findings_delta and score_changed_delta."
        ),
        author="agent",
        created_at=created_at or _dt.datetime.now(_dt.timezone.utc),
    )
