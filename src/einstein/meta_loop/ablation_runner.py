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

import contextlib
import json
import os
import sys
import time
from collections.abc import Callable, Iterator
from pathlib import Path

import numpy as np

from einstein.ablation_packing import evaluator as ev
from einstein.ablation_packing.families import get_family
from einstein.meta_loop.compounding_ablation import ArmConfig, Problem, SessionSpec, SolveResult
from einstein.meta_loop.trajectory import TrajectoryPoint

RESULT_FILENAME = "ablation_result.json"

# Tool set for BOTH arms — generic solving only, NO web/retrieval (air-gap).
# Read/Write/Edit + Bash (run python solvers) + Glob/Grep. Deliberately excludes
# WebSearch, WebFetch, and Task (a subagent could re-acquire web).
ALLOWED_TOOLS = ["Read", "Write", "Edit", "Bash", "Glob", "Grep"]


@contextlib.contextmanager
def _without_external_api_key(drop: bool) -> Iterator[None]:
    """Temporarily remove ANTHROPIC_API_KEY from the env so the headless `claude`
    subprocess falls back to the authenticated Claude Code login.

    Why default-on: a stale/invalid `ANTHROPIC_API_KEY` in the shell makes
    `claude -p` 401 ("Invalid API key") instead of using the OAuth session — it
    would silently kill an unattended 36-cell batch. The runner is sequential, so
    mutating os.environ around the call (and restoring it) is safe. Set
    drop=False to deliberately use a (valid) API key for pay-per-token billing.
    """
    if not drop:
        yield
        return
    saved = os.environ.pop("ANTHROPIC_API_KEY", None)
    try:
        yield
    finally:
        if saved is not None:
            os.environ["ANTHROPIC_API_KEY"] = saved


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
  (e.g. Nelder-Mead, SLSQP, basin-hopping, simulated annealing, multistart).
  Do NOT look up or hardcode any known/optimal configuration.
- Maximize the objective described above.
- Triple-check your own best objective value before finishing.
- Your budget for this problem is LIMITED. Spend it well — go straight to the
  approach you judge most efficient rather than exploring exhaustively.

## Deliverable (required) — write it INCREMENTALLY
Write a file named `{RESULT_FILENAME}` in the current directory with JSON:
  {{"centers": [[x, y], ...],   // your best {problem.n} centers so far
    "lesson": "<= one page: which operator/parameterization worked, dead-ends to
               skip, any transferable structural observation>",
    "techniques": ["slsqp", "multistart", ...]}}
Write this file as soon as you have ANY improved configuration, and OVERWRITE it
every time you find a better one — so your current best is always saved even if
you run out of budget. The `lesson` field is required even if progress was small.
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
    max_budget_usd: float | None = None,
    telemetry: list | None = None,
    drop_api_key: bool = True,
) -> Callable[[Problem, ArmConfig, int, SessionSpec], SolveResult]:
    """Build the production `solve_fn` the harness drives.

    `checkout_root` holds `einstein-cold/` and `einstein-warm/` (from
    build_ablation_repos.sh). `headless_run` is injected in tests; defaults to the
    repo's `claude_headless.run`. Per-cell cost/error telemetry is appended to
    `telemetry` if provided. `drop_api_key` (default True) removes a stale
    ANTHROPIC_API_KEY for the session so it uses the Claude Code login; set False
    to use a valid API key (pay-per-token billing).

    `max_budget_usd` caps each session's spend (held EQUAL across arms, pre-reg
    §3) — this is the efficiency-DV lever: under a tight cap a Cold session that
    must rediscover the method closes less of the gap than a Warm session that
    reuses it, so `gap_closed` becomes discriminating again and cost/wall measure
    efficiency. None = uncapped (the saturated regime).
    """
    checkout_root = Path(checkout_root)
    run = headless_run or _default_headless_run()

    def solve_fn(problem: Problem, cfg: ArmConfig, seed: int, spec: SessionSpec) -> SolveResult:
        cwd = checkout_root / f"einstein-{cfg.arm.value}"
        family = get_family(problem.family)
        init = ev.cold_init(problem.n, _init_seed(problem.n, seed))
        score_coldinit = family.score(init)

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
        if max_budget_usd is not None:
            kw["max_budget_usd"] = max_budget_usd
        with _without_external_api_key(drop_api_key):
            res = run(prompt, **kw)
        wall = time.monotonic() - t0

        centers, lesson, techniques = parse_result(cwd, problem.n)

        # HARNESS-SIDE scoring — never the agent's self-report. Infeasible/missing
        # output scores at the cold baseline (gap_closed → 0), recorded honestly.
        if centers is not None:
            tv = family.triple_verify(centers)
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


