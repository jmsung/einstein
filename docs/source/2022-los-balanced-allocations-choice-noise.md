---
type: source
kind: paper
title: Balanced Allocations with the Choice of Noise
authors: Dimitrios Los, Thomas Sauerwald
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2206.07503
source_local: ../raw/2022-los-balanced-allocations-choice-noise.pdf
topic: general-knowledge
cites:
---

# Balanced Allocations with the Choice of Noise

**Authors:** Dimitrios Los, Thomas Sauerwald  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2206.07503

## One-line
Analyzes the Two-Choice balls-into-bins process under noisy / outdated / adversarially-perturbed load comparisons, establishing tight gap bounds as a function of noise magnitude $g$.

## Key claim
For Two-Choice under a $g$-bounded adaptive adversary (who can flip the load comparison whenever load difference $\le g$), the gap is $\Theta(g + \frac{\log n}{\log g} \cdot \log\log n)$ w.h.p. for all $m \ge n$, revealing a phase transition at $g \approx \log n$.

## Method
Combines three interacting potential functions — linear (absolute-value $\Delta$), quadratic ($\Upsilon$), and exponential / hyperbolic-cosine ($\Lambda, \Gamma$) — to prove self-stabilization. For sub-logarithmic $g$, employs a **layered induction** over a tower of super-exponential potentials $\Phi_j, \Psi_j$ with smoothing parameter $\alpha_2 (\log n)^{1/k} \cdot g^{j-k}$, refining the technique of Berenbrink–Czumaj–Steger–Vöcking and Talwar–Wieder. Delay/batching settings reduce to a relaxed adversarial-comparison setting.

## Result
Three regimes: (1) $g \gtrsim \log n$: $\text{Gap}(m) = O(g)$, matched by a myopic lower bound; (2) $1 < g \lesssim \log n$: $\text{Gap}(m) = O(\frac{\log n}{\log g} \cdot \log\log n)$, matched below; (3) $g = O(1)$: recovers the classical $\log_2 \log n + O(1)$ Two-Choice gap, showing robustness to constant-load-difference comparison errors. For the $b$-batch setting with $b = n$, improves $O(\log n)$ from [Berenbrink et al. '12] to a tight $\Theta(\frac{\log n}{\log\log n})$.

## Why it matters here
General background; no direct arena tie. None of the 23 Einstein Arena problems are load-balancing / balls-into-bins / power-of-two-choices problems — the techniques (super-martingale potential cascades, layered induction over exponential potentials) don't transfer to sphere packing, autocorrelation, or extremal geometry contexts.

## Open questions / connections
- Tighter analysis for the probabilistic (Gaussian-noise) Noisy-Comp setting — current bounds only show polynomial-in-$\sigma$, poly-log-in-$n$ gap, not tight.
- Whether the layered-induction super-exponential potential machinery extends to graphical / non-uniform-sample variants studied by Peres–Talwar–Wieder.
- Application to the multi-counter distributed data structure of Nadiradze [44] / Alistarh et al. [3] — the improved $g$-Bounded bound here may yield a sharper data-structure analysis.

## Key terms
balls-into-bins, Two-Choice, power-of-two-choices, balanced allocations, gap bound, adversarial noise, $g$-Bounded process, batched allocation, exponential potential function, super-martingale, layered induction, heavily loaded case, Azar–Broder–Karlin–Upfal, Talwar–Wieder
