# CRC Shared Schema Registry

**Identifier:** CRC-SSR
**Version:** v1.2
**Authority:** Authorized by Constitutional Runtime Computation, Appendix B, section B.9. Bounded by that appendix.

CRC-SSR records canonical location and operative-version authority for the corpus's shared load-bearing objects. It holds no schema text. Each defining paper carries the canonical definition of its objects; this registry records where that definition lives and at what version it is operative.

## Status of this registry

CRC-SSR is authorized, published, and active as the registry of record. The
activation was carried by the v1.0 to v1.1 transition under Constitutional
Runtime Computation v5.10 Appendix B B.10. That activation exercises the
validation receipt at crc/registry-receipts/crc-ssr-v1.0-activation-validation-receipt.md,
which records gate_verdict PASS, validated_commit 2691d3f, and validation_date
2026-07-11. The B.7 inaugural registry in Core Appendix B is retained as the
archived inaugural docket with its seven rows unchanged. Exactly one active
registry of record exists in the corpus at any time.

CRC-SSR v1.1 derives from the validated CRC-SSR v1.0 seed without alteration to
any of its twelve entry definitions, pointers, statuses, or histories. Version
v1.1 records only the registry's constitutional activation state and the authority
and receipt references supporting that transition.

CRC-SSR v1.2 is a post-activation governed registry update. It becomes the
current operative registry version through this ratified change set, while v1.1
remains preserved as the prior active version and historical activation version.
The inaugural activation receipt continues to evidence only the validated v1.0
seed and the v1.1 activation lineage. It is not claimed to validate the four new
v1.2 entries. The current registry contains sixteen entries total: the twelve
validated seed entries preserved from v1.1 and four post-activation F-4
reconciliation additions.

Activation history: v1.0 to v1.1 records activation of CRC-SSR as the active
registry of record under Constitutional Runtime Computation v5.10 Appendix B B.10,
supported by crc/registry-receipts/crc-ssr-v1.0-activation-validation-receipt.md.
Version history: v1.1 to v1.2 records the F-4 post-activation governed registry
update, adding four entries while preserving the activation lineage and the
twelve-entry seed history.

## What this registry is and is not

It is the active registry of record by pointer for shared load-bearing objects:
for each object it names the owner, the operative version, and the canonical
location, plus the governance metadata around that pointer. It does not duplicate
or relocate any schema, and it does not itself reconcile divergences. An object
with an unsettled canonical definition is recorded at AMBIGUOUS or DIVERGENT with
its unresolved state named, not with a definition invented for it.

## Status vocabulary

- REGISTERED: single clear owner, one operative definition, no unreconciled divergence. The normal authoritative state, and where a previously reconciled object settles, with its earlier RESOLVED closure preserved in the append-only history.
- AMBIGUOUS: registered, but the canonical defining locus or schema is not settled. The entry names candidate loci and does not assert a settled definition or version.
- DIVERGENT: a clearly operative owner, with another paper carrying an undeclared, non-operative divergent definition pending reconciliation.
- AMENDMENT_PENDING: a lawful amendment is declared but not yet complete, for example a missing B.3.1 back-reference or a routed but uncarried Core-binding amendment.
- RESOLVED: a closure transition, not a steady state. A reconciled object settles to REGISTERED, and its RESOLVED closure is preserved in the append-only history.
- DEPRECATED: retired under a deprecate amendment, retained with a superseded_by pointer.

## Pointer and authority rules

Before activation, a REGISTERED entry records a settled candidate pointer, the triple of defining_paper, operative_version, and defining_anchor, that has passed or awaits activation validation. After CRC-SSR is activated, that REGISTERED entry establishes the authoritative pointer. For an AMBIGUOUS, DIVERGENT, or AMENDMENT_PENDING entry the pointer is explicitly non-settling: operative_version is unresolved, defining_paper may be marked unsettled, defining_anchor is not asserted as canonical, and the candidate or competing loci and the reconciliation dependency are recorded in notes and extension_or_amendment_refs. schema_id is immutable across renames, paper moves, and canonical_name changes. Each entry carries an append-only history; updating a pointer or status appends to the history and does not erase the prior state.

## Registry entries

### crc-ssr:transition-proposal

