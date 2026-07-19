---
type: source
kind: paper
title: "GraphCast: Learning skillful medium-range global weather forecasting"
authors: Rémi R. Lam, Alvaro Sanchez-Gonzalez, M. Willson, Peter Wirnsberger, Meire Fortunato, A. Pritzel, Suman V. Ravuri, T. Ewalds, Ferran Alet, Z. Eaton-Rosen, Weihua Hu, Alexander Merose, Stephan Hoyer, George Holland, Jacklynn Stott, O. Vinyals, S. Mohamed, P. Battaglia
year: 2022
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2212.12794
source_local: ../raw/2022-lam-graphcast-learning-skillful-medium-range.pdf
topic: general-knowledge
cites:
---

# GraphCast: Learning skillful medium-range global weather forecasting

**Authors:** Rémi R. Lam, Alvaro Sanchez-Gonzalez, M. Willson, Peter Wirnsberger, Meire Fortunato, A. Pritzel, Suman V. Ravuri, T. Ewalds, Ferran Alet, Z. Eaton-Rosen, Weihua Hu, Alexander Merose, Stephan Hoyer, George Holland, Jacklynn Stott, O. Vinyals, S. Mohamed, P. Battaglia  ·  **Year:** 2022  ·  **Source:** https://arxiv.org/abs/2212.12794

## One-line
A graph-neural-network weather model trained on ERA5 reanalysis that produces 10-day global forecasts at $0.25°$ resolution in under a minute and beats ECMWF's operational HRES on $90.3\%$ of 1380 verification targets.

## Key claim
GraphCast significantly outperforms HRES (the world's top deterministic NWP system) on $89.9\%$ of 1380 variable/level/lead-time targets ($p \leq 0.05$), and on $99.7\%$ when stratospheric levels (50, 100 hPa) are excluded; it also beats Pangu-Weather on $99.2\%$ of 252 targets and improves tropical cyclone track, atmospheric river ($25\% \to 10\%$ RMSE reduction), and extreme-heat forecasts despite not being trained for them.

## Method
Encode-process-decode GNN with 36.7M parameters operating on a "multi-mesh" — six-times-refined icosahedron (40,962 nodes) carrying the union of all intermediate-resolution edges, enabling simultaneous local + long-range message passing. Encoder maps a $721 \times 1440$ lat/lon grid (227 vars/point = 5 surface + 6 atmospheric $\times$ 37 pressure levels) onto the mesh; 16 unshared GNN layers process; decoder maps back as a residual update. Trained autoregressively (1979–2017 ERA5) with MSE loss whose horizon is curriculum-grown from 1 to 12 steps (6h to 3d), ~4 weeks on 32 TPU v4.

## Result
Single forecast: 10-day global state in <1 min on one TPU v4 vs ~1 hour on supercomputer for HRES. RMSE skill-score improvements of $7\%$–$14\%$ on the z500 headline. Stratospheric levels (50 hPa) are the dominant failure region — they carry the lowest training-loss weight. Training-data recency matters: retraining through 2020 measurably improves 2021 z500 skill over the <2018 variant. Optimally-blurred GraphCast still beats optimally-blurred HRES on $88.0\%$ of targets, ruling out "GraphCast just wins by blurring."

## Why it matters here
General background; no direct arena tie. The relevant transferable ideas are architectural — multi-mesh / icosahedral hierarchy as a way to handle long-range coupling in spherical geometry (faintly adjacent to sphere-packing / kissing problems on $S^d$) and the curriculum-rollout MSE-loss schedule as a stable training recipe for autoregressive numerical predictors.

## Open questions / connections
- Multi-mesh hierarchy on the icosahedron — could analogous hierarchical mesh structures help SDP/LP relaxations on $S^2$ packing problems (P-class: sphere packing, kissing)?
- Curriculum on autoregressive rollout horizon as a recipe for any iterated-map optimizer (basin hopping, parallel tempering chains) — does growing the horizon improve stability?
- Output blurring as expression of uncertainty: parallels to how mpmath-polished optima exhibit smoothing in equioscillation problems; failure-mode analogy worth a question.
- Stratosphere = lowest-loss-weighted region = worst-performing region. General principle: loss-weighting determines where the model concedes accuracy — direct analogue to objective weighting in multi-criteria arena problems.

## Key terms
GraphCast, graph neural network, multi-mesh, icosahedral refinement, encode-process-decode, ERA5, HRES, ECMWF, autoregressive rollout, weather forecasting, message passing, residual prediction, curriculum training
