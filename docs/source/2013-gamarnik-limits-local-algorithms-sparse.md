---
type: source
kind: paper
title: Limits of local algorithms over sparse random graphs
authors: D. Gamarnik, M. Sudan
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1304.1831
source_local: ../raw/2013-gamarnik-limits-local-algorithms-sparse.pdf
topic: general-knowledge
cites:
---

# Limits of local algorithms over sparse random graphs

**Authors:** D. Gamarnik, M. Sudan  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1304.1831

## One-line
Refutes the Hatami–Lovász–Szegedy conjecture by proving that no local (i.i.d. factor) algorithm can find independent sets in sparse random $d$-regular graphs larger than a $\tfrac{1}{2}+\tfrac{1}{2\sqrt{2}}$ fraction of the maximum, asymptotically as $d\to\infty$.

## Key claim
For all sufficiently large $d$, every $r$-local independence function $f_r$ on $G_d(n)$ produces independent sets of density at most $\hat{\alpha}_d/\alpha_d \le \tfrac{1}{2}+\tfrac{1}{2\sqrt{2}}+\epsilon$, whereas $\alpha_d \sim (2\log d)/d$. The authors conjecture the true barrier is exactly $1/2$.

## Method
Two-step proof: (1) a **first-moment / overlap argument** showing that for $\beta>1/\sqrt{2}$, with high probability *every* pair of independent sets of size $(1+\beta)(\log d/d)n$ has intersection either $\ge(1+z)(\log d/d)n$ or $\le(1-z)(\log d/d)n$ — no intermediate overlap exists (the **clustering / shattering property**). (2) A **coupling construction**: applying any $r$-local $f_r$ twice on $p$-correlated random seeds $(X,Y)$ continuously interpolates the expected overlap from $\alpha^2 n$ (independent) to $\alpha n$ (identical), so $f_r$ could realize forbidden intermediate overlaps — contradiction.

## Result
Theorem 2.5 (main): $\hat{\alpha}_d/\alpha_d \le 1/2 + 1/(2\sqrt{2}) + \epsilon$ for large $d$. Theorem 2.6 (overlap gap): for $\beta\in(1/\sqrt{2},1)$ and $0<z<2\beta^2-1$, no pair of size-$(1+\beta)(\log d/d)n$ independent sets in $G_d(n)$ (or $G(n,d/n)$) has overlap in the forbidden window — proved by Stirling-asymptotic first-moment computation on the configuration model. Theorem 2.7 (coupling continuity): $\gamma(p)=\Pr[f_r(X)=f_r(Y)=1]$ is continuous in $p$, with $\gamma(0)=\alpha^2$, $\gamma(1)=\alpha$, so every $\gamma\in[\alpha^2,\alpha]$ is realizable.

## Why it matters here
First rigorous proof that the **overlap-gap property (OGP)** is a genuine algorithmic obstruction, not coincidental — a template the Einstein agent should consider when optimizing combinatorial landscapes that look "shattered" (random K-SAT, max-IS, sphere packings with many near-optimal basins). Directly relevant to problems with **clustered near-optimal solution geometry** (autocorrelation, kissing, packing): if local/BP-style heuristics plateau at a fixed fraction of optimum, OGP may be the diagnostic and parallel-tempering / global moves are required.

## Open questions / connections
- Closing the gap from $1/2+1/(2\sqrt{2})$ down to the conjectured $1/2$ — improving the first-moment bound or using second-moment / interpolation methods.
- Extends [COE11] (typical-pair clustering) to the much stronger *every-pair* statement needed for hardness; suggests similar strengthening for K-SAT and other CSPs.
- Does OGP rule out broader algorithm classes (low-degree polynomials, message passing with $\omega(1)$ rounds, Langevin/MCMC)? Subsequent literature (Gamarnik–Sudan, Rahman–Virág, Wein) has pushed this program.
- Connection to spin-glass replica-symmetry-breaking / Sherrington–Kirkpatrick overlap structure.

## Key terms
overlap gap property, OGP, clustering, shattering, local algorithms, i.i.d. factors, Hatami-Lovász-Szegedy conjecture, maximum independent set, random regular graph, configuration model, Erdős-Rényi G(n,d/n), belief propagation, first moment method, Karp-Sipser, spin glass, Coja-Oghlan
