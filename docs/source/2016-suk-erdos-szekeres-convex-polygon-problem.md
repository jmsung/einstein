---
type: source
kind: paper
title: On the Erdos-Szekeres convex polygon problem
authors: Andrew Suk
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1604.08657
source_local: ../raw/2016-suk-erdos-szekeres-convex-polygon-problem.pdf
topic: general-knowledge
cites:
---

# On the Erdos-Szekeres convex polygon problem

**Authors:** Andrew Suk  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1604.08657

## One-line
Nearly settles the 1935 Erdős–Szekeres conjecture by proving that any $2^{n+o(n)}$ points in general position in the plane contain $n$ points in convex position.

## Key claim
For all $n \geq n_0$ (a large absolute constant), $ES(n) \leq 2^{n + 6n^{2/3}\log n}$, matching the conjectured lower bound $ES(n) \geq 2^{n-2} + 1$ up to a sub-exponential factor. This replaces the previous $\approx 4^n/\sqrt{n}$ upper bound that had stood with only constant-factor improvements since 1935.

## Method
Combines the positive-fraction Erdős–Szekeres theorem of Pór–Valtr (extract a $(k+3)$-cap/cup whose support regions each hold a $\geq N/2^{40k}$ fraction of points) with Dilworth's theorem applied to a natural partial order $\prec$ inside each support region. A two-case dichotomy — many antichains (giving disjoint caps that merge via support geometry) versus consecutive long chains (giving nested left-caps/right-caps that combine via Observation 3.1) — drives an inductive bootstrap using the cups-caps theorem $f(k,\ell) = \binom{k+\ell-4}{k-2}+1$ at each step. Sets parameter $k = \lceil n^{2/3}\rceil$ to balance the two cases.

## Result
$ES(n) \leq 2^{n + 6n^{2/3}\log n}$, so $\limsup \log_2 ES(n)/n = 1$, matching the lower bound $2^{n-2}+1$. The concluding remark notes Gábor Tardos subsequently improved the lower-order term to $2^{n + O(\sqrt{n\log n})}$. Closes (asymptotically in the exponent) the 80-year gap between $2^{n-2}$ and $\binom{2n-4}{n-2} \approx 4^n/\sqrt{n}$.

## Why it matters here
General background for extremal/discrete-geometry problems involving convex position, cups/caps, and Ramsey-style point-configuration arguments; informs the cups-caps + positive-fraction toolkit useful for any arena problem about forced convex sub-configurations. No direct tie to the current 23 arena problems unless one involves planar convex-position extraction.

## Open questions / connections
- Exact value of $ES(n)$ — the conjectured $2^{n-2}+1$ is still open; this work only matches the exponent.
- Higher-dimensional analogues ($ES_d(n)$ for $d \geq 3$, see Károlyi–Valtr, Suk) where bounds remain much weaker.
- Variants for families of convex bodies and order types (Dobbins–Holmsen–Hubard, Fox–Pach–Sudakov–Suk) — does the same dichotomy framework transfer?
- Tightening lower-order term beyond Tardos's $O(\sqrt{n\log n})$.

## Key terms
Erdős–Szekeres conjecture, convex position, cups and caps, $ES(n)$, positive-fraction Erdős–Szekeres, Pór–Valtr theorem, Dilworth's theorem, transitive 2-coloring, Ramsey theory, extremal discrete geometry, convex polygon, planar point sets in general position