- schema_id: crc-ssr:transition-proposal
- canonical_name: TransitionProposal
- object_kind: object (ten fields)
- defining_paper: Constitutional Runtime Computation (Core)
- operative_version: v5.9
- defining_anchor: Section 4, "This ten-field object is the canonical TransitionProposal for the corpus"
- authority_class: core_owned
- core_binding: core_bound
- consumers: Constitutional Boundary Contracts (validator via ProposalContract), Constitutional Tools (ToolInvocationProposal subtype), Constitutional Memory (MemoryOperationProposal subtype)
- dependency_surfaces: Boundary Contracts validator-consuming; Tools and Memory add subtypes, which are new objects rather than amendments
- extension_or_amendment_refs: none; the subtypes are new objects, not amendments of this object
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: the Core object is unchanged; subtypes extend by defining new objects that reuse it
- history: created at v1.0 publication, REGISTERED

### crc-ssr:resolution

- schema_id: crc-ssr:resolution
- canonical_name: Resolution
- object_kind: object (eight fields)
- defining_paper: Constitutional Runtime Computation (Core)
- operative_version: v5.9
- defining_anchor: Section 4, "A resolution carries a Resolution object"
- authority_class: core_owned
- core_binding: core_bound
- consumers: Constitutional Standing, Constitutional Task Ledger, Constitutional Boundary Contracts, and others, as ORSR lineage
- dependency_surfaces: lineage-consuming across the companions
- extension_or_amendment_refs: none
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: consumed widely as ORSR lineage; no divergent definition
- history: created at v1.0 publication, REGISTERED

### crc-ssr:continuation-state

- schema_id: crc-ssr:continuation-state
- canonical_name: ContinuationState
- object_kind: object
- defining_paper: Constitutional Runtime Computation (Core), originator, marked unsettled pending F-1
- operative_version: unresolved
- defining_anchor: unset as canonical; candidate anchor recorded in notes
- authority_class: core_owned
- core_binding: core_bound
- consumers: Constitutional Standing, Constitutional Task Ledger, Constitutional Feedback, as lineage
- dependency_surfaces: lineage-consuming; Standing specifies contents
- extension_or_amendment_refs: none declared; competing loci listed in notes
- back_reference_status: not_applicable
- registry_status: AMBIGUOUS
- supersedes: none
- superseded_by: none
- notes: candidate loci are the Core originator form at Section 4, "the substrate issues a substrate-owned ContinuationState", constructed in the Appendix A POC, and the fuller required-contents specification in Constitutional Standing v1.5 Part V; the two are not joined by a B.3 amendment; finding F-1; reconciliation dependency is F-1, scheduled in Phase 2 after F-4. This entry is authoritative as to the unresolved condition, not as to a settled location or version
- history: created at v1.0 publication, AMBIGUOUS

### crc-ssr:agent-observation

- schema_id: crc-ssr:agent-observation
- canonical_name: AgentObservation
- object_kind: object
- defining_paper: Constitutional Runtime Computation (Core), originator, marked unsettled pending F-2
- operative_version: unresolved
- defining_anchor: unset as canonical; candidate anchor recorded in notes
- authority_class: core_owned
- core_binding: core_bound
- consumers: Constitutional Boundary Contracts (ObservationContract typing), Constitutional Standing, Constitutional Task Ledger, as lineage
- dependency_surfaces: Boundary Contracts supplies the only field schema; others lineage-consuming
- extension_or_amendment_refs: none declared; competing loci listed in notes
- back_reference_status: not_applicable
- registry_status: AMBIGUOUS
- supersedes: none
- superseded_by: none
- notes: candidate loci are the Core originator by role at Section 4, "constructs the next AgentObservation", built in the Appendix A POC, and the ObservationContract field schema at Constitutional Boundary Contracts V.2, framed as a validation view; the Core publishes no field list beneath the C0 view; finding F-2; reconciliation dependency is F-2, the first lineage reconciliation in Phase 2 after F-4. Authoritative as to the unresolved condition, not as to a settled location or version
- history: created at v1.0 publication, AMBIGUOUS

### crc-ssr:binding-record

- schema_id: crc-ssr:binding-record
- canonical_name: BindingRecord
- object_kind: typed record
- defining_paper: Constitutional Runtime Computation (Core, POC) and Constitutional Standing (canonical), marked unsettled pending F-3
- operative_version: unresolved
- defining_anchor: unset as canonical; candidate anchors recorded in notes
- authority_class: core_owned
- core_binding: core_bound
- consumers: Constitutional Task Ledger, Constitutional Feedback
- dependency_surfaces: schema-consuming by the ledger and feedback companions
- extension_or_amendment_refs: none declared; competing loci listed in notes
- back_reference_status: not_applicable
- registry_status: AMBIGUOUS
- supersedes: none
- superseded_by: none
- notes: candidate loci are the Core POC construction with the field set binding_record_id, proposal_id, from_state, to_state, resolution_id, cycle_id, and the canonical BindingRecord in Constitutional Standing Part IV with a different field set, binding_id, proposal_ref, verdict_type, ContextPinned references, standing_id, state_mutation_ref, generalized across verdict paths; two typed forms, no amendment joining them; finding F-3; reconciliation dependency is F-3, the last lineage reconciliation in Phase 2. Authoritative as to the unresolved condition, not as to a settled location or version
- history: created at v1.0 publication, AMBIGUOUS

