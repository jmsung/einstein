---
type: source
kind: paper
title: On maximal cliques of Cayley graphs over fields
authors: Chi Hoi Yip
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2101.09652
source_local: ../raw/2021-yip-maximal-cliques-cayley-graphs.pdf
topic: general-knowledge
cites:
---

# On maximal cliques of Cayley graphs over fields

**Authors:** Chi Hoi Yip  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2101.09652

## One-line
Constructs a new family of maximal cliques with vector-space structure in Cayley graphs over fields, and uses it to prove the subfield $\mathbb{F}_{p^r}$ is a maximal clique in cubic and quadruple Paley graphs of cubic/quartic order.

## Key claim
If $S \subset F \setminus \{0\}$ is a multiplicatively closed connection set with $-1 \in S$ and a proper subfield $K \subset F$ forms a clique in $\mathrm{Cay}(F^+; S)$, then there exists a $K$-subspace $V \supseteq K$ that is a *maximal* clique. Applied: $\mathbb{F}_{p^r}$ is a maximal clique in $GP(p^{3r}, 3)$ when $p^{3r} \equiv 1 \pmod 6$, and in $GP(p^{4r}, 4)$ for any odd $p$.

## Method
Algebraic/structural — uses Zorn's lemma on the poset of $K$-subspace cliques to produce a maximal element; a key lemma shows that if a $K$-subspace clique $V$ extends by some $g$, then $V \oplus gK$ is also a clique (relying on $S$ being multiplicatively closed). Combined with the trivial $\sqrt{q}$ upper bound on $\omega(GP(q,d))$ and refined bounds (Theorem 3.4–3.5 of Yip 2021, plus a Lucas-theorem argument for $p \equiv 3 \pmod 4$) to rule out larger subspace cliques.

## Result
For $q = p^{3r}$ with $p^{3r} \equiv 1 \pmod 6$: $\mathbb{F}_{p^r}$ is a maximal clique in the cubic Paley graph $GP(q,3)$ — and when $p^r \equiv 5 \pmod 6$, this gives an explicit non-maximum maximal clique (max clique is $\mathbb{F}_{p^{3r}}$ of size $p^{3r}$). For $q = p^{4r}$ odd: $\mathbb{F}_{p^r}$ is a maximal clique in $GP(q,4)$. For Peisert graphs $P^*_q$ with $q = p^{4r}$, $p \equiv 3 \pmod 4$: if $\mathbb{F}_{p^r}$ is *not* maximal, then $\omega(P^*_q) = \sqrt{q}$ and $\{1, h, g^2, g^2h\}$ is a basis. Computationally: $\omega(P^*_{81}) = 9$, $\omega(P^*_{2401}) = 17$.

## Why it matters here
General background; no direct arena tie — the einstein arena problems don't currently include Cayley/Paley graph clique problems, but the technique (subspace-structured cliques on finite-field constructions) is the same algebraic toolkit used in Sidon-set, kissing-number, and finite-geometry extremal problems where subfield constructions yield lower bounds.

## Open questions / connections
- Conjecture 1.4: $\mathbb{F}_{p^r}$ is always a maximal clique in $GP(q,d)$ at the natural subfield-construction parameters — open in general.
- Conjecture 4.3/4.4: For $q > 3$ with $p \equiv 3 \pmod 4$, $\omega(P^*_{q^4}) < q^2$; $P^*_{81}$ is conjectured the unique exception attaining the $\sqrt{q}$ bound.
- Extends Blokhuis (1984) and Sziklai (1999) classifications of maximum cliques in $P_{q^2}$; complements Baker et al. and Goryainov et al. on non-maximum maximal cliques in square-order Paley graphs.

## Key terms
Cayley graph, Paley graph, Peisert graph, generalized Paley graph, maximal clique, clique number, finite field, subfield clique, Zorn's lemma, multiplicative subgroup, self-complementary symmetric graph, Lucas's theorem
