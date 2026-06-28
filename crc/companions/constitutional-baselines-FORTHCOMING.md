# Constitutional Baselines: Authority, Versioning, and Drift Measurement for Memory and Retrieval Governance

*This companion paper is currently in development.*

It will address the baseline-authority dependency that Constitutional Memory
v2.1 and Constitutional Retrieval v1.2 both leave open. Several mature drift
primitives, P_mem5 (constitutional drift through accumulated writes) on the
write side and P_ret5 (constructional narrowing) on the read side, together
with the full L2 construction-fidelity layer, are structurally specified but
operationally incomplete because each measures against an external baseline
that the monitored process itself cannot move.

This companion will give that baseline its own constitutional account: who
authorizes a baseline, how it is versioned, how an authorized baseline change
is distinguished from the drift the baseline is meant to detect, and how drift
is measured against it. It will unify the write-side and read-side
baseline-authority problems as instances of one question, governing the thing
against which drift is measured, since a baseline that can be moved to track
the drift it is meant to detect is no baseline at all on either side.

Series position: Companion 3 to Constitutional Runtime Computation v5.3,
continuing the memory and retrieval companions. Seeded by the
P_mem5 baseline-authority problem (Constitutional Memory v2.1) and the
shared baseline-authority problem named in Constitutional Retrieval v1.2.
