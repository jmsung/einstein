---
type: source
kind: paper
title: "Nemo/Hecke: Computer Algebra and Number Theory Packages for the Julia Programming Language"
authors: C. Fieker, W. Hart, Tommy Hofmann, Fredrik Johansson
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1705.06134
source_local: ../raw/2017-fieker-nemo-hecke-computer-algebra.pdf
topic: general-knowledge
cites:
---

# Nemo/Hecke: Computer Algebra and Number Theory Packages for the Julia Programming Language

**Authors:** C. Fieker, W. Hart, Tommy Hofmann, Fredrik Johansson  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1705.06134

## One-line
Introduces Nemo (computer algebra) and Hecke (algebraic number theory) — Julia packages combining JIT-compiled generic algorithms with thin wrappers around Flint, Arb, Antic, and Singular.

## Key claim
Julia's parametric type system + JIT enable generic computer-algebra code that runs within ~2× of hand-tuned C (Flint without asm) on the Fateman/Pearce sparse polynomial benchmarks, and dramatically beats SageMath/Magma on several mixed generic/specialised workloads (e.g., a generic resultant in $(\mathrm{GF}(17^{11})[y]/(y^3+3xy+1))[z]$: $0.2$ s in Nemo vs $82$ s Magma vs $179907$ s Sage).

## Method
Two-layer design: (i) wrap optimised C libraries (Flint integers/polynomials, Arb midpoint-radius ball arithmetic for $\mathbb{R}, \mathbb{C}$, Antic number fields, Singular) via Julia's zero-overhead C FFI, exposing them through a SageMath/Magma-style **parent object** model (singleton objects carry context like a modulus $n$, avoiding JIT recompilation per modulus); (ii) implement generic recursive constructions (univariate/multivariate polys, power series, residue rings, fraction fields, matrices) in pure Julia with abstract-type hierarchies (`Field <: Ring`) for multiple dispatch. New algorithmic contributions: a fraction-free **Danilevsky** characteristic-polynomial algorithm (similarity reductions to Frobenius form with provably-removable scaling factors); a **multimodular spinning** minimal-polynomial algorithm that leaks Krylov-basis-vector indices from one good prime $p$ to certify termination via cheap matrix-vector products $m(M)v_i'$; and a fast ideal-arithmetic scheme in $\mathcal{O}_K$ via **$S$-normal presentations** $(a,\alpha)$ where Lemma 6.3 ($\beta = vt\alpha + uas$ with $1 = \gcd(as,t)$) merges presentations for compatible $S$ at the cost of two gcds rather than a linear-algebra step.

## Result
Ideal multiplication in $\mathbb{Q}[X]/(X^n+2)$ on random products of 100 ideals: Hecke runs in $0.08$ s at $n=128$ vs $5.40$ s Pari vs $7572$ s Magma. Generic $80\times 80$ determinant over a cubic number field: $2.4$ s Nemo vs $5.3$ s Magma vs $21.9$ s Pari/GP vs $5893$ s Sage. Fateman $n=30$: $362$ s Nemo generic Julia vs $168$ s Flint-no-asm vs $439$ s Magma vs $1814$ s Sage. Hecke also delivers verified embeddings, torsion-unit testing via Dobrowolski's bound $|\sigma_k(\alpha)| > 1 + \tfrac{1}{6}(\log d/d^2)$, and certified Dedekind-zeta residues via Belabas–Friedman under GRH — all using Arb ball arithmetic for automatic error bounds.

## Why it matters here
General background; no direct arena tie. Potential indirect utility: Hecke/Nemo could serve as a verified-arithmetic backend for problems requiring exact algebraic number computations (e.g., closed-form configurations in discrete-geometry problems, exact resultants in P15/P16 equioscillation diagnostics) and Arb ball arithmetic is the same paradigm as mpmath used in triple-verify — relevant when mpmath is too slow and certified intervals suffice.

## Open questions / connections
- Could Arb's ball arithmetic replace mpmath for ulp-polish stages where guaranteed-correct intervals would catch the verifier-drift incidents (P9/P14/P17) without paying full-precision cost?
- The multimodular spinning algorithm's $O(n^4)$ worst-case bound is loose in practice — when does the leaked-Krylov-basis certificate fail, and what is the expected number of good primes for matrices arising in LP/SDP duality witnesses?
- Singular.jl integration (deferred to a future article) — relevant for any Gröbner-basis approach to extremal combinatorics or flag-algebra SDPs.

## Key terms
Julia, Nemo, Hecke, Flint, Arb, Antic, Singular, parent objects, multiple dispatch, ball arithmetic, midpoint-radius intervals, Danilevsky algorithm, Frobenius form, fraction-free elimination, Krylov subspace, spinning algorithm, minimal polynomial, multimodular, Chinese remaindering, $S$-normal presentation, Dedekind domain, ring of integers, ideal arithmetic, torsion units, Dobrowolski bound, Dedekind zeta function, Belabas-Friedman, analytic class number formula, sparse polynomial multiplication, Johnson algorithm, Monagan-Pearce, subresultant GCD, resultant, number field, JIT compilation, computer algebra system
