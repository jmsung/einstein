---
type: source
kind: paper
title: The Structure of Critical Product Sets
authors: Matt DeVos
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1301.0096
source_local: ../raw/2013-devos-structure-critical-product-sets.pdf
topic: general-knowledge
cites:
---

# The Structure of Critical Product Sets

**Authors:** Matt DeVos  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1301.0096

## One-line
Classifies all "critical" pairs $(A,B)$ of finite subsets in an arbitrary (possibly nonabelian) group $G$ satisfying $|AB| < |A|+|B|$, extending Vosper (prime cyclic) and Kemperman (abelian) to the general case.

## Key claim
Every nontrivial maximal critical subset trio in any group is built by a recursive sequence of "beats" and "cyclic/dihedral chords" relative to a descending chain of subgroups; as a corollary, Kneser's theorem generalizes: $\exists H \le G$ with $|AB| \ge |A|+|B|-|H|$ such that every $y \in AB$ admits $x \in G$ with $y(x^{-1}Hx) \subseteq AB$ (conjugate stability replaces left/right stability).

## Method
The proof departs from product sets into an incidence-geometry framework: associate a Cayley "chorus" / trio to $(A,B,C=(AB)^{-1})$ and classify the resulting $G$-equivariant incidence geometries (songs: beats, chords, videos, octahedral choruses). Core technique is a variant of Hamidoune's **isoperimetric method** combined with standard intersection-union ("uncrossing") and induction arguments. The structure theorem on incidence geometries is then translated back to subset trios via stabilizer / clone-partition analysis.

## Result
For any finite nonempty $A,B \subseteq G$: deficiency $\delta(A,B) = |A|+|B|-|AB|$ is bounded by $|H|$ for some $H \le G$, and the critical structure decomposes via pure/impure **beats** (subgroup-cosets), **cyclic chords** ($G/H$ cyclic, $|G/H| \ge 4$, geometric progressions), or **dihedral chords** ($G/H$ dihedral, $|G/H| \ge 8$, dihedral progressions). For $|A^2| < 2|A|$, $A$ lies in a coset $xH=Hx$ with $H/K$ cyclic or dihedral controlling the doubling (Corollary 1.10). For $|AB| < 2\min\{|A|,|B|\}$, analogous trichotomy holds (Corollary 14.4).

## Why it matters here
General background; no direct arena tie. Closest relevance is to combinatorial-extremal problems with additive/group structure (sieve theory, Sidon-set-adjacent problems) — the framework formalizes when small-doubling forces coset/progression structure, which is a recurring motif in extremal combinatorics.

## Open questions / connections
- Extends Hamidoune's isoperimetric program ([19], [23]–[26]) and Serra–Zémor [46] from $\delta=1$ to all critical pairs in nonabelian $G$.
- Companion paper (Boothby–DeVos–Montejano [2]) gives a simpler proof in the abelian case (recovering Kemperman); the incidence-geometry detour is the cost of nonabelian generality.
- Leaves open: quantitative Freiman-type bounds for $|A^2| < c|A|$ with $c \ge 2$ in nonabelian groups (Breuillard–Green–Tao [3] handles approximate-group regime; the gap to exact structure remains).

## Key terms
critical pair, product set, Cauchy-Davenport, Kneser theorem, Vosper theorem, Kemperman structure theorem, deficiency, isoperimetric method, Hamidoune, geometric progression, dihedral progression, beat, cyclic chord, dihedral chord, incidence geometry, Cayley chorus, conjugate stability, small doubling, nonabelian additive combinatorics, Freiman
