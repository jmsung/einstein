---
type: source
kind: paper
title: Extremal results for random discrete structures
authors: M. Schacht
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1603.00894
source_local: ../raw/2016-schacht-extremal-results-random-discrete.pdf
topic: general-knowledge
cites:
---

# Extremal results for random discrete structures

**Authors:** M. Schacht  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1603.00894

## One-line
Determines the threshold probabilities at which classical extremal theorems (Szemerédi, Furstenberg–Katznelson, Turán–Erdős–Stone) transfer from dense sets to sparse random substructures.

## Key claim
For every $k\geq 3$ and $\varepsilon>0$, the threshold for "every dense subset of $[n]_p$ contains a $k$-AP" is $p=\Theta(n^{-1/(k-1)})$; analogously $n^{-1/(|F|-1)}$ for Furstenberg–Katznelson configurations $F\subseteq\mathbb{N}^\ell$, $n^{-1/m(A)}$ for density-regular matrices $A$, $n^{-1/2}$ for Schur's equation, and $n^{-1/m(F)}$ for Turán-type problems in random graphs/hypergraphs $G^{(\ell)}(n,p)$ — verifying the Kohayakawa–Łuczak–Rödl conjecture.

## Method
A unified transference principle (Theorem 3.3): given a sequence of $k$-uniform hypergraphs $H_n$ encoding the forbidden configurations, if $H$ is $\alpha$-dense (supersaturation: dense subsets contain $\Omega(|E_n|)$ edges) and $(K,p)$-bounded (degree-squared moments controlled by $\mu_i(H,q)\leq Kq^{2i}|E_n|^2/|V_n|$), then the deterministic extremal property transfers a.a.s. to the random subset $V_{n,q}$ for $q\geq Cp_n$. The proof goes by induction on $k$ via a strengthened lemma (Lemma 3.4) using Chernoff plus a Rödl–Ruciński exponential upper-tail bound after deleting an $\eta q|V_n|$-sized exceptional set.

## Result
Each of Theorems 2.2–2.7 establishes a sharp 0/1 threshold: below $cp_n$ the property fails a.a.s. (standard second-moment / Markov arguments using the heuristic that expected configurations match expected vertices/edges), above $Cp_n$ it holds a.a.s. via Theorem 3.3. The parameter $m(A)$ for matrices and $m(F)$ for hypergraphs (defined via max sub-density) captures the correct scaling exponent in both cases, with denominator $\geq 1$ guaranteed for irredundant partition-regular $A$.

## Why it matters here
General background for random-structure thresholds and supersaturation arguments; light tie to Einstein Arena — the $m(F)$ density parameter and 0/1 threshold technology are the relevant tools for any arena problem framed as "find a sparse extremal substructure inside a random/large host" (extremal-graph and combinatorics families).

## Open questions / connections
- Turán density $\pi(F)$ for non-bipartite hypergraphs (e.g., $\pi(K_4^{(3)})$) remains open and is the bottleneck for sharp hypergraph thresholds.
- Extends Kohayakawa–Łuczak–Rödl (small cliques), Frankl–Rödl ($K_3$), Gerke–Schickinger–Steger ($K_5$); parallel to Conlon–Gowers' independent transference.
- Whether $(K,p)$-boundedness can be verified for other extremal contexts (e.g., Sidon-set thresholds, sum-free density) — the framework is generic but requires moment control case by case.

## Key terms
Szemerédi's theorem, arithmetic progressions, Furstenberg–Katznelson, Turán's theorem, Erdős–Stone, chromatic number, random graphs $G(n,p)$, Kohayakawa–Łuczak–Rödl conjecture, transference principle, density-regular matrices, Rado partition regular, Schur equation, Turán density, supersaturation, $(K,p)$-bounded hypergraphs, threshold probability
