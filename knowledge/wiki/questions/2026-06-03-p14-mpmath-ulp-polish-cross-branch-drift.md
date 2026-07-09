---
type: question
author: agent
drafted: 2026-06-03
asked_by: autonomous-loop
status: open
related_problems: [14]
related_concepts: [float64-ceiling, basin-rigidity, mpmath-precision]
cites:
  - knowledge/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md
  - src/einstein/optimizer_manifest.yaml
  - src/einstein/ulp_polish.py
---

# Why does `mpmath_ulp_polish` drift +4e-15 between branches on the same P14 seed?

## The observation

Running `uv run python -m einstein.optimizer_dispatch --problem-id 14 --strategy mpmath_ulp_polish`
(args from manifest: `--dps 80 --max-iter 100`, same seed file) yields:

| Branch | Score | Δ vs rank-2 seed |
|---|---|---|
| `js/feat/p14-mpmath-ulp-polish-body` (PR #111, cycle 53) | 2.6359830849175907 | +6.617e-14 |
| `js/feat/triple-verify-wiring` (this cycle, 2026-06-03)   | 2.6359830849175947 | +7.02e-14   |

Drift: **+4.0e-15** (~18 ulps at this magnitude), much smaller than arena
`minImprovement=1e-7` so submission-irrelevant, but much larger than 1 ulp so
NOT pure float-noise.

## Why it might happen

Cycle 53 wrote the body in `scripts/circle_packing_square/mpmath_ulp_polish.py`.
The Phase-2a refactor extracted the kernel to `src/einstein/ulp_polish.py`. If
the extracted engine reorders the sweep, changes accept-tie-breaking, or
recomputes the seed mpmath state differently, repeated coordinate-descent passes
will land on a neighbouring float64 ceiling vertex even though both runs are
"deterministic" in their own terms.

Both scores still satisfy the dual gate (arena float64 strict + mpmath exact ≥ 0)
by construction, so axiom A1 holds — this is *which* float64 vertex on the
basin's ceiling we settle at, not whether the score is real.

## What a falsifiable answer looks like

1. Diff `scripts/circle_packing_square/mpmath_ulp_polish.py` (PR #111 era) vs
   `src/einstein/ulp_polish.py` + the current script's call into it. Identify
   the divergence (sweep order? accept ordering? seed normalization?).
2. If the divergence is benign (e.g. dict-key iteration order vs explicit list),
   pin it deterministically and verify both branches converge to the same vertex.
3. If the divergence is substantive (e.g. accept-tie-breaking rule changed),
   document which rule yields the higher score and pick it.

## Why this matters

Without a deterministic, reproducible final-vertex rule, the "float64 ceiling"
becomes a small-set rather than a point — every refactor risks claiming a new
+sub-ulp "improvement" that's just a different ceiling vertex. Phase-2a's
generalization across P5/P11/P14 needs the engine to be byte-stable across
refactors, else the cycle log will be noisy.

## Out of scope

This is not a submission concern. P14 minImprovement = 1e-7 ≫ any drift here.
The question is engineering hygiene, not arena progress.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"float64 ceiling" OR all:"basin rigidity" OR all:"`mpmath_ulp_polish` drift +4e-15 between branches on") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
