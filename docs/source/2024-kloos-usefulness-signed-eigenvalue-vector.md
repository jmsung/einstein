---
type: source
kind: paper
title: Usefulness of signed eigenvalue/vector distributions of random tensors
authors: Max Regalado Kloos, Naoki Sasakura
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2403.12427
source_local: ../raw/2024-kloos-usefulness-signed-eigenvalue-vector.pdf
topic: general-knowledge
cites:
---

# Usefulness of signed eigenvalue/vector distributions of random tensors

**Authors:** Max Regalado Kloos, Naoki Sasakura  ·  **Year:** 2024  ·  **Source:** https://arxiv.org/abs/2403.12427

## One-line
Case study showing that the easier-to-compute *signed* eigenvalue/vector distribution of a real symmetric order-3 random tensor coincides with the genuine distribution near its edge, so signed distributions (computable as four-fermi partition functions) suffice to extract extreme-value information like the largest eigenvalue and best rank-one approximation.

## Key claim
For the real symmetric order-3 Gaussian random tensor $C_{abc}$ (with weight $e^{-\alpha C^2}$), the signed Z-eigenvector distribution has critical point $|v|_c = \tfrac{1}{2}\sqrt{3\alpha/(N-1)}$ and endpoint $|v|_\text{end} \sim 0.853479\sqrt{\alpha/N}$ in the large-$N$ limit, matching the genuine distribution and yielding $\zeta_\text{largest} \sim 1.17167\sqrt{N/\alpha}$.

## Method
Recast $\rho_\text{signed}(v) = \langle \det M(v,C)\,\delta^N(v_a - C_{abc}v_bv_c) \rangle_C$ as a zero-dimensional four-fermi partition function via $\det M = \int d\bar\psi d\psi\, e^{\bar\psi M \psi}$. Solve the large-$N$ four-fermi theory two ways: (i) a Schwinger-Dyson equation $1/Q + 2gQ - 1 = 0$ on the bilinear $\langle\bar\psi_a\psi_b\rangle = Q\delta_{ab}$, with $g = (N-1)|v|^2/(6\alpha)$; (ii) Lefschetz-thimble / saddle-point analysis of the explicit Hermite-polynomial form $\rho_\text{signed} \propto |v|^{-2}e^{-\alpha/|v|^2}H_{N-1}(\sqrt{3\alpha/2}/|v|)$. The endpoint is where $\lim_{N\to\infty} \tfrac{1}{N}\log\rho_\text{signed} = 0$.

## Result
Critical point $g_c = 1/8$ separates a monotone (one real saddle) regime from an infinitely oscillatory (two complex saddles) regime; endpoint $g_\text{end} \approx 0.121404$. Asymptotic smallest-eigenvector size $v_\text{min} \sim \sqrt{\alpha/N}(0.853 + a_1 \log N/N + a_2/N)$, confirmed by Monte Carlo for $N = 6$–$14$ with fitted leading coefficient $0.612 \pm 0.011$ vs. predicted $0.6035$. Application: best symmetric rank-1 approximation of Gaussian $C$ captures fraction $\sim 4.0588/N$ of $\|C\|^2$.

## Why it matters here
General background; no direct arena tie. The order-3 random-tensor model is adjacent to spin-glass complexity / SYK / spiked-tensor literature, and its techniques (four-fermi partition functions, Schwinger-Dyson, Lefschetz thimbles for extreme-value asymptotics of random nonconvex landscapes) could inform agent thinking about *typical* behavior of random objective functions, but no Einstein Arena problem in the current inventory maps directly to symmetric order-3 random-tensor eigenpair statistics.

## Open questions / connections
- Extends Auffinger–Ben Arous–Černý (2013) spin-glass complexity to a tensor-eigenvalue framing via QFT; can the same Schwinger-Dyson trick give endpoints for *non-Gaussian* or *structured* tensor ensembles?
- Signed-vs-genuine coincidence is argued from Hessian signature stability near edges — what is the precise width (in $N$) of the coincidence window, and does it survive at higher tensor order $p \geq 4$?
- Could similar four-fermi reductions yield typical-value asymptotics for injective norms / geometric entanglement measures relevant to other random extremal-geometry problems?

## Key terms
random tensor, signed eigenvalue distribution, Z-eigenvalue, real symmetric order-three tensor, four-fermi theory, Schwinger-Dyson equation, Lefschetz thimble, saddle point analysis, large-N limit, Hermite polynomial, best rank-one approximation, spin glass complexity, spiked tensor, Hessian signature, Sasakura
