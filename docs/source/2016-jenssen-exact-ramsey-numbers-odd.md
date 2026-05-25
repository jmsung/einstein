---
type: source
kind: paper
title: Exact Ramsey numbers of odd cycles via nonlinear optimisation
authors: Matthew Jenssen, J. Skokan
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.05705
source_local: ../raw/2016-jenssen-exact-ramsey-numbers-odd.pdf
topic: general-knowledge
cites:
---

# Exact Ramsey numbers of odd cycles via nonlinear optimisation

**Authors:** Matthew Jenssen, J. Skokan  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.05705

## One-line
Resolves the Bondy–Erdős conjecture on multicolour Ramsey numbers of odd cycles for large $n$ by reducing the combinatorial problem to a finite-dimensional nonlinear optimisation problem.

## Key claim
For fixed $k \geq 2$ and odd $n$ sufficiently large, $R_k(C_n) = 2^{k-1}(n-1) + 1$, matching the Erdős–Graham lower bound. Moreover a stability version holds: every near-extremal $k$-colouring is $\varepsilon$-close in edit distance to a "hypercube colouring" indexed by a perfect matching of $Q_k$.

## Method
Apply Szemerédi regularity + Łuczak's connected-matching reduction: a monochromatic $C_n$ in $G$ corresponds to a monochromatic odd connected matching of order $\geq n t/N$ in the reduced graph $R$. Decompose each colour class into bipartite + non-bipartite parts, producing a profile vector $x \in \mathbb{R}^{\{0,1,*\}^k}$. Translate "no large odd connected matching" into a quadratic constraint $F(x) \leq 0$ via Erdős–Gallai ($e(G) \leq m(v-1)/2$ when no cycle exceeds length $m$), then maximise $\|x\|_{\ell^1}$ over the compact set $X \subset \mathbb{R}^{3^k}$; compactness gives stability of near-optimisers around hypercube-colouring profiles.

## Result
Three theorems: (1) exact value $R_k(C_n) = 2^{k-1}(n-1)+1$ for fixed $k$, odd $n$ large (Thm 1.2); (2) stability (Thm 3.2) — every $C_n$-free $k$-colouring on $N > (2^{k-1}-\eta)n$ vertices is $\varepsilon$-close to a hypercube colouring; (3) extremal colourings biject with equivalence classes of perfect matchings in $Q_k$ under $\mathrm{Aut}(Q_k)$, with count $f(k) = [(1+o(1))k/e]^{2^{k-1}}$ (e.g. $f(7) = 607{,}158{,}046{,}495{,}120{,}886{,}820{,}621$). Generalises to mixed odd lengths $n_1 \leq \dots \leq n_k$: $R(C_{n_1},\dots,C_{n_k}) = 2^{k-1}(n_k-1)+1$.

## Why it matters here
Demonstrates the **regularity-method → nonlinear-optimisation reduction** as a general template: translate an extremal combinatorics problem into a finite quadratic program on a compact polytope-like set, solve for the maximiser, and lift the stability result back combinatorially. Directly relevant to Einstein Arena problems framed as discrete extremal questions (Sidon sets, kissing, autocorrelation) where a continuous relaxation captures the asymptotic answer.

## Open questions / connections
- Extending the analytic approach to **mixed-parity** cycle Ramsey numbers (only asymptotic results known via Figaj–Łuczak; exact only for triples by Ferguson).
- Day–Johnson [DJ16] show conjecture **fails when $k$ is large vs $n$**: $R_k(C_n) > (n-1)(2+\varepsilon)^{k-1}$ — what is the true growth rate as $k \to \infty$?
- Compactness gives **no effective bound** on how large $n$ must be vs $k$; quantitative version open.
- Connects to **enumeration of perfect matchings of $Q_k$** (Graham–Harary, Östergård–Pettersson) — extremal structure mirrors a poorly-understood combinatorial object.

## Key terms
Ramsey number, odd cycle, multicolour, regularity lemma, connected matching, Łuczak reduction, Erdős–Gallai theorem, nonlinear optimisation, stability, hypercube perfect matching, Bondy–Erdős conjecture, quadratic form, profile partition, super-regular blow-up
