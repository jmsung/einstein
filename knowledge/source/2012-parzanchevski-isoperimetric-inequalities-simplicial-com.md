---
type: source
kind: paper
title: Isoperimetric inequalities in simplicial complexes
authors: Ori Parzanchevski, Ron Rosenthal, Ran J. Tessler
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1207.0638
source_local: ../raw/2012-parzanchevski-isoperimetric-inequalities-simplicial-com.pdf
topic: general-knowledge
cites:
---

# Isoperimetric inequalities in simplicial complexes

**Authors:** Ori Parzanchevski, Ron Rosenthal, Ran J. Tessler  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1207.0638

## One-line
Generalizes the graph Cheeger inequality and Expander Mixing Lemma to higher-dimensional simplicial complexes via Eckmann's high-dimensional Laplacian, yielding a combinatorial notion of expansion linked to spectral gap and Gromov's geometric overlap.

## Key claim
For a finite $d$-complex $X$ with complete $(d-1)$-skeleton, the spectral gap $\lambda(X)$ of the upper Laplacian $\Delta^+$ on $(d-1)$-cycles upper-bounds a multipartite Cheeger constant: $\lambda(X) \le h(X)$, where $h(X) = \min_{V=\sqcup_{i=0}^d A_i} \frac{n \cdot |F(A_0,\dots,A_d)|}{|A_0|\cdots|A_d|}$ and $F$ counts $d$-cells with one vertex in each block.

## Method
Define $h(X)$ via partitions of vertices into $d+1$ nonempty blocks; build an explicit skew-symmetric test $(d-1)$-form $f \in \Omega^{d-1}$ from the minimizing partition (entries $\pm|A_{\pi(d)}|$), show $f \in Z_{d-1}$ using completeness of the skeleton, then apply Rayleigh's principle to $\Delta^+ = \partial_d \partial_d^*$. The Mixing Lemma uses the indicator-like forms $\delta_{A_0,\dots,A_{d-1}}$ and the Hodge decomposition $\Omega^{d-1} = B^{d-1} \oplus \mathcal{H}^{d-1} \oplus B_{d-1}$ with the identity $\Delta^- = n \cdot P_{B_{d-1}}$ on complete-skeleton complexes.

## Result
**Cheeger:** $\lambda(X) \le h(X)$ (Thm 1.2). **Mixing Lemma:** $\bigl||F(A_0,\dots,A_d)| - \tfrac{k \cdot |A_0|\cdots|A_d|}{n}\bigr| \le \rho \cdot (|A_0|\cdots|A_d|)^{d/(d+1)}$, with $\rho = \|kI - \Delta^+\|_{Z_{d-1}}$ (Thm 1.4). **Overlap:** $\mathrm{overlap}(X) \ge \frac{c_d^d}{e^{d+1}}(c_d - \tfrac{\varepsilon(d+1)}{k})$ via Pach's Tverberg-type theorem (Cor 1.6). **Random Linial–Meshulam $X(d,n,C\log n/n)$:** for large $C$, a.a.s. $h(X) \ge (C - O(\sqrt{C}))\log n$ and $\mathrm{overlap}(X) > \vartheta$ for some $\vartheta > 0$; for $C<1$, a.a.s. $h(X)=0$.

## Why it matters here
General background; no direct arena tie. Potentially relevant if any Einstein Arena problem involves high-dimensional simplicial expansion, hypergraph discrepancy, or geometric-overlap–style Tverberg bounds — extends the "spectral gap ⇒ combinatorial expansion" template from graphs to hypergraphs.

## Open questions / connections
- Lower Cheeger inequality $C h(X)^2 - c \le \lambda(X)$ for complete-skeleton complexes (only trivial bound established via Garland's link-spectrum technique).
- Generalize discrepancy/Mixing to complexes with non-complete skeletons via the refined $\tilde h(X)$ using $(d-1)$-sphere boundaries $F_\partial$.
- Inverse Mixing Lemma à la Bilu–Linial in higher dimension; spectral optimality of Lubotzky–Samuels–Vishne Ramanujan complexes; existence/expansion of $k$-semiregular random $d$-complexes.

## Key terms
simplicial complex, Cheeger inequality, Expander Mixing Lemma, Eckmann Laplacian, high-dimensional expander, coboundary expansion, Gromov geometric overlap, Pach Tverberg-type theorem, Linial–Meshulam random complex, Hodge decomposition, spectral gap, Garland method
