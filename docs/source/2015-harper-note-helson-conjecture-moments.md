---
type: source
kind: paper
title: A note on Helson's conjecture on moments of random multiplicative functions
authors: Adam J. Harper, A. Nikeghbali, Maksym Radziwill
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1505.01443
source_local: ../raw/2015-harper-note-helson-conjecture-moments.pdf
topic: general-knowledge
cites:
---

# A note on Helson's conjecture on moments of random multiplicative functions

**Authors:** Adam J. Harper, A. Nikeghbali, Maksym Radziwill  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1505.01443

## One-line
Proves new lower bounds and exact asymptotics for moments of partial sums $\sum_{n\le N} f(n)$ of Rademacher and Steinhaus random multiplicative functions, providing strong evidence against Helson's conjectured $o(\sqrt N)$ cancellation in the first absolute moment.

## Key claim
For $f(n)$ Rademacher or Steinhaus, $\mathbb{E}|\sum_{n\le N} f(n)| \gg \sqrt N (\log\log N)^{-3+o(1)}$, and the $2q$-th moments satisfy $\mathbb{E}|\sum_{n\le N} f(n)|^{2q} \gg N^q (\log\log N)^{-6+o(1)}$ for $0\le q\le 1$. For Steinhaus and integer $k\ge1$, $\mathbb{E}|\sum_{n\le N} f(n)|^{2k} \sim \gamma_k\, c_k\, N^k (\log N)^{(k-1)^2}$ where $\gamma_k$ involves the Birkhoff polytope volume and $c_k$ is an explicit Euler product.

## Method
A Halász-style Dirichlet-series / Euler-product lower bound transfers a supremum of $\sum_p f(p)\cos(t\log p)/p^{1/2+1/\log x}$ (from Harper 2013 on suprema of Gaussian processes) into a lower bound on integral averages of $\mathbb{E}|\sum_{n\le z} f(n)|$. A new "physical-space" decomposition splitting by largest prime factor $p>\sqrt x$, combined with Khintchine's inequality and symmetry/conditioning ($\mathbb{E}|X+Y| \ge \mathbb{E}|Y|$ via independent sign), upgrades the integral-average bound to a pointwise lower bound. Even-moment asymptotics use La Bretèche's theorem on multidimensional Dirichlet series with linear-form denominators, reducing the volume computation to the Birkhoff polytope $B_k$.

## Result
First absolute moment is at least $\sqrt N/(\log\log N)^{3+o(1)}$ for all large $N$ (improving Bondarenko–Seip's $\sqrt N(\log N)^{-\alpha}$). Even integer moments have leading constant $k^{-(k-1)} \binom{2k-2}{k-1} c_k \mathrm{Vol}(B_k)$ with logarithmic exponent $(k-1)^2$. Rademacher $k$-th moments ($k\ge 3$) scale as $N^{k/2}(\log N)^{k(k-3)/2}$. These bounds disprove the size predicted by Helson's conjecture (1) of $o(\sqrt N)$.

## Why it matters here
General background for the **autocorrelation/multiplicative-function** family — supplies sharp moment-method scaffolding (Halász Dirichlet-series transfer, largest-prime-factor decomposition, Khintchine, Cauchy–Schwarz between moments) reusable for Sidon-set and autocorrelation problems where partial sums of $\pm 1$-valued functions must be lower-bounded. The Birkhoff-polytope/Dirichlet-series-volume technique connects to LP/extremal counting routines.

## Open questions / connections
- Conjecture 1: $\mathbb{E}|\sum_{n\le N} f(n)|^{2q} \sim C(q) N^q$ for $0\le q\le 1$ and $\sim C(q) N^q (\log N)^{(q-1)^2}$ for $q\ge 1$ — non-integer $q$ behaviour wide open, especially $0<q<1$.
- Closed-form volume of Birkhoff polytope $B_k$ — open in enumerative combinatorics (Pak's "Four Questions").
- Implications for nonvanishing of $\theta(1,\chi)$ for a positive proportion of even Dirichlet characters mod $p$ via first-vs-second moment comparison.

## Key terms
random multiplicative function, Rademacher, Steinhaus, Helson conjecture, moments, Birkhoff polytope, Halász inequality, Dirichlet series, Euler product, Khintchine inequality, La Bretèche, Nehari theorem, theta functions, multiplicative chaos
