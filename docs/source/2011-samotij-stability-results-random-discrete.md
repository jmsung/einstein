---
type: source
kind: paper
title: Stability results for random discrete structures
authors: Wojciech Samotij
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1111.6885
source_local: ../raw/2011-samotij-stability-results-random-discrete.pdf
topic: general-knowledge
cites:
---

# Stability results for random discrete structures

**Authors:** Wojciech Samotij  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1111.6885

## One-line
A transference theorem that lifts deterministic extremal *stability* results (Erdős–Simonovits–type) to sparse random discrete structures with exponentially small error probability.

## Key claim
For every graph $H$ with a vertex of degree $\geq 2$ and every $\delta>0$, there exist $C,\varepsilon>0$ such that if $p_n \geq C n^{-1/m_2(H)}$, then with probability $1 - \exp(-\Omega(n^2 p_n))$, every $H$-free subgraph of $G(n,p_n)$ with $\geq (1 - 1/(\chi(H)-1) - \varepsilon)\binom{n}{2}p_n$ edges can be made $(\chi(H)-1)$-partite by deleting $\leq \delta n^2 p_n$ edges. Removes the "strictly 2-balanced" restriction of Conlon–Gowers and upgrades their $n^{-\omega(1)}$ tail to $\exp(-\Omega(n^2 p_n))$.

## Method
Extends Schacht's transference machinery by introducing $(\alpha,\mathcal{B})$-*stability* of hypergraph sequences (every dense substructure either has many forbidden configurations or is close to a member of a "structured" family $\mathcal{B}$) alongside $(K,\mathbf{p})$-boundedness of degree-square moments. Induction on the uniformity $k$ with multi-round exposure $U_q = U_{q_1}\cup\cdots\cup U_{q_R}$, plus the new "multiple exposure trick" — a measure-preserving bijection between $\mathcal{P}(U)$ and $\mathcal{P}(U)^R$ that preserves the "far from any $B\in\mathcal{B}$" property in a typical decomposition (Claim 1). Pairs the Erdős–Simonovits stability theorem with the (hyper)graph removal lemma to verify stability for concrete applications.

## Result
General Theorem 3.4 transfers any $(\alpha,\mathcal{B})$-stable, $(K,\mathbf{p})$-bounded hypergraph sequence with $|\mathcal{B}_n|=\exp(o(p_n|V(H_n)|))$ to the random setting at threshold $q \geq Cp_n$, with failure probability $\exp(-\Omega(q|V(H_n)|))$. Applications: (Thm 1.5) Kohayakawa–Łuczak–Rödl conjecture confirmed for all $H$ (not just strictly 2-balanced); (Thm 1.8) random stability for the 3-book of 2 pages and the 4-book of 3 pages; (Thm 1.11) random Green–Ruzsa stability for sum-free subsets of type-$I(q)$ Abelian groups at $p \geq Cn^{-1/2}$ with rate $1-\exp(-\Omega(np_n))$. Also drops the artificial $p_n \ll 1$ condition present in Schacht and Conlon–Gowers.

## Why it matters here
General background; no direct arena tie. Closest contact is methodological — the "stability of dense substructures" framework is the same shape as basin-rigidity / near-optimal-configuration arguments in problems like P1 (sphere packing) and P11 (Hardin–Sloane), where near-extremal solutions are forced to lie near a structured family. The multi-round exposure / induction technique is also a model for proving "every approximately-optimal $X$ is close to one of finitely many structures."

## Open questions / connections
- Does the same framework extend to *exact* (not just approximate) stability — i.e., random analogues of Simonovits' exact stability theorem?
- Beyond Fano / books, are there other 3- and 4-uniform hypergraphs with deterministic stability results that could be transferred? (Author punts because only ~3 known.)
- Connects to and supersedes Conlon–Gowers [arXiv:1011.4310] and Schacht's "Extremal results for random discrete structures"; precedes the hypergraph-container method (Balogh–Morris–Samotij, Saxton–Thomason) which subsumes much of this.
- Open: can the $\exp(-\Omega(n^2 p_n))$ rate be sharpened to match the lower bound from a single $K_2$-removal event?

## Key terms
sparse random graphs, transference theorem, Erdős–Simonovits stability, Kohayakawa–Łuczak–Rödl conjecture, Turán-type extremal, 2-density $m_2(H)$, $(K,p)$-bounded hypergraph, $(\alpha,\mathcal{B})$-stability, multiple exposure trick, hypergraph removal lemma, sum-free sets, Schur triples, Green–Ruzsa, Fano plane stability, Schacht, Conlon–Gowers
