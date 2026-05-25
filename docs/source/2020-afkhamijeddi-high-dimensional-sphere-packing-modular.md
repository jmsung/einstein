---
type: source
kind: paper
title: High-dimensional sphere packing and the modular bootstrap
authors: Nima Afkhami-Jeddi, Henry Cohn, Thomas Hartman, David de Laat, Amirhossein Tajdini
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2006.02560v2
source_local: ../raw/2020-afkhamijeddi-high-dimensional-sphere-packing-modular.pdf
topic: general-knowledge
cites: 
---

# High-dimensional sphere packing and the modular bootstrap

**Authors:** Nima Afkhami-Jeddi, Henry Cohn, Thomas Hartman, David de Laat, Amirhossein Tajdini  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2006.02560v2

## One-line
A large-scale numerical study of the $U(1)^c$ spinless modular bootstrap — equivalent to the Cohn–Elkies LP bound for sphere packing in $d=2c$ dimensions — extrapolated to $c \to \infty$, yielding a conjectured exponential improvement over Kabatyanskii–Levenshtein.

## Key claim
Numerical extrapolation gives an upper bound of $2^{-(\lambda+o(1))d}$ for the sphere packing density in $\mathbb{R}^d$ as $d \to \infty$ with $\lambda \approx 0.6044$ (vs Kabatyanskii–Levenshtein's $\kappa = 0.59905576\ldots$); equivalently spectral-gap bound $c/(\Lambda + o(1))$ with $\Lambda \approx 9.869$, speculatively conjectured to be exactly $\pi^2$.

## Method
Adapt the Afkhami-Jeddi–Hartman–Tajdini numerical bootstrap technique [12] to $U(1)^c$: truncate the functional space to derivative orders $\omega_1, \omega_3, \ldots, \omega_{4N-1}$ at $\tau=i$, then reformulate as a nonlinear optimization over the empirical root pattern (single roots at $0, \Delta_1$; double roots at $\Delta_2, \ldots, \Delta_N$) rather than LP/SDP, which would be limited to $N \lesssim 100$. Truncation $N$ must scale roughly linearly in $d$ for fixed accuracy. Implied-kissing-number constraints (Theorem 5.2, de Laat–de Oliveira Filho–Vallentin) are combined with Levenshtein spherical-code bounds to rule out LP-tightness.

## Result
(1) Conjecture 3.1: optimal LP density decay $\lambda \approx 0.6044$, an exponential improvement over KL. (2) Conjecture 3.2 (speculative): $\Lambda = \pi^2$ exactly. (3) Sharp LP bound numerically ruled out for all $d \le 250$ except $d \in \{1,2,8,24,180,181,192\}$ via implied-kissing-number contradictions. (4) Spectrum $\Delta_n/N$ has a piecewise structure with abrupt linear→nonlinear transition at $n \sim (2/\pi)N$; linear part matches generalized 1d free fermion. (5) Mysterious mod-8 periodicity in degeneracies (Cardy-like at multiples of 8) and scaling dimensions (free-fermion-like at $4 \pmod 8$).

## Why it matters here
Directly informs the Cohn–Elkies LP-bound program for sphere packing — gives the strongest numerical evidence to date that KL is not optimal, plus a concrete extrapolation methodology (root-pattern nonlinear optimization) that scales beyond the $N \sim 100$ LP/SDP ceiling. The implied-kissing-number elimination technique (Theorem 5.2 + Levenshtein) is a reusable tool for ruling out LP-tightness in any dimension; spectrum analysis (linear free-fermion regime + transition at $2/\pi$) provides structural targets for magic-function ansatze beyond $d=8, 24$.

## Open questions / connections
- Can $\Lambda = \pi^2$ be derived analytically? What hidden structure forces the transition at $n/N = 2/\pi$?
- Does the spinless bootstrap = Cohn–Elkies LP equivalence (Hartman–Mazáč–Rastelli 2019) lift fully, i.e. can any $-1$ Fourier eigenfunction always be realized as $h - \widehat{h}$ from a valid LP auxiliary?
- Why does sharp LP behavior cluster on $d \in \{1,2,8,24\}$ plus the anomalous $\{180,181,192\}$? Is there an interpolation-basis explanation (Cohn–Kumar–Miller–Radchenko–Viazovska universal optimality framework)?
- Does Barg–Jaffe's MRRW-is-optimal conjecture for binary codes survive in light of this evidence that KL is not LP-optimal?
- Mod-8 periodicity in degeneracies and scaling dimensions — no conceptual explanation yet.

## Key terms
sphere packing, linear programming bound, Cohn-Elkies, modular bootstrap, spinless bootstrap, U(1) current algebra, Kabatyanskii-Levenshtein, MRRW bound, Viazovska, Leech lattice, E8 lattice, implied kissing number, Levenshtein, spectral gap, Laguerre eigenfunctions, magic function, $-1$ Fourier eigenfunction, free fermion spectrum, interpolation basis, Delsarte, spherical codes, Cardy formula, semidefinite programming, sphere packing density asymptotic, $\pi^2$ conjecture
