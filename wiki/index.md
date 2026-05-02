---
type: index
author: human
drafted: 2026-05-02
status: seed
---

# Index

Catalog of all wiki pages. Updated as content lands.

## Entry points

- [home.md](home.md) — narrative front door
- [CLAUDE.md](CLAUDE.md) — wiki contract (machine-readable + prose)
- [log.md](log.md) — append-only ops record

## Concepts

*(populated in Goal 8 — concepts pass)*

## Techniques

*(populated in Goal 7 — techniques pass)*

## Personas

*(populated in Goal 4 — personas pass)*

## Findings

### Arena mechanics
- [findings/arena-api-mechanics.md](findings/arena-api-mechanics.md) — API endpoints, auth, rate limits, submission quirks
- [findings/arena-proximity-guard.md](findings/arena-proximity-guard.md) — minImprovement gate; self-improvement + claim-#1
- [findings/arena-scoring.md](findings/arena-scoring.md) — scoring exploit investigation + fair evaluation proposal

### Recon & warm-start
- [findings/warm-start-recon.md](findings/warm-start-recon.md) — download SOTA first; competitor copying patterns

### Basin analysis
- [findings/float64-ceiling.md](findings/float64-ceiling.md) — float64-ceiling problems; mpmath proof; theoretical-minimum freeze
- [findings/basin-rigidity.md](findings/basin-rigidity.md) — over-constrained Hessian; KKT solve; locking threshold
- [findings/frozen-problem-triage.md](findings/frozen-problem-triage.md) — entry-gate 3-check; magic numbers; saturation
- [findings/equioscillation-escape.md](findings/equioscillation-escape.md) — larger-n escape; equioscillation traps
- [findings/p22-d12-construction-survey.md](findings/p22-d12-construction-survey.md) — D12 kissing landscape

### Optimization techniques
- [findings/packing-techniques.md](findings/packing-techniques.md) — rank-#2 grab; arena-tolerance SLSQP
- [findings/hinge-overlap-rank3-squeeze.md](findings/hinge-overlap-rank3-squeeze.md) — rank-3 squeeze; first-order link tangent
- [findings/sa-parallel-tempering.md](findings/sa-parallel-tempering.md) — SA + tempering; cage diagnostics
- [findings/perturbation-landscape.md](findings/perturbation-landscape.md) — fractal scales; weighted sampling
- [findings/discrete-optimization.md](findings/discrete-optimization.md) — ILP walls; custom BnB; soundness caveats
- [findings/optimizer-recipes.md](findings/optimizer-recipes.md) — Dinkelbach; Adam; bounded L-BFGS; multi-seed BH
- [findings/k-climbing.md](findings/k-climbing.md) — k-climbing; diminishing returns; gate feasibility
- [findings/lp-solver-scaling.md](findings/lp-solver-scaling.md) — LP monotonicity; IPM vs simplex
- [findings/prime-number-theorem-lp.md](findings/prime-number-theorem-lp.md) — P7 is an LP; formulation; dead ends

### Float64 polish & verification
- [findings/float64-polish.md](findings/float64-polish.md) — mpmath; ulp-step; verifier-shift trap
- [findings/polish-race-dynamics.md](findings/polish-race-dynamics.md) — polish race; cron timing; theoretical freeze
- [findings/verification-patterns.md](findings/verification-patterns.md) — two-tier verification; false positives

### Strategy & process
- [findings/strategic-approach.md](findings/strategic-approach.md) — literature first; breadth-before-depth
- [findings/council-dispatch.md](findings/council-dispatch.md) — council convergence; persona trust *(experience finding; the policy lives in `.claude/rules/council-dispatch.md`)*

### Infrastructure
- [findings/infrastructure-discipline.md](findings/infrastructure-discipline.md) — output management; private paths; shared tooling
- [findings/gpu-modal-compute.md](findings/gpu-modal-compute.md) — GIL pitfall; GPU overhead; Modal economics

## Problems

- [problems/_inventory.md](problems/_inventory.md) — concept-coverage compass across 23 problems
- *(per-problem index pages populated in Goal 9 — tracking move)*

## Questions

*(populated as council dispatches and gap-detection cycles run)*

## Source corpus

44 references migrated from mb/wiki/reference/ on 2026-05-02. Layout in `../source/`:

- **papers/** (38) — academic papers, 1959 → 2026
- **arxiv/** (0) — currently empty; future arxiv-direct distillations
- **repos/** (2) — jmsung-einstein, jmsung-einstein-codebase
- **blog/** (4) — togetherai-einstein-arena, cohn-kissing-numbers, bloom-erdos-problems, friedman-packing-records
- **oeis/** (0) — currently empty; reserved for OEIS sequence pages

24 PDFs copied to `../raw/papers/` (gitignored). Originals can be re-fetched from `source_url` in each `source/<provenance>/<stem>.md` frontmatter.
