---
type: finding
author: agent
drafted: 2026-06-01
question_origin: problem-2,4,5,11,15,16,18,19
status: answered
related_concepts: [float64-ceiling, arena-tolerance-drift, basin-rigidity]
cites:
  - scripts/verify_seed.py
  - src/einstein/optimizer_dispatch.py
  - src/einstein/optimizer_manifest.yaml
  - docs/wiki/findings/dead-end-p14-dispatch-cli-noop.md
  - docs/agent/cycle-log.md
---

# The verify_seed dispatch pattern: how to make basin-locked problems dispatch real numbers

## The question

The strategy_picker kept ending cycles on P1–P19 with
`strategy-picked-no-execution; dispatch: no-manifest-entry` (cycle-log rows
45–46, 58–77). The manifest had real entries only for P14 and a P22 stub. The
sprint question: **how do you wire ~10 frozen/basin-locked problems into the
optimizer manifest without writing (and maintaining) a bespoke optimizer wrapper
per problem?**

## The answer — one generic emitter, not N wrappers

Two facts made a single generic emitter strictly better than 11 bespoke
wrappers:

1. **All problem evaluators share a uniform contract.** Every
   `src/einstein/<problem>/evaluator.py` exposes `evaluate(data: dict) -> float`
   that *is* the arena verifier (the heilbronn pair instead expose
   `arena_score(data["points"])` — one adapter row covers it).
2. **For a basin-locked problem, the rank-current "optimizer" *is* "verify the
   best known basin".** Re-running the heavy search (CMA-ES, basin-hopping,
   parallel tempering) just rederives the same float64-ceiling number at great
   compute cost (confirmed across P5, P11, P15, P16, P19 — see their
   experiment-logs). So "load best seed → re-score" is not a degenerate
   stand-in; it is the honest rank-current operation.

`scripts/verify_seed.py` implements this: a `SPECS` registry maps `problem_id →
(evaluator module, scorer fn, data key, in-repo seed, output)`. It loads the
in-repo seed, scores it through the audited arena evaluator — which is
**triple-verify checks #1 (fast evaluator) + #2 (independent reimpl) in one
call** — and emits `{"score", "payload"}` for the `json_score_payload` parser.

Seeds live in-repo at `scripts/<problem>/seeds/best.json[.gz]` (gzipped for the
30k/100k-float autocorrelation vectors, to stay under the 1 MB large-file gate),
mirroring the `slsqp_polish.py` discipline: deterministic, self-contained, no
dependence on the gitignored `results-temp/` or the private `mb/` tree.

**Prerequisite (the load-bearing fix):** `optimizer_dispatch.py` had no CLI, so
the documented `python -m einstein.optimizer_dispatch` command was a silent
no-op — *every* manifest problem was unreachable via the autonomous toolset, not
just P14. Adding an `argparse main()` (prints `DispatchResult` JSON, sets exit
code) is what turns the wiring from theatre into real dispatch. See
[dead-end-p14-dispatch-cli-noop](dead-end-p14-dispatch-cli-noop.md).

Wired (8): P2, P4, P5, P11, P15, P16, P18, P19. Each re-scores its basin
deterministically (pinned in `tests/test_verify_seed.py`). None can trigger a
spurious auto-submit: a basin-locked re-score never beats arena #1, so the
gate chain (axiom A1 submission policy) stays closed by construction.

## Why this is honest, not a shortcut

- The bandit now gets a **real, triple-verified** outcome per cycle ("P5 →
  12.88922990769401, Δ=0") instead of a `no-manifest-entry` non-event. That a
  frozen problem yields Δ=0 every cycle is the *truth*, not a degenerate signal.
- The heavy optimizers stay in `scripts/<problem>/` for Phase-2 record
  campaigns. Wiring `verify_seed` doesn't claim those problems are "solved by
  re-scoring"; it claims the dispatch *channel* now produces a real number.
- One arena-tolerance subtlety surfaced and was handled honestly: P18's backed-up
  rank-#1 config sits 1.98e-9 over our local `PERIMETER_TOL=1e-12` though the
  arena accepts it. Rather than loosen the strict check, the seed is uniformly
  shrunk to strict-valid (the documented `uniform-radius-shrink-fallback` op),
  costing 1.23e-9 of score — a real local↔arena drift datum, not a hidden fudge.

## What this rules out

- The "wire each problem's heavy optimizer individually" plan: it's higher-risk
  (per-problem scoring bugs), higher-maintenance, and produces nothing the
  re-score doesn't for a basin-locked problem.
- Reading the no-manifest-entry rows as signal about the *problems*. They were
  signal about *plumbing*, now closed.

## What's still open — the seed-backfill gap (P3, P10, P12, P2-at-n=90k)

Four rank-current solutions were **not backed up cleanly** to `mb/problems/*/
solutions/`, so they have no in-repo seed and were deferred:

| pid | slug | rank-current | why no seed |
|---|---|---|---|
| 2 | first-autocorrelation | 1.502861628 (n=90000) | only the n=30000 basin (1.50286286) is backed up; P2 is wired to that |
| 3 | second-autocorrelation | 0.96221 (n=100000) | no `values` array backed up; `solution-best.json` is a bare submission record |
| 10 | thomson-n282 | #5 frozen | no solution file in mb at all |
| 12 | flat-polynomials | 1.3539 | stochastic-search result, not backed up; no in-repo construction reproduces it (turyn=1.515 is the closest algebraic) |

This is a **backup-discipline gap** (axiom A3: never lose a solution — these
weren't lost, but they were never crystallized into the canonical
`solution-best.json` shape). The fix is a follow-up branch that regenerates each
(re-run the conquering recipe from the experiment-log, verify, back up), then
adds the seed + a one-line `SPECS`/`EXPECTED` row. The wiring infrastructure is
ready; only the seeds are missing.

## See also

- [dead-end-p14-dispatch-cli-noop](dead-end-p14-dispatch-cli-noop.md) — the CLI no-op this fixed.
- [float64-ceiling](float64-ceiling.md) — why re-score == rank-current for these.
- `scripts/verify_seed.py` — the emitter + `SPECS` registry.
