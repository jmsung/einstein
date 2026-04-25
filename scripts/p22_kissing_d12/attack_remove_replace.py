"""Remove-and-replace attack: remove 1 of CHRONOS's 840, add 2 new optimized.

Theory:
- CHRONOS 840 + 1 duplicate → score 2.0.
- Remove v_i, add v_a and v_b. 839 core is still kissing (score 0 among core).
- Pairs (v_a, core_j), (v_b, core_j), (v_a, v_b) — minimize total hinge.
- If we can place v_a and v_b near v_i's "hole" with smaller total overlap
  than CHRONOS's single duplicate, we beat 2.0.

Massive parallel via MPS: for each v_i (try all 840), sample B random
(v_a, v_b) pairs near v_i, score on GPU, refine top-K on CPU.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch

sys.path.insert(0, "src")

RESULTS_DIR = Path("results/p22_kissing_d12")
CHRONOS_PATH = RESULTS_DIR / "sota_best_chronos_rank1_id2081.json"


def load_core() -> np.ndarray:
    data = json.loads(CHRONOS_PATH.read_text())
    v = np.array(data["vectors"], dtype=np.float64)
    seen = {}
    keep = []
    for i, row in enumerate(v):
        key = tuple(row.tolist())
        if key not in seen:
            seen[key] = i
            keep.append(i)
    return v[keep] / np.linalg.norm(v[keep], axis=1, keepdims=True)


def score_pair_gpu(core_t: torch.Tensor, Va: torch.Tensor, Vb: torch.Tensor) -> torch.Tensor:
    """Core-remove ignored here — pass full core with v_i already removed.

    core_t: (839, 12). Va, Vb: (B, 12) each. Returns (B,) scores.
    """
    # gamma_a = Va @ core.T, gamma_b = Vb @ core.T
    ga = Va @ core_t.t()
    gb = Vb @ core_t.t()
    gab = (Va * Vb).sum(dim=1, keepdim=True)  # (B, 1)
    # Pair penalties
    def pen(g):
        g = g.clamp(-1.0, 1.0)
        dist = 2.0 * torch.sqrt(2.0 * (1.0 - g))
        return (2.0 - dist).clamp(min=0.0)
    pen_a = pen(ga).sum(dim=1)
    pen_b = pen(gb).sum(dim=1)
    pen_ab = pen(gab).squeeze(-1)
    return pen_a + pen_b + pen_ab


def score_pair_cpu(core: np.ndarray, va: np.ndarray, vb: np.ndarray) -> float:
    va = va / np.linalg.norm(va)
    vb = vb / np.linalg.norm(vb)
    ga = core @ va
    gb = core @ vb
    gab = va @ vb
    def pen(g):
        g = np.clip(g, -1.0, 1.0)
        dist = 2.0 * np.sqrt(2.0 * (1.0 - g))
        return np.maximum(0.0, 2.0 - dist)
    return float(pen(ga).sum() + pen(gb).sum() + pen(np.array([gab])).sum())


def pair_rgd_cpu(core: np.ndarray, va0: np.ndarray, vb0: np.ndarray, steps: int, lr: float) -> tuple[np.ndarray, np.ndarray, float]:
    va = va0 / np.linalg.norm(va0)
    vb = vb0 / np.linalg.norm(vb0)
    best_va, best_vb = va.copy(), vb.copy()
    best_s = score_pair_cpu(core, va, vb)
    vel_a = np.zeros_like(va)
    vel_b = np.zeros_like(vb)
    cur_lr = lr
    for t in range(steps):
        # Gradients
        ga = core @ va
        mask_a = ga > 0.5 + 1e-15
        grad_va_amb = np.zeros_like(va)
        if np.any(mask_a):
            g = np.clip(ga[mask_a], -1.0, 1.0 - 1e-15)
            dh = np.sqrt(2.0) / np.sqrt(1.0 - g)
            grad_va_amb = (dh[:, None] * core[mask_a]).sum(axis=0)
        # Include pair (va, vb)
        gab = va @ vb
        if gab > 0.5 + 1e-15:
            g = np.clip(gab, -1.0, 1.0 - 1e-15)
            dh_ab = np.sqrt(2.0) / np.sqrt(1.0 - g)
            grad_va_amb += dh_ab * vb
        grad_va = grad_va_amb - (grad_va_amb @ va) * va

        gb = core @ vb
        mask_b = gb > 0.5 + 1e-15
        grad_vb_amb = np.zeros_like(vb)
        if np.any(mask_b):
            g = np.clip(gb[mask_b], -1.0, 1.0 - 1e-15)
            dh = np.sqrt(2.0) / np.sqrt(1.0 - g)
            grad_vb_amb = (dh[:, None] * core[mask_b]).sum(axis=0)
        if gab > 0.5 + 1e-15:
            grad_vb_amb += dh_ab * va
        grad_vb = grad_vb_amb - (grad_vb_amb @ vb) * vb

        vel_a = 0.9 * vel_a + grad_va
        vel_b = 0.9 * vel_b + grad_vb
        va = va - cur_lr * vel_a
        vb = vb - cur_lr * vel_b
        va /= np.linalg.norm(va)
        vb /= np.linalg.norm(vb)
        cur_lr *= 0.999
        s = score_pair_cpu(core, va, vb)
        if s < best_s:
            best_s = s
            best_va = va.copy()
            best_vb = vb.copy()
    return best_va, best_vb, best_s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-remove", type=int, default=10, help="Try removing first K core vectors")
    ap.add_argument("--n-samples-per-remove", type=int, default=2_000_000)
    ap.add_argument("--batch", type=int, default=200_000)
    ap.add_argument("--top-k", type=int, default=100)
    ap.add_argument("--refine-steps", type=int, default=2000)
    ap.add_argument("--refine-lr", type=float, default=5e-4)
    ap.add_argument("--seed", type=int, default=20260425)
    args = ap.parse_args()

    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Device: {device}", flush=True)
    dtype = torch.float32

    core_full = load_core()
    print(f"Core: {core_full.shape}", flush=True)

    best_overall = {"score": 2.0, "rem_i": None, "va": None, "vb": None}

    for rem_i in range(args.n_remove):
        core = np.delete(core_full, rem_i, axis=0)
        core_t = torch.tensor(core, dtype=dtype, device=device)
        v_removed = core_full[rem_i]

        print(f"\n=== Remove core[{rem_i}] ===", flush=True)

        gen = torch.Generator(device=device).manual_seed(args.seed + rem_i)
        top_scores = torch.full((args.top_k,), float("inf"), device=device, dtype=dtype)
        top_va = torch.zeros((args.top_k, 12), device=device, dtype=dtype)
        top_vb = torch.zeros((args.top_k, 12), device=device, dtype=dtype)

        total = args.n_samples_per_remove
        n_batches = (total + args.batch - 1) // args.batch
        t0 = time.time()

        # v_removed seed: perturbations of v_removed for v_a and v_b
        v_rem_t = torch.tensor(v_removed, dtype=dtype, device=device)
        for b in range(n_batches):
            B = min(args.batch, total - b * args.batch)
            # Sample v_a near v_removed + small random perturbation
            # Mix: half random, half v_removed-perturbed
            half = B // 2
            va_rand = torch.randn(half, 12, device=device, dtype=dtype, generator=gen)
            vb_rand = torch.randn(half, 12, device=device, dtype=dtype, generator=gen)

            pert_scale = 0.3
            va_pert = v_rem_t[None] + pert_scale * torch.randn(B - half, 12, device=device, dtype=dtype, generator=gen)
            vb_pert = v_rem_t[None] + pert_scale * torch.randn(B - half, 12, device=device, dtype=dtype, generator=gen)

            Va = torch.cat([va_rand, va_pert])
            Vb = torch.cat([vb_rand, vb_pert])
            Va = Va / Va.norm(dim=1, keepdim=True)
            Vb = Vb / Vb.norm(dim=1, keepdim=True)

            scores = score_pair_gpu(core_t, Va, Vb)
            combined_s = torch.cat([top_scores, scores])
            combined_va = torch.cat([top_va, Va])
            combined_vb = torch.cat([top_vb, Vb])
            idx = torch.topk(combined_s, args.top_k, largest=False).indices
            top_scores = combined_s[idx]
            top_va = combined_va[idx]
            top_vb = combined_vb[idx]

        elapsed = time.time() - t0
        best_gpu = top_scores.min().item()
        print(f"  GPU phase: {total} samples in {elapsed:.1f}s  best={best_gpu:.6f}", flush=True)

        # Refine top-K
        top_scores_cpu = top_scores.cpu().numpy().astype(np.float64)
        top_va_cpu = top_va.cpu().numpy().astype(np.float64)
        top_vb_cpu = top_vb.cpu().numpy().astype(np.float64)
        order = np.argsort(top_scores_cpu)
        best_refined_s = np.inf
        best_refined_va, best_refined_vb = None, None
        for i in order[:args.top_k]:
            va_opt, vb_opt, s_opt = pair_rgd_cpu(core, top_va_cpu[i], top_vb_cpu[i], args.refine_steps, args.refine_lr)
            if s_opt < best_refined_s:
                best_refined_s = s_opt
                best_refined_va = va_opt
                best_refined_vb = vb_opt

        print(f"  refined best: {best_refined_s:.12f}", flush=True)
        if best_refined_s < best_overall["score"]:
            best_overall = {
                "score": best_refined_s,
                "rem_i": rem_i,
                "va": best_refined_va.tolist(),
                "vb": best_refined_vb.tolist(),
            }
            print(f"  >>> NEW BEST: {best_refined_s!r} (rem_i={rem_i})", flush=True)

    print(f"\n=== FINAL ===", flush=True)
    print(f"Best: {best_overall['score']!r}  rem_i={best_overall['rem_i']}", flush=True)
    if best_overall["va"] is not None:
        core_final = np.delete(core_full, best_overall["rem_i"], axis=0)
        vectors = np.vstack([core_final, np.array([best_overall["va"]]), np.array([best_overall["vb"]])])
        out = {
            "method": "remove_replace",
            "best_score": best_overall["score"],
            "rem_i": best_overall["rem_i"],
            "vectors": vectors.tolist(),
        }
        json.dump(out, open(RESULTS_DIR / "attack_remove_replace.json", "w"))


if __name__ == "__main__":
    main()
