---
type: question
author: agent
drafted: 2026-05-27
asked_by: autonomous_loop (cycle 52 attempt 2)
related_problems: [14]
status: open
related_concepts: [float64-ceiling, basin-rigidity, mpmath-precision]
cites:
  - src/einstein/optimizer_manifest.yaml
  - scripts/circle_packing_square/slsqp_polish.py
  - docs/wiki/techniques/mpmath-ulp-polish.md
  - docs/wiki/findings/p14-manifest-wired-slsqp-polish.md
  - docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md
---

# Wire an mpmath-ulp-polish optimizer block into the P14 manifest

## The question

Now that `slsqp_polish` is the strict-tol-safe default for P14
(`docs/wiki/findings/p14-manifest-wired-slsqp-polish.md`) and reproducibly lands
`score=2.6359830849175245`, the next door is **higher-precision arithmetic on the
same basin**. AlphaEvolve's rank-#1 `2.6359830849176` sits ~8e-14 above our floor —
that is sub-float64-ulp territory.

What is the minimal change to wire an `mpmath_polish` optimizer block into
`src/einstein/optimizer_manifest.yaml` for problem 14 that:

1. Reads the canonical SLSQP-floor warm-start (from the in-repo
   `scripts/circle_packing_square/seeds/p14_canonical.json` or the latest
   `slsqp_polish_result.json`),
2. Runs the technique documented in `docs/wiki/techniques/mpmath-ulp-polish.md`
   (typical dps 50–80; per `triple-verify.md` P14 is in the "float-precision-critical"
   family),
3. Emits `{"score": float, "payload": {"circles": [[cx, cy, r] × 26]}}` to
   `results/circle_packing_square/mpmath_polish_result.json`,
4. Triple-verifies the resulting circles under strict tol=0 (mpmath at the chosen
   dps + the existing `evaluate_strict(sol)` + an analytical cross-check)?

## Why this is open

- Cycle 49 of the autonomous loop picked `mpmath-ulp-polish` as the *novel* strategy
  for P14 but found it unwired — recorded as
  `docs/wiki/findings/dead-end-newton-max-strict-tol-lockout-p14.md`. The SLSQP
  wiring (cycles 50–52, finding `p14-manifest-wired-slsqp-polish.md`) resolved the
  default-strict-tol problem but did NOT add mpmath as a separate block.
- Without an mpmath block, the autonomous loop can never explore the sub-ulp
  precision gap to AlphaEvolve's `2.6359830849176` — it dispatches to float64
  SLSQP, reads the float64 ceiling, and converges.
- mpmath-ulp-polish is a high-hit-rate technique (8 tried, 5 top-3, hit_rate 0.62
  per `skill-library.md`) — exactly the kind of mature tool that deserves manifest
  exposure on the problems where it has prior wins.

## What an answer looks like

A concrete diff that:

1. Adds `scripts/circle_packing_square/mpmath_polish.py`:
   - Loads the SLSQP-floor circles (warm-start).
   - At `mpmath.mp.dps=60` (matching the [triple-verify](../../.claude/rules/triple-verify.md)
     suggested range for P5/P6/P11/P14/P17), runs a high-precision local refine
     analogous to `polish.polish()` but in mpmath arithmetic.
   - Round-trips back to float64, runs `evaluate_strict(sol)`, only emits the
     payload if strict tol=0 passes AND the float64 score strictly exceeds
     `2.6359830849175245` (the current strict floor).
   - Otherwise emits the strict floor unchanged (mpmath polish converged within
     float64 ulp).
2. Adds an `mpmath_polish` block to manifest entry 14 with `result_parser:
   json_score_payload`, `timeout_seconds: 1800`.
3. Leaves `default: slsqp_polish` (mpmath is opt-in / used by the autonomous loop
   when the strategy_picker selects it).
4. Adds a minimal test in `tests/circle_packing_square/test_p14_mpmath_polish.py`
   that asserts strict-tol=0 verification and score ≥ SLSQP floor.

## Expected outcome (honest)

Probably no improvement. AlphaEvolve's `2.6359830849176` is one bit-flip above our
floor — the basin is documented as float64-ceiling. The expected value of wiring
mpmath is:

- **Positive case (~10%)**: A different round-off pattern at dps=60 settles into a
  circles configuration that float64-rounds to a `2.6359830849176`-class layout
  (matching AE within minImprovement). This would be a verifiable rank-#1 grab.
- **Negative case (~90%)**: mpmath-polish converges to the same floor at higher
  precision — proof that the basin truly is locked, generates a
  `dead-end-mpmath-cannot-cross-p14-floor.md` finding ruling out
  "higher-precision-only" attacks on this class of arena-tied packing problems.
  This rules-out finding is itself valuable (transferable to P17/P18).

Either way, the manifest gains a high-hit-rate strategy slot the autonomous loop
can actually invoke.

## Why not just run mpmath ad-hoc from scratch/

Same reason `slsqp_polish` was wired structurally rather than left as a one-off
script: the autonomous loop's strategy_picker dispatches by manifest, not by
"agent remembers the right script." Without the manifest entry, the technique
is invisible to the loop forever, and the skill-library counters never
increment from automated invocations.

## Cross-refs

- [p14-manifest-wired-slsqp-polish](../findings/p14-manifest-wired-slsqp-polish.md) — the SLSQP wiring this builds on
- [dead-end-newton-max-strict-tol-lockout-p14](../findings/dead-end-newton-max-strict-tol-lockout-p14.md) — cycle-49 origin
- [techniques/mpmath-ulp-polish](../techniques/mpmath-ulp-polish.md) — the technique to wrap
- [triple-verify](../../../.claude/rules/triple-verify.md) — dps=60 floor for P14
- [float64-ceiling](../concepts/float64-ceiling.md)

## Suggested sources

*Auto-suggested by `docs/tools/gap_search.py` — arxiv query: `(all:"float64 ceiling" OR all:"basin rigidity" OR all:"Wire an mpmath-ulp-polish optimizer block into") AND (cat:math.NT OR cat:math.CO OR cat:math.OC OR cat:math.MG OR cat:math.PR OR cat:math.CA OR cat:math.NA)`*

Review and `/wiki-ingest <arxiv-url>` any that look relevant. If none fit, close the question with `status: superseded` and a one-line explanation.

*(no results; broaden the search terms or query the web)*
