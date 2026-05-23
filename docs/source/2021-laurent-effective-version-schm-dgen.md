---
type: source
kind: paper
title: An effective version of Schmüdgen’s Positivstellensatz for the hypercube
authors: M. Laurent, Lucas Slot
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2109.09528
source_local: ../raw/2021-laurent-effective-version-schm-dgen.pdf
topic: general-knowledge
cites:
---

# An effective version of Schmüdgen's Positivstellensatz for the hypercube

**Authors:** M. Laurent, Lucas Slot  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2109.09528

## One-line
Quadratically sharpens the degree bound for SOS-based positivity certificates of polynomials on the hypercube $[-1,1]^n$ from $O(1/\eta)$ to $O(1/\sqrt{\eta})$ using the Jackson kernel.

## Key claim
For $f \in \mathbb{R}[\mathbf{x}]$ of degree $d$ nonnegative on $B_n = [-1,1]^n$, and any $\eta > 0$, the shifted polynomial $f + \eta$ admits a Schmüdgen-type SOS decomposition in the truncated preordering $Q(B_n)_r$ at degree $r = O(1/\sqrt{\eta})$. Equivalently, the Lasserre hierarchy lower bound $f^{(r)}$ satisfies $f_{\min} - f^{((r+1)n)} \le C(n,d)/r^2 \cdot (f_{\max} - f_{\min})$ for $r \ge \pi d\sqrt{2n}$, where $C(n,d)$ is polynomial in $n$ (fixed $d$) and in $d$ (fixed $n$).

## Method
Polynomial kernel method: construct a nonsingular linear operator $K_r$ on $\mathbb{R}[\mathbf{x}]_r$ from the *multivariate Jackson kernel* $K_r(\mathbf{x},\mathbf{y}) = \prod_i K_r^{ja}(x_i, y_i)$, which (i) maps $P(B_n)_r$ into $Q(B_n)_{(r+1)n}$ via Fekete/Markov–Lukács univariate factorization, and (ii) diagonalizes in the multivariate Chebyshev basis with eigenvalues $\lambda_\kappa^r = \prod_i \lambda_{\kappa_i}^r$. The $O(1/r^2)$ rate then drops out of the Jackson-kernel eigenvalue estimate $|1 - \lambda_k^r| \le \pi^2 d^2/(r+2)^2$ combined with Bernoulli's inequality and Cauchy–Schwarz on the Chebyshev expansion.

## Result
**Theorem 2:** $f_{\min} - f^{((r+1)n)} \le \tfrac{C(n,d)}{r^2}(f_{\max} - f_{\min})$ for $r \ge \pi d\sqrt{2n}$, with explicit constants $C(n,d) \le 2\pi^2 d^2 n \cdot 2^{n/2}(d+1)^n$ and $C(n,d) \le 2\pi^2 d^2 n \cdot 2^{d/2}(n+1)^d$. This matches Stengle's $\Omega(1/r^2)$ lower bound for the related (nonstandard) interval description, so the rate is tight for that variant.

## Why it matters here
General background for SDP/SOS-based bounds: the Lasserre/Schmüdgen machinery underpins SDP relaxations potentially relevant to extremal-geometry and packing problems via flag algebras or moment relaxations on box-constrained variables. No direct Einstein-Arena problem ties — this is theoretical infrastructure for *why* polynomial-optimization hierarchies converge at the rates we'd see if we tried Lasserre on a $[-1,1]^n$-parameterized problem.

## Open questions / connections
- Can $C(n,d)$ be made to depend only on $d$ (not $n$), as known for the sphere [Fang–Fawzi] and boolean cube [Slot–Laurent]?
- Does the $O(1/\sqrt{\eta})$ bound extend from preordering (Schmüdgen) to quadratic-module (Putinar) certificates on $B_n$?
- Negative results for the *standard* hypercube description $g_i = 1 - x_i^2$ — Stengle's $\Omega(1/r^2)$ only applies to the description $g = (1-x^2)^3$.

## Key terms
Schmüdgen Positivstellensatz, Lasserre hierarchy, sum-of-squares, preordering, quadratic module, Jackson kernel, Chebyshev polynomials, polynomial kernel method, hypercube optimization, Putinar certificate, semialgebraic set, polynomial positivity certificate
