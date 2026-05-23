---
type: source
kind: paper
title: An old approach to the giant component problem
authors: B. Bollobás, O. Riordan
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1209.3691
source_local: ../raw/2012-bollobs-old-approach-giant-component.pdf
topic: general-knowledge
cites:
---

# An old approach to the giant component problem

**Authors:** B. Bollobás, O. Riordan  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1209.3691

## One-line
Proves a strong (exponential large-deviation) version of the Molloy–Reed giant-component theorem for the configuration model under minimal moment conditions, via branching-process approximation plus sprinkling.

## Key claim
If a degree sequence $d_n$ converges to a distribution $D$ with $0 < E(D) < \infty$ (i.e., $n_i(d_n)/|d_n| \to r_i = P(D=i)$ and $m(d_n)/|d_n| \to E(D)/2$), then $L_1(G_{d_n})/|d_n| \to_p \rho(D)$ where $\rho(D) = P(|T_D|=\infty)$ is the survival probability of the associated Galton–Watson tree $T_D$ with size-biased offspring $Z_D$ (offspring law $P(Z_D=i)=(i+1)r_{i+1}/E(D)$); deviations $\geq \varepsilon n$ have probability $\leq e^{-\delta n}$.

## Method
Three ingredients: (1) couple the local neighborhood $\Gamma_t(v)$ of a random vertex in the configuration multigraph $G^*_d$ to $T_D|_t$, giving $E[N_P(G^*_d)] \approx n \cdot P(T_D \in P)$ for any local property $P$; (2) Hoeffding–Azuma on a switching-martingale over pairings, made Lipschitz by restricting to vertices whose $t$-neighborhood has max degree $\leq \Delta$ (the property $M_{\Delta,t}$); (3) Erdős–Rényi-style sprinkling — split edges by 2-coloring at rate $p$, find "usable" helpful vertices in the red giant, then use blue edges as sprinkled bridges to rule out bad cuts. Simple-graph case follows because $P(G^*_d \text{ simple}) \geq e^{-o(n)}$.

## Result
Theorem 2: for $D \in \mathcal{D}$ with $P(D \geq 3) > 0$ and $\varepsilon > 0$, there exists $\delta > 0$ such that $d_{\text{conf}}(d, D) < \delta$ implies $P(|L_1(G_d) - \rho(D)n| \geq \varepsilon n) \leq e^{-\delta n}$, $P(L_2 \geq \varepsilon n) \leq e^{-\delta n}$, and analogously for $N_k$ and any local property $P$ (Theorem 25 — counts in the giant). The survival probability satisfies $\rho(D) > 0 \iff E(D(D-2)) > 0$, with $\rho(D) = 1 - \sum_i r_i (1-x_+)^i$ where $x_+$ is the largest root in $[0,1]$ of $x = 1 - \sum_{i\geq 1} (ir_i/E(D))(1-x)^{i-1}$. Percolation threshold (Remark 23): $p_c = E(D)/E(D(D-1))$.

## Why it matters here
General background; no direct arena tie. Configuration-model giant-component asymptotics are not among the 23 Einstein Arena problems (sphere packing, kissing, autocorrelation, etc.); the branching-process + sprinkling toolkit could inform extremal-graph problems if one arises, but no current problem in the wiki uses this machinery.

## Open questions / connections
- Extends Molloy–Reed [12], Janson–Luczak [9], Fountoulakis [5] by dropping max-degree / second-moment conditions while gaining exponential concentration.
- Unbounded local functionals (e.g., $\sum_{v \in C_1} d(v)^2$) need separate moment control — paper leaves general $L^p$ extensions unstated.
- Sparse regime $m(d_n)/n \to \infty$ with vanishing $p_n$ (Remark 24) — percolation on dense configuration graphs reduces to the bounded-mean case via $p$-thinning, but a unified statement is not given.

## Key terms
giant component, configuration model, Molloy–Reed, Galton–Watson branching process, size-biased distribution, survival probability, sprinkling, Erdős–Rényi, Hoeffding–Azuma, switching martingale, local weak convergence, percolation threshold, Bollobás, Janson–Luczak
