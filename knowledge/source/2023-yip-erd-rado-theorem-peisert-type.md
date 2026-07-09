---
type: source
kind: paper
title: Erdős–Ko–Rado theorem in Peisert-type graphs
authors: Chi Hoi Yip
year: 2023
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2302.00745
source_local: ../raw/2023-yip-erd-rado-theorem-peisert-type.pdf
topic: general-knowledge
cites:
---

# Erdős–Ko–Rado theorem in Peisert-type graphs

**Authors:** Chi Hoi Yip  ·  **Year:** 2023  ·  **Source:** https://arxiv.org/abs/2302.00745

## One-line
Shows that for almost all Peisert-type Cayley graphs over $\mathbb{F}_{q^2}$ with edge density $\le 1/2$, every maximum clique is "canonical" (an $\mathbb{F}_q$-coset translate), extending the Erdős–Ko–Rado theorem from Paley graphs to a much wider random family.

## Key claim
As $q \to \infty$, almost all Peisert-type graphs of type $(\frac{q+1}{2}, q)$ have the stability property $ST(\sqrt{q}/2)$ (every clique of size $\ge q - \sqrt{q}/2$ sits in a canonical clique); when $q=p$ prime, almost all of type $(\lfloor \frac{2p-2}{3}\rfloor, p)$ have strict-EKR, and $ST(p/20)$ holds at density $1/2$. Conversely, if $m = q - o(p^t)$ where $t$ is the largest proper divisor of $n$ ($q=p^n$), almost all such graphs fail strict-EKR.

## Method
A "projective realization" identifies Peisert-type graph cliques with direction sets $D(U) \subset PG(1,q)$ determined by affine point sets $U \subset AG(2,q)$ (Proposition 4.1). Counting Grassmannian $\mathbb{F}_p$-subspaces of size $q$ via $\#Gr(n,2n)(\mathbb{F}_p) \le q^{2n}$ and combining with Corollary 2.3 ($\ge \sqrt{q}+1$ cosets needed to cover a non-subfield $\mathbb{F}_p$-subspace) gives a union-bound argument: the bad-graph density is bounded by $\exp(2(\log q)^2 - \sqrt{q}\log 2) \to 0$. Stability uses Rédei–Megyesi / Gács / Szőnyi direction theorems plus the "bad direction set" exclusion $|\mathcal{B}_q| \le q^5$.

## Result
- Theorem 1.2: $ST(\sqrt{q}/2)$ for almost all type-$(\frac{q+1}{2}, q)$ graphs.
- Theorem 1.3: strict-EKR for almost all type-$(\lfloor\frac{2p-2}{3}\rfloor, p)$; $ST(p/20)$ at density $1/2$ for primes.
- Theorem 1.4: strict-EKR fails almost surely once $m \ge q - o(p^t)$, locating a phase transition around edge density $1/2$.
- Proposition 4.6: improvement to type $(\frac{p^2+p}{2}, p^2)$ via Gács–Lovász–Szőnyi.

## Why it matters here
General background; no direct arena tie — Peisert-type Cayley graphs over finite fields are a structurally distinct extremal-combinatorics setting from the Einstein Arena's geometric optimization problems. Could inform finite-field tooling if a problem involves cyclotomic/strongly-regular constructions or direction-set counting in $AG(2,q)$.

## Open questions / connections
- Baker–Ebert–Hemmeter–Woldar conjecture: second-largest maximal clique in Paley graph of order $q^2$ has size $\frac{q+r(q)}{2}$ — would follow if $D(X) \notin \mathcal{B}_q$ for Paley $X$ (Remark 4.4).
- Complete classification of Peisert-type graphs with strict-EKR (Asgarli–Goryainov–Lin–Yip) — special case of open Problem 16.4.1 (Godsil–Meagher) on orthogonal-array block graphs.
- Phase transition: sharper threshold between density $1/2$ (EKR holds) and $q - o(p^t)$ (EKR fails) is unmapped.
- Extends Blokhuis (1984), Sziklai (1999), Mullin (Peisert graph), and Asgarli–Yip (2022) from specific algebraic families to "generic" Peisert-type graphs.

## Key terms
Erdős–Ko–Rado theorem, Peisert-type graph, Paley graph, maximum clique, Cayley graph, finite field, direction set, pseudo-Paley graph, Blokhuis, Szőnyi, Rédei, strongly regular graph, cyclotomy, Grassmannian, strict-EKR property
