---
type: source
kind: paper
title: Lorentzian polynomials.
authors: Petter Brand'en, June Huh
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.03719
source_local: ../raw/2019-branden-lorentzian-polynomials.pdf
topic: general-knowledge
cites:
---

# Lorentzian polynomials.

**Authors:** Petter Brand'en, June Huh  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.03719

## One-line
Introduces *Lorentzian polynomials* — a class of homogeneous polynomials whose Hessian has exactly one positive eigenvalue on the positive orthant — unifying stable polynomials, volume polynomials, and matroid basis generating functions under one Hodge–Riemann-style framework.

## Key claim
A nonzero polynomial $f \in \mathcal{L}^d_n$ has Hessian with signature $(+,-,\ldots,-)$ at every point of the positive orthant; equivalently, the classes of Lorentzian, strongly log-concave (Gurvits), and completely log-concave (Anari–Oveis Gharan–Vinzant) homogeneous polynomials *coincide*. Supports of Lorentzian polynomials are *exactly* M-convex sets (matroids in the multi-affine case).

## Method
Inductive definition via partial derivatives bottoming out at quadratics of Lorentzian signature $(+,-,\ldots,-)$. A Nuij-type homotopy $f \mapsto (1+\theta w_i \partial_j)f$ shows the strictly-Lorentzian interior is dense in the M-convex-support set $\mathcal{L}^d_n$. Tropicalization over Puiseux series links Lorentzian polynomials bijectively to M-convex/valuated-matroid functions (discrete convex analysis of Murota).

## Result
Three headline applications: (1) The homogenized multivariate Tutte polynomial $Z_{q,M}$ of any matroid is Lorentzian for $0 < q \le 1$, proving the *strongest* Mason conjecture (1972): $I_k(M)^2 / \binom{n}{k}^2 \ge \bigl(I_{k-1}(M)/\binom{n}{k-1}\bigr)\bigl(I_{k+1}(M)/\binom{n}{k+1}\bigr)$. (2) The multivariate characteristic polynomial of any M-matrix is Lorentzian (strengthening Holtz's ultra-log-concavity). (3) The uniform measure on independent sets of a matroid is 2-Rayleigh: $\Pr(i,j \in F) \le 2 \Pr(i)\Pr(j)$, partial progress on Kahn–Grimmett–Winkler.

## Why it matters here
Direct toolkit for autocorrelation/extremal-combinatorics and discrete-geometry problems: Lorentzian = "Hodge–Riemann holds at every point" is a *checkable* certificate of log-concavity for generating polynomials, and the linear-operator-preservation theorems give a closed algebra for manipulating bounds. Volume polynomials of convex bodies being Lorentzian (Section 4.1) ties mixed-volume / sphere-packing bounds into the same framework as matroid bases.

## Open questions / connections
- Question 4.9: is every Lorentzian polynomial a volume polynomial of some convex body / projective variety? (Open.)
- Conjecture 2.29: $P\mathcal{L}^d_n$ is homeomorphic to a closed Euclidean ball.
- Sharpening 2-Rayleigh to 1-Rayleigh for graphic matroids would settle Kahn–Grimmett–Winkler.
- Parallel/independent line: Anari–Liu–Oveis Gharan–Vinzant (completely log-concave polynomials) — same class, different proof route; led to FPRAS for counting matroid bases and resolved Mihail–Vazirani matroid-expansion conjecture.
- Extends Adiprasito–Huh–Katz Hodge theory for combinatorial geometries to a derivative-based (rather than intersection-theoretic) formulation.

## Key terms
Lorentzian polynomials, Hodge–Riemann relations, M-convex sets, matroid basis generating polynomial, strongly log-concave, completely log-concave, ultra log-concave, Mason's conjecture, stable polynomials, multivariate Tutte polynomial, M-matrix, mixed volume, Brändén, Huh, negative dependence, strongly Rayleigh, valuated matroid, tropicalization, Murota discrete convex analysis
