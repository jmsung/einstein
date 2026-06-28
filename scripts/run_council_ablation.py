#!/usr/bin/env python3
"""Persona-council ablation runner (JSAgent claim #1).

Tests the claim "the persona council (writing QUESTIONS before solving) improves
outcomes" as a controlled, equal-solve-budget ablation. Two arms differ ONLY by
whether a wiki-less math council's questions are injected into the solve prompt:

- COUNCIL-ON : run one headless `claude` session per persona with
  `build_enriched_prompt(... hits=[] ...)` (WIKI-LESS — isolates persona framing
  from the KB claim), collect their questions, concatenate into a
  "## Questions from a math council" block, INJECT it into the normal solve
  prompt, then run the SAME solve as council-off with the SAME budget.
- COUNCIL-OFF: the normal solve, no questions block, SAME budget.

Both arms reuse the existing solver verbatim (`ablation_runner.make_solve_fn`):
same air-gapped checkout, same cold-init per (problem, seed) (paired), same
harness-side triple-verified `gap_closed`. The injection is done by appending the
council block to `problem.statement` (via `dataclasses.replace`) so the IDENTICAL
`solve_fn` builds both prompts — the cold-init depends only on (n, seed), so
pairing is preserved.

This file is a thin orchestrator: it does NOT duplicate the solver. It reuses
`make_solve_fn`, `build_session_spec`, `gap_closed`, `dispatch`,
`build_enriched_prompt`, and the headless runner.

SMOKE mode (default): one (heilbronn n=13, seed=1) cell per arm (~5-6 LLM
sessions). Verifies end-to-end wiring; does NOT run the full experiment.
"""

from __future__ import annotations

import argparse
import dataclasses
import time
from pathlib import Path

from einstein.council import build_enriched_prompt, dispatch
from einstein.meta_loop.ablation_runner import (
    ALLOWED_TOOLS,
    _default_headless_run,
    _without_external_api_key,
    audit_checkout,
)
from einstein.meta_loop.compounding_ablation import (
    ARM_CONFIGS,
    Arm,
    build_session_spec,
    gap_closed,
    load_problems,
)

REPO = Path(__file__).resolve().parents[1]
COUNCIL_FILE = REPO / "config" / "ablation_council_smoke.md"
HEILBRONN_CONFIG = REPO / "config" / "ablation_heilbronn_problems.yaml"
CHECKOUT_ROOT = REPO / "ablation-build"

# Heilbronn category for council framing (core personas ignore it for selection;
# it only labels the prompt). Best-known table is the gap_closed denominator.
PROBLEM_CATEGORY = "discrete_geometry"


def _trunc(s: str, n: int = 400) -> str:
    s = s.strip()
    return s if len(s) <= n else s[:n] + " …[truncated]"


def gather_council_questions(
    *,
    problem_id: int,
    model: str,
    timeout_s: int,
    cap_usd: float,
    cwd: Path,
) -> tuple[dict[str, str], list[dict]]:
    """Run one WIKI-LESS headless persona session each; return {persona: questions}.

    Wiki-less by construction: `build_enriched_prompt(hits=[], qmd_runner=None)`
    so the literature block is "(no relevant hits)" — isolates persona framing
    from the KB claim. Air-gapped: a no-web allow-list (`ALLOWED_TOOLS`) and the
    Claude Code login (stale ANTHROPIC_API_KEY dropped).
    """
    run = _default_headless_run()
    personas = dispatch(PROBLEM_CATEGORY, path=COUNCIL_FILE)
    if not personas:
        raise SystemExit(f"no personas dispatched from {COUNCIL_FILE}")
    questions: dict[str, str] = {}
    telem: list[dict] = []
    for p in personas:
        prompt = build_enriched_prompt(
            p,
            problem_id=problem_id,
            problem_category=PROBLEM_CATEGORY,
            hits=[],  # WIKI-LESS: force "(no relevant hits)" (qmd IS on PATH here)
            qmd_runner=None,
        )
        t0 = time.monotonic()
        with _without_external_api_key(True):
            res = run(
                prompt,
                allowed_tools=["Read"],  # no web tool -> air-gapped persona session
                timeout_seconds=timeout_s,
                output_format="json",
                model=model,
                cwd=cwd,
            )
        wall = time.monotonic() - t0
        text = (res.stdout or "").strip() if getattr(res, "ok", False) else ""
        questions[p.name] = text or f"[no questions returned; ok={getattr(res, 'ok', False)} kind={getattr(res, 'error_kind', '')}]"
        telem.append(
            {
                "persona": p.name,
                "ok": getattr(res, "ok", False),
                "error_kind": getattr(res, "error_kind", ""),
                "cost_usd": getattr(res, "cost_usd", None),
                "wall_s": wall,
            }
        )
    return questions, telem


