---
type: source
kind: paper
title: Three tutorial lectures on entropy and counting
authors: David J. Galvin
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1406.7872
source_local: ../raw/2014-galvin-three-tutorial-lectures-entropy.pdf
topic: general-knowledge
cites:
---

# Three tutorial lectures on entropy and counting

**Authors:** David J. Galvin  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1406.7872

## One-line
Tutorial notes introducing Shannon entropy as a combinatorial enumeration tool, with worked applications to counting subsets, projections, permanents, colorings, and graph homomorphisms.

## Key claim
The entropy method — built on Maximality of the uniform ($H(X) \le \log|\text{range}(X)|$, equality when $X$ is uniform), Subadditivity, the Chain rule, Dropping conditioning, and Shearer's lemma — yields short proofs of tight bounds in combinatorial enumeration, including Loomis–Whitney ($|B| \le \prod_j |B_j|^{1/(n-1)}$), Brégman's permanent bound, and Galvin–Tetali's $\hom(G,H) \le \hom(K_{d,d},H)^{n/2d}$ for $d$-regular bipartite $G$.

## Method
Encode an unknown set $C$ as the entropy of a uniformly chosen element $X \in C$, so $|C| = 2^{H(X)}$, then bound $H(X)$ by decomposing $X$ as a random vector $(X_1,\dots,X_n)$ and applying Shearer's lemma: for a cover $\mathcal{F}$ of $[n]$ where each $i$ lies in $\ge t$ sets, $H(X_1,\dots,X_n) \le \tfrac{1}{t}\sum_{F\in\mathcal{F}} H(X_F)$. Local entropies $H(X_F)$ are then estimated combinatorially (often via $|\text{trace}_F(\mathcal{A})|$) or, in the Galvin–Tetali / Kahn coloring proof, via the Chain rule plus Jensen's inequality on conditional distributions over neighborhood colorings.

## Result
Worked tight/near-tight bounds include: $\sum_{i\le \alpha n}\binom{n}{i} \le 2^{H(\alpha)n}$; coin-weighing lower bound $f(n) \ge (2n\log n)/\log n \cdot (1+\Omega(1/\log\log n))$ (Erdős–Rényi, sharpened by Pippenger); Loomis–Whitney isoperimetric projection inequality; Brégman's bound on permanents of 0/1 matrices with fixed row sums (Radhakrishnan's proof); $c_q(G) \le c_q(K_{d,d})^{n/2d}$ for $d$-regular bipartite $G$ (tight when $2d \mid n$); and a non-bipartite weakening $\hom(G,H) \le \prod_v \hom(K_{p(v),p(v)},H)^{1/d}$ via Kahn's second conditional Shearer.

## Why it matters here
Direct relevance to einstein-arena problems in extremal graph theory, sphere packing/kissing-number bounds, and combinatorial enumeration: Shearer's lemma and conditional entropy are the standard machinery behind LP/entropy upper bounds (e.g., Kahn's independent-set bound, Galvin–Tetali, Lubetzky–Zhao) that often parallel or complement Cohn–Elkies-style LP duality arguments. Provides a clean toolkit (subadditivity, Shearer, Chain rule, Dropping conditioning, Jensen) for proving tight upper bounds on counting/projection quantities that arise in autocorrelation and discrete-geometry problems.

## Open questions / connections
- Upper Matching Conjecture (Friedland–Krop–Markström): $|M_t(G)| \le |M_t(K(n,d))|$ for $d$-regular $G$ — open for general $t$; entropy-friendly target.
- Kahn's conjecture: $i_t(G) \le i_t(K(n,2d))$ for independent sets of fixed size $t$ — open beyond $t \le 4$.
- Extending Galvin–Tetali $\hom(G,H) \le \hom(K_{d,d},H)^{n/2d}$ to non-bipartite $d$-regular $G$ — false for general $H$ (Sernau), open for $H = K_q$ and the Widom–Rowlinson graph $H_{WR}$.

## Key terms
Shannon entropy, Shearer's lemma, subadditivity, conditional entropy, chain rule, Loomis–Whitney inequality, Brégman's theorem, Kahn–Lovász theorem, graph homomorphisms, independent sets, Galvin–Tetali, permanent of 0-1 matrix, Friedgut–Kahn, intersecting families, coin-weighing problem, binomial coefficient bounds, Jensen's inequality, Maximality of the uniform
