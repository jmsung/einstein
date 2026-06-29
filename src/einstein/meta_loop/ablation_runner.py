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
  family's generic evaluator from the configuration the agent emits and
  triple-verified (A1). A self-reported score is ignored — an agent cannot inflate
  the DV.

The agent result contract: the session writes `ablation_result.json` into its cwd
under the family's answer key (`centers` / `vectors` / `values`, from the Family
adapter), so the runner is correct for any domain (2D points, sphere vectors, 1D
sequences):
    {"<answer_key>": <best configuration>, "lesson": "<<=1-page lesson>>",
     "techniques": ["slsqp", ...]}   # techniques optional
"""

from __future__ import annotations

import contextlib
import json
import os
import shutil
import sys
import tempfile
import time
from collections.abc import Callable, Iterator
from pathlib import Path

import numpy as np

from einstein.ablation_packing.families import Family, get_family
from einstein.meta_loop.compounding_ablation import ArmConfig, Problem, SessionSpec, SolveResult
from einstein.meta_loop.prompt_tone import PREAMBLES, PromptTone
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


def _init_seed(n: int, seed: int, replicate: int = 0) -> int:
    """Per-(problem, seed, replicate) init seed — identical across arms (paired
    design), independent across problems, seeds, and within-cell replicates. The
    replicate offset (1e6) is far above the seed*1000+n range so distinct replicates
    never alias another (seed, n) cell's cold-init."""
    return replicate * 1_000_000 + seed * 1000 + n


def build_prompt(
    problem: Problem,
    spec: SessionSpec,
    init: np.ndarray,
    family: Family,
    tone: PromptTone = PromptTone.NEUTRAL,
) -> str:
    """Build the session prompt. Identical skeleton for both arms; the Warm prompt
    additionally carries the accumulated lessons block. The config-space description,
    the start config, and the answer key come from the family adapter, so the prompt
    is correct for any domain (2D points, sphere vectors, 1D sequences).

    `tone` (prereg §4) prepends a verbatim preamble — the ONE variable of the
    prompt-tone ablation. NEUTRAL (default) prepends "" so the prompt is
    byte-identical to the pre-tone prompt; ENCOURAGING prepends the frozen
    motivational string."""
    preamble = PREAMBLES[tone]
    prefix = f"{preamble}\n\n" if preamble else ""
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
    key = family.answer_key
    return (
        prefix
        + f"""You are solving an optimization problem from a random cold start.

{problem.statement}

## Your starting configuration ({family.config_space(problem.n)})
Begin from exactly this configuration and improve the objective described above:
{json.dumps(family.format_init(init))}
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
  {{"{key}": <your best configuration, same shape as the starting configuration above>,
    "lesson": "<= one page: which operator/parameterization worked, dead-ends to
               skip, any transferable structural observation>",
    "techniques": ["slsqp", "multistart", ...]}}
Write this file as soon as you have ANY improved configuration, and OVERWRITE it
every time you find a better one — so your current best is always saved even if
you run out of budget. The `lesson` field is required even if progress was small.
"""
    )


