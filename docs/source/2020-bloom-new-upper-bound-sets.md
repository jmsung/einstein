---
type: source
kind: paper
title: A new upper bound for sets with no square differences
authors: Thomas F. Bloom, James Maynard
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2011.13266v2
source_local: ../raw/2020-bloom-new-upper-bound-sets.pdf
topic: general-knowledge
cites: 
---

# A new upper bound for sets with no square differences

**Authors:** Thomas F. Bloom, James Maynard  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2011.13266v2

## One-line
Improves the Pintz–Steiger–Szemerédi upper bound on the largest subset of $\{1,\dots,N\}$ whose difference set avoids non-zero squares, replacing one $\log\log$ in the denominator's exponent with a $\log\log\log$.

## Key claim
If $A\subset\{1,\dots,N\}$ has no solutions to $a-b=n^2$ with $a,b\in A$, $n\geq 1$, then $|A| \ll N/(\log N)^{c\log\log\log N}$ for some absolute constant $c>0$ — strictly stronger than the previous $N/(\log N)^{c\log\log\log\log N}$ bound of Pintz–Steiger–Szemerédi (1988).

## Method
Fourier-analytic density-increment argument via the circle method, in the lineage of Sárközy. The key new ingredient (Theorem 2) is an upper bound on the $2m$-fold additive energy $E_{2m}(B)$ of sets $B\subset\mathbb{Q}_{\leq Q}$ of rationals with bounded multiplicity per denominator: $E_{2m}(B)\leq (\log Q)^{C^m}(Qn)^m$, established by an iterative "few solutions to linear equations in small-denominator rationals" lemma (Lemma 1) plus a Chang-type lemma (Lemma 7) relating large Fourier coefficients to approximate additive energy. The energy bound is non-trivial up to $m\sim c\log\log Q$, which is what powers the improved increment $\rho\approx\exp(-C\log(1/\alpha)/\log\log(1/\alpha))$.

## Result
For any $A\subset\{1,\dots,N\}$ with no non-zero square differences, $|A|/N \ll (\log N)^{-c\log\log\log N}$. Best known lower bound (Ruzsa, Lewko) is $r(N)\gg N^{0.73}$ — gap to truth (between $N^{1-o(1)}$ and $N^{1-c}$) remains open. The function-field analogue (Green) achieves $|A|\ll q^{(1-c(q))n}$ via the polynomial method.

## Why it matters here
General background; no direct arena tie. The additive-energy / density-increment toolkit (Chang's lemma variants, dissociated-set bounds, circle-method major-arc analysis) is the same machinery used for Roth-type problems and could inform any arena problem involving sumset structure or autocorrelation of integer/rational sets.

## Open questions / connections
- True order of $r(N)$: is it $N^{1-o(1)}$ or $N^{1-c}$? Wide gap between $N^{0.73}$ lower and $(\log N)^{-c\log\log\log N}$ upper.
- Extending the technique to differences of the form $f(n)$ for intersective polynomials $f\in\mathbb{Z}[x]$ (Rice 2019, Balog–Pelikan–Pintz–Szemerédi 1994) — authors note this should be feasible but don't pursue it.
- Theorem 2 is independent-interest: dissociated-set-like energy bounds for small-denominator rationals; cf. Bourgain–Dilworth–Ford–Konyagin–Kutzarova for RIP matrix constructions.

## Key terms
Sárközy theorem, Furstenberg, square differences, density increment, circle method, additive energy, Chang's lemma, dissociated sets, Fourier analysis, major arcs, Weyl sum, Gauss sum, Pintz-Steiger-Szemerédi, divisor function, intersective polynomial
