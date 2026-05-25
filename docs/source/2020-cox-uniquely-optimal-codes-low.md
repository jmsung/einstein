---
type: source
kind: paper
title: Uniquely optimal codes of low complexity are symmetric
authors: C. Cox, E. King, D. Mixon, Hans Parshall
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2008.12871
source_local: ../raw/2020-cox-uniquely-optimal-codes-low.pdf
topic: general-knowledge
cites:
---

# Uniquely optimal codes of low complexity are symmetric

**Authors:** C. Cox, E. King, D. Mixon, Hans Parshall  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2008.12871

## One-line
Formalizes "optimality implies symmetry" by conjecturing that uniquely optimal codes of polynomial-time complexity in compact metric spaces must be invariant under some nontrivial isometry, then tests this across many concrete spaces.

## Key claim
**Conjecture A**: In any "unicorn space" $(M,d)$ — a compact metric space with a polynomial-time computable sequence $\{C_i\}$ of uniquely optimal codes of sizes $n_1 < n_2 < \cdots$ — for all sufficiently large $i$, there exists $g \in G \setminus \{\mathrm{id}\}$ in the isometry group with $g C_i = C_i$. **Conjecture B**: optimal codes of size $|C_i| - 1$ retain a "partial symmetry" $|gC \cap C| > t$, where $t$ is the symmetry strength of $M$. Verified/supported in interval, circle, equilateral triangle, orthotopes under $\|\cdot\|_\infty$, metric trees, ultrametric spaces, an $\ell^p$ example, and partially the Hilbert cube.

## Method
Definitional/structural: rigorize "low complexity" via Turing-machine-style polynomial-time encoding of $(M,d)$ over strings (Def 4: U1–U4 conditions on metric computability and code computability). For metric graphs, the proof tool is a **linear-programming relaxation** parametrized by per-edge point assignments $\{t_e\}_{e \in E}$, which becomes tight once $|C| \geq 2 \sum_e w_e / \min_e w_e$. Orthotope characterization uses **volume/Minkowski-sum packing bounds** ($|C| \leq \prod_i(u_i/\delta + 1)$) combined with a **rattle-elimination argument** forcing $\delta \mid u_i$ for each coordinate. Spherical orthoplex-bound case uses **Perron–Frobenius on $I-G$** (Gram matrix) to decompose into orthogonal blocks.

## Result
**Theorem 2** (orthoplex bound): equality cases at $|X| = d+k$ on $S^{d-1}$ decompose into orthogonal blocks $X_0 \sqcup X_1 \sqcup \cdots \sqcup X_l$ with $l \geq k$, $|X_i| = \dim\mathrm{span}\, X_i + 1$. **Theorem 7** (orthotopes): $(M, \|\cdot\|_\infty)$ is a unicorn space iff coordinates of $u$ are commensurable; unique optimal codes have size $\prod_i(u_i/\delta + 1)$ for some divisor $\delta \mid \gcd(u)$. **Theorem 20**: unit-distance metric graphs $(M,d)$ on a graph $G$ admit a unicorn sequence of size $|V| + k|E|$ iff $G$ is a tree or has no leaves. **Theorem 21**: complete divisibility characterization for unique optimal codes on metric trees via leaf-pairing functions $f, g$ with $\delta \mid d(u,f(u)) + d(u,v)$. **Lemma 24**: homogeneous ultrametric spaces without isolated points have infinite symmetry strength (so Conj. A/B trivially hold).

## Why it matters here
Directly relevant to multiple Arena problems involving optimal codes — sphere-packing/Tammes-type ($P_1, P_{15}, P_{16}$), kissing-number, and any "$n$ points in compact space maximizing min-distance" formulation. Provides a **heuristic prior**: if a putatively optimal config lacks symmetry, suspect either non-uniqueness (rattle) or sub-optimality — a useful sanity check on candidate solutions and an argument for **parametrizing optimizers in the symmetric subspace** (dimension reduction).

## Open questions / connections
- Tori $\mathbb{R}^4/D_4$, $\mathbb{R}^8/E_8$, $\mathbb{R}^{24}/\Lambda_{24}$ conjectured to be unicorn spaces with lattice-code unicorn sequences — uniqueness proofs needed.
- Equilateral-triangle optimal codes of size $T(k)-1$ (Erdős–Oler conjecture) and Lubachevsky–Graham–Stillinger sizes still open; LP-bound approach may resolve.
- Whether every unicorn ultrametric space has infinite symmetry strength; characterizing optimal codes of size $\geq 4$ in the Hilbert cube; is the Hilbert cube a unicorn space?
- How to extend the unicorn formalism to spaces (sphere, $\mathbb{CP}^{d-1}$, Grassmannians) that lack polynomial-time-computable uniquely-optimal sequences.

## Key terms
optimal codes, symmetry-optimality correspondence, unicorn space, Rankin orthoplex bound, rattler/rattle, symmetry strength, partial symmetries, metric tree, orthotope codes, ultrametric space, Hilbert cube, linear programming bound, spherical codes, Tammes problem, Cohn–Kumar, Viazovska, $E_8$ lattice, Leech lattice, Elekes–Sharir, Guth–Katz
