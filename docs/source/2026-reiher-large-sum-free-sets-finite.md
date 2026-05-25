---
type: source
kind: paper
title: Large sum-free sets in finite vector spaces II
authors: Christian Reiher, Sofia Zotova
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2604.02894v1
source_local: ../raw/2026-reiher-large-sum-free-sets-finite.pdf
topic: general-knowledge
cites: 
---

# Large sum-free sets in finite vector spaces II

**Authors:** Christian Reiher, Sofia Zotova  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2604.02894v1

## One-line
Determines the second-largest sum-free set size $\mathrm{sf}_1(\mathbb{F}_5^n)$ in 5-element finite vector spaces, closing the last open prime case in this hierarchy.

## Key claim
For every $n \geq 3$, $\mathrm{sf}_1(\mathbb{F}_5^n) = 28 \cdot 5^{n-3}$, and every sum-free $A \subseteq \mathbb{F}_5^n$ with $|A| \geq 28 \cdot 5^{n-3}$ is either *normal* (contained in $H \cup (-H)$ for an affine hyperplane $H$) or a *VL-set* (isomorphic to $\Lambda \times \mathbb{F}_5^{n-3}$ for the Lev–Versteegen configuration $\Lambda \subseteq \mathbb{F}_5^3$ of size 28).

## Method
Reduction to combinatorial analysis of "fishy" density functions $f_\varphi^A : \mathbb{F}_5^2 \to \mathbb{R}_{\geq 0}$ obtained by projecting $A$ through linear epimorphisms $\varphi : \mathbb{F}_5^n \to \mathbb{F}_5^2$, with bounded $\ell^1, \ell^\infty$ norms and a sum-free triangle inequality. Heavy use of Kneser's theorem on sumset sizes plus its symmetry-subgroup structure (via $\mathrm{Sym}(A+B)$) to force the support of $f_\varphi^A$ either onto three parallel lines (yielding normality via Lemma 5.5) or onto one of three exceptional configurations $f_\alpha, f_\beta, f_\gamma$ (yielding VL-structure via Lemma 5.9). Three-dimensional refinement uses "acceptable" functions on $\mathbb{F}_5^3$ and induction on $n$.

## Result
$\mathrm{sf}_1(\mathbb{F}_5^n) = 28 \cdot 5^{n-3}$ with full classification of extremal sets; also $\mathrm{sf}_1(\mathbb{F}_5^2) = 5$ with two isomorphism classes. As corollary, $t(\mathbb{F}_5^3) = 28$ for the maximum aperiodic inclusion-maximal sum-free set. Completes the picture: $\mathrm{sf}_1(\mathbb{F}_p^n)$ now known for all primes $p$ ($p=2$: Davydov–Tombak; $p=3$: Lev; $p\geq 7$: prior; $p=5$: this paper).

## Why it matters here
General background — no direct arena tie. Relevant adjacent to extremal combinatorics / additive combinatorics problems if any future arena problem involves sum-free or cap-set type structures in $\mathbb{F}_p^n$; demonstrates a clean "density projection + Kneser + case analysis" template that mirrors LP-bound + structural classification patterns used elsewhere in this wiki.

## Open questions / connections
- Extend $\mathrm{sf}_1(G)$ classification beyond elementary abelian groups to broader finite abelian groups.
- $\mathrm{sf}_k(\mathbb{F}_5^n)$ for $k \geq 2$ — paper notes $\Lambda \cup (\Lambda+\Lambda) \cup (\Lambda-\Lambda) = \mathbb{F}_5^3$ suggests the hierarchy is non-trivial here.
- Determine $t(\mathbb{F}_5^n)$ (max aperiodic inclusion-maximal sum-free set) for $n \geq 4$ — currently open.
- Extends Davydov–Tombak ($p=2$), Lev ($p=3$, ternary), Versteegen (upper bounds $6 \cdot 5^{n-2}$); part II of Reiher–Zotova series (Part I is arXiv:2408.11232).

## Key terms
sum-free sets, finite vector spaces, $\mathbb{F}_5^n$, Kneser's theorem, symmetry set, sumset, normal sum-free set, VL-set, Lev-Versteegen configuration, fishy function, additive combinatorics, extremal combinatorics, Schur, Reiher, Zotova, Versteegen
