---
type: source
kind: paper
title: "OptNet: Differentiable Optimization as a Layer in Neural Networks"
authors: Brandon Amos, J. Kolter
year: 2017
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/1703.00443
source_local: ../raw/2017-amos-optnet-differentiable-optimization-layer.pdf
topic: general-knowledge
cites:
---

# OptNet: Differentiable Optimization as a Layer in Neural Networks

**Authors:** Brandon Amos, J. Kolter  ·  **Year:** 2017  ·  **Source:** https://arxiv.org/abs/1703.00443

## One-line
Embeds a quadratic program as a differentiable neural-network layer, with gradients obtained by implicit differentiation of the KKT conditions and a batched GPU primal-dual interior-point solver.

## Method
Forward pass solves $\min_z \tfrac12 z^TQz + q^Tz$ s.t. $Az=b,\ Gz\le h$ via a batched primal-dual interior-point method (PDIPM) implemented with custom CUBLAS batch LU factorizations. Backward pass differentiates the KKT stationarity, primal-feasibility, and complementary-slackness conditions (matrix differentials, including through inequality constraints rather than barrier-smoothing them) — gradients $\nabla Q, \nabla q, \nabla A, \nabla b, \nabla G, \nabla h$ are recovered by one transposed solve of the already-factored KKT matrix, so backprop is essentially free given the forward solve.

## Result
Batched solver beats Gurobi/CPLEX by ~100× at minibatch 128 (0.18s vs 4.7s for a batch of QPs with 100 vars / 100 ineq constraints). Theorems: (i) $z^*(\theta)$ is subdifferentiable everywhere and differentiable off a measure-zero set when $Q\succ0$ and $A$ has full row rank; (ii) any elementwise piecewise-linear function with $k$ pieces, including ReLU, is exactly representable by an OptNet layer with $O(nk)$ params; (iii) there exist functions an OptNet layer represents with $p$ params that any 2-layer ReLU net needs $O(c^p)$ to approximate (e.g. $\max\{a_1^Tx,a_2^Tx,a_3^Tx\}$, simplex projection). Demos: improves on 1-D total-variation denoising by learning the differencing matrix $D$ (12% test-MSE gain over hand-tuned TV); learns 4×4 Sudoku from input–output pairs alone, where a 10-layer ConvNet overfits.

## Why it matters here
General background; no direct arena tie. Potentially relevant to OptNet-style differentiable LP/SDP layers if the agent ever wants to learn cost coefficients of an inner program (e.g. learning a Cohn–Elkies-like LP objective from data), but the cubic-in-vars complexity caps usefulness at <1000-dim QPs — too small for current arena LP/SDP workloads.

## Open questions / connections
- Sparse-matrix KKT factorizations (cuSOLVER batched sparse QR) to scale beyond dense ~1000-var QPs.
- Extending implicit-KKT differentiation to conic/SDP layers — would tie directly to flag-algebra and Cohn–Elkies LP machinery used in arena work.
- Parameter-manifold redundancies (row scaling of $A$, $b$) complicate training — open question on conditioning / canonicalization.

## Key terms
OptNet, differentiable optimization, KKT conditions, implicit differentiation, primal-dual interior point method, quadratic programming, batched GPU solver, argmin differentiation, bilevel optimization, sensitivity analysis, total variation denoising, Sudoku constraint learning
