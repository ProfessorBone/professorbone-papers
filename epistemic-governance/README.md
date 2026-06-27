# Epistemic Governance — Cluster Overview

**Author:** Clarence "Faheem" Downs (Professor Bone Lab)

---

## The Central Problem

Agentic systems fail in a specific way that is poorly named in the literature.
An agent fails to act on information that was technically available to it, not
because retrieval failed, but because the information never became behaviorally
operative. Standard remediation adds more memory. That addresses the wrong layer.

This cluster of papers formalizes the problem: what does it mean for information
to be not just present but operative? And at what level does governance fail when
the component governing all agents is itself ungoverned?

---

## Papers

### Anchor Papers

- [Orchestrator Epistemic Capture v2](orchestrator-epistemic-capture-v2.md)
  Identifies and formalizes a governance failure mode that operates at the
  control plane rather than the data plane. When an orchestrator develops
  systematic biases through continuous exposure to the agents it governs,
  it does not produce bad answers. It produces a distorted understanding
  of what a bad answer is. Proposes a five-mechanism solution anchored by
  a meta-evaluation checkpoint outside the orchestrator's epistemic influence.

- [The Cognitive Horizon of an Agent v6](cognitive-horizon-v6.md)
  Introduces the cognitive horizon as a structural framework for diagnosing
  gating failures. Develops the control model: Cognition approximates State
  times Attention times Policy. Presents a three-question diagnostic protocol
  for isolating the layer at which a gating failure occurred.

- [Agent State in Agentic AI Systems v3](agent-state-framework-v3.md)
  Practitioner-oriented framework for working memory design, logging strategy,
  and multi-agent coordination. Extends the CoALA framework with actionable
  engineering guidance. Introduces the latent-state versus operative-state
  distinction as a design and debugging instrument.

### Validation Companion

- [Epistemic Governance Deep Research](epistemic-governance-deep-research.md)
  Independent deep research validation of the architectural claims made across
  this cluster. Grounds informal claims in established literature and surfaces
  the limits of that grounding honestly. Not a standalone paper. Read after
  the three anchor papers.

---

## Recommended Reading Order

1. Agent State Framework v3 (foundation, establishes operative vs. latent)
2. Cognitive Horizon v6 (extends the framework to gating failures)
3. Orchestrator Epistemic Capture v2 (applies it at the control plane)
4. Epistemic Governance Deep Research (validation companion)
