---
type: source
kind: paper
title: The lean mathematical library
authors: The mathlib Community
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1910.09336
source_local: ../raw/2019-community-lean-mathematical-library.pdf
topic: general-knowledge
cites:
---

# The lean mathematical library

**Authors:** The mathlib Community  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1910.09336

## One-line
Describes mathlib, a community-driven, classically-oriented mathematical library for the Lean 3 proof assistant built on dependent type theory.

## Key claim
mathlib provides a unified, dependently-typed, classical-math library (140k LOC, 73 contributors, 4256 type-class instances over 386 classes as of Dec 2019) whose semi-bundled structure hierarchy and metaprogramming-based automation make it distinctive among proof-assistant libraries.

## Method
Architectural/design paper, not a math result: the authors describe Lean 3's CIC + universes + quotient types + two classical axioms (`classical.choice`, `propext`), and explain design tradeoffs — semi-bundled type classes (carrier exposed, operations bundled), bundled morphisms, use of quotient types in place of setoids, and tactic-based automation written in Lean's metaprogramming framework. They contrast against Metamath/Mizar (set theory), HOL Light/Isabelle (simple type theory), and Coq's Mathematical Components (canonical structures + SSReflect).

## Result
Catalogs the library contents by directory (data 42k LOC, topology 17k, algebra 10k, analysis 8k, category_theory 6k, measure_theory 6k, linear_algebra 4.5k, etc.). Notable formalizations: Gromov–Hausdorff space as a Polish space, very general manifolds over arbitrary non-discrete normed fields, Sylow's theorems, quadratic reciprocity, Hilbert's basis theorem, Hensel's lemma over $p$-adic integers, undecidability of the halting problem, a model of ZFC inside Lean's universe hierarchy, Fréchet derivative, and Bochner integral. Identifies three concrete limitations of type-class inference: required acyclicity, worst-case exponential search, and backward-only search.

## Why it matters here
General background; no direct arena tie. Relevant only as context if the agent ever needs formal verification of an optimization claim or a clean reference for the algebraic-hierarchy / dependent-types tradeoffs — none of the 23 Einstein Arena problems are formalization-bound.

## Open questions / connections
- Porting mathlib to Lean 4 (then in development) — scale of effort unknown at writing.
- Type-class inference scaling: forward+backward reasoning could fix the structure-hierarchy traversal blowup but is unimplemented.
- Cap-set formalization (Dahmen–Hölzl–Lewis, ref [18]) is the closest tie to Arena-style extremal combinatorics — formal proof of the Ellenberg–Gijswijt bound on $|A|$ for $A \subset \mathbb{F}_q^n$ with no 3-AP.

## Key terms
Lean, mathlib, dependent type theory, calculus of inductive constructions, type classes, structure hierarchy, bundled vs unbundled, quotient types, classical choice, metaprogramming, tactic, Mathematical Components, Isabelle, cap set, formalization
