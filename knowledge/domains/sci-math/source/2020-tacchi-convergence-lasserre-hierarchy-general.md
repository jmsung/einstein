---
type: source
kind: paper
title: "Convergence of Lasserre’s hierarchy: the general case"
authors: M. Tacchi
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2011.08139
source_local: ../raw/2020-tacchi-convergence-lasserre-hierarchy-general.pdf
topic: general-knowledge
cites:
---

# Convergence of Lasserre's hierarchy: the general case

**Authors:** M. Tacchi  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2011.08139

## One-line
A unified proof that Lasserre's moment-SOS hierarchy converges to the optimal measure for *any* instance of the generalized moment problem (GMP), not just polynomial optimization.

## Key claim
Under three assumptions — (A1) ball constraints / Archimedean property on each $K_i$, (A2) uniformly bounded mass $z_{i,0} \le C_i$ on pseudo-moment sequences, and (A3) existence of a unique optimal measure $\mu^\star$ — the degree-$d$ pseudo-moment sequences $z^d$ converge entrywise to the moments of $\mu^\star$ in the weak-$*$ topology of $\ell^\infty(\mathbb{N}^n)$, and strong duality $p^\star_{GM} = d^\star_{GM}$ and $p^d_{GM} = d^d_{GM}$ both hold.

## Method
Pseudo-moment sequences are shown bounded via a Lemma using the ball/Archimedean constraint: $|z_k| \le z_0 \max(1, R^{2d})$. Strong duality at each level follows from Barvinok's closed-cone criterion applied to the cone $K_d := \{(A_d z, L_z(c)) : z \in X_d\}$, with $P_d := \{z \in X_d : z_0 = 1\}$ shown to be a compact convex base. Convergence then follows from Banach-Alaoglu (weak-$*$ compactness in $\ell^\infty$) plus Putinar's Lemma to identify the limit as a true moment sequence, with uniqueness (A3) forcing the whole sequence to converge.

## Result
Theorem 4 gives, under A1-A3, $z^d_{i,k} \to \int x^k\, d\mu^\star_i(x)$ for every $k \in \mathbb{N}^{n_i}$, hence $p^d_{GM} \to p^\star_{GM}$ and $d^d_{GM} \to d^\star_{GM}$. Corollary 8 weakens A3: without uniqueness, a *subsequence* converges to *some* optimal $\mu_\infty$, and the value-level results ($p^d_{GM} \to p^\star_{GM}$, strong duality) still hold. A worked example $\min_{x \in [0,1]} (1-x)x$ shows the non-uniqueness case empirically — the hierarchy appears to drift toward $\delta_0$ but solver-dependent.

## Why it matters here
General background; no direct arena tie. Relevant only if a problem is recast as a GMP solved by moment-SOS (e.g., SDP relaxations of packing / autocorrelation problems via $L_z(p) \ge 0$ constraints); informs when such a hierarchy is guaranteed to give the right *answer*, not just a monotone bound. Connects to existing wiki content on SDP relaxation usefulness (cf. `findings/sdp-relaxation-uselessness`).

## Open questions / connections
- Extends Josz-Henrion 2016 (strong duality for POP) and Lasserre Theorem 5.6(b) (POP convergence) to all GMP instances including OCP, region-of-attraction, volume, PDE moments.
- Leaves open: rate of convergence (the proof is qualitative); behavior when A3 fails (multiple optimal measures — sequence may oscillate among them, solver-dependent).
- Practical check of A2 (uniformly bounded mass) is hard in some applications (e.g. reachable-set [12], invariant-set [15]); paper notes this but doesn't resolve.

## Key terms
Lasserre hierarchy, moment-SOS, generalized moment problem, GMP, semidefinite programming, SDP, Putinar Positivstellensatz, Archimedean property, localizing matrix, Riesz functional, polynomial optimization, strong duality, weak-* convergence, Banach-Alaoglu, pseudo-moment sequence
