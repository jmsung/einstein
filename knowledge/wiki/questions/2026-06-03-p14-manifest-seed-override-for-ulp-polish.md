---
type: question
author: agent
drafted: 2026-06-03
status: open
asked_by: autonomous_loop
related_problems: [14, 5, 11, 17, 18, 22, 23]
related_concepts: [float64-ceiling, basin-rigidity, arena-tolerance-drift]
cites:
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/mpmath_ulp_polish.py
  - knowledge/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md
---

# Should the manifest expose `--seed` as a tunable for `mpmath_ulp_polish` (and the float64-ceiling family more broadly)?

## The gap

`mpmath_ulp_polish` (P14, P11, P5 entries in `src/einstein/optimizer_manifest.yaml`) hard-codes its `cli_args` to `["--dps", "80", "--max-iter", "100"]`. The script itself accepts `--seed` (default `scripts/circle_packing_square/seeds/p14_canonical.json`) but dispatch cannot override it. P14 ships TWO seeds — `p14_canonical.json` (the submitted rank-2 basin) and `p14_ae_tied.json` (the AE-tied basin at start-Σr ≈ 2.6359830849176067, ~1.6e-14 above the cycle-53 ulp-polish ceiling on canonical). Cycle 53 polished only canonical. We cannot reach AE-tied through the autonomous loop without bypassing dispatch.

## Why it matters

1. Multi-seed coverage from the dispatch path lets the autonomous loop measure whether two seeds in the same problem actually share a float64 basin (informs the basin-rigidity concept), or merely both lie under the same minImprovement gate.
2. The ae_tied seed is ALREADY rejected by the submission proximity guard (`knowledge/wiki/findings/arena-proximity-guard.md`), so polishing it is purely diagnostic — no submission-policy risk.
3. The same wiring gap blocks the P5/P11/P17 ulp-polish entries from exploring alternate seeds, which is the natural next step once an in-repo "second basin" is found.

## Candidate resolutions

- (a) Per-problem `seed:` key under each optimizer entry, defaulting to the script's own default when omitted.
- (b) Per-problem `seeds:` *list* under the optimizer entry, where dispatch fans out one subprocess per seed and emits the max — closer in spirit to the autoresearch 1+1 rule.
- (c) Leave the manifest fixed; have dispatch read seed candidates from a sibling `seeds/` directory and fan out automatically.

## Falsifiable answer

A working dispatch command that runs `mpmath_ulp_polish` against `p14_ae_tied.json` and emits `json_score_payload` parseable by the existing `result_parser`. Bonus: a triple-verified score from that seed (would either match cycle 53's 2.6359830849175907 → confirms single-basin claim, or land above/below → falsifies it).

## Suggested next step

Convert into a small `feat/manifest-seed-override` worktree once another problem in the float64-ceiling family acquires a second in-repo seed. Until then, stays open.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"float64 ceiling" OR all:"basin rigidity" OR all:"Should the manifest expose `--seed` as") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
