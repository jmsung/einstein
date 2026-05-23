---
type: source
kind: paper
title: On replica symmetry of large deviations in random graphs
authors: E. Lubetzky, Yufei Zhao
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1210.7013
source_local: ../raw/2012-lubetzky-replica-symmetry-large-deviations.pdf
topic: general-knowledge
cites:
---

# On replica symmetry of large deviations in random graphs

**Authors:** E. Lubetzky, Yufei Zhao  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1210.7013

## One-line
Identifies the exact replica-symmetric phase for upper-tail large deviations of $d$-regular subgraph densities (and the spectral radius) in the Erdős–Rényi random graph $G(n,p)$ at fixed $p$.

## Key claim
For a fixed $d$-regular graph $H$ and $0<p\le r<1$, conditioning $G(n,p)$ on $t(H,G_n)\ge r^{e(H)}$ produces a graph close in cut-distance to constant graphon $r$ **iff** $(r^d, h_p(r))$ lies on the convex minorant of $x\mapsto h_p(x^{1/d})$ — for triangles this is $h_p(\sqrt{x})$, not the previously guessed $h_p(x^{1/3})$, so the symmetric phase is strictly larger than Chatterjee–Varadhan's bound.

## Method
Analyzes the graphon variational problem $\inf\{h_p(f) : t(H,f)\ge r^{e(H)}\}$ arising from the Chatterjee–Varadhan large-deviation framework (built on Szemerédi regularity + Lovász–Szegedy graph limits). The symmetric side uses a generalized Hölder inequality (Finner 1992) to show $t(H,f)\le \|f\|_d^{e(H)}$ with equality only for constants; the symmetry-breaking side constructs explicit two-step/three-step "clique-like" graphons that beat the constant. Extends the framework from subgraph counts to operator norm and to linear $k$-uniform hypergraphs.

## Result
- **Theorem 1.1**: Phase boundary for $d$-regular $H$ is the convex-minorant condition on $h_p(x^{1/d})$; for $d=2$, symmetry breaks iff $p<(1+(r^{-1}-1)^{1/(1-2r)})^{-1}$.
- **Theorem 1.2**: Spectral-radius deviations $\lambda_1(G_n)\ge nr$ have the same boundary as triangles.
- **Theorem 1.3**: Generalized exponential random graph $\propto\exp(\beta_1 t(K_2)+\beta_2 t(H)^\alpha)$ with $\beta_2>0$ exhibits symmetry breaking iff $\alpha<d/e(H)$ — new phase transition absent in the standard $\alpha=1$ model.
- **§6**: Short entropy-free proof of the Kahn / Galvin–Tetali bound $\hom(G,H)\le \hom(K_{d,d},H)^{|V(G)|/(2d)}$ via generalized Hölder.

## Why it matters here
General background; no direct arena tie. The convex-minorant-of-$h_p(x^{1/d})$ pattern is a useful reference for variational problems where the natural exponent ($1/e(H)$) is wrong and the correct exponent comes from the maximum degree; potentially relevant as a meta-lesson for extremal-graph / autocorrelation problems where guessing the wrong scaling exponent misidentifies the optimization landscape.

## Open questions / connections
- No explicit minimizer is known anywhere in the symmetry-breaking phase — are they always 2-step graphons (constant on $[0,w]^2$, off-block, $[w,1]^2$)?
- Phase boundary for non-regular $H$ remains unknown (no matching upper/lower bounds).
- Lower-tail phase transition tied to Sidorenko's conjecture (open for general bipartite $H$); non-bipartite lower-tail diagram unknown.
- Extension to sparse $G(n,p)$ ($p\to 0$) and to non-linear hypergraphs requires sparse / hypergraph regularity refinements.

## Key terms
large deviations, Erdős-Rényi random graph, replica symmetry, symmetry breaking, graphon, cut-distance, Szemerédi regularity lemma, Chatterjee-Varadhan framework, convex minorant, generalized Hölder inequality, Kahn-Galvin-Tetali homomorphism bound, Sidorenko conjecture, exponential random graph, triangle upper tail, spectral radius deviation, linear hypergraph
