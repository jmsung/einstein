---
type: source
kind: paper
title: Sparse sums of squares on finite abelian groups and improved semidefinite lifts
authors: Hamza Fawzi, J. Saunderson, P. Parrilo
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1503.01207
source_local: ../raw/2015-fawzi-sparse-sums-squares-finite.pdf
topic: general-knowledge
cites:
---

# Sparse sums of squares on finite abelian groups and improved semidefinite lifts

**Authors:** Hamza Fawzi, J. Saunderson, P. Parrilo  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1503.01207

## One-line
Gives a combinatorial (chordal-cover) sufficient condition under which Fourier-sparse nonnegative functions on a finite abelian group admit Fourier-sparse sum-of-squares certificates, yielding small SDP lifts of cut and cyclic polytopes.

## Key claim
For $G$ finite abelian and $S \subseteq \widehat G$, any nonnegative function with Fourier support $S$ is a sum of squares of functions supported on $T(\Gamma,\{\chi_C\}) = \bigcup_C \chi_C C$, where $\Gamma$ is any chordal cover of the Cayley graph $\mathrm{Cay}(\widehat G, S)$ and $\chi_C \in \widehat G$ are arbitrary translations of its maximal cliques $C$.

## Method
Three-step construction: (1) sparse Gram matrix — a nonneg function $S$-supported has an SOS Gram matrix sparse on $\mathrm{Cay}(\widehat G, S)$; (2) chordal completion — apply the Grone–Johnson–Sá–Wolkowicz / Griewank–Toint decomposition to split the Gram matrix into PSD pieces supported on maximal cliques of a chordal cover $\Gamma$; (3) character translation — multiply each clique-supported square $|h|^2$ by a character $\chi_C$ (preserving $|h|^2$) to shift cliques into a common small target $T$. Dual view: $T$-sized Hermitian PSD lift of the moment polytope $M(G,S)$ via chordal matrix completion (Theorem 6).

## Result
Two applications. (i) **Boolean hypercube** $G = \mathbb{Z}_2^n$: any nonnegative quadratic on $\{-1,1\}^n$ is SOS of polynomials of degree $\le \lceil n/2 \rceil$, proving Laurent's 2003 conjecture and showing the $\lceil n/2 \rceil$ Lasserre level for $\mathrm{CUT}_n$ is exact (tight). (ii) **Cyclic group** $G = \mathbb{Z}_N$ with $d \mid N$: nonneg functions of degree $\le d$ admit SOS supported on $|T| \le 3 d \log(N/d)$ Fourier modes; equivalently the trigonometric cyclic polytope $TC(N,2d) \subset \mathbb{R}^{2d}$ has a Hermitian PSD lift of size $\le 3 d \log(N/d)$ (real lift $\le 4 d \log(N/d)$). Setting $N = d^2$ gives the first explicit family $(P_d)$ with $\mathrm{xc}_{\mathrm{PSD}}(P_d)/\mathrm{xc}_{\mathrm{LP}}(P_d) = O(\log d / d)$, since $d$-neighborliness forces $\mathrm{xc}_{\mathrm{LP}} \ge \Omega(d^2)$ while $\mathrm{xc}_{\mathrm{PSD}} = O(d \log d)$.

## Why it matters here
Directly relevant to SDP/Lasserre-hierarchy machinery used in arena problems with finite-group symmetry (autocorrelation/Fourier problems on $\mathbb{Z}_N$, boolean-quadratic problems, extremal-graph / cut-type problems): chordal-cover + character-translation is a constructive recipe for shrinking SDP lifts when the Cayley graph is sparse. Connects to existing wiki concepts (Lasserre hierarchy, LP/SDP duality, equioscillation-adjacent Fourier extremal questions); complements `findings/sdp-relaxation-uselessness` by showing where SDP genuinely beats LP.

## Open questions / connections
- Lower bounds on (equivariant) PSD lifts of $TC(N,2d)$ for general $d$ — the paper only proves the $d=1$ regular $N$-gon case ($\ge \ln(N/2)$).
- Largest provable gap $\mathrm{xc}_{\mathrm{LP}}/\mathrm{xc}_{\mathrm{PSD}}$ for cyclic polytopes — current $O(\log d / d)$ is far from the conjectured exponential gap (Problem 9.9 of [FGP+14]).
- Extends Blekherman–Gouveia–Pfeiffer 2014 (which needed an SOS multiplier) to a clean multiplier-free Laurent-conjecture proof; extends Fawzi–Saunderson–Parrilo 2014 regular-$N$-gon construction beyond powers of two.
- When $d \nmid N$: only crude workaround (round up to nearest divisor) — sharper construction open.

## Key terms
sum-of-squares, Fourier sparsity, finite abelian group, Cayley graph, chordal cover, chordal completion, Lasserre hierarchy, cut polytope, trigonometric cyclic polytope, semidefinite extension complexity, Laurent conjecture, moment polytope, equivariant lift, neighborly polytope, character translation
