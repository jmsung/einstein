---
type: source
kind: paper
title: Borsuk - Ulam Type spaces
authors: O. Musin, A. Volovikov
year: 2015
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1507.08872
source_local: ../raw/2015-musin-borsuk-ulam-type-spaces.pdf
topic: general-knowledge
cites:
---

# Borsuk - Ulam Type spaces

**Authors:** O. Musin, A. Volovikov  ·  **Year:** 2015  ·  **Source:** https://arxiv.org/abs/1507.08872

## One-line
Characterizes "Borsuk–Ulam Type" (BUT) spaces — free $\mathbb{Z}_2$-spaces $(X,A)$ where every $f:X\to\mathbb{R}^n$ has a point with $f(Ax)=f(x)$ — via Yang's cohomological index, and shows equivalence with Lusternik–Schnirelmann, Tucker, Ky Fan, and Kakutani-type combinatorial/covering statements.

## Key claim
$(X,A)$ is a BUT$_n$-space iff the topological Yang index $\text{t-ind}\,X \ge n$; for closed manifolds (and closed almost-pseudomanifolds) with free involution, $\text{t-ind}\,M = \dim M$ iff $\text{h-ind}_2\,M = \dim M$ (Corollaries 3.1, 3.2). Equivalently for a $d$-manifold $M$ with free involution: BUT$_d$ iff every equivariant $h:M\to S^d$ has $\deg_2 h = 1$ iff $M$ admits an antipodal transversal-to-zero map $h:M\to\mathbb{R}^d$ with $|h^{-1}(0)| = 4k+2$.

## Method
Cohomological/topological index theory: Yang's index $\text{h-ind}_2$ defined three equivalent ways (Smith sequence iteration $\delta^n(1)$; powers of Stiefel–Whitney class $w(X)$ of the line bundle $(X\times\mathbb{R})/T \to X/T$; pullback of $w \in H^1(\mathbb{RP}^\infty;\mathbb{Z}_2)$). Integer version $\text{h-ind}_\mathbb{Z}$ uses Richardson–Smith sequences and van Kampen obstruction classes $u_k(X)$. Property 8 (an equivariant map between spaces of equal finite index $k$ kills $H^k$) is the workhorse — chains discrete Tucker/Ky Fan/Pn statements to topological BUT via Sperner-style barycentric subdivision + compactness limit.

## Result
Theorem 2.1: BUT$_n$ ⇔ LS$_n$ ⇔ Tucker$_n$ ⇔ Tucker–Bacon$_n$ ⇔ Yang$_n$ for normal spaces with free involution. Theorem 2.2: for finite simplicial complexes, also equivalent to $\tilde T_n$ (antipodal labeling has complementary edge), $F_n$ (Ky Fan alternating-sign simplex), and $P_n$ (convex hull of labeled points covers origin). Theorem 2.3: Kakutani-type — set-valued $F:X\to 2^{\mathbb{R}^n}$ with closed graph, convex compact values, antipodal symmetry, must cover $0$ somewhere iff BUT$_n$. Section 4 extends to "bounded" BUT-spaces via the doubling/camomile construction $D(X,Z)$. Theorem 5.6: smooth manifold $(M,A)$ is BUT$_n$ iff $w_1^n(M/A)\ne 0$ iff $[M,A] = \sum [V^k][S^{n-k},A]$ in $\mathfrak{N}_n(\mathbb{Z}_2)$ (Conner–Floyd cobordism). Yields a classification: 2-dim BUT$_2$ manifolds are orientable $M_g^2$ with even genus and non-orientable $P_m^2$ with even $m$.

## Why it matters here
General background; no direct arena tie. Borsuk–Ulam machinery is the canonical topological lower-bound tool for discrete-geometry problems (Kneser-graph chromatic number, ham-sandwich, necklace splitting) but Einstein Arena's 23 problems are optimization-on-real-parameters, not topological lower bounds. Could become relevant if a problem needs a parity/obstruction argument (e.g., proving a configuration must exist via degree-mod-2, or ruling out an equivariant map between configuration spaces).

## Open questions / connections
- Authors' conjecture: in Theorem 5.7 the chain $M_1\subset\cdots\subset M_n=M$ of nested BUT-submanifolds can be chosen with all $M_i$ connected — would strengthen Theorem 5.6 statement 3 to "$|h^{-1}(0)|=2$".
- Extension to $G$-spaces for finite $G\ne\mathbb{Z}_2$ promised in companion paper (ref [15], Musin–Volovikov, Tucker type lemmas for G-spaces).
- Open: classify BUT$_n$-manifolds in dimensions $\ge 3$ (2-dim case fully classified here).
- Yang's example of finite $X$ with $\text{h-ind}_2 X < \text{h-ind}_\mathbb{Z} X = \text{t-ind}\,X$ shows the three indices genuinely differ — when does $\text{h-ind}_2 = \text{t-ind}$ fail outside manifolds/pseudomanifolds?

## Key terms
Borsuk–Ulam theorem, Tucker lemma, Ky Fan lemma, Yang cohomological index, Lusternik–Schnirelmann category, free Z2-action, equivariant map, Stiefel–Whitney class, Smith sequence, van Kampen obstruction, Conner–Floyd cobordism, pseudomanifold, antipodal labeling, complementary edge, Kakutani theorem, BUT-space
