# Einstein

Solver for the [Uncertainty Principle](https://www.einsteinarenaproblem.com/) problem from Einstein Arena.

## Problem

Minimize the largest sign change of a quotient function built from generalized Laguerre polynomials, by choosing optimal double-root positions.

## Approach

- **Evaluation**: Two-tier numerical evaluator — mpmath for the ill-conditioned linear system, vectorized NumPy/SciPy for fast q(x) scanning with Brent refinement (`fast_eval.py`)
- **Optimization**: Hillclimb optimizer with coordinate-wise perturbation, random multi-coordinate moves, and adaptive step sizes (`optimize.py`)
- **Verification**: Exact symbolic verifier using SymPy (`verifier.py`)

## Setup

Requires Python 3.13+.

```bash
uv sync
```

## Usage

```bash
uv run python scripts/optimize.py
```

## Project Structure

```
src/einstein/
├── fast_eval.py    # Fast numerical evaluator (mpmath + NumPy/SciPy)
└── verifier.py     # Exact symbolic verifier (SymPy)
scripts/
└── optimize.py     # Hillclimb optimizer entry point
```

## License

MIT
