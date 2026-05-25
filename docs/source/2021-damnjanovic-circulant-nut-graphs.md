---
type: source
kind: paper
title: On circulant nut graphs
authors: Ivan Damnjanovi'c, Dragan Stevanović
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2104.10755
source_local: ../raw/2021-damnjanovic-circulant-nut-graphs.pdf
topic: general-knowledge
cites:
---

# On circulant nut graphs

**Authors:** Ivan Damnjanovi'c, Dragan Stevanović  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2104.10755

## One-line
Characterizes which circulant graphs $\mathrm{Circ}(n,S)$ are *nut graphs* (adjacency-matrix kernel is 1-dimensional with a nowhere-zero eigenvector) via cyclotomic-polynomial divisibility of the generator polynomial.

## Key claim
(1) The generator set $S$ of any circulant nut graph contains equally many odd and even integers, so the degree is $4t$. (2) $\mathrm{Circ}(n,\{x,x{+}1,\ldots,x{+}2t{-}1\})$ is a nut graph iff $\gcd(n/2,t)=\gcd(n/2,2x{+}2t{-}1)=1$. (3) For odd $t\geq 3$ with $t\not\equiv 1\pmod{10}$ and $t\not\equiv 15\pmod{18}$, $\mathrm{Circ}(n,\{1,\ldots,2t{+}1\}\setminus\{t\})$ is a nut graph for every even $n\geq 4t+4$, resolving Bašić et al.'s Conjecture 9 (case $t=3$, 12-regular).

## Method
Compute eigenvalues of the circulant adjacency matrix via the generator polynomial $P(y)$ evaluated at $n$-th roots of unity, then convert "$P$ has no roots among non-trivial $n$-th roots of unity" into "no cyclotomic polynomial $\Phi_b$ divides the auxiliary polynomial $Q_{S_t}(y)=(y-1)y^{\max(S)}P(y)$". Bound $b$ via $\phi(b)\leq N$ using Rosser–Schoenfeld's lower bound on $\phi$, then apply the Filaseta–Schinzel theorem on cyclotomic divisors of lacunary polynomials to peel off large prime factors and finitely many small-$b$ cases handled by direct computation.

## Result
Full equivalence (Theorem 6) for consecutive-window generators, generalizing Bašić et al.'s Theorem 2. Existence theorem (Theorem 9) producing $4t$-regular circulant nut graphs of all even orders $n\geq 4t+4$ for the "almost-consecutive" set $S_t=\{1,\ldots,2t+1\}\setminus\{t\}$ under mild congruence exclusions. Concrete propositions: 4-regular nut graphs for all even $n\geq 8$; 8-regular nut graphs iff $n=14$ or even $n\geq 18$ (using $\{3,4,5,8\}$); 12-regular via $\{1,2,4,5,6,7\}$ for all even $n\geq 16$. Computational table of universal generator sets for $3\leq t\leq 120$.

## Why it matters here
General background; no direct arena tie. Touches spectral graph theory / cyclotomic-polynomial methods that could inform spectral approaches in extremal graph problems, but the nut-graph existence question is orthogonal to the current Einstein Arena problem set (sphere packing, autocorrelation, kissing numbers, etc.).

## Open questions / connections
- Conjecture 19: for every odd $t\geq 3$, $\exists\, p_t$ such that $\{1,\ldots,2t{+}1\}\setminus\{p_t\}$ is universal; for every even $t\geq 4$, $\exists\,\{q_t,r_t\}$ such that $\{1,\ldots,2t{+}2\}\setminus\{q_t,r_t\}$ is universal — would fully resolve Bašić et al.'s Conjecture 10.
- Extends Fowler et al. (2020) Question 11 on vertex-transitive nut graphs: characterize all admissible $(n,d)$ pairs realized by *circulant* nut graphs.
- The Filaseta–Schinzel + Rosser–Schoenfeld combination as a generic toolkit for "no cyclotomic factor of a sparse polynomial" problems beyond nut graphs.

## Key terms
circulant graph, nut graph, cyclotomic polynomial, generator set, eigenvalue multiplicity, Euler totient, Filaseta–Schinzel theorem, Rosser–Schoenfeld bound, vertex-transitive graph, spectral graph theory, lacunary polynomial, roots of unity
