---
type: source
kind: paper
title: Private selection from private candidates
authors: Jingcheng Liu, Kunal Talwar
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1811.07971
source_local: ../raw/2018-liu-private-selection-private-candidates.pdf
topic: general-knowledge
cites:
---

# Private selection from private candidates

**Authors:** Jingcheng Liu, Kunal Talwar  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1811.07971

## One-line
Algorithms for differentially-private selection among $K$ candidates when the candidate score functions are themselves differentially private (not just Lipschitz), at only a factor-2 privacy overhead and $\tilde{O}(K)$ oracle calls.

## Key claim
Given $K$ candidate mechanisms $M_i$ that are each $\varepsilon_1$-DP, one can output a sample $(x,q)$ competitive with $\max_i \text{Median}(M_i(D))$ while preserving $(2\varepsilon_1+\varepsilon_0)$-DP — only a factor-2 loss vs. the $\varepsilon_1$-DP of a single candidate, and this factor of 2 is shown to be tight (Theorem D.2).

## Method
Boost a trivially-private but useless baseline (pick $i$ uniform, sample $m\sim M_i(D)$) into a useful one via two devices: (i) **thresholding with geometric stopping** — resample until $q\ge\tau$ or a $\gamma$-coin halts (Alg. 1), and (ii) **random stopping without thresholds** — sample until a $\gamma$-coin halts, then output the running max (Alg. 2). Privacy follows from explicit probability-ratio bounds on the stopping-time mixture; an online "private sparse vector" variant (Theorem 1.5) generalizes the sparse-vector technique to the DP-stability setting.

## Result
- **Known-$\tau$ (Thm 1.2 / 3.1):** $(2\varepsilon_1)$-DP, returns $q\ge\tau$ if any candidate has median $\ge\tau$, expected calls $\le 2K$.
- **Random-stop (Thm 1.3 / 3.2):** $(3\varepsilon_1)$-DP, expected calls $\le 1/\gamma$, output is best-seen sample.
- **Two-$\varepsilon_1$ general (Thm 1.4):** $(2\varepsilon_1+\varepsilon_0,\delta)$-DP, $x$ has score $\ge \tau^*-1/R$ except w.p. $\beta+\delta/R$, with $T = O\!\left(K \cdot \tfrac{6+12\varepsilon_1/\varepsilon_0}{\beta} \ln \tfrac{R}{\delta\varepsilon_0^2} + \tfrac{R+1}{\beta^2}\right)$ oracle calls.
- **Lower bound (Thm D.2):** any $K^{-\alpha}$-weakly-useful selector must lose factor $\ge 2(1-3\alpha)$ in $\varepsilon$ — the 2× overhead is unavoidable.

## Why it matters here
General background; no direct arena tie. Tangentially informs the **autonomous-loop / hyperparameter-selection** layer if the agent ever needs to choose among private candidate optimizers/scorings with formal privacy — not the math-wisdom layer for sphere-packing / autocorrelation problems. Useful as a pattern: "boost a trivial private baseline by random-stopping" is a clean composition trick worth knowing.

## Open questions / connections
- Generalizes the Exponential Mechanism (McSherry–Talwar 2007) and Raskhodnikova–Smith's generalized exponential mechanism to private (not Lipschitz) scores; can it recover smoothed-sensitivity Exponential mechanism unconditionally?
- Extends Gupta–Ligett–McSherry–Roth–Talwar 2010 private-amplification (Appendix C improves their bound from quadratic to near-linear oracle calls).
- Connection to adaptive data analysis "garden of forking paths" (Gelman–Loken) — selection cost collapses from $K$ queries to $O(1)$.

## Key terms
differential privacy, private selection, exponential mechanism, sparse vector technique, hyperparameter selection, private amplification, max-divergence, Laplace mechanism, propose-test-release, smoothed sensitivity, adaptive data analysis, McSherry-Talwar
