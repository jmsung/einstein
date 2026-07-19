---
type: source
kind: paper
title: On the number of pentagons in triangle-free graphs
authors: Hamed Hatami, J. Hladký, D. Král, Sergey Norin, A. Razborov
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1102.1634
source_local: ../raw/2011-hatami-number-pentagons-triangle-free-graphs.pdf
topic: general-knowledge
cites:
---

# On the number of pentagons in triangle-free graphs

**Authors:** Hamed Hatami, J. Hladký, D. Král, Sergey Norin, A. Razborov  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1102.1634

## One-line
Proves Erdős's 1984 conjecture that the balanced blow-up of $C_5$ maximizes the pentagon count among triangle-free graphs, via a flag-algebra Cauchy–Schwarz calculation.

## Key claim
Every triangle-free graph $G$ on $n$ vertices contains at most $(n/5)^5$ copies of $C_5$, with equality iff $5 \mid n$ and $G$ is the balanced blow-up of the pentagon; equivalently, $C_5 \le 5!/5^5$ in the flag algebra $\mathcal{A}^0[T_{\text{TF-Graph}}]$.

## Method
Flag-algebra SDP/Cauchy–Schwarz: exhibits an explicit inequality $62500\,C_5 + \sum_i \llbracket Q_i^+(g_i^+) \rrbracket_{\sigma_i} + \cdots \le 2400$ as a sum-of-squares over types $\sigma_0, \sigma_1, \sigma_2, P$ with specified PSD matrices $M_i^\pm$, verifiable by expanding into the 14 triangle-free 5-vertex graphs. Uniqueness is obtained by analyzing the extension measure $P_P$ on $\text{Hom}^+(\mathcal{A}^P, \mathbb{R})$ and showing it collapses to $\phi_{C_5}$; the exact (non-divisible $n$) case uses graph-limit cut-distance stability (Alon's $\delta_\square$ vs $\delta_1$ bound) to force almost-balanced $C_5$ blow-up structure for $n \ge n_0$.

## Result
Density bound $p(C_5, G) \le 5!/5^5$ asymptotically; exact bound $(n/5)^5$ when $5 \mid n$; for sufficiently large $n = 5\ell + a$ the extremal count is $\chi(n) = \ell^{5-a}(\ell+1)^a$, attained only by almost-balanced $C_5$-blow-ups. Settles Erdős's question (iii) on quantifying "non-bipartiteness" of triangle-free graphs by pentagon count. Improves Győri's factor-1.03 bound and Füredi's 1.001 bound to tight.

## Why it matters here
Canonical worked example of the flag-algebra method delivering an exact extremal-combinatorics bound with PSD certificate — directly relevant to Einstein Arena problems in the extremal_graph / combinatorics categories where SDP flag-algebra is a candidate technique. Concretely informs the `techniques/flag-algebras` and `concepts/cauchy-schwarz-sos` wiki entries, and the Razborov persona (this is one of his showcase applications).

## Open questions / connections
- Conjecture 1 (full exact bound for all $n$, including the sporadic $n=8$ Michael example with 8 pentagons) — only proved for $n \ge n_0$ here; finite $n$ regime open.
- Generalization to maximum number of $C_{2\ell+1}$ (and induced $C_{2\ell+1}$) copies in triangle-free graphs; Vaughan reported flag-algebra proofs that $C_7$-blow-ups (resp. pentagon/heptagon blow-ups) are asymptotically extremal for $\ell=3$.
- Extends Razborov's flag-algebra programme (Raz07, Raz08 on triangle densities, Raz10 on 3-hypergraph configurations); independent contemporaneous proof of Theorem 3.1 by Grzesik [Grz12].

## Key terms
flag algebras, triangle-free graphs, pentagon $C_5$, Erdős conjecture, balanced blow-up, Cauchy–Schwarz SOS, semidefinite programming, extremal graph theory, graph homomorphism, graph limits, cut distance, Razborov, Lovász, Győri, extension measure, strong homomorphism
