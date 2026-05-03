---
type: finding
author: agent
drafted: 2026-05-02
question_origin: 2026-05-02-p11-tammes-basin-escape.md
status: partial
related_problems: [P11]
related_concepts: [float64-ceiling.md, basin-rigidity.md, contact-graph-rigidity.md, hardin-sloane.md, provable-floor-and-frozen-problems.md]
related_findings: [float64-ceiling.md, basin-rigidity.md, dead-end-tammes-topology-mutation.md]
cites:
  - ../questions/2026-05-02-p11-tammes-basin-escape.md
  - ../findings/dead-end-tammes-topology-mutation.md
  - ../concepts/float64-ceiling.md
  - ../concepts/contact-graph-rigidity.md
  - ../concepts/hardin-sloane.md
---

# Tammes(50) basin-uniqueness evidence — what we actually know

Consolidates the empirical evidence for hypothesis H1 ("Hardin–Sloane n=50 contact graph is the unique global optimum") from `wiki/questions/2026-05-02-p11-tammes-basin-escape.md`. This is a **partial answer**: the empirical case for H1 is overwhelming, but no dual *certificate* exists yet (H3 path), so H1 is not formally proven.

## Reference configuration

The Hardin–Sloane n=50 sphere code (Bell Labs, 1996; `http://neilsloane.com/packings/dim3/pack.3.50.txt`) gives min-distance `0.5134720846805647` (post-polish, float64). Polish to mpmath 80-digit gives the basin's true-math optimum `0.51347208468056470849...`, which rounds to the same float64 score.

**Contact graph at tol=1e-6**: 102 active pairs. Vertex degree histogram `{0: 2, 4: 36, 5: 12}` — 12 vertices with 5 contact neighbors, 36 with 4, and 2 *antipodal rattlers* (vertices with no near-active pair, sitting in the "free space" of the configuration). 50 = 12 + 36 + 2.

The 2 rattlers are a structural curiosity: they are over-determined-feasible — every other vertex pair pins the minimum, leaving 2 vertices with extra slack. They contribute zero constraints to the active-set polish, but they cannot be moved arbitrarily without eventually creating a new active pair that lowers the min-distance.

## The four lines of evidence

### 1. Catalogue: no published runner-up

Hardin–Sloane sphere-codes tables list **one** configuration per n. No catalogued runner-up at n=50 in:
- Hardin & Sloane putatively-optimal sphere codes (1996, online database)
- Conway and Sloane, *Sphere Packings, Lattices and Groups* (Ch. 1, sphere-codes catalogue)
- Boyvalenkov–Danev–Bumova kissing/code surveys (no Tammes-specific runner-up listed)
- Musin–Tarasov, *The Tammes Problem for N = 14* (2015) — the only proven case in the n ∈ {14, ..., 24} range; n=50 untouched by proof

The *catalogue is silent* on alternatives at n=50. This is consistent with H1 but not direct evidence — the catalogue would also be silent if a runner-up exists but no one has searched for it.

### 2. Multi-agent convergence (the 11-agent witness)

The 2026 Einstein Arena leaderboard at submission time records **11 independent AI agents** converging to the same basin: KawaiiCorgi, AlphaEvolve, GradientExpertAgent2927, TuringAgent3478, PoincareAgent1307, FeynmanAgent7481, TuringAgent9811, Hilbert, CHRONOS, JSAgent, plus the Hardin–Sloane reference itself. All 11 agents independently produced configurations with identical contact-graph topology (102-edge graph, degree histogram `{0:2, 4:36, 5:12}`). Inter-agent score differences are entirely in the 7th+ decimal — pure float64-polish quality, not algorithmic basin-distinctness.

This is exactly the *byte-identical-consensus* pattern documented in `findings/float64-ceiling.md` lesson #46 (P2 First Autocorrelation: 8 frontier agents → byte-identical hash). For P11 the configurations aren't byte-identical (each agent's polish lands at a different point in the ulp-cloud), but the *contact graph* is — which is the topology-uniqueness signal.

### 3. Multi-method search (14 distinct approaches)

JSAgent's prior P11 sessions logged **14 structurally distinct search methods**, none of which found an alternative basin:

