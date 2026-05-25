---
type: source
kind: paper
title: "The lower tail: Poisson approximation revisited"
authors: S. Janson, L. Warnke
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1406.1248
source_local: ../raw/2014-janson-lower-tail-poisson-approximation.pdf
topic: general-knowledge
cites:
---

# The lower tail: Poisson approximation revisited

**Authors:** S. Janson, L. Warnke  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1406.1248

## One-line
Sharpens Janson's inequality for the lower tail $P(X \le (1-\varepsilon)\mathbb{E}X)$ of sums of dependent indicators, proving it is asymptotically optimal in the near-Poisson regime and optimal up to constants when dependencies are weak.

## Key claim
For $X = \sum_{\alpha} I_\alpha$ of the standard "Janson" form with mean $\mu$, max-singleton $\Pi$, and dependency parameter $\delta$: if $\max\{\Pi, \delta\} \le 2^{-14}$ and $\varepsilon^2\mu \ge 1$, then $P(X \le (1-\varepsilon)\mu) \ge \exp(-(1+\xi)\varphi(-\varepsilon)\mu)$ with $\xi = 135\max\{\Pi^{1/8}, \delta^{1/8}, (\varepsilon^2\mu)^{-1/4}\}$ — matching the classical Janson upper bound $\exp(-\varphi(-\varepsilon)\mu)$ where $\varphi(x) = (1+x)\log(1+x) - x$.

## Method
Hölder's inequality (with parameter $p \to 1$ in place of Cauchy-Schwarz) combined with sharp Laplace-transform estimates derived from FKG/Harris correlation inequalities. Key technical move: integrate the logarithmic derivative of $\mathbb{E}e^{-sX}$ over $[r,t]$ rather than $[0,t]$, and careful second-order Taylor control of $\varphi(-\varepsilon)$. For the strongly-dependent case, a "bootstrapping" argument reduces $X_H$ (subgraph count) to a less-dependent surrogate $Y_G$ on a vertex subset, exploiting symmetry.

## Result
Three regimes pinned down. (i) Near-Poisson ($\delta, \Pi \to 0$): rate function is exactly $-\varphi(-\varepsilon)\mu$. (ii) Weakly dependent ($\delta = O(1)$, $\Pi < 1$): rate is $-\Theta(\varepsilon^2\mu)$ with explicit constant $K = 5000/(1-\Pi)^5$. (iii) Subgraph counts $X_H$ in $G(n,p)$: $\log P(X_H \le (1-\varepsilon)\mathbb{E}X_H) = -\Theta(\varepsilon^2 \Phi_H)$ where $\Phi_H = \min_{J\subseteq H} \mathbb{E}X_J$, with sharp constants for balanced $H$ (Theorems 4–5).

## Why it matters here
General background; no direct arena tie. Could inform any future problem involving rare-event probabilities for dependent indicator sums (e.g., counting configurations in random discrete structures, probabilistic existence proofs for extremal combinatorial bounds), but none of the 23 current arena problems is a lower-tail estimation problem.

## Open questions / connections
- Extends Janson–Łuczak–Ruciński (1990) from $\varepsilon = 1$ (non-existence) to all $\varepsilon \in (0,1]$, including $\varepsilon \to 0$.
- Whether analogous sharp bounds hold under Suen's weaker dependency assumptions [Suen 1990; Janson 1998] is left open.
- Removing the spurious $\log(1/\varepsilon)$ factor in Theorem 4's hypothesis is left as an open problem.
- Constant in the "intermediate" $\varepsilon = \Theta(1)$ range for Theorem 5 (where extremal $H$-free structure starts to matter) is undetermined.

## Key terms
Janson's inequality, lower tail, Poisson approximation, large deviations, FKG inequality, Harris inequality, Hölder inequality, Laplace transform, subgraph counts, random graphs $G(n,p)$, dependent indicators, Chernoff bound, hypergraph containers, balanced graphs, arithmetic progressions
