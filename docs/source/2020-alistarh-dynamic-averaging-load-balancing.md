---
type: source
kind: paper
title: Dynamic Averaging Load Balancing on Cycles
authors: Dan Alistarh, Giorgi Nadiradze, Amirmojtaba Sabour
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2003.09297
source_local: ../raw/2020-alistarh-dynamic-averaging-load-balancing.pdf
topic: general-knowledge
cites:
---

# Dynamic Averaging Load Balancing on Cycles

**Authors:** Dan Alistarh, Giorgi Nadiradze, Amirmojtaba Sabour  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2003.09297

## One-line
Proves an $O(\sqrt{n}\log n)$ upper bound on the expected max–min load gap for dynamic continuous-averaging load balancing on an $n$-cycle, via a new $k$-hop potential and a recursive "gap covering" argument.

## Key claim
For the process where each step inserts a unit weight at a random node and averages with a random neighbor on the cycle $C_n$, $\mathbb{E}[\mathrm{Gap}(t)] = O(\sqrt{n}\log n)$, and $\mathbb{E}[\mathrm{Gap}(t)^2] = \Omega(n)$ — improving the previously best $O(n\log n)$ bound from Peres–Talwar–Wieder.

## Method
Introduces a parametrized $k$-hop potential $\phi_k(t) = \sum_i (x_i(t)-x_{i+k}(t))^2$ measuring squared load differences between $k$-hop neighbors. Derives a linear recurrence on $\mathbb{E}[\phi_k]$ (each step couples $\phi_k$ to $\phi_{k-1},\phi_{k+1},\phi_1$) and shows $\mathbb{E}[\phi_k(t)] \le k(n-k)-1$ via a comparison/induction argument on the vector $Y - \Phi(t)$. A "gap covering" recursion on sets $A^i_k = \{i, i+2^k, i+2\cdot 2^k,\dots\}$ then bootstraps pointwise gap bounds from these potentials, plus Cauchy–Schwarz to convert $\ell_2$ to $\ell_\infty$.

## Result
Upper bound: $\mathbb{E}[\mathrm{Gap}(t)] = O(\sqrt{n}\log n)$ on $C_n$ in the dynamic, heavily-loaded continuous-averaging regime, with weight distributions of bounded second moment. Matching lower bound on the second moment: $\lim_{t\to\infty}\mathbb{E}[\mathrm{Gap}(t)^2] = \Omega(n\mathbb{E}[W^2])$. Experiments on unit-weight runs show $\mathrm{Gap}(t)/\sqrt{n} \in [1, 1.4]$ at steady state, supporting a conjectured $\Theta(\sqrt{n})$ truth. Extends to Harary graphs (adding 2-hop edges) with the same $O(\sqrt{n}\log n)$ bound and a $2/5$-improved constant on $\phi_k$.

## Why it matters here
General background; no direct arena tie. Could inform any future combinatorial/discrete-geometry problem where local averaging on a low-expansion graph induces a global imbalance ($k$-hop quadratic potentials + gap-covering recursion is a transferable analysis template), but none of the 23 current arena problems is a load-balancing instance.

## Open questions / connections
- Is the true expected gap $\Theta(\sqrt{n})$ (closing the log gap between upper bound and second-moment lower bound)?
- Does the same template extend to grids and general regular expanders — what is the right $k$-hop bound and set family for each?
- Majorization argument linking pure-averaging gap to $(1+\beta)$-choice gap on cycles — would transfer the $\Omega(\sqrt{n})$ second-moment lower bound to two-choice.
- Sharpens prior majorization-via-clique reduction of Peres–Talwar–Wieder for low-expansion graphs; complements Sauerwald–Sun static-discrete bounds.

## Key terms
dynamic load balancing, continuous averaging, cycle graph, $k$-hop potential, gap covering, spectral gap, two-choice process, majorization, Peres–Talwar–Wieder, Sauerwald–Sun, Harary graph, heavily-loaded balls-into-bins
