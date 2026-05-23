---
type: source
kind: paper
title: Density criteria for Fourier uniqueness phenomena in $\mathbf{R}^d$
authors: Anshul Adve
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2306.07475
source_local: ../raw/2023-adve-density-criteria-fourier-uniqueness.pdf
topic: general-knowledge
cites:
---

# Density criteria for Fourier uniqueness phenomena in $\mathbf{R}^d$

**Authors:** Anshul Adve  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2306.07475

## One-line
Proves that whether a discrete set $A \subseteq \mathbf{R}^d$ is a Fourier uniqueness set is determined by its density, with a sharp critical threshold $\{|n|^{-1/2}n : n \in \mathbf{Z}^d\}$ in all dimensions.

## Key claim
For closed discrete $A,B \subseteq \mathbf{R}^d$ that are $(p,\delta)$- and $(q,\delta)$-dense/separated: if $pq<1$ (subcritical), $F_{A,B}: f \mapsto (f|_A, \hat{f}|_B)$ is surjective (with infinite-dim kernel); if $pq>1$ (supercritical), $F_{A,B}$ is injective (with infinite-dim cokernel) for $\delta$ small. The diagonal critical density is $\{|n|^{-1/2}n\}$, generalizing Radchenko–Viazovska's $\{\pm\sqrt{n}\}$ in $d=1$ to all dimensions.

## Method
Purely real-variable / analytic — no modular forms, no spherical symmetry. Construction of an explicit parametrix $P$ for $F_{A,B}$ (or its dual) using Schwartz bumps adapted to balls of radius $\sim \langle a_0\rangle^{-p}$ around each lattice point, iterated via the Neumann series $\sum (1-F_{A,B}P)^j$; "shrinking essential support" closes the iteration when $pq<1$. For injectivity, a variably-rescaled Gabor transform decomposes functions into wave packets adapted to $B_{R_{y,\eta}}(y) \times B_{R_{y,\eta}^{-1}}(\eta)$ with $R_{y,\eta} = \langle y\rangle^{1/2}/\langle\eta\rangle^{1/2}$, combined with a twisted Poisson summation formula and stationary/non-stationary phase estimates on a three-regime split of dual-lattice indices.

## Result
Theorems 1.3–1.6 cover all four regimes (sub/supercritical × sparse/dense critical). Concretely (Cor. 1.7): for $t+u=1$ and $A = \{\delta|n|^{t-1}n\}$, $B = \{\delta|n|^{u-1}n\}$ in $\mathbf{Z}^d$, $(A,B)$ is a Fourier uniqueness pair when $\delta$ is sufficiently small, and has infinite-dim kernel when $\delta$ is large. Yields the simplest known higher-dim discrete Fourier uniqueness sets with $\sim R^{2d}$ points in the ball of radius $R$ (taking $p=q=1$); these are optimally well-separated up to constants. First purely analytic construction of discrete Fourier uniqueness pairs in $d>1$ (prior $d>1$ work was algebraic/modular).

## Why it matters here
General background — Fourier uniqueness / interpolation is the analytic engine behind universal optimality of $E_8$ and Leech (Cohn–Kumar–Miller–Radchenko–Viazovska), which directly informs sphere-packing problems in the arena. The density threshold $\{|n|^{-1/2}n\}$ and the parametrix/Gabor-transform technology are reusable framing for any problem family where "density vs structure" governs solvability (LP duality bounds, magic-function constructions, autocorrelation extremal problems).

## Open questions / connections
- Exact value of $\delta_{\text{crit}}$ in higher dimensions — Kulikov–Nazarov–Sodin pin it down in $d=1$; this paper only shows existence of small/large regimes.
- Optimality of the $R^{2d}$ point count for higher-dim Fourier uniqueness sets — strongly suggested by Theorems 1.3/1.5 but not proven.
- Extends Radchenko–Viazovska [9], Cohn–Kumar–Miller–Radchenko–Viazovska [3], Ramos–Sousa [10], Ramos–Stoller [11], Viazovska [18], Kulikov–Nazarov–Sodin [6]; relates to Radchenko–Stoller [8] (number-field constructions of non-uniqueness sets).
- Whether the pseudohomogeneity hypothesis on $\sigma_A, \sigma_B$ can be relaxed.

## Key terms
Fourier uniqueness pair, Fourier uniqueness set, Radchenko–Viazovska interpolation, Kulikov–Nazarov–Sodin, Cohn–Elkies, universal optimality, E8 lattice, Leech lattice, Gabor transform, wave packet, parametrix, Schwartz function, twisted Poisson summation, pseudohomogeneous diffeomorphism, stationary phase, sphere packing, magic function, modular forms, uncertainty principle, density threshold
