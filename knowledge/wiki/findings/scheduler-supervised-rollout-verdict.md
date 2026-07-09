---
type: finding
author: agent
drafted: 2026-06-09
question_origin: problem-meta
status: answered
related_problems: [2, 3, 4, 10, 12]
related_concepts: [meta-learning-automation]
cites:
  - inner-agent-first-run.md
  - dead-end-p12-stochastic-exhausted-no-algebraic-operator-wired.md
  - autocorrelation-family-displaced-2026-06.md
  - ../../agent/inner-agent-readiness.md
  - ../../agent/unattended-runbook.md
  - ../../tools/problem_priority.py
  - ../../../scripts/scheduled_cycle.py
---

# Finding: Phase 3 supervised rollout — the picker is only as honest as its inputs

## Question

Is the scheduled autonomous loop (`scheduled_cycle.py` → `--one-problem
--by-priority`) ready for **unattended** cadence — measured on records/attempts,
$/run, LLM-path reliability, capture quality, and (the failure mode that
motivated Phase 3) whether it targets headroom instead of grinding one problem?

## Rollout setup

7 attended scheduler runs on 2026-06-09/10 (cadence compressed:
`--skip-if-recent 0`, back-to-back, otherwise the production invocation; auto-
submit at its armed default, 6-gate protected). Runs 1–3 on the v0 picker,
4–5 after fix-1, 6–7 after the full v2 fix set.

## Measurements (runs 1–5; per-cycle exact from telemetry)

| Metric | Value | Bar |
|---|---|---|
| LLM-path rate | **13/13 cycles** (0 fallback, 0 parse fail, 0 timeout) | R2 ≤ 20% fallback ✅ |
| Cost | **$0.51–0.61/cycle**, ~$1.20–1.40/run, $7.3 total | R5 ≪ $5/cycle ✅ |
| Wall-clock | 18–26 min/run (LLM 26–82s/cycle; post-cycle discipline dominates) | 7200s cap ✅ |
| Records / submissions | 0 / 0 (all visits honest-converged; agent cited existing dead-ends instead of re-deriving or spamming) | R8/R9 ✅ |
| New captures | 0 findings (correct: all visited problems were at known walls) | anti-spam held |
| Targeting | **runs 1–3 ALL ground P12; runs 4–5 both picked P10** | ❌ the Phase-3 point |

## What broke, and why (three layered causes)

1. **Stale `score_current` frontmatter** — P12's page said 1.3539 while the
   repo's verified seed reaches 1.2809320520721 (= SOTA basin,
   minImprovement-blocked from submission). That inflated its relative
   headroom 6 orders of magnitude (5.7e-2 vs the true ~0), and headroom
   dominates the priority product → permanent grind. P2's page was similarly
   stale in the *other* direction (rank-3-displaced the day after our record).
2. **Raw headroom spread defeats rotation** — relative headrooms span 6+
   orders across problems, so no floor on hit-rate/staleness could ever
   rotate the queue away from the largest entry (380:1 ratio).
3. **No-data categories outranked measured ones** — a category with no
   skill-library rows got the fixed 0.5 neutral, beating every *real* rate
   (0.1–0.3); that's why runs 4–5 repeated P10 instead of moving to P4.

## The v2 fix set (all live-verified on the ranked queue)

- **Live our-score**: one leaderboard fetch per problem now yields arena #1
  AND our standing; "our score" = direction-best(live, frontmatter), covering
  both staleness modes (frontmatter lags retakes; the board lags
  unsubmittable local capability).
- **Log-compressed headroom**: `log10(1 + h/1e-7)` (minImprovement units)
  keeps headroom dominant but lets hit-rate/staleness rotate the queue.
- **Empirical-Bayes neutral**: unknown categories get the library-wide
  tried-weighted rate, not 0.5.
- Data fixes: P12 + P2 frontmatter corrected with provenance comments.

Post-fix ranked queue (live): **P3 → P10 → P4** — matches the human
retake-priority audit of the same evening (P4/P3 top targets; P12/P2/P11
correctly sunk).

## Runs 6–7 (picker v2)

Both runs picked **P3** (cycles 300–303, seed re-verified at 0.96227384,
honest-converged; no submission — gap to #1 is 4.3e-4). Two observations:

1. **Rotation across problem classes works** (P12 → P10 → P3 followed the
   data fixes), but back-to-back runs stick on the same #1: the 0.1
   staleness floor flattens recency differences, so consecutive-run ordering
   is static headroom×hit-rate. Acceptable at cron cadence (a 2h gap accrues
   real staleness... slowly) but the sterile-visit decay below is the real
   fix.
2. **New R3 regression caught**: 2 of 4 cycles fell back to mechanical
   because `notes` exceeded the strict 200-char schema cap (283/294 chars) —
   the cited_sources strict-parse failure mode reborn on a different field.
   Fixed the same way: lenient truncate/flatten with a warning, never reject
   the whole response over a cosmetic constraint.

## Collateral finding: test suites were polluting production ledgers

Two test-isolation leaks found during the rollout (same class as Goal 0's
`claude -p` leak): tests auto-importing the real `try_submit` made **live
arena calls** and appended ~40 fake rows/run to the weekly-audited
`mb/logs/auto-submit.md` (gates held — 0 spurious submissions, defense in
depth worked). Sealed with a `tests/conftest.py` autouse fixture (module-attr
patch; the two modules that test the real chain are exempt and self-isolated).
Pattern for the wiki: **a lazily-imported production side-effect is a test
landmine — seal at conftest level, not per-test.**

## Verdict

**Iterate-complete; NOT yet promoted to unattended.** The architecture is
sound (reliability + cost + anti-spam all green; kill-switch stack and
monitor in place) and the targeting failure was found and fixed — but the
v2 picker has only the runs 6–7 window behind it. Preconditions for flipping
the cron on (runbook cadence):

1. One more clean attended window (≥3 runs) showing rotation + ≥1
   non-sterile visit on the v2 picker.
2. The weekly-audit habit started (the audit ledger now has a corrigendum to
   exclude the test-artifact rows).
3. P7 (PNT) onboarded — most recently taken #1, zero dead-end ledger, but
   invisible to the picker until it has a problem page + queue entry.

## What might still work (next levers, in order)

1. **Onboard P7** — highest information-per-dollar target the picker can't see.
2. **Sterile-visit feedback** — visits that converge with only a cite (no new
   page, no score move) should decay the problem's priority faster than
   staleness recovers it. Needs a reliable cite-vs-create signal in the
   cycle-log row (current `findings_added` counts both — fix the row writer
   first, then add the decay).
3. **P4 via warm self-pruning** — the connect-the-dots section now puts the
   P2 record's prescription in front of every P4 visit; the picker ranks P4
   top-3. The first unattended record attempt is most likely here.
