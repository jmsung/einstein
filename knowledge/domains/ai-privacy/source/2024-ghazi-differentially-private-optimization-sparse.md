---
type: source
kind: paper
title: Differentially Private Optimization with Sparse Gradients
authors: Badih Ghazi, Cristóbal Guzmán, Pritish Kamath, Ravi Kumar, Pasin Manurangsi
year: 2024
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2404.10881v2
source_local: ../raw/2024-ghazi-differentially-private-optimization-sparse.pdf
topic: general-knowledge
cites: 
---

# Differentially Private Optimization with Sparse Gradients

**Authors:** Badih Ghazi, Cristóbal Guzmán, Pritish Kamath, Ravi Kumar, Pasin Manurangsi  ·  **Year:** 2024  ·  **Source:** http://arxiv.org/abs/2404.10881v2

## One-line
Near-optimal differentially private (DP) optimization rates when each individual gradient has at most $s$ nonzero entries, achieving nearly dimension-independent error in high dimensions.

## Key claim
Under per-example gradient sparsity $\|\nabla f(x,z)\|_0 \le s$, DP mean estimation and DP-SCO admit rates that scale poly-logarithmically in $d$ — e.g., approximate-DP mean estimation error $\lesssim 1 \wedge \frac{(s\log(d/s)\log(1/\delta))^{1/4}}{\sqrt{\varepsilon n}} \wedge \frac{\sqrt{d\log(1/\delta)}}{\varepsilon n}$, with matching lower bounds up to a $\log(d/s)^{1/4}$ gap.

## Method
Projection mechanism with convex relaxation $K = B_1^d(0, L\sqrt{s})$ for $\ell_2$-mean estimation; an $\ell_1$-regression refinement combining compressed-sensing ideas (Wojtaszczyk) with Approximate Carathéodory (Pisier–Maurey) for sharper approximate-DP rates. For ERM/SCO: biased SGD with telescopic bias-reduction (random exponential batch schedule, à la Blanchet–Glynn) + randomly-stopped SGD under fully-adaptive DP composition (Whitehouse et al.), plus regularized output perturbation with $\ell_\infty$-projection post-processing. Lower bounds: novel block-diagonal bootstrapping of sparse packings / fingerprinting codes.

## Result
Pure-DP mean estimation: $\tilde O\!\left(1 \wedge \frac{s\ln d}{\varepsilon n} \wedge \frac{\sqrt{sd}}{\varepsilon n}\right)$ upper bound, with matching $\Omega(s\log(d/s)/(n\varepsilon))$ lower bound after block bootstrapping. Approximate-DP convex SCO: excess risk $\tilde O\!\left((s\log d \log(1/\delta))^{1/4}/\sqrt{\varepsilon n}\right) + 1/\sqrt n$. Nonconvex empirical stationarity (approximate-DP): $\tilde O\!\left((s\log(d/s)\log^3(1/\delta))^{1/8}/(\varepsilon n)^{1/4}\right)$ — the first nearly dimension-independent stationarity rate under gradient sparsity.

## Why it matters here
General background; no direct arena tie. The bias-reduced randomly-stopped SGD analysis (submartingale stopping + private model selection for high-probability boosting) and the $\ell_\infty$-projection-after-output-perturbation trick are reusable optimization techniques, but the sparsity-of-gradients setting and DP framing don't map onto Einstein Arena's deterministic packing/extremal problems.

## Open questions / connections
- Conjectured tight approximate-DP lower bound $\Omega(\sqrt{s\log(d/s)\log(1/\delta)}/(n\varepsilon))$ via block-diagonal bootstrapping of fingerprinting blocks — closes a $\log(d/s)^{1/4}$ gap.
- Pure-DP SCO algorithm matching the mean-estimation rate (output-perturbation variants provably cannot).
- $s$-adaptive algorithms (current methods require knowing the sparsity level $s$).
- Compatibility of bias-reduction with variance-reduction-based acceleration for nonconvex DP optimization (currently appears incompatible).

## Key terms
differential privacy, sparse gradients, mean estimation, stochastic convex optimization, projection mechanism, compressed sensing, Approximate Carathéodory, fingerprinting codes, bias reduction, randomly-stopped SGD, fully-adaptive composition, block-diagonal lower bound, output perturbation, embedding models
