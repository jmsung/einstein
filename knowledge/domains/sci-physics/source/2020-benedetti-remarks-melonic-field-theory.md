---
type: source
kind: paper
title: Remarks on a melonic field theory with cubic interaction
authors: D. Benedetti, N. Delporte
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2012.12238
source_local: ../raw/2020-benedetti-remarks-melonic-field-theory.pdf
topic: general-knowledge
cites:
---

# Remarks on a melonic field theory with cubic interaction

**Authors:** D. Benedetti, N. Delporte  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2012.12238

## One-line
Revisits the Amit-Roginsky model — a cubic scalar QFT with SO(3) symmetry whose large-$N$ limit is melonic — and extends it with a long-range propagator that yields an exactly marginal coupling and a line of unitary CFTs.

## Key claim
The Amit-Roginsky cubic interaction (mediated by a Wigner 3jm symbol with $N=2j+1$) is dominated by melonic diagrams at large $N$; in the short-range version a real CFT exists for $5.74 < d < 6$ (complex dimensions appear below, via merging of $h_{0,0}$ with its shadow $\tilde h_{0,0}=d-h_{0,0}$), and in the long-range version ($\zeta=d/6$) a real, unitary CFT exists for all $d<6$ at small $|g|$, for either real or imaginary coupling, up to explicit critical couplings.

## Method
Schwinger-Dyson equation for the two-point function under the melonic large-$N$ ansatz $G(p)\sim p^{-d/3}$, yielding a cubic algebraic equation whose solution is the generating function of 3-Catalan (Fuss-Catalan) numbers $Z_{LR}=\sum_n \tfrac{1}{3n+1}\binom{3n+1}{n}(-a)^n$. Combined with $\varepsilon$-expansion beta-function analysis ($d=6-\varepsilon$ short-range, $\zeta=(d+\varepsilon)/6$ long-range) using prior 4-loop multiscalar cubic results, plus conformal partial wave / ladder-kernel diagonalization to extract the spectrum of bilinear operators.

## Result
Short-range fixed points $g_*^\pm = \pm 8\sqrt{2\pi^3\varepsilon} + O(\varepsilon^{3/2})$ with $\eta=\varepsilon/3$; spectrum stays real up to $\varepsilon\sim 0.264$, then $h_{0,0}$ collides with its shadow at $d/2$. Long-range model is exactly marginal at large $N$; explicit critical couplings $g_{c,+}^2 = \lambda^2 Z_{SR}^3$ and $g_{c,-}^2 = -\tfrac12 g_{c,+}^2$ bound the conformal window; numerical merging values $g_{0,0\text{-shadow}}\approx 3.69, 1.57, 0.72, 0.36$ at $d=4,3,2,1$ and $g\approx i15.2$ (imaginary) at $d=5$. Appendix corrects a recurring error: a shadow pole of $\phi^2$ has been mistakenly identified as a $\phi^4$ operator in prior sextic melonic CFT literature.

## Why it matters here
General background; no direct arena tie — this is melonic QFT / SYK-adjacent literature, not optimization. Tangentially relevant to the agent only insofar as Fuss-Catalan / 3-Catalan generating functions and Wigner $3jm$ / $6j$ / $9j$ recoupling identities surface in some combinatorial enumeration problems.

## Open questions / connections
- Rigorous proof of the bound $|\{3nj\}|\lesssim N^{-n+1-\alpha}$ controlling melonic dominance in AR — currently only numerically checked up to $n=6$.
- All-order resummation of the ladder four-point function (extending Usyukina-Davydychev polylogarithmic results) for the long-range propagator $p^{-d/3}$.
- Crossover behavior between long-range and short-range AR analogous to the long-range/short-range Ising crossover (Sak; Behan-Rastelli-Rychkov-Zan), complicated here by the $\phi\partial^2\phi$ operator crossing marginality before the shadow-merging instability.

## Key terms
Amit-Roginsky model, melonic limit, SYK model, tensor models, Wigner 3jm symbol, SO(3) irreducible representation, Fuss-Catalan / 3-Catalan numbers, cubic interaction, Schwinger-Dyson equation, conformal partial wave, shadow operator, Breitenlohner-Freedman bound, long-range propagator