def build_council_block(questions: dict[str, str]) -> str:
    names = ", ".join(questions)
    lines = [
        "## Questions from a math council",
        "",
        f"A council of mathematicians ({names}) considered this exact problem and "
        "posed the questions below to guide your approach. They are FRAMING, not "
        "solutions — use them to choose and focus your method.",
        "",
    ]
    for name, q in questions.items():
        lines += [f"### {name}", q.strip(), ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--problem-id", default="heil-n13")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--model", default="haiku", help="model for persona + solve sessions")
    ap.add_argument("--persona-timeout", type=int, default=120)
    ap.add_argument("--persona-cap", type=float, default=0.50)
    ap.add_argument("--solve-timeout", type=int, default=600)
    ap.add_argument("--solve-cap", type=float, default=1.50)
    args = ap.parse_args()

    problems = {p.problem_id: p for p in load_problems(HEILBRONN_CONFIG)}
    if args.problem_id not in problems:
        raise SystemExit(f"unknown problem {args.problem_id}; have {sorted(problems)}")
    problem = problems[args.problem_id]
    seed = args.seed
    cold_cwd = CHECKOUT_ROOT / "einstein-cold"

    print("=" * 72)
    print("PERSONA-COUNCIL ABLATION — SMOKE (one cell per arm)")
    print("=" * 72)
    print(f"problem={problem.problem_id} n={problem.n} seed={seed} "
          f"ref_opt={problem.reference_optimum} family={problem.family}")
    print(f"model={args.model}  solve_budget: timeout={args.solve_timeout}s "
          f"cap=${args.solve_cap}  (SAME for both arms)")

    # Air-gap receipt for the checkout both arms run in.
    audit = audit_checkout(cold_cwd)
    print(f"air-gap audit (einstein-cold): passed={audit['passed']} "
          f"web_tools={audit['web_tools_in_allowlist']} "
          f"leaked={audit['leaked_answer_key_files'][:3]}")

    # ---- COUNCIL-ON: gather wiki-less persona questions ----
    print("\n[1] Council dispatch (wiki-less personas writing questions)…")
    questions, council_telem = gather_council_questions(
        problem_id=problem.n,
        model=args.model,
        timeout_s=args.persona_timeout,
        cap_usd=args.persona_cap,
        cwd=cold_cwd,
    )
    council_block = build_council_block(questions)
    for name, q in questions.items():
        print(f"\n  --- {name} ---\n  {_trunc(q, 350)}")
    council_cost = sum((t["cost_usd"] or 0.0) for t in council_telem)
    council_wall = sum(t["wall_s"] for t in council_telem)
    print(f"\n  council: {len(questions)} personas, "
          f"{sum(1 for t in council_telem if t['ok'])} ok, "
          f"cost=${council_cost:.4f}, wall={council_wall:.1f}s")

    # ---- shared solver (identical for both arms; the ONLY arm difference is the
    #      injected questions block in problem.statement) ----
    from einstein.meta_loop.ablation_runner import make_solve_fn

    solve_telem: list[dict] = []
    solve_fn = make_solve_fn(
        CHECKOUT_ROOT,
        model=args.model,
        timeout_seconds=args.solve_timeout,
        max_budget_usd=args.solve_cap,
        telemetry=solve_telem,
        drop_api_key=True,  # use Claude Code login (stale ANTHROPIC_API_KEY dropped)
    )
    cfg = ARM_CONFIGS[Arm.COLD]  # read_kb=False, write_kb=False -> no lesson, identical both arms

    problem_off = problem
    problem_on = dataclasses.replace(
        problem, statement=problem.statement + "\n\n" + council_block
    )

    # injection confirmation
    print(f"\n[2] Injection: council block = {len(council_block)} chars; "
          f"on-arm statement {len(problem_off.statement)} -> {len(problem_on.statement)} chars "
          f"(block present in on-arm prompt: {council_block[:40]!r} … "
          f"{'## Questions from a math council' in problem_on.statement})")

    spec_off = build_session_spec(problem_off, Arm.COLD, seed, run_kb=None)
    spec_on = build_session_spec(problem_on, Arm.COLD, seed, run_kb=None)

    print("\n[3] COUNCIL-OFF solve…")
    res_off = solve_fn(problem_off, cfg, seed, spec_off)
    print("[4] COUNCIL-ON solve…")
    res_on = solve_fn(problem_on, cfg, seed, spec_on)

    gc_off = gap_closed(res_off.score_coldinit, res_off.score_final,
                        problem.reference_optimum, minimize=problem.minimize)
    gc_on = gap_closed(res_on.score_coldinit, res_on.score_final,
                       problem.reference_optimum, minimize=problem.minimize)

    paired = abs(res_off.score_coldinit - res_on.score_coldinit) < 1e-15

    def cost(arm_val: str) -> float:
        return sum((t["cost_usd"] or 0.0) for t in solve_telem if t["arm"] == arm_val)

    print("\n" + "=" * 72)
    print("RESULTS")
    print("=" * 72)
    print(f"PAIRING: score_coldinit off={res_off.score_coldinit:.10f} "
          f"on={res_on.score_coldinit:.10f}  -> same cold-init: {paired}")
    print(f"COUNCIL-OFF: score_final={res_off.score_final:.8f}  "
          f"gap_closed={gc_off:.4f}  wall={res_off.wall_clock_s:.1f}s  "
          f"solve_cost=${cost('cold'):.4f}")
    print(f"COUNCIL-ON : score_final={res_on.score_final:.8f}  "
          f"gap_closed={gc_on:.4f}  wall={res_on.wall_clock_s:.1f}s  "
          f"(+ council ${council_cost:.4f}, {council_wall:.1f}s)")
    print(f"Δ gap_closed (on - off) = {gc_on - gc_off:+.4f}  "
          f"[SMOKE: n=1, not inferential]")
    print("\nper-cell solve telemetry:")
    for t in solve_telem:
        print(f"  arm={t['arm']} ok={t['ok']} kind={t.get('error_kind','')} "
              f"cost=${t.get('cost_usd') or 0:.4f} "
              f"verify={t.get('verify','')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
