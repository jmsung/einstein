#!/usr/bin/env python3
"""claude_headless.py — shared `claude -p` subprocess wrapper.

Single source of truth for headless Claude Code invocations. Callers today:

  - `llm_distill.py`        — distill papers into source/. Text output, no tools.
  - `inner_agent.py` (7.2)  — autonomous-loop inner cycle. Tool allow-list,
                              optional JSON output with schema validation.

Goal 7.2 of `mb/active/feat-autonomous-loop.md`. The point of the extraction
is to keep the auth/quota detection, timeout handling, and CLI-flag glue in
one place so the two callers don't drift.

Anti-goals:
  - Streaming output. Use `claude -p --output-format stream-json` directly if
    you need it; this wrapper assumes one-shot stdout capture.
  - Interactive sessions. Plain `claude` covers that.

Error model: `run()` raises nothing on Claude failures. Every failure mode
lands as `HeadlessResult(ok=False, error_kind=<tag>)`. Callers decide whether
to retry / back off / abort the cycle.

  error_kind values
    ""             ok
    "unavailable"  auth / quota / 429 / overload — back off, don't retry hard
    "timeout"      wall-clock budget exceeded — partial stdout may be present
    "non-zero"     anything else (CLI flag misuse, internal claude bug)
"""

from __future__ import annotations

import logging
import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

log = logging.getLogger("claude_headless")


DEFAULT_MODEL = "claude-opus-4-7[1m]"
DEFAULT_TIMEOUT_SECONDS = 180


# ---------------- error tags ----------------


class ClaudeHeadlessError(RuntimeError):
    """Base error for callers that prefer exceptions over result inspection.

    `run()` itself never raises this — it's a convenience for shrink_to_error
    semantics in higher layers (e.g. `llm_distill.DistillError`).
    """


# Lower-cased substrings on stdout/stderr that mean "Claude Code is
# temporarily unavailable, not that the request was wrong." Detected on
# either stream because claude -p sometimes prints the message to stdout
# with a zero exit code (looks superficially like success).
_UNAVAILABLE_PATTERNS = (
    "you've hit your session limit",
    "usage-credits",
    "failed to authenticate",
    "invalid authentication credentials",
    "not logged in",
    "please run /login",
    "api error: 401",
    "api error: 429",
    "overloaded",
)


def _is_unavailable(text: str) -> bool:
    if not text:
        return False
    lower = text.lower()
    return any(p in lower for p in _UNAVAILABLE_PATTERNS)


# ---------------- result ----------------


@dataclass
class HeadlessResult:
    """One headless invocation's outcome."""

    ok: bool
    stdout: str = ""
    stderr: str = ""
    returncode: int = 0
    cmd: list[str] = field(default_factory=list)
    error_kind: str = ""  # "" | "unavailable" | "timeout" | "non-zero"
    error_message: str = ""

    def raise_for_error(self, exc_cls: type[Exception] = ClaudeHeadlessError) -> None:
        """Raise `exc_cls(error_message)` if not ok. No-op otherwise.

        Lets callers opt into exception-style flow without losing the
        structured fields when they want to inspect them first.
        """
        if not self.ok:
            raise exc_cls(self.error_message or f"claude -p failed: kind={self.error_kind}")


# ---------------- run ----------------


def _decode(b: bytes | str | None) -> str:
    if b is None:
        return ""
    if isinstance(b, str):
        return b
    return b.decode(errors="replace")


