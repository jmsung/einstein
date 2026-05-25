---
type: source
kind: paper
title: Ramanujan complexes and high dimensional expanders
authors: A. Lubotzky
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1301.1028
source_local: ../raw/2012-lubotzky-ramanujan-complexes-high-dimensional.pdf
topic: general-knowledge
cites:
---

# Ramanujan complexes and high dimensional expanders

**Authors:** A. Lubotzky  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1301.1028

## One-line
Survey lecture notes (Takagi 2012) describing Ramanujan graphs, their generalization to Ramanujan complexes via Bruhat–Tits buildings of $PGL_d$, and competing definitions of high-dimensional expansion for simplicial complexes.

## Key claim
Ramanujan graphs (optimal spectral expanders with non-trivial eigenvalues bounded by $2\sqrt{k-1}$) generalize to Ramanujan complexes — finite quotients $\Gamma\backslash B_d$ of Bruhat–Tits buildings of $PGL_d(F)$ — whose spectral properties are controlled by Lafforgue's proof of the Ramanujan conjecture in positive characteristic; but in dimension $\ge 2$ there is no single agreed definition of "expander," with at least three competitors (spectral gap of Laplacians, $\mathbb{F}_2$-coboundary expansion, Cheeger constant on $(d+1)$-partitions) that are provably inequivalent.

## Method
Survey/exposition. Ties together: (i) Alon–Boppana spectral bound and Cheeger inequality $h^2/(8k) \le k - \mu_1 \le h$; (ii) representation-theoretic construction via $K$-spherical unramified reps of $PGL_d(F)$ acting on $L^2(\Gamma\backslash G)$, where tempered = Ramanujan; (iii) explicit arithmetic constructions (LPS graphs from Hamilton quaternions; LSV complexes from division algebras over function fields); (iv) high-dim analogues — Linial–Meshulam coboundary expansion, Parzanchevski–Rosenthal–Tessler Cheeger inequality $\frac{d}{2}\left(1 - \sqrt{1 - \frac{2h(X)}{d|X(0)|}}\right) - (d-1)k \le \lambda(X) \le h(X)$, and Gromov's overlap property.

## Result
- LPS construction: for primes $p \equiv q \equiv 1 \pmod 4$, $p \ne q$, the Cayley graph $X^{p,q}$ on $PGL_2(\mathbb{F}_q)$ (or $PSL_2$ if $p$ is a QR mod $q$) with $p+1$ generators from quaternion solutions of $x_0^2+\cdots+x_3^2 = p$ is a $(p+1)$-regular Ramanujan graph.
- Ramanujan complexes exist as quotients of $B(PGL_d(F))$ for all prime powers $q$ via Lafforgue.
- For $d$-complexes with complete $(d-1)$-skeleton, an expander mixing lemma holds: $|F(A_0,\ldots,A_d)| - k|A_0|\cdots|A_d|/|X(0)| \le \mu_0(X)(|A_0|\cdots|A_d|)^{d/(d+1)}$.
- Gromov: $\mathbb{F}_2$-coboundary expansion $\Rightarrow$ topological overlap property; geometric overlap follows from spectral concentration plus Pach's Tverberg-type theorem.

## Why it matters here
General background; no direct arena tie. Closest relevance: extremal combinatorics / hypergraph problems where high-dim expansion or LDPC-style code constructions matter — most Einstein Arena problems are continuous optimization (sphere packing, autocorrelation, kissing), so this is a meta-reference for the Ramanujan persona and for any future problem touching simplicial / hypergraph extremal structure.

## Open questions / connections
- Open Problem 1.1.9: for $k$ not of the form $p^\alpha+1$ (e.g. $k=7$), do infinitely many $k$-regular Ramanujan graphs exist?
- Conjecture 3.2.4: Gromov "filling" constant $\nu_i(X)$ is bounded uniformly across finite quotients of $B(PGL_d(F))$ for $d \ge 3$.
- Is there a bounded-degree family of higher-dim $\mathbb{F}_2$-coboundary expanders? (Ramanujan complexes fail when $H^1(\Gamma\backslash B, \mathbb{F}_2) \ne 0$.)
- Relation between coboundary expansion and spectral gap remains unclear — examples exist where each is small while the other is bounded.

## Key terms
Ramanujan graph, Ramanujan complex, Bruhat-Tits building, $PGL_d$, Lafforgue, LPS construction, Alon-Boppana, Cheeger constant, spectral gap, coboundary expansion, Gromov overlap property, simplicial complex Laplacian, expander mixing lemma, Hecke operator, automorphic forms
