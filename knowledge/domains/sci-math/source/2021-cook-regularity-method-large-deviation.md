---
type: source
kind: paper
title: Regularity method and large deviation principles for the Erdős–Rényi hypergraph
authors: Nicholas A. Cook, A. Dembo, H. Pham
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2102.09100
source_local: ../raw/2021-cook-regularity-method-large-deviation.pdf
topic: general-knowledge
cites:
---

# Regularity method and large deviation principles for the Erdős–Rényi hypergraph

**Authors:** Nicholas A. Cook, A. Dembo, H. Pham  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2102.09100

## One-line
Develops a sparse-hypergraph regularity method via new cut-type tensor norms ($B^*$-norms) to prove sharp large-deviation asymptotics for upper and lower tails of homomorphism counts in $r$-uniform Erdős–Rényi hypergraphs $G(n, p^r)$.

## Key claim
For fixed $r$-graphs $H_1,\dots,H_m$ and densities $p$ allowed to vanish polynomially ($n^{-1/\Delta^*_{\max}} \ll p < 1$ for upper tail; $n^{-1/\Delta^*_{\max}}\log n \ll p < 1$ for lower tail), the joint upper- and lower-tail rates equal the entropic optimization $\Phi_{n,p}(H,\delta)$ / $\Psi_{n,p}(H,\delta)$ up to $1+o(1)$ — giving a quantitative LDP that generalizes Chatterjee–Varadhan ($r=2$, fixed $p$) and improves Cook–Dembo ($r=2$, spectral norm).

## Method
Introduces a family of **cut-type tensor norms** $\|\cdot\|_{B^*}$ indexed by "weighted base systems" that detect localized dense substructures invisible to the cut norm. The core technical tools are: (i) a **sparse tensor decomposition lemma** generalizing Frieze–Kannan, covering most of $Q_{n,r}$ by $\varepsilon p$-neighborhoods of low-complexity "structured" tensors plus a small exceptional set; (ii) a **deterministic sparse counting lemma** giving Lipschitz control $|t(H,G_1)-t(H,G_2)| \lesssim \varepsilon p^{e(H)}$ under $\|A_{G_1}-A_{G_2}\|_{B^*} \le \varepsilon p$, assuming $t(H',G_i) = O(p^{e(H')})$ on proper sub-hypergraphs. LDP upper bounds follow by minimax + union bound over the covering; lower bounds via tilted-measure / Finner–Hölder variance control (Proposition 9.2).

## Result
Theorem 1.1: joint upper/lower-tail asymptotics (1.8)–(1.10) at $1+o(1)$ precision in the stated sparsity regimes. Theorem 3.1: quantitative LDP at finite $n$ over general subsets of $Q_{n,r}$ under $B^*$-norm approximation. Theorem 10.1: same upper-tail asymptotics for **induced** homomorphism counts. Theorem 10.2: lower-tail rate $\sim \binom{n}{r} I_p(q)$ with $\hat q^{e(H)} = (1-\delta) p^{e(H)}$ for **Sidorenko** $r$-graphs $H$ whenever $p = \omega(n^{-1/\Delta(H)})$ — improving the $r=2$ threshold from Cook–Dembo. Extends to inhomogeneous Erdős–Rényi measures (Remark 1.4).

## Why it matters here
General background; no direct arena tie. Relevant peripherally to extremal-graph reasoning on **P12 Sidon-set / autocorrelation** style problems and to any future arena problem on subgraph counts or hypergraph densities — the regularity/decomposition + counting-lemma template is a general extremal-combinatorics tool the council (Szemerédi, Erdős, Tao, Razborov) may reference.

## Open questions / connections
- Can the $B^*$-norm decomposition (Theorem 2.13) be sharpened by a factor of $p$ in condition (2.16) to push joint LDP to the conjecturally optimal range $p \gg n^{-1/\Delta_{\max}}$?
- Does an analogue of Harel–Mousset–Samotij's "core" truncated-moment method (sharp for regular $H$ at $r=2$) extend to $r$-graphs below the $n^{-1/\Delta^*(H)}$ threshold?
- Apply $B^*$-norm regularity to random regular hypergraphs (parallel to Bhattacharya–Dembo for $r=2$) and to sparse stochastic block / inhomogeneous tensor models.
- Sidorenko's conjecture for hypergraphs: which $r$-graphs admit the Sidorenko property and thus the sharp lower-tail bound (10.4)?

## Key terms
large deviations, Erdős–Rényi hypergraph, homomorphism count, cut norm, tensor decomposition, Frieze–Kannan, Szemerédi regularity, sparse counting lemma, B-star norm, upper tail, lower tail, Sidorenko, entropic optimization, Finner inequality, graphon
