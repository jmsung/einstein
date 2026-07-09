---
type: source
kind: paper
title: "Large N limit of irreducible tensor models: O(N) rank-3 tensors with mixed permutation symmetry"
authors: Sylvain Carrozza
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.02496
source_local: ../raw/2018-carrozza-large-limit-irreducible-tensor.pdf
topic: general-knowledge
cites:
---

# Large N limit of irreducible tensor models: O(N) rank-3 tensors with mixed permutation symmetry

**Authors:** Sylvain Carrozza  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.02496

## One-line
Proves that the third (mixed-symmetry $S_3$) irreducible $O(N)$ rank-3 tensor representation admits a melonic large-$N$ expansion, completing the irreducible-rank-3 classification.

## Key claim
For a real rank-3 tensor projected onto the two-dimensional mixed-symmetry $S_3$ representation (Young tableau $\tableau{1 2}{3}$) with quartic "tetrahedral" interaction at 't Hooft scaling $\lambda/(4N^{3/2})$, the connected two-point function converges in the large-$N$ limit to the melonic two-point function: $\langle T_{abc} T_{a'b'c'}\rangle_c = (K_0(\lambda) + O(1/\sqrt N))\, P_{abc,a'b'c'}$, where $K_0 = 1 + \lambda^2 K_0^4/12$.

## Method
Builds the orthogonal projector $\tilde P = \tfrac{3}{4} S S^\top$ onto the irreducible subspace (Young symmetrizer composed with traceless projection) as the propagator, removing trace/vector modes that otherwise generate "bad-tadpole" $\sim N^{p/2}$ chains. Expands amplitudes over Feynman maps decomposed into $10^{2V}$ stranded-graph configurations with degree $\omega(G) = 3 + \tfrac{3}{2}V + B - F$; resums the melon-tadpole family via a Schwinger-Dyson equation $K = 1 + \lambda f_T(N) K^2 + \lambda^2 f_M(N) K^4$. Then uses Proposition 1 of Benedetti-Carrozza-Gurau-Kolanowski (no melon/tadpole $\Rightarrow \omega \geq 0$; no generalized melon/tadpole $\Rightarrow \omega \geq 1/2$) to isolate melon dominance.

## Result
Tadpole contribution $f_T(N) = (N-2)(2N+1)/(2N^{3/2}(N-1))$ vanishes as $N \to \infty$; melon contribution $f_M(N) \to 1/12$. The leading large-$N$ two-point function is governed purely by melonic diagrams, satisfying the same algebraic equation $K_0 = 1 + \lambda^2 K_0^4/12$ as the symmetric-traceless and antisymmetric sectors. Combined with [1] this closes the proof for all three irreducible rank-3 $O(N)$ tensor sectors.

## Why it matters here
General background; no direct arena tie. Mathematical adjacency only — irreducible-representation decomposition under $S_n \times O(N)$ and Young-symmetrizer projection are tools that occasionally appear in extremal combinatorics / SDP flag-algebra contexts, but the paper itself is 0-d QFT and unrelated to the 23 arena problems.

## Open questions / connections
- Conjecture: extends to higher-rank $r \geq 4$ irreducible tensors with complete $(r+1)$-valent interaction — explicit proof open.
- Alternative route via introducing independent 't Hooft couplings for trace/vector modes could yield mixed melonic+bubble large-$N$ limits (vector-tensor hybrids).
- Methods transfer to $d \geq 1$ tensor field theories: yields integro-differential Schwinger-Dyson rather than algebraic, analogous to SYK and Klebanov-Tarnopolsky models.

## Key terms
tensor models, large N expansion, melon diagrams, melonic limit, irreducible representation, Young tableau, mixed permutation symmetry, S3 representation, O(N) symmetry, Schwinger-Dyson equation, SYK model, trace instability, stranded graph, Feynman map, 't Hooft coupling
