---
type: source
kind: paper
title: How well can we estimate a sparse vector?
authors: E. Candès, M. Davenport
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1104.5246
source_local: ../raw/2011-cands-how-well-can-estimate.pdf
topic: general-knowledge
cites:
---

# How well can we estimate a sparse vector?

**Authors:** E. Candès, M. Davenport  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1104.5246

## One-line
Establishes an information-theoretic minimax lower bound on the mean-squared error for estimating a $k$-sparse vector in $\mathbb{R}^n$ from $m$ noisy linear measurements, showing that no choice of sensing matrix or recovery algorithm can essentially beat $\ell_1$-minimization.

## Key claim
For any $m \times n$ matrix $A$ with $m \geq k$ and Gaussian noise $z \sim N(0,\sigma^2 I)$, the minimax risk satisfies $M^*(A) \geq C_1 \frac{k\sigma^2}{\|A\|_F^2} \log(n/k)$ (with $C_1 \approx 1/128$ asymptotically) and also $M^*(A) \geq \frac{k\sigma^2}{\|A\|_F^2}$. This matches the Dantzig-selector/Lasso upper bound $C_0 (k\sigma^2/m) \log n$ up to a $\log n / \log(n/k)$ factor.

## Method
Fano's inequality applied to a packing set of $k$-sparse vectors, combined with convexity of KL divergence to bound mutual information by pairwise $\|Ax_i - Ax_j\|_2^2$ distances. The packing set $X \subset \Sigma_k$ of size $(n/k)^{k/4}$ is constructed via the probabilistic method on $\{0, \pm 1/\sqrt{k}\}^n$, and its empirical covariance is controlled using the Ahlswede–Winter matrix Bernstein inequality so that $\|\frac{1}{|X|}\sum x_i x_i^* - \frac{1}{n}I\| \leq \beta/n$. The key innovation versus Raskutti–Wainwright–Yu is that no RIP-type assumption is placed on $A$ — the matrix-Bernstein bound on the random packing's covariance replaces it.

## Result
Theorem 1: $M^*(A) \geq C_1 \frac{k\sigma^2}{\|A\|_F^2}\log(n/k)$ for all $A$, all estimators, finite $n,k$. Corollary 1: in the signal-noise model $y = A(x+w)$, $M^*(A) \geq C_1 (k\sigma^2/m)\log(n/k)$ regardless of $A$ — the $1/m$ penalty is unavoidable because noise is scaled by $A$. The simpler oracle-based bound (6) is obtained by exploiting that some subset $T_0$ of $k$ columns has $\|A_{T_0}\|_F^2 \leq (k/n)\|A\|_F^2$ and that subset-known minimax risk is $\frac{1}{n}\sum 1/\lambda_i(A_T^* A_T)$.

## Why it matters here
General background; no direct arena tie. Provides the canonical template for *minimax lower bounds via Fano + random packing + matrix concentration* — useful methodology if the agent ever needs to prove a lower bound is tight (e.g., for autocorrelation or sparse-recovery-flavored Arena problems), and a clean example of how matrix Bernstein replaces RIP-style assumptions.

## Open questions / connections
- Optimal constant $C_1$ (paper achieves $1/128$, admits this is far from sharp) — leaves room for tightening.
- Closes the gap left by Raskutti–Wainwright–Yu (RIP-dependent) and Ye–Zhang (asymptotic only $k,n \to \infty$, $k/n \to 0$) to a fully general, finite-$n$ statement.
- The residual $\log n / \log(n/k)$ slack between lower and upper bound — does the upper bound have a matching $\log(n/k)$ form for some recovery procedure?

## Key terms
compressive sensing, sparse estimation, minimax lower bound, Fano's inequality, matrix Bernstein inequality, Ahlswede-Winter, packing set, KL divergence, Dantzig selector, Lasso, restricted isometry property, Candès, Davenport, sparse linear regression
