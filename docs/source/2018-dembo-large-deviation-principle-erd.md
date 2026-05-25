---
type: source
kind: paper
title: A large deviation principle for the Erd\H{o}s-R\'enyi uniform random graph
authors: A. Dembo, E. Lubetzky
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.11327
source_local: ../raw/2018-dembo-large-deviation-principle-erd.pdf
topic: general-knowledge
cites:
---

# A large deviation principle for the Erd\H{o}s-R\'enyi uniform random graph

**Authors:** A. Dembo, E. Lubetzky  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.11327

## One-line
Transfers the Chatterjee–Varadhan large deviation principle from the binomial random graph $G(n,p)$ to the edge-conditioned uniform random graph $G(n,m_n)$ with $m_n/\binom{n}{2}\to p$.

## Key claim
For fixed $0<p<1$ and $m_n/\binom{n}{2}\to p$, $G(n,m_n)$ satisfies an LDP on the graphon space $(\widetilde{\mathcal W}_0,\delta_\square)$ at speed $n^2$ with good rate function $J_p(W)=I_p(W)$ on $\widetilde{\mathcal W}_0(p)=\{W:\|W\|_1=p\}$ and $+\infty$ otherwise; consequently upper-tail subgraph-count rates are $-\psi_H(p,r)$ matching the constrained-graph variational problem $F_H(p,r)=-\psi_H(p,r)+h_e(p)$.

## Method
A general conditional-LDP lemma (Proposition 2.1) extending Dembo–Zeitouni's exponential-approximation framework (Thm 4.2.16) to point conditioning $f(x)=s$, paired with a combinatorial coupling that adds/deletes $|D_n|<\eta n^2$ edges to convert $G(n,p)$ conditioned on $|E|\in((p-\eta)\binom{n}{2},(p+\eta)\binom{n}{2})$ into $G(n,m_n)$. The cut-distance bound $\delta_\square(G,G')\le 22/\log_2 k$ from a few subgraph densities (Borgs–Chayes–Lovász–Sós–Vesztergombi Thm 2.7(b)) certifies the coupling is an exponentially good approximation. The sparse regime $m_n\ge n^2/\log^c n$ is handled separately via the weak regularity lemma plus Cramér.

## Result
Theorem 1.1 gives the full LDP. Corollary 1.2: $\psi_H(p,\cdot)$ is zero on $[0,t_H(p)]$, strictly increasing and finite on $[t_H(p),r_H]$, lsc/left-continuous; at every right-continuity point $r$, $\lim n^{-2}\log\mathbb P(t_H(G_n)\ge r)=-\psi_H(p,r)$ and conditional on $\{t_H\ge r\}$, $G_n$ concentrates exponentially ($e^{-Cn^2}$) on the minimizer set $\mathcal F^*$. Equation (1.9) gives an interchange-of-limits counting interpretation $F_H(p,r)=\lim n^{-2}\log|\mathcal H_{n,m_n,r}|$. Proposition 3.2 covers $p_n(\log n)^{1/(2\kappa)}\to\infty$ via a discrete variational problem.

## Why it matters here
General background; no direct arena tie. The paper supplies a transfer principle (binomial $\to$ uniform / edge-constrained ensembles) and a conditional-LDP toolkit that could inform extremal-graph problems with hard edge-count constraints, but none of the 23 arena problems currently use the edge/triangle model.

## Open questions / connections
- Behavior at discontinuities of $\psi_H(p,\cdot)$ (Remark 1.3): the limit fails when $m_n/\binom{n}{2}\uparrow p$ slowly — what is the right correction?
- Sparse regime $p_n=n^{-c}$ remains delicate; extends nonlinear large deviations of Chatterjee–Dembo and Eldan.
- Structure of minimizers of $F_H(p,r)$ (multipodal, bipodal phases of Kenyon–Radin–Ren–Sadun) — still open beyond triangles.
- The interchange-of-limits identity (1.9) suggests counting techniques for any subgraph $H$ with joint edge/$H$-density constraints.

## Key terms
large deviation principle, Erdős–Rényi, uniform random graph, $G(n,m)$, graphon, cut-metric, Chatterjee–Varadhan, subgraph density, edge-triangle model, conditional LDP, exponentially good approximation, weak regularity lemma, Kenyon–Radin, variational problem, replica symmetry, upper tail, entropy function $h_e$, Lubetzky–Zhao
