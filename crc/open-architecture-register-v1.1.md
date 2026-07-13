# CRC Open Architecture Register

**Artifact name:** CRC Open Architecture Register
**Short identifier:** CRC-OAR
**Version:** v1.1
**Artifact class:** governance-operational and historical
**Corpus:** Constitutional Runtime Computation
**Ratifying authority:** Faheem Downs
**Current status:** current after publication
**Publication state:** draft until commit and push
**Governance context:** first post-publication F-5 Phase 1 transition package
**Predecessor:** CRC-OAR v1.0

CRC-OAR is not a normative doctrine paper and is not the shared-schema registry.
CRC-OAR v1.0 remains historical and unchanged. CRC-OAR v1.1 does not modify
Core, companions, CRC-SSR, or corpus-entry doctrine. CRC-OAR v1.1 does not
restart F-3 and does not mark any entry `RESOLVED`.

## Purpose and Authority

CRC-OAR tracks unresolved status, dependency lineage, discovery locus, blocking
relationships, and closure state for unresolved architectural findings, blocked
apparatus, missing predicates, cross-cutting architecture issues, deferred
amendments, and evidence gaps. CRC-OAR is authoritative for those
governance-operational facts.

CRC-OAR is not authoritative for canonical doctrine, object schemas, predicates,
enumerations, or implementation permission. Recognition in CRC-OAR does not make
a concept canonical, valid, reachable, executable, admissible, binding, or
available for implementation. Canonical doctrine remains in Core or companion
papers. Canonical shared-object pointers remain in CRC-SSR. Published historical
CRC-OAR versions remain unchanged.

Governing principle: An OAR entry recognizes an unresolved corpus dependency. It
does not make the referenced concept canonical, valid, reachable, or available
for normative use or implementation.

## Entry Classes

- `finding`: a named reconciliation or architecture finding.
- `apparatus`: a missing or unsettled object, record, mechanism, or object family.
- `predicate`: a missing or unsettled predicate or validation rule.
- `architecture_issue`: a cross-cutting sequence, boundary, branch, or write-order issue.
- `deferred_amendment`: a known governance change not yet carried.
- `evidence_gap`: a missing validation, proof, receipt, or instrumentation surface.

There is no separate blocked-object class. A blocked object is an `apparatus` or
`finding` whose status is `BLOCKED`.

## Status Vocabulary

### OPEN

Recognized but not yet under active specification.

- predecessor: none
- successors: `SPECIFYING`, `BLOCKED`, `WITHDRAWN`, `SUPERSEDED`

### SPECIFYING

Active architectural analysis, reconciliation, or specification work is underway.

- predecessors: `OPEN`, `BLOCKED`
- successors: `SPECIFIED`, `BLOCKED`, `WITHDRAWN`, `SUPERSEDED`

### SPECIFIED

A ratified specification exists, but required corpus integration or publication
is incomplete.

- predecessor: `SPECIFYING`
- successors: `RESOLVED`, `BLOCKED`, `SUPERSEDED`

### BLOCKED

The entry cannot close until another entry or corpus condition is resolved.

- predecessors: `OPEN`, `SPECIFYING`, `SPECIFIED`
- successors: `SPECIFYING`, `WITHDRAWN`, `SUPERSEDED`

### RESOLVED

Canonical destination and all applicable closure conditions are complete and
publicly published.

- ordinary predecessor: `SPECIFIED`
- terminal except for historical correction through a later CRC-OAR version
- do not reopen the same entry

### WITHDRAWN

The concern is no longer pursued and is not replaced as the same concern.

- predecessor: any non-`RESOLVED` status
- terminal
- withdrawal rationale required

### SUPERSEDED

Another OAR entry replaces the concern.

- predecessor: any non-`RESOLVED` status
- terminal
- `superseded_by` required
- no successor
- superseded identifiers are never reused or reopened

## Historical Bootstrap Rule

