---
type: source
kind: paper
title: Difference Sets and Positive Exponential Sums I. General Properties
authors: M. Matolcsi, I. Ruzsa
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1207.1781
source_local: ../raw/2012-matolcsi-difference-sets-positive-exponential.pdf
topic: general-knowledge
cites:
---

# Difference Sets and Positive Exponential Sums I. General Properties

**Authors:** M. Matolcsi, I. Ruzsa  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1207.1781

## One-line
Establishes a systematic framework linking the maximum-size $B$ with $(B-B)\cap A=\{0\}$ in a finite abelian group to positive-Fourier-coefficient exponential sums supported on $A$, unifying Turán/Delsarte-type constants under set-theoretic operations.

## Key claim
For any standard set $A \subset G$ ($A=-A$, $0\in A$), the basic chain $1/q \le \underline{\delta}(A) \le \lambda_-(A),\,\lambda(A),\,\lambda_\pm(A) \le \lambda_+(A) \le \overline{\delta}(A) \le 1$ holds, and $\underline{\delta}$↔$\overline{\delta}$, $\lambda_-$↔$\lambda_+$ are dual via standard complements ($\varphi(A)\varphi'(A')=1/q$); the gap can be huge — e.g., a random set $R\subset\mathbb{Z}_2^n$ with $\delta\approx 1/2$ can have $\lambda(R)<\varepsilon$ while $\lambda_\pm(R)>1/2-\varepsilon$.

## Method
Linear-programming duality on the cone of functions $f\in S_*(A)$ with $\hat f \ge 0$, minimizing $f(0)/\hat f(\mathbf 1)$ — the four classes $S, S_-, S_+, S_\pm$ encode sign restrictions on $A$ vs $G\setminus A$. Set-operation bounds come from products/convolutions of admissible $f$'s; random-set estimates use Bernstein/Chernov on $\hat f_0(\gamma)=\sum_y \xi_y \gamma(y)$; the dyadic $\mathbb{Z}_2^n$ analysis uses Krawchouk polynomials and Samorodnitsky's degree-$k$ polynomial-positivity lemma.

## Result
Invariance: $\varphi(A)$ doesn't depend on ambient $G$ (Thm 2.2). Product: $\lambda(A_1\times A_2)=\lambda(A_1)\lambda(A_2)$, similarly $\lambda_+$ (Thm 8.1). For Hamming balls $B_k \subset \mathbb{Z}_2^n$ with $\alpha=k/(2n)$: $\lambda(B_k) \ge c_2\alpha^{1/4} q^{-\beta}$ where $\beta=H_2(\alpha)$, recovering MRRW-style behavior; and $\lambda_\pm(A_k) \ge 1 - n/(2k+2)$, witnessing the random-set separation. Random standard set with prob. $\rho$: w.h.p. $\lambda_\pm(R) \asymp \sqrt{(1-\rho)/(\rho q)}\cdot \sqrt{\log q}$, and $\Delta(R) \lesssim (\log q / \log(1/\rho))^2$ (Alon-Orlitsky-style).

## Why it matters here
Direct background for the LP/Delsarte framework underlying multiple Einstein Arena problems — autocorrelation inequalities, kissing-number/sphere-packing dual LPs, and any "max set avoiding differences in $A$" formulation; clarifies which of $\lambda, \lambda_\pm, \lambda_-, \lambda_+$ a given Cohn–Elkies-style construction actually bounds, and where the Delsarte bound is provably loose versus the combinatorial truth.

## Open questions / connections
- Problem 1.5: is there any reverse function $\lambda_-(A) \le f(\delta(A))$ with $f(x)\to 0$ as $x\to 0$, i.e., can the LP relaxation ever be a one-sided certificate?
- Extending Bourgain's cyclic-$\mathbb{Z}_q$ separation $\delta < \varepsilon$, $\lambda_+ > 1/2-\varepsilon$ to the stronger $\mathbb{Z}_2^n$ result of part (b).
- Sharp order of $\Delta$ for random Cayley graphs (Green's $O(\log q)$ vs Prakash for groups with few prime factors); whether $\lambda$-concentration is tighter than the proven log-factor.
- Better lower estimates for $\lambda_\pm(A_1\cap A_2)$ / upper for $\lambda_\pm(A_1\cup A_2)$ (Problem 6.5).

## Key terms
Turán constant, Delsarte constant, difference set, standard set, positive exponential sum, LP duality, Fourier nonnegativity, Krawchouk polynomial, Cayley graph clique number, Hamming bound, Delsarte linear program, McEliece-Rodemich-Rumsey-Welch bound, Samorodnitsky, Gilbert-Varshamov, random standard set, abelian group duality