### crc-ssr:task-ledger

- schema_id: crc-ssr:task-ledger
- canonical_name: TaskLedger
- object_kind: typed record
- defining_paper: Constitutional Task Ledger (C8)
- operative_version: v1.2
- defining_anchor: C8 III.1, "The central substrate-owned object"
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Standing (lineage), Core Appendix A POC (illustrative sketch)
- dependency_surfaces: lineage-consuming; the Core POC uses an illustrative ledger
- extension_or_amendment_refs: none
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: C8 owns the canonical object; the Core POC uses a substrate-owned ledger with a different, explicitly illustrative field set, a latent drift to watch, not an ownership conflict, since the POC is explicitly illustrative
- history: created at v1.0 publication, REGISTERED

### crc-ssr:pending-obligation

- schema_id: crc-ssr:pending-obligation
- canonical_name: PendingObligation
- object_kind: typed record (twenty fields)
- defining_paper: Constitutional Task Ledger (C8)
- operative_version: v1.2
- defining_anchor: C8 III.2, "retained as a first-class typed object, not a structured field"
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Feedback (population home, PendingObligationLinked), Core Appendix A POC (names it without a field list)
- dependency_surfaces: Feedback schema-consuming; Core POC naming reference
- extension_or_amendment_refs: none
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: C8 owns the canonical twenty-field object; the Core POC names it without a field list, a latent sketch gap; heavily consumed by Feedback
- history: created at v1.0 publication, REGISTERED

### crc-ssr:non-formation-receipt

- schema_id: crc-ssr:non-formation-receipt
- canonical_name: NonFormationReceipt
- object_kind: typed record (twelve fields)
- defining_paper: Constitutional Standing (C6)
- operative_version: v1.5
- defining_anchor: C6 Part II, the twelve-field typed object list
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Task Ledger (source_event_type), Constitutional Feedback (source-record union)
- dependency_surfaces: schema-consuming by the ledger and feedback companions
- extension_or_amendment_refs: none
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: C6 owns the canonical schema; the Core POC names it without a competing field list
- history: created at v1.0 publication, REGISTERED

### crc-ssr:learning-candidate

- schema_id: crc-ssr:learning-candidate
- canonical_name: LearningCandidate
- object_kind: typed record
- defining_paper: Constitutional Memory (C1)
- operative_version: v2.2
- defining_anchor: C1 IV-A.3, the typed LearningCandidate definition
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Feedback through explicit mapping
- dependency_surfaces: Feedback mapping-consuming, not schema-redefining
- extension_or_amendment_refs: F-4 resolved by withdrawal and new-object specialization in Constitutional Feedback v1.1
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: Memory owns the canonical Hold-specific object; Constitutional Feedback consumes it through an interoperability mapping and does not amend it
- history: created at v1.2 publication, REGISTERED; F-4 resolved by withdrawal of the Constitutional Feedback v1.0 extension claim and explicit mapping in Constitutional Feedback v1.1

### crc-ssr:feedback-observation

- schema_id: crc-ssr:feedback-observation
- canonical_name: FeedbackObservation
- object_kind: typed record
- defining_paper: Constitutional Memory (C1)
- operative_version: v2.2
- defining_anchor: C1 IV-A.6, the typed FeedbackObservation definition
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Feedback through explicit mapping
- dependency_surfaces: Feedback mapping-consuming, not schema-redefining
- extension_or_amendment_refs: F-4 resolved by withdrawal and new-object specialization in Constitutional Feedback v1.1
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: Memory owns the canonical Hold-specific observation object; Constitutional Feedback consumes it through an interoperability mapping and does not amend it
- history: created at v1.2 publication, REGISTERED; F-4 resolved by withdrawal of the Constitutional Feedback v1.0 extension claim and explicit mapping in Constitutional Feedback v1.1

### crc-ssr:operational-learning-candidate

