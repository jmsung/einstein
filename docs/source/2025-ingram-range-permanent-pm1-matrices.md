---
type: source
kind: paper
title: On the Range of the Permanent of $(\pm1)$-Matrices
authors: DeVon Ingram, Alexander Razborov
year: 2025
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2507.09433v1
source_local: ../raw/2025-ingram-range-permanent-pm1-matrices.pdf
topic: general-knowledge
cites: 
---

# On the Range of the Permanent of $(\pm1)$-Matrices

**Authors:** DeVon Ingram, Alexander Razborov  ·  **Year:** 2025  ·  **Source:** http://arxiv.org/abs/2507.09433v1

## One-line
Establishes the first superpolynomial lower bound on the number of distinct values attained by the permanent over $n \times n$ matrices with $\pm 1$ entries.

## Key claim
$r_n \geq n^{\Omega(\log n / \log \log n)}$, where $r_n = |\{\operatorname{per}(A) : A \in \Omega_{n,n}\}|$. More precisely (Theorem 1): for every $k \geq 1$, $r_{k+1,n} \geq \epsilon_k n^{k-2}$ with $\epsilon_k \geq k^{-O(k^2)}$. This drastically improves the prior best lower bound of $n+1$ due to Kräuter.

## Method
Construct a structured family $B_{\vec n}$ of $\pm 1$ matrices where each column has at most one $-1$ entry and row $i$ contains $n_i = \mu_i(n-n_0)$ such entries for a fixed rational probability vector $\mu$. Laplace expansion in a free first row exhibits $\{\operatorname{per}(a * B)\}$ as a $k$-dimensional generalized arithmetic progression with basis given by permanental minors $p_i$, computed in closed form via Möbius inversion as a polynomial in $n$ involving elementary symmetric polynomials of the $\mu_i$. The main lemma shows the $p_i(n)$ span a $\mathbb{Q}$-subspace of codimension $\leq 2$ (Jacobian of symmetric polynomials + a recursive rank argument on $S_{\ell,a}$ vectors), yielding a proper sub-GAP of size $(\delta_k n)^{k-2}$.

## Result
For $k = \lfloor \epsilon \log n / \log \log n \rfloor$, the bound $r_n \geq k^{-O(k^2)} n^{k-2}$ becomes superpolynomial: $r_n \geq n^{\Omega(\log n / \log \log n)}$. The construction is explicit; $\delta_k \geq k^{-O(k)}$ via $M_k \leq (16k^5)^k$. Still exponentially far from the conjectured exponential growth, and far behind the $n!$ lower bound long known for $0/1$ matrices.

## Why it matters here
General background; no direct arena tie. Relevant adjacencies for the agent: GAP-based structural arguments in additive combinatorics (Tao–Vu), Möbius inversion / Laplace expansion as a counting tool, and Jacobian-of-symmetric-polynomials nondegeneracy — techniques transferable to extremal-combinatorics and anti-concentration problems that may arise in arena work.

## Open questions / connections
- Problem 1: prove $r_n$ grows exponentially in $n$ (matching numerical evidence).
- Problem 2: $\Omega(2^n)$ lower bound on range of determinant of normalized $\pm 1$ matrices; implies same for $0/1$ matrices via the $2^{-(n-1)}$ bijection (Orrick), improving Shah's $\Omega(2^n/n)$.
- Problem 3 (Kräuter): minimum positive permanent value is $2^{n - \lfloor \log_2 n \rfloor - 1}$ or $2^{n - \lfloor \log_2 n \rfloor}$ depending on $n$; still open.
- Problem 4: do "upper triangular" $\pm 1$ matrices realize the full range of $\operatorname{per}$ on $\Omega_{n,n}$? The $B_{\vec n}$ family provably does not.
- Connects to anti-concentration of the permanent of random Bernoulli matrices (Tao–Vu, Kwan–Sauermann) and BosonSampling complexity (Aaronson–Arkhipov).

## Key terms
permanent, $\pm 1$ matrices, generalized arithmetic progression, Möbius inversion, Laplace expansion, elementary symmetric polynomial, Jacobian symmetric polynomials, additive combinatorics, Kräuter conjecture, anti-concentration, Bernoulli matrices, Razborov
