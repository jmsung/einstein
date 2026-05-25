---
type: source
kind: paper
title: Melonic dominance and the largest eigenvalue of a large random tensor
authors: O. Evnin
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.11220
source_local: ../raw/2020-evnin-melonic-dominance-largest-eigenvalue.pdf
topic: general-knowledge
cites:
---

# Melonic dominance and the largest eigenvalue of a large random tensor

**Authors:** O. Evnin  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.11220

## One-line
Estimates the largest E-eigenvalue of a large Gaussian random fully-symmetric real tensor by tracking norm growth under power iteration and isolating the dominant melonic Feynman diagram.

## Key claim
For a Gaussian rotationally-invariant ensemble of real fully-symmetric rank-$(q+1)$ tensors in $N$ dimensions, the largest E-eigenvalue scales as $|\lambda_{\max}| \approx \sqrt{N/(q+1)}$ — i.e., $\sim \sqrt{N}$, mirroring the Wigner edge for random symmetric matrices ($q=1$).

## Method
Power iteration $x_i^{(p+1)} = C_{i\,i_1\cdots i_q} x_{i_1}^{(p)} \cdots x_{i_q}^{(p)}$ gives super-exponential norm growth $\ln\|x^{(p)}\|^2 \sim 2\ln|\lambda|\cdot[p]_q$ where $[p]_q = (q^p-1)/(q-1)$. The expectation $\langle x_k^{(p)} x_k^{(p)}\rangle_C$ is expanded via Wick's theorem into "hourglass" Feynman diagrams; melonic-dominance combinatorics (bounding faces $\sum F_l \le V$) singles out a unique balanced recursive contraction pattern at leading order in $N$.

## Result
The dominant diagram evaluates to $\langle x_k^{(p)} x_k^{(p)}\rangle_C = (N/(q+1))^{[p]_q}$ at large $N$, yielding $|\lambda_{\max}| \approx \sqrt{N/(q+1)}$. The variance factorizes ($\langle (x\cdot x)^2\rangle = \langle x\cdot x\rangle^2$ at leading order), giving $1/N$-suppressed fluctuations and suggesting concentration of $\lambda_{\max}$ — a tensor analog of large-$N$ factorization.

## Why it matters here
General background for the agent: connects random-tensor melonic dominance to optimization-flavored "best rank-1 approximation" (largest E-eigenvalue = best symmetric rank-1 fit), which is structurally adjacent to multilinear extremal problems but has no direct Einstein Arena problem tie in the current inventory.

## Open questions / connections
- Rigorous Kac–Rice-style derivation of the $\sqrt{N/(q+1)}$ bound and a Wigner-semicircle analog for tensor eigenvalue density (cf. Gurau arXiv:2004.02660, appeared concurrently).
- Universality beyond Gaussian ensembles for independently-distributed tensor entries (extends Gurau's tensor universality, arXiv:1111.0519).
- Basin-of-attraction structure for power iterations (3) — accessibility of $\lambda_{\max}$ vs. mere existence; relevance to spiked-tensor recovery thresholds (Montanari–Richard, Ros et al.).
- Characteristic polynomials and resolvents of random tensors via Morozov–Shakirov machinery, in analogy to Brézin–Hikami for matrices.

## Key terms
random tensor, melonic dominance, largest eigenvalue, E-eigenvalue, power iteration, Gaussian orthogonal ensemble, Wick's theorem, Feynman diagram, hourglass diagram, best rank-1 approximation, symmetric tensor, large-N factorization, spiked tensor model, Wigner semicircle, Gurau, Evnin
