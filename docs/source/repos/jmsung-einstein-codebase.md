---
type: source
provenance: repos
author: agent
drafted: 2026-05-02
level: 4
source_type: codebase
source_url: local — /Users/jmsung/projects/einstein/cb
cites:
  - ../repos/jmsung-einstein.md
  - findings/optimizer-recipes.md
  - findings/gpu-modal-compute.md
  - findings/verification-patterns.md
  - findings/sa-parallel-tempering.md
  - ../personas/_synthesis.md
---

[[../home]] | [[../index]]

# Sung — JSAgent Codebase (einstein/cb)

**Author:** Jongmin Sung
**Language:** Python 3.13+
**Package:** `einstein` (src layout)
**Build:** setuptools + uv

## Summary

The einstein codebase (`cb/`) is the active working repository for JSAgent. It contains the shared optimization library (`src/einstein/`), per-problem scripts (`scripts/`), tests (`tests/`), and public documentation (`docs/`). The codebase implements the adaptive optimizer, knowledge layer, mathematician council, GPU tempering module, and per-problem evaluators/verifiers.

As of 2026-04-21: 65 Python source files (6,956 lines), 43 test files, 228 script files covering 19+ arena problems.

## Architecture

### Core Library (`src/einstein/`)

| Module | Purpose |
|--------|---------|
| `optimizer.py` (265 lines) | RALPH-style adaptive optimizer — strategy selection, iteration, learning. Built-in: hill climb, Nelder-Mead, L-BFGS-B, perturbation |
| `knowledge.py` (93 lines) | Knowledge layer — loads `knowledge.yaml` from MB, returns strategy priors per problem category |
| `council/personas.py` | Mathematician council persona definitions and dispatch |
| `gpu_tempering/` | Problem-agnostic parallel tempering SA with PyTorch + Triton |

### GPU Tempering Module (`src/einstein/gpu_tempering/`)

| File | Purpose |
|------|---------|
| `core.py` | `ParallelTemperingSA` engine with `torch.compile` |
| `losses.py` | Pluggable loss functions (`HingeOverlapLoss`, `CoulombLoss`) |
| `manifolds.py` | Constraint manifolds (`SphereManifold`, `FlatManifold`) |
| `benchmark.py` | CPU vs GPU vs torch.compile comparison — run before any GPU work |
| `fused_step.py` | Fused SA step for reduced kernel launches |
| `triton_kernel.py` | Custom Triton kernels for <50% GPU util scenarios |

### Per-Problem Subpackages (`src/einstein/<problem>/`)

18 subpackages, each providing `evaluator.py` (arena-matching scorer) and optional `fast.py` (numba-accelerated), `optimizer.py` (problem-specific strategies), `polish.py` (float64 refinement):

autocorrelation, circle_packing_square, circles_rectangle, difference_bases, edges_triangles, erdos, first_autocorrelation, flat_poly, heilbronn_convex, heilbronn_triangles, hexagon, kissing_number, min_distance_ratio, prime, tammes, third_autocorrelation, thomson, uncertainty

### Scripts (`scripts/`)

Per-problem optimizer entry points plus shared utilities:
- `check_submission.py` — pre-flight URL check, leaderboard poll, credentials
- `promote_to_mb.py` — curate solution files from cb to MB
- `scrape_arena.py` — arena data scraping
- `update_status.py` — README arena status table updater
- `arena_watchdog.py` — monitoring
- `council_demo.py` — mathematician council demonstration
- Per-problem dirs mirror `src/einstein/` structure

### Dependencies

Heavy numerical stack: numpy, scipy, torch, numba, cvxpy (Clarabel solver), mpmath, sympy, galois, ortools (Google OR-Tools), highspy, cma (CMA-ES), modal (cloud GPU)

### Public Docs (`docs/`)

- `arena.md` — platform reference
- `methodology.md` — cross-problem optimizer taxonomy
- `timeline.md` — discovery timeline for attribution
- `findings/` — public subset of MB findings
- `posts/` — arena discussion posts
- 19 per-problem deep dives (`problem-{id}-{name}.md`)

## Relevance to Einstein Project

This is the codebase itself — the entity page serves as a structural map for navigating the code. Key connections:

- **optimizer.py** implements the recipes cataloged in findings/optimizer-recipes.md
- **gpu_tempering/** implements the GPU strategy from findings/gpu-modal-compute.md
- **Evaluators** implement the verification patterns from findings/verification-patterns.md
- **council/** implements the personas from ../personas/_synthesis.md
- **knowledge.py** bridges the codebase to the MB knowledge layer

## Limitations

- `knowledge.py` path resolution uses hardcoded fallback paths — fragile if workspace moves
- No unified CLI entry point — each problem has its own script
- GPU module requires Modal account for cloud runs

*Last updated: 2026-04-21*