Findings resolved before CRC-OAR existed may be seeded directly as `RESOLVED`.
Such entries must identify their published canonical destinations. Their history
must state that the status was imported from completed corpus reconciliation.
This exception applies only to historical initialization of CRC-OAR v1.0. It does
not create a general direct transition from `OPEN` to `RESOLVED`.

## Ratification Rules

Creation of entries requires a ratified corpus edit. All status transitions
require ratification. `SPECIFIED`, `RESOLVED`, `WITHDRAWN`, and `SUPERSEDED`
require an explicit ratification record in entry history. CRC-SSR treatment is
required only where the entry concerns an eligible shared load-bearing object.

## Stable Identifiers

- `OAR-F###`: findings
- `OAR-A###`: apparatus
- `OAR-P###`: predicates
- `OAR-X###`: architecture issues
- `OAR-E###`: evidence gaps

For `deferred_amendment`, use the `OAR-X###` sequence unless a later register
version establishes a distinct identifier family.

Identifiers are global and append-only. Numbers are never reused. Titles may
change, but identifiers do not. Renamed concepts use `aliases`. Superseded
concepts use `superseded_by`. F-1 through F-5 are retained as aliases for
`OAR-F001` through `OAR-F005`.

## Entry Schema

Required for every entry:

- `register_id`
- `title`
- `entry_class`
- `status`
- `discovered_in`
- `discovery_version`
- `gap_statement`
- `current_loci`
- `dependency_relationships`
- `current_authority`
- `required_resolution`
- `closure_conditions`
- `registry_implications`
- `history`

Conditional fields:

- `aliases`
- `blocked_by`
- `blocks`
- `candidate_owner`
- `settled_owner`
- `unresolved_questions`
- `canonical_destination`
- `superseded_by`
- `withdrawal_rationale`

Optional fields:

- `notes`

Rules: `candidate_owner` is used only while ownership is unresolved.
`settled_owner` is required for a `RESOLVED` apparatus or ownership-bearing
finding where ownership has been settled. `canonical_destination` is required
for `RESOLVED` entries. `blocked_by` is required for `BLOCKED` entries.
`superseded_by` is required for `SUPERSEDED` entries. `withdrawal_rationale` is
required for `WITHDRAWN` entries. `history` is append-only within the version
lineage. `notes` are explicitly non-authoritative.

## Admission Rule

An OAR entry is mandatory when:

- a paper depends on an object without a canonical owner or locus
- a named field references an undefined object
- multiple papers define competing versions
- an architecture review discovers missing apparatus blocking a registered or registrable object
- a required predicate lacks an owner
- lawful implementation cannot proceed without missing corpus architecture

An OAR entry is not required for merely desirable future extensions, speculative
ideas, concepts not yet relied upon by a corpus surface, or every undefined
ordinary-language term. Those belong in research notes until they become corpus
dependencies.

## Closure Rule

An entry may become `RESOLVED` only after all applicable conditions are satisfied:

- doctrine or schema has been ratified
- ownership has been settled
- a versioned canonical anchor exists
- required companion alignment is complete
- CRC-SSR has been updated where applicable
- README navigation has been updated where applicable
- validation has passed
- publication has occurred

Closure occurs after public publication, not draft approval or local commit
alone. Dependent entries do not all need to close unless the entry's own closure
conditions require them. `RESOLVED` entries remain visible as historical lineage.

## Change Governance and Versioning

CRC-OAR uses corpus artifact versioning. The first version is v1.0. Every
published entry addition, status transition, closure, withdrawal, supersession,
or governance-rule change creates a new versioned register file. Previous
versions remain historical and unchanged. Bodies may be corrected only in a new
version. Corrections must be recorded in history. Identifiers remain stable
across versions. Status-only changes still require a new version.

## CRC-SSR Boundary

CRC-OAR tracks unresolved architecture and dependencies. CRC-SSR tracks canonical
locations and operative versions for shared load-bearing objects. An OAR
apparatus entry becomes CRC-SSR-eligible only after object identity, owner,
defining paper, operative version, and anchor are ratified.

