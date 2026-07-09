---
type: source
kind: paper
title: Deep Learning for Symbolic Mathematics
authors: Guillaume Lample, François Charton
year: 2019
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1912.01412
source_local: ../raw/2019-lample-deep-learning-symbolic-mathematics.pdf
topic: general-knowledge
cites:
---

# Deep Learning for Symbolic Mathematics

**Authors:** Guillaume Lample, François Charton  ·  **Year:** 2019  ·  **Source:** https://arxiv.org/abs/1912.01412

## One-line
Trains a transformer seq2seq model on synthetically generated (expression, solution) pairs to perform symbolic integration and solve 1st/2nd-order ODEs, outperforming Mathematica/Maple/Matlab.

## Key claim
A 6-layer transformer (8 heads, dim 512) achieves $\approx 99.6\%$ accuracy on symbolic integration and $97.0\%$ / $81.0\%$ on 1st / 2nd-order ODEs (beam 50), versus Mathematica's $84.0\%$ / $77.2\%$ / $61.6\%$ at 30 s timeout.

## Method
Expressions are represented as unary-binary trees serialized in prefix (Polish) notation; problem-space sizing is derived via generating functions (Catalan $C_n$ for binary, Schroeder $S_n$ for unary-binary), with recurrence $(n+1)E_n = (p_1 + 2Lp_2)(2n-1)E_{n-1} - p_1(n-2)E_{n-2}$. Three data-generation schemes are introduced: **FWD** (random $f$, integrate via CAS), **BWD** (random $F$, differentiate to get $(F', F)$ — fast, CAS-free), and **IBP** (compose two random functions via integration-by-parts to discover new (integrand, integral) pairs). ODE generation starts from a solvable bivariate $F(x,y)=c$, eliminates the constant by differentiation, yielding (ODE, solution) pairs; verification is by substitution into the equation or by differentiating the predicted primitive.

## Result
Beam search is critical (especially for ODEs: +38 points on ODE2 from beam 1 to 50, because equivalent solutions are abundant). FWD-trained models transfer poorly to BWD test sets ($\approx 17\%$) and vice versa, because the two generators induce sharply different input/output length distributions (BWD: long input, short output; FWD: opposite; IBP balanced). Mixing IBP/FWD into BWD restores cross-distribution accuracy. The model frequently produces algebraically distinct but equivalent solutions, confirmed via SymPy.

## Why it matters here
General background; no direct arena tie. Possibly relevant as methodological inspiration for **synthetic data generation via inverse problem construction** (BWD trick — generate $F$, take derivative as input) and the **tree-as-prefix-sequence** representation, both of which could apply to learned guidance for combinatorial/symbolic search in arena problems where exact closed forms are needed (e.g., autocorrelation, equioscillation polynomials). Not directly informative on sphere packing, LP bounds, or any specific arena concept.

## Open questions / connections
- Can transformer-generated symbolic *candidates* (followed by exact verification) substitute for/augment Remez exchange or magic-function search in problems like Cohn–Elkies LP duals?
- Distribution-mismatch lesson: any synthetic-data pipeline for optimizer-guidance models in this repo must match deployment input length/structure or learn the bias.
- Verification asymmetry (integration $\to$ differentiate to check) parallels triple-verify: cheap forward check on a candidate solution beats trying to certify the search.

## Key terms
seq2seq transformer, symbolic integration, ordinary differential equations, prefix notation, Polish notation, Catalan numbers, Schroeder numbers, generating functions, backward generation, integration by parts, beam search, SymPy verification, Risch algorithm, synthetic dataset generation, unary-binary trees
