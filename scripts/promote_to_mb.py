"""Promote a curated solution file from results/polish-trail/ to the workbench MB.

This is the ONLY sanctioned way to add files to memory-bank/einstein/docs/<problem>/solutions/.
Every file in MB should have a human who said "this matters."

Usage:
    uv run python scripts/promote_to_mb.py <source-file> \\
        --tag milestone-id1315 --score 1.5263e-13

    # Dry run:
    uv run python scripts/promote_to_mb.py <source-file> \\
        --tag reserve-ulp-1.5263 --score 1.5263e-13 --dry-run

    # Force overwrite:
    uv run python scripts/promote_to_mb.py <source-file> \\
        --tag sota-chronos-id1149 --score 0.156 --force
"""

from __future__ import annotations

import argparse
import re
import shutil
import time
from pathlib import Path

KNOWN_PREFIXES = {"milestone", "reserve", "sota", "submitted"}
DEFAULT_MB_ROOT = Path.home() / "projects" / "workbench" / "memory-bank" / "einstein"


def dest_filename(tag: str, score: float) -> str:
    """Compute destination filename from tag and score.

    If tag starts with a known prefix (milestone, reserve, sota, submitted),
    use that as the file prefix and strip it from the tag label.
    Otherwise, use 'promoted' as the default prefix.
    """
    parts = tag.split("-", 1)
    if parts[0] in KNOWN_PREFIXES and len(parts) > 1:
        prefix = parts[0]
        label = parts[1]
    else:
        prefix = "promoted"
        label = tag

    today = time.strftime("%Y-%m-%d")
    return f"{prefix}-{today}-{label}-{score}.json"


def derive_problem(source_path: str) -> str | None:
    """Extract problem directory name from a source path.

    Looks for 'problem-N-name' in the path components.
    """
    for part in Path(source_path).parts:
        if re.match(r"problem-\d+-", part):
            return part
    return None


def promote(
    source: Path,
    tag: str,
    score: float,
    problem: str,
    force: bool,
    dry_run: bool,
    mb_root: Path = DEFAULT_MB_ROOT,
) -> Path:
    """Copy source file to MB solutions dir and append experiment-log entry.

    Returns the destination path.
    """
    source = Path(source)

    # Safety: refuse non-JSON without --force
    if source.suffix.lower() != ".json" and not force:
        raise ValueError(f"Refusing to promote non-JSON file: {source.name}. Use --force to override.")

    # Safety: check for suspicious path chars in tag
    if ".." in tag or "/" in tag or "\x00" in tag:
        raise ValueError(f"Suspicious characters in tag: {tag!r}")

    # Compute destination
    fname = dest_filename(tag, score)
    solutions_dir = mb_root / "docs" / problem / "solutions"
    dest = solutions_dir / fname

    # Safety: refuse clobber without --force
    if dest.exists() and not force:
        raise FileExistsError(f"Destination already exists: {dest}. Use --force to overwrite.")

    # Experiment log entry
    log_file = mb_root / "docs" / problem / "experiment-log.md"
    log_line = f"- {time.strftime('%Y-%m-%d')} promoted {tag} @ {score} from {source.name} → {fname}"

    if dry_run:
        print(f"[DRY RUN] Would copy: {source} → {dest}")
        print(f"[DRY RUN] Would append to {log_file}: {log_line}")
        return dest

    # Ensure destination directory exists
    solutions_dir.mkdir(parents=True, exist_ok=True)

    # Copy (not move — preserve source)
    shutil.copy2(source, dest)

    # Append to experiment log (idempotent — skip if line already present)
    if log_file.exists():
        existing = log_file.read_text()
        if log_line not in existing:
            with open(log_file, "a") as f:
                f.write(f"\n{log_line}")
    else:
        log_file.write_text(f"# Experiment Log\n\n{log_line}\n")

    print(f"Promoted: {source} → {dest}")
    print(f"Log entry: {log_line}")
    return dest


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Promote a curated solution file to the workbench memory bank.",
    )
    parser.add_argument("source", type=Path, help="Path to the solution file to promote")
    parser.add_argument("--tag", required=True, help="Human-meaningful label (e.g., milestone-id1315)")
    parser.add_argument("--score", required=True, type=float, help="Score associated with this solution")
    parser.add_argument(
        "--problem",
        default=None,
        help="Target problem directory in MB (default: derived from source path)",
    )
    parser.add_argument("--force", action="store_true", help="Allow overwriting existing destination")
    parser.add_argument("--dry-run", action="store_true", help="Print planned action, don't touch filesystem")
    args = parser.parse_args()

    if not args.source.exists():
        parser.error(f"Source file does not exist: {args.source}")

    problem = args.problem
    if problem is None:
        problem = derive_problem(str(args.source))
        if problem is None:
            parser.error(
                "Could not derive problem name from source path. "
                "Use --problem to specify explicitly."
            )

    promote(
        source=args.source,
        tag=args.tag,
        score=args.score,
        problem=problem,
        force=args.force,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
