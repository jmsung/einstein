---
type: source
kind: paper
title: An efficient container lemma
authors: J. Balogh, Wojciech Samotij
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1910.09208
source_local: ../raw/2019-balogh-efficient-container-lemma.pdf
topic: general-knowledge
cites:
---

# An efficient container lemma

**Authors:** J. Balogh, Wojciech Samotij  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1910.09208

## One-line
A refined hypergraph container lemma whose key parameter $\delta$ shrinks only polynomially (not factorially) in the uniformity $s$, enabling sharper bounds when uniformity grows with vertex count.

## Key claim
For $s$-uniform hypergraphs satisfying co-degree conditions $\Delta_t(H) \le K(q/(10^6 s^5))^{t-1} \cdot e(H)/v(H)$, there exist containers of size $(1-\delta)v(H)$ with $\delta = (10^3 s^4 K)^{-1}$ — i.e. $\delta$ is polynomial in $1/s$, vs. the earlier $\delta \le 1/s!$ from Balogh–Morris–Samotij and Saxton–Thomason.

## Method
Replaces $\infty$-norm degree control with **2-norm of the degree-measure vector** $\sigma_H^{(t)}$, viewing hypergraphs as vectors in high-dimensional Euclidean space. The vertex-selection step in the inductive container construction is reduced to an elementary convex-geometry problem (Lemma 4.12, inspired by Buhovski). A "robust density → bounded max-degree" lemma (Lemma 2.2, after Morris–Saxton) packages the recursive step.

## Result
Four sharpened applications: (1) almost all $K_{r+1}$-free graphs on $n$ vertices are $r$-partite whenever $r \le \log n/(121 \log\log n)$ (was $r \le (\log n)^{1/4}$); (2) planar $\varepsilon$-nets for lines may require $\ge (1/(80\varepsilon)) \cdot \log(1/\varepsilon)/\log\log(1/\varepsilon)$ points (improves Balogh–Solymosi's $1/3$-exponent to $1/2$); (3) Folkman number $F(n;k) \le \exp(Ckn^3 \log k)$; (4) induced Ramsey $R_{\mathrm{ind}}(H;k) \le \exp(Ckn^2 \log k)$. Application (1) suggests the new lemma is near-optimal for general high-uniformity hypergraphs.

## Why it matters here
General background; no direct arena tie. Container methods are an extremal-combinatorics tool for *counting* / *typical structure* of forbidden-substructure families — relevant to potential meta-questions about how many configurations realize a given extremal value (e.g. typical structure of near-optimal autocorrelation sequences or extremal graphs) but not to numerical optimization of a single arena instance.

## Open questions / connections
- Can the $\log\log n$ factor in the $K_{r+1}$-free clique-size threshold be removed (the conjectured truth is $(2-\varepsilon)\log_2 n$)?
- Is Alon's $\Omega((1/\varepsilon)\log(1/\varepsilon))$ lower bound for planar $\varepsilon$-nets achievable, closing the gap above $(1/2)$-exponent?
- Extends Balogh–Morris–Samotij (2015) and Saxton–Thomason (2015, 2016) container theorems; uses Morris–Saxton (2016) supersaturation; refines Nenadov–Steger random-Ramsey method.

## Key terms
hypergraph container lemma, degree measure, 2-norm, convex geometry, independent sets, $K_{r+1}$-free graphs, typical structure, Kolaitis–Prömel–Rothschild, $\varepsilon$-nets, VC dimension, Folkman numbers, induced Ramsey numbers, extremal graph theory, Balogh, Samotij, Saxton–Thomason
