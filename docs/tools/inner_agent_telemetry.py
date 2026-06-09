#!/usr/bin/env python3
"""inner_agent_telemetry.py — per-cycle telemetry for the LLM inner-agent path.

Phase 2 Goal 1 of `mb/active/js-feat-meta-learning-inner-agent.md`. The wired
LLM path (`autonomous_loop._try_llm_path`) is *graceful* on failure — every
error returns None and the loop falls back to mechanical — but until now the
failures were only visible as scattered WARNING logs. That made the readiness
criteria in `docs/agent/inner-agent-readiness.md` (fallback rate, parse-success
rate, timeout rate, wall-clock, tokens) un-measurable.

This module is the structured sink. `_try_llm_path` calls `record_cycle()` at
every exit point — one JSON line per LLM-path attempt — and `summarize()`
turns the accumulated ledger into exactly the R2/R3/R4/R5 numbers the GO/NO-GO
verdict (Goal 4) is measured against. The ledger is JSONL (not markdown) for
the same reason `cited-sources.jsonl` / `capture-queue.jsonl` are: it's an
append-only machine record, not a human-read narrative.

Error model: `record_cycle` creates parent dirs and appends; it raises only on
genuine I/O failure. Callers wrap it best-effort so telemetry never breaks a
cycle. `read_records` skips malformed lines rather than raising.

  path_taken values
    "llm"        the LLM path produced a result dict (success)
    "fallback"   the attempt fell back to mechanical; see llm_error_kind

  llm_error_kind values (only meaningful when path_taken == "fallback")
    ""                  n/a (path_taken == "llm")
    "import-error"      LLM path components not importable
    "render-error"      inner_agent_prompt.render_prompt raised
    "headless-exception" claude_headless.run raised unexpectedly
    "unavailable"       auth / quota / 429 / overload (from HeadlessResult)
    "timeout"           claude -p wall-clock cap exceeded
    "non-zero"          claude -p exited non-zero
    "parse-error"       inner_agent_output.parse_response raised
"""

from __future__ import annotations

import datetime as dt
import json
import logging
from dataclasses import asdict, dataclass, field
from pathlib import Path

log = logging.getLogger("inner_agent_telemetry")


# Error kinds that mean "Claude Code was temporarily unavailable" rather than
# "the request was wrong" — separated out for the summary so a run that failed
# only because the laptop was offline isn't counted against the LLM path's
# quality. Mirrors claude_headless's _UNAVAILABLE_PATTERNS taxonomy.
ENVIRONMENTAL_ERROR_KINDS = frozenset({"unavailable", "import-error", "headless-exception"})


@dataclass
class CycleTelemetry:
    """One LLM-path attempt's structured outcome.

    Fields map 1:1 to the readiness criteria they feed:
      path_taken / llm_error_kind → R2 (fallback rate), R4 (timeout rate)
      parse_ok                    → R3 (parse-success rate)
      wall_clock_s                → R4 (timeout rate), latency
      input_tokens / output_tokens / token_source → R5 (cost ceiling)
    """

    problem_id: int = -1
    attempt_index: int = -1
    path_taken: str = "fallback"  # "llm" | "fallback"
    llm_error_kind: str = ""  # see module docstring
    parse_ok: bool = False
    wall_clock_s: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0
    token_source: str = "estimate"  # "estimate" | "exact" (json-envelope, Goal 3)
    cost_usd: float = 0.0  # exact total_cost_usd from the json envelope (Goal 3)
    ts: str = ""

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


def _now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def record_cycle(
    telemetry_path: Path,
    *,
    problem_id: int,
    attempt_index: int,
    path_taken: str,
    llm_error_kind: str = "",
    parse_ok: bool = False,
    wall_clock_s: float = 0.0,
    input_tokens: int = 0,
    output_tokens: int = 0,
    token_source: str = "estimate",
    cost_usd: float = 0.0,
    ts: str | None = None,
) -> CycleTelemetry:
    """Append one telemetry record to the JSONL ledger; return the record.

    Creates the parent directory and file if absent. Single-writer append —
    the autonomous_loop's O_EXCL lockfile serializes cycles, so this is safe
    in practice (same guarantee as `inner_agent_gates.record_token_usage`).
    """
    rec = CycleTelemetry(
        problem_id=int(problem_id),
        attempt_index=int(attempt_index),
        path_taken=path_taken,
        llm_error_kind=llm_error_kind,
        parse_ok=bool(parse_ok),
        wall_clock_s=float(wall_clock_s),
        input_tokens=int(input_tokens),
        output_tokens=int(output_tokens),
        token_source=token_source,
        cost_usd=float(cost_usd),
        ts=ts if ts is not None else _now_iso(),
    )
    p = Path(telemetry_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(rec)) + "\n")
    return rec


def read_records(telemetry_path: Path) -> list[CycleTelemetry]:
    """Read every record from the ledger. Skips malformed / partial lines.

    Returns [] if the file is absent. Tolerant by design — a half-written
    line from an interrupted append must not crash the summary.
    """
    p = Path(telemetry_path)
    if not p.is_file():
        return []
    out: list[CycleTelemetry] = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError:
            log.debug("skipping malformed telemetry line: %.80s", line)
            continue
        if not isinstance(d, dict) or "path_taken" not in d:
            continue
        # Drop unknown keys so a schema bump in the writer doesn't crash old
        # readers; fill missing keys from the dataclass defaults.
        known = {f.name for f in CycleTelemetry.__dataclass_fields__.values()}  # type: ignore[attr-defined]
        out.append(CycleTelemetry(**{k: v for k, v in d.items() if k in known}))
    return out


