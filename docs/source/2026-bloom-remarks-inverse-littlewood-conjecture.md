---
type: source
kind: paper
title: Remarks on the inverse Littlewood conjecture
authors: Thomas F. Bloom, Ben Green
year: 2026
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2602.16482v2
source_local: ../raw/2026-bloom-remarks-inverse-littlewood-conjecture.pdf
topic: general-knowledge
cites: 
---

# Remarks on the inverse Littlewood conjecture

**Authors:** Thomas F. Bloom, Ben Green  ·  **Year:** 2026  ·  **Source:** http://arxiv.org/abs/2602.16482v2

## One-line
Sets of $N$ integers with small Fourier $L^1$-norm $\|\widehat{1_A}\|_1 \le K \log N$ must contain a large nearly-full-density subset with constant additive energy, forcing long arithmetic progressions.

## Key claim
If $A \subset \mathbb{Z}$ has $|A| = N$ and $\|\widehat{1_A}\|_1 \le K \log N$, then for any $\delta \in (0, 1/2]$ there is an initial segment $A' \subseteq A$ with $|A'| \gg N^{1-\delta}$ and normalised additive energy $\omega[A'] \gg (\delta/K)^2$ — yielding $|A'+A'| \ll K^{O(1)} |A'|$ on a subset of size $\ge N^{0.99}$, and an arithmetic progression of any length $k$ for $N$ large. Bonus: the Littlewood constant is improved to $c = 0.170934\ldots$ (previous best Yabuta $\approx 0.1295$; conjectured optimum $4/\pi^2 \approx 0.405$).

## Method
Inverse analysis of the McGehee–Pigno–Smith test function $R$ built iteratively from nested initial segments $A_1 \subseteq \cdots \subseteq A_J$ of $A$ with geometric growth $|A_{j+1}| \ge \lambda |A_j|$. The lower bound $\|\widehat{1_A}\|_1 \ge (1-e^{-b}) J - b(\lambda^{1/2}-1)^{-1} \sum_i (\omega[A_i] + |A_i|^{-1})^{1/2}$ (Proposition 3.1) forces one of the $\omega[A_i]$ to be large when $\|\widehat{1_A}\|_1$ is small. Improved Littlewood constant uses a Gabriel-style rearrangement inequality giving $\omega[A_i] \le 2/3 + o(1)$ for initial segments, then optimises over $b \approx 0.932$, $\lambda \approx 9.112$.

## Result
- **Theorem 1.2:** $|A'| \gg N^{1-\delta}$, $\omega[A'] \gg (\delta/K)^2$, $A'$ an initial segment of $A$.
- **Corollary 1.3 (Balog–Szemerédi–Gowers + Freiman–Ruzsa):** $A$ has positive density $\gg_K 1$ on an AP of length $\ge N^{c_K}$.
- **Corollary 1.4:** APs of every length $k \ge 3$ exist in $A$ for $N$ large depending on $K, k$ (via Szemerédi).
- **Theorem 1.5:** $\|\widehat{1_A}\|_1 \ge (0.170934\ldots - o(1)) \log N$.

## Why it matters here
General background; no direct arena tie. Closest relevance is conceptual cross-pollination — additive energy lower bounds from a Fourier $L^1$ assumption use the same dual machinery (test-function construction, Parseval, Cauchy–Schwarz on convolution tails) that recurs in autocorrelation / uncertainty-style problems, and the rearrangement inequality $\omega \le 2/3$ for monotone integer sets is a clean reusable lemma.

## Open questions / connections
- **Conjecture 6.1 (Petridis-style):** $1_A$ decomposes as $\sum \pm 1_{P_i} + \sum \pm 1_{X_j}$ with $O_K(1)$ APs and a small unstructured remainder — analogue of Green–Sanders idempotent theorem for $\mathbb{Z}$.
- **Conjecture 6.2:** $\dim A \ll_K (\log N)^2$ under the same hypothesis (Pichorides has $(\log N)^3$; Bedert independently rediscovered the Zygmund bound); and a subset of size $\gg_K N$ with $\dim \ll_K \log N$.
- Strong Littlewood: gap from $0.171$ to the conjectured $4/\pi^2 \approx 0.405$ remains a factor of $\sim 2.4$.
- Connection to Bourgain's sum-free subset problem (Bedert 2025 made progress via this route).

## Key terms
Littlewood conjecture, inverse Littlewood, Fourier $L^1$ norm, additive energy, McGehee–Pigno–Smith test function, Balog–Szemerédi–Gowers, Freiman–Ruzsa, Szemerédi's theorem, dissociated set, idempotent theorem, rearrangement inequality, Bloom, Green, Petridis, Bedert
