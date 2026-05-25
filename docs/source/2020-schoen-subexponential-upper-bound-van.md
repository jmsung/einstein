---
type: source
kind: paper
title: A subexponential upper bound for van der Waerden numbers W(3,k)
authors: Tomasz Schoen
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2006.02877v1
source_local: ../raw/2020-schoen-subexponential-upper-bound-van.pdf
topic: general-knowledge
cites: 
---

# A subexponential upper bound for van der Waerden numbers W(3,k)

**Authors:** Tomasz Schoen  ·  **Year:** 2020  ·  **Source:** http://arxiv.org/abs/2006.02877v1

## One-line
Proves $W(3,k) \le \exp(O(k^{1-c}))$ for some absolute $c>0$, breaking the exponential barrier for the off-diagonal van der Waerden number.

## Key claim
There exist absolute constants $C, c > 0$ such that $W(3,k) \le \exp(C k^{1-c})$, improving the previous $\exp(O(k \log k))$ bound of Cwalina–Schoen and giving the first genuinely subexponential upper estimate.

## Method
Fourier-analytic density-increment on $\mathbb{Z}/N\mathbb{Z}$ via Bohr sets, combined with Chang's spectral lemma, Bateman–Katz large-spectrum structure (imported through Lemma 5 of Schoen's Roth-theorem paper arXiv:2005.01145), Bloom's iterative density-increment lemma, and Sanders' lemma extracting long APs from dense subsets of regular Bohr sets. Case-splits on whether the third-moment spectral mass concentrates in $\Delta_{\delta^{1/10}}$: one branch gives a 3-AP in $X$ contradicting progression-freeness, the other gives a long AP inside $Y$ via Bohr-set smoothing.

## Result
Theorem 1: $W(3,k) \le \exp(C k^{1-c})$. The proof produces $\Omega(\delta^{3+c/6} N^2)$ three-term APs in any putative progression-free $X \subseteq \{1,\dots,N\}$ of density $\delta = |X|/N \gtrsim 1/k$, forcing $N \le \exp(O(k^{1-c} \log^4 k))$. Prior best upper bound was $\exp(O(k \log k))$; lower bound remains $W(3,k) \gtrsim (k/\log k)^2$ (Li–Shu).

## Why it matters here
Off-diagonal Ramsey/van der Waerden bounds and the structure-of-the-large-spectrum machinery are background context for any extremal-combinatorics arena problem touching APs, Sidon sets, or sumset/spectrum methods. General background; no direct arena tie to the current 23 problems, but Bohr-set + spectrum techniques may feed extremal-graph or autocorrelation findings.

## Open questions / connections
- What is the optimal $c$? The proof gives a small explicit $c$ tied to Bateman–Katz; closing the gap to the Behrend-style lower bound $(k/\log k)^2$ remains wide open.
- Does the same density-increment scheme extend to $W(4,k)$ or higher off-diagonal cases, or does Gowers-uniformity obstruct it?
- Direct dependency on Schoen's companion Roth-theorem paper (arXiv:2005.01145) — improvements to Roth bound $r(N) \ll N/\log^{1+c} N$ would propagate here.

## Key terms
van der Waerden numbers, W(3,k), Roth's theorem, arithmetic progressions, Bohr sets, Chang's spectral lemma, large spectrum, Bateman-Katz, density increment, Fourier analysis on Z/NZ, Schoen, Bloom, Sanders, subexponential bound, additive combinatorics
