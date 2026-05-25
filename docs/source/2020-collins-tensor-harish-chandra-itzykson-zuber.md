---
type: source
kind: paper
title: "The tensor Harish-Chandra–Itzykson–Zuber integral I: Weingarten calculus and a generalization of monotone Hurwitz numbers"
authors: B. Collins, R. Gurau, L. Lionni
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2010.13661
source_local: ../raw/2020-collins-tensor-harish-chandra-itzykson-zuber.pdf
topic: general-knowledge
cites:
---

# The tensor Harish-Chandra–Itzykson–Zuber integral I: Weingarten calculus and a generalization of monotone Hurwitz numbers

**Authors:** B. Collins, R. Gurau, L. Lionni  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2010.13661

## One-line
Generalizes the HCIZ matrix integral to tensor products of $D$ unitary groups $U(N)^{\otimes D}$, expands its log on trace-invariants of the external tensors, and identifies the coefficients as a new class of "higher" monotone double Hurwitz numbers counting branched covers of a bouquet of $D$ 2-spheres.

## Key claim
For $I_{D,N}(t,A,B) = \mathbb{E}_U[\exp(t\,\mathrm{Tr}(AUBU^*))]$ with $U = U^{(1)} \otimes \cdots \otimes U^{(D)}$, the cumulants admit a topological $1/N$ expansion whose coefficients $\hat p_\mathcal{C}[\sigma,\tau;l]$ (Thm. 4.1) enumerate transitive factorizations of $D$-tuples of permutations into monotone transpositions; in $D=1$ these reduce to monotone double Hurwitz numbers, and for general $D$ they count isomorphism classes of branched covers of a bouquet of $D$ 2-spheres joined at one common non-branch node.

## Method
Weingarten calculus on $U(N)^{\otimes D}$: each Haar integral over $U^{(c)}$ produces a Weingarten function $W^{(N)}(\sigma_c \tau_c^{-1})$, and the product yields a sum over $D$-tuples $(\sigma,\tau) \in S_n^D$ of trace-invariants weighted by $\prod_c W^{(N)}$. The cumulants are extracted via Möbius inversion on the partition lattice, giving "cumulant Weingarten functions" $W^{(N)}_\mathcal{C}[\sigma,\tau]$ expressed as monotone-transposition counts $\hat p_\mathcal{C}$. A geometric reinterpretation recasts these counts as sums over "foldings" $S(\sigma,\tau;\{\pi_c\}_c)$ — nodal surfaces of fixed arithmetic genus whose colored nodes carry single monotone Hurwitz number weights (Prop. 5.14).

## Result
- Exact combinatorial formula (Prop. 3.6) for $\hat p_\mathcal{C}[\sigma,\tau;l]$ as alternating sum over weakly-monotone transposition factorizations.
- Leading-order $1/N$ asymptotics of the cumulant Weingarten functions (Thm. 4.1): leading exponent is $-nD + 2G(\sigma,\tau) - \ell(\sigma,\tau)$ where $G(\sigma,\tau)$ is the arithmetic genus of an associated nodal topological constellation.
- Higher-order monotone double Hurwitz numbers $H_l(\{\alpha_c,\beta_c\}_c)$ count branched covers of the $D$-bouquet (Cor. 5.4) with Riemann-Hurwitz-type relation $l = \sum_c[\#(\alpha_c)+\#(\beta_c)] + 2H - 2 - 2n(D-1)$.
- Expression of higher-genus monotone double Hurwitz numbers in terms of monotone single Hurwitz numbers (Prop. 5.14).

## Why it matters here
General background; no direct arena tie. Tensor integrals over $U(N)^{\otimes D}$ and Weingarten calculus are abstract algebraic-combinatorics machinery for tensor random matrix theory and 2D quantum gravity — far from the optimization-flavored arena problems (sphere packing, autocorrelation, kissing, discrete geometry). The closest tangential link is to combinatorial enumeration on surfaces (constellations, Hurwitz numbers), which could conceivably inform extremal-graph or partition-counting problems but is not direct.

## Open questions / connections
- Extension to orthogonal/symplectic groups (the authors flag this as future work).
- BGW-tensor variant $\log \mathbb{E}_U[\exp(t\,\mathrm{Re}\,\mathrm{Tr}(B U A^*))]$ — deferred to a sequel.
- Whether the colored-node combinatorics admits a higher-dimensional (rather than nodal-surface) geometric interpretation, hinted at via the link to colored triangulations / random tensor models.
- Connection to Deligne-Mumford compactification for $D=2$ (nodal surfaces where two surfaces meet at a node).
- Relation to topological recursion for weighted/monotone Hurwitz numbers (Alexandrov-Chapuy-Eynard-Harnad).

## Key terms
Harish-Chandra-Itzykson-Zuber integral, HCIZ, Weingarten calculus, monotone Hurwitz numbers, double Hurwitz numbers, constellations, tensor integrals, branched coverings, nodal surfaces, Möbius inversion, Bousquet-Mélou-Schaeffer, Brézin-Gross-Witten, random tensors, $1/N$ expansion, non-crossing partitions
