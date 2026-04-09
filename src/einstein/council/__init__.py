"""Mathematician council — dispatch scaffolding for research subagents.

The council is a panel of mathematician personas (Gauss, Riemann, Tao,
Conway, Euler, Poincaré, Erdős, Noether, Cohn, Razborov, plus a
specialist bench) used to seed parallel research subagents during the
Recon goal of a new problem.

This package is intentionally a thin scaffold: persona content (prompt
seeds, trigger rules, literature focus) lives in a private config file
loaded at runtime. The public package only exposes the data shape and
dispatch logic.

Typical usage:

    from einstein.council import dispatch

    for persona in dispatch("kissing_number"):
        # seed a subagent prompt with persona.prompt_seed
        ...
"""

from einstein.council.personas import Persona, dispatch, load_personas

__all__ = ["Persona", "dispatch", "load_personas"]
