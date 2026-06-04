---
type: question
author: agent
asked_by: tao
drafted: 2026-06-04
status: open
related_problems: [3]
---

# Tao — P3 headroom: what is the obstruction to a score-preserving downsample, named precisely

The single obstruction: a high-res f scores 0.9627 locally but that number does not
transfer to a 100k arena submission, and naive decimation destroys the function. I want
to name the obstruction at the Fourier/scale level, not just observe it.

1. **Is the score loss under downsampling an aliasing phenomenon — i.e., does f★f have
   energy above the 100k Nyquist frequency, and is that the entire ‖·‖∞-vs-‖·‖₂ shift?**
   Why it matters: if the loss is aliasing, an ideal anti-aliased (band-limited) downsample
   is *provably* the right operator and the question reduces to "low-pass f★f below 100k
   Nyquist, then resample." A good answer is the power spectrum of the SOTA autoconvolution
   with the fraction of L2 energy above the 100k Nyquist quoted as a number.

2. **Does the autoconvolution commute usefully with downsampling — i.e., is
   downsample(f)★downsample(f) ≈ downsample(f★f) for a band-limited kernel, or does the
   quadratic ★ generate new high-frequency content that no f-side kernel can pre-empt?**
   Why it matters: the score depends on f★f, but we can only submit f; if ★ injects
   frequencies above Nyquist that depend on f's fine structure, then NO f-side downsample
   preserves the score and the high-res path is structurally dead (a real finding either way).
   A good answer is a numerical commutator norm ‖down(f)★down(f) − down(f★f)‖ vs kernel bandwidth.

3. **Decompose f into a structured (sparse-block) part plus a pseudo-random fine part:
   which part carries the 4e-4 headroom?** Why it matters: prior work shows the SOTA basin
   is sparse-block with ~274k active points; if the headroom lives in the structured part it
   survives a 100k downsample, if it lives in the fine pseudo-random part it is the
   un-submittable resolution artifact. A good answer attributes the C2 contribution to each
   part by zeroing one and re-scoring.
