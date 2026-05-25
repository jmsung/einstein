---
type: source
kind: paper
title: "Quantum Lovász local lemma: Shearer’s bound is tight"
authors: Kun He, Qian Li, Xiaoming Sun, Jiapeng Zhang
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1804.07055
source_local: ../raw/2018-he-quantum-lov-local-lemma.pdf
topic: general-knowledge
cites:
---

# Quantum Lovász local lemma: Shearer's bound is tight

**Authors:** Kun He, Qian Li, Xiaoming Sun, Jiapeng Zhang  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1804.07055

## One-line
Proves that Shearer's bound — the tight criterion for the classical Lovász Local Lemma — is also tight for the quantum LLL, fully characterizing frustration-freeness of local Hamiltonians via the independent set polynomial.

## Key claim
For any interaction bipartite graph $G$ and rational relative-dimension vector $p$: if $p$ lies in Shearer's bound $I(G)$, then almost all local Hamiltonians with these parameters (on sufficiently large qudits) are frustration-free with satisfying-subspace relative dimension $\to q(G,p)$ (the multivariate independence polynomial); if $p \notin I(G)$, almost all are unsatisfiable. This affirms the Sattath–Morampudi–Laumann–Moessner (PNAS 2015) conjecture.

## Method
Induction on the number of left vertices in the interaction bipartite graph, combined with Laumann et al.'s **geometrization theorem** ("existence ⇒ almost-all" for random Haar-measure subspaces). Construct explicit satisfying / unsatisfying instances on carefully chosen qudit dimensions $d_j \leq 4^N$ (resp. $\leq 8N \cdot 4^N$), then geometrization lifts to almost-all Hamiltonians. For the commuting LLL (CLLL) portion: Bravyi–Vyalyi structure lemma decomposes commuting projectors into product subspaces, allowing solitary qudits to be reduced to classical variables.

## Result
**Theorem 1.3:** Shearer's bound is the exact tight region for QLLL on any interaction graph; the relative dimension of the smallest satisfying subspace equals $q(G,p)$. Implies Gilyén–Sattath's (FOCS 2017) algorithm converges up to the tight region (under uniform inverse-poly spectral gap), and the lattice gas partition function's first negative fugacity zero exactly characterizes quantum satisfiability for almost all Hamiltonians with large qudits. **CLLL is different:** Shearer's bound is *not* tight for CLLL in general — gapless if base graph is a tree, gapful if base graph has an induced cycle of length ≥ 4 (3-clique case open).

## Why it matters here
General background; no direct arena tie. Independent-set polynomials, LLL-style dependency-graph reasoning, and lattice-gas / hardcore-model partition functions occasionally surface in extremal combinatorics and discrete-geometry problems, but the QLLL machinery itself is quantum-complexity territory and unlikely to inform the current 23-problem set directly.

## Open questions / connections
- How small can $N_0$ (qudit dimension threshold) be — can it be polynomial in $p$? Important for computational/algorithmic aspects of QLLL.
- When inside Shearer's bound but with high relative dimensions, must the satisfying state be entangled? The "three-range" picture (classical / entangled-satisfiable / unsatisfiable) is unresolved.
- CLLL tightness for base graphs containing only 3-cliques remains open — mirrors the same unresolved case for variable-version classical LLL (He et al. FOCS 2017).

## Key terms
Lovász local lemma, quantum LLL, Shearer's bound, independent set polynomial, frustration-free Hamiltonian, lattice gas partition function, hardcore model, commuting local Hamiltonian, geometrization theorem, Bravyi–Vyalyi structure lemma, quantum satisfiability, k-QSAT
