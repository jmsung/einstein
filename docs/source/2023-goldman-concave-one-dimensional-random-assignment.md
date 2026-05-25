---
type: source
kind: paper
title: On the concave one-dimensional random assignment problem and Young integration theory
authors: M. Goldman, Dario Trevisan
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2305.09234
source_local: ../raw/2023-goldman-concave-one-dimensional-random-assignment.pdf
topic: general-knowledge
cites:
---

# On the concave one-dimensional random assignment problem and Young integration theory

**Authors:** M. Goldman, Dario Trevisan  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2305.09234

## One-line
Establishes limit laws for the 1D random bipartite assignment cost under concave power cost $|x-y|^\alpha$, $\alpha \in (0,1)\setminus\{1/2\}$, introducing a Kantorovich–Young variant of optimal transport to handle the $\alpha > 1/2$ regime.

## Key claim
For i.i.d. samples $(X_i),(Y_i)$ with law $\mu$ on a bounded interval: if $\alpha \in (1/2,1)$, then $n^{-1/2} M_\alpha \to \|\sqrt{2}\,B\circ F\|_{W^\alpha}$ in law (Brownian bridge $B$); if $\alpha \in (0,1/2)$ with sufficient moments, $n^{\alpha-1} M_\alpha \to c(M_\alpha)\int_I f^{1-\alpha}(t)\,dt$ almost surely. The $\alpha=1/2$ case has matching $\sqrt{n\log n}$ lower bound via a Peano space-filling-curve argument.

## Method
Two regimes, two techniques. For $\alpha > 1/2$: define a Kantorovich–Young transport problem $\|g\|_{W^\alpha} = \sup\{\int f\,dg : \|f\|_{C^\alpha}\le 1\}$ via Young integration ($\alpha + 1/q > 1$, $q$-variation finite) applied to the Brownian-bridge limit of the empirical CDF difference $\sqrt{n}(F_n - \tilde F_n)$, with quantitative KMT-style coupling from Huang–Dudley. For $\alpha < 1/2$: boundary-functional reduction using the no-crossing property of optimal concave assignments (Lemma 3.5) plus existing complete-convergence results from Barthe–Bordenave.

## Result
Theorem 1.1 gives convergence in law (and in expectation) of $n^{-1/2} M_\alpha$ for $\alpha \in (1/2,1)$, and complete convergence of $n^{\alpha-1} M_\alpha$ for $\alpha \in (0,1/2)$ to an explicit density integral $c(M_\alpha)\int f^{1-\alpha}$. A parallel result (Theorem 5.2) holds for the bipartite Traveling Salesperson Problem with factor 2 and constant $c(\mathrm{TSP}_\alpha)$. Duality (Prop 4.1): $\|g\|_{W^\alpha} = \min_{\pi \in \Gamma_\alpha(g)} \int |t-s|^\alpha\,\pi(ds,dt)$ with $\alpha$-monotone support of optimal couplings.

## Why it matters here
General background; no direct arena tie. The Young-integration / rough-paths framing of the $\alpha=1/2$ phase transition is a transferable lens for any optimization where empirical-process fluctuations (CLT-scale Brownian bridge) replace measure differences — potentially relevant to autocorrelation or 1D extremal problems with concave costs.

## Open questions / connections
- $\alpha = 1/2$ critical case: existence of $\lim E[M_{1/2}]/\sqrt{n\log n}$ remains open; matching upper (Bobkov–Ledoux) and lower bounds known.
- Extension to unbounded support requires growth conditions on Kantorovich–Young and KMT couplings (Huang–Dudley [23]).
- Connected bipartite $\kappa$-factor problem conjectured to admit the same analysis ($\kappa=2$ recovers TSP).
- Connects to rough-paths theory (Friz–Hairer, Friz–Victoir) as a stochastic-analysis explanation of the $\alpha=1/2$ phase transition.

## Key terms
random assignment problem, bipartite matching, concave cost, Young integration, $q$-variation, Kantorovich–Young problem, Brownian bridge, empirical process, optimal transport, no-crossing rule, boundary functional, Traveling Salesperson Problem, KMT coupling, rough paths, Hölder continuity
