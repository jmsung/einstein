---
type: question
author: agent
drafted: 2026-05-02
status: open
asked_by: agent
related_problems: [P12]
related_concepts: [float64-ceiling.md, basin-rigidity.md, discretization-as-structure.md, probabilistic-method.md, provable-floor-and-frozen-problems.md]
related_findings: [float64-ceiling.md, discrete-optimization.md]
empirical_h1_supported: true
formal_h1_proven: false
---

# Is the byte-identical SOTA at deg-69 ±1 Littlewood polynomials the unique global optimum?

## Question

For Problem 12 (Flat Polynomials, deg 69, ±1 coefficients on the unit circle, score `max|p(z)| / √71` at 10⁶ sample points), the leaderboard SOTA at `1.2809320528` is **byte-identical across the top 3 agents** (Together-AI, GaussAgent3615, alpha_omega_agents — sha256 prefix `992570de7873`). JSAgent's own MTS independently rediscovered the same configuration. Exhaustive 1-to-4-bit-flip neighborhood search confirms it is a 4-flip local optimum. Seven algebraic constructions (Turyn, Rudin–Shapiro, Fekete, CRT-tensor, Kloosterman, Sidelnikov, period-3) all fail to reach this basin.

**The question**: is this configuration the *unique global optimum* over `{−1, +1}⁷⁰`, or does a structurally distinct ±1 configuration achieve a strictly lower score?

## Why it matters

- The empirical evidence (multi-agent byte-convergence + multi-method rediscovery) is overwhelming for *uniqueness within reach of stochastic search*. But ±1 problems have a known history of algebraically special optima invisible to SA/GA/tabu — the Erdős "ultraflat" conjecture is still open precisely because such optima may exist.
- A formal proof would close P12 as a frozen problem (case b/c in `concepts/provable-floor-and-frozen-problems.md`) and let the agent permanently retire it from the active queue.
- The same uniqueness question shape applies cross-problem: P2 (byte-identical autocorrelation construction), P11 (Hardin–Sloane Tammes basin), P14 (Packomania circle-packing). A general method for "proving uniqueness via dual certificate" would unlock several frozen problems at once.

## What's been tried

- **Stochastic search**: Memetic Tabu Search (1.26 B evaluations, 18 K rounds) independently rediscovered the SOTA. SA (2 M iters × 10 restarts) and GA (200 pop, 500 gens) cannot escape the 1.4 plateau — both converge to inferior basins.
- **Algebraic seeds**: 7 distinct construction families warm-started the search; none lands in the SOTA basin under polish.
- **Local-optimality**: exhaustive 1-to-4-bit-flip search from SOTA confirms it is a 4-flip local optimum. No 1-, 2-, 3-, or 4-flip move improves it.
- **Multi-agent witness**: 3 frontier-AI agents produce byte-identical solutions independently — the canonical lesson #46 byte-identical-SOTA pattern (cf. P2 First Autocorrelation: 8 agents byte-identical at hash `19fdb2925f5f9024`).
- **Spectral equalization** (Remez exchange + log-barrier) — no improvement over SA.
- **Period-3 structured perturbation**: SOTA's first 18 coefficients are `[-1,-1,1]×6`. Fixing this prefix and searching the remaining 52 positions found no improvement — the period-3 pattern is *consequence*, not *cause*, of optimality.

What has *not* been done: an LP/SDP dual certificate (the L4-norm or Mahler-measure analog of Cohn–Elkies for spherical codes), a 5-bit or 6-bit exhaustive flip neighborhood search, or a formal connection to PSL-related binary code theory.

## Hypotheses

- **H1 (uniqueness)**: The byte-identical configuration is the unique global optimum over `{−1, +1}⁷⁰`. Strongest evidence: 3-way byte-convergence from independent agents + JSAgent's MTS rediscovery + 4-flip local optimality. Disproof: a single ±1 sequence with strictly lower `max|p(z)|/√71`.
- **H2 (alternative basin)**: A topologically distinct optimum exists in a deep basin not reached by any tested method. Evidence: Erdős's flat-polynomial conjectures predict ultraflat sequences exist for *all* n, suggesting the search space contains structure unreachable by 4-flip-neighborhood methods. The Mossinghoff (2024) Turyn analysis at adjacent primes hints at families of constructions tied to specific p that may parameterize alternative optima.
- **H3 (LP/SDP cap)**: There is an LP or SDP certificate that bounds `max|p(z)|/√71` from below for any `±1` deg-69 polynomial, matching SOTA's basin floor. Recent work on the L4-norm Mahler-measure variant (Jedwab–Katz–Schmidt 2013) gives related but not directly applicable bounds. The path is: write the L∞-norm lower bound as a moment-of-positive-trigonometric-polynomial SDP, solve, compare to 1.2809.

## Next steps

Ordered by cheapest-informative-move to most-decisive:

1. **Adjacent-degree catalogue check** — Mossinghoff (2024) and Balister et al. (2019) construct flat sequences at all degrees. If their constructions at deg 68 / deg 70 produce different SOTA topologies, that's evidence for an alternative-family at deg 69.
2. **5-bit or 6-bit exhaustive flip search** from SOTA — `C(70,5) = 12 271 512` and `C(70,6) = 131 115 985` neighborhood evaluations, each a 1M-FFT (~10 ms). Tractable on local M5 Max. If 5/6-flip moves all worsen the score, raises empirical confidence; if any improves, H1 collapses.
3. **PSL / cyclotomic factor analysis** — SOTA's `Φ_35` cyclotomic component is the documented spectral bottleneck (`evaluator.phi35_score`). Dissect the SOTA's character against PSL₂(p) representations for relevant primes; check whether the construction is a Φ₃₅-engineered design.
4. **L4-Mahler SDP cap** — write the moment-positivity SDP for the L∞ norm of ±1 polynomials at degree 69, solve via MOSEK or HiGHS dual, compare bound to SOTA. The Cohn–Elkies analog for this problem family.

The cheapest informative move is (1); the most decisive is (4). (2) is the brute-force corroboration of empirical H1; (3) is exploratory and would generate cross-problem wisdom on cyclotomic structure.

## References

- `wiki/concepts/float64-ceiling.md` — byte-identical-SOTA pattern
- `wiki/concepts/provable-floor-and-frozen-problems.md` — three flavors of frozen
- `wiki/findings/float64-ceiling.md` — cross-problem inventory (P2, P11, P12 added 2026-05-02)
- `wiki/findings/discrete-optimization.md` — ILP/BnB experience for ±1 problems
- `cb/source/papers/2024-mossinghoff-turyn-mahler.md` (cited by literature.md)
- `cb/source/papers/2019-balister-flat-littlewood.md` (already in source/)
- Erdős (1957), "Some unsolved problems" — flat-polynomial conjecture
- Jedwab, Katz, Schmidt (2013), "Small L4 norm Littlewood polynomials" (arXiv:1205.0260)
