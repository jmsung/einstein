"""P22 — kissing number in d=12.

The manifest entry is a ``stub_no_op`` recon dry-run (``--dry-run``) with no
real solution payload, so there is nothing to triple-verify yet. Register
honestly as *unavailable* rather than leave P22 out of the registry: gate 2
then hard-rejects any P22 candidate with ``reason="stub_no_op_no_solution"``
(honest-zero over fake-pass). Replace this with three real checks once the
first-order link-tangent + squeeze recipe emits a scored solution.
"""

from __future__ import annotations

from ..core import register

register(22, unavailable_reason="stub_no_op_no_solution")