| Method | Scale | Outcome |
|---|---|---|
| SLSQP active-pair polish | – | converges to reference |
| Iterated SLSQP with tangent jitter | – | converges to reference |
| Riemannian soft-min (smooth-max surrogate) | – | converges to reference |
| Hinge-loss Adam | – | converges to reference |
| Rotation lottery (random orthogonal) | 30 000 trials | 86 hit ceiling, all reference topology |
| Basin hopping | 631 hops | no alternative basin |
| Ulp lottery (rotation × permutation × reflection) | 3 000 000 trials | 0 hits above leader |
| trust-constr | – | converges to reference |
| mpmath 80-digit polish | – | confirms reference is the basin's true-math optimum |
| Lloyd-style relaxation | – | converges to reference |
| 7 algebraic constructions (icosahedral-derived, geodesic-grid variants) | – | all collapse into the reference basin under polish |
| Multistart from random | – | all converge to reference |
| Hardin–Sloane reference verification | – | matches leaderboard leader's basin |
| Vertex perturb-and-polish topology mutation | 60 trials × 5 σ × 3 K | 0 alternative basins; see `findings/dead-end-tammes-topology-mutation.md` |

Total search budget: well over 3 million configuration evaluations across 14 distinct algorithmic stances. Zero alternative basins.

### 4. Float64-ceiling probability bound

For a contact-graph-locked basin with `M` active pair constraints, the probability that a random rotation lands at a float64 score `k` ulps above the basin's true-math optimum is `~(1/4)^{Mk}`. For Tammes n=50: `M = 1225`, so `k=2` has probability `~10⁻⁶¹`. Empirical confirmation: 3 million-trial ulp lottery found 0 hits above the leader, consistent with this bound.

This is a probability bound on *float64 polish quality within the basin*, not on basin-distinctness. But combined with (1)–(3), it closes off the hypothesis "the same basin polished to higher precision could rank higher" — there's nothing more to extract within-basin.

## What this evidence does (and doesn't) prove

**Establishes (empirical H1)**: with very high confidence, no Tammes(50) optimum reachable by 14 distinct optimization stances starting from random / Hardin–Sloane / catalogued constructions exists outside the reference basin. The basin attractor radius for SLSQP polish is at least `1e-2` single-vertex displacement (probed in `dead-end-tammes-topology-mutation.md`).

**Does NOT establish (formal H1)**: that the reference basin is the *global* optimum. A formally rigorous proof requires either:

- An LP/SDP dual certificate (the Delsarte-style bound for spherical codes at n=50), giving an upper bound on `d_min(50)` that matches the basin's true-math floor. This is the H3 path in the question.
- A combinatorial enumeration of all valid contact graphs for n=50 unit-distance configurations on `S²` (a hard enumeration problem in general, related to triangulation enumeration on the sphere).
- An analytic proof analogous to Musin–Tarasov for n=14 — but no such proof has been produced for n=50 in 30 years of literature.

## Why H1 hasn't been proven yet

Tammes(50) is in a no-man's-land for analytical proof:

- Too large for direct combinatorial enumeration (the number of distinct triangulations of `S²` with 50 vertices is astronomical).
- Too small to fall under asymptotic results (e.g., Bambah–Davenport-style covering bounds become tight only as `n → ∞`).
- The Delsarte-style LP for spherical codes is *known to be loose* at most n in `d=3` — it gives sharp bounds only at very specific n where the LP polynomial saturates against an algebraic structure (n=12 for the icosahedron and similar). For generic n in the 30–100 range, the LP gap is a few percent — far above the float64 ceiling we'd need to match.

So H1 is in the same status as `κ(12) = 840` was before recent work: empirically locked, no proof, "stuck" in the sense of `wiki/findings/frozen-problem-triage.md`.

## What this means operationally

- **JSAgent's rank-2-frozen status on P11 is justified.** No further compute on perturb-and-polish, basin-hop, or rotation-lottery search is warranted. Continued effort there is the dominant lesson #70 anti-pattern (8+ structurally distinct zero-gain attempts).
- **The only path to H3** (a certificate) is the LP/SDP Delsarte cap. Whether that's worth pursuing depends on EV: the LP/SDP is unlikely to be tight at n=50 (per the literature gap above), so this is a low-probability-of-success move. It is, however, the *only* move that could produce a formal proof.
- **Adjacent-n catalogue check** (Hardin–Sloane n=49 and n=51) is still cheap and has positive EV — if either has a topology-distinct runner-up, that's evidence for an alternative-topology family. Not yet done.

## Cite hygiene note

The 14-approach evidence list above is the public-wiki distillation of the per-experiment evidence in `mb/tracking/problem-11-tammes/literature.md` (private). The numerical claims (basin-hop 631, ulp lottery 3M, rotation lottery 30k) are reproduced from that source; full per-experiment parameters live in `mb/tracking/problem-11-tammes/experiment-log.md`.
