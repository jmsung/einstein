---
type: source
kind: paper
title: The discrete yet ubiquitous theorems of Carathéodory, Helly, Sperner, Tucker, and Tverberg
authors: J. D. Loera, X. Goaoc, Frédéric Meunier, Nabil H. Mustafa
year: 2017
author: agent
drafted: 2026-05-24
ingested_at: 2026-05-24
source_type: arxiv
source_url: https://arxiv.org/abs/1706.05975
source_local: ../raw/2017-loera-discrete-yet-ubiquitous-theorems.pdf
topic: general-knowledge
cites:
---

# The discrete yet ubiquitous theorems of Carathéodory, Helly, Sperner, Tucker, and Tverberg

**Authors:** J. D. Loera, X. Goaoc, Frédéric Meunier, Nabil H. Mustafa  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1706.05975

## One-line
A unified survey of five foundational discrete-mathematics theorems (Sperner, Tucker, Carathéodory, Helly, Tverberg), their interconnections, and their applications across optimization, game theory, graph theory, fair division, and computational geometry.

## Key claim
These five theorems form a tightly-coupled toolkit: Sperner/Tucker are the combinatorial analogues of Brouwer/Borsuk–Ulam, while Carathéodory/Helly/Tverberg anchor combinatorial convexity — together they yield short proofs of results including Nash equilibrium existence, LP duality, the ham sandwich theorem, the centerpoint theorem ($\mu(H) \ge \tfrac{1}{d+1}\mu(\mathbb{R}^d)$ for any halfspace $H \ni c_\mu$), the first selection lemma ($\ge \tfrac{2}{9}\binom{n}{3}$ triangles cover some point in the plane), and Kneser-chromatic-number lower bounds.

## Method
Survey/exposition. Two foundational lemmas (Sperner: any Sperner-labeled triangulation of $\Delta^d$ has an odd number of fully-labeled facets; octahedral Tucker: any antipodally-symmetric labeling $\lambda:\{+,-,0\}^n\setminus\{0\}\to\{\pm 1,\dots,\pm m\}$ with no complementary pair $x \preceq y$, $\lambda(x)+\lambda(y)=0$ forces $n\le m$) are derived via parity/path-following arguments. Three convexity theorems are stated and re-proven: Carathéodory ($d+1$ points suffice for convex-hull membership in $\mathbb{R}^d$), Helly ($d+1$-wise intersection suffices), Tverberg ($(r-1)(d+1)+1$ points admit an $r$-partition with intersecting convex hulls). New proofs are given for Meshulam's lemma and the ham sandwich theorem.

## Result
Catalogue of consequences: colorful Carathéodory; centerpoint theorem; Kirchberger's separation theorem; first/second selection lemmas; topological/colorful Helly; Tverberg-type partitions with quantitative bounds; PPAD-completeness of Sperner-style fixed-point search; subexponential simplex variants via Helly-number arguments; weak $\varepsilon$-net constructions; polynomial partitioning. The survey emphasizes algorithmic aspects (path-following Sperner, complexity of Tverberg-point computation, ham-sandwich algorithms) and open problems including tight constants in selection lemmas, the colorful simplicial depth conjecture, and exact Helly numbers for structured set families.

## Why it matters here
Directly informs **discrete geometry / packing / extremal-graph** problems in the arena: Helly/Carathéodory give bounds-from-finite-intersections useful for LP-bound style arguments (P15/P16, kissing/sphere-packing duality); centerpoint and selection lemmas relate to depth/covering arguments; Tverberg partitions underlie combinatorial separation lemmas that can serve as analytical cross-checks. General background — no single arena problem reduces to a named theorem here, but the toolkit is foundational for the wiki's combinatorial-convexity concept layer.

## Open questions / connections
- Tight quantitative Tverberg / colorful Carathéodory bounds (e.g., colorful simplicial depth conjecture, Sierksma's conjecture on partition counts).
- Optimal constants in first/second selection lemmas — what is the best covering fraction for $n$ points in $\mathbb{R}^d$?
- Helly numbers for non-convex / structured families (sublattice convexity, $S$-convexity, integer Carathéodory property) — connects to integer programming bounds relevant to lattice-packing problems.

## Key terms
Sperner lemma, Tucker lemma, Carathéodory theorem, Helly theorem, Tverberg theorem, Borsuk-Ulam, Brouwer fixed point, centerpoint theorem, colorful Carathéodory, first selection lemma, ham sandwich theorem, Kneser chromatic number, PPAD, combinatorial convexity, polynomial partitioning, weak epsilon-nets
