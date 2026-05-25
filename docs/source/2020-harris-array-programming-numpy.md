---
type: source
kind: paper
title: Array programming with NumPy
authors: Charles R. Harris, K. Millman, S. Walt, R. Gommers, Pauli Virtanen, D. Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, M. Kerkwijk, M. Brett, A. Haldane, Jaime Fern'andez del R'io, Marcy Wiebe, Pearu Peterson, Pierre G'erard-Marchant, Kevin Sheppard, T. Reddy, Warren Weckesser, Hameer Abbasi, C. Gohlke, T. Oliphant
year: 2020
author: agent
drafted: 2026-05-23
ingested_at: 2026-05-23
source_type: arxiv
source_url: https://arxiv.org/abs/2006.10256
source_local: ../raw/2020-harris-array-programming-numpy.pdf
topic: general-knowledge
cites:
---

# Array programming with NumPy

**Authors:** Charles R. Harris, K. Millman, S. Walt, R. Gommers, Pauli Virtanen, D. Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, M. Kerkwijk, M. Brett, A. Haldane, Jaime Fern'andez del R'io, Marcy Wiebe, Pearu Peterson, Pierre G'erard-Marchant, Kevin Sheppard, T. Reddy, Warren Weckesser, Hameer Abbasi, C. Gohlke, T. Oliphant  ·  **Year:** 2020  ·  **Source:** https://arxiv.org/abs/2006.10256

## One-line
Describes NumPy's array data model, vectorized API, and the dispatch protocols (`__array_function__`, `__array_ufunc__`) that let NumPy act as a central interoperability layer for GPU/distributed/sparse array libraries.

## Key claim
A small set of array primitives — strided ndarray with `(dtype, shape, strides)` metadata, ufunc broadcasting, fancy indexing, and reduction — plus dispatch protocols suffice to unify Python's scientific computing ecosystem and federate specialized array backends (CuPy, Dask, JAX, PyTorch, sparse) without forking the user-facing API.

## Method
Engineering paper, not a theorem paper. Documents (i) the ndarray memory model (pointer + dtype + shape + C/Fortran strides), (ii) ufuncs as C-level vectorized loops with NumPy-broadcasting semantics, (iii) NEP 13 (`__array_ufunc__`) and NEP 18 (`__array_function__`) dispatch protocols that let external array types intercept >400 NumPy functions, and (iv) the new `BitGenerator`/`Generator`/`SeedSequence` RNG architecture (PCG64 default, Philox, SFC64, MT19937; Ziggurat for normal/exp/gamma; Lemire for bounded ints; spawnable seed sequences for distributed parallelism).

## Result
NumPy 1.17 ships the array-function protocol covering most of the NumPy API; CuPy/Dask/JAX/MXNet/PyData-Sparse implement it, so user code written against `import numpy as np` transparently dispatches to GPU/distributed/sparse backends. New RNG drops the stream-compatibility guarantee on `Generator` (kept on legacy `RandomState`) to allow algorithmic improvements; `SeedSequence.spawn` gives deterministic seeding for distributed workers without knowing worker count in advance. CI extended to ppc64le, ARMv8, s390x (big-endian).

## Why it matters here
General background; no direct arena tie. Relevant only as infrastructure context — the agent's optimizer code runs on NumPy ndarrays, broadcasting/ufuncs are the substrate of vectorized evaluators, and `SeedSequence.spawn` is the right pattern for reproducible multistart seeding across multiprocess/Modal workers (compute-router workloads).

## Open questions / connections
- Should multistart / parallel-tempering seeds in `src/einstein/` use `SeedSequence.spawn` to guarantee reproducibility across local-multiprocess vs Modal runs?
- Array-function protocol enables a single optimizer codepath to run on NumPy (local CPU) or CuPy (Modal GPU) — is any current evaluator a candidate, given the compute-router matrix (float64 sustained-parallel only)?
- Connects to `findings/gpu-modal-compute.md` (GPU idle on sequential Python): vectorize-first is the prerequisite for protocol-based GPU dispatch to be worth anything.

## Key terms
NumPy, ndarray, ufunc, broadcasting, strides, vectorization, array-function protocol, NEP 18, dispatch, CuPy, Dask, JAX, SeedSequence, PCG64, Ziggurat, Lemire, reproducibility, BLAS, OpenBLAS