def parse_result(
    cwd: Path, family: Family, n: int
) -> tuple[np.ndarray | None, str | None, set[str]]:
    """Read the agent's `ablation_result.json`. Returns (config, lesson, techniques).
    `config` is parsed via the family adapter from `family.answer_key`, and is None if
    the file is missing/unparseable or has the wrong shape (the run is then scored at
    the cold baseline)."""
    path = cwd / RESULT_FILENAME
    if not path.exists():
        return None, None, set()
    try:
        obj = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return None, None, set()
    config = family.parse(obj.get(family.answer_key), n)
    lesson = obj.get("lesson") if isinstance(obj.get("lesson"), str) else None
    techniques = {str(t) for t in obj.get("techniques", []) if isinstance(t, str)}
    return config, lesson, techniques


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
    transcripts_dir: str | Path | None = None,
    prompt_tone: PromptTone = PromptTone.NEUTRAL,
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

    `prompt_tone` (prereg §4) selects the verbatim preamble prepended to every
    session this solve_fn launches — the ONE variable of the prompt-tone ablation.
    Bound here (not on `Arm`/`SessionSpec`) so it stays orthogonal to the Cold/Warm
    memory axis and never touches the cold-init seed; run two tone-bound solve_fns
    at equal seeds to get a paired tone comparison. NOTE on the §3 fixed-budget cap:
    the binding lever is `max_budget_usd` (the token/cost ceiling) — the headless
    `claude -p` CLI exposes no per-session turn/cycle cap, so "max cycles" has no
    referent in this single-session runner; hold `max_budget_usd` equal across arms
    for the fixed-budget regime.
    """
    checkout_root = Path(checkout_root)
    run = headless_run or _default_headless_run()

    def solve_fn(problem: Problem, cfg: ArmConfig, seed: int, spec: SessionSpec) -> SolveResult:
        family = get_family(problem.family)
        init = family.cold_init(problem.n, _init_seed(problem.n, seed, spec.replicate))
        score_coldinit = family.score(init)

        # PER-CELL ISOLATED CWD (fixes cross-cell filesystem contamination): each cell
        # runs in a fresh empty dir, removed after, so a later cell can never read an
        # earlier cell's scratch — the cold arm's "no memory" guarantee is restored, and
        # the empty dir is air-gapped by emptiness (no answers reachable). The agent
        # writes its own numpy/scipy solver here; python/venv is env-level, not cwd-bound.
        # (Note: not a hard sandbox — absolute-path access remains; containerize for an
        # adversarial threat model. This closes the *accidental* channel.)
        cell = f"{problem.problem_id}-{cfg.arm.value}-s{seed}-r{spec.replicate}"
        # Fresh per-cell subdir INSIDE the arm checkout (not /tmp): `uv run`/python must
        # resolve the project env (pyproject + .venv found upward) — an empty /tmp dir
        # breaks `uv run` (no numpy). Inside the checkout the env resolves AND the cell
        # still starts empty (isolation); removed after, so cells never share scratch.
        cell_parent = checkout_root / f"einstein-{cfg.arm.value}" / "_cells"
        cell_parent.mkdir(parents=True, exist_ok=True)
        cwd = Path(tempfile.mkdtemp(prefix=f"{cell}-", dir=str(cell_parent)))
        try:
            prompt = build_prompt(problem, spec, init, family, tone=prompt_tone)
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

            config, lesson, techniques = parse_result(cwd, family, problem.n)

            # Transcript log (auditability — was a channel used?): save prompt + the
            # session's stdout per cell before the cwd is removed.
            if transcripts_dir is not None:
                td = Path(transcripts_dir)
                td.mkdir(parents=True, exist_ok=True)
                (td / f"{cell}.txt").write_text(
                    f"PROMPT:\n{prompt}\n\n--- STDOUT ---\n{getattr(res, 'stdout', '') or ''}"
                )
        finally:
            shutil.rmtree(cwd, ignore_errors=True)

        # HARNESS-SIDE scoring — never the agent's self-report. Infeasible/missing
        # output scores at the cold baseline (gap_closed → 0), recorded honestly.
        if config is not None:
            tv = family.triple_verify(config)
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
                    "prompt_tone": prompt_tone.value,
                    "seed": seed,
                    "replicate": spec.replicate,
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


# Answer-key DATA the §7 strip removes — their presence in a checkout is a leak.
# (Directories of pre-built knowledge/SOTA + solution dumps. NOT source files: the
# URL/substring firewall in `ablation.is_firewalled` is for transcript tool-call
# targets, not filesystem paths — applied to every file it false-flags code like
# `scripts/leaderboard_standings.py`.)
_ANSWER_KEY_DIRS = ("docs/wiki", "docs/source", "docs/agent", "mb", "results")


def audit_checkout(checkout: str | Path) -> dict:
    """Air-gap receipt for one clean-room checkout (pre-reg §10.7).

    Verifies the §7 strip held: the pre-built knowledge layer + answer/solution
    dumps are physically absent, and no web tool is in the session allow-list.
    Passing is the structural guarantee — the agent could not reach an answer key
    because it isn't on disk and the web tool isn't granted.
    """
    checkout = Path(checkout)

    def _is_env(p: Path) -> bool:
        # Skip the Python environment: its packages (e.g. osqp) ship test fixtures
        # under .../tests/solutions/*.npz that are NOT problem answer keys — a
        # `/solutions/` substring false-positive, not a real leak.
        s = str(p)
        return "/.venv/" in s or "/site-packages/" in s

    leaked = [d for d in _ANSWER_KEY_DIRS if (checkout / d).exists()]
    leaked += [
        str(p.relative_to(checkout))
        for p in checkout.rglob("solution-best*")
        if p.is_file() and not _is_env(p)
    ]
    leaked += [
        str(p.relative_to(checkout))
        for p in checkout.rglob("*")
        if p.is_file() and "/solutions/" in str(p) and not _is_env(p)
    ]
    web_tools = [t for t in ALLOWED_TOOLS if "web" in t.lower()]
    return {
        "checkout": str(checkout),
        "leaked_answer_key_files": leaked,
        "web_tools_in_allowlist": web_tools,
        "passed": not leaked and not web_tools,
    }


class AirGapViolation(RuntimeError):
    """A clean-room checkout failed the air-gap audit (pre-reg §7).

    Raised by `assert_clean_checkout` so the batch driver REFUSES to run on a
    contaminated checkout — the audit is a hard gate, not just a post-hoc
    receipt (air-gap fidelity audit, 2026-06-28). A leaked answer-key/wiki dir
    or a web tool in the allow-list aborts before any compute is spent.
    """


def assert_clean_checkout(checkout: str | Path) -> dict:
    """Pre-flight HARD GATE: audit the checkout and raise on any breach.

    Returns the passing receipt; raises `AirGapViolation` if the checkout is
    missing or `audit_checkout` reports a leak / a web tool. Use this (not the
    bare `audit_checkout` receipt) wherever a contaminated checkout must STOP
    the run rather than merely be recorded.
    """
    checkout = Path(checkout)
    if not checkout.exists():
        raise AirGapViolation(f"clean-room checkout missing: {checkout}")
    receipt = audit_checkout(checkout)
    if not receipt["passed"]:
        raise AirGapViolation(
            f"air-gap breached in {checkout}: "
            f"leaked_answer_key_files={receipt['leaked_answer_key_files']} "
            f"web_tools_in_allowlist={receipt['web_tools_in_allowlist']}"
        )
    return receipt


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
    replicates: int = 1,
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

    # PRE-FLIGHT HARD GATE (pre-reg §7): audit BOTH arm checkouts before any
    # compute. A leaked wiki/answer-key dir or a web tool aborts the batch here —
    # the audit is a gate, not just the post-hoc receipt below. Receipts are
    # recorded first so the audit log shows what was checked even on abort.
    for arm in Arm:
        checkout = checkout_root / f"einstein-{arm.value}"
        try:
            receipt = assert_clean_checkout(checkout)
        except AirGapViolation:
            fail = {**audit_checkout(checkout), "arm": arm.value, "phase": "preflight"}
            audits.append(fail)
            with audit_path.open("a") as fh:
                fh.write(json.dumps(fail) + "\n")
            raise
        receipt.update({"arm": arm.value, "phase": "preflight"})
        audits.append(receipt)
        with audit_path.open("a") as fh:
            fh.write(json.dumps(receipt) + "\n")

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
                replicates=replicates,
            )
            (resumed if is_resume else ran).append(label)

            # Post-run receipt = drift detection: catches a checkout mutated
            # mid-run (e.g. an answer-key dir created during the session). Record
            # first, then abort the batch if the air-gap was breached.
            receipt = audit_checkout(checkout_root / f"einstein-{arm.value}")
            receipt.update({"arm": arm.value, "seed": seed, "phase": "postrun"})
            audits.append(receipt)
            with audit_path.open("a") as fh:
                fh.write(json.dumps(receipt) + "\n")
            if not receipt["passed"]:
                raise AirGapViolation(
                    f"air-gap breached during run (arm={arm.value}, seed={seed}): "
                    f"leaked_answer_key_files={receipt['leaked_answer_key_files']} "
                    f"web_tools_in_allowlist={receipt['web_tools_in_allowlist']}"
                )

    return {
        "ran": ran,
        "resumed": resumed,
        "skipped": skipped,
        "n_records": len(load_records(log_path)),
        "audits": audits,
    }
