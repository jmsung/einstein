"""P13 extreme push: scallop reallocation + L-BFGS.

The prior "globally optimal" proof tested point-wise moves within a fixed scallop
allocation. This script tries STRUCTURAL changes: reallocating points between
scallops, then re-optimizing positions with bounded L-BFGS.

Target: improve score by ≥8e-6 to clear the minImprovement gate.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "src"))
from einstein.edges_triangles.evaluator import compute_score, turan_row  # noqa: E402

RESULTS = Path("results/problem-13-edges-triangles")
torch.set_default_dtype(torch.float64)


def load_xs(path: Path) -> tuple[np.ndarray, np.ndarray]:
    with open(path) as f:
        w = np.array(json.load(f)["weights"], dtype=np.float64)
    w = np.maximum(w, 0.0)
    w /= w.sum(axis=1, keepdims=True)
    s2 = np.sum(w**2, axis=1)
    xs = np.sort(1.0 - s2)
    bi = xs[xs <= 0.5 + 1e-12]
    multi = xs[xs > 0.5 + 1e-12]
    return bi, multi


def assign_scallops(xs: np.ndarray) -> np.ndarray:
    ks = np.floor(1.0 / (1.0 - xs) + 1e-10).astype(int)
    return np.clip(ks, 2, 19)


def turan_y_np(x: float, k: int) -> float:
    """Turán y-value for x on scallop k."""
    disc = 4.0 * k**2 - 4.0 * k * (k + 1) * x
    if disc < 0:
        return 0.0
    sqrt_disc = np.sqrt(disc)
    c = (2.0 * k + sqrt_disc) / (2.0 * k * (k + 1))
    c = np.clip(c, 1.0 / (k + 1), 1.0 / k)
    rem = max(0.0, 1.0 - k * c)
    s2 = k * c**2 + rem**2
    s3 = k * c**3 + rem**3
    return 1.0 - 3.0 * s2 + 2.0 * s3


def compute_area(bi_xs: np.ndarray, multi_xs: np.ndarray) -> float:
    """Compute score from x-positions using Turán rows."""
    all_xs = np.concatenate([bi_xs, multi_xs])
    w = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in all_xs])
    return compute_score(w)


def turan_y_torch(x: torch.Tensor, k: torch.Tensor) -> torch.Tensor:
    kf = k.to(x.dtype)
    disc = 4.0 * kf * kf - 4.0 * kf * (kf + 1.0) * x
    disc = torch.clamp(disc, min=0.0)
    sqrt_disc = torch.sqrt(disc)
    c = (2.0 * kf + sqrt_disc) / (2.0 * kf * (kf + 1.0))
    c = torch.clamp(c, min=1.0 / (kf + 1.0), max=1.0 / kf)
    rem = torch.clamp(1.0 - kf * c, min=0.0)
    s2 = kf * c * c + rem * rem
    s3 = kf * c * c * c + rem * rem * rem
    return 1.0 - 3.0 * s2 + 2.0 * s3


def score_torch(raw: torch.Tensor, bi_xs: torch.Tensor,
                lo: torch.Tensor, hi: torch.Tensor,
                k_vec: torch.Tensor) -> torch.Tensor:
    xs = lo + (hi - lo) * torch.sigmoid(raw)
    sort_idx = torch.argsort(xs)
    xs_sorted = xs[sort_idx]
    k_sorted = k_vec[sort_idx]
    ys = turan_y_torch(xs_sorted, k_sorted)

    zero = torch.zeros(1, dtype=xs.dtype)
    one = torch.ones(1, dtype=xs.dtype)
    bi_ys = torch.zeros_like(bi_xs)

    xs_full = torch.cat([zero, bi_xs, xs_sorted, one])
    ys_full = torch.cat([zero, bi_ys, ys, one])

    hs = xs_full[1:] - xs_full[:-1]
    dys = ys_full[1:] - ys_full[:-1]
    y1 = ys_full[1:]
    y0 = ys_full[:-1]

    area_a = y1 * hs
    area_b = -dys * dys / 6.0 + y1 * hs
    area_c = y0 * hs + 1.5 * hs * hs
    area_per = torch.where(dys < 0, area_a,
                           torch.where(dys <= 3.0 * hs, area_b, area_c))
    area = area_per.sum()
    max_gap = hs.max()
    return -(area + 10.0 * max_gap)


def scallop_bounds(k: np.ndarray, eps: float = 1e-12):
    lo = 1.0 - 1.0 / k + eps
    hi = 1.0 - 1.0 / (k + 1) - eps
    return lo, hi


def inverse_sigmoid(xs, lo, hi):
    u = (xs - lo) / (hi - lo)
    u = np.clip(u, 1e-14, 1 - 1e-14)
    return np.log(u / (1 - u))


def lbfgs_optimize(multi_xs: np.ndarray, bi_xs: np.ndarray,
                   max_rounds: int = 60) -> tuple[np.ndarray, float]:
    """L-BFGS with strict scallop bounds."""
    k_np = assign_scallops(multi_xs)
    lo_np, hi_np = scallop_bounds(k_np)
    multi_clamped = np.clip(multi_xs, lo_np, hi_np)
    raw_np = inverse_sigmoid(multi_clamped, lo_np, hi_np)

    bi_t = torch.tensor(bi_xs, dtype=torch.float64)
    lo_t = torch.tensor(lo_np, dtype=torch.float64)
    hi_t = torch.tensor(hi_np, dtype=torch.float64)
    k_t = torch.tensor(k_np, dtype=torch.int64)
    raw = torch.tensor(raw_np, dtype=torch.float64, requires_grad=True)

    opt = torch.optim.LBFGS(
        [raw], lr=1.0, max_iter=40,
        tolerance_grad=1e-20, tolerance_change=1e-20,
        history_size=100, line_search_fn="strong_wolfe",
    )

    best_score = -float("inf")
    best_raw = raw.detach().clone()

    for r in range(max_rounds):
        def closure():
            opt.zero_grad()
            s = score_torch(raw, bi_t, lo_t, hi_t, k_t)
            loss = -s
            loss.backward()
            return loss
        loss = opt.step(closure)
        cur = -loss.item()
        if cur > best_score:
            best_score = cur
            best_raw = raw.detach().clone()

    with torch.no_grad():
        new_xs = lo_t + (hi_t - lo_t) * torch.sigmoid(best_raw)
        new_xs = torch.sort(new_xs).values.numpy()
    return new_xs, best_score


def create_allocation(alloc: dict, x_lo: float = 0.5, x_hi: float = 0.95) -> np.ndarray:
    """Create initial x-positions from scallop allocation."""
    xs = []
    for k in sorted(alloc.keys()):
        n = alloc[k]
        if n <= 0:
            continue
        lo = 1.0 - 1.0 / k
        hi = 1.0 - 1.0 / (k + 1)
        # Evenly space within scallop (with margins)
        margin = (hi - lo) * 0.01
        pts = np.linspace(lo + margin, hi - margin, n)
        xs.extend(pts)
    return np.sort(np.array(xs))


def get_current_allocation(multi_xs: np.ndarray) -> dict:
    """Count points per scallop."""
    ks = assign_scallops(multi_xs)
    alloc = {}
    for k in range(2, 20):
        alloc[k] = int(np.sum(ks == k))
    return alloc


def main():
    sol_path = RESULTS / "solution.json"
    bi_xs, multi_xs = load_xs(sol_path)
    init_score = compute_area(bi_xs, multi_xs)
    print(f"Initial: {init_score:.14f} ({len(multi_xs)} multipartite pts)")
    print(f"Target:  -0.71170119000000 (SOTA + 1e-5)")
    print(f"Gap:     {-0.71170119 - init_score:.2e}")
    print()

    # Get current allocation
    alloc = get_current_allocation(multi_xs)
    total = sum(alloc.values())
    print("Current scallop allocation:")
    for k in range(2, 20):
        if alloc[k] > 0:
            lo = 1.0 - 1.0 / k
            hi = 1.0 - 1.0 / (k + 1)
            width = hi - lo
            density = alloc[k] / width if width > 0 else 0
            print(f"  k={k:2d}: n={alloc[k]:3d}  x=[{lo:.6f},{hi:.6f}]  density={density:.0f}/unit")
    print(f"  Total: {total}")
    print()

    best_score = init_score
    best_multi = multi_xs.copy()

    # Phase 1: Re-polish current solution with aggressive L-BFGS
    print("=== Phase 1: Re-polish with aggressive L-BFGS ===")
    polished, torch_score = lbfgs_optimize(multi_xs, bi_xs, max_rounds=80)
    true_score = compute_area(bi_xs, polished)
    delta = true_score - init_score
    print(f"  torch={torch_score:.14f}  true={true_score:.14f}  delta={delta:+.2e}")
    if true_score > best_score + 1e-15:
        best_score = true_score
        best_multi = polished.copy()
        print("  ** Improved!")
    print()

    # Phase 2: Try scallop reallocation — move 1 point between each pair
    print("=== Phase 2: Scallop reallocation (move 1 pt between pairs) ===")
    t0 = time.time()
    n_tried = 0
    n_improved = 0

    scallops = [k for k in range(2, 20) if alloc[k] > 0]

    for src_k in scallops:
        if alloc[src_k] <= 1:  # keep at least 1 point per scallop
            continue
        for dst_k in range(2, 20):
            if dst_k == src_k:
                continue

            # Create new allocation
            new_alloc = alloc.copy()
            new_alloc[src_k] -= 1
            new_alloc[dst_k] = new_alloc.get(dst_k, 0) + 1

            # Create initial positions from new allocation
            new_multi = create_allocation(new_alloc)
            if len(new_multi) != total:
                continue

            # Quick check: score without L-BFGS
            quick_score = compute_area(bi_xs, new_multi)

            # Run L-BFGS
            try:
                opt_multi, opt_torch = lbfgs_optimize(new_multi, bi_xs, max_rounds=30)
                opt_true = compute_area(bi_xs, opt_multi)
            except Exception:
                opt_true = -float("inf")

            n_tried += 1
            if opt_true > best_score + 1e-15:
                best_score = opt_true
                best_multi = opt_multi.copy()
                n_improved += 1
                print(f"  {src_k}->{dst_k}: {opt_true:.14f} NEW BEST (+{opt_true-init_score:.3e})")

            if n_tried % 50 == 0:
                elapsed = time.time() - t0
                print(f"  ... {n_tried} tried, {n_improved} improved, {elapsed:.0f}s elapsed")

    elapsed = time.time() - t0
    print(f"  Done: {n_tried} tried, {n_improved} improved, {elapsed:.0f}s")
    print()

    # Phase 3: Try moving 2 points
    print("=== Phase 3: Move 2 points (top scallop pairs) ===")
    t0 = time.time()
    n_tried2 = 0

    for src_k in scallops:
        if alloc[src_k] <= 2:
            continue
        for dst_k in range(2, 20):
            if dst_k == src_k:
                continue
            new_alloc = alloc.copy()
            new_alloc[src_k] -= 2
            new_alloc[dst_k] = new_alloc.get(dst_k, 0) + 2
            new_multi = create_allocation(new_alloc)
            if len(new_multi) != total:
                continue
            try:
                opt_multi, _ = lbfgs_optimize(new_multi, bi_xs, max_rounds=30)
                opt_true = compute_area(bi_xs, opt_multi)
            except Exception:
                opt_true = -float("inf")
            n_tried2 += 1
            if opt_true > best_score + 1e-15:
                best_score = opt_true
                best_multi = opt_multi.copy()
                print(f"  {src_k}->{dst_k} (x2): {opt_true:.14f} NEW BEST (+{opt_true-init_score:.3e})")

    print(f"  Done: {n_tried2} tried, {time.time()-t0:.0f}s")
    print()

    # Phase 4: Random from-scratch with different allocations
    print("=== Phase 4: Random allocations (20 seeds) ===")
    t0 = time.time()
    rng = np.random.default_rng(42)

    for seed in range(20):
        # Random allocation proportional to scallop width
        widths = np.array([1.0/(k*(k+1)) for k in range(2, 20)])
        # Add noise to the proportions
        props = widths + rng.exponential(0.001, size=len(widths))
        props = props / props.sum()
        counts = np.round(props * total).astype(int)
        # Adjust to sum to total
        diff = total - counts.sum()
        for _ in range(abs(diff)):
            if diff > 0:
                idx = rng.integers(len(counts))
                counts[idx] += 1
            elif diff < 0:
                idx = rng.choice(np.where(counts > 1)[0])
                counts[idx] -= 1

        rand_alloc = {k + 2: int(c) for k, c in enumerate(counts)}
        new_multi = create_allocation(rand_alloc)
        if len(new_multi) != total:
            continue
        try:
            opt_multi, _ = lbfgs_optimize(new_multi, bi_xs, max_rounds=40)
            opt_true = compute_area(bi_xs, opt_multi)
        except Exception:
            opt_true = -float("inf")
        if opt_true > best_score + 1e-15:
            best_score = opt_true
            best_multi = opt_multi.copy()
            print(f"  seed={seed}: {opt_true:.14f} NEW BEST (+{opt_true-init_score:.3e})")
        elif seed % 5 == 0:
            print(f"  seed={seed}: {opt_true:.14f} (best={best_score:.14f})")

    print(f"  Done: {time.time()-t0:.0f}s")
    print()

    # Phase 5: Full-weight optimization with PyTorch (no Turán constraint)
    print("=== Phase 5: Free weight optimization (no Turán constraint) ===")
    all_xs = np.concatenate([bi_xs, best_multi])
    w_init = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in all_xs])
    w_t = torch.tensor(w_init, dtype=torch.float64, requires_grad=True)

    def score_from_weights(ww):
        ww_pos = torch.clamp(ww, min=0.0)
        ww_norm = ww_pos / ww_pos.sum(dim=1, keepdim=True)
        s2 = (ww_norm ** 2).sum(dim=1)
        s3 = (ww_norm ** 3).sum(dim=1)
        xs = 1.0 - s2
        ys = 1.0 - 3.0 * s2 + 2.0 * s3
        sort_idx = torch.argsort(xs)
        xs_s = xs[sort_idx]
        ys_s = ys[sort_idx]
        zero = torch.zeros(1, dtype=ww.dtype)
        one = torch.ones(1, dtype=ww.dtype)
        xs_full = torch.cat([zero, xs_s, one])
        ys_full = torch.cat([zero, ys_s, one])
        hs = xs_full[1:] - xs_full[:-1]
        dys = ys_full[1:] - ys_full[:-1]
        y1 = ys_full[1:]
        y0 = ys_full[:-1]
        area_a = y1 * hs
        area_b = -dys * dys / 6.0 + y1 * hs
        area_c = y0 * hs + 1.5 * hs * hs
        area_per = torch.where(dys < 0, area_a,
                               torch.where(dys <= 3.0 * hs, area_b, area_c))
        return -(area_per.sum() + 10.0 * hs.max())

    opt_w = torch.optim.LBFGS(
        [w_t], lr=0.001, max_iter=20,
        tolerance_grad=1e-20, tolerance_change=1e-20,
        history_size=50, line_search_fn="strong_wolfe",
    )

    best_w_score = -float("inf")
    for r in range(30):
        def closure():
            opt_w.zero_grad()
            s = score_from_weights(w_t)
            (-s).backward()
            return -s
        loss = opt_w.step(closure)
        cur = -loss.item()
        if cur > best_w_score:
            best_w_score = cur

    # Verify with numpy evaluator
    w_final = torch.clamp(w_t.detach(), min=0.0).numpy()
    w_final = w_final / w_final.sum(axis=1, keepdims=True)
    final_score = compute_score(w_final)
    print(f"  Free-weight L-BFGS: torch={best_w_score:.14f}  true={final_score:.14f}")
    if final_score > best_score + 1e-15:
        best_score = final_score
        print("  ** Improved via free weights!")
    print()

    # Summary
    print("=" * 60)
    print(f"Initial:  {init_score:.14f}")
    print(f"Best:     {best_score:.14f}")
    print(f"Delta:    {best_score - init_score:+.3e}")
    print(f"Target:   -0.71170119000000")
    print(f"To target: {-0.71170119 - best_score:.3e}")
    print()

    if best_score > init_score + 1e-13:
        # Save improved solution
        all_xs = np.concatenate([bi_xs, best_multi])
        w_best = np.array([turan_row(np.clip(x, 0.0, 0.95)) for x in all_xs])
        sol = {"weights": w_best.tolist()}
        out = RESULTS / "solution-extreme.json"
        with open(out, "w") as f:
            json.dump(sol, f)
        print(f"Saved improved solution to {out}")
        # Also update main solution
        main_out = RESULTS / "solution.json"
        with open(main_out, "w") as f:
            json.dump(sol, f)
        print(f"Updated {main_out}")
    else:
        print("No improvement found. The 500-pt Turán placement appears truly optimal.")


if __name__ == "__main__":
    main()
