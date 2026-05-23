---
type: source
kind: paper
title: Breaking down the reduced Kronecker coefficients
authors: Igor Pak, G. Panova
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.11398
source_local: ../raw/2020-pak-breaking-down-reduced-kronecker.pdf
topic: general-knowledge
cites:
---

# Breaking down the reduced Kronecker coefficients

**Authors:** Igor Pak, G. Panova  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.11398

## One-line
Resolves three problems on reduced Kronecker coefficients $\overline{g}(\alpha,\beta,\gamma)$: disproves the saturation conjecture, bounds their maximum value, and proves strong #P-hardness of their computation.

## Key claim
(1) Saturation fails: the triple $(1^{k^2-1},1^{k^2-1},k^{k-1})$ is a counterexample for all $k\geq 3$, and more generally $(a^b,a^b,\gamma)$ with $\gamma_2\geq 3$ yields infinite families of counterexamples. (2) $\max_{a+b+c\leq 3n}\overline{g}(\alpha,\beta,\gamma)=\sqrt{n!}\,e^{O(n)}$. (3) Computing $\overline{g}(\alpha,\beta,\gamma)$ is strongly #P-hard (input in unary).

## Method
Saturation disproof combines Dvir's Durfee-size inequality $d(\lambda)\leq 2d(\mu)d(\nu)$ (forcing $\overline{g}(\alpha,\alpha,\gamma)=0$) with the semigroup property and a positivity lemma of Ikenmeyer–Panova for rectangular Kronecker coefficients (forcing $\overline{g}(N\alpha,N\alpha,N\gamma)>0$). The max bound uses the Bowman–De Visscher–Orellana identity expressing $\overline{g}$ via LR-coefficient triples and Stanley's bounds on max Kronecker / LR coefficients. Hardness uses the Briand–Orellana–Rosas identity $g(\lambda,\mu,\nu)=\sum_i(-1)^i\overline{g}(\lambda^{\langle i\rangle},\mu,\nu)$ to polynomially reduce from Ikenmeyer–Mulmuley–Walter's strong #P-hardness of Kronecker.

## Result
Disproves the Kirillov–Klyachko saturation conjecture for reduced Kronecker coefficients via explicit families. Establishes $\sqrt{n!}\,e^{O(n)}$ as the asymptotic max (matching the Kronecker upper bound but over a $3n$-budget over all three partitions). Strong #P-hardness shows the problem is at least as hard as Kronecker even in unary encoding, contradicting common belief that reduced Kroneckers are simpler.

## Why it matters here
General background; no direct arena tie. Relevant only as deep-structural context for extremal combinatorics / representation-theoretic complexity — none of the 23 Einstein Arena problems involve symmetric group characters or LR/Kronecker coefficients.

## Open questions / connections
- Does saturation hold for other families of stable limits in the Sam–Snowden framework (Manivel's question)?
- Is the vanishing problem $\overline{g}(\alpha,\beta,\gamma)>?\,0$ NP-hard? (Conjectured by authors, analog to IMW17.)
- Asymptotic limit shape of maximizers in Theorem 4 — conjectured to be Plancherel (VKLS shape), extending PPY19.
- Is computing LR-coefficients $c^\lambda_{\mu\nu}$ also strongly #P-hard? (Pak–Panova conjecture.)

## Key terms
reduced Kronecker coefficients, saturation conjecture, Kirillov-Klyachko, Littlewood-Richardson coefficients, strong #P-hardness, Murnaghan stability, Durfee size, semigroup property, Dvir inequality, symmetric group representations, Knutson-Tao saturation, Pak, Panova
