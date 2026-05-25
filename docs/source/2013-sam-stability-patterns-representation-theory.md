---
type: source
kind: paper
title: STABILITY PATTERNS IN REPRESENTATION THEORY
authors: Steven V. Sam, Andrew Snowden
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1302.5859
source_local: ../raw/2013-sam-stability-patterns-representation-theory.pdf
topic: general-knowledge
cites:
---

# STABILITY PATTERNS IN REPRESENTATION THEORY

**Authors:** Steven V. Sam, Andrew Snowden  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1302.5859

## One-line
Develops a unified theory of stable representation categories for five families of groups (GL, O, Sp, S, GA) by establishing equivalences with diagram categories, twisted commutative algebras (tcas), and generalized Schur functors.

## Key claim
For each of $GL(\infty)$, $O(\infty)$, $Sp(\infty)$, $S(\infty)$, $GA(\infty)$, the stable representation category $\mathrm{Rep}(G)$ is simultaneously equivalent to (i) finite-length representations of a diagram category (Brauer / walled Brauer / partition / downwards-upwards variants), (ii) finite-length modules over a specific tca ($\mathrm{Sym}(\mathrm{Sym}^2 V)$, $\mathrm{Sym}(\wedge^2 V)$, $\mathrm{Sym}(V\otimes V')$, $\mathrm{Sym}(V)$), and (iii) a category of generalized Schur functors satisfying an explicit universal property.

## Method
Identify stable categories with algebraic representations of $G(\infty)=\bigcup_d G(d)$; use Schur–Weyl duality to convert diagram-algebra actions on $V^{\otimes n}$ into tca module structures (the contraction map $\alpha_n:n\to n+2$ becomes the multiplication $\mathrm{Sym}^2 V\otimes V_n\to V_{n+2}$); discard co-contraction (which has no $d=\infty$ invariant) to get well-defined infinite-rank objects. Specialization functors $\Gamma_d:\mathrm{Rep}(G)\to\mathrm{Rep}(G(d))$ are recovered from universal properties; their derived behavior is imported from [SSW] and [SS1].

## Result
Concrete consequences: (1) orthogonal–symplectic duality $\mathrm{Rep}(O)\simeq\mathrm{Rep}(Sp)$ as asymmetric tensor equivalence via partition transpose interchanging $\mathrm{Sym}(\mathrm{Sym}^2 V)\leftrightarrow\mathrm{Sym}(\wedge^2 V)$; (2) all five categories are Koszul, with $\mathrm{Rep}(GL)$ and $\mathrm{Rep}_{\mathrm{pol}}(GA)\simeq\mathrm{Rep}(S)$ Koszul self-dual via a Fourier-transform auto-equivalence on $D^b$; (3) tensor multiplicity in $\mathrm{Rep}(O)$ is $[V_\nu:V_\lambda\otimes V_\mu]=\sum_{\alpha,\beta,\gamma}c^\lambda_{\alpha,\beta}c^\mu_{\beta,\gamma}c^\nu_{\alpha,\gamma}$ (sums of products of Littlewood–Richardson coefficients), recovering Koike's formulas. Branching, comultiplication, restriction, and polarization rules all reduce to graph-labelled LR sums.

## Why it matters here
General background; no direct arena tie — the wiki currently has no problem in the symmetric-function / classical-group representation theory family. Could inform any future problem involving stable Kronecker coefficients, Schur–Weyl duality, or LR-coefficient calculations (e.g. extremal combinatorics framed via $S_n$-representations).

## Open questions / connections
- Is there a uniform theory unifying all five families (the paper observes a generic-stabilizer pattern $V^*\supset\mathrm{open}$ orbit $\Rightarrow$ $\mathrm{Mod}_K\simeq\mathrm{Rep}(H)$ but cannot prove it independently)?
- Positive-characteristic analogues fail because $\mathrm{Rep}_{\mathrm{pol}}(GL(\infty))$ ceases to be semisimple.
- Are $D^b(\mathrm{Rep}_{\mathrm{pol}}(GA))$ and $D^b(\mathrm{Rep}(S))$ equivalent as triangulated tensor categories despite isomorphic Grothendieck rings? Conjectured no.
- Categorification of the Rees-algebra degeneration $K(\mathrm{Rep}(S))\rightsquigarrow K(\mathrm{Rep}_{\mathrm{pol}}(GA))$ (stable Kronecker $\to$ LR coefficients).

## Key terms
stable representation theory, twisted commutative algebra, Schur–Weyl duality, Brauer algebra, walled Brauer category, partition algebra, Littlewood–Richardson coefficients, stable Kronecker coefficients, Koszul duality, orthogonal-symplectic duality, Schur functor, FI-modules, Deligne interpolation category, $GL(\infty)$, classical groups, specialization functor
