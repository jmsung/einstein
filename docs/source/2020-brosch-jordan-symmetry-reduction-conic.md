---
type: source
kind: paper
title: "Jordan symmetry reduction for conic optimization over the doubly nonnegative cone: theory and software"
authors: Daniel Brosch, Etienne de Klerk
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2001.11348
source_local: ../raw/2020-brosch-jordan-symmetry-reduction-conic.pdf
topic: general-knowledge
cites:
---

# Jordan symmetry reduction for conic optimization over the doubly nonnegative cone: theory and software

**Authors:** Daniel Brosch, Etienne de Klerk  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2001.11348

## One-line
Extends Parrilo–Permenter's Jordan symmetry reduction from symmetric cones to the doubly nonnegative cone $D_n = S^n_+ \cap \mathbb{R}^{n\times n}_+$, and ships a Julia package `SDPSymmetryReduction.jl` that automatically finds the minimal admissible partition subspace for an SDP.

## Key claim
For conic problems over $D_n$ that contain $I$ and $J$ (which includes the Zhao–Karisch–Rendl–Wolkowicz QAP SDP and the $\vartheta'$-function SDP), the optimal admissible reducing subspace is automatically a **Jordan configuration** (a unital 0/1-basis partition subspace closed under squaring), and it can be found by a randomized partition-refinement algorithm (Algorithm 3) that is at least as strong as group-symmetry reduction and Weisfeiler–Leman coherent-algebra reduction — and strictly stronger on at least one QAPLib instance (esc16f).

## Method
Reformulate the CSIC (Constraint Set Invariance Conditions) of Parrilo–Permenter for the $D_n$ cone: prove (Prop. 3.1, 3.5, 3.6) that any orthogonal projection $P_S$ with $P_S(D_n)\subseteq D_n$ and $I\in S$ already satisfies $P_S(N_n)\subseteq N_n$, forcing $S$ to admit a nonnegative orthonormal basis with disjoint supports — i.e. a partition subspace. Find this subspace via a randomized refinement: initialize $P \leftarrow \text{part}(C_L) \wedge \text{part}(X_{0,L^\perp})$, then iterate $P \leftarrow P \wedge \text{part}(P_L(X)) \wedge \text{part}(X^2)$ for a random $X\in P$ until stable. Then numerically block-diagonalize the resulting Jordan algebra (Murota–Kanno–Kojima–Kojima algorithm) and solve the much smaller SDP.

## Result
- **QAP SDP relaxation (Zhao et al.):** Theorem 4.1 shows the minimal admissible subspace is always a Jordan configuration for $n>2$. Applied to QAPLib, reproduces all previously known group-symmetry reductions, beats them on `esc16f`, and reduces several larger instances (e.g. `chr18b`: $52650 \to 14742$ dim) for the first time in ~0.4 s.
- **$\vartheta'$ of Erdős–Rényi (incidence) graphs $ER(q)$:** the reduction collapses to blocks of structure $3\times 1, 2\times \lceil q/2\rceil$; e.g. $q=97$ reduces a 9507-dim problem to a tiny LP in seconds. Bounds match the eigenvalue (EV) bound (5.1) to within $\sim 1$ unit.
- **Software:** `SDPSymmetryReduction.jl` exposes `admPartSubspace(C,A,b)` and `blockDiagonalize(P)` — the first public implementation of numerical $*$-algebra block diagonalization.

## Why it matters here
General background for any SDP-relaxation-of-combinatorial-problem workflow: the einstein wiki already discusses Lovász $\vartheta$ / SDP relaxations and the "SDP relaxation uselessness" finding for P1; this paper supplies the *correct* symmetry-reduction toolchain that can collapse a 10⁴-dim SDP to a 10²-dim one before solving — directly relevant if any arena problem reduces to a doubly-nonnegative-cone SDP with latent symmetry (kissing-like configurations, QAP-shaped energy minimizations, $\vartheta'$ bounds on stability/independence). No direct P1–P23 tie identified.

## Open questions / connections
- Does $D_n$-positive imply $S^n_+$-positive for orthogonal projections? (Open in paper.)
- Is every Jordan configuration the symmetric part of some coherent configuration? (Cameron 2003, [16] p.218 — still open.)
- Extends Parrilo–Permenter (2020) and de Klerk–Sotirov (2010, 2012); generalizes Schrijver-1979 / Bachoc–Gijswijt–Schrijver–Vallentin symmetry-reduction lineage.
- Suggests an avenue: any combinatorial arena problem with a natural QAP / stable-set / coloring SDP relaxation should be preprocessed through `admPartSubspace` before solving.

## Key terms
Jordan algebra, symmetry reduction, doubly nonnegative cone, semidefinite programming, SDP relaxation, quadratic assignment problem, QAP, Lovász theta prime, $\vartheta'$-function, Erdős–Rényi graph, coherent configuration, Weisfeiler–Leman, partition subspace, block diagonalization, Parrilo–Permenter, Zhao–Karisch–Rendl–Wolkowicz, independence number, stable set, admissible subspace, Julia SDPSymmetryReduction
