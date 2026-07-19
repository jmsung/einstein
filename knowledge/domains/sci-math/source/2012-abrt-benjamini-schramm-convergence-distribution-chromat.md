---
type: source
kind: paper
title: Benjamini-Schramm convergence and the distribution of chromatic roots for sparse graphs
authors: M. Abért, Tamás Hubai
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1201.3861
source_local: ../raw/2012-abrt-benjamini-schramm-convergence-distribution-chromat.pdf
topic: general-knowledge
cites:
---

# Benjamini-Schramm convergence and the distribution of chromatic roots for sparse graphs

**Authors:** M. Abért, Tamás Hubai  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1201.3861

## One-line
For Benjamini-Schramm convergent bounded-degree graph sequences, the holomorphic moments of the chromatic-root distribution converge, so the normalized log chromatic polynomial converges to a real-analytic function off a bounded disc.

## Key claim
If $(G_n)$ is Benjamini-Schramm convergent with max degree $\le d$, then for any holomorphic $f$ on a neighborhood of $\overline{B(0, Cd)}$ (Sokal's disc, $C<8$), $\int f\,d\mu_{G_n}$ converges; consequently $t_{G_n}(z) = \ln \mathrm{ch}_{G_n}(z)/|V(G_n)|$ converges to a real-analytic function on $\mathbb{C}\setminus \overline{B(0,Cd)}$.

## Method
Express the holomorphic moment $p_k(G)=\sum \lambda_i^k$ as a finite, fixed integer/rational linear combination of homomorphism counts $\mathrm{hom}(T,G)$ over connected graphs $T$ with $\le k+1$ vertices, via Newton identities + Möbius inversion on the partition lattice $\mathcal{P}(G)$ (Claims 1 & 2 in Lemma 3.1, then Theorem 3.4). Since BS-convergence is equivalent to convergence of $\mathrm{hom}(H,G_n)/|V(G_n)|$ for every connected $H$ (Lovász, Lemma 2.2), moment convergence follows; harmonicity of $\ln|z_0-\lambda|$ + local uniform convergence gives analyticity.

## Result
Explicit large-girth bound (Theorem 1.4): for girth $g$, max degree $d$, $q > Cd$,
$$\left|\frac{\ln \mathrm{ch}_G(q)}{|V(G)|} - \ln q + \frac{|E(G)|}{|V(G)|}\ln(1-1/q)\right| \le 2\frac{(Cd/q)^{g-1}}{1-Cd/q}.$$
For $d$-regular graphs with $g = c\ln|V(G)|$ this is $O(|V(G)|^{-c'})$. Weak (not just holomorphic) convergence fails in general (counterexample: $P_n$ vs $C_n$) but holds for the $C_4\times P_n$ tube via Mergelyan's theorem on the transfer-matrix limit curve.

## Why it matters here
General background; no direct arena tie — none of the 23 Einstein Arena problems is a chromatic-polynomial or graph-limits problem. Closest tangential relevance: the moments-from-homomorphisms machinery and Sokal-type root bounds are a template for "extract analytic invariants of a graph polynomial from local statistics," which could inform extremal-graph problems if they ever surface a Tutte/chromatic angle.

## Open questions / connections
- Problem 1.5: does $\mu_{G_n}$ weakly converge for $d$-regular graphs with girth $\to\infty$? (Would define the chromatic measure of the $d$-regular infinite tree.)
- Extension to the full Tutte polynomial $T_G(x,y)$ — partially answered by Csikvári-Frenkel (arXiv:1204.0463) for large $|x|,|y|$; still open at combinatorially natural points like $(2,1)$, $(1,2)$.
- Improving the analyticity radius from $Cd$ (Sokal, $C<8$) down to $d+1$ as in Bandyopadhyay-Gamarnik's free-energy result.

## Key terms
Benjamini-Schramm convergence, chromatic polynomial, chromatic roots, graph limits, holomorphic moments, homomorphism counts, Sokal bound, Tutte polynomial, antiferromagnetic Potts model, Mergelyan's theorem, Möbius inversion, large girth, transfer matrix method, free energy per vertex, Newton identities
