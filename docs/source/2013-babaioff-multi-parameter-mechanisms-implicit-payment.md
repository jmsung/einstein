---
type: source
kind: paper
title: Multi-parameter mechanisms with implicit payment computation
authors: Moshe Babaioff, Robert D. Kleinberg, Aleksandrs Slivkins
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1302.4138
source_local: ../raw/2013-babaioff-multi-parameter-mechanisms-implicit-payment.pdf
topic: general-knowledge
cites:
---

# Multi-parameter mechanisms with implicit payment computation

**Authors:** Moshe Babaioff, Robert D. Kleinberg, Aleksandrs Slivkins  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1302.4138

## One-line
A black-box reduction turning any cyclically-monotone allocation rule into a truthful multi-parameter mechanism using a single call to the allocation rule, applied to sponsored-search auctions with unknown click-through rates.

## Key claim
For any multi-parameter domain with rescalable, non-negative types, any cyclic-monotone (CMON) allocation rule $A$ can be converted — via random bid rescaling $\chi_i \in \{1, \gamma_i^{1/(1-\delta)}\}$ — into a stochastically truthful, information-feasible mechanism $M_\delta$ that agrees with $A$ with probability $\geq 1 - n\delta$ and preserves an $\alpha$-approximation up to factor $\alpha/(1 - \tfrac{\delta}{2-\delta})$, with a single call to $A$.

## Method
Generalizes the single-parameter self-resampling transformation of Babaioff–Kleinberg–Slivkins 2010 to abstract type spaces (types as functions $x_i : O \to \mathbb{R}$). Each agent's bid $b_i$ is rescaled by an independent random scalar $\chi_i$ drawn from a specific two-mass distribution; payments are $P_i(b) = b_i(A_i(x)) \cdot [\mathbb{1}_{\chi_i=1} - \tfrac{1}{\delta}\mathbb{1}_{\chi_i<1}]$, which has the correct Rochet-formula expectation (5) without ever simulating $A$ on a different bid vector. CMON is preserved under the transformation; truthfulness follows from Rochet's theorem.

## Result
(1) The transformation theorem above is proved for arbitrary CMON allocation rules — strictly more general than MIDR (Wilkens–Sivan 2012). (2) Impossibility: any ex-post truthful mechanism for sponsored search with unknown CTRs and multiple ads per advertiser is essentially bid-independent (no better than random). (3) Construction: an allocation rule ALL is built and directly proved stochastically CMON via an affine-maximizer characterization (Lemma 6.4) plus positive-definite Hessian (Claim 6.5); for $\sigma$-skewed instances with $(M_2)^2 \geq \sigma (M_1)^2$, $M_\delta$ strictly beats random allocation when $\sigma > 1$ ($\geq 2$ agents) or $\sigma > 1 + \tfrac{m\epsilon}{m+1} + \tfrac{1}{\epsilon(T-1)}$ (single agent).

## Why it matters here
General background; no direct arena tie. The mechanism-design / auction framework here is orthogonal to the Einstein Arena optimization problems (sphere packing, kissing, autocorrelation, etc.); the only conceptual touch-point is the affine-maximizer / positive-definite-Hessian style argument, which is standard linear algebra.

## Open questions / connections
- How to design stochastically CMON allocation rules with stronger welfare guarantees — current ALL only marginally beats random; the bottleneck is keeping the analysis Hessian positive-definite.
- Extends Lavi–Swamy 2007 (the only other non-MIDR truthful multi-parameter mechanism) and complements Wilkens–Sivan 2012 (MIDR-restricted single-call transformations).
- Open: characterize when truthful multi-parameter mechanisms exist beyond MIDR and the pricing/menu technique (Bartal et al., Dobzinski–Nisan).

## Key terms
cyclic monotonicity, CMON, multi-parameter mechanism design, truthful mechanism, implicit payment computation, sponsored search auction, click-through rate, multi-armed bandit, Rochet theorem, MIDR, affine maximizer, VCG, no-simulation constraint, Babaioff, Kleinberg, Slivkins, Lavi-Swamy
