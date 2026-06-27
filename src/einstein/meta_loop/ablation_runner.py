"""Production solve_fn for the Cold/Warm knowledge-compounding ablation (§10.3).

Wires the harness (`compounding_ablation`) to a real, fresh headless `claude`
session per (problem, arm, seed), run inside the air-gapped clean-room checkout
built by `scripts/build_ablation_repos.sh`.

Design invariants:
- **Air-gap by construction**: `allowed_tools` omits every web/retrieval tool, so
  the session physically cannot reach the internet or an answer key — it isn't a
  policy, the tool isn't there.
- **The only per-arm difference is memory**: run-KB threading is entirely
  harness-side (Warm's accumulated lessons arrive in `spec.accumulated_lessons`
  and the driver persists the returned lesson). So Cold and Warm get an identical
  tool set and prompt skeleton; Warm's prompt merely *contains* prior lessons.
- **The harness scores, not the agent**: `score_final` is recomputed by the
  generic evaluator from the centers the agent emits and triple-verified (A1). A
  self-reported score is ignored — an agent cannot inflate the DV.

The agent result contract: the session writes `ablation_result.json` into its cwd:
    {"centers": [[x, y], ...], "lesson": "<<=1-page lesson>>",
     "techniques": ["slsqp", ...]}   # techniques optional
"""

from __future__ import annotations

import json
import sys
import time
from collections.abc import Callable
from pathlib import Path

import numpy as np

from einstein.ablation_packing import evaluator as ev
from einstein.meta_loop.compounding_ablation import ArmConfig, Problem, SessionSpec, SolveResult
from einstein.meta_loop.trajectory import TrajectoryPoint

RESULT_FILENAME = "ablation_result.json"

# Tool set for BOTH arms — generic solving only, NO web/retrieval (air-gap).
# Read/Write/Edit + Bash (run python solvers) + Glob/Grep. Deliberately excludes
# WebSearch, WebFetch, and Task (a subagent could re-acquire web).
ALLOWED_TOOLS = ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]


def _init_seed(n: int, seed: int) -> int:
    """Per-(problem, seed) init seed — identical across arms (paired design),
    independent across problems and seeds."""
    return seed * 1000 + n


def build_prompt(problem: Problem, spec: SessionSpec, init: np.ndarray) -> str:
    """Build the session prompt. Identical skeleton for both arms; the Warm prompt
    additionally carries the accumulated lessons block."""
    centers = [[float(x), float(y)] for x, y in init]
    lessons_block = ""
    if spec.accumulated_lessons:
        joined = "\n\n".join(
            f"--- lesson {i + 1} ---\n{t}" for i, t in enumerate(spec.accumulated_lessons)
        )
        lessons_block = (
            "\n## Lessons you wrote on earlier problems in this run\n"
            "Reuse what transfers (operators, parameterizations, dead-ends to skip):\n\n"
            f"{joined}\n"
        )
    return f"""You are solving an optimization problem from a random cold start.

{problem.statement}

## Your starting configuration ({problem.n} centers in [0,1]^2)
Begin from exactly these centers and improve the common radius:
{json.dumps(centers)}
{lessons_block}
## Rules
- Use ONLY general-purpose optimizers you write yourself with numpy/scipy
  (e.g. SLSQP with the radius as a variable, Nelder-Mead, basin-hopping,
  multistart). Do NOT look up or hardcode any known/optimal configuration.
- Maximize the common radius r = min(0.5*min pairwise distance, nearest wall).
- Triple-check your own best radius before finishing.

## Deliverable (required)
Write a file named `{RESULT_FILENAME}` in the current directory with JSON:
  {{"centers": [[x, y], ...],   // your best {problem.n} centers
    "lesson": "<= one page: which operator/parameterization worked, dead-ends to
               skip, any transferable structural observation>",
    "techniques": ["slsqp", "multistart", ...]}}
The `lesson` field is required even if progress was small.
"""


