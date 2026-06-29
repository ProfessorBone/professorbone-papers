# Constitutional Runtime Computation: Series Overview

**Author:** Clarence "Faheem" Downs (Professor Bone Lab)

---

## The Central Argument

Most agentic systems treat governance as an external corrective layer applied
after an agent has already reasoned and acted. This series proposes a different
architecture: a Constitutional Runtime Substrate in which governance defines the
topology of reachable state transitions before any action occurs.

Under this model, agents no longer hold terminal execution sovereignty. An agent
observes, reasons, and submits a typed transition proposal. The substrate
adjudicates whether that transition is constitutionally reachable from current
state. This reconstructs the traditional Observe-Reason-Act loop into
Observe-Reason-Submit-Resolve (ORSR).

---

## Series Structure

This is a living series. The core paper defines the foundational architecture.
Companion papers mature it by closing specific identified gaps. Domain application
documents demonstrate the architecture operating under real constraints.

### Core Paper

- [Constitutional Runtime Computation v5.3](constitutional-runtime-computation-v5.3.md)
  The foundational paper. Introduces ORSR, CTLC, L1/L2 governance separation,
  the Q/P constitutional ontology, and the Constitutional Engineering Lifecycle.

### Companion Papers

Companion papers extend the core architecture. Each addresses a gap that the
core paper identifies but does not close.

- [Constitutional Memory v2.1](companions/constitutional-memory-v2.1.md)
  Companion 1. Argues that the substrate's authority over state transitions
  extends necessarily to memory. If the substrate owns the present transition,
  it must also own the record of past transitions and the conditions under
  which they shape future ones.

- [Constitutional Retrieval: Memory View Issuance and Observe Construction
  in Governed Agentic Systems](companions/constitutional-retrieval-v1.2.md)
  Companion 2. Argues that retrieval is not access but the construction of
  Observe, the entrance to every ORSR cycle. Where Constitutional Memory
  governs whether a memory view may be issued, this paper governs how the
  issued view is constructed: how it is ranked, scoped, summarized,
  compressed, and assembled. It closes the cross-cycle feedback loop on the
  read side, completing what the memory companion closed on the write side.

- [Constitutional Baselines: Authority, Versioning, and Drift Measurement
  for Memory and Retrieval Governance](companions/constitutional-baselines-v1.2.md)
  Companion 3. Governs the external baselines that P_mem5 (write side) and
  P_ret5 (read side) both depend on but cannot move. Whoever can move the
  baseline controls whether drift is detectable at all, so the paper derives
  the Baseline Sovereignty Principle: baseline-change authority must reside in
  the sovereign, a baseline change is a typed, traced reconstitution act, and
  the baseline must be independent of the process it measures. It shows the
  regress terminates at the sovereign rather than an infinite monitoring tower,
  and it is the meta-level closure of the corpus's drift architecture.

- [Constitutional Coherence: Baseline Generations, Cross-Surface Consistency,
  and the Governance of Multi-Surface Drift](companions/constitutional-coherence-v1.2.md)
  Companion 4. Constitutional Baselines governs baseline authority one surface
  at a time, but the corpus has a family of baselines, and per-surface validity
  does not guarantee family coherence. This paper matures the BaselineGeneration
  into a constitutional object and derives the Generation Coherence Principle:
  coherence of the standard-set is sovereign-authored, not an emergent property
  of individually valid baselines. Its load-bearing contribution is the
  cross-surface non-masking property, the gate that catches a family in which
  every member baseline is valid yet one surface hides exactly what another
  surface expects to escalate.

- Constitutional Thresholds: Trigger Authority, Decision Boundaries, and
  Evidence-Packet Provenance in Governed Drift Monitoring *(forthcoming)*
  Companion 5. The corpus now governs the substrate, memory, retrieval, the
  per-surface baselines, and the coherence of the baseline family. This paper
  will take up the two human-interface residues named and scoped out across
  Constitutional Baselines v1.2 and Constitutional Coherence v1.2: the
  threshold-authority problem (the baseline, metric, threshold, and trigger
  distinction, and threshold capture, in which a doctrine-grounded baseline is
  blinded by a quietly raised decision boundary) and the evidence-packet-provenance
  problem behind mediated capture (whether the briefing through which a sovereign
  decides traces to the monitored process), which Constitutional Coherence v1.2
  elevated to a deployment precondition. The two meet at the cross-surface
  threshold, the seam at which threshold authority and the coherence of the
  standard-set become one question.

### Domain Applications

Domain application documents show the CRC architecture instantiated in
specific systems under real engineering and operational constraints.
These are not implementation guides. They are architectural records.

- [Apex Architecture Seed](domain-applications/apex-architecture-seed.md)
  The founding insight: that constitutional reachability computation and
  knowledge-graph traversal are structurally identical operations on
  different graph encodings. This convergence is the architectural origin
  of Apex.

- [Apex Build Specification v0.5](domain-applications/apex-build-spec-v0.5.md)
  CRC applied end to end in a constitutionally governed bug bounty research
  architecture. Shows ORSR, CTLC, L1/L2 separation, memory governance, and
  the full constitutional spine operating under domain-specific constraints.
  See the document's own preamble for notes on maturity and stub status.

### Historical Companions

These papers were written against earlier versions of the CRC architecture.
They remain part of the intellectual lineage of the series.

- [The Knowledge Graph as Constitutional Substrate](companions/knowledge-graph-as-substrate.md)
  Written as a companion to CRC v3.0. Argues that constitutional reachability
  is structurally graph traversal, and that a knowledge graph is therefore the
  natural implementation substrate. This insight was later generalized and
  carried forward into the Apex architecture.

---

## Recommended Reading Order

1. Constitutional Runtime Computation v5.3 (core)
2. Constitutional Memory v2.1 (companion 1)
3. Constitutional Retrieval v1.2 (companion 2)
4. Constitutional Baselines v1.2 (companion 3)
5. Constitutional Coherence v1.2 (companion 4)
6. Apex Architecture Seed (domain application, short)
7. Apex Build Specification v0.5 (domain application, full)
8. The Knowledge Graph as Constitutional Substrate (historical lineage)
