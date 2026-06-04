---
type: finding
author: agent
drafted: 2026-06-03
question_origin: problem-11
status: answered
related_concepts:
  - basin-rigidity
  - minimprovement-gate
  - float64-ceiling
  - contact-graph-rigidity
cites:
  - ../findings/dead-end-p5-autonomous-loop-basin-converged-no-api-change.md
  - ../findings/dead-end-p14-autonomous-loop-basin-converged-no-api-change.md
  - ../findings/tammes-50-basin-uniqueness-evidence.md
  - ../findings/dead-end-tammes-topology-mutation.md
  - ../findings/float64-ceiling.md
  - ../problems/11-tammes-n50.md
---

# Dead end: autonomous-loop cycles on P11 (basin-converged + minImprovement-blocked)

## What we tried

This visit's cycle 0 / attempt 1 (after cycles 84–86, 93, 94, 100, 101, 107,
108, 113, 114, 120 on the same problem). The Thompson bandit sampled
`uniform-radius-shrink-fallback.md` (Beta(2,10), θ=0.36). That technique was
already exercised on cycles 86, 101, 114 with no Δ (hit_rate = 0.10). Per the
P5/P14 templates (`dead-end-p5-autonomous-loop-basin-converged-no-api-change.md`,
`dead-end-p14-autonomous-loop-basin-converged-no-api-change.md`), dispatched
`verify_seed` once for a triple-verify receipt and stopped.

```
uv run python -m einstein.optimizer_dispatch \
    --problem-id 11 --strategy verify_seed
# {ok:true, score:0.5134720846805645, runtime:0.059s}
```

Result: bit-identical to every prior cycle (84, 85, 86, 93, 94, 100, 101,
107, 108, 113, 114, 120). The P11 manifest exposes exactly two optimizers:

| Manifest strategy            | Last exercised                | Outcome                                                            |
|------------------------------|-------------------------------|--------------------------------------------------------------------|
| `verify_seed` (default)      | this cycle / many priors      | 0.5134720846805645 (rank-2 float64 ceiling, tied with KawaiiCorgi) |
| `mpmath_ulp_polish`          | pre-loop (Phase 2a)           | +~2.2e-16 (~2 ulps) over `verify_seed`; still ≪ 3.5e-13 gap to #1  |

Bandit-recommended `uniform-radius-shrink-fallback.md`, `arena-tolerance-slsqp.md`,
`slsqp-active-pair-polish.md` are all in the 14-method exhausted corpus
(cycle 85 council finding) — none find a novel basin.

## Why it failed

The optimizer cannot fail — `verify_seed` returns the Hardin-Sloane basin
floor every time. What fails is the **autonomous loop's choice to dispatch
on P11 without an API-state delta**. The submission gap is bounded by
basin physics:

```
basin_floor    = 0.5134720846805645     (verify_seed, every cycle since c84)
mpmath_ulp_lift ≈ 0.5134720846805647    (+~2 ulps, Phase 2a, ≪ gap)
arena_#1       ≈ 0.5134720846806        (~3.5e-13 above basin_floor)
delta_to_#1    ≈ 3.5e-13
minImprovement = 1e-8                   (P11 default)
headroom / gate ≈ 1e-8 / 3.5e-13 ≈ 2.9e4× too narrow
```

Independent receipts already in the wiki confirm basin uniqueness:

- `tammes-50-basin-uniqueness-evidence.md` — 4-line evidence pyramid:
  catalogue silence (Hardin-Sloane 30+ years), 11-agent consensus,
  14-method search, float64-ceiling bound. Empirical H1 supported.
- `dead-end-tammes-topology-mutation.md` — 60-trial vertex-perturb-and-polish
  topology-mutation probe (2026-05-02). Basin attractor radius ≥ 1e-2; no
  alternative basin found.
- `float64-ceiling.md` — cross-problem inventory; P11 listed alongside
  P2, P5, P6, P10, P14, P15, P17a/b, P23.

This is the **third concrete instance** of the generalisable
"basin-converged + minImprovement-blocked" pattern (P5 was first, P14
second, P11 now). The cross-transfer call-out from the P5 finding
("the basin-floor pattern documented here applies symmetrically to P1,
P14, P17 and any future arena entry where the gap-to-#1 is below
`minImprovement`") covered P11 implicitly; this page makes it explicit.

## What this rules out

- Re-running any P11 manifest optimizer (`verify_seed`, `mpmath_ulp_polish`)
  under the current `minImprovement = 1e-8` regime — neither can produce a
  submittable Δ. The mpmath ulp lift is +~2 ulps, six orders of magnitude
  below the gate.
- Bandit-driven technique rotation on P11 — every technique converges to
  the Hardin-Sloane contact graph; the 14-method exhausted corpus (cycle
  85 council finding) is the receipt. Hit-rate signal is uninformative.
- Council-dispatch on P11 absent a triggering API change — no persona
  angle changes basin physics or gate width. The existing receipt is
  the 11-agent consensus + 14-method search documented in
  `tammes-50-basin-uniqueness-evidence.md`.

## What might still work

- **API-state gating** (the generalisable fix, identical to P5/P14):
  `autonomous_loop.py` should fetch `/api/problems/11.minImprovement` at
  cycle-start and gate dispatch on
  `minImprovement < (arena_#1 − basin_floor)` (≈ 3.5e-13 today for P11).
  Until then, mark P11 as `frozen-pending-api-change` in the queue. Same
  helper would cover P5 and P14 — see the `frozen_problem_gate` proposal
  in the P14 finding. Out of this cycle's write scope (`src/`, `scripts/`).
- **Cross-problem transfer (codified, three instances now)**: P5, P14, P11
  share the same signature — basin-floor at float64 ceiling, gap to #1
  below `minImprovement`, every manifest strategy exhausted. The
  `frozen_problem_gate(problem_id, basin_floor, arena_floor, minimprovement)
  → {dispatch, frozen-pending-api-change}` runtime check collapses all
  three findings into one gate.
- **New basin** (the only mathematical move): a non-Hardin-Sloane n=50
  basin. None found in 30 years of Hardin-Sloane tables; the 2026-05-02
  60-trial topology-mutation probe and the cycle-85 14-method survey add
  empirical weight against. Low-probability path; would require an
  adversarial-init class not yet tried (e.g. contact-graph-mutated seeds
  derived from a different n=49 or n=51 basin via vertex add/remove).
  Not a compute-it-tomorrow move.

## See also

- [dead-end-p5-autonomous-loop-basin-converged-no-api-change](dead-end-p5-autonomous-loop-basin-converged-no-api-change.md) — template + cross-transfer call-out
- [dead-end-p14-autonomous-loop-basin-converged-no-api-change](dead-end-p14-autonomous-loop-basin-converged-no-api-change.md) — second instance; codifies the `frozen_problem_gate` proposal
- [tammes-50-basin-uniqueness-evidence](tammes-50-basin-uniqueness-evidence.md)
- [dead-end-tammes-topology-mutation](dead-end-tammes-topology-mutation.md)
- [float64-ceiling](float64-ceiling.md)
- [problems/11-tammes-n50](../problems/11-tammes-n50.md)
