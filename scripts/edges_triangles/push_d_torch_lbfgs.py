"""P13 push: PyTorch autodiff + L-BFGS-B on x-positions.

True gradient-based optimization. Prior work used CD/GS/BH only — no true gradient.
Parameterizes 490 multipartite x-values via unconstrained log-gap representation
to preserve ordering during optimization.

Usage:
    uv run python scripts/edges_triangles/push_d_torch_lbfgs.py
"""

import json
import sys
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")

torch.set_default_dtype(torch.float64)


def load_xs_from_solution(path: Path) -> tuple[np.ndarray, np.ndarray]:
    """Load solution, return (bipartite_xs[10], multipartite_xs[490])."""
    with open(path) as f:
        w = np.array(json.load(f)["weights"], dtype=np.float64)
    w = np.maximum(w, 0.0)
    w /= w.sum(axis=1, keepdims=True)
    s2 = np.sum(w**2, axis=1)
    xs = np.sort(1.0 - s2)
    bi = xs[xs <= 0.5 + 1e-12]
    multi = xs[xs > 0.5 + 1e-12]
    return bi, multi


def assign_scallops(multi: np.ndarray) -> np.ndarray:
    """Return integer scallop k for each x in multi. k ∈ {2,..,19}."""
    ks = np.floor(1.0 / (1.0 - multi) + 1e-10).astype(int)
    return np.clip(ks, 2, 19)


def turan_y_torch(x: torch.Tensor, k: torch.Tensor) -> torch.Tensor:
    """Differentiable Turán y-value for x within scallop k.

    x shape: (m,), k shape: (m,) integer tensor.
    """
    kf = k.to(x.dtype)
    disc = 4.0 * kf * kf - 4.0 * kf * (kf + 1.0) * x
    disc = torch.clamp(disc, min=0.0)
    sqrt_disc = torch.sqrt(disc)
    c = (2.0 * kf + sqrt_disc) / (2.0 * kf * (kf + 1.0))
    c = torch.clamp(c, min=1.0 / (kf + 1.0), max=1.0 / kf)
    remainder = torch.clamp(1.0 - kf * c, min=0.0)
    s2 = kf * c * c + remainder * remainder
    s3 = kf * c * c * c + remainder * remainder * remainder
    # y = 1 - 3s2 + 2s3
    return 1.0 - 3.0 * s2 + 2.0 * s3


def score_torch(
    raw_gaps: torch.Tensor,
    bipartite_xs: torch.Tensor,
    k_vec: torch.Tensor,
    x_lo: float,
    x_hi: float,
) -> torch.Tensor:
    """Differentiable score from unconstrained gap parameterization.

    raw_gaps: (m+1,) unconstrained — softplus → positive gaps, normalized.
    Multipartite x positions fill [x_lo, x_hi]. Bipartite xs fixed.
    """
    # Softplus to get positive gaps, then normalize to sum to (x_hi - x_lo)
    pos_gaps = torch.nn.functional.softplus(raw_gaps)
    pos_gaps = pos_gaps / pos_gaps.sum() * (x_hi - x_lo)
    multi_xs = x_lo + torch.cumsum(pos_gaps[:-1], dim=0)
    # multi_xs has m values in (x_lo, x_hi) if last gap > 0
    # Clamp for numerical safety
    multi_xs = torch.clamp(multi_xs, min=x_lo + 1e-14, max=x_hi - 1e-14)

    multi_ys = turan_y_torch(multi_xs, k_vec)

    # Assemble full curve: 0, bipartite_xs (y=0), x_lo (boundary, y=0), multi_xs (y=multi_ys), 1 (y=1)
    # NOTE: x_lo = 0.5 is already in bipartite_xs (last entry), don't double
    zero = torch.zeros(1, dtype=x_lo.dtype if isinstance(x_lo, torch.Tensor) else torch.float64)
    one = torch.ones(1, dtype=zero.dtype)

    bi_ys = torch.zeros_like(bipartite_xs)
    xs_full = torch.cat([zero, bipartite_xs, multi_xs, one])
    ys_full = torch.cat([zero, bi_ys, multi_ys, one])

    hs = xs_full[1:] - xs_full[:-1]
    dys = ys_full[1:] - ys_full[:-1]
    y1 = ys_full[1:]
    y0 = ys_full[:-1]

    # Three branches:
    # dy < 0: area = y1*h
    # 0 <= dy <= 3h: area = -dy²/6 + y1*h
    # dy > 3h: area = y0*h + 1.5*h²
    area_a = y1 * hs
    area_b = -dys * dys / 6.0 + y1 * hs
    area_c = y0 * hs + 1.5 * hs * hs
    area_per = torch.where(dys < 0, area_a, torch.where(dys <= 3.0 * hs, area_b, area_c))
    area = area_per.sum()
    max_gap = hs.max()
    return -(area + 10.0 * max_gap)


