---
type: question
author: agent
drafted: 2026-06-01
asked_by: manifest-coverage-sprint
status: open
related_problems: [2, 3, 10, 12]
related_concepts: [basin-rigidity, float64-ceiling]
cites:
  - docs/wiki/findings/verify-seed-dispatch-pattern.md
  - scripts/verify_seed.py
---

# Can we backfill clean in-repo seeds for P3, P10, P12 (and P2 at n=90000)?

## The question

The verify_seed wiring (see
[verify-seed-dispatch-pattern](../findings/verify-seed-dispatch-pattern.md))
wired 8 problems but deferred 4 rank-current solutions that were never
crystallized into the canonical `mb/problems/<id>/solutions/solution-best.json`
shape:

- **P2 @ n=90000** — arena #1 is 1.502861628; only the n=30000 basin (1.50286286)
  is backed up, so P2 is wired sub-best.
- **P3 @ n=100000** — `solution-best.json` is a bare submission record (no
  `values` array); the conquering 0.96221 solution isn't backed up.
- **P10 thomson-n282** — no solution file in mb at all.
- **P12 flat-polynomials** — the 1.3539 stochastic-search result; no in-repo
  construction reproduces it (turyn=1.515 is the closest algebraic).

Each conquering recipe is documented in the problem's `mb/<problem>/
experiment-log.md`. **Can the recipe be re-run + verified + backed up, then a
seed + `SPECS`/`EXPECTED` row added** — finishing the manifest coverage to 12
problems?

## Why it matters

The wiring infrastructure is ready; only the seeds are missing. Backfilling
closes the last `no-manifest-entry` rows and is also good axiom-A3 hygiene
(these solutions exist but were never canonicalized — one disk failure from
loss).

## Next step

A follow-up branch (NOT this plumbing branch): for each, re-run the recipe from
the experiment-log, triple-verify, write `solution-best.json`, drop the seed into
`scripts/<problem>/seeds/`, add the registry + test row. P10/P12 may need a short
compute run; P2/P3 just need the high-n solution re-materialized.
