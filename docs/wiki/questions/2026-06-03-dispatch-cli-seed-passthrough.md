---
type: question
author: agent
drafted: 2026-06-03
status: open
asked_by: autonomous_loop_p14_cycle89
related_problems: [14, 5, 11]
related_concepts: [float64-ceiling, mpmath-ulp-polish, basin-rigidity]
cites:
  - docs/wiki/questions/2026-06-01-p14-ae-tied-seed-mpmath-polish.md
  - src/einstein/optimizer_manifest.yaml
  - src/einstein/optimizer_dispatch.py
---

# Should `optimizer_dispatch` pass `--seed` (and other per-run args) through to the strategy script?

## Background

`scripts/circle_packing_square/mpmath_ulp_polish.py` accepts `--seed <path>` to
override the canonical warm-start, but `optimizer_dispatch --problem-id 14
--strategy mpmath_ulp_polish` exposes no way to forward extra args. The dispatch
CLI accepts only `--problem-id`, `--strategy`, `--manifest`, `--timeout`,
`--dry-run`, `--payload`.

Consequence: the cycle-54 open question
([`2026-06-01-p14-ae-tied-seed-mpmath-polish.md`](2026-06-01-p14-ae-tied-seed-mpmath-polish.md))
— "does ulp-polish from the archived AE-tied seed yield more sub-ulp slack than
from our rank-2 seed?" — cannot be answered via the sanctioned autonomous-loop
dispatch path. Same shape blocks P5/P11/P17/P18/P22/P23 if/when those problems
acquire archived alternative seeds worth re-polishing.

This cycle (89) re-dispatched `mpmath_ulp_polish` on the canonical seed and got
`2.6359830849175947` — identical to cycle 87. The float64 ceiling holds; arena
#1 is ~5e-15 above. Useful negative result, but the AE-seed variant remains
untouched because of the wiring gap.

## The question

What's the right shape for per-run arg passthrough in `optimizer_dispatch`?

Two candidates:

1. **Generic `--strategy-args "<json>"` flag** — JSON blob forwarded as
   `argparse` args to the script. Simple, but encodes unsafe coupling between
   dispatch CLI and arbitrary script flags.
2. **Manifest-encoded seed variants** — register e.g.
   `mpmath_ulp_polish_ae_seed` as a distinct strategy with a different seed
   path baked into the manifest. Clean per-strategy auditability; multiplies
   the manifest by the number of viable seeds (small in practice — we have at
   most 2–3 alternative seeds per float64-ceiling problem).

## Falsifiable answer

Either:
- A PR that adds whichever variant + runs the AE-tied seed test, with the
  result triple-verified and a finding written, OR
- A documented decision (in this question, status: superseded) that
  per-run seed override is out of scope and AE-tied tests will be one-off
  manual runs outside the autonomous loop.

## Suggested next step

Manifest-encoded variant (option 2) is the lower-risk path — touches one YAML
entry per problem, no dispatch CLI change. Add `mpmath_ulp_polish_ae_seed` to
the P14 manifest entry, point at `mb/.../solution-AE-tied-rank2.json`, run via
dispatch, close
[`2026-06-01-p14-ae-tied-seed-mpmath-polish.md`](2026-06-01-p14-ae-tied-seed-mpmath-polish.md)
with a finding. ~10 min of work.

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"float64 ceiling" OR all:"mpmath ulp polish" OR all:"Should `optimizer_dispatch` pass `--seed` and other") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
