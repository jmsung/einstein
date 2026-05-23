---
type: source
kind: paper
title: A note on Schwartz functions and modular forms
authors: Larry Rolen, Ian Wagner
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1903.05737
source_local: ../raw/2019-rolen-note-schwartz-functions-modular.pdf
topic: general-knowledge
cites:
---

# A note on Schwartz functions and modular forms

**Authors:** Larry Rolen, Ian Wagner  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1903.05737

## One-line
Generalizes Viazovska's magic-function construction to an infinite family of Cohn–Elkies Schwartz functions built from quasi-modular and modular forms, giving the best modular-forms sphere-packing upper bounds in every dimension $d \equiv 0 \pmod 8$.

## Key claim
For each $d \equiv 0 \pmod 8$, there exist explicit radial Schwartz functions $f_\pm : \mathbb{R}^d \to \mathbb{R}$ with $\widehat{f_\pm} = \pm f_\pm$, simple zeros at $r = \sqrt{2 n_\pm}$, and double zeros at $r = \sqrt{2m}$ for $m > n_\pm$, where $n_+ = d/16 + 1/2$ and $n_- = d/16 + 1$. After checking the required sign inequalities this yields $\Delta_d \le 2^{-0.4529\, d}$ as $d \to \infty$ for $d \equiv 0 \pmod 8$, recovering Viazovska's $E_8$ (d=8) and the Leech (d=24) functions exactly, and the Cohn–Gonçalves $A_+(12) = \sqrt{2}$ uncertainty-principle function as a side product.

## Method
"Plus" eigenfunction: contour-integrate a weakly holomorphic depth-2 quasi-modular form $\varphi$ of weight $-d/2 + 4$ on $SL_2(\mathbb{Z})$ (a polynomial in $E_2, E_4, E_6$ divided by $\Delta^n$) against $e^{\pi i |x|^2 z}$ along a Viazovska-style keyhole contour; the modular transformation under $S$ forces the Fourier $+1$ eigenvalue, and a $\sin^2(\pi r^2/2)$ factor produces the double zeros. "Minus" eigenfunction: same scheme using weight $-d/2 + 2$ weakly holomorphic forms on $\Gamma(2)$ in the algebra $C[U, V, W]$ plus a correction $f \cdot L(z)$, where $L$ is a regularized Eichler integral of $\lambda'/\lambda$ (the holomorphic part of a weight-0 harmonic Maass form, playing the role $E_2$ plays on the plus side). The minimal valuation $n$ is then a dimension-count problem: solve a homogeneous system in the space $E_2^2 M_{*} \oplus E_2 M_{*} \oplus M_{*}$ (plus side) or $(U^2 - V^2) M_{*} \oplus W M_{*} \oplus L M_{*}$ (minus side), giving the bounds $2n > d/8 - 1$ and $2n \ge d/8 + 1$.

## Result
Explicit functions in every dimension $d \equiv 0 \pmod 8$ giving Cohn–Elkies-style upper bounds: e.g. $\Delta_8 \le 0.2537$ (tight, $E_8$), $\Delta_{24} \le 0.0019$ (tight, Leech), $\Delta_{48} \le 2.310 \times 10^{-5}$, $\Delta_{72} \le 4.495 \times 10^{-10}$, $\Delta_{96} \le 7.666 \times 10^{-12}$. In $d = 48$ the plus-side bound matches the $P_{48n}$ lattice's lower bound exactly, but the minus-side minimal $n = 4$ does not match the plus-side $n_+$, so the sphere-packing problem is *not* resolved by this family for $d = 48$. The asymptotic rate is $2^{-0.4529 d}$ — worse than Kabatianskii–Levenshtein's $2^{-0.599 d}$, identifying a ceiling for this whole Viazovska-style modular-forms approach.

## Why it matters here
Direct background for any arena problem whose SOTA is a Cohn–Elkies LP-bound magic function (sphere packing, kissing, $+1$-uncertainty / Bourgain–Clozel–Kahane, energy minimization): explains *what space the magic function lives in*, the parameter $n$ that controls where double zeros start, and the dimension-count bottleneck that makes $d = 48$ and beyond resist resolution. Particularly relevant to any P-problem framed as "construct radial Schwartz $f$ with $\widehat{f} = \pm f$, prescribed zero pattern, sign conditions" — the paper gives a recipe and the algebraic structure of the candidate space.

## Open questions / connections
- Is there a *different* modular family (perhaps higher level, non-trivial multiplier, or vector-valued) that beats $2^{-0.4529 d}$ and approaches Kabatianskii–Levenshtein?
- Cohn's remark: in $d = 28$ this construction would give $A_+(28) \le 2$ for the BCK uncertainty problem, but Cohn–Gonçalves conjecture an optimal function with non-zero roots at radii $2j + o(1)$ for $j \ge 2$ — i.e. the modular-forms family is provably suboptimal at $d = 28$.
- Generalizes Viazovska (2017, $d=8$), CKMRV (2017, $d=24$), Cohn–Gonçalves (2017, $d=12$ uncertainty); leaves open whether the same scheme generalizes to energy-minimization / universal-optimality bounds beyond $E_8$ and Leech.
- The remark "$\hat{f}(\sqrt{2m})$ are all numerically non-zero for $0 \le m < n_\pm$" is checked case-by-case but not proven in general — a concrete unresolved sub-question.

## Key terms
Cohn–Elkies linear programming bound, magic function, sphere packing, Viazovska, $E_8$ lattice, Leech lattice, quasi-modular forms, Eisenstein series $E_2$, Schwartz function, Fourier $\pm 1$ eigenfunction, weakly holomorphic modular form, $\Gamma(2)$, Hauptmodul $\lambda$, theta functions, Eichler integral, harmonic Maass form, uncertainty principle $A_+(d)$, Bourgain–Clozel–Kahane, Kabatianskii–Levenshtein bound, $P_{48n}$ lattice
