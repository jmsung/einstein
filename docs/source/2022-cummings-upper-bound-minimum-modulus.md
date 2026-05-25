---
type: source
kind: paper
title: An upper bound for the minimum modulus in a covering system with squarefree moduli
authors: Maria Cummings, M. Filaseta, O. Trifonov
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2211.08548
source_local: ../raw/2022-cummings-upper-bound-minimum-modulus.pdf
topic: general-knowledge
cites:
---

# An upper bound for the minimum modulus in a covering system with squarefree moduli

**Authors:** Maria Cummings, M. Filaseta, O. Trifonov  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2211.08548

## One-line
Refines the Balister–Bollobás–Morris–Sahasrabudhe–Tiba (BBMST) distortion method to prove that any covering system with distinct squarefree moduli has minimum modulus $\le 118$.

## Key claim
**Theorem 1.1:** Every covering system with distinct squarefree moduli has minimum modulus $\le 118$ (down from the BBMST bound of roughly $\exp(10^{200})$). **Theorem 1.2:** For each fixed $k\ge 0$, the $(k{+}1)$-st smallest modulus in any covering system with distinct moduli (where the first $k$ congruences don't already cover) is bounded by an absolute constant $B(k+1)$.

## Method
Recasts congruences with squarefree moduli as hyperplanes in $Q=S_1\times\cdots\times S_n$ with $S_j=\{1,\dots,p_j\}$, then assigns inductive **weights** $w_k$ on fibers tuned by parameters $\delta_k\in[0,1/2]$ (a weighted-sum reformulation of the BBMST probabilistic distortion). The key inequality $\alpha_k(x)^2/(4\delta_k)\ge \alpha_k(x)-\delta_k$ converts fiber-coverage proportions into a bound $w_k(B_k)\le E_{k-1}/(4\delta_k(1-\delta_k))$; choosing $\delta_j$ stagewise (e.g. $\delta_8\!\approx\!0.171,\ldots,\delta_{\ge 10^6}=1/2$) and tail-bounding via Rosser–Schoenfeld prime estimates yields $\sum_k w_k(B_k)<1$, forcing non-coverage. Theorem 1.2 follows by an inductive contradiction: glue $m_1m_2\cdots m_k$ independent coverings together to violate Hough's $k=0$ bound.

## Result
Minimum-modulus bound dropped from $\exp(10^{200})$ to **118** for distinct-squarefree-moduli coverings — leaving a wide gap to Selfridge's 1981 conjecture (no such covering with minimum modulus $>2$ is known; the canonical example uses moduli $\{2,3,5,6,7,10,14,15,21,30,35,42,70,105\}$, $\mathrm{lcm}=210$). Numerically: $\sum_{k=1}^{7} w_k(B_k)\le 194/1365$, $\sum_{k=8}^{10^6} w_k(B_k)\le 0.857$, tail $\sum_{k>10^6}\le 4.0\times 10^{-4}$, total $<0.9994$. Theorem 1.2 establishes existence of $B(k+1)$ but gives no explicit value.

## Why it matters here
General background; no direct arena tie. Covering systems / squarefree moduli are not among the 23 Einstein Arena problems, but the **weighted-fiber distortion method** (assigning $\delta_k$-tuned weights so a sum stays $<1$ and contradicts coverage) is a transferable technique: it is the LP/probabilistic-method dual of the "find weights so that $\sum w_k\cdot(\text{coverage indicator})<1$" pattern used in $LP$-bound proofs (Cohn–Elkies, Delsarte LP for kissing numbers) and could inform any arena problem reframed as "no finite family of structured sets covers $Q$."

## Open questions / connections
- Explicit value of $B(k)$ for $k\ge 2$ — Theorem 1.2's proof is constructive but the authors make no attempt at optimization.
- How close to Selfridge's conjectured bound of $2$ can this refinement push? The gap 2 → 118 is still enormous.
- Extends Hough 2015 ($\le 10^{16}$) and BBMST 2022 ($\le 615999$ general / $\exp(10^{200})$ squarefree); compresses the squarefree case dramatically while leaving the general squarefree LCM-of-4-primes classification (Kruckenberg) untouched.

## Key terms
covering system, minimum modulus problem, squarefree moduli, Erdős covering, Selfridge problem, Hough, Balister-Bollobás-Morris-Sahasrabudhe-Tiba, distortion method, weighted fiber bound, hyperplane covering, Rosser-Schoenfeld prime estimates, Chinese Remainder Theorem
