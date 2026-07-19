---
type: source
kind: paper
title: Distribution of power residues over shifted subfields and maximal cliques in generalized Paley graphs
authors: Greg Martin, Chi Hoi Yip
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2403.04312v2
source_local: ../raw/2024-martin-distribution-power-residues-shifted.pdf
topic: general-knowledge
cites: 
---

# Distribution of power residues over shifted subfields and maximal cliques in generalized Paley graphs

**Authors:** Greg Martin, Chi Hoi Yip  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2403.04312v2

## One-line
Asymptotic count for $d$-th-power residues lying in a shifted subfield, used to build new families of maximal (non-maximum) cliques in generalized Paley graphs and Peisert graphs.

## Key claim
For $d \ge 2$, $q \equiv 1 \pmod d$, and any $m$ with $\operatorname{rad}(m) \mid \operatorname{rad}(d)$, the $d$-Paley graph $GP(q^d, d)$ contains a maximal clique of size $q/m + O(d \log_r m \cdot \sqrt{q})$, where $r$ is the smallest prime divisor of $d$; in particular many "fractional-of-subfield" sizes $q/m$ are realized.

## Method
Weil's bound on multiplicative character sums, combined with the norm-map criterion $N_{F_{q^n}/F_q}(x)$ a $d$-th power $\iff x$ a $d$-th power (Lemma 2.1), gives the local count of common $d$-th-power neighbors in a subfield: $M = q \prod_i \gcd(d/d_i, n)/(d/d_i) + O(\sum_i d_i \sqrt{q})$ where $d_i = [\mathbb F_q(v_i):\mathbb F_q]$ (Theorem 1.2). A companion bound via Dirichlet characters over function fields (Theorem 3.2) handles the $n=2$ case where $q \not\equiv 1 \pmod d$. Cliques are then built by inductively choosing $v_1, \dots, v_k$ of prescribed subfield degrees $d_1 \mid \dots \mid d_k \mid d$ with $\prod d_i = m$, and taking their common $\mathbb F_q$-neighborhood.

## Result
Three concrete theorems: (1) Theorem 1.4 — for $q > (8\log_r m + 4) d^2 m^2$, maximal cliques of size $\approx q/m$ in $GP(q^d, d)$ exist for every $m$ with $\operatorname{rad}(m)\mid\operatorname{rad}(d)$; (2) Theorem 1.5 — confirms the Goryainov–Shalaginov–Yip conjecture: in $GP(q^2, d)$ with $d \mid q+1$, $d \ge 3$, and $q > 10 d^4/(d-1)^2$, the $(\mathbb F_q, \alpha)$-construction $N(u) \cup \{u\}$ (or $\cup\{u, u^q\}$) is a maximal clique of size $(q+1)/d$ or $(q+d+1)/d$; (3) Theorem 1.6 — the analogous $(\mathbb F_q,\alpha)$-cliques of size $(q+1)/2$ are maximal in Peisert graphs $P^*_{q^2}$ for all $q \equiv 3\pmod 4$, $q\ge 7$. Conjecture 6.4: the limit points of $r_q/q$ over maximal-clique sizes are exactly $\{0\} \cup \{1/m : \operatorname{rad}(m)\mid\operatorname{rad}(d)\}$.

## Why it matters here
General background; no direct arena tie. Closest hooks are P7 / Sidon-like extremal-set problems and any future problem involving cliques in Cayley graphs over finite fields — the norm-criterion + Weil-bound recipe for counting power residues in a shifted subfield is a clean, reusable technique if extremal-set work over $\mathbb F_q$ surfaces.

## Open questions / connections
- Baker–Ebert–Hemmeter–Woldar second-largest-clique conjecture: no maximal clique in $GP(q^2,2)$ has size strictly between $(q+\delta_q)/2 + 1$ and $q-1$ — still open; Conjecture 6.4 here is a strict generalization.
- Clique number of Paley graphs of non-square order — major open problem in additive combinatorics (Croot–Lev surveys), not addressed but motivated.
- Extends Hirschfeld–Szőnyi (1991) square-order Paley results from $d=2$ to general $d$ and from quadratic extensions to degree-$d$ extensions.
- Gives a new (clique-structural) proof that $P_{q^2}$ and $P^*_{q^2}$ are non-isomorphic for $q\equiv 3 \pmod 4$, $q\ge 7$, sidestepping Peisert's group-theoretic argument.

## Key terms
generalized Paley graph, Peisert graph, maximal clique, $(F_q,\alpha)$-construction, Weil bound, character sum, power residue, shifted subfield, norm map, Cayley graph, Erdős–Ko–Rado, finite field, Dirichlet character
