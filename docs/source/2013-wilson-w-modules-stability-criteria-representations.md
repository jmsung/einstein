---
type: source
kind: paper
title: FI_W-modules and stability criteria for representations of the classical Weyl groups
authors: Jenny Wilson
year: 2013
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1309.3817
source_local: ../raw/2013-wilson-w-modules-stability-criteria-representations.pdf
topic: general-knowledge
cites:
---

# FI_W-modules and stability criteria for representations of the classical Weyl groups

**Authors:** Jenny Wilson  ·  **Year:** 2013  ·  **Source:** https://arxiv.org/abs/1309.3817

## One-line
Extends the Church–Ellenberg–Farb FI-module framework from symmetric groups $S_n$ to the hyperoctahedral groups $B_n$ and even-signed permutation groups $D_n$, giving a categorical machine that turns "finite generation" into "uniform representation stability" for sequences of classical Weyl-group representations.

## Key claim
**Theorem 4.22:** An FI$_W$-module $V$ over a characteristic-zero field is uniformly representation stable iff it is finitely generated, with stabilization once $n \geq \max(g,r) + d$ where $d$ = weight, $g$ = generation degree, $r$ = relation degree (plus $n \geq g+1$ in type $D$ when $d=0$). **Theorem 4.21:** FI$_W$-modules are Noetherian — sub-FI$_W$-modules of f.g. FI$_W$-modules are f.g.

## Method
Define categories FI$_A$, FI$_{BC}$, FI$_D$ whose objects are $\mathbf{n} = \{\pm 1,\ldots,\pm n\}$ and whose morphisms are sign-respecting injections (with parity constraints in type $D$); an FI$_W$-module is a functor from FI$_W$ to $k$-modules. Restriction and induction between the three families are built via Kan extensions. Branching rules + a weight filtration $\tau_{\geq d}V$ reduce finite generation to control over induced representations $\mathrm{Ind}_{W_m \times W_{n-m}}^{W_n}(U_m \boxtimes k)$.

## Result
Proves type-$B/C$ and type-$D$ analogues of **Murnaghan's stability theorem (Thm 5.3, Cor 5.4):** for double partitions $\lambda,\mu$, the Kronecker-like coefficients $g^\nu_{\lambda,\mu}$ in $V(\lambda)_n \otimes V(\mu)_n = \sum_\nu g^\nu_{\lambda,\mu} V(\nu)_n$ are eventually $n$-independent and finitely supported. Applied to $r$-diagonal coinvariant algebras $C^{(r)}(n)$ for $S_n, B_n, D_n$ (Thms 6.1–6.4, Cor 6.5): each multigraded piece $C^{(r)}_J(n)$ has weight $\leq |J|$, is uniformly multiplicity stable, has characters given by a character polynomial of degree $\leq |J|$ in signed cycle counts $X_r, Y_r$, and has dimensions eventually polynomial in $n$ (degree $\leq |J|$) — including over positive characteristic. Cohomology rings $H^*(G_{W_n}/B_{W_n};\mathbb{C})$ of generalized flag varieties inherit these properties.

## Why it matters here
General background; no direct arena tie. The paper is pure representation-stability machinery — useful only as a reference framework if any Einstein problem ever requires sequence-of-representations bookkeeping (e.g., a symmetry-orbit decomposition that grows with $n$). No optimization, bound, or constructive technique that maps onto the 23 packing / autocorrelation / extremal problems.

## Open questions / connections
- Computing character polynomials $F_J$ for $C^{(r)}_J$ at $|J| > 3$ is open (Problem 6.6); only the $|J| \leq 3$ type-$B/C$ cases are tabulated.
- Relation to Snowden's twisted commutative algebras and Sam–Snowden's category-theoretic analysis of FI-modules left unresolved.
- Sequel [Wil14] promises full character-polynomial theory + polynomial dimension growth over arbitrary fields.

## Key terms
FI-module, FI_W-module, representation stability, hyperoctahedral group, signed permutation group, Weyl group, Murnaghan stability, Kronecker coefficients, character polynomial, diagonal coinvariant algebra, flag variety cohomology, Kan extension, Noetherian category, Church-Ellenberg-Farb, branching rules