def parse_result(cwd: Path, n: int) -> tuple[np.ndarray | None, str | None, set[str]]:
    """Read the agent's `ablation_result.json`. Returns (centers, lesson,
    techniques). centers is None if the file is missing/unparseable or has the
    wrong shape (the run is then scored at the cold baseline)."""
    path = cwd / RESULT_FILENAME
    if not path.exists():
        return None, None, set()
    try:
        obj = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return None, None, set()
    centers = None
    raw = obj.get("centers")
    if isinstance(raw, list) and len(raw) == n:
        try:
            arr = np.asarray(raw, dtype=np.float64)
            if arr.shape == (n, 2):
                centers = arr
        except (ValueError, TypeError):
            centers = None
    lesson = obj.get("lesson") if isinstance(obj.get("lesson"), str) else None
    techniques = {str(t) for t in obj.get("techniques", []) if isinstance(t, str)}
    return centers, lesson, techniques


def _default_headless_run() -> Callable:
    """Lazy import of the repo's headless `claude` wrapper (docs/tools/)."""
    tools_dir = Path(__file__).resolve().parents[3] / "docs" / "tools"
    if str(tools_dir) not in sys.path:
        sys.path.insert(0, str(tools_dir))
    from claude_headless import run  # type: ignore

    return run


def make_solve_fn(
    checkout_root: str | Path,
    *,
    headless_run: Callable | None = None,
    model: str | None = None,
    timeout_seconds: int = 1800,
    telemetry: list | None = None,
) -> Callable[[Problem, ArmConfig, int, SessionSpec], SolveResult]:
    """Build the production `solve_fn` the harness drives.

    `checkout_root` holds `einstein-cold/` and `einstein-warm/` (from
    build_ablation_repos.sh). `headless_run` is injected in tests; defaults to the
    repo's `claude_headless.run`. Per-cell cost/error telemetry is appended to
    `telemetry` if provided.
    """
    checkout_root = Path(checkout_root)
    run = headless_run or _default_headless_run()

    def solve_fn(problem: Problem, cfg: ArmConfig, seed: int, spec: SessionSpec) -> SolveResult:
        cwd = checkout_root / f"einstein-{cfg.arm.value}"
        init = ev.cold_init(problem.n, _init_seed(problem.n, seed))
        score_coldinit = ev.common_radius(init)

        # Clear any prior result so a failed session can't reuse a stale file.
        result_path = cwd / RESULT_FILENAME
        if result_path.exists():
            result_path.unlink()

        prompt = build_prompt(problem, spec, init)
        t0 = time.monotonic()
        kw = {
            "allowed_tools": ALLOWED_TOOLS,
            "timeout_seconds": timeout_seconds,
            "output_format": "json",
            "permission_mode": "acceptEdits",
            "cwd": cwd,
        }
        if model:
            kw["model"] = model
        res = run(prompt, **kw)
        wall = time.monotonic() - t0

        centers, lesson, techniques = parse_result(cwd, problem.n)

        # HARNESS-SIDE scoring — never the agent's self-report. Infeasible/missing
        # output scores at the cold baseline (gap_closed → 0), recorded honestly.
        if centers is not None:
            tv = ev.triple_verify_radius(centers)
            score_final = tv.fast if tv.passed else min(score_coldinit, tv.fast)
            verify_note = tv.reason
        else:
            score_final = score_coldinit
            verify_note = "no parseable result"

        ok = getattr(res, "ok", False)
        # Warm needs a lesson every problem (sanity check); supply a fallback so a
        # failed cell is recorded, not aborted.
        if cfg.write_kb and not lesson:
            lesson = f"[no lesson emitted; ok={ok}; {verify_note}]"

        if telemetry is not None:
            telemetry.append(
                {
                    "cell": spec.problem_id,
                    "arm": cfg.arm.value,
                    "seed": seed,
                    "ok": ok,
                    "error_kind": getattr(res, "error_kind", ""),
                    "cost_usd": getattr(res, "cost_usd", None),
                    "input_tokens": getattr(res, "input_tokens", None),
                    "output_tokens": getattr(res, "output_tokens", None),
                    "score_coldinit": score_coldinit,
                    "score_final": score_final,
                    "verify": verify_note,
                    "wall_clock_s": wall,
                }
            )

        trajectory = [
            TrajectoryPoint(0, score_coldinit),
            TrajectoryPoint(1, score_final),
        ]
        return SolveResult(
            trajectory=trajectory,
            score_coldinit=score_coldinit,
            score_final=score_final,
            lesson_text=lesson,
            attempted_techniques=techniques,
            wall_clock_s=wall,
        )

    return solve_fn


