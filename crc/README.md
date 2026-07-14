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

- [Constitutional Runtime Computation v5.14](constitutional-runtime-computation-v5.14.md)
  The foundational paper. Introduces ORSR, CTLC, L1/L2 governance separation,
  the Q/P constitutional ontology, and the Constitutional Engineering Lifecycle.
  v5.4 adds §6a, formalizing HOLD verdict completeness (non-formation,
  non-replayability, non-bypassability) as an invariant rather than an
  asserted norm; it does not change CTLC's Reachable(τ) predicate or the
  Emit and Escalate paths that every companion below builds on. v5.11 formalizes
  Core ownership of AgentObservation and publishes its canonical schema. v5.12
  formalizes Core ownership of ContinuationState and publishes its canonical
  schema. ContinuationState outcome lineage reconstructs through Resolution,
  CycleRecord, Task Ledger, and audit trace, with no `derived_from_ref` field.
  v5.13 publishes the generic F-5 apparatus connecting Resolution(Emit) to
  substrate-owned ActuationCommand issuance, ActuationResult recording,
  ActuationAdmissionRecord, GovernedStateMutationRecord, and the dependency
  contract for later BindingRecord reconciliation. v5.14 establishes Core
  ownership of canonical BindingRecord and BindingRecordValid. Binding occurs
  at valid applied governed mutation. BindingRecord records and proves binding
  without creating it. F-3 is RESOLVED in CRC-OAR v1.4.

### Companion Papers

Companion papers extend the core architecture. Each addresses a gap that the
core paper identifies but does not close.

- [Constitutional Boundary Contracts: Governed Interface Exchange at the
  Agent-Substrate Boundary](companions/constitutional-boundary-contracts-v1.3.md)
  Companion 0. Foundational interface companion. ORSR produces two primary
  governed boundaries in the core agent-substrate loop: Agent-to-Substrate
  (TransitionProposal) and Substrate-to-Agent (AgentObservation). This paper
  argues that boundary crossings are constitutional events, not transport
  events, and establishes typed contracts for both. Contributions include the
  Boundary Sovereignty Principle, ProposalContract and ObservationContract with
  full schemas and validation predicates, the BoundaryValidationFunction as a
  constitutionally separated substrate component, a six-class violation severity
  taxonomy (B0-B5), and five boundary-specific primitive failure topologies
  (P_bnd). v1.3 clarifies that C0 owns ObservationContract and
  ObservationConformant, validates the crossing representation of the Core-owned
  AgentObservation, and retains `contract_version` as C0 crossing metadata
  without creating a new envelope object. Logically prior to all subsequent
  companions. May be read immediately after the core paper.

- [Constitutional Memory v2.2](companions/constitutional-memory-v2.2.md)
  Companion 1. Argues that the substrate's authority over state transitions
  extends necessarily to memory. If the substrate owns the present transition,
  it must also own the record of past transitions and the conditions under
  which they shape future ones. v2.2 adds failure-derived learning and the
  Constitutional Feedback Loop: a Hold may become a learning signal only
  through a substrate-mediated LearningCandidate, never through private
  agent reflection, overgeneralization, or learned bypass.

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
  and the Governance of Multi-Surface Drift](companions/constitutional-coherence-v1.4.md)
  Companion 4. Constitutional Baselines governs baseline authority one surface
  at a time, but the corpus has a family of baselines, and per-surface validity
  does not guarantee family coherence. This paper matures the BaselineGeneration
  into a constitutional object and derives the Generation Coherence Principle:
  coherence of the standard-set is sovereign-authored, not an emergent property
  of individually valid baselines. Its load-bearing contribution is the
  cross-surface non-masking property, the gate that catches a family in which
  every member baseline is valid yet one surface hides exactly what another
  surface expects to escalate.

- [Constitutional Thresholds: Trigger Authority, Decision Boundaries, and
  Evidence-Packet Provenance in Governed Drift Monitoring](companions/constitutional-thresholds-v1.4.md)
  Companion 5. Closes the threshold-authority and evidence-packet-provenance
  residues named and scoped out across Constitutional Baselines v1.2 and
  Constitutional Coherence v1.2. It distinguishes four objects the corpus had
  treated as one, the baseline, the metric, the threshold, and the trigger, and
  derives the Trigger Authority Principle: whoever can move the threshold or
  the trigger controls whether an honestly measured deviation ever produces
  action, so threshold and trigger authority must be sovereign. It also extends
  Constitutional Boundary Contracts v1.1's boundary-contract pattern to the
  evidence-packet-to-sovereign crossing with the EvidencePacketContract,
  closing the mechanically detectable form of the mediated-capture deployment
  precondition Constitutional Coherence v1.2 named, while naming evidentiary
  sufficiency and candidate-selection capture as a distinct, still-open form.
  Threshold capture is identified as a third, independent axis of false
  stability alongside baseline capture's vertical axis and family incoherence's
  horizontal axis.

