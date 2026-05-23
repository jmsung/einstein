---
type: source
kind: paper
title: Tetrahedral colloidal clusters from random parking of bidisperse spheres.
authors: N. Schade, Miranda C. Holmes-Cerfon, E. R. Chen, D. Aronzon, J. Collins, Jonathan A. Fan, F. Capasso, V. Manoharan
year: 2012
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1201.3952
source_local: ../raw/2012-schade-tetrahedral-colloidal-clusters-random.pdf
topic: general-knowledge
cites:
---

# Tetrahedral colloidal clusters from random parking of bidisperse spheres.

**Authors:** N. Schade, Miranda C. Holmes-Cerfon, E. R. Chen, D. Aronzon, J. Collins, Jonathan A. Fan, F. Capasso, V. Manoharan  ·  **Year:** 2012  ·  **Source:** https://arxiv.org/abs/1201.3952

## One-line
Irreversible random "parking" of large spheres on a smaller central sphere yields ~90% tetrahedral clusters at a critical size ratio $\alpha_c = 1+\sqrt{2}$, where minimum-parking lower bound meets the packing upper bound.

## Key claim
At size ratio $\alpha = R_{\text{big}}/R_{\text{small}} = 1+\sqrt{2} \approx 2.41$, the random-parking process is geometrically forced to produce exactly $N=4$ (tetrahedral) clusters with theoretical 100% yield — the unique nontrivial point where $N_{\min}(\alpha) = N_{\max}(\alpha) = 4$.

## Method
Three-track approach: (1) experiments with oppositely-charged polystyrene colloids and DNA-functionalized colloids in 100:1 stoichiometric ratio; (2) Monte Carlo "random parking" simulation that sticks discs of radius $r=R_{\text{big}}/(R_{\text{big}}+R_{\text{small}})$ uniformly on the unit sphere subject to no-overlap, with coarse + fine insertion stages; (3) analytical bounds — $N_{\max}(\alpha)$ from spherical packing solutions (Sloane–Hardin–Smith tables), and a new $N_{\min}(\alpha)$ bound derived from spherical covering solutions, verified to coincide with optimal parking for $n=4,\ldots,130$ by checking covering radius $<$ 2× packing radius.

## Result
The critical ratio $\alpha_c = 1+\sqrt{2}$ is the unique nontrivial point where $N_{\max}$ (drops $6\to 4$) and $N_{\min}$ (drops $4\to 2$) curves meet, forcing deterministic tetramer yield. Experimentally at $\alpha=2.45$: 90.2% tetramers; simulations at $\alpha\approx 2.41$ reach 100%. Octahedral yield maximum is ~70% at $\alpha=1.42$; only $N=2$ and $N=4$ yields can approach 100%. Verification table gives packing/covering radii for $n=2$–$130$.

## Why it matters here
Direct relevance to **spherical codes / spherical covering / spherical packing** family (Problems P1–P3 territory) — establishes the rare coincidence-point between covering and packing optima at $N=4$ on $S^2$ with $\alpha_c=1+\sqrt{2}$, and uses the Sloane spherical-codes tables [ref 27] as ground truth. Adds a "minimum parking" / dual covering bound framing that complements packing-only thinking, plus a numerical table of packing vs covering radii for $n\le 130$ usable as a verifier cross-check.

## Open questions / connections
- Does the covering-radius < 2×(packing-radius) condition hold for $n > 130$? (verified manually only through 130)
- Generalizations to non-spherical central particles, or to higher-dimensional analogs of the $\alpha_c$ coincidence point.
- Connection to jamming thresholds and coordination-number distributions in bidisperse bulk packings [refs 25, 28].
- Cross-pollination: the "minimum parking number" concept (smallest saturated configuration) is a covering dual seldom invoked alongside packing — potentially useful in extremal-geometry problems with irreversibility/online structure.

## Key terms
spherical covering, spherical packing, spherical codes, random parking, bidisperse spheres, minimum parking number, critical size ratio, $1+\sqrt{2}$, tetrahedral cluster, covering radius, packing radius, Sloane spherical codes, irreversible aggregation, colloidal self-assembly, Conway-Sloane
