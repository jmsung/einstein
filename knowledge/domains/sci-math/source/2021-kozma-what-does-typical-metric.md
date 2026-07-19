---
type: source
kind: paper
title: What does a typical metric space look like?
authors: Gady Kozma, Tom Meyerovitch, Ron Peled, Wojciech Samotij
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: http://arxiv.org/abs/2104.01689v2
source_local: ../raw/2021-kozma-what-does-typical-metric.pdf
topic: general-knowledge
cites: 
---

# What does a typical metric space look like?

**Authors:** Gady Kozma, Tom Meyerovitch, Ron Peled, Wojciech Samotij  ·  **Year:** 2021  ·  **Source:** http://arxiv.org/abs/2104.01689v2

## One-line
Proves that a uniformly random finite metric space on $n$ points with diameter $\le 2$ is, in the large-$n$ limit, essentially the cube $[1,2]^{\binom{n}{2}}$ — all pairwise distances cluster near $[1,2]$ and the triangle inequality becomes vacuous.

## Key claim
For the metric polytope $M_n = \{(d_{ij}) : d_{ij} \le 2,\ d_{ij} \le d_{ik}+d_{kj}\}$: $\exp((1/6-o(1))n^{3/2}) \le \mathrm{Vol}(M_n) \le \exp(Cn^{3/2})$, and for $d$ sampled uniformly from $M_n$, $\Pr[\min_{i,j} d_{ij} \le 1 - n^{-c}] \le Cn^{-c}$ for some $c>0$ (proof shows $c$ up to $1/30$).

## Method
Entropy techniques: (i) a pigeonhole conditioning step finds a set $F$ of $\le n^{3/2}$ pairs such that, conditioned on $\{d_f: f\in F\}$, edges of triangles outside $F$ become almost independent (controlled in average KL divergence); (ii) Steiner-triple-system subadditivity decomposes the remaining entropy into per-triangle terms; (iii) a max-entropy lemma bounds the entropy of a vector almost-supported in a convex set $P$ by $\log\mathrm{Vol}$(largest box in $P$), with the unique largest box in $M_3$ being $[1,2]^3$. Lower bound uses the Lovász Local Lemma; alternative routes via hypergraph containers (Balogh–Wagner + Morris) give $\exp(Cn^{3/2}(\log n)^3)$, and Kővári–Sós–Turán gives $\exp(Cn^2(\log\log n)^2/\log n)$.

## Result
Volume sandwiched between $\exp((1/6-o(1))n^{3/2})$ and $\exp(Cn^{3/2})$; the limit $\lim \mathrm{Vol}(M_n)^{1/\binom{n}{2}}$ exists and equals $1$. Minimum distance is at least $1-n^{-c}$ w.h.p.; a matching lower-tail bound (Prop. 4.5) shows $\Pr[d_{12}<1-a/\sqrt n]\to 1$ for any $a<1/3$. Discrete analogue $|M_n^M|$ matches via $\mathrm{Vol}(M_n)\le|M_n^M|(2/M)^{\binom{n}{2}}\le(1+2/M)^{\binom{n}{2}}\mathrm{Vol}(M_n)$.

## Why it matters here
General background; no direct arena tie. Useful as a worked example of entropy + conditional-independence + Shearer + KL-divergence proving a tight $n^{3/2}$ exponent for a convex body's volume — methodology transferable to extremal/packing volume estimates and lower-tail concentration arguments.

## Open questions / connections
- Is $\mathrm{Vol}(M_{n+1}) \ge \mathrm{Vol}(M_n)$ monotone? Open; would simplify the min-distance bound.
- Is $\Pr(d_{12}<1) = \Theta(n^{-1/2})$? Does $f_n(1-t/\sqrt n)$ have a limit; does $(d_{ij})$ satisfy an LDP and with what rate function?
- Extends Balogh–Wagner [8] container bound $\exp(n^{11/6+o(1)})$; connects to Tao's entropy-regularity [38], Loomis–Whitney stability via Ellis–Friedgut–Kindler–Yehudayoff [15], Lovász–Szegedy Hilbert-space regularity [31]; method later adapted to lower tails of Bernoulli polynomials (Kozma–Samotij [28]).

## Key terms
metric polytope, differential entropy, Shearer's inequality, Kullback-Leibler divergence, Lovász Local Lemma, hypergraph containers, Szemerédi regularity lemma, Kővári-Sós-Turán, Loomis-Whitney, Steiner triple system, conditional almost independence, triangle inequality volume bound