- [Constitutional Standing: Formation, Binding, and Non-Formation in Governed
  Runtime Transitions](companions/constitutional-standing-v1.7.md)
  Companion 6. Formalizes the Standing (STAND) step CTLC's own CRA Assembly
  has named since its earliest formalization but specified only as a single
  sentence, and substantially advances, though does not complete, the
  task-state continuity residue named directly in Constitutional Runtime
  Computation v5.4's Open Problems. It separates five stages the corpus had
  touched but never organized into one pipeline, Formation, Standing,
  Reachability, Binding, and Continuation, none of which entails the others.
  FormationValid(π) and the NonFormationReceipt build on Constitutional
  Boundary Contracts v1.0 and Constitutional Memory v2.2; ContinuationIssued
  and the ContinuationState close the private-continuation failure mode named
  directly in the parent's Open Problems. v1.7 aligns Standing to F-3:
  Standing owns standing applicability, positive non-applicability evidence,
  standing validation evidence, StandingFailureRecord, and historical standing
  timing. Core v5.14 owns BindingRecord and BindingRecordValid.
  Cumulative Standing Creep is classified, against an explicit
  four-part test, as the corpus's fourth sovereign-terminal primitive, after
  Constitutional Baselines v1.2, Constitutional Coherence v1.2, and
  Constitutional Thresholds v1.2's own contributions.

- [Constitutional Tools: Capability Invocation, External Effects, and
  Tool-Result Admission in Governed Agentic Systems](companions/constitutional-tools-v1.2.md)
  Companion 7. Sits alongside Constitutional Memory v2.2 as the other major
  agent-capability surface ORSR cannot leave ungoverned. Argues that tool
  invocation is a constitutional transition surface, not a neutral capability
  call: if the substrate owns terminal execution authority, that authority
  cannot stop at Act while tool invocation remains agent-owned, since a tool
  can retrieve, generate, transform, or misframe evidence, mutate substrate or
  external state, shape future Observe, and produce real-world effects. The
  agent does not call tools; it submits ToolInvocationProposals, and a tool
  result has no constitutional force merely because a tool produced it.
  Contributions include the Tool Sovereignty Principle, a seven-class
  tool-operation taxonomy by constitutional effect, ToolInvocationReachable(κ)
  and ToolResultAdmissible(ρ), the Tool Governance Boundary as a third instance
  of Constitutional Boundary Contracts v1.1's six-component pattern, and an
  eight-primitive P_tool family, with an explicit four-part sovereign-terminal
  test applied to the two strongest candidates and neither found to qualify.
  v1.2 aligns Tools to F-5: ToolInvocationProposal remains a proposal,
  ToolResultRecord specializes ActuationResult, ToolResultAdmissible specializes
  ActuationResultAdmissible, tool admission maps to ActuationAdmissionRecord,
  downstream tool effects conform to GovernedStateMutationRecord, and final
  tool binding consumes Core v5.14 BindingRecord lineage without expanding
  Tools authority.

- [Constitutional Task Ledger: Task State, Continuation, and Terminal Criteria
  in Governed Agentic Systems](companions/constitutional-task-ledger-v1.4.md)
  Companion 8. Argues that task continuity cannot live in agent memory:
  Constitutional Standing v1.3 named ContinuationState, ContinuationIssued,
  TaskActive, and CycleCurrent as vocabulary without specifying the governed
  task-state object they presuppose, and Constitutional Memory v2.2's cycle-
  closure model depends on a Task Ledger carrying pending obligations forward
  without that Ledger existing anywhere in the corpus. The agent does not own
  the task, does not decide what remains or when it is complete, and does not
  carry task continuity in private reasoning; the substrate owns task state,
  records progress, issues continuation, and defines terminal criteria.
  Contributions include the Constitutional Task Ledger Principle, seven
  governed objects (TaskLedger, PendingObligation, CycleRecord, TerminalCriteria,
  TaskClosureRecord, AllowedNextAffordanceSet, and a scaffolded
  ReconstitutionRecord) with PendingObligation established as first-class
  rather than a structured field, two independently evaluated predicates
  (TaskContinuationReachable and TaskClosureValid) kept separate in the manner
  of Constitutional Tools v1.1's own Emit and Admit separation, an obligation-
  carrying table with a governing no-silence rule, and an eight-primitive
  P_task family. Task-State False Stability (P_task8) is evaluated against
  the corpus's own four-part sovereign-terminal test and conditionally
  classified, given the current corpus's absence of a pinned
  TaskResolutionPracticeContract or equivalent, as the corpus's fifth formally
  named sovereign-terminal primitive, the opposite finding from Constitutional
  Tools v1.1's own strongest candidates. v1.3 aligns Task Ledger to F-5 by
  preserving CycleRecord outcome_type, expanding PendingObligation sources for
  admission, result, compensation, and audit-repair cases, and requiring every
  failed, rejected, unknown, partial, held, escalated, or verification-required
  actuation state to produce either a PendingObligation or an explicit
  no_obligation_reason. v1.4 aligns Task Ledger to F-3 by requiring
  CycleRecord Bind outcome_ref to point to BindingRecord, adding binding-closure
  repair obligations, and preserving CycleRecord outcome vocabulary.

