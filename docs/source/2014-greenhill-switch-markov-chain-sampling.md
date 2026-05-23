---
type: source
kind: paper
title: The switch Markov chain for sampling irregular graphs (Extended Abstract)
authors: Catherine S. Greenhill
year: 2014
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1412.5249
source_local: ../raw/2014-greenhill-switch-markov-chain-sampling.pdf
topic: general-knowledge
cites:
---

# The switch Markov chain for sampling irregular graphs (Extended Abstract)

**Authors:** Catherine S. Greenhill  ·  **Year:** 2014  ·  **Source:** https://arxiv.org/abs/1412.5249

## One-line
Proves the switch Markov chain mixes rapidly when sampling simple graphs with a given (possibly irregular) degree sequence, under a mild density bound on the maximum degree.

## Key claim
For any graphical degree sequence $d$ with $d_{\min} \geq 1$ and $3 \leq d_{\max} \leq \tfrac{1}{4}\sqrt{M}$ (where $M = \sum_j d_j$), the switch chain on $\Omega(d)$ has mixing time $\tau(\varepsilon) \leq 10 \, d_{\max}^{14} M^9 \bigl(M \log M + \log \varepsilon^{-1}\bigr)$ — only a factor of $n$ worse than the regular case.

## Method
Multicommodity flow argument (Sinclair) re-using the canonical-path construction of Cooper–Dyer–Greenhill, since the flow definition depends only on the 2-edge-coloured symmetric difference $G \triangle G'$ and is already insensitive to regularity. The critical "encoding" counting lemma is re-proved without regularity by introducing a *3-switch* (circular $C_6$-swap) operation and running a three-phase switching argument: Phase 1 removes a $(2,-1)$-defect pair, Phase 2 removes 2-defects, Phase 3 removes $(-1)$-defects, each yielding a double-counting ratio bound $|C(p,q)|/|C(p',q')|$.

## Result
Establishes $|\mathcal{L}^*(Z)|/|\Omega(d)| \leq 15 M^6$ (Lemma 3.4), combined with the standard bound $f(e) \leq d_{\max}^{14} |\mathcal{L}^*(Z)|/|\Omega(d)|$ (Lemma 3.3), the path length $\ell(f) \leq M/2$, and $\log(1/\pi_*) \leq M \log M$ from the configuration-model count. Covers regimes including sparse graphs with $d_{\max} = O(\sqrt{n})$ and dense graphs with $d_{\max} = \Theta(n)$ provided $d_{\max} \leq \tfrac{1}{4}\sqrt{M}$.

## Why it matters here
General background; no direct arena tie. Potentially relevant if extremal-graph or contact-graph problems ever need uniform sampling of graphs with prescribed degrees (e.g., as a randomized search prior over kissing-graph structures), but not load-bearing for any current Einstein problem.

## Open questions / connections
- Extension of the same technique to irregular directed degree sequences (parallel to Greenhill 2011).
- Closing the gap between $d_{\max} \leq \tfrac{1}{4}\sqrt{M}$ and the full graphical regime; can the $\sqrt{M}$ ceiling be removed?
- Clarify connections between *stable* (Jerrum–Sinclair–McKay), *tame* (Barvinok–Hartigan), and switch-rapidly-mixing degree sequences.

## Key terms
switch Markov chain, rapid mixing, multicommodity flow, degree sequence, irregular graphs, Sinclair canonical paths, 3-switch, circular C6-swap, configuration model, switching argument, Cooper-Dyer-Greenhill, Greenhill
