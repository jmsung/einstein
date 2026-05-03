"""Branch-and-bound atom solver for P19 Difference Bases.

Goal: find a 90-mark atom A ⊆ [0, S_max] with internal coverage c(A) ≥ target_v.
If found, plug into Kronecker B = A ⊕ 8011·{0,1,4,6} to beat the SOTA score of
2.6390274695066 (v=49109, k=360).

Algorithm — goal-directed DFS with aggressive pruning:
- At each node, find smallest uncovered d* in [1, target_v]
- Branch only on "new mark p = a + d* for some existing a" (branching factor ≤ k_current)
- Prune on cardinality feasibility, coverage capacity, d* reachability
- Iterative DFS with numba-compiled inner loop

Two modes:
    direct  — search from scratch starting at A = [0]
    lns     — fix (90 - w) marks from SOTA, search for w replacement marks
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path

import numpy as np
import numba as nb

SOTA_PATH = (
    Path.home()
    / "projects/einstein/mb/tracking/problem-19-difference-bases"
    / "solutions/sota-rank01-CHRONOS-score2.6390274695.json"
)
RESULTS_DIR = Path("results/problem-19-difference-bases")

LAMBDA = 8011
R_KRON = [0, 1, 4, 6]

# Bitset sized for target_v up to ~1100
N_WORDS = 18  # 18 * 64 = 1152 bits


@nb.njit(cache=True, boundscheck=False, nogil=True)
def bit_set(bm, d):
    bm[d >> 6] |= np.int64(1) << (d & 63)


@nb.njit(cache=True, boundscheck=False, nogil=True)
def bit_get(bm, d):
    return (bm[d >> 6] >> (d & 63)) & 1


@nb.njit(cache=True, boundscheck=False, nogil=True)
def bit_copy(src, dst):
    for i in range(N_WORDS):
        dst[i] = src[i]


@nb.njit(cache=True, boundscheck=False, nogil=True)
def bit_popcount(bm, up_to):
    """Count set bits in positions [1, up_to]."""
    c = 0
    for d in range(1, up_to + 1):
        c += (bm[d >> 6] >> (d & 63)) & 1
    return int(c)


@nb.njit(cache=True, boundscheck=False, nogil=True)
def bit_lowest_unset(bm, start, end):
    """Smallest d in [start, end] with bit not set; -1 if all set."""
    for d in range(start, end + 1):
        if not ((bm[d >> 6] >> (d & 63)) & 1):
            return d
    return -1


@nb.njit(cache=True, boundscheck=False, nogil=True)
def compute_coverage(marks, n_marks, target_v, out_bm):
    """Fill out_bm with bits for every d in [1, target_v] that appears as a
    positive difference in marks[:n_marks]."""
    for i in range(N_WORDS):
        out_bm[i] = np.int64(0)
    for i in range(1, n_marks):
        ai = marks[i]
        for j in range(i):
            d = ai - marks[j]
            if 1 <= d <= target_v:
                bit_set(out_bm, d)


@nb.njit(cache=True, boundscheck=False, nogil=True)
def add_mark_coverage(marks, n_marks, p, target_v, in_bm, out_bm):
    """Copy in_bm to out_bm then set bits for diffs between p and marks[:n_marks]."""
    for i in range(N_WORDS):
        out_bm[i] = in_bm[i]
    for j in range(n_marks):
        d = p - marks[j]
        if 1 <= d <= target_v:
            bit_set(out_bm, d)


@nb.njit(cache=True, nogil=True)
def bnb_direct_batch(
    marks,
    covered,
    partner_idx,
    start_level,
    k_target,
    target_v,
    S_max,
    budget_nodes,
):
    """Goal-directed BnB from scratch, run for budget_nodes then return.

    Mutates marks/covered/partner_idx in-place. Caller resumes by calling again.

    Returns (status, level_out, nodes_done).
        status: 0 = in-progress (budget hit), 1 = solution found, 4 = search tree exhausted.
    """
    level = start_level
    nodes = 0
    status = 0

    while level >= 1:
        nodes += 1
        if nodes >= budget_nodes:
            status = 0
            break

        # Check if complete
        if level == k_target:
            last_cov = covered[level - 1]
            all_covered = True
            for d in range(1, target_v + 1):
                if not ((last_cov[d >> 6] >> (d & 63)) & 1):
                    all_covered = False
                    break
            if all_covered:
                status = 1
                break
            # Backtrack
            level -= 1
            continue

        # Pruning 1: cardinality — can we still fit k_target marks?
        remaining = k_target - level
        last_mark = marks[level - 1]
        if last_mark + remaining > S_max:
            # Can't fit; backtrack
            partner_idx[level] = 0
            level -= 1
            continue

        # Current coverage (from covered[level - 1], the state after placing level marks)
        cov = covered[level - 1]

        # Find smallest uncovered d
        d_star = -1
        for d in range(1, target_v + 1):
            if not ((cov[d >> 6] >> (d & 63)) & 1):
                d_star = d
                break

        if d_star == -1:
            # All covered. Fill remaining with consecutive marks from last+1.
            # We just need to reach k_target marks without breaking anything.
            # Since coverage can only grow, any addition works.
            # Take the smallest valid next mark.
            p = last_mark + 1
            if p + (remaining - 1) > S_max:
                level -= 1
                partner_idx[level] = 0
                continue
            marks[level] = p
            add_mark_coverage(marks, level, p, target_v, cov, covered[level])
            level += 1
            partner_idx[level] = 0
            continue

        # Pruning 2: d_star reachability — need a + d_star > last_mark for some
        # existing a, so max(existing) = last_mark; we need some a with a + d_star ≤ S_max
        # and a + d_star > last_mark, i.e., a > last_mark - d_star.
        # Also need a + d_star ≤ S_max.
        # Simpler: find valid pair partners in marks[0..level-1] with
        # a > last_mark - d_star AND a + d_star ≤ S_max.

        # Pruning 3: coverage capacity
        uncovered_count = 0
        for d in range(1, target_v + 1):
            if not ((cov[d >> 6] >> (d & 63)) & 1):
                uncovered_count += 1
        # Max new diffs from remaining marks: each new mark creates ≤ level + i new pair diffs
        # (where i is the number of already-new marks added). Total ≤ Σ_{i=0}^{remaining-1}(level+i)
        max_new_pairs = 0
        for i in range(remaining):
            max_new_pairs += level + i
        if max_new_pairs < uncovered_count:
            # Infeasible
            level -= 1
            partner_idx[level] = 0
            continue

        # Branch: try pair partners a in marks[:level] (in sorted order, increasing a)
        # such that p_new = a + d_star > last_mark and ≤ S_max.
        # We iterate by partner_idx[level] which tracks the next a to try.

        found_next = False
        while partner_idx[level] < level:
            a_idx = partner_idx[level]
            a = marks[a_idx]
            partner_idx[level] += 1
            p_new = a + d_star
            if p_new > last_mark and p_new <= S_max - (remaining - 1):
                # Valid branch
                marks[level] = p_new
                add_mark_coverage(marks, level, p_new, target_v, cov, covered[level])
                level += 1
                partner_idx[level] = 0
                found_next = True
                break

        if not found_next:
            # Exhausted branches at this level
            partner_idx[level] = 0
            level -= 1

    if level < 1 and status == 0:
        status = 4  # tree exhausted
    return status, level, nodes


@nb.njit(cache=True, nogil=True)
def bnb_lns_batch(
    combined,
    n_fixed,
    covered,
    uncov_cache,
    d_star_cache,
    partner_idx,
    start_level,
    k_target,
    target_v,
    S_max,
    budget_nodes,
):
    """LNS batch BnB with incremental counters.

    uncov_cache[level]: number of uncovered diffs in [1, target_v] at that level
    d_star_cache[level]: smallest uncovered diff at that level (or target_v+1 if none)
    Both are maintained incrementally — no per-node full bit scans.

    Returns (status, level_out, nodes_done).
        status: 0 = in-progress, 1 = solution, 4 = tree exhausted.
    """
    n_new_target = k_target - n_fixed
    level = start_level
    nodes = 0
    status = 0

    while level >= 0:
        nodes += 1
        if nodes >= budget_nodes:
            status = 0
            break

        if level == n_new_target:
            if uncov_cache[level] == 0:
                status = 1
                break
            level -= 1
            continue

        total_placed = n_fixed + level
        cov = covered[level]
        u = uncov_cache[level]
        d_star = d_star_cache[level]

        if u == 0:
            # All covered. Fill remaining with smallest unused position.
            picked = -1
            p_try = 0
            while p_try <= S_max:
                in_combined = False
                for i in range(total_placed):
                    if combined[i] == p_try:
                        in_combined = True
                        break
                if not in_combined:
                    picked = p_try
                    break
                p_try += 1
            if picked == -1:
                level -= 1
                if level >= 0:
                    partner_idx[level + 1] = 0
                continue
            combined[total_placed] = picked
            # Copy bitmask
            for i in range(N_WORDS):
                covered[level + 1, i] = cov[i]
            # Coverage doesn't drop; new marks just add pairs (all bits already set)
            new_bits = 0
            for j in range(total_placed):
                diff = picked - combined[j]
                if diff < 0:
                    diff = -diff
                if 1 <= diff <= target_v:
                    word_idx = diff >> 6
                    mask = np.int64(1) << (diff & 63)
                    if not (covered[level + 1, word_idx] & mask):
                        covered[level + 1, word_idx] |= mask
                        new_bits += 1
            uncov_cache[level + 1] = u - new_bits
            d_star_cache[level + 1] = d_star  # unchanged (d_star was target_v+1 sentinel)
            level += 1
            partner_idx[level] = 0
            continue

        # Pruning: coverage capacity
        remaining = n_new_target - level
        max_new_pairs = 0
        for i in range(remaining):
            max_new_pairs += total_placed + i
        if max_new_pairs < u:
            level -= 1
            if level >= 0:
                partner_idx[level + 1] = 0
            continue

        # Branch: pair partners for d_star
        found_next = False
        while partner_idx[level] < total_placed * 2:
            choice = partner_idx[level]
            partner_idx[level] += 1
            a_idx = choice // 2
            sign = choice % 2
            a = combined[a_idx]
            if sign == 0:
                p_new = a + d_star
            else:
                p_new = a - d_star
            if p_new < 0 or p_new > S_max:
                continue
            already = False
            for i in range(total_placed):
                if combined[i] == p_new:
                    already = True
                    break
            if already:
                continue

            # Accept branch — build new bitmask incrementally
            combined[total_placed] = p_new
            for i in range(N_WORDS):
                covered[level + 1, i] = cov[i]
            new_bits = 0
            for j in range(total_placed):
                diff = p_new - combined[j]
                if diff < 0:
                    diff = -diff
                if 1 <= diff <= target_v:
                    word_idx = diff >> 6
                    mask = np.int64(1) << (diff & 63)
                    if not (covered[level + 1, word_idx] & mask):
                        covered[level + 1, word_idx] |= mask
                        new_bits += 1
            uncov_cache[level + 1] = u - new_bits

            # Update d_star: it only increases. Scan from current d_star.
            new_d_star = d_star
            cov_next = covered[level + 1]
            while new_d_star <= target_v and ((cov_next[new_d_star >> 6] >> (new_d_star & 63)) & 1):
                new_d_star += 1
            if new_d_star > target_v:
                new_d_star = target_v + 1
            d_star_cache[level + 1] = new_d_star

            level += 1
            partner_idx[level] = 0
            found_next = True
            break

        if not found_next:
            partner_idx[level] = 0
            level -= 1

    if level < 0 and status == 0:
        status = 4
    return status, level, nodes


def load_sota_atom():
    sol = json.loads(SOTA_PATH.read_text())
    B = sorted(set([0] + sol["set"]))
    return [b for b in B if b <= 6967]


def verify_atom(A, target_v):
    """Return c(A) = longest contiguous prefix of positive diffs."""
    diffs = set()
    for i in range(len(A)):
        for j in range(i):
            diffs.add(A[i] - A[j])
    v = 0
    while (v + 1) in diffs:
        v += 1
    return v


def run_direct(args):
    print(f"Direct BnB: k={args.k}, target_v={args.target_v}, S_max={args.S_max}",
          flush=True)

    # Initialize state
    marks = np.zeros(args.k, dtype=np.int32)
    covered = np.zeros((args.k + 1, N_WORDS), dtype=np.int64)
    partner_idx = np.zeros(args.k + 1, dtype=np.int32)
    marks[0] = 0
    level = 1

    t_start = time.time()
    total_nodes = 0
    batch = 5_000_000
    print("JIT compile (first call takes ~5s)...", flush=True)
    while True:
        status, level, nodes = bnb_direct_batch(
            marks, covered, partner_idx, level,
            args.k, args.target_v, args.S_max, batch,
        )
        total_nodes += nodes
        wall = time.time() - t_start
        if status == 1:
            A = sorted(int(x) for x in marks)
            c = verify_atom(A, args.target_v)
            print(f"Found atom: k={len(A)}, c(A)={c}, "
                  f"nodes={total_nodes:,}, wall={wall:.1f}s", flush=True)
            return A
        if status == 4:
            print(f"Tree exhausted, no solution. "
                  f"nodes={total_nodes:,}, wall={wall:.1f}s", flush=True)
            return None
        # In progress
        print(f"  ... {total_nodes:,} nodes, {wall:.1f}s, level={level}",
              flush=True)
        if wall > args.time_limit:
            print(f"Time limit hit. nodes={total_nodes:,}, wall={wall:.1f}s",
                  flush=True)
            return None
        if total_nodes > args.max_nodes:
            print(f"Node limit hit. nodes={total_nodes:,}", flush=True)
            return None


def run_lns(args):
    A_sota = load_sota_atom()
    k = len(A_sota)
    assert k == 90
    print(f"LNS: remove {args.w} marks from SOTA (k={k}), search replacements",
          flush=True)
    print(f"target_v={args.target_v}, S_max={args.S_max}", flush=True)

    rng = random.Random(args.seed)
    found = None
    t_overall = time.time()
    for trial in range(args.trials):
        if time.time() - t_overall > args.time_limit:
            print(f"Overall time limit hit at trial {trial}", flush=True)
            break

        remove_idx = sorted(rng.sample(range(k), args.w))
        fixed = [A_sota[i] for i in range(k) if i not in remove_idx]
        n_fixed = len(fixed)
        n_new_target = k - n_fixed

        combined = np.zeros(k, dtype=np.int32)
        for i, v in enumerate(fixed):
            combined[i] = v

        covered = np.zeros((n_new_target + 1, N_WORDS), dtype=np.int64)
        for i in range(1, n_fixed):
            for j in range(i):
                d = fixed[i] - fixed[j]
                if 1 <= d <= args.target_v:
                    covered[0, d >> 6] |= np.int64(1) << (d & 63)

        # Initialize uncov + d_star caches at level 0
        uncov_cache = np.zeros(n_new_target + 1, dtype=np.int32)
        d_star_cache = np.zeros(n_new_target + 1, dtype=np.int32)
        covered0_count = 0
        for d in range(1, args.target_v + 1):
            if (covered[0, d >> 6] >> (d & 63)) & 1:
                covered0_count += 1
        uncov_cache[0] = args.target_v - covered0_count
        d0 = 1
        while d0 <= args.target_v and ((covered[0, d0 >> 6] >> (d0 & 63)) & 1):
            d0 += 1
        d_star_cache[0] = d0 if d0 <= args.target_v else args.target_v + 1

        partner_idx = np.zeros(n_new_target + 1, dtype=np.int32)

        uncovered_before = int(uncov_cache[0])

        t_trial = time.time()
        total_nodes = 0
        level = 0
        status = 0
        batch = 2_000_000
        while True:
            status, level, nodes = bnb_lns_batch(
                combined, n_fixed, covered, uncov_cache, d_star_cache,
                partner_idx, level,
                k, args.target_v, args.S_max, batch,
            )
            total_nodes += nodes
            wall_trial = time.time() - t_trial
            if status == 1 or status == 4:
                break
            if wall_trial > args.per_trial_time:
                status = 2  # per-trial timeout
                break

        msg = (f"Trial {trial + 1}/{args.trials}: rm={remove_idx[:5]} "
               f"unc_before={uncovered_before} status={status} "
               f"nodes={total_nodes:,} wall={wall_trial:.1f}s")
        print(msg, flush=True)
        if status == 1:
            A = sorted(int(combined[i]) for i in range(k))
            c = verify_atom(A, args.target_v)
            print(f"*** Candidate atom! c(A)={c} ***", flush=True)
            if c >= args.target_v:
                found = A
                break
    return found


def kronecker_score(A):
    B = sorted(a + LAMBDA * r for a in A for r in R_KRON)
    diffs = set()
    for i in range(len(B)):
        for j in range(i):
            diffs.add(B[i] - B[j])
    v = 0
    while (v + 1) in diffs:
        v += 1
    score = len(B) ** 2 / v if v > 0 else float("inf")
    return B, v, score


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["direct", "lns"], default="lns")
    parser.add_argument("--target-v", type=int, default=1044)
    parser.add_argument("--S-max", type=int, default=6967)
    parser.add_argument("--k", type=int, default=90)
    parser.add_argument("--time-limit", type=int, default=60,
                        help="Total time limit (direct mode)")
    parser.add_argument("--max-nodes", type=int, default=1_000_000_000)
    parser.add_argument("--w", type=int, default=5, help="LNS swap width")
    parser.add_argument("--trials", type=int, default=100, help="LNS random trials")
    parser.add_argument("--per-trial-time", type=int, default=10,
                        help="Time per LNS trial (seconds)")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.mode == "direct":
        A = run_direct(args)
    else:
        A = run_lns(args)

    if A is not None:
        B, v, score = kronecker_score(A)
        sota = 360 ** 2 / 49109
        print(f"Kronecker B: k={len(B)}, v={v}, score={score:.16f}", flush=True)
        print(f"Δ vs SOTA: {score - sota:+.6e}", flush=True)
        if v > 49109:
            RESULTS_DIR.mkdir(parents=True, exist_ok=True)
            out = RESULTS_DIR / f"atom-bnb-{args.mode}-v{v}-score{score:.10f}.json"
            out.write_text(json.dumps({
                "set": [int(b) for b in B],
                "atom": [int(a) for a in A],
                "score": float(score),
                "k": len(B),
                "v": int(v),
                "mode": args.mode,
            }, indent=2))
            print(f"Wrote {out}", flush=True)


if __name__ == "__main__":
    main()
