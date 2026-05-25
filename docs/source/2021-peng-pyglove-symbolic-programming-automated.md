---
type: source
kind: paper
title: "PyGlove: Symbolic Programming for Automated Machine Learning"
authors: Daiyi Peng, Xuanyi Dong, Esteban Real, Mingxing Tan, Yifeng Lu, Gabriel Bender, Hanxiao Liu, Adam Kraft, Chen Liang, Quoc V. Le
year: 2021
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2101.08809
source_local: ../raw/2021-peng-pyglove-symbolic-programming-automated.pdf
topic: general-knowledge
cites:
---

# PyGlove: Symbolic Programming for Automated Machine Learning

**Authors:** Daiyi Peng, Xuanyi Dong, Esteban Real, Mingxing Tan, Yifeng Lu, Gabriel Bender, Hanxiao Liu, Adam Kraft, Chen Liang, Quoc V. Le  ·  **Year:** 2021  ·  **Source:** https://arxiv.org/abs/2101.08809

## One-line
A Python library that reformulates AutoML as symbolic manipulation of mutable program objects, decoupling search space, search algorithm, and child program so each can be changed independently.

## Key claim
By making ML programs symbolically mutable (via a `@symbolize` decorator that turns classes/functions into tree-structured objects with `rebind`-able hyper-parameters), the triangle of {child program, search space, search algorithm} can be decoupled — including the search-space ↔ algorithm coupling that previously blocked weight-sharing NAS (ENAS, DARTS) from being swapped in without rewriting model code.

## Method
Every program construct $t$ is symbolized to $s = S(t) = \langle t, P(t)\rangle$ where $P(t)$ are its hyper-parameters; symbolic objects form a tree and support operations `rebind`, `clone`, `query`, `isinstance`, `equal`. A search space is built by "hyperifying" — replacing fixed sub-nodes with `pg.oneof`, `pg.manyof`, `pg.floatv` placeholders. Search algorithms operate on an abstract search space; child programs are materialized by recursively merging algorithm decisions into the symbolic tree (Algorithms 1–2). Eager vs late-bound materialization both supported.

## Result
Case studies on ImageNet (MobileNetV2 search spaces S1/S2/S3 over kernel sizes, expansion ratios, channel widths) and NAS-Bench-101 (standard / factorized / hybrid search flows) demonstrate that switching search space, search algorithm (random, Bayesian, RL, regularized evolution, TuNAS weight-sharing), or search flow takes only a few lines of code. No new mathematical bound is established — the contribution is the programming paradigm and its empirical expressiveness.

## Why it matters here
General background; no direct arena tie. Relevant only as a *meta-tool* if the agent ever wants to express its optimizer-configuration space (basin-hopping params, parallel-tempering temperatures, parameterizations) as a searchable symbolic tree rather than ad-hoc CLI flags — i.e. a possible substrate for the self-improvement loop's "execute" step, not for any math problem itself.

## Open questions / connections
- Could symbolic program manipulation express the council-dispatch + materialization pipeline (persona → question → search-space → optimizer config) more cleanly than current scripts?
- Connects to AutoML-Zero (Real et al. 2020, ref [62]) — evolving ML algorithms from scratch, which is closer in spirit to discovering optimizer ingredients.
- No guidance on continuous/black-box optimization over high-precision (mpmath) numerical search spaces — the abstraction is built for discrete architectural choices.

## Key terms
symbolic programming, AutoML, neural architecture search, NAS, PyGlove, mutable program, search space decoupling, weight sharing, ENAS, DARTS, regularized evolution, hyper-parameter search
