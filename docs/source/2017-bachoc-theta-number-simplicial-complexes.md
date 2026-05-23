---
type: source
kind: paper
title: The Theta Number of Simplicial Complexes
authors: Christine Bachoc, Anna Gundert, Alberto Passuello
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1704.01836v1
source_local: ../raw/2017-bachoc-theta-number-simplicial-complexes.pdf
topic: general-knowledge
cites: 
---

# The Theta Number of Simplicial Complexes

**Authors:** Christine Bachoc, Anna Gundert, Alberto Passuello  ·  **Year:** 2017  ·  **Source:** http://arxiv.org/abs/1704.01836v1

## One-line
Generalizes the Lovász theta number from graphs to pure $k$-dimensional simplicial complexes via combinatorial Laplacians, giving an SDP upper bound on the independence number with a Lasserre-style hierarchy.

## Key claim
For a pure $k$-complex $X$, the new invariant $\vartheta_k(X)$ satisfies $\alpha(X) \le \vartheta_k(X)$, refines Golubev's spectral bound $\alpha(X) \le n(1 - d_{k-1}/\mu_{k-1})$ on complexes with complete $(k-1)$-skeleton, and extends to a decreasing hierarchy $\hat\vartheta_\ell(X)$ with $\alpha(X) = \hat\vartheta_{\alpha(X)}(X) \le \cdots \le \hat\vartheta_k(X) \le \vartheta_k(X)$.

## Method
The independent-set indicator matrix $Y^S = \delta_{(S_k)}\delta_{(S_k)}^T$ is shown to be a submatrix of the down-Laplacian $L^\downarrow_{k-1}$ of the complete complex; this motivates an SDP whose primal maximizes $\langle L^\downarrow_{k-1}, Y\rangle$ over PSD $Y$ with face-support and incidence-consistency constraints, and whose dual minimizes $\lambda_{\max}(L^\downarrow_{k-1} + T)$. The hierarchy is built by indexing matrices over independent sets of increasing dimension and adding "shadow" PSD constraints via averaging maps $\tau_{\ell-1}$. Random-complex analysis uses Garland-style localization to $(k-2)$-face links, reducing to known $G(n,p)$ theta-number estimates of Juhász / Coja-Oghlan.

## Result
On dense Linial–Meshulam random complexes $X_k(n,p)$ with $c_0\log n/n \le p \le 1 - c_0\log n/n$: $c_1\sqrt{(n-k)q/p} \le \vartheta_k(X_k(n,p)) \le c_2\sqrt{(n-k)q/p}$ w.h.p., generalizing Juhász's $\Theta(\sqrt{nq/p})$ for graphs. The $\vartheta(G) \le \chi(G)$ sandwich does NOT extend as $\vartheta_k(X) \le k\chi(X)$ (counterexample: $K^2_{m,m}$ has $\vartheta_2 = (8m-4)/(m+1)$ but $\chi = 2$); instead an ad-hoc $\chi_k(X)$ via $(k-1)$-face homomorphisms to $K^k_\ell$ recovers $\vartheta_k(X) \le \chi_k(X)$. Explicit computations: $\vartheta_2(K^2_{m,m,m}) = 2m$ (tight), $\vartheta_2(\overline{K^2_{m,m,m}}) = 3$ (tight, beats Golubev's $(7m-1)/3$ and $m+2$).

## Why it matters here
Direct relevance to **kissing-number / sphere-packing LP-SDP families** (Lovász theta is the discrete prototype of Cohn–Elkies and Bachoc–Vallentin SDP bounds the agent uses) and to **extremal hypergraph problems** that show up as higher-dimensional analogs of P-class problems — particularly any arena problem framable as "independence number of a $k$-uniform hypergraph" (P21-class extremal graph/hypergraph density). Adds: an SDP hierarchy converging to $\alpha$ in finitely many levels, providing a principled lifting scheme beyond first-order spectral bounds.

## Open questions / connections
- For which $\ell = \ell(n)$ does $\vartheta_\ell(G(n,p))$ approach $\alpha(G(n,p))$? Authors call this out of reach by their methods.
- Extension of the hierarchy analysis to non-constant $\ell$ on random $k$-complexes — open.
- Relationship between $\chi_k$ (homomorphism-to-$K^k_\ell$ chromatic number) and existing strong/weak hypergraph chromatic numbers; the three notions $\chi, \chi_k, \chi(X_1)$ are all distinct.
- Connects to Garland's method (localization to links) — the bridge from spectral-graph proofs to spectral-complex proofs.

## Key terms
Lovász theta number, simplicial complex, combinatorial Laplacian, up-Laplacian, down-Laplacian, independence number, semidefinite programming, Hoffman ratio bound, Linial-Meshulam random complex, Lasserre hierarchy, Garland localization, hypergraph chromatic number, Delsarte LP bound, Bachoc, Golubev