def run(
    prompt: str,
    *,
    model: str = DEFAULT_MODEL,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
    allowed_tools: list[str] | None = None,
    output_format: str = "text",  # text | json | stream-json
    json_schema: str | None = None,
    max_budget_usd: float | None = None,
    permission_mode: str | None = None,  # acceptEdits | auto | ...
    fallback_model: str | None = None,
    system_prompt: str | None = None,
    append_system_prompt: str | None = None,
    add_dirs: list[Path] | None = None,
    extra_args: list[str] | None = None,
    env: dict[str, str] | None = None,
    cwd: Path | None = None,
    claude_bin: str = "claude",
) -> HeadlessResult:
    """Invoke `claude -p <prompt>` once and return a structured result.

    No exception path for Claude failures — see error_kind on the result.
    Subprocess-level errors (binary not found, permission denied launching)
    raise `FileNotFoundError` / `PermissionError` from the OS layer.

    Args:
        prompt: the full prompt body (last positional arg to claude).
        model: claude --model. Default Opus 4.7 1M-context.
        timeout_seconds: wall-clock cap. subprocess.run reaps the child on
            timeout. For long cycles (Goal 7.5) pass 1800+.
        allowed_tools: list passed to --allowedTools. Use the same syntax the
            CLI accepts, e.g. `["Read", "Grep", "Bash(qmd:*)", "Task"]`.
            None → claude uses its default allow-list.
        output_format: --output-format. "json" gives a single JSON document;
            "stream-json" emits incremental events (use the CLI for that).
        json_schema: --json-schema. Only honored when output_format="json".
        max_budget_usd: --max-budget-usd (only meaningful with -p).
        permission_mode: --permission-mode. "acceptEdits" avoids prompts for
            edits; the autonomous loop usually wants "default" because
            wiki/mb writes are mediated via the orchestrator (Goal 7.6).
        fallback_model: --fallback-model. Auto-switch on overload.
        system_prompt / append_system_prompt: optional.
        add_dirs: extra dirs claude is allowed to read.
        extra_args: escape hatch — appended verbatim before the prompt.
        env: env vars merged over os.environ.
        cwd: working directory for the subprocess.
        claude_bin: override the binary name (tests pass a stub script).

    Returns:
        HeadlessResult — ok=True on a clean run; ok=False with error_kind set
        otherwise. See module docstring for error_kind taxonomy.
    """
    cmd: list[str] = [claude_bin, "-p", "--model", model]

    if allowed_tools:
        # Pass as a single comma-joined arg. Even comma-form is necessary
        # but not sufficient — `--allowedTools` is variadic (`<tools...>`
        # in commander.js) and consumes ALL following positionals up to
        # the next flag, INCLUDING the prompt. Comma-join + the `--`
        # separator below (inserted before the prompt) makes the boundary
        # explicit and the prompt unambiguous. Without both, `claude -p`
        # exits 1 with "Input must be provided either through stdin or as
        # a prompt argument".
        cmd.extend(["--allowedTools", ",".join(allowed_tools)])
    if output_format != "text":
        cmd.extend(["--output-format", output_format])
    if json_schema:
        cmd.extend(["--json-schema", json_schema])
    if max_budget_usd is not None:
        cmd.extend(["--max-budget-usd", str(max_budget_usd)])
    if permission_mode:
        cmd.extend(["--permission-mode", permission_mode])
    if fallback_model:
        cmd.extend(["--fallback-model", fallback_model])
    if system_prompt:
        cmd.extend(["--system-prompt", system_prompt])
    if append_system_prompt:
        cmd.extend(["--append-system-prompt", append_system_prompt])
    if add_dirs:
        cmd.append("--add-dir")
        cmd.extend(str(p) for p in add_dirs)
    if extra_args:
        cmd.extend(extra_args)

    # `--` makes the prompt unambiguous: any preceding variadic flag (e.g.
    # `--allowedTools <tools...>`) stops eating positionals here. Cheap
    # insurance that costs nothing when no variadic flag is present.
    cmd.extend(["--", prompt])

    log.debug(
        "claude_headless: %s ... (prompt %d chars, timeout %ds)",
        cmd[:6],
        len(prompt),
        timeout_seconds,
    )

    full_env = os.environ.copy()
    if env:
        full_env.update(env)

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            env=full_env,
            cwd=cwd,
        )
    except subprocess.TimeoutExpired as e:
        return HeadlessResult(
            ok=False,
            cmd=cmd,
            stdout=_decode(e.stdout),
            stderr=_decode(e.stderr),
            error_kind="timeout",
            error_message=(
                f"claude -p timed out after {timeout_seconds}s "
                f"(partial stdout {len(_decode(e.stdout))} chars)"
            ),
        )

    stdout = proc.stdout or ""
    stderr = proc.stderr or ""

    # Auth/quota first — these can land with exit 0 + an error message on
    # stdout, so checking returncode alone misses them.
    if _is_unavailable(stdout) or _is_unavailable(stderr):
        return HeadlessResult(
            ok=False,
            cmd=cmd,
            stdout=stdout,
            stderr=stderr,
            returncode=proc.returncode,
            error_kind="unavailable",
            error_message="Claude Code unavailable: auth, quota, or 429/overload",
        )

    if proc.returncode != 0:
        # Keep the tail of stderr (or stdout if stderr is empty) so callers
        # can surface a useful message without dumping megabytes.
        detail = (stderr or stdout)[-500:].strip() or "unknown"
        return HeadlessResult(
            ok=False,
            cmd=cmd,
            stdout=stdout,
            stderr=stderr,
            returncode=proc.returncode,
            error_kind="non-zero",
            error_message=f"claude -p exit {proc.returncode}: {detail}",
        )

    return HeadlessResult(
        ok=True,
        cmd=cmd,
        stdout=stdout,
        stderr=stderr,
        returncode=0,
    )