def initialize_raw_gaps_from_multi(
    multi_xs: np.ndarray, x_lo: float, x_hi: float
) -> np.ndarray:
    """Invert softplus+normalize to get raw_gaps matching a given multi_xs layout."""
    m = len(multi_xs)
    gaps = np.empty(m + 1)
    gaps[0] = multi_xs[0] - x_lo
    gaps[1:m] = np.diff(multi_xs)
    gaps[m] = x_hi - multi_xs[-1]
    # Normalize: gaps sum to (x_hi - x_lo). Our param: softplus(raw)/sum*(x_hi-x_lo) = gap
    # So softplus(raw) = gap  (pre-normalization; sum is preserved post-normalization)
    # raw = inverse_softplus(gap) = log(exp(gap) - 1)
    gaps = np.maximum(gaps, 1e-15)
    raw = np.log(np.expm1(gaps))
    return raw


def save_solution(multi_xs: np.ndarray, bi_xs: np.ndarray, out_dir: Path, tag: str = "") -> Path:
    """Reconstruct weight matrix and save."""
    from einstein.edges_triangles.evaluator import compute_densities, turan_row
    all_xs = np.concatenate([bi_xs, multi_xs])
    weights = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in all_xs])
    score = compute_score(weights)
    out_dir.mkdir(parents=True, exist_ok=True)
    suffix = f"-{tag}" if tag else ""
    out_path = out_dir / f"solution{suffix}.json"
    with open(out_path, "w") as f:
        json.dump({"weights": weights.tolist()}, f)
    print(f"  Saved {out_path}  score={score:.14f}")
    return out_path


def main():
    sol_path = RESULTS / "solution.json"
    bi_xs_np, multi_xs_np = load_xs_from_solution(sol_path)
    print(f"Loaded: {len(bi_xs_np)} bipartite, {len(multi_xs_np)} multipartite")

    # Current score
    from einstein.edges_triangles.evaluator import compute_densities, turan_row
    init_w = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in np.concatenate([bi_xs_np, multi_xs_np])])
    init_score = compute_score(init_w)
    print(f"Initial score: {init_score:.14f}")

    x_lo = 0.5
    x_hi = 0.95
    k_np = assign_scallops(multi_xs_np)
    print(f"Scallop distribution: {np.bincount(k_np, minlength=20)[2:]}")

    # Set up PyTorch tensors
    bipartite_t = torch.tensor(bi_xs_np, dtype=torch.float64)
    k_t = torch.tensor(k_np, dtype=torch.int64)

    raw_np = initialize_raw_gaps_from_multi(multi_xs_np, x_lo, x_hi)
    raw = torch.tensor(raw_np, dtype=torch.float64, requires_grad=True)

    # Verify initial score via autodiff forward
    with torch.no_grad():
        init_score_torch = score_torch(raw, bipartite_t, k_t, x_lo, x_hi).item()
    print(f"Torch initial: {init_score_torch:.14f}  (delta {init_score_torch - init_score:+.2e})")

    # L-BFGS
    opt = torch.optim.LBFGS(
        [raw],
        lr=1.0,
        max_iter=50,
        tolerance_grad=1e-18,
        tolerance_change=1e-18,
        history_size=100,
        line_search_fn="strong_wolfe",
    )

    best_score = init_score_torch
    best_raw = raw.detach().clone()

    def closure():
        opt.zero_grad()
        # NEGATIVE score (we maximize)
        s = score_torch(raw, bipartite_t, k_t, x_lo, x_hi)
        loss = -s
        loss.backward()
        return loss

    print("\n=== L-BFGS iterations ===")
    for round_i in range(40):
        loss = opt.step(closure)
        with torch.no_grad():
            cur_score = -loss.item()
        if cur_score > best_score:
            best_score = cur_score
            best_raw = raw.detach().clone()
        print(f"  round {round_i:3d}: {cur_score:.14f}  best={best_score:.14f}")

    print(f"\nFinal best: {best_score:.14f}  (gain {best_score - init_score:+.2e})")

    # Reconstruct multipartite xs from best raw
    with torch.no_grad():
        pos = torch.nn.functional.softplus(best_raw)
        pos = pos / pos.sum() * (x_hi - x_lo)
        new_multi = (x_lo + torch.cumsum(pos[:-1], dim=0)).numpy()
    new_multi = np.clip(new_multi, 0.5 + 1e-14, 0.95 - 1e-14)
    new_multi.sort()

    # Save
    out = save_solution(new_multi, bi_xs_np, RESULTS, tag="torch-lbfgs")
    print(f"\nDone. New solution at {out}")


if __name__ == "__main__":
    main()
