---
type: source
kind: paper
title: The Phase Transition in the Configuration Model
authors: O. Riordan
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1104.0613
source_local: ../raw/2011-riordan-phase-transition-configuration-model.pdf
topic: general-knowledge
cites:
---

# The Phase Transition in the Configuration Model

**Authors:** O. Riordan  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1104.0613

## One-line
Precise distributional analysis of the giant component's emergence in random graphs with a given (bounded) degree sequence, near criticality.

## Key claim
For a configuration multigraph $G^m_d$ with bounded degrees and branching factor $\lambda = \mu_2/\mu_1 = 1+\varepsilon$, when $\varepsilon \to 0$ and $\varepsilon^3 n \to \infty$: above the window, $L_1 - \rho n$ and $N_1 - \rho^* n$ are jointly asymptotically normal with $\mathrm{Var}(L_1') \sim 2\mu_1 \varepsilon^{-1} n$, $\mathrm{Var}(N_1') \sim (10\mu_1^3/3\mu_3^2)\varepsilon^3 n$, correlation $3/5$; below the window, $L_1 = \delta_n^{-1}(\log\Lambda - \tfrac{5}{2}\log\log\Lambda + O_p(1))$ with $\delta_n \sim \varepsilon^2/(2v_0)$; in the window, sorted component sizes/nullities converge to Aldous-style Brownian-excursion limits.

## Method
Exploration-process / random-walk approach following Aldous, Nachmias–Peres, and Bollobás–Riordan: track $X_t = A_t - 2C_t$ (active stubs minus twice components started) as a random walk with increments $\eta_{t+1} - 2 - 2\theta_{t+1}$, then analyze its trajectory against an idealized deterministic curve. Supercritical and critical regimes use trajectory-tracking + martingale CLT; subcritical regime uses stochastic-domination sandwiching plus an exponential-tilting (Cramér) local limit theorem (Lemma 6.3, proved via Bernoulli-part decomposition and Esseen/Berry–Esseen).

## Result
Establishes the *full* distributional picture (mean, variance, limiting law) of the giant component for the configuration model across all three regimes near criticality — strictly sharper than Molloy–Reed (LLN only), Nachmias–Peres (size only, regular case), and Janson–Łuczak (supercritical only). Window width is confirmed at $\varepsilon = \Theta(n^{-1/3})$. Corollary 1.4 specializes to bond percolation on random $r$-regular graphs: $\rho_0 \sim 2\varepsilon r/(r-2)$, $\sigma^2 = 2\varepsilon^{-1} r/(r-1)$, $\delta_n \sim (r-1)\varepsilon^2/(2(r-2))$.

## Why it matters here
General background; no direct arena tie. Tangential relevance to extremal-graph / random-graph problems if any arena task touches phase-transition asymptotics, branching-factor heuristics, or exploration-process arguments — the random-walk / exploration framework and the exponential-tilting local-CLT trick are reusable techniques.

## Open questions / connections
- Extends Bollobás–Riordan [6] (G(n,p) random-walk method) to configuration model; could be pushed to unbounded-degree sequences.
- Strongly supercritical regime ($\varepsilon$ not $\to 0$) left for other methods; Riordan suggests small-component approaches are simpler there.
- Joint normality of degree-stratified component counts $L_1(d)$ (sketched via (13)) not fully proved here — natural follow-up.
- Connects to Aldous's multiplicative-coalescent picture of the critical window; the two-parameter family of limiting processes (size + nullity) generalizes Aldous's one-parameter family.

## Key terms
configuration model, giant component, phase transition, scaling window, branching factor, exploration process, random walk, Aldous Brownian excursion, multiplicative coalescent, exponential tilting, Cramér local limit theorem, Berry-Esseen, Bernoulli part, Molloy-Reed, Nachmias-Peres, Bollobás-Riordan, random regular graph percolation, degree sequence
