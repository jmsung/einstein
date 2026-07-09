---
type: finding
author: agent
drafted: 2026-06-08
question_origin: knowledge/wiki/questions/2026-06-01-p14-ae-tied-seed-mpmath-polish.md
status: answered
related_problems: [14]
related_concepts: [float64-ceiling, basin-rigidity, mpmath-ulp-polish, n-agent-tie-not-global-min]
cites:
  - mb/problems/14-circle-packing-square/solutions/solution-AE-tied-rank2.json
  - knowledge/wiki/findings/mpmath-ulp-polish-dual-gate-p14.md
  - scripts/circle_packing_square/mpmath_ulp_polish.py
---

# P14 AE-tied seed is at its basin's float64 ceiling — ulp polish nets zero

## The question (closes 2026-06-01)

Does `mpmath_ulp_polish` from the archived AE-tied seed reveal more sub-ulp
slack than it did from our rank-2 seed (cycle 53: +6.617e-14)?

## The answer

**No.** Running the dual-gated ulp coordinate descent at `--dps 80 --max-iter 100`
from `solution-AE-tied-rank2.json` accepted 6 ulp moves over 3 sweeps that
net to **Δ = 0.000e+00** at float64 sum precision.

| Quantity | Value |
|---|---|
| Seed strict-tol Σr (arena f64) | 2.6359830849176076 |
| After ulp polish (dual-gate) | 2.6359830849176076 |
| Float64 Δ | 0.000e+00 |
| Accepted ulp moves | 6 (over 3 full sweeps) |
| Compute | ~30s, dps=80 |

Compare with cycle 53's run from the rank-2 seed `p14_canonical.json`
(2.6359830849175245 → 2.6359830849175907, Δ +6.617e-14): the rank-2 seed
had SLSQP line-search residual to reclaim; the AE-tied seed does not.

## What this rules out

The hypothesis that AE's submitted #1 is line-search-residual-above-ceiling
(i.e. that AE submits without ulp polish). At least at the float64 sum
resolution accessible to dual-gated ulp coordinate descent at dps=80, the
AE-tied seed sits at its basin's true float64 ceiling. 6 ulp accepts that
cancel in the float64 sum is the signature of a configuration whose
binding active set is already saturated — every gain a coordinate move
produces in one direction is balanced by a loss elsewhere.

## What this confirms

1. **AE's optimizer discipline is high** on packing problems — the seed AE
   published is already at its basin's float64 ceiling.
2. **The 1.7e-14 gap between AE-tied (2.6359830849176076) and our
   rank-2-polished (2.6359830849175907)** is real and persistent — both
   strict-tol-feasible, distinct float64-quantization vertices of the SAME
   basin (per the 10-approach parallel survey from 2026-04-08/09).
3. **The proximity-guard rule that blocked submitting AE-tied in 2026-04 was
   correct** — display-tied with AE#1 (`2.6359830849176`) at arena display
   precision; the +6.7e-15 over display would not pass arena's
   `minImprovement=1e-7` strict-improvement gate.

## What might still work (next-door operator candidates)

The basin's f64 ceiling on P14 is now characterised on both seeds we hold.
Further wisdom gains require either:

- **A genuinely different basin** (no 10-approach evidence of one exists).
- **A dual certificate** (Cohn–Elkies-style LP/SDP bound matching 2.6359...)
  proving the basin IS the global optimum — would close the wall-ledger row
  permanently and let the autonomous loop stop attempting P14.
- **mpmath polish at much higher dps** (e.g. dps=200) testing whether the
  6-ulp cancellation hides a deeper move — almost certainly no
  (cancellation pattern at dps=80 is already past float64 representability).

No new compute-only attack is in scope. The honest move on P14 is
**stop attempting** until a dual certificate is built — file as a research
direction at the concepts layer if pursued.

## Generalises to

The same one-line check (mpmath polish from archived AE-tied seeds, dual-gate)
applies on every float64-ceiling problem with an archived AE-tied seed —
P5/P11/P17/P18/P22/P23. If they all return Δ=0, "AE polishes to float64 ceiling"
is a cross-problem regularity worth promoting to a concept.

## Reproduction

```bash
uv run python scripts/circle_packing_square/mpmath_ulp_polish.py \
  --seed mb/problems/14-circle-packing-square/solutions/solution-AE-tied-rank2.json \
  --dps 80 --max-iter 100 \
  --output /tmp/p14_ae_tied_ulp_result.json
```

Deterministic, ~30s. Result file held at `/tmp/`; not promoted to
`mb/.../solutions/` because Δ=0 produces no new artifact (identical to seed).