- schema_id: crc-ssr:operational-learning-candidate
- canonical_name: OperationalLearningCandidate
- object_kind: typed record
- defining_paper: Constitutional Feedback (C9)
- operative_version: v1.1
- defining_anchor: C9 IV.1, OperationalLearningCandidate
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: FeedbackLedger, FeedbackLearningReachable, and the operational feedback lifecycle
- dependency_surfaces: Memory mapping source for Hold-derived instances; Task Ledger population home through PendingObligation; operational source-record consumers across Standing, Tools, and Task Ledger
- extension_or_amendment_refs: F-4 new-object specialization; not an amendment to Memory
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: generalized operational object owned by Constitutional Feedback; distinct from Memory's Hold-specific LearningCandidate
- history: created at v1.2 publication, REGISTERED; F-4 resolved through withdrawal plus new-object specialization

### crc-ssr:operational-feedback-observation

- schema_id: crc-ssr:operational-feedback-observation
- canonical_name: OperationalFeedbackObservation
- object_kind: typed record
- defining_paper: Constitutional Feedback (C9)
- operative_version: v1.1
- defining_anchor: C9 IV.2, OperationalFeedbackObservation
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: FeedbackLedger, FeedbackLearningReachable, and the operational feedback lifecycle
- dependency_surfaces: Memory mapping source for Hold-derived observations; Task Ledger task and PendingObligation linkage; lineage consumption through ContinuationState
- extension_or_amendment_refs: F-4 new-object specialization; not an amendment to Memory
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: generalized operational observation object owned by Constitutional Feedback; distinct from Memory's Hold-specific FeedbackObservation
- history: created at v1.2 publication, REGISTERED; F-4 resolved through withdrawal plus new-object specialization

### crc-ssr:generation-member

- schema_id: crc-ssr:generation-member
- canonical_name: GenerationMember
- object_kind: typed record
- defining_paper: Constitutional Coherence (C4)
- operative_version: v1.4, with a Constitutional Thresholds v1.4 compatible extension
- defining_anchor: C4 Part II, member concept "remains this paper's"
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Thresholds (types it with an optional threshold_set_version)
- dependency_surfaces: Thresholds schema-consuming, via a declared compatible extension
- extension_or_amendment_refs: R6, compatible extension declared in Constitutional Thresholds v1.3, back-reference carried in Constitutional Coherence v1.3; the typed form is sited in the owner
- back_reference_status: present
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: R6 compatible-extension history; the earlier deferred-typing commitment is satisfied by authoritative registration, the schema text stays with the defining and amending papers and is not relocated by registration
- history: created at v1.0 publication, REGISTERED; prior RESOLVED closure R6, compatible extension declared in Constitutional Thresholds v1.3 with the Constitutional Coherence v1.3 back-reference

### crc-ssr:goal-status-enum

- schema_id: crc-ssr:goal-status-enum
- canonical_name: GoalStatusEnum
- object_kind: enumeration (seven values)
- defining_paper: Constitutional Boundary Contracts (C0)
- operative_version: v1.2
- defining_anchor: C0 V.3, "Boundary Contracts owns the GoalStatusEnum value set"
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Task Ledger (reuses the value set, supplies operational semantics), Core B.6 (coarse projection onto goal_status)
- dependency_surfaces: Task Ledger schema-consuming; Core B.6 projection declaration
- extension_or_amendment_refs: R4, RECONSTITUTED admitted as a seventh value, a compatible extension in Constitutional Boundary Contracts v1.2, coupled with the Core v5.7 B.6 projection; Constitutional Task Ledger v1.2 reuses the value
- back_reference_status: present
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: R4 closure recorded in history; GoalStatusConsistent is a ledger-match check, not an enum-membership gate
- history: created at v1.0 publication, REGISTERED; prior RESOLVED closure R4, RECONSTITUTED admitted in Constitutional Boundary Contracts v1.2 with the B.6 projection in Core v5.7

### crc-ssr:authority-context-ref

- schema_id: crc-ssr:authority-context-ref
- canonical_name: authority_context_ref
- object_kind: field
- defining_paper: Constitutional Runtime Computation (Core)
- operative_version: v5.9
- defining_anchor: Section 6a, "a pinned reference to the authority context A, the requester's standing and the authority graph, at evaluation time"
- authority_class: core_owned
- core_binding: core_bound
- consumers: Constitutional Standing (StandingContext supplies the requester-standing component), Constitutional Task Ledger, Constitutional Tools
- dependency_surfaces: Standing supplies a component; others field-consuming
- extension_or_amendment_refs: R5, resolved by withdrawal; Constitutional Standing v1.4 withdrew its in-text rebinding of this Core field, Core unchanged, no amendment declaration required
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: R5 by-withdrawal closure recorded in history; C6 StandingContext supplies the requester-standing component of the Core field, it does not rebind or exhaust it
- history: created at v1.0 publication, REGISTERED; prior RESOLVED-by-withdrawal closure R5, Constitutional Standing v1.4 under B.4