- [Constitutional Feedback: Cross-Surface Learning and the Governance of
  Corpus-Wide Adaptation](companions/constitutional-feedback-v1.1.md)
  Companion 9. Generalizes Constitutional Memory v2.2's own Part IV-A
  feedback loop, Hold-derived learning only, across the further outcome
  types Constitutional Standing (NonFormationReceipt, StandingFailureRecord),
  Constitutional Tools (ToolResultHold), and Constitutional Task Ledger
  (PendingObligation, the shared population object that finally gives
  cross-surface feedback somewhere to land) have since produced, and opens a
  second, structurally distinct branch for whether a sovereign reconstitution
  already confirmed on one surface, a baseline re-anchoring, a generation
  re-cohering, a threshold recalibration, should propagate to a second
  surface's own standard. The two branches are kept deliberately separate
  rather than composed: operational feedback asks whether a governed outcome
  may become a scoped lesson, doctrinal feedback asks whether a sovereign
  correction should propagate, and a baseline reconstitution is a sovereign
  act rather than a failure awaiting one. Contributions include the
  Constitutional Feedback Principle, C9-owned OperationalLearningCandidate and
  OperationalFeedbackObservation objects for the operational branch, an
  explicit mapping from Memory's Hold-specific objects into the operational
  population, a new ReconstitutionFeedbackRecord with an explicit
  proposal-to-confirmation lifecycle for the doctrinal branch, and a shared
  FeedbackLedger indexing both under a governing no-silence rule.
  OperationalFeedbackSourceValid(σ)
  and FeedbackLearningReachable(λ) generalize Memory's own SourceHoldValid
  and FailureLearningReachable(λ); DoctrinalFeedbackReachable(δ) is new, with
  CrossSurfaceApplicabilityAssessed and AuthorityBoundaryPreserved as its
  load-bearing conjuncts, neither of which has any analogue in Memory's own
  apparatus. A six-primitive P_fbk family includes Cross-Surface Bypass
  Learning (P_fbk4), named as the primitive that most justifies this
  companion's own existence since no single surface's non-bypassability
  apparatus can see a lesson that moves its target effect to a different
  governed surface, and Feedback Corpus Drift (P_fbk6), tested against the
  corpus's own four-part sovereign-terminal test and recorded as a candidate,
  deliberately not entered into the formally named sovereign-terminal
  lineage, on the reasoning that an absence-of-a-fixed-reference argument can
  be invoked for nearly any new corpus-wide drift problem.

- [Constitutional Actuation and Effect Admission](companions/constitutional-actuation-and-effect-admission-v1.0.md)
  Companion 10. Provides the F-5 branch mechanics and conformance doctrine for
  Core v5.13's generic actuation apparatus. It defines how substrate-owned
  actuation commands, attempts, results, admission decisions, governed state
  mutations, failure handling, replay, retry, idempotency, compensation,
  rollback, and audit durability connect adjudicative authorization to governed
  causal force. It does not own Core sovereignty, BindingRecord schema, Tools,
  Task Ledger, Standing, Memory, or domain semantics. F-3 is RESOLVED in
  CRC-OAR v1.4, and the F-5 apparatus entries are RESOLVED in CRC-OAR v1.4.

### Governance Artifacts

Governance artifacts are not papers in the conceptual reading order; they are corpus-level control surfaces that the papers are read against.

