---
type: source
kind: paper
title: Borsuk-Ulam theorems for products of spheres and Stiefel manifolds revisited
authors: Yu Hin Chan, Shujian Chen, F. Frick, J. Hull
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1902.00935
source_local: ../raw/2019-chan-borsuk-ulam-theorems-products-spheres.pdf
topic: general-knowledge
cites:
---

# Borsuk-Ulam theorems for products of spheres and Stiefel manifolds revisited

**Authors:** Yu Hin Chan, Shujian Chen, F. Frick, J. Hull  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1902.00935

## One-line
Gives a more elementary, degree-parity-based proof of Ramos' general Borsuk–Ulam theorem for products of spheres and uses it to sharpen Fadell–Husseini's Borsuk–Ulam theorem on Stiefel manifolds.

## Key claim
Every $(\mathbb{Z}/2)^k$-equivariant map $V_{n,k} \to \mathbb{R}^{n-1} \oplus \mathbb{R}^{n-2} \oplus \cdots \oplus \mathbb{R}^{n-k}$ (with $\varepsilon_j$ acting by sign-flip on the $j$th factor) has a zero (Theorem 1.1), closing the $\binom{k}{2}$-dimensional gap in Fadell–Husseini's result that mapped $V_{n,k} \to (\mathbb{R}^{n-k})^k$.

## Method
Defines a $\mathbb{Z}/2$-valued obstruction $r(n_1,\ldots,n_k;V) \in \mathbb{Z}/2$ as the parity of the degree of an equivariant map restricted to a fundamental-domain boundary, using mapping-degree theory plus the Kushkuley–Balanov congruence ($\deg f_1 \equiv \deg f_2 \pmod{|G|}$ for free actions). Derives a recursion (Theorem 2.5) that reduces $r(n_1,\ldots,n_k;V)$ via Pascal-like identities; Stiefel results follow by extending $V_{n,k} \to S(V)$ to $(S^{n-1})^k \to V$ and appending the orthogonality coordinates $\langle x_i,x_j\rangle$ as an extra equivariant block in $\bigoplus_{|\alpha|=2} V_\alpha$.

## Result
Theorem 1.1 (Stiefel BU with telescoping codomain $\mathbb{R}^{n-1}\oplus\cdots\oplus\mathbb{R}^{n-k}$, $\binom{k}{2}$ dimensions tighter than Fadell–Husseini). Theorem 3.3 generalizes to arbitrary $(\mathbb{Z}/2)^k$-actions on the codomain. Corollary 3.5 restricts zeros of any equivariant $V_{n,k} \to (V_{\varepsilon_1}\oplus\cdots\oplus V_{\varepsilon_k})^{\oplus(n-k)}$ to a fixed codimension-$\binom{k}{2}$ submanifold $M = \{(x_1,\ldots,x_k) \in S^{n-k}\times\cdots\times S^{n-1} : \langle x_i,x_j\rangle = 0\}$. Lemma 3.2: $r(k-1,k-2,\ldots,1,0;\bigoplus_{|\alpha|=2}V_\alpha)=1$. Remark 2.8: $r(n_1,n_2;V_{\varepsilon_1+\varepsilon_2}^{\oplus(n_1+n_2)})=1$ iff $\binom{n_1+n_2}{n_1}$ is odd (binary expansions of $n_1,n_2$ share no common 1).

## Why it matters here
General background; no direct arena tie. Closest contact is the parity/Lucas-style condition on $\binom{n_1+n_2}{n_1}$ (a discrete combinatorial invariant), and the general principle that codomain-dimension counting plus a degree-mod-$|G|$ argument yields tight nonexistence bounds — a stance reusable for any extremal problem whose obstruction can be cast as an equivariant map.

## Open questions / connections
- Can the codimension-$\binom{k}{2}$ submanifold $M$ in Corollary 3.5 be further shrunk while retaining a zero?
- Extends Fadell–Husseini [8], Ramos [16], Dzedzej–Idzik–Izydorek [7]; reproves Mani-Levitska–Vrećica–Živaljević [11] obstruction for $S^{3n-1}\times S^{3n-2}\to S((V_{\varepsilon_1}\oplus V_{\varepsilon_2}\oplus V_{\varepsilon_1+\varepsilon_2})^{\oplus(2n-1)})$ at $n=2^t$.
- Connection to hyperplane mass-partition (Grünbaum–Hadwiger–Ramos), Tverberg-type results, and topological lower bounds for chromatic numbers of hypergraphs.

## Key terms
Borsuk-Ulam theorem, Stiefel manifold, equivariant map, mapping degree, $(\mathbb{Z}/2)^k$-action, products of spheres, Fadell-Husseini index, Ramos theorem, hyperplane mass partition, Tverberg, obstruction cocycle, Kushkuley-Balanov
