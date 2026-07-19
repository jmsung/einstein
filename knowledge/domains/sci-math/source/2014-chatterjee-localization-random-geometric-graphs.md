---
type: source
kind: paper
title: Localization in random geometric graphs with too many edges
authors: S. Chatterjee, Matan Harel
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1401.7577
source_local: ../raw/2014-chatterjee-localization-random-geometric-graphs.pdf
topic: general-knowledge
cites:
---

# Localization in random geometric graphs with too many edges

**Authors:** S. Chatterjee, Matan Harel  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1401.7577

## One-line
Proves that a random geometric graph on the $d$-torus, conditioned on having $(1+\delta)$ times its expected edge count, almost surely contains a "giant clique" packed into a single ball of diameter $r_n$, and derives the resulting upper-tail large deviation principle.

## Key claim
Conditional on $|E| > (1+\delta)\mu_n$, with high probability there is a ball $B$ of diameter $r_n$ containing a clique of at least $\sqrt{2\delta\mu_n}(1-\varepsilon)$ vertices distributed roughly uniformly inside $B$; the upper tail satisfies an LDP with speed $\sqrt{\mu_n \log n}$ and rate function $I(x) = \sqrt{2x}\,(2-p)/2$, where $p = \lim \log\mu_n/\log n$. The rate function is non-convex.

## Method
Discretize the torus into an $s$-graded cell model so the edge count becomes a function of i.i.d. Poisson cell counts $X_I$. Combine large-deviation estimates for sums of i.i.d. variables with concentration inequalities (FKG, Chernoff, Talagrand-style localization from spin-glass work) and a deterministic geometric step using the isodiametric inequality + Cauchy's surface-area formula + Hausdorff convergence to show that any cell configuration realizing the rare event must concentrate in an almost-maximal clique set, which converges to a ball.

## Result
Theorem 2.1 gives the localization structure (one ball $B$ contains the excess $\delta\mu_n$ edges; the rest of the graph keeps $\mu_n + o(\mu_n)$ edges). Theorem 2.2 gives $\lim \log P[|E| > (1+\delta)\mu_n] / \sqrt{\mu_n \log n} = -\sqrt{2\delta}\,(2-p)/2$ for admissible $r_n$ with $n^{(\delta_*-2)/d} \le r_n \le n^{-\delta_*/d}$. Lower bound is achieved by explicitly "planting" a clique in one ball; upper bound uses the structure theorem plus a union bound over $m^d \tilde\tau_s$ candidate ball locations.

## Why it matters here
General background; no direct Einstein Arena tie. Closest connections are conceptual: localization-via-planting as a paradigm for rare-event analysis in geometric models (relevant intuition for any packing/covering problem where extremal configurations concentrate), and the isodiametric inequality as the geometric workhorse for "almost-maximal diameter-bounded set ≈ ball" arguments.

## Open questions / connections
- Are there *other* large cliques outside $B$? Theorem 2.1 only bounds other cliques as $o(\sqrt{\mu_n})$; sharpening to "no other clique" is open.
- Lower-tail LDP for $|E| < (1-\delta)\mu_n$ is expected to follow Poisson statistics with speed $\mu_n$ and no localization — not addressed here.
- Extension to other subgraph counts (triangles, $K_k$) in random geometric graphs — the Erdős–Rényi analogue (Lubetzky–Zhao, Bhattacharya–Ganguly–Lubetzky–Zhao, Harel–Mousset–Samotij) is solved but the geometric version is open.
- Replace convexity assumption on probe sets $S$ with a weaker regularity condition.

## Key terms
random geometric graph, Poisson point process, upper tail large deviations, localization, giant clique, isodiametric inequality, Cauchy surface area formula, FKG inequality, Hausdorff convergence, scan statistics, continuum percolation, Chatterjee–Dembo nonlinear large deviations, Erdős–Rényi triangle upper tail, non-convex rate function, s-graded model
