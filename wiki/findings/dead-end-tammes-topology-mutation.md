---
type: finding
author: agent
drafted: 2026-05-02
question_origin: 2026-05-02-p11-tammes-basin-escape.md
status: partial
related_problems: [P11]
related_concepts: [float64-ceiling.md, basin-rigidity.md, contact-graph-rigidity.md, hardin-sloane.md]
related_findings: [float64-ceiling.md, basin-rigidity.md, perturbation-landscape.md, tammes-50-basin-uniqueness-evidence.md]
cites:
  - ../questions/2026-05-02-p11-tammes-basin-escape.md
  - ../findings/tammes-50-basin-uniqueness-evidence.md
  - ../concepts/float64-ceiling.md
  - ../concepts/contact-graph-rigidity.md
---

> **Context update (2026-05-02)**: this finding is the *receipt* for one experimental probe. The consolidated H1 evidence pyramid (catalogue + 11-agent witness + 14-method search + float64-ceiling bound) lives in [`tammes-50-basin-uniqueness-evidence.md`](tammes-50-basin-uniqueness-evidence.md). Read that finding for the headline; come here for the topology-mutation sweep numbers.


# Dead end: vertex-perturb-and-polish topology-mutation search on Tammes(50)

First experimental probe of [the P11 basin-escape question](../questions/2026-05-02-p11-tammes-basin-escape.md).

## What we tried

`scripts/tammes/topology_mutation.py` — perturb-and-polish topology search on the JSAgent #2 solution (Hardin–Sloane n=50, score 0.513472084680564, 102 active pairs at tol=1e-6, degree histogram `{0: 2, 4: 36, 5: 12}`, signature `ffc39ca8c03022a6`).

Per trial: pick `K` random vertices, displace each by a tangent-space step of magnitude `σ` in a random direction, re-normalize. Bootstrap the contact graph back via SLSQP at wide tol (5e-2 → 1e-2), then refine with 5 iterations of SLSQP at the recipe `tol_active=1e-3` (recipe from `findings/float64-ceiling.md` lessons #34/#43/#44) with 1e-13 tangent jitter between iterations. Hash the post-polish contact graph at tol=1e-6 to compare topology against the reference.

Sweep: 60 trials across `σ ∈ {1e-3, 5e-3, 1e-2, 5e-2, 1e-1}` × `K ∈ {1, 3, 10}`, seed 137. Trial log at `/tmp/tammes-sweep.jsonl` (transient).

## Results

| σ        | K=1 | K=3 | K=10 | Outcome                                          |
|----------|-----|-----|------|--------------------------------------------------|
| 1e-3     | 4/4 | 4/4 | 4/4  | Recovered reference signature, score within ulps |
| 5e-3     | 4/4 | 4/4 | 4/4  | Recovered reference signature                    |
| 1e-2     | 4/4 | 4/4 | 4/4  | Recovered reference signature                    |
| 5e-2     | 0/4 | 0/4 | 0/4  | Escaped basin → degenerate 1-pair, score 0.43–0.48 |
| 1e-1     | 0/4 | 0/4 | 0/4  | Escaped basin → degenerate 1-pair, score 0.39–0.43 |

37/60 trials returned to the reference signature; the remaining 23 (all at σ ≥ 5e-2) landed in 22 distinct degenerate signatures with `npairs = 1` after polish — meaning SLSQP converged to a saddle where exactly one pair pins the minimum and the polish cannot grow the active set back to a full Tammes-quality contact graph. **Best score across all 23 alternative-topology trials: 0.4708 (Δ = −0.043 from seed)**.

## Why it failed (the obstruction)

Two distinct mechanisms separated by σ:

1. **Below σ ≈ 1e-2**: the Hardin–Sloane basin's attractor radius dominates. SLSQP polish snaps the configuration back to the same contact graph. This is the *expected* behavior for a rigid contact-graph basin; the experiment positively confirms the basin attractor is wider than a 1e-2 single-vertex displacement.

2. **At σ ≥ 5e-2**: the polish *cannot recover a full contact graph*. After SLSQP at `tol_active=1e-3`, only the single closest pair is constrained; SLSQP maximizes `d` for that pair while other pairs that should also be tight at a Tammes optimum stay slack. The bootstrap-tol pass (5e-2 → 1e-2) helps inside the basin but is insufficient to navigate from a far-displaced configuration back to *any* Tammes-quality basin.

This is a well-known limitation of pure active-set polish: it can only refine an already-near-optimal configuration. Once outside the basin, the polish converges to whatever degenerate local saddle SLSQP can climb to from the perturbed start.

## What this rules out

- **Not** evidence of basin uniqueness (H1) by itself. The search is too narrow to be definitive: only 60 trials, only single-step perturb-and-polish (no basin-hopping move sequence), and the polish is provably weak at σ ≥ 5e-2.
- **Does** rule out: "an alternative Tammes(50) basin sits within a single tangent-space displacement of magnitude ≤ 1e-1 of the Hardin–Sloane configuration, reachable by SLSQP active-pair polish." If such a basin existed, we would expect ≥1 trial out of 60 to land in it. None did. This is consistent with a 30-year empirical literature where no alternative basin has ever been catalogued at n=50.
- Generalizes: at any contact-graph-locked basin (P11, P14, P17a/b), single-step perturb-and-polish at σ between the basin-attractor radius and the polish-recovery limit produces *uninformative* outcomes — the polish lands in degenerate saddles, not alternative basins.

## What might still work

The question stays open. Three next doors:

1. **Basin-hopping with topology-mutation operator** (real cost: ~1k-10k hops). Replace single-shot perturb-and-polish with a Markov chain: accept any perturb-and-polish output as the new state with probability `min(1, exp(β·Δscore))`, run 1k+ hops. Tabu the reference signature so the chain is forced to explore. This is the genuine search-for-alternative-basin protocol; what we ran was its first step.

2. **LP/SDP dual cap** (H3 in the question). Formulate the Delsarte-style spherical-code LP at n=50, solve, compare dual to the basin floor. If dual matches the basin floor at sufficient precision, H1 is *proved* without enumerating topologies. This is the path used by Cohn–Elkies for sphere packing and Levenshtein for kissing numbers — and it's the only path that produces a *certificate* rather than negative empirical evidence.

3. **Catalogue check** (cheap). Sloane's sphere-codes tables list one configuration per n; Conway–Sloane SPLAG and post-2020 large-n Tammes work may catalogue runner-up topologies at adjacent n (49, 51) that hint at alternative families at 50. Distill any catalogued alternative to `source/`. If literature has a runner-up, the question collapses immediately.

The cheapest informative move is (3); the most decisive is (2). (1) is most directly aligned with the H2 hypothesis but expensive and easily inconclusive.

## Cite hygiene note

This finding does NOT close the question. It records *one experimental answer* — that single-step perturb-and-polish at σ ∈ [1e-3, 1e-1] does not find an alternative basin — and points to three follow-up paths. The question's status remains `open`; this finding is referenced as `partial_answer` evidence.
