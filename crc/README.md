# Constitutional Runtime Computation — Series Overview

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

- Constitutional Retrieval: Memory View Issuance and Observe Construction
  in Governed Agentic Systems *(forthcoming)*
  Companion 2. Currently in development.

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
3. Apex Architecture Seed (domain application, short)
4. Apex Build Specification v0.5 (domain application, full)
5. The Knowledge Graph as Constitutional Substrate (historical lineage)
