---
type: source
kind: paper
title: Distributionally robust optimization with polynomial densities: theory, models and algorithms
authors: Etienne de Klerk, Daniel Kuhn, Krzysztof Postek
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/1805.03588v1
source_local: ../raw/2018-klerk-distributionally-robust-optimization-polynomial.pdf
topic: general-knowledge
cites: 
---

# Distributionally robust optimization with polynomial densities: theory, models and algorithms

**Authors:** Etienne de Klerk, Daniel Kuhn, Krzysztof Postek  ·  **Year:** 2018  ·  **Source:** http://arxiv.org/abs/1805.03588v1

## One-line
Introduces distributionally robust optimization (DRO) ambiguity sets restricted to distributions with sum-of-squares polynomial densities, yielding tractable SDP reformulations of worst-case expectation constraints.

## Key claim
Worst-case expectation constraints $\sup_{P \in \mathcal{P}} \mathbb{E}_P f(x,z) \le 0$ over ambiguity sets of distributions with degree-$2r$ SOS polynomial densities admit exact SDP reformulations of size $O\!\left(\binom{n+r}{r}\right)$, and the feasible set admits a polynomial-time separation oracle — eliminating the pathological discrete worst-case distributions endemic to classical moment-DRO.

## Method
Leverages Lasserre's measure-based hierarchy [SIAM J. Optim. 21(3), 2011]: parameterize candidate densities $h \in \Sigma[x]_r$ (SOS polys of degree $\le 2r$) against a reference measure $\mu$ with known moments $m_\alpha(K) = \int_K x^\alpha d\mu$, reducing the worst-case-expectation problem to a generalized eigenvalue problem $Av = \lambda Bv$ with $A_{\alpha,\beta} = \sum_\delta p_\delta m_{\alpha+\beta+\delta}$, $B_{\alpha,\beta} = m_{\alpha+\beta}$. A heuristic Algorithm 1 iteratively re-bases the reference measure via $d\mu' = h \cdot d\mu$ to climb the hierarchy without blowing up matrix size.

## Result
Three theoretical results: (i) exact SDP reformulation of worst-case expectation under SOS-density ambiguity sets; (ii) monotone convergence of the bound to the classical moment-DRO bound as $r \to \infty$, with extremal densities converging to the pathological discrete distributions of unrestricted moment-DRO; (iii) the ambiguity set encodes moments, conditional probabilities, conditional moments, and exact marginal distributions through linear constraints on density coefficients. Numerical experiments (portfolio + insurance Fréchet/risk-aggregation problems) show worst-case probabilities much smaller than the unrestricted moment limit (e.g., 0.0262 vs. 0.0615 at $r=12$ with 2nd-moment matching).

## Why it matters here
General background; no direct arena tie — this is DRO/SDP machinery, not packing/extremal-combinatorics. The Lasserre measure-based hierarchy and generalized-eigenvalue reformulation are reusable as a numerical technique for any Einstein Arena problem whose dual/relaxation reduces to a polynomial-density optimization (e.g., extending Cohn–Elkies-style LP duality to SDP with density restrictions), and the SOS-density framework is conceptually adjacent to SOS bounds for sphere-packing / kissing.

## Open questions / connections
- Extension to piecewise polynomial $f(x,z)$ (e.g., recourse functions of two-stage stochastic programs) — explicitly listed as a shortcoming.
- Scalability: SDPs of order $\binom{n+r}{r}$ become poorly conditioned; better than the Algorithm 1 heuristic is needed.
- Connects to Lasserre's K-moment problem [25], measure-based bounds analyzed by de Klerk–Laurent [7,8,9], and Bertsimas–Popescu optimal probability inequalities [4].

## Key terms
distributionally robust optimization, sum-of-squares polynomials, SOS density, Lasserre hierarchy, measure-based hierarchy, generalized eigenvalue problem, semidefinite programming, moment problem, ambiguity set, polynomial optimization, worst-case expectation, de Klerk, Kuhn, Lasserre
