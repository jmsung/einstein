---
type: source
kind: paper
title: Spectra of Uniform Hypergraphs
authors: Joshua N. Cooper, Aaron Dutle
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1106.4856
source_local: ../raw/2011-cooper-spectra-uniform-hypergraphs.pdf
topic: general-knowledge
cites:
---

# Spectra of Uniform Hypergraphs

**Authors:** Joshua N. Cooper, Aaron Dutle  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1106.4856

## One-line
Builds a spectral theory of $k$-uniform hypergraphs by defining eigenvalues of the adjacency hypermatrix via the multipolynomial resultant, then ports core spectral-graph-theory results (Perron-Frobenius, chromatic bound, coefficient–subgraph correspondence) to that setting.

## Key claim
For a $k$-uniform hypergraph $H$ with adjacency hypermatrix $A_H$ (entries $1/(k-1)!$ on edges), the eigenvalues defined by $A_H x^{k-1} = \lambda x^{[k-1]}$ satisfy $d \le \lambda_{\max} \le \Delta$ (average ≤ largest ≤ maximum degree), $\chi(H) \le \lambda_{\max}(H) + 1$, and the codegree-$(k+1)$ coefficient of $\phi_H(\lambda)$ equals $-C_k (k-1)^{n-k} \cdot (\text{\# simplices in } H)$ with explicit $C_2{=}2,\ C_3{=}21,\ C_4{=}588,\ C_5{=}28230$.

## Method
Eigenvalues are roots of the characteristic polynomial $\phi_A(\lambda) = \mathrm{Res}(\lambda I - A)$ where $\mathrm{Res}$ is Gelfand–Kapranov–Zelevinsky's multipolynomial resultant; combined with Qi/Lim's variational formulation $F_H(x) = \sum_{e\in H} k\, x^e$ maximized on $S_{\ge 0} = \{x \ge 0 : \sum x_i^k = 1\}$. Coefficient identification uses the Morozov–Shakirov $\log\det = \mathrm{tr}\log$ analogue with Schur polynomials in generalized traces; spectra of $k$-cylinders, Cartesian products, ultracubes $Q^d_k = E_k \,\square\, \cdots \,\square\, E_k$, and complete $k$-graphs follow from direct manipulation of the eigenvalue equations.

## Result
Established: disjoint-union spectrum (with multiplicity $(k-1)^{|H_2|}$), Perron-type largest-eigenvalue theorem for connected $H$, degree-sandwich $d \le \lambda_{\max} \le \Delta$, Wilf-style chromatic bound $\chi \le \lambda_{\max} + 1$, subgraph monotonicity $\lambda_{\max}(G) \le \lambda_{\max}(H)$, $k$-th-root-of-unity invariance of spectra of $k$-cylinders (one direction only — converse fails for $k>2$), explicit $\phi_{E_k}(\lambda) = \lambda^{k(k-1)^{k-1} - k^{k-1}} (\lambda^k - 1)^{k^{k-2}}$, $\mathrm{spec}(G\,\square\,H) \supseteq \mathrm{spec}(G)+\mathrm{spec}(H)$ (strict — "sporadic" eigenvalues like $\sqrt[k]{d} \in \mathrm{spec}(Q^d_k)$ exist), and a closed-form description of complete-$k$-cylinder spectra via $(k-1)$-st roots of unity.

## Why it matters here
General background; no direct arena tie — none of the 23 problems are currently framed as hypergraph spectral problems. Possible touchpoints: extremal graph theory (P-class — chromatic / clique bounds via $\lambda_{\max}$) and uncertainty/autocorrelation problems where a $k$-uniform incidence structure with spectral bound could replace pairwise-only adjacency arguments. The resultant-as-eigenvalue framework also generalizes the LP-duality machinery already in the wiki to higher-order tensor constraints.

## Open questions / connections
- Spectrum of the complete $k$-graph for $k > 3$, and multiplicities for $k = 3$ — open in the paper; combinatorial-design problems may need it.
- Whether "second-largest-modulus eigenvalue" controls hypergraph expansion/quasirandomness (Kohayakawa–Rödl–Skokan, Conlon–Hàn–Person–Schacht) — extends Cheeger/Alon-Boppana to $k$-graphs.
- Efficient computation: resultant via $\binom{n(k-1)}{n-1} \times \binom{n(k-1)}{n-1}$ Macaulay matrix is $O(16^n/\sqrt n)$ for $k=3$ — stalls at $n \approx 9$. Connects to compute-router question: is the resultant amenable to GPU float64 batched determinant?
- Sporadic eigenvalues of $Q^d_k$ — recursive construction gives $\sqrt[k]{d}$ but no full description; relates to ultracube structure.

## Key terms
adjacency hypermatrix, symmetric hyperdeterminant, multipolynomial resultant, characteristic polynomial, Perron-Frobenius for tensors, Qi eigenvalue, Lim eigenvalue, chromatic number bound, $k$-uniform hypergraph, $k$-cylinder, ultracube, Cartesian product, complete $k$-graph, Schur polynomial, Morozov-Shakirov, $k$-th root of unity invariance
