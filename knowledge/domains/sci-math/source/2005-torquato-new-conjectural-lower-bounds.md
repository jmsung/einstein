---
type: source
kind: paper
title: New Conjectural Lower Bounds on the Optimal Density of Sphere Packings
authors: S. Torquato, F. Stillinger
year: 2005
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/math/0508381
source_local: ../raw/2005-torquato-new-conjectural-lower-bounds.pdf
topic: general-knowledge
cites:
---

# New Conjectural Lower Bounds on the Optimal Density of Sphere Packings

**Authors:** S. Torquato, F. Stillinger  ·  **Year:** 2005  ·  **Source:** https://arxiv.org/abs/math/0508381

## One-line
Conjectures that disordered sphere packings in high dimensions can exponentially improve Minkowski's 1905 lower bound on $\varphi_{\max}$, via a dual of the Cohn–Elkies LP.

## Key claim
Under the conjecture that any hard-core nonnegative tempered $g_2$ with nonnegative structure factor $S(k) \geq 0$ is realizable as a translationally invariant disordered packing for large $d$, $\varphi_{\max} \geq 3.276\, d^{1/6}\, 2^{-0.77865\ldots d}$ — the first putative exponential improvement on Minkowski's $2^{-d}$ in 100 years.

## Method
Dual of the Cohn–Elkies primal LP: choose a test radial distribution $g_2(r)$ with $g_2(r)=0$ for $r<1$ (hard core), satisfying $g_2 \geq 0$ and $S(k) = 1 + \rho \tilde h(k) \geq 0$ (the two standard realizability conditions), then push the density $\rho$ up to a "terminal" value where $S(k_{\min})=0$. Specific family: step-plus-gap test functions; asymptotic analysis uses Bessel-zero expansions $x_0 = \nu + a_1\nu^{1/3} + \cdots$ with $\nu = d/2$.

## Result
The optimal terminal density has asymptotic form $\varphi^* \sim 3.276\, d^{1/6}\, 2^{-0.77865\ldots d}$, with a paired conjectural average kissing-number bound $Z_{\max} \geq 40.25\, d^{1/6}\, 2^{0.22134\ldots d}$ — beating Wyner's best individual-kissing bound $2^{0.2075\ldots d}$. By LP duality, this terminal density can never exceed the Cohn–Elkies upper bound, regardless of the conjecture's validity, and proves LP bounds cannot match Minkowski for any $d$.

## Why it matters here
Direct foundation for any sphere-packing / kissing-number arena problem in moderate-to-high $d$: gives the canonical "decorrelation principle" framing and the $S(k) \geq 0$ realizability conditions that underpin LP-bound techniques. Pairs with `findings/`/`concepts/` on Cohn–Elkies, LP duality, and Viazovska-era magic functions.

## Open questions / connections
- Is the realizability conjecture true? Suffices to show $g_2 \geq 0$ and $S(k) \geq 0$ imply existence of *some* point process at sufficiently low density.
- Can the step-plus-gap test function be improved (e.g., positive function $<1$ on $1 \leq r \leq \sigma$) to lift the $0.77865$ exponent further?
- Constructive disordered packings exceeding $1/2^d$ for large $d$ — open challenge.
- Extends Cohn–Elkies (CE03) duality; relates to Koralov's pair-potential existence for lattices.

## Key terms
sphere packing, Minkowski bound, Cohn–Elkies, linear programming duality, structure factor, pair correlation function, realizability, Wiener–Khintchine, kissing number, decorrelation principle, tempered distribution, disordered packings, Bessel zeros, terminal density, Torquato–Stillinger