A CRC-SSR `AMBIGUOUS` entry should normally have an OAR entry when the ambiguity
is active or blocking. Not every OAR entry belongs in CRC-SSR. Architecture
issues, write-order gaps, evidence gaps, and findings may never become registry
objects. `RESOLVED` OAR entries remain and point to their canonical destinations.
CRC-OAR itself is not entered into CRC-SSR.

## Wikilink Policy

CRC-OAR permits Obsidian-style unresolved references such as
`\[\[BindingRecord\]\]`, `\[\[ActuationCommand\]\]`,
`\[\[ActuationResult\]\]`, and `\[\[StateMutationRecord\]\]`.

Rules:

- unresolved wikilinks may appear only in a clearly marked `wikilinks` or alias context within an OAR entry
- a broken wikilink is allowed only for a concept explicitly marked unresolved
- canonical corpus references must use normal Markdown links
- where a canonical target exists, provide a Markdown link even if an alias wikilink is also shown
- an unresolved wikilink does not require creating an empty placeholder file
- unresolved wikilinks must not appear as if they were canonical citations
- GitHub portability must be preserved through ordinary prose and typed corpus references

Individual placeholder files are not created by this register version.

## Normative-Use Boundary

Normative papers may reference OAR identifiers only as unresolved, provisional,
blocked, illustrative, or outside scope. Candidate schemas in CRC-OAR are not
canonical. A CRC-OAR entry cannot authorize implementation. CRC-OAR cannot
replace a Core or companion schema anchor. CRC-OAR cannot replace CRC-SSR
registration.

## Initial Seed Entries

### OAR-F001

- register_id: OAR-F001
- title: ContinuationState lineage reconciliation
- aliases: F-1
- entry_class: finding
- status: RESOLVED
- discovered_in: CRC-SSR lineage reconciliation sequence
- discovery_version: CRC-SSR v1.3 and Core v5.11 active corpus
- gap_statement: ContinuationState originated in Core, was constructed in Core Appendix A, and was specified more fully in Constitutional Standing, leaving canonical ownership and schema locus unsettled before reconciliation.
- current_loci: [Core v5.12](constitutional-runtime-computation-v5.12.md), [Standing v1.6](companions/constitutional-standing-v1.6.md), [CRC-SSR v1.4](shared-schema-registry-v1.4.md)
- dependency_relationships: none
- current_authority: historical-bootstrap `RESOLVED`; status imported from completed corpus reconciliation.
- required_resolution: completed by Core owner-side schema formalization, Standing clarification, and CRC-SSR registry reconciliation.
- closure_conditions: canonical schema published, ownership settled, Standing role clarified, CRC-SSR updated, README updated, validation passed, public publication completed.
- registry_implications: `crc-ssr:continuation-state` is REGISTERED in CRC-SSR v1.4.
- settled_owner: Core owns ContinuationState; Standing and Task Ledger retain their ratified referenced semantics.
- canonical_destination: [Core v5.12 Canonical ContinuationState](constitutional-runtime-computation-v5.12.md), [Standing v1.6](companions/constitutional-standing-v1.6.md), [CRC-SSR v1.4 crc-ssr:continuation-state](shared-schema-registry-v1.4.md)
- history: historical bootstrap entry imported from completed corpus reconciliation; public completion commit `d3b8f96905a0d2a6c353bbe73e4da5a693eae6e8`.

### OAR-F002

