---
type: source
kind: paper
title: The L^1-norm of exponential sums in Z^d
authors: G. Petridis
year: 2011
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1110.2014
source_local: ../raw/2011-petridis-1-norm-exponential-sums.pdf
topic: general-knowledge
cites:
---

# The L^1-norm of exponential sums in Z^d

**Authors:** G. Petridis  ·  **Year:** 2011  ·  **Source:** https://arxiv.org/abs/1110.2014

## One-line
Lower bounds on $\|F_A\|_1 = \int_{\mathbb{T}^d} |\sum_{a\in A} e(a\cdot x)| dx$ when $A \subset \mathbb{Z}^d$ has genuine multidimensional structure, beating the classical $\log|A|$ bound by extra log factors.

## Key claim
If $A \subset \mathbb{Z}^2$ has $\geq r$ rows of size $\geq s$, then $\|F_A\|_1 \geq c \log s \cdot (\log r / \log\log r)^{1/2}$ (Thm 1.2). If $B \subset \mathbb{Z}$ is Freiman-isomorphic of degree $k = 62 \log r \log s \log p$ to a genuinely 3D set in $\mathbb{Z}^3$ with $p$ planar slices × $r$ rows × $s$ size, then $\|F_B\|_1 \geq c (\log s \log r \log p / \log\log s \log\log r \log\log p)^{1/2}$ — i.e. $\geq \log^{3/2-\varepsilon}|B|$ (Thm 1.3).

## Method
Hybrid combination of the McGehee–Pigno–Smith test-function construction (used in one dimension to seed row-level functions $\Phi_{n_i}$) with the Cohen–Davenport–Pichorides iteration (used to combine them via $g_{i+1} = g_i(1 - 1/t) - g_i \cdot \frac{1}{t^2}\sum \Phi_{m_i}\overline{\Phi_{m_j}} + \frac{1}{4t^{3/2}}|\sum \Phi_{m_i}|$, choosing $t \approx \log R / \log\log R$ iterations). Central tool is Lemma 2.1: from functions $\Phi_{n_i}$ satisfying $\|\Phi_{n_i}\|_\infty \leq 1$, $\langle \Phi_{n_i}, F\rangle \geq K$, and a sumset support condition (C), one constructs $g$ with $\|g\|_\infty \leq 1$ and $\langle g, F\rangle \geq cK(\log R/\log\log R)^{1/2}$. Freiman isomorphism of sufficient degree $k$ preserves the support condition (C) when transferring from $\mathbb{Z}^3$ to $\mathbb{Z}$.

## Result
Establishes partial progress on Gowers' question of whether $\|F_A\|_1 \geq c \log r \log s$ for genuinely 2D sets — Petridis only proves $\log s \cdot \log^{1/2-\varepsilon} r$. For Freiman-isomorphic copies of 3D structured sets in $\mathbb{Z}$, exponential sums are forced strictly above the Littlewood floor $\log|A|$, ruling out such multidimensional structure for any $A \subset \mathbb{Z}$ with $\|F_A\|_1 \leq C\log|A|$. Section 5 shows the dimensionality notion is too restrictive to fully characterize near-minimal $\|F_A\|_1$: lacunary sequences and a dense mod-$p$ construction both have $\|F_A\|_1$ near minimal yet fail to decompose into few APs.

## Why it matters here
General background; no direct arena tie. Relevant as deep technique on $L^1$ exponential-sum lower bounds, which connects tangentially to autocorrelation inequalities and Fourier-analytic approaches used in problems involving $\hat{1}_A$ on $\mathbb{T}$ — could inform constructions where one wants to lower-bound $\|F_A\|_1$ or upper-bound $\|F_A\|_\infty$ for structured $A$.

## Open questions / connections
- Is Gowers' stronger bound $\|F_A\|_1 \geq c \log r \log s$ for 2D sets achievable? Petridis loses a $(\log\log r)^{1/2}$ factor and a square root.
- Question 5.1 (Green): does $\|F_A\|_1 \leq K\log|A|$ force $F_A = F_X + \sum_{i=1}^{g(K)} \pm F_{P_i}$ with $|X| \leq \exp(\|F_A\|_1^\eta)$ and $P_i$ APs, for some $1/2 \leq \eta < 1$?
- Can the Freiman-isomorphism degree $k = 62\log r\log s\log p$ in Thm 1.3 be reduced? Can a $\log^{1+\eta}|A|$ bound be shown for sets Freiman-isomorphic to 2D structure?

## Key terms
Littlewood conjecture, L1-norm exponential sums, McGehee-Pigno-Smith, Konyagin, Cohen-Davenport-Pichorides, Freiman isomorphism, multidimensional arithmetic progression, idempotent measures, Green-Sanders, Petridis, lacunary sequence, Dirichlet kernel