- [CRC Open Architecture Register v1.4](open-architecture-register-v1.4.md)
  A standalone governance-operational and historical artifact for tracking
  unresolved findings, missing apparatus, blocked dependencies, and closure
  state. CRC-OAR provides an Obsidian-like unresolved-link function for the
  corpus without making unresolved concepts canonical or normatively usable.
  CRC-OAR v1.4 is active after publication. OAR-F003 is RESOLVED. OAR-F005
  remains RESOLVED. OAR-A001, OAR-A002, OAR-P001, OAR-A003, and OAR-X001
  through OAR-X005 are RESOLVED. The F-3/F-5 OAR workstream is
  lifecycle-closed. No doctrine or schema version changed in this lifecycle
  package. Unrelated OAR entries are not affected. CRC-OAR does not define
  canonical schemas or doctrine. CRC-SSR remains the artifact that tracks
  canonical shared-object locations and operative versions.

- [CRC Shared Schema Registry v1.6](shared-schema-registry-v1.6.md)
  A standalone governance artifact authorized by Core Appendix B B.9 and active as the registry of record by pointer for the corpus's shared load-bearing objects. CRC-SSR v1.1 carried the activation transition from the validated v1.0 seed; v1.6 is the current post-activation governed registry update. For REGISTERED objects it records the settled owner, operative version, and canonical location. For unresolved objects it records the honest ambiguity or divergence, candidate loci, and reconciliation dependency without asserting a canonical pointer. v1.3 records the F-2 reconciliation: Core owns canonical AgentObservation, C0 validates the crossing representation, `contract_version` remains C0 crossing metadata, and no new envelope object is introduced. v1.4 records the F-1 reconciliation: Core owns canonical ContinuationState, Standing owns continuation predicates and standing-local records, Task Ledger owns authoritative task state, no `derived_from_ref` exists, and outcome lineage reconstructs through Resolution, CycleRecord, Task Ledger, and audit trace. v1.5 registers ActuationCommand, ActuationResult, ActuationAdmissionRecord, and GovernedStateMutationRecord as Core-owned F-5 shared objects. v1.6 resolves `crc-ssr:binding-record` to REGISTERED with Core v5.14 as owner, Standing v1.7 as standing elaboration, and Task Ledger v1.4 as consumer. CRC-OAR v1.4 records formal closure of the F-3/F-5 OAR workstream. It holds no schema text: every definition stays in its defining paper. CRC-SSR sits outside the conceptual reading order.

### Corpus Governance and Entry

- [How to Enter the CRC Corpus](corpus-entry/README.md)
  The public entry point for corpus orientation, artifact admission, new-paper
  integration, amendment discipline, validation, publication, and
  corpus-engineering methodology.

### Methodology Papers

- [Constitutional Corpus Engineering v1.0](methodology/constitutional-corpus-engineering-v1.0.md)
  Explanatory methodology paper and CRC case-study synthesis. It explains how
  distributed technical papers can be transformed into a governed, coherent
  knowledge architecture through ownership mapping, authority boundaries,
  registry discipline, open-architecture lifecycle tracking, publication gates,
  historical preservation, and active navigation. It is not CRC runtime doctrine
  and does not govern corpus-entry procedure.

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

## Public Artifacts and Corpus Admission

A file does not become part of the CRC corpus merely because it is useful,
complete, or present in a working directory. Entry into the tracked public surface
is a governed act. Tracked artifacts may carry different roles and levels of
authority: normative artifacts carry doctrine; governance artifacts define how
the corpus operates and may carry a bounded authority effect; evidentiary
artifacts record validation or audit evidence; navigational artifacts control
discoverability; explanatory artifacts clarify the corpus without replacing
doctrine; operational templates standardize work without settling substantive
questions.

Not every tracked file is doctrinal authority. Readers should consult the
artifact's type, status, version, and authority statement before treating it as
operative. The admission rules for new papers, amendments, registries, receipts,
guides, diagrams, templates, and other public artifacts are defined in
[How to Enter the CRC Corpus](corpus-entry/README.md).

---

## Recommended Reading Order

1. Constitutional Runtime Computation v5.5 (core)
2. Constitutional Boundary Contracts v1.3 (companion 0, foundational interface)
3. Constitutional Memory v2.2 (companion 1)
4. Constitutional Retrieval v1.2 (companion 2)
5. Constitutional Baselines v1.2 (companion 3)
6. Constitutional Coherence v1.4 (companion 4)
7. Constitutional Thresholds v1.4 (companion 5)
8. Constitutional Standing v1.7 (companion 6)
9. Constitutional Tools v1.2 (companion 7)
10. Constitutional Task Ledger v1.4 (companion 8)
11. Constitutional Feedback v1.1 (companion 9)
12. Constitutional Actuation and Effect Admission v1.0 (companion 10)
12. Apex Architecture Seed (domain application, short)
13. Apex Build Specification v0.5 (domain application, full)
14. The Knowledge Graph as Constitutional Substrate (historical lineage)
