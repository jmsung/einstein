---
type: question
author: agent
drafted: 2026-05-02
status: open
asked_by: agent
related_problems: [P11]
related_concepts: [float64-ceiling.md, basin-rigidity.md, contact-graph-rigidity.md, sphere-packing.md, hardin-sloane.md, provable-floor-and-frozen-problems.md]
related_findings: [float64-ceiling.md, basin-rigidity.md, tammes-50-basin-uniqueness-evidence.md, dead-end-tammes-topology-mutation.md]
partial_answer: ../findings/tammes-50-basin-uniqueness-evidence.md
empirical_h1_supported: true
formal_h1_proven: false
---

# Is the Hardin–Sloane n=50 contact graph the global Tammes(50) optimum, or does a topology-distinct configuration exist?

## Question

For Tammes n=50 the Hardin–Sloane 1996 configuration appears to be the global optimum: every leaderboard agent converges to it modulo ulps, and JSAgent is rank #2 tied at score `0.513472084680564` (2 ulps below KawaiiCorgi #1). The basin is contact-graph-locked with `M = 1225` active pair constraints; probability of beating by `k` ulps via random rotation is `~(1/4)^{Mk} ≈ 10⁻⁶¹` for `k=2`.

**The question**: is there a *topology-distinct* configuration (different contact graph; different active-pair multiset; different vertex-degree sequence) that achieves a strictly better minimum pairwise distance? Or can we prove the Hardin–Sloane contact graph is the unique optimal topology?

## Why it matters

- If a distinct topology exists, P11 is winnable with a structurally new approach — escape the basin instead of polishing inside it.
- If no distinct topology exists, P11 is provably frozen (case b in `concepts/provable-floor-and-frozen-problems.md`) and the rank-2 freeze is the endgame; further compute is wasted.
- Either answer is wisdom that generalizes — the same topology-uniqueness question applies to P14, P17a, P17b, P22, P23, and any sphere-codes problem at fixed n.

## What's been tried

The full 14-approach evidence pyramid is consolidated in [`findings/tammes-50-basin-uniqueness-evidence.md`](../findings/tammes-50-basin-uniqueness-evidence.md). Highlights:

- **Catalogue check (1)** — Hardin–Sloane sphere-codes tables, Conway–Sloane SPLAG, Boyvalenkov surveys, Musin–Tarasov 2015. **Result**: no published runner-up at n=50. Catalogue is silent.
- **Multi-agent convergence (2)** — 11 independent arena AI agents (KawaiiCorgi, AlphaEvolve, GradientExpertAgent2927, TuringAgent3478, PoincareAgent1307, FeynmanAgent7481, TuringAgent9811, Hilbert, CHRONOS, JSAgent, plus Hardin–Sloane reference) all converge to the same 102-edge contact graph with degree histogram `{0:2, 4:36, 5:12}`.
- **14 distinct optimization stances (3)** — SLSQP, iterated SLSQP, Riemannian soft-min, hinge Adam, rotation lottery (30 000 trials), basin hopping (631 hops), ulp lottery (3 000 000 trials), trust-constr, mpmath 80-digit, Lloyd, 7 algebraic constructions, multistart, Hardin–Sloane comparison, and 2026-05-02 vertex-perturb topology mutation (60 trials). **All 14 converge to the reference basin.**
- **Float64-ceiling bound (4)** — `M = 1225` active pair constraints; probability of beating leader by `k` ulps is `~(1/4)^{Mk}`, giving `~10⁻⁶¹` for `k=2`. Empirically confirmed by 3 M-trial ulp lottery → 0 hits.
- **Topology-mutation probe** ([dead-end finding](../findings/dead-end-tammes-topology-mutation.md)) — 60 trials at σ ∈ {1e-3 … 1e-1} × K ∈ {1, 3, 10}. Basin attractor radius confirmed ≥ 1e-2; σ ≥ 5e-2 escapes the basin but the polish lands in degenerate 1-pair saddles 9–23 % below Tammes. Search budget too narrow to be alone-sufficient; corroborates the prior 14-approach corpus.

**Empirical H1 status**: overwhelming. **Formal H1 status**: not proven.

What has *not* been done: LP/SDP Delsarte cap (the only path to a formal certificate), adjacent-n catalogue check (n=49, n=51 — cheap, residual EV).

## Hypotheses

- **H1 (uniqueness)**: The Hardin–Sloane contact graph is uniquely optimal for n=50. Evidence: 30-year stability across multiple independent search efforts; the contact graph has high symmetry (5-fold + 4-fold vertex valences match icosahedral-like patterns at this n). Disproof would be a single configuration with strictly larger min-distance and a different contact graph.
- **H2 (alternative topology)**: A topology-distinct optimum exists but lies in a deep basin not reached from random starts or Hardin–Sloane perturbations. Evidence: for some n in the 24–60 range, multiple putative-optimal configurations are catalogued (Sloane's sphere-codes tables list runner-ups). Hardin–Sloane lists *one* configuration per n; the fact that it's tied at the leaderboard does not prove it is unique.
- **H3 (LP/SDP cap)**: There is an LP or SDP dual certificate that bounds Tammes(n=50) from above at the basin's true-math value, analogous to Cohn–Elkies for sphere packings or Levenshtein for kissing numbers. If the bound matches the basin floor, H1 is proven without enumerating topologies.

## Next steps

Ordered by cheapest-informative-move to most-decisive:

1. **Catalogue check** *(cheapest, highest-leverage on a positive find)* — query Sloane's sphere-codes database, Conway–Sloane SPLAG, and any post-2020 large-n Tammes work for *catalogued runner-up* configurations at n=50. Distill any distinct topology to `source/`. If literature has a runner-up, the question collapses immediately to "verify against the runner-up."
2. **Adjacent-n check** — Hardin–Sloane n=49 and n=51 contact graphs may give hints. If n=49 + 1 vertex inserted "deepens" near n=50 in a way that doesn't recover Hardin–Sloane, an alternative topology family exists.
3. **Basin-hopping with topology-mutation operator** *(direct H2 test; ~1k–10k hops)* — replace single-shot perturb-and-polish with a Metropolis chain over polished configurations, tabu the reference signature so the chain is forced to explore. Required to upgrade the partial-answer in `findings/dead-end-tammes-topology-mutation.md` from "no alternative basin within single-step reach" to "no alternative basin within Markov-chain reach."
4. **LP/SDP cap attempt** *(most decisive — produces a certificate)* — formulate the Delsarte-style LP for spherical codes at n=50, solve, compare dual to the basin floor. If dual = floor → H3 confirmed and H1 is *proven* without enumerating topologies. This is the path used by Cohn–Elkies for sphere packing and Levenshtein for kissing numbers.

## References

- `wiki/concepts/float64-ceiling.md`
- `wiki/concepts/basin-rigidity.md`
- `wiki/concepts/contact-graph-rigidity.md`
- `wiki/concepts/hardin-sloane.md`
- `wiki/concepts/sphere-packing.md`
- `wiki/findings/float64-ceiling.md` (cross-problem inventory)
- `wiki/problems/11-tammes-n50.md`
- Hardin–Sloane sphere codes — `http://neilsloane.com/packings/dim3/pack.3.50.txt`
- Conway and Sloane, *Sphere Packings, Lattices and Groups* (Ch. 1, sphere-codes catalogue)
- Musin and Tarasov, *The Tammes Problem for N = 14* (Experimental Mathematics, 2015) — only proven case in this n-range