- register_id: OAR-F002
- title: AgentObservation lineage reconciliation
- aliases: F-2
- entry_class: finding
- status: RESOLVED
- discovered_in: CRC-SSR lineage reconciliation sequence
- discovery_version: CRC-SSR v1.2 and Core v5.10 active corpus
- gap_statement: AgentObservation originated in Core while Boundary Contracts supplied the only complete field schema under ObservationContract, leaving ownership and schema locus unsettled before reconciliation.
- current_loci: [Core v5.12](constitutional-runtime-computation-v5.12.md), [Boundary Contracts v1.3](companions/constitutional-boundary-contracts-v1.3.md), [CRC-SSR v1.4](shared-schema-registry-v1.4.md)
- dependency_relationships: none
- current_authority: historical-bootstrap `RESOLVED`; status imported from completed corpus reconciliation.
- required_resolution: completed by Core owner-side schema formalization, Boundary Contracts validation-view clarification, and CRC-SSR registry reconciliation.
- closure_conditions: canonical schema published, ownership settled, Boundary Contracts role clarified, CRC-SSR updated, README updated, validation passed, public publication completed.
- registry_implications: `crc-ssr:agent-observation` is REGISTERED in CRC-SSR v1.3 and inherited by CRC-SSR v1.4.
- settled_owner: Core owns AgentObservation; Boundary Contracts owns ObservationContract and ObservationConformant.
- canonical_destination: [Core v5.11 inherited by Core v5.12](constitutional-runtime-computation-v5.12.md), [Boundary Contracts v1.3](companions/constitutional-boundary-contracts-v1.3.md), [CRC-SSR v1.4 crc-ssr:agent-observation](shared-schema-registry-v1.4.md)
- history: historical bootstrap entry imported from completed corpus reconciliation; public completion commit `b01a4ad756532b07f5dd8f9d74733f3da8b6258b`.

### OAR-F003

- register_id: OAR-F003
- title: BindingRecord lineage reconciliation
- aliases: F-3
- entry_class: finding
- status: BLOCKED
- discovered_in: CRC-SSR lineage reconciliation sequence
- discovery_version: CRC-SSR v1.4 and Core v5.12 active corpus
- gap_statement: BindingRecord cannot be canonically settled until mutation, admission, and binding lineage are defined.
- current_loci: [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Standing v1.6](companions/constitutional-standing-v1.6.md), [Constitutional Task Ledger v1.3](companions/constitutional-task-ledger-v1.3.md), [CRC-SSR v1.5](shared-schema-registry-v1.5.md)
- dependency_relationships: OAR-F005
- blocked_by: OAR-F005
- blocks: none
- candidate_owner: Core
- current_authority: non-canonical; `crc-ssr:binding-record` remains AMBIGUOUS, while the F-5 dependency contract is now public.
- required_resolution: restart F-3 under separate ratification, then settle final BindingRecord schema, ownership, predicate, Standing alignment, and registry treatment.
- closure_conditions: F-5 prerequisite architecture published, F-3 restart ratified, BindingRecord ownership settled, canonical anchor published, CRC-SSR updated where applicable, README updated where applicable, validation passed, publication completed.
- registry_implications: `crc-ssr:binding-record` remains AMBIGUOUS.
- unresolved_questions: final BindingRecord schema, final owner reconciliation, BindingRecordValid, Standing alignment, and registry settlement.
- notes: non-authoritative wikilinks: [[BindingRecord]]
- history: created in CRC-OAR v1.0 as BLOCKED by OAR-F005; v1.1 records F-5 Phase 1 publication and a public dependency contract while preserving BLOCKED pending separate F-3 restart ratification.

### OAR-F004

