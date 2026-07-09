---
type: source
kind: paper
title: Equivariant log concavity and representation stability
authors: Jacob P. Matherne, Dane Miyata, N. Proudfoot, Eric Ramos
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2104.00715
source_local: ../raw/2021-matherne-equivariant-log-concavity-representation.pdf
topic: general-knowledge
cites:
---

# Equivariant log concavity and representation stability

**Authors:** Jacob P. Matherne, Dane Miyata, N. Proudfoot, Eric Ramos  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2104.00715

## One-line
Lifts log-concavity of matroid characteristic polynomials from integers to graded $S_n$-representations, conjecturing that Orlik–Solomon, Cordovil, and Orlik–Terao algebras of symmetric matroids/arrangements are "strongly equivariantly log concave," and verifies this in low degree for the $\mathfrak{sl}_n$ Coxeter arrangement using representation stability + computer check.

## Key claim
Define $V$ strongly equivariantly log concave if $V^i \otimes V^l \hookrightarrow V^j \otimes V^k$ as $\Gamma$-subrepresentations whenever $i \le j \le k \le l$ with $j+k=i+l$. Conjecturally this holds for $A_n, B_n, C_n, D_n, M_n$ (Orlik–Solomon, reduced OS, Cordovil, $H^*(\mathrm{Conf}(n,SU_2)/SU_2)$, and intersection cohomology of the $\mathfrak{sl}_n$ hypertoric variety). Proven in degrees $\le 14$ for $A_n,B_n,C_n,D_n$ and $\le 8$ for $M_n$; the isomorphism $D_n \cong M_n$ (Conjecture 1.4 of [MPY17]) is established for all $i \le 7$ (and verified for $n \le 22$).

## Method
Representation stability (Church–Ellenberg–Farb FI-modules): each sequence $\{V_n\}$ stabilizes at some $d$ — its irreducible decomposition in the "padded" basis $V_{\lambda[n]}$ becomes constant for $n \ge d$. They show $A^i, C^i$ stabilize at $3i{+}1, 3i$ (Hersh–Reiner) and derive $B^i$ at $3i{+}1$, $D^i, M^i$ at $3i$. A new ingredient: a sharp sub-additive stability bound for tensor products (Theorem 3.3), proved via Briand–Orellana–Rosas's Kronecker-coefficient stability [BOR11]. This reduces each conjecture to a finite SageMath check.

## Result
For $n \le 21$, $D_n^i \cong M_n^i$ as $S_n$-reps for $i \le 7$; hence the isomorphism holds for all $n$ in those degrees. Strong equivariant log concavity (subrep inclusions of all $V^i \otimes V^l$ into $V^j \otimes V^k$) verified by computer for $A_n,B_n,C_n,D_n$ up to degree 14 and $M_n$ up to degree 8. Also proved abstractly (Prop. 2.3, via virtual-rep ring identity): strong equivariant log concavity is closed under tensor product — the right equivariant analog of log-concavity-with-no-internal-zeros.

## Why it matters here
General background; no direct arena tie. Touches matroid log-concavity (Adiprasito–Huh–Katz, Ardila–Denham–Huh) which underlies Lorentzian-polynomial / Hodge-theoretic optimization frameworks occasionally invoked in extremal combinatorics — relevant only if an arena problem reduces to a matroid characteristic polynomial or broken-circuit $h$-vector. Useful as a pointer to the AHK and ADH log-concavity theorems and to representation-stability tooling for symmetric-group-indexed sequences.

## Open questions / connections
- Full Conjecture 1.6 (strong equivariant log concavity in all degrees for $A_n,B_n,C_n,D_n,M_n$) and Conjectures 2.5, 2.10, 2.13 for arbitrary matroids/oriented matroids/arrangements with group action remain open.
- Conjecture 1.4 ($D_n \cong M_n$): smallest unverified case is $D_{23}^8 \cong M_{23}^8$.
- Stronger FI-module version (Remark 3.16): is $A^i \otimes A^l$ an FI-quotient of $A^j \otimes A^k$? Authors doubt it for $i>0$.
- Extends the Hersh–Reiner stability ranges and is the first direct use of FI-modules to prove isomorphism of two infinite rep sequences.

## Key terms
equivariant log concavity, Orlik–Solomon algebra, Cordovil algebra, Orlik–Terao algebra, hypertoric variety, representation stability, FI-modules, Kronecker coefficients, braid matroid, configuration space cohomology, Adiprasito–Huh–Katz, broken-circuit complex, characteristic polynomial, $\mathfrak{sl}_n$ Coxeter arrangement, Church–Ellenberg–Farb