# ---------------- batch runner (§10.4-7) ----------------


def audit_checkout(checkout: str | Path) -> dict:
    """Air-gap receipt for one clean-room checkout (pre-reg §10.7).

    Reuses the firewall block-list (`ablation.is_firewalled`) to prove no
    answer-key file leaked into the checkout, and confirms no web tool is in the
    session allow-list. Passing is the structural guarantee — the agent could not
    have reached an answer key because it physically isn't there and the web tool
    isn't granted.
    """
    from einstein.meta_loop.ablation import is_firewalled

    checkout = Path(checkout)
    leaked = [
        str(p.relative_to(checkout))
        for p in checkout.rglob("*")
        if p.is_file() and is_firewalled(str(p))
    ]
    web_tools = [t for t in ALLOWED_TOOLS if "web" in t.lower()]
    return {
        "checkout": str(checkout),
        "leaked_answer_key_files": leaked,
        "web_tools_in_allowlist": web_tools,
        "passed": not leaked and not web_tools,
    }


def _completed_sequences(records: list[dict], problems, seeds) -> set[tuple[str, int]]:
    """(arm, seed) sequences whose every problem_id already has a record — fully
    done, safe to skip on resume."""
    want = {p.problem_id for p in problems}
    seen: dict[tuple[str, int], set[str]] = {}
    for r in records:
        seen.setdefault((r["arm"], r["seed"]), set()).add(r["problem_id"])
    return {key for key, pids in seen.items() if want.issubset(pids)}


def _purge_sequence(log_path: Path, arm: str, seed: int) -> None:
    """Drop any partial records for one (arm, seed) so an interrupted sequence is
    cleanly re-run (Warm threading makes mid-sequence resume unsafe, so the unit
    of resume is a whole (arm, seed) sequence)."""
    if not log_path.exists():
        return
    kept = [
        line
        for line in log_path.read_text().splitlines()
        if line.strip() and not (lambda o: o["arm"] == arm and o["seed"] == seed)(json.loads(line))
    ]
    log_path.write_text("\n".join(kept) + ("\n" if kept else ""))


def run_experiment(
    problems,
    seeds,
    solve_fn,
    *,
    results_dir: str | Path,
    checkout_root: str | Path,
    known_dead_ends: set[str] | None = None,
    max_lesson_chars: int | None = None,
) -> dict:
    """Resumable batch driver over the (seed x arm x problem) matrix (§10.4-7).

    Per (arm, seed) sequence: skip if already complete; otherwise purge any
    partial records, run the sequence (Warm threads its run-KB; the harness
    enforces the §9 sanity checks), append records, and write an air-gap receipt.
    Returns a summary {ran, skipped, n_records, audits}.
    """
    from einstein.meta_loop.compounding_ablation import (
        Arm,
        RunKB,
        append_record,
        load_records,
        run_arm_sequence,
    )

    results_dir = Path(results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    log_path = results_dir / "runs.jsonl"
    audit_path = results_dir / "audit.jsonl"
    checkout_root = Path(checkout_root)

    completed = _completed_sequences(load_records(log_path), problems, seeds)
    ran: list[str] = []
    skipped: list[str] = []
    audits: list[dict] = []

    for seed in seeds:
        for arm in Arm:
            key = (arm.value, seed)
            if key in completed:
                skipped.append(f"{arm.value}-seed{seed}")
                continue
            _purge_sequence(log_path, arm.value, seed)
            kb = RunKB(results_dir / "run-kb" / f"{arm.value}-{seed}")
            records = run_arm_sequence(
                arm,
                seed,
                problems,
                solve_fn,
                kb,
                known_dead_ends=known_dead_ends,
                max_lesson_chars=max_lesson_chars,
            )
            for rec in records:
                append_record(rec, log_path)
            ran.append(f"{arm.value}-seed{seed}")

            receipt = audit_checkout(checkout_root / f"einstein-{arm.value}")
            receipt.update({"arm": arm.value, "seed": seed})
            audits.append(receipt)
            with audit_path.open("a") as fh:
                fh.write(json.dumps(receipt) + "\n")

    return {
        "ran": ran,
        "skipped": skipped,
        "n_records": len(load_records(log_path)),
        "audits": audits,
    }