@dataclass
class TelemetrySummary:
    """Aggregate over a set of records — the readiness-criteria numbers."""

    cycles: int = 0
    llm_cycles: int = 0
    fallback_cycles: int = 0
    environmental_fallbacks: int = 0
    parse_attempts: int = 0  # runs that returned ok=True (parse was attempted)
    parse_ok: int = 0
    timeouts: int = 0
    total_tokens: int = 0
    total_cost_usd: float = 0.0
    exact_cost_cycles: int = 0  # llm cycles with a real cost_usd (>0)
    wall_clock_total_s: float = 0.0
    error_kind_counts: dict[str, int] = field(default_factory=dict)

    @property
    def fallback_rate(self) -> float:
        """R2 — fraction of cycles that fell back. Environmental fallbacks are
        excluded from the denominator: a fallback because the laptop was
        offline isn't evidence the LLM path is unreliable."""
        decided = self.cycles - self.environmental_fallbacks
        if decided <= 0:
            return 0.0
        non_env_fallbacks = self.fallback_cycles - self.environmental_fallbacks
        return non_env_fallbacks / decided

    @property
    def parse_success_rate(self) -> float:
        """R3 — of runs where a parse was attempted, fraction that parsed."""
        if self.parse_attempts == 0:
            return 1.0  # vacuously true; no parse attempted yet
        return self.parse_ok / self.parse_attempts

    @property
    def timeout_rate(self) -> float:
        """R4 — fraction of cycles that hit the wall-clock cap."""
        if self.cycles == 0:
            return 0.0
        return self.timeouts / self.cycles

    @property
    def mean_tokens_per_llm_cycle(self) -> float:
        """R5 — mean tokens for cycles that actually ran the LLM."""
        if self.llm_cycles == 0:
            return 0.0
        return self.total_tokens / self.llm_cycles

    @property
    def mean_wall_clock_s(self) -> float:
        if self.cycles == 0:
            return 0.0
        return self.wall_clock_total_s / self.cycles

    @property
    def mean_cost_per_llm_cycle(self) -> float:
        """$/cycle over cycles with an exact cost (Goal 3). 0.0 if none had
        exact cost (e.g. all token_source=estimate, pre-json-mode)."""
        if self.exact_cost_cycles == 0:
            return 0.0
        return self.total_cost_usd / self.exact_cost_cycles


def summarize(records: list[CycleTelemetry]) -> TelemetrySummary:
    """Fold records into the readiness-criteria summary (R2–R5)."""
    s = TelemetrySummary()
    for r in records:
        s.cycles += 1
        s.wall_clock_total_s += r.wall_clock_s
        if r.path_taken == "llm":
            s.llm_cycles += 1
            s.total_tokens += r.total_tokens
            if r.cost_usd > 0:
                s.total_cost_usd += r.cost_usd
                s.exact_cost_cycles += 1
        else:
            s.fallback_cycles += 1
            if r.llm_error_kind:
                s.error_kind_counts[r.llm_error_kind] = (
                    s.error_kind_counts.get(r.llm_error_kind, 0) + 1
                )
            if r.llm_error_kind in ENVIRONMENTAL_ERROR_KINDS:
                s.environmental_fallbacks += 1
            if r.llm_error_kind == "timeout":
                s.timeouts += 1
        # A parse is "attempted" exactly when claude returned ok=True: that is
        # the llm-success path (parse_ok=True) or a parse-error fallback.
        if r.path_taken == "llm" or r.llm_error_kind == "parse-error":
            s.parse_attempts += 1
            if r.parse_ok:
                s.parse_ok += 1
    return s


# ---------------- CLI ----------------


def _cli(argv: list[str] | None = None) -> int:
    """Print the readiness summary for a telemetry ledger.

    Usage:
        uv run python docs/tools/inner_agent_telemetry.py summary <path>
    """
    import argparse

    p = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    ps = sub.add_parser("summary", help="Print the R2–R5 readiness numbers.")
    ps.add_argument("path", type=Path)
    args = p.parse_args(argv)

    if args.cmd == "summary":
        s = summarize(read_records(args.path))
        print(
            f"cycles={s.cycles} llm={s.llm_cycles} fallback={s.fallback_cycles} "
            f"(env={s.environmental_fallbacks})"
        )
        print(f"R2 fallback_rate    = {s.fallback_rate:.3f}  (GO ≤ 0.20)")
        print(f"R3 parse_success    = {s.parse_success_rate:.3f}  (GO ≥ 0.90)")
        print(f"R4 timeout_rate     = {s.timeout_rate:.3f}  (GO ≤ 0.10)")
        print(f"R5 mean_tokens/llm  = {s.mean_tokens_per_llm_cycle:.0f}  (GO ≤ 250000)")
        print(
            f"   mean_$/llm_cycle  = ${s.mean_cost_per_llm_cycle:.4f}  "
            f"(over {s.exact_cost_cycles} exact-cost cycles; total ${s.total_cost_usd:.4f})"
        )
        print(f"   mean_wall_clock  = {s.mean_wall_clock_s:.1f}s")
        if s.error_kind_counts:
            kinds = ", ".join(f"{k}={v}" for k, v in sorted(s.error_kind_counts.items()))
            print(f"   error_kinds      = {kinds}")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(_cli())
