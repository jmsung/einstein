---
type: source
kind: paper
title: Anomalies and bounds on charged operators
authors: Ying-Hsuan Lin, Shu-Heng Shao
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1904.04833
source_local: ../raw/2019-lin-anomalies-bounds-charged-operators.pdf
topic: general-knowledge
cites:
---

# Anomalies and bounds on charged operators

**Authors:** Ying-Hsuan Lin, Shu-Heng Shao  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1904.04833

## One-line
Modular-bootstrap bounds on the lightest charged operator in 2d CFTs with $\mathbb{Z}_2$ (and $U(1)$) global symmetry, showing the bound exists iff the symmetry is 't Hooft anomalous.

## Key claim
For unitary bosonic 2d CFTs with internal $\mathbb{Z}_2$ symmetry: a universal upper bound on the lightest $\mathbb{Z}_2$-odd primary $\Delta^-_{\text{gap}}$ exists **iff** the $\mathbb{Z}_2$ is anomalous. Analytic bound for $1<c<3$: $\Delta^-_{\text{gap}} \le (\hat y + 1)\, c/12$ where $\hat y$ is the largest root of a cubic depending on $c$. Saturated by $su(2)_1$ WZW at $c=1$ with $\Delta^-_{\text{gap}}=1/2$.

## Method
Modular bootstrap with linear functionals (semidefinite-programming-style) applied to the torus partition functions $Z(\tau,\bar\tau)$, $Z^{\mathcal{L}}$ (defect-line insertion in time), and $Z_{\mathcal{L}}$ (defect Hilbert space). The 't Hooft anomaly $\alpha\in H^3(\mathbb{Z}_2,U(1))=\mathbb{Z}_2$ enters via the spin selection rule on $\mathcal{H}_{\mathcal{L}}$: $s\in\mathbb{Z}/2$ if non-anomalous, $s\in 1/4+\mathbb{Z}/2$ if anomalous — the latter forces $\Delta\ge 1/4$ on every defect-Hilbert state, which is what enables the bound. Crossing $Z^{\mathcal{L}}(-1/\tau)=Z_{\mathcal{L}}(\tau)$ plus Virasoro-character positivity gives the functional.

## Result
Anomalous case: closed-form analytic bound (cubic in $c$) for $1<c<3$; refined numerical bounds for $c<25$ (Figs. 1, 15), saturated by $su(2)_1$, $(C_3)_1$, $su(6)_1$, $(E_7)_1$. Non-anomalous case: no bound on $\Delta^-_{\text{gap}}$ alone, but an "order–disorder" joint bound — the lightest $\mathbb{Z}_2$-odd state and the defect ground state cannot both be parametrically heavy in $c$ (Fig. 17). Corollary: no $\mathbb{Z}_2$-protected gapless phase without fine-tuning for $1<c<7$ (extends to $1<c<7.81$ if non-anomalous). $U(1)$ analog: bound exists only for holomorphic-current $U(1)$'s (automatically anomalous); none for momentum/winding $U(1)$ of the free boson.

## Why it matters here
General background; no direct arena tie — this is a CFT modular-bootstrap result about 't Hooft anomalies, not a sphere-packing / autocorrelation / extremal-combinatorics technique. The shared machinery is the **linear functional method on modular crossing equations**, which is morphologically similar to the Cohn–Elkies LP bound for sphere packing (search for a functional with sign/positivity constraints that certifies an upper bound) — a methodological cross-link only.

## Open questions / connections
- Extension to non-abelian and higher-form global symmetries — what is the analog of the $1/4$ spin shift?
- Sharpness of the analytic cubic-functional bound vs the SDPB numerical envelope for $c>3$.
- Weak gravity conjecture interpretation in $\text{AdS}_3/\text{CFT}_2$ — non-anomalous $U(1)$ has no light-charged-state bound, tension with sublattice WGC of Heidenreich–Reece–Rudelius (arXiv:1606.08437).

## Key terms
modular bootstrap, 't Hooft anomaly, $\mathbb{Z}_2$ global symmetry, topological defect line, defect Hilbert space, spin selection rule, linear functional method, Virasoro characters, WZW models, $su(2)_1$, free compact boson, weak gravity conjecture, group cohomology $H^3(G,U(1))$, fusion category
