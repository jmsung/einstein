---
type: source
kind: paper
title: On Saturated k-Sperner Systems
authors: Natasha Morrison, Jonathan A. Noel, A. Scott
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1402.5646
source_local: ../raw/2014-morrison-saturated-k-sperner-systems.pdf
topic: general-knowledge
cites:
---

# On Saturated k-Sperner Systems

**Authors:** Natasha Morrison, Jonathan A. Noel, A. Scott  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1402.5646

## One-line
Disproves the Gerbner et al. conjecture that the minimum saturated $k$-Sperner system has size exactly $2^{k-1}$, and pins down the asymptotic order of the oversaturated variant.

## Key claim
There exists $\varepsilon > 0$ (concretely $\varepsilon \approx 1 - \log_2(15)/4 \approx 0.0233$) such that $\mathrm{sat}(k) \le 2^{(1-\varepsilon)k}$ for all $k$, with $k=6$ the first counterexample to the conjecture ($\mathrm{sat}(6) \le 30 < 32 = 2^5$). For oversaturated systems, $\mathrm{osat}(k) = 2^{(1/2+o(1))k}$.

## Method
Structural decomposition: any saturated $k$-Sperner system with a homogeneous set splits into a layered sequence of $k$ pairwise-disjoint saturated antichains (canonical decomposition; Lemmas 14–17). A combination lemma (Lemma 18) glues a saturated $k_1$-system on $X_1$ with a saturated $k_2$-system on $X_2$ into a saturated $(k_1+k_2-2)$-system of size $|\mathcal{F}_1^{\text{small}}||\mathcal{F}_2^{\text{small}}| + |\mathcal{F}_1^{\text{large}}||\mathcal{F}_2^{\text{large}}|$, yielding submultiplicativity and (via Fekete's lemma) convergence of $\mathrm{sat}(k)^{1/k}$. The oversaturated upper bound is probabilistic: random collections of $\sim 2^{k/2}$ sets of cardinality $ak$ and $(1-a)k$ with first-moment union bounds.

## Result
$\mathrm{sat}(k) \le 2^{(1-\varepsilon)k}$ with $\varepsilon \approx 0.0233$; explicit base case $\mathrm{sat}(6) \le 30$ via a construction with $|\mathcal{A}_i^{\text{small}}| = 1,5,9,0$ across layers. $\mathrm{sat}(k) = 2^{(1+o(1))ck}$ for some $c \in [1/2, 1-\varepsilon]$ (exact $c$ left open). $\mathrm{osat}(k) = O(k^5 2^{k/2})$, matching the $2^{k/2-1}$ lower bound up to a polynomial factor. For $k \le 5$, $\mathrm{sat}(k) = 2^{k-1}$ exactly (Proposition 21).

## Why it matters here
General background; no direct arena tie — this is extremal set theory (Sperner / chain saturation) rather than packing, autocorrelation, or kissing. Methodologically, the canonical-antichain decomposition + submultiplicativity-via-Fekete pattern is a transferable template for any extremal problem with "combine two small structures into one larger" lemmas.

## Open questions / connections
- Problem 5: determine the exact constant $c$ in $\mathrm{sat}(k) = 2^{(1+o(1))ck}$; current sandwich $1/2 \le c \le 1 - \varepsilon$.
- Lower-bound improvement strategy: show every saturated antichain with homogeneous set and element sizes in $[k/2, n-k/2+1]$ has $\ge 2^{(1+o(1))ck}$ elements for some $c > 1/2$.
- Extends Sperner (1928) and Erdős (1945); parallels minimum-saturation literature for graphs (Erdős–Hajnal–Moon, Zykov) and hypergraphs (Pikhurko).

## Key terms
saturated k-Sperner system, oversaturated k-Sperner system, antichain, Sperner's theorem, chain saturation, homogeneous set, canonical decomposition, layered antichain sequence, Fekete's lemma, submultiplicativity, probabilistic construction, extremal set theory