def _done_pids(records: list[dict]) -> dict[tuple[str, int], set[str]]:
    """Map (arm, seed) → set of problem_ids already logged."""
    d: dict[tuple[str, int], set[str]] = {}
    for r in records:
        d.setdefault((r["arm"], r["seed"]), set()).add(r["problem_id"])
    return d


def _purge_sequence(log_path: Path, arm: str, seed: int) -> None:
    """Drop all logged records for one (arm, seed) — used only as the fallback when
    an interrupted sequence's on-disk KB no longer matches the log."""
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
    """Resumable, crash-resilient batch driver over the matrix (pre-reg v2 §8-9).

    Per (arm, seed): skip if every problem is logged; else **resume per-cell** —
    run only the not-yet-logged problems in this seed's counterbalanced order,
    reusing the on-disk Warm run-KB (records are appended as each cell finishes, so
    a crash keeps completed cells). If the on-disk KB no longer matches the log
    (e.g. a crash mid-write), fall back to a clean restart of that sequence.
    Returns {ran, resumed, skipped, n_records, audits}.
    """
    from einstein.meta_loop.compounding_ablation import (
        ARM_CONFIGS,
        Arm,
        RunKB,
        append_record,
        cyclic_order,
        load_records,
        run_arm_sequence,
    )

    results_dir = Path(results_dir)
    results_dir.mkdir(parents=True, exist_ok=True)
    log_path = results_dir / "runs.jsonl"
    audit_path = results_dir / "audit.jsonl"
    checkout_root = Path(checkout_root)
    want = {p.problem_id for p in problems}

    done_map = _done_pids(load_records(log_path))
    ran: list[str] = []
    resumed: list[str] = []
    skipped: list[str] = []
    audits: list[dict] = []

    for seed in seeds:
        for arm in Arm:
            label = f"{arm.value}-seed{seed}"
            done = done_map.get((arm.value, seed), set())
            if want.issubset(done):
                skipped.append(label)
                continue

            kb = RunKB(results_dir / "run-kb" / f"{arm.value}-{seed}")
            is_resume = bool(done)
            if is_resume:
                # KB-vs-log consistency: Warm must have one persisted lesson per
                # completed problem; otherwise the crash left them out of sync.
                consistent = (not ARM_CONFIGS[arm].write_kb) or (kb.lesson_count() == len(done))
                if not consistent:
                    _purge_sequence(log_path, arm.value, seed)
                    kb.wipe()
                    done = set()
                    is_resume = False

            run_arm_sequence(
                arm,
                seed,
                problems,
                solve_fn,
                kb,
                known_dead_ends=known_dead_ends,
                max_lesson_chars=max_lesson_chars,
                order=cyclic_order(problems, seed),
                skip_done=done,
                on_record=lambda rec: append_record(rec, log_path),  # durable per-cell
            )
            (resumed if is_resume else ran).append(label)

            receipt = audit_checkout(checkout_root / f"einstein-{arm.value}")
            receipt.update({"arm": arm.value, "seed": seed})
            audits.append(receipt)
            with audit_path.open("a") as fh:
                fh.write(json.dumps(receipt) + "\n")

    return {
        "ran": ran,
        "resumed": resumed,
        "skipped": skipped,
        "n_records": len(load_records(log_path)),
        "audits": audits,
    }
