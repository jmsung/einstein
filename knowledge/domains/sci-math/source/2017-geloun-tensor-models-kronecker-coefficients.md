---
type: source
kind: paper
title: Tensor models, Kronecker coefficients and permutation centralizer algebras
authors: J. B. Geloun, S. Ramgoolam
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1708.03524
source_local: ../raw/2017-geloun-tensor-models-kronecker-coefficients.pdf
topic: general-knowledge
cites:
---

# Tensor models, Kronecker coefficients and permutation centralizer algebras

**Authors:** J. B. Geloun, S. Ramgoolam  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1708.03524

## One-line
Organizes the counting and correlators of rank-$d$ tensor model observables via a family of semi-simple "permutation centralizer algebras" $K(n,d)$ whose Wedderburn-Artin matrix decomposition is governed by Kronecker coefficients of $S_n$.

## Key claim
The algebra $K(n)$ controlling rank-3 tensor invariants has $\dim K(n) = \sum_{R_1,R_2,S \vdash n} C(R_1,R_2,S)^2$, where $C(\cdot)$ is the Kronecker coefficient; its Wedderburn-Artin blocks are labeled by triples of Young diagrams with non-vanishing Kronecker multiplicity, and the matrix basis $Q^{R_1,R_2,R_3}_{\tau_1,\tau_2}$ built from $S_n$ Clebsch-Gordan coefficients diagonalizes Gaussian two-point functions.

## Method
Tensor invariants of degree $n$ in $d$ indices are parametrized by $d$-tuples of $S_n$ permutations modulo diagonal left/right $S_n$ action (a double coset). Fourier transform on $S_n$ via characters and Clebsch-Gordan coefficients converts the double-coset algebra to a direct sum of matrix algebras (Wedderburn-Artin). Color-exchange $S_d$ symmetry is then layered on by decomposing $K(n)$ into $S_d$ irreps using projector techniques.

## Result
At rank $d$: $\dim K(n,d) = \sum_{R_1,\dots,R_{d-1},S \vdash n} C_d(R_1,\dots,R_{d-1},S)^2$, expressible as products of Kronecker coefficients. Gaussian one-point functions evaluate as $\langle O_{\sigma_1,\dots,\sigma_d}\rangle = \sum_\gamma N^{c(\gamma\sigma_1)+\cdots+c(\gamma\sigma_d)}$. The color-symmetrized sub-algebra under $S_d$ also has dimension a sum of squares of representation-theoretic quantities, proving integrality of the previously-conjectured sequences $S_p^{(d)}(n)$. Correlators have a permutation-TFT$_2$ interpretation as covers of singular 2-complexes, generalizing the matrix-model/Belyi-map link.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: representation-theoretic decomposition of symmetric-group double cosets via Clebsch-Gordan / Kronecker coefficients is a tool that could inform extremal problems with $S_n$-symmetric structure (combinatorics, autocorrelation), but none of the 23 Einstein Arena problems currently invoke tensor-model machinery.

## Open questions / connections
- Computational complexity gap between "central correlators" in matrix vs. tensor models — Kronecker coefficient positivity is in GapP (Ikenmeyer-Mulmuley-Walter); does this asymmetry have a physical interpretation?
- Young-diagram statistical models and field theories: the matrix basis suggests new statistical ensembles indexed by Young diagrams.
- Holographic duals of tensor models: counting observables constrains the spectrum of any putative dual.

## Key terms
permutation centralizer algebra, Kronecker coefficient, Clebsch-Gordan coefficients, symmetric group representation theory, Wedderburn-Artin decomposition, tensor model, double coset, Young diagram, semi-simple algebra, color-exchange symmetry, character orthogonality, topological field theory
