---
type: source
kind: paper
title: Equiangular lines and spherical codes in Euclidean space
authors: Igor Balla, Felix Dräxler, Peter Keevash, B. Sudakov
year: 2016
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1606.06620
source_local: ../raw/2016-balla-equiangular-lines-spherical-codes.pdf
topic: general-knowledge
cites:
---

# Equiangular lines and spherical codes in Euclidean space

**Authors:** Igor Balla, Felix Dräxler, Peter Keevash, B. Sudakov  ·  **Year:** 2016  ·  **Source:** https://arxiv.org/abs/1606.06620

## One-line
Resolves the Lemmens–Seidel problem: for every fixed angle $\arccos\alpha$ and sufficiently large $n$, the maximum number of equiangular lines in $\mathbb{R}^n$ is $2n-2$, attained iff $\alpha=1/3$.

## Key claim
For fixed $\alpha\in(0,1)$ and $n$ large, $N_\alpha(n)\le 2n-2$ with equality iff $\alpha=1/3$; otherwise $N_\alpha(n)\le 1.93n$. For any fixed $k$ angles and fixed $\beta\in(0,1]$, any $[-1,-\beta]\cup\{\alpha_1,\dots,\alpha_k\}$-spherical code in $\mathbb{R}^n$ has size $\le c_{\beta,k}n^k$ (proving Bukh's conjecture, improving Delsarte–Goethals–Seidel's $O(n^{2k})$ to $O(n^k)$), with explicit constant $2^k(k-1)!(1+\alpha_1/\beta)$.

## Method
Ramsey's theorem extracts a large positive $\alpha$-clique $Y$ inside the $\{-\alpha,\alpha\}$-code's edge-labeled graph $G_C$; vertex-negation symmetry is used to force most remaining vertices to attach to $Y$ entirely via positive edges. Orthogonal projection onto $\mathrm{span}(Y)^\perp$ converts the problem into bounding an $L(\alpha,t)$-code with controlled angles, then a rank inequality $\mathrm{rk}(M)\ge\mathrm{tr}(M)^2/\mathrm{tr}(M^2)$ (Bellman/Schnirelman) applied to the shifted Gram matrix $M_C-\epsilon J$ closes the bound. The multi-angle case uses iterated projection plus a monochromatic-pair Ramsey lemma and induction on $k$.

## Result
$N_{1/3}(n)=2n-2$ exactly for large $n$, realized by $n-1$ block-diagonal $2\times 2$ Gram blocks $\begin{pmatrix}1&-1/3\\-1/3&1\end{pmatrix}$ with off-block entries $1/3$. For other fixed $\alpha$, $N_\alpha(n)\le 1.93n$. Lower-bound construction shows the $n^k$ rate is tight: a $[-1,-\beta]\cup\{\alpha_1,\dots,\alpha_k\}$-code of size $(1+r)\binom{n}{k}$ exists in $\mathbb{R}^{n+r}$ with $\beta=\alpha_1/r-O(\sqrt{\log n/n})$, refuting Bukh's linear conjecture for $[-1,0)\cup\{\alpha\}$-codes when $\beta\to 0$.

## Why it matters here
Direct relevance to **kissing-number / spherical-code** Einstein problems and any arena task involving Gram-matrix-rank arguments on $\{\pm\alpha\}$-coded line sets; the Schnirelman rank inequality $\mathrm{rk}(M)\ge\mathrm{tr}(M)^2/\mathrm{tr}(M^2)$ is a reusable tool for any combinatorial-geometry bound argument. Adds a sharp "$\alpha=1/3$ extremal" finding and the projection-onto-clique reduction technique not yet captured in the wiki.

## Open questions / connections
- Conjecture 6.1: $N_{1/(2r-1)}(n)=r\lfloor(n-1)/(r-1)\rfloor+O(1)$ for every integer $r\ge 2$ — confirmed for $r=2$ (Lemmens–Seidel) and $r=3$ (Neumaier); open for $r\ge 4$.
- When $\alpha=\alpha(n)\to 0$ faster than $\Theta(\log^{-1}n)$, Ramsey-clique extraction breaks; methods may still extend if a large positive clique exists by other means.
- Is Delsarte–Goethals–Seidel's $O(n^{2k})$ for $k\ge 2$ tight when angles are allowed to shrink with $n$? No matching constructions known for $k\ge 2$.
- Connects to Gerzon's $\binom{n+1}{2}$ absolute bound (saturated only at $n\in\{2,3,7,23\}$) and to de Caen's $2(n+1)^2/9$ construction with vanishing $\alpha$.

## Key terms
equiangular lines, spherical codes, Lemmens–Seidel problem, Gerzon bound, Bukh conjecture, Delsarte–Goethals–Seidel, Gram matrix rank inequality, Ramsey monochromatic pair, orthogonal projection clique, Neumann odd-integer theorem, $L$-code, $\arccos(1/3)$ extremal, polynomial method
