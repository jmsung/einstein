---
type: source
kind: paper
title: Length of the Longest Common Subsequence between Overlapping Words
authors: B. Bukh, Raymond Hogenson
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1803.03238
source_local: ../raw/2018-bukh-length-longest-common-subsequence.pdf
topic: general-knowledge
cites:
---

# Length of the Longest Common Subsequence between Overlapping Words

**Authors:** B. Bukh, Raymond Hogenson  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1803.03238

## One-line
Tail bounds for the length of the longest common subsequence (LCS) between two random $[k]^n$ words that share a length-$\alpha n$ overlap (one's prefix equals the other's suffix).

## Method
Geometric edge-crossing model for LCS (noncrossing edges between aligned positions), partitioned by the minimum-span edge of the LCS into cases (negative span, $0<\text{span}\le \varepsilon n$, span $>\varepsilon n$). Concentration via Azuma (Lipschitz LCS), Hoeffding for block sums, and a custom MGF tail bound on sums of exponentials (Lemma 4) — applied through a coupling that generates $Z$ by interleaving two i.i.d. streams $R,S\sim[k]^\infty$ so subsequence-containment events become geometric-sum tail events.

## Result
Let $\text{SHIFT}(n,k,\alpha n) := \mathrm{LCS}(Z[0,n), Z[\alpha n, n+\alpha n))$ with $Z\sim[k]^{n+\alpha n}$, and $\gamma_k := \lim E[L_n]/n$ for independent LCS. There exists $c_k>0$ such that for $n$ large:
- **Upper tail (Thm 1):** for $t\ge 6\sqrt{n}$, $\Pr[\text{SHIFT}\ge \max(n-\alpha n+1,\, \gamma_k n + t)] \le \exp(-c_k t^2/n)$.
- **Lower tail (Thm 2):** for $t\ge 5 n^{3/4}\sqrt{\log n}$, $\Pr[\text{SHIFT}\le \gamma_k n - t] \le \exp(-c_k t^2/n^{3/4})$.

Together: $E[\text{SHIFT}] \approx \max(\alpha n,\, E[L_n])$, i.e., the overlap is a useful lower bound only when $\alpha n \gtrsim \gamma_k n$.

## Why it matters here
General background; no direct arena tie. Closest tangent is methodology — coupling tricks to convert subsequence containment into geometric-sum tail events, plus the "partition by extremal-edge span" decomposition, which are reusable patterns for combinatorial concentration arguments.

## Open questions / connections
- Conjecture $\text{SHIFT}(n,k,\alpha n) = \max(n-\alpha n, E[L_n]) + O(\sqrt{n})$ w.h.p. — the $n^{3/4}\sqrt{\log n}$ lower-tail threshold is likely loose.
- Extends Chvátal–Sankoff (1975) and Alexander (1994) $\gamma_k n - 4\sqrt{n\log n}$ convergence rate; uses Kiwi–Loebl–Matoušek (2005) $\gamma_k\sqrt{k}\to 2$ and Lueker (2009) numerical bounds on $\gamma_k$.
- Motivated by DNA-sequencing overlap detection — whether shared-region similarity exceeds chance.

## Key terms
longest common subsequence, LCS, Chvátal–Sankoff constant, $\gamma_k$, random words, overlapping sequences, Azuma's inequality, Hoeffding's inequality, concentration inequalities, subadditive sequences, Bukh, DNA sequence alignment, geometric noncrossing-edges model
