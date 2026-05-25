---
type: source
kind: paper
title: Generalized Collatz Maps with Almost Bounded Orbits
authors: Felipe Gonçalves, Rachel Greenfeld, Jose Madrid
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2111.06170v2
source_local: ../raw/2021-gonalves-generalized-collatz-maps-almost.pdf
topic: general-knowledge
cites: 
---

# Generalized Collatz Maps with Almost Bounded Orbits

**Authors:** Felipe Gonçalves, Rachel Greenfeld, Jose Madrid  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2111.06170v2

## One-line
Generalizes Tao's "almost all Collatz orbits attain almost bounded values" breakthrough from the classical $3N+1$ map to a wide family of Collatz-like maps $C(N)=N/p$ or $qN+r(j)$ depending on $N\bmod p$.

## Key claim
For $C_{p,q,r}$ with (a) $\gcd(p,q)=1$, (b) $q<p^{p/(p-1)}$, (c) $qj+r(j)\not\equiv 0\pmod p$: for every growth function $f(N)\to\infty$, the sets $\{N:S_{\min}(N)>f(N)\}$ and $\{N:C_{\min}(N)>f(N)\}$ have zero logarithmic density. Quantitatively, for every $\delta>0$ there is $B_\delta$ with $\sum_{N\le x,\,C_{\min}(N)<B_\delta}1/N\ge(1-\delta)\log x$.

## Method
Reduces the dynamics to a Syracuse-style map on $\mathbb{N}\setminus p\mathbb{N}$ and studies the $p$-adic valuation sequence of iterates as a 2D arithmetic renewal process $X_{1,k}=\sum X_j$ with i.i.d. heavy-tailed-but-exponentially-bounded increments. Extracts from Tao's proof a modular "triangle-avoiding renewal" black-box (Theorem 1.9): bounds the expected time the walk spends in a disjoint union of triangles $\Delta(j_\Delta,l_\Delta,s_\Delta)$ with slope $\eta<\omega=E[L]/E[J]$, uniformly separated by $\log(1/\varepsilon)$. Combines this with Fourier/character-sum estimates on $\xi r(j_0)(p-1)(p^{1-l}\bmod q^n)/q^{2B+2}$ to handle non-prime $q$.

## Result
Theorem 1.3 (log-density "almost bounded orbits") under (a)+(b)+(c); Theorem 1.8 (natural-density variant): if also $r(j)\ge 0$, then $\{N:C_{\min}(N)<N^{\gamma+c}\}$ has natural density 1, where $\gamma=\tfrac{p}{p-1}\log_p q<1$. Theorem 1.9 (renewal black-box): $E[\#\{k\in[n]:X_{1,k}\in B\}]\le n-A\log n+O_{A,\varepsilon}(1)$, with stronger exponential moment bound $\le n^{-A}$. Conjecture 1.5 asserts genuinely bounded orbits under the same conditions (numerics in §8 support it; counter-examples to converses given).

## Why it matters here
General background; no direct arena tie — Collatz dynamics, $p$-adic valuation renewal, and Conway's FRACTRAN undecidability are outside the current 23 problems (sphere packing, kissing, autocorrelation, extremal graphs, sieves). The two-dimensional triangle-avoiding renewal theorem (Theorem 1.9) is the only piece with potential cross-pollination — as a probabilistic tool for "walk avoids bad regions" estimates that could conceivably appear in extremal combinatorics or random-construction arguments.

## Open questions / connections
- Strengthen log-density → natural density for arbitrary $f(N)\to\infty$ (out of reach).
- Generalize Krasikov–Lagarias $\#\{N\le x:T_{\min}(N)=1\}\gtrsim x^{0.841}$ to this class.
- Conjecture 1.5: do (a)+(b)+(c) suffice for genuine boundedness? Numerically yes for $2\le p\le q\le 10^2$.
- Existence/uniqueness of an attracting limiting random variable for orbit-sequences viewed in $\{0,1\}^\mathbb{N}$.
- Extends Tao 2022 (Forum of Math Pi) and the Matthews–Watts (1984) framework; sits inside Conway's FRACTRAN universe (undecidability is the structural obstruction).

## Key terms
Collatz conjecture, Syracuse map, FRACTRAN, $p$-adic valuation, renewal process, logarithmic density, natural density, triangle-avoiding random walk, Matthews-Watts maps, Tao breakthrough, Krasikov-Lagarias, Korec density, two-dimensional renewal, exponential tail bound
