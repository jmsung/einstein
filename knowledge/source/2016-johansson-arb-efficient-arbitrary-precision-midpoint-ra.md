---
type: source
kind: paper
title: "Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic"
authors: Fredrik Johansson
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1611.02831
source_local: ../raw/2016-johansson-arb-efficient-arbitrary-precision-midpoint-ra.pdf
topic: general-knowledge
cites:
---

# Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic

**Authors:** Fredrik Johansson  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1611.02831

## One-line
Describes Arb, a C library implementing arbitrary-precision ball (midpoint-radius interval) arithmetic that rigorously tracks error bounds while running competitively with non-interval floating-point libraries like MPFR/MPC.

## Key claim
Midpoint-radius intervals $[m \pm r]$ — with $m$ stored to full precision and $r$ as a low-precision $\sim 30$-bit floating-point bound — achieve $(1+\varepsilon)$ overhead vs floating-point at high precision (a factor-2 saving over endpoint intervals $[a,b]$), while supplying provable enclosures for elementary, gamma/beta, zeta, Bessel, Airy, hypergeometric, modular, elliptic and other special functions of real and complex arguments.

## Method
Two-tier number representation: an `arf_t` arbitrary-precision dyadic midpoint (mantissa $a \cdot 2^b$, $1/2 \le |a| < 1$, dynamic mantissa allocation) paired with a 2-word `mag_t` unsigned floating-point radius. Complex numbers, polynomials, matrices, and power series are built atop real balls. Polynomial multiplication uses a stability-preserving block algorithm (van der Hoeven 2008): scale $x \to 2^c x$, split into blocks of bounded height ($\le 3p + 512$ bits), multiply each block pair exactly in $\mathbb{Z}[x]$ via FLINT (Schönhage–Strassen FFT for large products), then accumulate — preserving schoolbook-quality error bounds at FFT speed.

## Result
Arb computes $p(10^{10})$ (111391 digits) in 0.3 s vs Mathematica 9.0's 1 minute, and the record $p(10^{20})$ (11 billion digits) in 110 hours; isolates 6710 Airy roots on $[-1000, 0]$ in 0.4 s and refines to 1000 digits in 16 s; computes $\{f^{(i)}(0.5)\}_{i=0}^{1000}$ for $\zeta$ to 1000 digits in 1.9 s. Cross-testing against MPFR 3.1.3 uncovered bugs in MPFR's square root, Bessel, and $\zeta$ routines.

## Why it matters here
Triple-verify (axiom A1) and the float-precision-critical problems (P5, P6, P11, P14, P17) currently rely on mpmath at 50–80 dps as check #2; Arb is a faster, rigorous alternative that returns provable enclosures rather than just high-precision floats, eliminating an entire class of numerical bugs from the verification pipeline. Particularly relevant to equioscillation diagnostics, Cohn–Elkies LP polish, and any score whose validity hinges on whether a small quantity is provably above zero.

## Open questions / connections
- Could Arb-based enclosures replace mpmath polish stages and tighten the "exact reimplementation" leg of triple-verify with proof-grade certainty?
- Degenerate near-exact rounding cases (e.g. $\tanh(10000) \approx 1$ to 28852 bits) still need special handling — does this affect any arena problem where a near-integer score is the boundary?
- Builds on van der Hoeven's ball arithmetic [8] and FLINT's exact polynomial layer [18]; complements MPFI [5] (endpoint intervals) and iRRAM [10] (exact-real).

## Key terms
ball arithmetic, midpoint-radius interval, arbitrary precision, rigorous enclosure, MPFR, MPFI, FLINT, dyadic floating-point, FFT polynomial multiplication, Schönhage–Strassen, automatic differentiation, special functions, Riemann zeta, Bessel, partition function, Keiper-Li coefficients, Johansson, error bounds, triple-verify
