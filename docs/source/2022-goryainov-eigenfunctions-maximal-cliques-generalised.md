---
type: source
kind: paper
title: On eigenfunctions and maximal cliques of generalised Paley graphs of square order
authors: S. Goryainov, L. Shalaginov, Chi Hoi Yip
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2203.16081
source_local: ../raw/2022-goryainov-eigenfunctions-maximal-cliques-generalised.pdf
topic: general-knowledge
cites:
---

# On eigenfunctions and maximal cliques of generalised Paley graphs of square order

**Authors:** S. Goryainov, L. Shalaginov, Chi Hoi Yip  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2203.16081

## One-line
Constructs new maximal-but-not-maximum cliques in generalised Paley graphs $GP(q^2, m)$ with $m \mid (q+1)$, proves the weight-distribution bound is tight for the smallest eigenvalue $-\frac{q}{m}+1$, and improves stability of the EKR-type theorem for canonical cliques.

## Key claim
For $m \mid (q+1)$, $m > 1$: (1) explicit maximal cliques of size $\frac{q}{m}+1$ or $\frac{q}{m}+2$ exist in $GP(q^2,m)$ (Theorem 5.3); (2) the weight-distribution bound on $|\mathrm{supp}(f)|$ is tight for eigenvalue $-\frac{q}{m}+1$ (Theorem 4.3); (3) any non-maximum maximal clique $C'$ satisfies $|C'| \le (\frac{q}{m}+1-1)^2$, improving to $|C'| \le 1 + \frac{q}{m}+1(\frac{q}{m}+1 - 3)$ when $p \nmid (m-1)$ and $m \le \frac{q+1}{4}$ (Theorem 6.1).

## Method
Identifies $GP(q^2, m)$ with the block graph of an orthogonal array $\mathrm{OA}(\frac{q+1}{m}, q)$ built from $m$-ary slopes in the affine plane $AG(2,q)$. Combines this geometric realization with Katz-type incomplete character-sum bounds (Lemma 2.9) over affine $\mathbb{F}_p$-lines to rule out subfield obstructions, plus the Blokhuis–Sziklai polynomial-method EKR theorem (Lemma 1.1) for control of maximum cliques. Eigenfunction tightness is shown by exhibiting induced complete bipartite subgraphs of the critical size $2 \cdot \frac{q}{m}+1$.

## Result
Theorem 4.3 closes the support gap by realising the lower bound $2(\frac{q}{m}+1)$ with explicit eigenfunctions. Theorem 5.3 constructs the new clique family $N(u) \cup \{u\}$ (size $\frac{q}{m}+1$) and $N(u) \cup \{u, u^q\}$ (size $\frac{q}{m}+2$) under $\gcd(q-1, \frac{q}{m}+1-2) \in \{1,2\}$. Corollary 6.2 sharpens Sziklai's $q - (1-1/m)\sqrt q$ stability threshold to $(\frac{q}{m}+1 - 1)^2$ whenever $m > \frac{q+1}{\sqrt q + 1}$. Example 5.9 ($q = r^3$, $m = r^2-r+1$) shows these bounds are tight up to subfield obstructions.

## Why it matters here
General background; no direct arena tie. Closest adjacency is to extremal graph / EKR-stability themes (relevant to combinatorics problems if any in the 23-problem inventory touch on Cayley-graph clique numbers or strongly-regular-graph spectra); the orthogonal-array $\leftrightarrow$ block-graph trick is a transferable algebraic-combinatorics technique.

## Open questions / connections
- Improve the stability lower bound on $|C|$ from $q - O(\sqrt q)$ toward the conjectured $q/m + O(1)$ (open even for $m=2$ Paley graphs at $\frac{q+3}{2}$).
- Conjecture 4.9: $N(\alpha) \cup \{\alpha, -\alpha\}$ remains a maximal clique in cubic Paley graphs $GP(q^2, 3)$ when $q \equiv 1 \pmod 4$ (verified computationally for $q \le 1200$).
- Extension of all results to general Peisert-type Cayley graphs on $\mathbb{F}_{q^2}^+$ with connection set a union of $\mathbb{F}_q^*$-cosets — most arguments port, but parameters are messier.

## Key terms
generalised Paley graph, maximal clique, eigenfunction, weight-distribution bound, strongly regular graph, orthogonal array block graph, affine plane $AG(2,q)$, Erdős-Ko-Rado theorem, Blokhuis, Sziklai, Katz character sum, Peisert-type graph, cyclotomic, subfield obstruction
