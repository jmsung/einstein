---
type: source
kind: paper
title: A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm
authors: Chi Jin, Praneeth Netrapalli, Rong Ge, S. Kakade, Michael I. Jordan
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.03736
source_local: ../raw/2019-jin-short-note-concentration-inequalities.pdf
topic: general-knowledge
cites:
---

# A Short Note on Concentration Inequalities for Random Vectors with SubGaussian Norm

**Authors:** Chi Jin, Praneeth Netrapalli, Rong Ge, S. Kakade, Michael I. Jordan  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.03736

## One-line
Introduces "norm-subGaussian" (nSG) random vectors — a class strictly between $\mathrm{subGaussian}(\sigma/\sqrt{d})$ and $\mathrm{subGaussian}(\sigma)$ — and proves Hoeffding-type vector concentration with only logarithmic (not linear) dependence on dimension $d$.

## Key claim
For a vector martingale $X_1,\dots,X_n \in \mathbb{R}^d$ with $X_i \mid \mathcal{F}_{i-1}$ zero-mean nSG$(\sigma_i)$, with probability $\geq 1-\delta$:
$$\left\|\sum_{i=1}^n X_i\right\| \leq c\sqrt{\sum_{i=1}^n \sigma_i^2 \cdot \log(2d/\delta)}$$
(Corollary 7). The $d$-dependence is $\sqrt{\log d}$, versus $\sqrt{d}$ from naive subGaussian bounds.

## Method
Definition 3: $X$ is nSG$(\sigma)$ iff $P(\|X-\mathbb{E}X\| \geq t) \leq 2e^{-t^2/(2\sigma^2)}$. To handle the fact that $\|X\|$ is not zero-mean even when $X$ is, the authors lift $X \in \mathbb{R}^d$ to a symmetric $(d+1)\times(d+1)$ matrix $Y = \begin{pmatrix} 0 & X^\top \\ X & 0\end{pmatrix}$ whose eigenvalues are $\pm\|X\|$, control its MGF $\mathbb{E}e^{\theta Y} \preceq e^{c\theta^2\sigma^2}I$ (Lemma 4), then apply Lieb's concavity / Tropp's matrix Laplace transform machinery to telescope the filtration.

## Result
Three concentration bounds: Lemma 6 (general, parameter $\theta$ free), Corollary 7 (Hoeffding-type, $\sqrt{\sum \sigma_i^2 \log(2d/\delta)}$ scaling), Corollary 8 (adaptive when $\sum \sigma_i^2$ is itself random, paying only $\log\log(B/b)$ extra). Lemma 1 shows nSG$(c\sigma)$ contains: bounded vectors with $\|X\| \leq \sigma$, scalar subGaussians embedded as $\xi e_1$, and $(\sigma/\sqrt{d})$-subGaussian vectors. Class inclusion: $\mathrm{subG}(\sigma/\sqrt{d}) \subseteq \mathrm{nSG}(\sigma) \subseteq \mathrm{subG}(\sigma)$.

## Why it matters here
General background; no direct arena tie. Potentially useful if any Einstein problem reduces to controlling $\|\sum X_i\|$ for high-dimensional bounded-norm increments (e.g., random multistart trajectories, stochastic-optimization style analyses of basin-hopping ensembles) — the $\log d$ vs $d$ savings would matter for $d \geq 50$ problems like P11 (kissing-related) or sphere-packing dimensions.

## Open questions / connections
- Is the $\log d$ factor tight, or removable entirely? (Stated open in Section 4.)
- Extends Tropp's matrix concentration (2012) and Vershynin's subGaussian analysis (2010) by giving a tighter intermediate class.
- Adaptive version (Corollary 8) suggests online/anytime variants for sequential optimizer diagnostics.

## Key terms
norm-subGaussian, subGaussian random vector, concentration inequality, Hoeffding inequality, Lieb concavity theorem, Tropp matrix Laplace transform, vector martingale, MGF characterization, dimension-free concentration, covering number, sphere covering, sub-exponential norm-squared
