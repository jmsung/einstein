---
type: source
kind: paper
title: On smoothness of extremizers of the Tomas-Stein inequality for $S^1$
authors: Shuanglin Shao
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1601.07119
source_local: ../raw/2016-shao-smoothness-extremizers-tomas-stein-inequality.pdf
topic: general-knowledge
cites:
---

# On smoothness of extremizers of the Tomas-Stein inequality for $S^1$

**Authors:** Shuanglin Shao  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1601.07119

## One-line
Proves that any $L^2$ extremizer of the Tomas-Stein Fourier restriction inequality on the circle $S^1$ is in fact smooth ($C^\infty$).

## Key claim
**Theorem 1.1.** Any $L^2$ solution of the generalized Euler-Lagrange equation $f\sigma * f\sigma * f\sigma * \tilde f\sigma * \tilde f\sigma(x) = \lambda f(x)$ on $S^1$ (with $\lambda = R^6 \|f\|_{L^2}^4$, $\tilde f(x)=\bar f(-x)$) is smooth on $S^1$. In particular, every extremizer of $\|\widehat{f\sigma}\|_{L^6(\mathbb R^2)} \le R_1 \|f\|_{L^2(S^1)}$ is $C^\infty$.

## Method
Two-step regularity argument modeled on Christ-Shao (2012). Step 1 (Lemma 3.4): split $f = \phi_\epsilon + g_\epsilon$ with $\phi_\epsilon \in C^\infty$ and $\|g_\epsilon\|_{L^2}$ small; rewrite the Euler-Lagrange equation as a fixed-point problem $g_\epsilon = L(\phi_\epsilon,g_\epsilon)+N(\phi_\epsilon,g_\epsilon)$ and apply a Picard contraction in $H^{s(\epsilon)}$ to gain an initial sliver of Sobolev regularity. Step 2 (Lemma 3.5, Proposition 3.6): bootstrap via the convolution bound $\|f_1\sigma * \cdots * f_5\sigma\|_{H^s} \lesssim \prod \|f_i\|_{H^s}$, which rests on the uniform boundedness of $\sigma^{*5}$ — obtained from Hausdorff-Young plus the explicit $\sigma * \sigma(x) = C\sqrt{4-|x|^2}/|x|$.

## Result
Every $L^2$ extremizer for the $S^1$ Tomas-Stein inequality is $C^\infty(S^1)$. The technical engine is uniform boundedness of the five-fold convolution $\mu = \sigma^{*5}$ on $\{|x|\le 5\}$ (Lemma 3.2), and a Sobolev product estimate (Lemma 3.3) giving $\|f_1\sigma * \cdots * f_5\sigma\|_{H^s} \le C\prod_{i=1}^5 \|f_i\|_{H^s}$ for $s\ge 0$. The author notes the same approach simplifies a step in Christ-Shao's $S^2$ smoothness proof, since $\sigma_2^{*3}$ is similarly uniformly bounded.

## Why it matters here
General background; no direct arena tie. Closest contact is with autocorrelation / Fourier-restriction problems where one extremizes $L^p$ norms of $\widehat{f\sigma}$ on a low-dimensional manifold — regularity of optimizers justifies parameterizing extremizers by smooth ansätze rather than rough $L^2$ data.

## Open questions / connections
- Combined with Carneiro-Foschi-Silva-Thiele's conditional uniqueness (constants are the only extremizers on $S^1$), full unconditional uniqueness for $d=1$ remains open — smoothness is a needed input but not sufficient.
- Extends Christ-Shao [12] ($S^2$ case) and Shao [28] (existence for $S^1$); leaves open analogous smoothness for the paraboloid Strichartz extremizers in $d\ge 3$ and for the wave-equation extremizers (Bulut [7]).
- The Frank-Lieb-Sabin [17] conditional existence in all dimensions raises the question of whether the same Picard-iteration + convolution-bound scheme upgrades regularity once existence is known.

## Key terms
Tomas-Stein inequality, Fourier restriction, extremizer regularity, Euler-Lagrange equation, Strichartz inequality, sphere $S^1$ surface measure, convolution of surface measures, Hausdorff-Young inequality, Sobolev space $H^s$, Picard iteration bootstrap, Christ-Shao, Foschi, profile decomposition
