---
type: source
kind: paper
title: Prismatic large 
N
 models for bosonic tensors
authors: S. Giombi, I. Klebanov, F. Popov, S. Prakash, G. Tarnopolsky
year: 2018
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1808.04344
source_local: ../raw/2018-giombi-prismatic-large-models-bosonic.pdf
topic: general-knowledge
cites:
---

# Prismatic large
N
models for bosonic tensors

**Authors:** S. Giombi, I. Klebanov, F. Popov, S. Prakash, G. Tarnopolsky  ·  **Year:** 2018  ·  **Source:** https://arxiv.org/abs/1808.04344

## One-line
Constructs and solves a bosonic $O(N)^3$ tensor QFT with sextic "prism" interaction in $d<3$, finding a stable large-$N$ fixed point with real scaling dimensions in two windows of $d$.

## Key claim
The $O(N)^3$ scalar theory with sextic prism interaction $\phi^{a_1 b_1 c_1}\phi^{a_1 b_2 c_2}\phi^{a_2 b_1 c_2}\phi^{a_3 b_3 c_1}\phi^{a_3 b_2 c_3}\phi^{a_2 b_3 c_3}$ admits a melonic-style large-$N$ limit (with $g_1 N^3$ fixed) whose bilinear spectrum is free of complex dimensions for $2.81 < d < 3$ and $d < 1.68$; in $d=3-\epsilon$ a real prismatic RG fixed point exists for $N > N_{\rm crit} \approx 53.65$.

## Method
Auxiliary-field trick: introduce a tensor $\chi^{abc}$ to convert the sextic prism into a tetrahedral cubic action with two rank-3 tensors, then resum melon-like diagrams via Schwinger–Dyson equations for the two-point functions $G(p), F(p)$ ansatz $A/p^{2a}$, $B/p^{2b}$. Cross-checked with two-loop renormalized perturbation theory in $d = 3-\epsilon$, treating all eight $S_3 \times O(N)^3$-invariant sextic operators. Scaling-dimension eigenvalue equations $f(d,\Delta_\phi)=1$ solved numerically and matched against $\epsilon$-expansions of bilinear dimensions.

## Result
Conformal data: $3\Delta_\phi + \Delta_\chi = d$; at $d=2.9$, $\Delta_\phi \approx 0.456$, $\Delta_\chi \approx 1.531$; at $d=2$, $\Delta_\phi = (13 - \sqrt{4})/something$ from $3(3\Delta_\phi-1)^2 = (\Delta_\phi-1)^2$; at $d=1$, $\Delta_\phi \approx -0.0906$ (above unitarity). The $\epsilon$-expansion gives $\Delta_\phi = 1/2 - \epsilon/2 + 2\epsilon^2(1 - 12/N) + \ldots$ and $\Delta_{\phi^2} = 1 - \epsilon + 32\epsilon^2(1 - 12/N) + \ldots$. Bilinear A/C spectrum has complex dimensions in the band $1.68 < d < 2.81$ via a fixed-point merger at $\Delta = d/2$; at $N = N_{\rm crit} \approx 53.65$ the prismatic fixed point collides with another and becomes complex.

## Why it matters here
General background; no direct arena tie. The work is QFT/holography, not Einstein Arena math — the technical machinery (Schwinger-Dyson resummation, fixed-point mergers producing complex dimensions, $\epsilon$-expansion cross-check of large-$N$) is unrelated to sphere packing / autocorrelation / extremal combinatorics. Possibly tangential reference for fixed-point-merger phenomenology if a problem ever exhibits a two-solution-merging-into-complex-pair structure in a parameter sweep (e.g. the $d_{\rm crit}$ behavior in some optimization landscape).

## Open questions / connections
- Generalization to $O(N)^p$ models with rank-$p$ tensors and order-$2p$ potentials for odd $p \geq 3$ (action sketched but not solved).
- Effect of 4-loop and higher corrections on the prismatic fixed-point location and on $N_{\rm crit}$.
- Whether the $d=1$ quantum mechanics with negative $\Delta_\phi \approx -0.09$ admits a sensible holographic dual (dilaton gravity in AdS$_2$?).
- Possibility of alternative large-$N$ scalings dominated by the "wheel" interaction $g_2$ rather than the prism $g_1$.
- Supersymmetric extension via $\mathcal{N}=1$ superfield $\Phi^{abc}$ with tetrahedral superpotential — three couplings, computable beta functions.

## Key terms
tensor model, $O(N)^3$ symmetry, sextic interaction, prismatic large N limit, melonic diagrams, Schwinger-Dyson equations, bilinear operators, complex scaling dimensions, fixed point merger, $\epsilon$-expansion, Breitenlohner-Freedman bound, SYK model, conformal field theory
