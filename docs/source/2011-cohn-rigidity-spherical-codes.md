---
type: source
kind: paper
title: Rigidity of Spherical Codes
authors: Henry Cohn, Y. Jiao, Abhinav Kumar, S. Torquato
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1102.5060
source_local: ../raw/2011-cohn-rigidity-spherical-codes.pdf
topic: general-knowledge
cites:
---

# Rigidity of Spherical Codes

**Authors:** Henry Cohn, Y. Jiao, Abhinav Kumar, S. Torquato  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1102.5060

## One-line
Systematic study of when spherical cap packings (spherical codes) are jammed vs deformable, applied to kissing configurations through 32 dimensions, with new kissing-number records in dimensions 25–31.

## Key claim
The Coxeter–Todd $K_{12}$ kissing configuration is *not* jammed (analogous to fcc in $\mathbb{R}^3$), yet many others — Barnes–Wall $\Lambda_{16}$, $D_n$ for $n\geq 4$, $E_6,E_7,E_8$, and all best known kissing configs in dimensions 4–12 — are infinitesimally jammed; exploiting non-jamming of the previous records yields new kissing-number lower bounds in $\mathbb{R}^{25}$–$\mathbb{R}^{31}$ (e.g., $197040, 198480, 199912, 204188, 207930, 219008, 230872$).

## Method
Infinitesimal jamming reduced to linear programming: perturb $x_i \to x_i + \varepsilon y_i$ with $\langle x_i,y_i\rangle = 0$ and $\langle x_i,y_j\rangle + \langle x_j,y_i\rangle \leq 0$ on contact pairs; a code is infinitesimally jammed iff every such deformation is an infinitesimal rotation (skew-symmetric $\Phi$ with $y_i = \Phi x_i$). Connelly–Roth–Whiteley: infinitesimal jamming $\Rightarrow$ jamming (via tensegrity frameworks with bars to origin, struts between neighbors). Rigorous proofs use QSopt_ex exact-rational LP; conceptual proofs use a key lemma — if $C \subseteq D$ share minimal distance and $C$ is infinitesimally jammed in its span, then inner products inside $C$ are first-order frozen in any deformation of $D$ (so e.g. the regular-hexagon $A_2$ embeds rigidly into root systems).

## Result
- $A_n$ root system is *not* jammed for $n\geq 3$ (explicit cuboctahedron-style unjamming via matched-pair perturbations).
- $D_n$ ($n\geq 4$), $E_6, E_7, E_8$, $\Lambda_{16}$ (Barnes–Wall): infinitesimally jammed.
- $K_{12}$ (Coxeter–Todd): not jammed despite being locally jammed.
- New kissing lower bounds in $\mathbb{R}^{24+d}$ via Theorem 7.5: pick subset $S \subset $ Leech minimal vectors with pairwise $\langle x,y\rangle \leq 1$ ($|S|=480$ achieved by computer; LP bound $\leq 850$), partition $S_1,\ldots,S_N$ by random Leech-automorphism translates (probabilistic argument: $|S_i| \geq |S|(1 - \sum_{j<i}|S_j|/196560)$), then lift to $(x\sqrt{2/3}, y\sqrt{4/3})$ using equilateral-triangle/antipodal partitions of cross-section kissing configs.
- Records improve all of dims 25–31 over the 1982 laminated-lattice values.

## Why it matters here
Directly informs **kissing-number** problems and **sphere-packing local-optimality** reasoning: jamming is the structural test for whether a configuration can be deformed to a better one (cuboctahedron $\to$ icosahedron is the canonical case). Concepts to wire into the wiki: *infinitesimal jamming as LP*, *tensegrity-framework lift*, *Lemma 3.1 (jammed sub-code freezes inner products)*, *cross-section lifting for kissing-number records*, and *Eisenstein-structure partition into equilateral triangles*.

## Open questions / connections
- Is there a spanning spherical code that is jammed but not infinitesimally jammed? (Authors suspect yes, found none.)
- Efficient algorithm to test jamming on the sphere? (Quantifier elimination works in principle but is impractical; Euclidean LP test doesn't transfer due to curvature normalization.)
- Is the Barnes–Wall $\Lambda_{16}$ kissing config (4320 points) optimal in $\mathbb{R}^{16}$? Not unique either way.
- Conjecture: in all sufficiently high dimensions, optimal kissing configurations exist with *no contacts at all* (unjammed in strongest sense); known only in $\mathbb{R}^3$.
- Are there exponentially large jammed kissing configurations in high $d$? Even super-quadratic? $D_n$ gives only $2n(n-1)$.
- Optimizing $|R|, |S|$ in Leech-based constructions = max-clique in highly symmetric graphs (NP-hard general, open in practice).
- Improvement room: Shtrom upper / new lower bound ratio grows $\sim 1.4^d$ in $24+d$ dims.

## Key terms
spherical code, kissing number, infinitesimal jamming, tensegrity framework, rigidity, Leech lattice, Barnes–Wall lattice, Coxeter–Todd K12, root system jamming, Cohn, Connelly, Roth–Whiteley, LP rigidity test, Eisenstein lattice, Nordstrom–Robinson code, cross-section lifting