### crc-ssr:proposal-conformant

- schema_id: crc-ssr:proposal-conformant
- canonical_name: ProposalConformant
- object_kind: predicate (thirteen conjuncts)
- defining_paper: Constitutional Boundary Contracts (C0)
- operative_version: v1.2
- defining_anchor: C0 IV.3, the proposal-crossing validator
- authority_class: companion_owned
- core_binding: not_core_bound
- consumers: Constitutional Standing (imports it directly)
- dependency_surfaces: Standing validator-consuming
- extension_or_amendment_refs: R7, the Standing alias BoundaryConformant reconciled to the operative name ProposalConformant in Constitutional Standing v1.5
- back_reference_status: not_applicable
- registry_status: REGISTERED
- supersedes: none
- superseded_by: none
- notes: R7 closure recorded in history; Standing imports the boundary companion's validator directly and now uses the operative name
- history: created at v1.0 publication, REGISTERED; prior RESOLVED closure R7, alias reconciled in Constitutional Standing v1.5

## Expansion

The validated seed registry held the twelve highest-drift objects. CRC-SSR v1.2
adds four post-activation governed entries for F-4, bringing the current registry
to sixteen entries total. The remaining shared objects from the Cluster 1
inventory are registered post-activation, by drift rank, each as its own governed
addition.

## F-4 reconciliation history

F-4 concerned Constitutional Feedback v1.0's undeclared claim to extend the
Memory-owned `LearningCandidate` and `FeedbackObservation` objects. That claim
remained non-operative under Constitutional Runtime Computation Appendix B B.2:
no B.3 amendment declaration and no B.3.1 Memory back-reference joined the
definitions. Constitutional Feedback v1.1 withdraws the extension claim.
Memory's `LearningCandidate` and `FeedbackObservation` remain REGISTERED at
Constitutional Memory v2.2. Constitutional Feedback's new generalized operational
objects, `OperationalLearningCandidate` and `OperationalFeedbackObservation`, are
separately REGISTERED at Constitutional Feedback v1.1. No Memory amendment
occurred. No B.3.1 back-reference was owed. No Core amendment occurred. F-1,
F-2, and F-3 remain unresolved.

## Inaugural registry migration history

Upon activation under Constitutional Runtime Computation v5.10 Appendix B B.10,
the seven resolved divergences recorded in Core Appendix B B.7 are incorporated
into CRC-SSR as archival migration history. This record alters no registered
object's definition, pointer, operative version, status, or entry history. B.7
remains the original docket of record.

| Record | Shared item | Migration status | Source docket | Resolving or amendment reference |
|---|---|---|---|---|
| R1 | `GenerationPinAdmissible` | RESOLVED | Core Appendix B B.7 | R1a declared in Constitutional Thresholds v1.4 with a Constitutional Coherence v1.4 back-reference; R1b phantom rename removed under Route C, F27 closed |
| R2 | `GenerationCoherenceReachable` | RESOLVED | Core Appendix B B.7 | Declared in Constitutional Thresholds v1.3, back-reference in Constitutional Coherence v1.3 |
| R3 | `goal_status` coarse-to-operational mapping | RESOLVED | Core Appendix B B.7 | Projection declared in Core Appendix B B.6, Core v5.7, `ESCALATED` to `IN_PROGRESS` and `RECONSTITUTED` to `IN_PROGRESS` |
| R4 | `GoalStatusEnum` value set | RESOLVED | Core Appendix B B.7 | `RECONSTITUTED` admitted in Constitutional Boundary Contracts v1.2 with the B.6 projection in Core v5.7; Constitutional Task Ledger v1.2 reuse |
| R5 | `authority_context_ref` binding | RESOLVED | Core Appendix B B.7 | Resolved by withdrawal, Constitutional Standing v1.4; Core unchanged, no amendment declaration required |
| R6 | `GenerationMember` | RESOLVED | Core Appendix B B.7 | Declared in Constitutional Thresholds v1.3, back-reference in Constitutional Coherence v1.3, typed form sited in the owner |
| R7 | `ProposalConformant` name | RESOLVED | Core Appendix B B.7 | Alias reconciled to `ProposalConformant` in Constitutional Standing v1.5 |
