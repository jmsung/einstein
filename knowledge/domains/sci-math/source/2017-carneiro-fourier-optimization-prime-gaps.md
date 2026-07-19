---
type: source
kind: paper
title: Fourier optimization and prime gaps
authors: E. Carneiro, M. Milinovich, K. Soundararajan
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.04122
source_local: ../raw/2017-carneiro-fourier-optimization-prime-gaps.pdf
topic: general-knowledge
cites:
---

# Fourier optimization and prime gaps

**Authors:** E. Carneiro, M. Milinovich, K. Soundararajan  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.04122

## One-line
Defines two Fourier extremal problems on bandlimited / sign-restricted functions, establishes existence/uniqueness of extremizers and explicit numerical bounds on the sharp constants, and uses them via the Guinand–Weil explicit formula to sharpen the conditional (RH) upper bound on prime gaps.

## Key claim
Assuming RH, $p_{n+1}-p_n \le \tfrac{22}{25}\sqrt{p_n}\log p_n$ for all $p_n>3$ (Theorem 5), improving Dudek's constant $c=1$ in Cramér's $\sqrt{p_n}\log p_n$ bound; the limit of the method is $1/2$.

## Method
Three ingredients: (i) the Guinand–Weil explicit formula linking primes to nontrivial zeros of $\zeta$, (ii) the Brun–Titchmarsh inequality (Montgomery–Vaughan explicit version, and Iwaniec's $B\le 36/11$) to control prime contributions near the edges of the test interval, and (iii) two Fourier extremal problems $C(A), C^+(A)$ — sup of $(|F(0)| - A\!\int_{|t|>1}|\widehat F|)/\|F\|_1$ — whose optimization governs the constant in the prime-gap bound. Existence of extremizers proved via $L^2$ weak-compactness + Mazur's lemma; uniqueness in the bandlimited case via a Krein factorization $R=|S|^2$. Explicit lower bounds come from dilations of $H(x)=\cos(2\pi x)/(1-16x^2)$ and the Fejér kernel; upper bounds from a dual formulation using Gorbachev's piecewise-linear mollified test function.

## Result
- $1.08185 \le C(\infty) \le 1.09769$ (Gorbachev); $C(\infty)\le C^+(\infty)<1.2$.
- $C^+(36/11) > 25/21 = 1.1904\ldots$ via the explicit example $F(x)=-4.8x^2 e^{-3.3x^2}+1.5x^2 e^{-7.4x^2}+520x^{24}e^{-9.7x^2}+1.3e^{-2.8x^2}+0.18e^{-2x^2}$ giving $1.1943$.
- General Theorem 3: $\limsup (p_{n+1}-p_n)/(\sqrt{p_n}\log p_n) \le 1/C^+(B) < 21/25$ on RH.
- Explicit Theorem 5 uses $F(x)=H(x/0.9)$, $\lambda=0.9$, $B\le 4$, giving constant $22/25$ for $x\ge 4\cdot 10^{18}$ (smaller $x$ covered by Oliveira e Silva et al.).

## Why it matters here
Directly relevant to the Cohn–Elkies / sphere-packing family of Fourier-uncertainty extremal problems used in this wiki (P-family bandlimited problems); Proposition 10 also gives an existence result for the Cohn–Elkies sphere-packing extremizer in arbitrary $d$. The $C(A), C^+(A)$ problems are sign-constrained variants of the "one-delta" / Cohn–Elkies template and the duality machinery (mollify a dual test function to push delta masses outside $[-1,1]$) is a transferable technique for any Arena problem cast as a Fourier extremal with finite-$A$ slack.

## Open questions / connections
- Explicit value of $C(\infty), C^+(\infty)$ — neither uniqueness nor a closed form is known; gap between $1.08185$ and $1.09769$ unclosed.
- Multidimensional analogue $C_{d,K}(\infty)$ for cube $Q$ tensorizes ($=C(\infty)^d$); for the ball $B$ uniqueness of radial extremizers holds via de Branges spaces, but sharp constants are open.
- Connects to: Beurling–Selberg majorants, Vaaler interpolation, pair-correlation conjecture (which would give $\limsup = 0$), Gorbachev's $(C,L)$-Nikol'skii constants, and the "one-delta problem for $K$" (open except cube/ball).

## Key terms
Cohn-Elkies, sphere packing, Fourier uncertainty, bandlimited functions, Beurling-Selberg, prime gaps, Riemann hypothesis, Guinand-Weil explicit formula, Brun-Titchmarsh inequality, Fejér kernel, Cramér conjecture, Viazovska, magic function, extremal problem, duality, mollification, Gorbachev, autocorrelation, one-delta problem