- register_id: OAR-F004
- title: Feedback object reconciliation
- aliases: F-4
- entry_class: finding
- status: RESOLVED
- discovered_in: CRC-SSR F-4 reconciliation
- discovery_version: CRC-SSR v1.2 and active corpus at commit `a7e4d30a38696adfcf79938028219fa20f12c186`
- gap_statement: Feedback v1.0 claimed extension of Memory objects without the required operative joining, requiring withdrawal and new-object specialization.
- current_loci: [Memory v2.2](companions/constitutional-memory-v2.2.md), [Feedback v1.1](companions/constitutional-feedback-v1.1.md), [CRC-SSR v1.4](shared-schema-registry-v1.4.md)
- dependency_relationships: none
- current_authority: historical-bootstrap `RESOLVED`; status imported from completed corpus reconciliation.
- required_resolution: completed by withdrawal of the extension claim and registration of Feedback-owned specialized objects.
- closure_conditions: ownership split settled, canonical destinations published, CRC-SSR updated, README updated, validation passed, public publication completed.
- registry_implications: Memory-owned and Feedback-owned objects are REGISTERED in CRC-SSR v1.2 and inherited by CRC-SSR v1.4.
- settled_owner: Memory owns LearningCandidate and FeedbackObservation; Feedback owns OperationalLearningCandidate and OperationalFeedbackObservation.
- canonical_destination: [Memory v2.2](companions/constitutional-memory-v2.2.md), [Feedback v1.1](companions/constitutional-feedback-v1.1.md), [CRC-SSR v1.4 inherited F-4 registrations](shared-schema-registry-v1.4.md)
- history: historical bootstrap entry imported from completed corpus reconciliation; public completion commit `a7e4d30a38696adfcf79938028219fa20f12c186`.

### OAR-F005

