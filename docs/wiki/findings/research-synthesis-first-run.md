---
type: finding
author: agent
drafted: 2026-05-25
question_origin: js/feat/research-synthesis G7
status: scaffolded
related_findings:
  - research-synthesis-design
  - qmd-metal-embed-fix
cites:
  - ../../../scripts/research_synthesis_shadow.py
  - ../../../src/einstein/research_synthesis/shadow.py
  - ../../../docs/ops/com.einstein.research-synthesis-shadow.plist
---

# Research-synthesis first unattended run

**status: scaffolded — awaits operator-initiated execute pass.**

## What this finding will document (post-run)

After the first unattended `--execute --n-cycles 10` pass produces a
result in `mb/logs/research-synthesis-shadow.md`, the operator (or the
next agent session) fills in:

1. **Cross-source patterns the agent surfaced** — read each cycle's
   `mb/problems/<id>-<slug>/literature-synthesis-<date>.md` and group the
   `cross_source_patterns[]` entries by pattern type. Report frequency
   and which problems triggered them.
2. **Which sources informed real attempts** — count entries in
   `mb/logs/cited-sources.jsonl` per `docs/source/<file>.md`. Cross-check
   against `mb/logs/promotion-candidates.md` (any source ≥3 cites is a
   promotion candidate already).
3. **What generalized vs domain-specific** — same table as Goal 0's
   finding (`research-synthesis-design.md`) but populated with concrete
   evidence from the run rather than from literature alone.

## How to run the experiment (operator)

```bash
# From the worktree root (cb-js-feat-research-synthesis/ or main after merge):
PROJECT_ROOT="$(pwd)"
PLIST_LOCAL="docs/ops/com.einstein.research-synthesis-shadow.plist"
PLIST_INSTALLED="$HOME/Library/LaunchAgents/com.einstein.research-synthesis-shadow.plist"

# 1. Dry-run check — verifies the proposal + plan without forking worktrees.
uv run python scripts/research_synthesis_shadow.py --dry-run

# 2. Substitute the placeholder + install.
sed "s|__PROJECT_ROOT__|$PROJECT_ROOT|g" "$PLIST_LOCAL" > "$PLIST_INSTALLED"
launchctl bootstrap "gui/$UID" "$PLIST_INSTALLED"

# 3. Watch progress (heavy — 2-4 hours wall clock for N=10).
tail -f ../mb/logs/research-synthesis-shadow.out.log

# 4. After completion, uninstall (one-shot — not a recurring job).
launchctl bootout "gui/$UID/com.einstein.research-synthesis-shadow"
rm "$PLIST_INSTALLED"

# 5. Read the result + populate this finding's "post-run" sections.
cat ../mb/logs/research-synthesis-shadow.md
```

Manual alternative (run in foreground):

```bash
uv run python scripts/research_synthesis_shadow.py --execute --n-cycles 10
```

## Promotion gate (automated)

`synthesis_promotion_decision()` enforces three gates:

1. `findings_delta >= 0` — arm A authored at least as many findings/cycle as arm B
2. `score_changed_delta >= 0` — arm A didn't regress on score moves
3. `cycles_with_citations_a >= 1` — at least one cycle in arm A produced
   a citation-grounded attempt (the citation-grounded improvement
   requirement from the G6 plan)

CLI exits 0 if all gates pass, 2 if any gate fails. Human still signs off
on the final merge to main.

## Portable primitives surfaced (for post-run extraction)

The branch G7 plan calls for extracting domain-agnostic primitives after
the first run. Candidates already isolated by package boundary:

- **`research_synthesis.query`** (qmd subprocess wrapper, gather/dedupe) —
  portable; depends only on `subprocess` + a `Hit` dataclass.
- **`research_synthesis.schema.LiteratureSynthesis`** — portable; the
  `cross_source_patterns`/`proposed_approaches`/`gaps_identified` shape
  is domain-agnostic.
- **`research_synthesis.synthesizer.synthesize`** — portable except for
  the prompt body; lift the prompt into a template, the rest moves.
- **`promotion_candidates.py`** — portable; takes any JSONL of
  `{cycle_id, problem, cited_sources}` records.
- **`research_synthesis.shadow.{cycles_with_citations, synthesis_promotion_decision}`** —
  citation-grounded promotion logic; depends on the cycle-log row format
  but not the meaning of the citations.

Math-specific bits to leave behind: `qmd` collection names
(`einstein-wiki`, `einstein-wiki-source`), the `mb/problems/<id>-<slug>/`
layout, the council persona triggers, the arena-verifier coupling in the
inner agent.

The extraction itself ships as a follow-on branch
(`js/refactor/research-synthesis-portable`) after this finding is
populated with first-run evidence — per the agent-stance "don't
pre-abstract; extract after the fact" rule.
