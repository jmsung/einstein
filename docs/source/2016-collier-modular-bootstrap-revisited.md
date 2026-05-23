---
type: source
kind: paper
title: Modular bootstrap revisited
authors: S. Collier, Ying-Hsuan Lin, Xi Yin
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1608.06241
source_local: ../raw/2016-collier-modular-bootstrap-revisited.pdf
topic: general-knowledge
cites:
---

# Modular bootstrap revisited

**Authors:** S. Collier, Ying-Hsuan Lin, Xi Yin  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1608.06241

## One-line
Uses semi-definite programming on the torus modular crossing equation to derive spin-resolved upper bounds on operator-dimension gaps in 2D unitary CFTs with $c > 1$.

## Key claim
Modular invariance + unitarity alone force a nontrivial scalar gap $\Delta_{\rm mod}^{s=0}(c) < 2$ for $c < 8$ (saturated by $E_8$ WZW at level 1, $\Delta = 2$ kink) and finite for $c < 25$; the all-spin gap satisfies $\Delta_{\rm mod}(c) = c/6 + 1/3$ exactly on $c \in [1,4]$, with asymptotic slope $b_{\rm mod} \in [1/12, 1/9)$.

## Method
Decompose $Z(\tau,\bar\tau)$ into non-degenerate Virasoro characters with positive degeneracies, then act on the modular crossing equation $E_{h,\bar h} = \chi_h\bar\chi_{\bar h} - \chi_h(-1/\tau)\bar\chi_{\bar h}(-1/\bar\tau)$ with linear functionals $\alpha = \sum_{m+n \text{ odd} \leq N} \alpha_{m,n}\partial_z^m\partial_{\bar z}^n|_{z=\bar z=0}$ (with $\tau = ie^z$). SDPB solves for functionals proving exclusion of a hypothetical spectrum; extrapolation $N \to \infty$ at fixed $c$ recovers the optimal bound. Refines Hellerman/Friedan-Keller by using full $(\tau,\bar\tau)$ derivatives rather than just imaginary-axis $\tau$.

## Result
At $c=4$, $\Delta_{\rm mod} = 1$ exactly (kink, $\partial \Delta/\partial c$ jumps from $1/6$ to $1/8$). For $c>4$, $\Delta_{\rm mod}(c) < 1/2 + c/8$. Twist gap bound $t_{\rm mod} = (c-1)/12$ reproduced numerically. Extremal spectra at maximal gap for $c=1,2,14/5,4$ are SU(2)$_1$, SU(3)$_1$, $G_{2,1}$, SO(8)$_1$ WZW; at $c=8$, $\Delta^{s=0}_{\rm gap}=2$ is realized by $\Gamma_8$ Narain lattice $(j(\tau)\bar j(\bar\tau))^{1/3}$ with 248 spin-1 currents.

## Why it matters here
General background; no direct arena tie. The semidefinite-programming-on-positivity-with-derivative-functional template is structurally identical to the Cohn-Elkies LP bound for sphere packing — both extract optimal exclusion functionals from positivity of an unknown distribution, and the "extremal functional zeroes determine the spectrum" idea parallels active-constraint extraction in packing/kissing optimizers.

## Open questions / connections
- What is the exact asymptotic slope $b_{\rm mod}$? Resolution would bound the lightest massive particle mass in AdS$_3$ gravity.
- Why does the optimal functional shift from $\sin+\sinh$ form at small $c$ to $te^{-at^2}$ form at large $c$? Suggests integral-transform basis beats derivative-at-self-dual-point at large $c$.
- Connection to multi-correlator / higher-genus bootstrap (Hogervorst-Rychkov radial coordinates; Castedo Echeverri-von Harling-Serone effective bootstrap).
- Existence of unitary compact CFTs with nonzero twist gap and no extra conserved currents remains open.

## Key terms
modular bootstrap, semidefinite programming, SDPB, Virasoro characters, modular crossing equation, twist gap, extremal spectrum, optimal linear functional, Hellerman-Friedan-Keller bound, WZW models, $E_8$ lattice, Narain lattice, conformal field theory
