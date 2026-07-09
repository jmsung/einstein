---
type: source
kind: paper
title: On the Finite Field Cone Restriction Conjecture in Four Dimensions and Applications in Incidence Geometry
authors: Doowon Koh, Sujin Lee, T. Pham
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2004.06593
source_local: ../raw/2020-koh-finite-field-cone-restriction.pdf
topic: general-knowledge
cites:
---

# On the Finite Field Cone Restriction Conjecture in Four Dimensions and Applications in Incidence Geometry

**Authors:** Doowon Koh, Sujin Lee, T. Pham  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2004.06593

## One-line
Settles the finite-field cone restriction conjecture in four dimensions when $-1$ is a non-square, and applies cone restriction to derive sharp point-sphere incidence bounds for small sphere families.

## Method
Decompose $\|\widehat{g}\|_{L^2(C_n,d\sigma)}^2$ for characteristic functions into terms whose signs are controlled by Gauss sums; the explicit value $G_1^{n-2} = -|F|^{(n-2)/2}$ (when $|F|\equiv 3 \bmod 4$, $n\equiv 0 \bmod 4$) forces large terms to be negative, yielding an unusually small $L^2$ norm. Lift to general test functions via dyadic decomposition (Minkowski + pigeonhole over level sets $G_i = \{2^{-j-1} < g \le 2^{-j}\}$) split across three size regimes. The incidence application reduces point-sphere counts to $L^2$ cone restriction on the lifted cone $C_{d+2}$ via the parametrization $s\mapsto t(-2a, 1, \|a\|-r)$.

## Result
**Theorem 1.4/1.5:** For $|F|\equiv 3 \bmod 4$ and $n\equiv 0 \bmod 4$, $R^*_{C_n}(2 \to \tfrac{2n+4}{n}) \lesssim 1$; in particular $R^*_{C_4}(2\to 3)\lesssim 1$ resolves the 4D conjecture in the non-square case (improves the Stein–Tomas bound $R^*_{C_4}(2\to 4)$). **Theorem 1.6:** For small sphere sets ($|S|\le |F|^{d/2}$, $|F|^{(d-2)/2}$, or $|F|^{(d-1)/2}$ depending on parity/quadratic character), $|I_w(P,S) - |F|^{-1}|P|\sum_S w| \lesssim |F|^{(d-1)/2}|P|^{1/2}(\sum |w|^2)^{1/2}$ — sharp, and a substantial improvement over the Cilleruelo–Iosevich–Lund–Roche-Newton–Rudnev bound $|F|^{d/2}\sqrt{|P||S|}$.

## Why it matters here
General background; no direct arena tie. Closest relevance is methodological: Fourier-decay/Gauss-sum sign control in restriction problems is a paradigm worth knowing for any extremal/incidence-flavored arena problem (e.g. Sidon-set or autocorrelation variants), and the L^p restriction → incidence reduction template parallels how LP/duality bounds get extracted in sphere-packing work.

## Open questions / connections
- Can $|S|\le |F|^{d/2}$ in Theorem 1.6(1) be relaxed to $|S|\le |F|^{(d+2)/2}$? If yes, it would settle the Erdős–Falconer distance conjecture for $d\equiv 2 \bmod 4$, $|F|\equiv 3 \bmod 4$ (Subsection 6.2).
- Extends Mockenhaupt–Tao (3D cone) and parallels Rudnev–Shkredov 4D paraboloid result, but via Gauss-sum signs rather than point-plane incidences — works over arbitrary finite fields, not just primes.
- Conjecture 1.3 remains open at the critical endpoint for $n\ge 8$ even when $-1$ is non-square; method gives sharp "$r$" but not sharp "$p$".

## Key terms
finite field restriction, cone restriction conjecture, Gauss sums, quadratic character, Stein-Tomas, Mockenhaupt-Tao, paraboloid restriction, point-sphere incidences, Erdős-Falconer distance problem, Fourier decay, dyadic decomposition, Plancherel
