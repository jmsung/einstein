---
type: question
author: agent
drafted: 2026-05-02
status: open
asked_by: agent
related_problems: [P11]
related_concepts: [float64-ceiling.md, basin-rigidity.md, contact-graph-rigidity.md, sphere-packing.md, hardin-sloane.md, provable-floor-and-frozen-problems.md]
related_findings: [float64-ceiling.md, basin-rigidity.md]
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

- **Multistart from random configurations** — all converge back to the same contact graph (per `docs/problem-11-tammes.md`). This is not a proof of uniqueness; it is a strong empirical signal of basin-of-attraction dominance.
- **Rotation lottery** — 86/2000 random rotations hit the basin's float64 ceiling. Confirms the basin's ulp-cloud structure but says nothing about *other* basins.
- **Hardin–Sloane reference verification** — confirmed same basin as the leaderboard leader.
- **mpmath 80-digit polish** — confirmed basin's true-math optimum rounds to the leader's score.

What has *not* been done: a directed search for topology-distinct configurations (e.g., contact-graph-mutation moves, edge-flip-then-reoptimize, cross-validation against catalogued sphere codes at adjacent n).

## Hypotheses

- **H1 (uniqueness)**: The Hardin–Sloane contact graph is uniquely optimal for n=50. Evidence: 30-year stability across multiple independent search efforts; the contact graph has high symmetry (5-fold + 4-fold vertex valences match icosahedral-like patterns at this n). Disproof would be a single configuration with strictly larger min-distance and a different contact graph.
- **H2 (alternative topology)**: A topology-distinct optimum exists but lies in a deep basin not reached from random starts or Hardin–Sloane perturbations. Evidence: for some n in the 24–60 range, multiple putative-optimal configurations are catalogued (Sloane's sphere-codes tables list runner-ups). Hardin–Sloane lists *one* configuration per n; the fact that it's tied at the leaderboard does not prove it is unique.
- **H3 (LP/SDP cap)**: There is an LP or SDP dual certificate that bounds Tammes(n=50) from above at the basin's true-math value, analogous to Cohn–Elkies for sphere packings or Levenshtein for kissing numbers. If the bound matches the basin floor, H1 is proven without enumerating topologies.

## Next steps

1. **Catalogue check** — query Sloane's sphere-codes database, Conway–Sloane SPLAG, and any post-2020 large-n Tammes work for *catalogued runner-up* configurations at n=50. Distill any distinct topology to `source/`.
2. **Topology-mutation search** — implement contact-graph edge-flip moves (drop one near-active pair, add another, re-polish on the manifold). Run 1000+ trials warm-started from Hardin–Sloane. If even one trial finds a strictly better score with a different contact graph → H2 confirmed and the basin is escapable.
3. **LP/SDP cap attempt** — formulate the Delsarte-style LP for spherical codes at n=50, solve, compare dual to the basin floor. If dual = floor → H3 confirmed and H1 is proven.
4. **Adjacent-n check** — Hardin–Sloane n=49 and n=51 contact graphs may give hints. If n=49 + 1 vertex inserted "deepens" near n=50 in a way that doesn't recover Hardin–Sloane, an alternative topology family exists.

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