- register_id: OAR-F005
- title: Substrate Actuation and Effect Admission
- aliases: F-5
- entry_class: finding
- status: SPECIFIED
- discovered_in: F-2, F-1, F-3, and F-5 architecture analyses
- discovery_version: Core v5.12, Standing v1.6, Task Ledger v1.2, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus lacks a generalized constitutional architecture between Resolution and BindingRecord for actuation, actuation result, result admission, governed state mutation, binding, write order, failure topology, and retry or replay.
- current_loci: [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [Constitutional Task Ledger v1.3](companions/constitutional-task-ledger-v1.3.md), [CRC-SSR v1.5](shared-schema-registry-v1.5.md), [CRC README](README.md) for navigation and publication-state evidence only
- dependency_relationships: OAR-A001, OAR-A002, OAR-P001, OAR-A003, OAR-X001, OAR-X002, OAR-X003, OAR-X004, OAR-X005
- blocks: OAR-F003
- candidate_owner: coordinated Core plus new actuation companion, with Tools specialization
- current_authority: F-5 specification is ratified, the generic apparatus is publicly published, and the architecture is active. OAR closure remains pending, and F-5 is not yet formally `RESOLVED` in OAR lifecycle terms.
- required_resolution: specification and publication are complete; formal OAR closure requires a later lawful transition from `SPECIFIED` to `RESOLVED`.
- closure_conditions: public evidence exists for ActuationCommand, ActuationResult, ActuationAdmissionRecord, GovernedStateMutationRecord, command predicates, result validity, result admission, state-mutation reachability and validity, actuation-to-binding write order, internal and external branches, failure and partial effects, replay, retry, idempotency, compensation, rollback, audit durability, Tools specialization, Task Ledger obligation alignment, and the BindingRecord dependency contract. Formal OAR closure remains pending later lifecycle transition.
- registry_implications: CRC-SSR v1.5 registers four F-5 shared objects; `crc-ssr:binding-record` remains AMBIGUOUS, and F-3 remains responsible for final BindingRecord settlement.
- unresolved_questions: formal OAR closure timing and downstream F-3 restart remain open; final BindingRecord reconciliation remains separate.
- history: created in CRC-OAR v1.0 as SPECIFYING after completion of the read-only F-5 architecture analysis; v1.1 records public F-5 Phase 1 publication and moves OAR-F005 from `SPECIFYING` to `SPECIFIED`.

### OAR-A001

- register_id: OAR-A001
- title: ActuationCommand
- entry_class: apparatus
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus needs a governed command or equivalent object between adjudicative authorization and substrate-owned actuation attempt.
- current_loci: [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [CRC-SSR v1.5](shared-schema-registry-v1.5.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core
- canonical_destination: [Core v5.13 ActuationCommand](constitutional-runtime-computation-v5.13.md)
- current_authority: ActuationCommand is publicly defined in Core v5.13 and registered in CRC-SSR v1.5. The first lawful OAR transition is `SPECIFYING` despite public definition because CRC-OAR lifecycle requires staged progression.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving Core ownership, schema anchor, one-use authority, scope containment, audit lineage, and relationship to Resolution.
- closure_conditions: owner settled, schema or equivalent doctrine ratified, anchor published, CRC-SSR updated if registered, validation passed, publication completed.
- registry_implications: registered as `crc-ssr:actuation-command` in CRC-SSR v1.5.
- notes: non-authoritative wikilinks: [[ActuationCommand]]
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public definition evidence and moves OAR-A001 from `OPEN` to `SPECIFYING`.

### OAR-A002

- register_id: OAR-A002
- title: ActuationResult
- entry_class: apparatus
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus needs a generalized result object or equivalent record for attempted, completed, failed, partial, timed out, unknown, externally irreversible, compensated, duplicate, or replay-detected actuation outcomes.
- current_loci: [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [CRC-SSR v1.5](shared-schema-registry-v1.5.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core
- canonical_destination: [Core v5.13 ActuationResult](constitutional-runtime-computation-v5.13.md)
- current_authority: ActuationResult is publicly defined in Core v5.13 and registered in CRC-SSR v1.5. Tools v1.2 specializes the generic object. The first lawful OAR transition is `SPECIFYING` pending later lifecycle advancement.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving the generic actuation-result surface and Tools specialization boundary.
- closure_conditions: owner settled, generic result semantics ratified, Tools specialization aligned, CRC-SSR updated if registered, validation passed, publication completed.
- registry_implications: registered as `crc-ssr:actuation-result` in CRC-SSR v1.5.
- notes: non-authoritative wikilinks: [[ActuationResult]]
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public definition evidence and moves OAR-A002 from `OPEN` to `SPECIFYING`.

### OAR-P001

- register_id: OAR-P001
- title: Generalized actuation-result admission
- entry_class: predicate
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus has Tools-specific `ToolResultAdmissible`, but lacks a generalized predicate for whether an actuation result may enter governed state.
- current_loci: [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core
- canonical_destination: [Core v5.13 ActuationResultAdmissible](constitutional-runtime-computation-v5.13.md), [Core v5.13 ActuationAdmissionRecord](constitutional-runtime-computation-v5.13.md)
- current_authority: ActuationResultAdmissible is publicly defined in Core v5.13, and ActuationAdmissionRecord provides the associated durable representation. The predicate and record are related but not identical objects. Tools v1.2 specializes the predicate through ToolResultAdmissible.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving the generalized admission predicate, durable admission-record relationship, and specialization boundaries.
- closure_conditions: owner settled, predicate ratified, specialization boundaries aligned, CRC-SSR updated if registered, validation passed, publication completed.
- registry_implications: predicate registry treatment remains separate; ActuationAdmissionRecord is registered as `crc-ssr:actuation-admission-record` in CRC-SSR v1.5.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public definition evidence and moves OAR-P001 from `OPEN` to `SPECIFYING`.

### OAR-A003

- register_id: OAR-A003
- title: StateMutationRecord
- entry_class: apparatus
- status: SPECIFYING
- discovered_in: F-3 and F-5 architecture analyses
- discovery_version: Standing v1.6, Core v5.12, and CRC-SSR v1.4 active corpus
- gap_statement: Standing's existing `state_mutation_ref` does not establish a canonical state-mutation object, leaving mutation lineage unresolved.
- current_loci: [Standing v1.6](companions/constitutional-standing-v1.6.md), [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [CRC-SSR v1.5](shared-schema-registry-v1.5.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core or the future actuation companion, subject to ratification
- canonical_destination: [Core v5.13 GovernedStateMutationRecord](constitutional-runtime-computation-v5.13.md)
- current_authority: StateMutationRecord remains the historical seed name. GovernedStateMutationRecord is the published canonical object in Core v5.13. The historical seed name must not become a competing canonical object.
- required_resolution: advance through later OAR lifecycle stages after ratification under the canonical GovernedStateMutationRecord destination, preserving F-3 dependency clarity.
- closure_conditions: owner settled, canonical mutation apparatus ratified, F-3 dependency clarified, CRC-SSR updated if registered, validation passed, publication completed.
- registry_implications: registered as `crc-ssr:governed-state-mutation-record` in CRC-SSR v1.5.
- notes: non-authoritative wikilinks: [[StateMutationRecord]]
- history: created in CRC-OAR v1.0 as OPEN under the historical seed name StateMutationRecord; v1.1 records GovernedStateMutationRecord as the published canonical name and moves OAR-A003 from `OPEN` to `SPECIFYING`.

### OAR-X001

- register_id: OAR-X001
- title: Actuation-to-binding write order
- entry_class: architecture_issue
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Standing v1.6, Task Ledger v1.2, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus lacks a non-circular ordering among Resolution, actuation command, result, admission, mutation, BindingRecord, CycleRecord, Task Ledger, ContinuationState, and AgentObservation.
- current_loci: [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Task Ledger v1.3](companions/constitutional-task-ledger-v1.3.md)
- dependency_relationships: OAR-F005
- current_authority: actuation-to-binding write order is publicly specified in Core v5.13 and elaborated in C10. The first lawful OAR transition is `SPECIFYING` pending later lifecycle advancement.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving the non-circular ordering among Resolution, actuation command, result, admission, mutation, BindingRecord, CycleRecord, Task Ledger, ContinuationState, and AgentObservation.
- closure_conditions: write-order doctrine ratified, object references settled, F-3 unblocking effect recorded, validation passed, publication completed.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public write-order evidence and moves OAR-X001 from `OPEN` to `SPECIFYING`.

### OAR-X002

- register_id: OAR-X002
- title: Failure and partial-effect topology
- entry_class: architecture_issue
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Tools v1.1, Core v5.12, and Task Ledger v1.2 active corpus
- gap_statement: The corpus lacks generalized handling for actuator unavailable, failed attempts, unknown results, partial completion, compensation, rollback, and irreversible external effects.
- current_loci: [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Task Ledger v1.3](companions/constitutional-task-ledger-v1.3.md)
- dependency_relationships: OAR-F005
- current_authority: failure and partial-effect topology is publicly specified in C10 with Core v5.13 generic constraints and Task Ledger v1.3 obligation accounting. The first lawful OAR transition is `SPECIFYING` pending later lifecycle advancement.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving failure, partial completion, unknown result, compensation, rollback, and irreversible-effect treatment.
- closure_conditions: failure topology ratified, obligation and escalation consequences aligned, validation passed, publication completed.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public failure-topology evidence and moves OAR-X002 from `OPEN` to `SPECIFYING`.

### OAR-X003

- register_id: OAR-X003
- title: Replay, retry, and idempotency
- entry_class: architecture_issue
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and Task Ledger v1.2 active corpus
- gap_statement: The corpus lacks generalized rules for one-use commands, duplicate detection, retry authority, and unknown-result retry restrictions.
- current_loci: [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.13](constitutional-runtime-computation-v5.13.md)
- dependency_relationships: OAR-F005, OAR-X002
- current_authority: replay, retry, and idempotency rules are publicly specified in C10 and Core v5.13. The first lawful OAR transition is `SPECIFYING` pending later lifecycle advancement.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving one-use commands, duplicate detection, fresh retry authority, and unknown-result retry restrictions.
- closure_conditions: replay and retry doctrine ratified, relationship to failure topology settled, validation passed, publication completed.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public replay and idempotency evidence and moves OAR-X003 from `OPEN` to `SPECIFYING`.

### OAR-X004

- register_id: OAR-X004
- title: Internal versus external effect branches
- entry_class: architecture_issue
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, Memory v2.2, Task Ledger v1.2, and domain application corpus
- gap_statement: The corpus lacks a shared branch model for internal mutation, memory, ledger, tools, communications, financial effects, and external-world actions.
- current_loci: [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.13](constitutional-runtime-computation-v5.13.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [Memory v2.2](companions/constitutional-memory-v2.2.md), [Constitutional Task Ledger v1.3](companions/constitutional-task-ledger-v1.3.md)
- dependency_relationships: OAR-F005
- current_authority: internal and external branch taxonomy is publicly specified in C10 with Core v5.13 generic actuator and mutation invariants. The first lawful OAR transition is `SPECIFYING` pending later lifecycle advancement.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving shared constitutional interfaces and typed branches for internal mutation, memory, ledger, tools, communications, financial effects, and external-world actions.
- closure_conditions: branch architecture ratified, specialization owners settled, validation passed, publication completed.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public branch-architecture evidence and moves OAR-X004 from `OPEN` to `SPECIFYING`.

### OAR-X005

- register_id: OAR-X005
- title: Tools specialization relationship
- entry_class: architecture_issue
- status: SPECIFYING
- discovered_in: F-5 architecture analysis
- discovery_version: Tools v1.1, Core v5.12, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus must determine how ToolInvocationProposal, ToolResultRecord, and ToolResultAdmissible conform to or specialize generalized Core actuation apparatus.
- current_loci: [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.13](constitutional-runtime-computation-v5.13.md), [CRC-SSR v1.5](shared-schema-registry-v1.5.md)
- dependency_relationships: OAR-F005, OAR-A001, OAR-A002, OAR-P001
- current_authority: Tools v1.2 specializes the generalized F-5 apparatus. Tools does not own generic actuation authority, and no Tools authority expansion occurred. The first lawful OAR transition is `SPECIFYING` pending later lifecycle advancement.
- required_resolution: advance through later OAR lifecycle stages after ratification, preserving ToolInvocationProposal, ToolResultRecord, and ToolResultAdmissible conformance to the generalized Core actuation apparatus.
- closure_conditions: Tools specialization doctrine ratified, generic apparatus relationship settled, Tools version alignment completed if required, validation passed, publication completed.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public Tools-specialization evidence and moves OAR-X005 from `OPEN` to `SPECIFYING`.

## Version History

*v1.1. First post-publication F-5 Phase 1 transition package. Records public
publication of Core v5.13, Companion 10 Constitutional Actuation and Effect
Admission v1.0, Constitutional Tools v1.2, Constitutional Task Ledger v1.3, and
CRC-SSR v1.5. Moves OAR-F005 from `SPECIFYING` to `SPECIFIED`. Moves OAR-A001,
OAR-A002, OAR-P001, OAR-A003, and OAR-X001 through OAR-X005 from `OPEN` to
`SPECIFYING`. Preserves OAR-F003 as `BLOCKED`. No F-3 restart occurs. No
BindingRecord settlement occurs. No CRC-SSR change occurs in this register
version. No entry becomes `RESOLVED`.*

*v1.0. Creates CRC-OAR as the governance-operational and historical register for
open architecture dependencies. Ratifies the register boundary: authoritative for
unresolved status, dependency lineage, discovery locus, blocking relationships,
and closure state, but not authoritative for canonical doctrine, schema,
predicate, enumeration, registry pointer, or implementation permission.
Historically imports resolved F-1, F-2, and F-4. Records F-3 as `BLOCKED`.
Records F-5 as `SPECIFYING`. Creates the initial open apparatus and architecture
entries for actuation command, actuation result, generalized result admission,
state mutation, write order, failure topology, replay and idempotency,
internal-external effect branching, and Tools specialization. No CRC-SSR
activation or registration event occurs. No unresolved entry gains normative
authority.*
