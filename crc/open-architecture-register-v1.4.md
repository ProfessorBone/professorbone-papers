# CRC Open Architecture Register

**Artifact name:** CRC Open Architecture Register
**Short identifier:** CRC-OAR
**Version:** v1.4
**Artifact class:** governance-operational and historical
**Corpus:** Constitutional Runtime Computation
**Ratifying authority:** Faheem Downs
**Current status:** current after publication
**Publication state:** draft until commit and push
**Governance context:** formal closure of F-3 BindingRecord reconciliation and the F-5 apparatus architecture
**Predecessor:** CRC-OAR v1.3

CRC-OAR is not a normative doctrine paper and is not the shared-schema registry.
CRC-OAR v1.0, v1.1, v1.2, and v1.3 remain historical and unchanged.
CRC-OAR v1.4 is a lifecycle-only closure package. No doctrine, schema,
predicate, ownership, registry, or active artifact version changes occur.
Closure is based on already published and verified evidence.

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
- status: RESOLVED
- discovered_in: CRC-SSR lineage reconciliation sequence
- discovery_version: CRC-SSR v1.4 and Core v5.12 active corpus
- gap_statement: BindingRecord cannot be canonically settled until mutation, admission, and binding lineage are defined.
- current_loci: [Core v5.14](constitutional-runtime-computation-v5.14.md), [Standing v1.7](companions/constitutional-standing-v1.7.md), [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md), [CRC README](README.md) for navigation and publication-state evidence only, [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md) and [Core v5.13](constitutional-runtime-computation-v5.13.md) as supporting F-5 evidence
- dependency_relationships: OAR-F005
- blocks: none
- settled_owner: Core owns BindingRecord and BindingRecordValid; Standing owns standing applicability and validation contribution; Task Ledger consumes BindingRecord through CycleRecord.
- current_authority: BindingRecord reconciliation is formally closed. Core ownership of BindingRecord and BindingRecordValid, the canonical BindingRecord schema, historical validation context, binding at valid applied GovernedStateMutationRecord, Standing applicability and non-applicability, standing timing, standing failure placement, CycleRecord Bind lineage, Task Ledger binding-closure repair, missing-record reconciliation, reconstructed BindingRecord provenance, duplicate and replay handling, append-only historical integrity, CRC-SSR registration, and F-5 dependency settlement are fully settled. No BindingRecord ownership or schema ambiguity remains, and no unresolved F-3 architectural question remains.
- required_resolution: complete.
- closure_conditions: satisfied. Closure evidence is supplied by Core v5.14, Standing v1.7, Constitutional Task Ledger v1.4, CRC-SSR v1.6, F-5 public evidence, and CRC README navigation and publication evidence only.
- registry_implications: `crc-ssr:binding-record` is REGISTERED in CRC-SSR v1.6.
- canonical_destination: [Core v5.14 Canonical BindingRecord](constitutional-runtime-computation-v5.14.md), [Standing v1.7](companions/constitutional-standing-v1.7.md), [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md), [CRC-SSR v1.6 crc-ssr:binding-record](shared-schema-registry-v1.6.md)
- unresolved_questions: none.
- notes: non-authoritative wikilinks: [[BindingRecord]]
- history: created in CRC-OAR v1.0 as BLOCKED by OAR-F005; v1.1 records F-5 Phase 1 publication and a public dependency contract while preserving BLOCKED pending separate F-3 restart ratification; v1.2 moves OAR-F003 from `BLOCKED` to `SPECIFYING`, records F-3 specification restart, Core v5.14 BindingRecord publication, Standing v1.7 standing alignment, Task Ledger v1.4 Bind outcome lineage alignment, and CRC-SSR v1.6 BindingRecord registration; v1.3 moves OAR-F003 from `SPECIFYING` to `SPECIFIED` after public specification evidence was verified; v1.4 moves OAR-F003 from `SPECIFIED` to `RESOLVED` after independent closure evidence verification. No doctrine or schema change was required. F-3 is formally closed.

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
- status: RESOLVED
- discovered_in: F-2, F-1, F-3, and F-5 architecture analyses
- discovery_version: Core v5.12, Standing v1.6, Task Ledger v1.2, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus lacks a generalized constitutional architecture between Resolution and BindingRecord for actuation, actuation result, result admission, governed state mutation, binding, write order, failure topology, and retry or replay.
- current_loci: [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [Standing v1.7](companions/constitutional-standing-v1.7.md) as BindingRecord-dependent evidence, [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md), [CRC README](README.md) for navigation and publication-state evidence only
- dependency_relationships: OAR-A001, OAR-A002, OAR-P001, OAR-A003, OAR-X001, OAR-X002, OAR-X003, OAR-X004, OAR-X005
- blocks: none
- candidate_owner: coordinated Core plus new actuation companion, with Tools specialization
- current_authority: F-5's architectural question is fully settled. The generalized actuation and effect-admission architecture is publicly active. The dependent BindingRecord condition is settled. No remaining F-5 question blocks closure.
- required_resolution: complete.
- closure_conditions: satisfied. Public evidence covers ActuationCommand, ActuationResult, ActuationAdmissionRecord, GovernedStateMutationRecord, command predicates, result predicates, admission predicates, mutation predicates, canonical write order, internal and external branches, partial effects, failed and unknown results, retry and idempotency, duplicate-effect handling, rollback, compensation, audit durability, Tools specialization, Task Ledger obligation handling, BindingRecord dependency settlement, CRC-SSR registration, and cross-artifact ownership consistency.
- registry_implications: CRC-SSR v1.6 inherits the four F-5 shared-object registrations and registers `crc-ssr:binding-record` through F-3. OAR-F005 is `RESOLVED`; apparatus entries close independently in CRC-OAR v1.4.
- canonical_destination: [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md)
- unresolved_questions: none for OAR-F005 closure. Apparatus-entry lifecycle closure is recorded independently in CRC-OAR v1.4.
- history: created in CRC-OAR v1.0 as SPECIFYING after completion of the read-only F-5 architecture analysis; v1.1 records public F-5 Phase 1 publication and moves OAR-F005 from `SPECIFYING` to `SPECIFIED`; v1.3 moves OAR-F005 from `SPECIFIED` to `RESOLVED` after BindingRecord dependency settlement and verification of all applicable F-5 closure conditions. OAR-F005 is the only newly `RESOLVED` entry in v1.3.

### OAR-A001

- register_id: OAR-A001
- title: ActuationCommand
- entry_class: apparatus
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus needs a governed command or equivalent object between adjudicative authorization and substrate-owned actuation attempt.
- current_loci: [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core
- canonical_destination: [Core v5.13 ActuationCommand](constitutional-runtime-computation-v5.13.md)
- current_authority: ActuationCommand closure is complete. Core ownership, canonical ActuationCommand schema, `ActuationCommandIssuable`, `ActuationCommandValid`, substrate issuance, authority-context pinning, domain-constitution pinning, task and cycle lineage, scope containment, command identity, one-use behavior, retry interaction, duplicate prevention, Tools specialization boundary, CRC-SSR registration, and absence of a competing canonical command object are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: registered as `crc-ssr:actuation-command` in CRC-SSR v1.6.
- unresolved_questions: none.
- notes: non-authoritative wikilinks: [[ActuationCommand]]
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public definition evidence and moves OAR-A001 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-A001 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-A001 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-A002

- register_id: OAR-A002
- title: ActuationResult
- entry_class: apparatus
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus needs a generalized result object or equivalent record for attempted, completed, failed, partial, timed out, unknown, externally irreversible, compensated, duplicate, or replay-detected actuation outcomes.
- current_loci: [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core
- canonical_destination: [Core v5.13 ActuationResult](constitutional-runtime-computation-v5.13.md)
- current_authority: ActuationResult closure is complete. Core ownership, canonical ActuationResult schema, `ActuationResultValid`, exact status vocabulary, command linkage, attempt linkage, result identity, provenance, audit, partial completion, failure, timeout, `RESULT_UNKNOWN`, replay-sensitive treatment, duplicate detection, CRC-SSR registration, and absence of a competing canonical result object are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: registered as `crc-ssr:actuation-result` in CRC-SSR v1.6.
- unresolved_questions: none.
- notes: non-authoritative wikilinks: [[ActuationResult]]
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public definition evidence and moves OAR-A002 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-A002 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-A002 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-P001

- register_id: OAR-P001
- title: Generalized actuation-result admission
- entry_class: predicate
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus has Tools-specific `ToolResultAdmissible`, but lacks a generalized predicate for whether an actuation result may enter governed state.
- current_loci: [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core
- canonical_destination: [Core v5.13 ActuationResultAdmissible](constitutional-runtime-computation-v5.13.md), [Core v5.13 ActuationAdmissionRecord](constitutional-runtime-computation-v5.13.md)
- current_authority: Generalized result admission closure is complete. Generalized admission ownership, `ActuationResultAdmissible`, ActuationAdmissionRecord, AdmissionStatus, partial admission, rejected admission, held admission, escalated admission, verification-required admission, admitted and unadmitted scope, standing-sensitive admission, mutation dependency, branch neutrality, Tools specialization, audit durability, CRC-SSR registration, and absence of a competing generalized admission object are settled. The predicate and record are related but not identical objects.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: predicate registry treatment remains separate; ActuationAdmissionRecord is registered as `crc-ssr:actuation-admission-record` in CRC-SSR v1.6.
- unresolved_questions: none.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public definition evidence and moves OAR-P001 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-P001 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-P001 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-A003

- register_id: OAR-A003
- title: StateMutationRecord
- entry_class: apparatus
- status: RESOLVED
- discovered_in: F-3 and F-5 architecture analyses
- discovery_version: Standing v1.6, Core v5.12, and CRC-SSR v1.4 active corpus
- gap_statement: Standing's existing `state_mutation_ref` does not establish a canonical state-mutation object, leaving mutation lineage unresolved.
- current_loci: [Standing v1.7](companions/constitutional-standing-v1.7.md), [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md)
- dependency_relationships: OAR-F005
- candidate_owner: Core
- canonical_destination: [Core v5.13 GovernedStateMutationRecord](constitutional-runtime-computation-v5.13.md)
- current_authority: StateMutationRecord remains the historical seed name. GovernedStateMutationRecord is the published canonical object. Core ownership, canonical schema, `StateMutationReachable`, `GovernedStateMutationValid`, prior and resulting state lineage, admitted-scope containment, task and cycle alignment, partial mutation treatment, rollback and compensation as later movements, mutation-time binding relationship, CRC-SSR registration, and absence of a competing canonical mutation object are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: registered as `crc-ssr:governed-state-mutation-record` in CRC-SSR v1.6.
- unresolved_questions: none.
- notes: non-authoritative wikilinks: [[StateMutationRecord]]
- history: created in CRC-OAR v1.0 as OPEN under the historical seed name StateMutationRecord; v1.1 records GovernedStateMutationRecord as the published canonical name and moves OAR-A003 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-A003 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-A003 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-X001

- register_id: OAR-X001
- title: Actuation-to-binding write order
- entry_class: architecture_issue
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Standing v1.6, Task Ledger v1.2, Tools v1.1, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus lacks a non-circular ordering among Resolution, actuation command, result, admission, mutation, BindingRecord, CycleRecord, Task Ledger, ContinuationState, and AgentObservation.
- current_loci: [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md)
- dependency_relationships: OAR-F005
- current_authority: actuation-to-binding write order closure is complete. The canonical order is Resolution, ActuationCommand where applicable, attempt, ActuationResult where applicable, ActuationAdmissionRecord, GovernedStateMutationRecord, BindingRecord, CycleRecord, Task Ledger update, ContinuationState, and AgentObservation. Binding at mutation, evidentiary BindingRecord, mutation and BindingRecord atomicity allowance, prohibition on BindingRecord preceding mutation, missing BindingRecord repair, CycleRecord Bind waiting for BindingRecord, Task Ledger update after CycleRecord, continuation after closure or lawful repair only, and AgentObservation remaining last are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- unresolved_questions: none.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public write-order evidence and moves OAR-X001 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-X001 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-X001 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-X002

- register_id: OAR-X002
- title: Failure and partial-effect topology
- entry_class: architecture_issue
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Tools v1.1, Core v5.12, and Task Ledger v1.2 active corpus
- gap_statement: The corpus lacks generalized handling for actuator unavailable, failed attempts, unknown results, partial completion, compensation, rollback, and irreversible external effects.
- current_loci: [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md)
- dependency_relationships: OAR-F005
- current_authority: failure and partial-effect topology closure is complete. Failed attempt, partial completion, timeout, unknown result, rejected admission, partial admission, partial mutation, inadmissible external effect, accounting, obligation creation, no_obligation_reason, repair, rollback, compensation, CycleRecord outcome, Task Ledger update, and continuation restrictions are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- unresolved_questions: none.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public failure-topology evidence and moves OAR-X002 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-X002 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-X002 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-X003

- register_id: OAR-X003
- title: Replay, retry, and idempotency
- entry_class: architecture_issue
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, and Task Ledger v1.2 active corpus
- gap_statement: The corpus lacks generalized rules for one-use commands, duplicate detection, retry authority, and unknown-result retry restrictions.
- current_loci: [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md)
- dependency_relationships: OAR-F005, OAR-X002
- current_authority: replay, retry, and idempotency closure is complete. Command identity, attempt identity, result identity, admission identity, mutation identity, BindingRecord identity, retry authorization, silent retry prohibition, idempotency, duplicate result detection, duplicate effect detection, duplicate mutation detection, duplicate bind detection, uncertain persistence, reconstruction, conflicting-evidence escalation, and append-only historical integrity are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- unresolved_questions: none.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public replay and idempotency evidence and moves OAR-X003 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-X003 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-X003 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-X004

- register_id: OAR-X004
- title: Internal versus external effect branches
- entry_class: architecture_issue
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Core v5.12, Tools v1.1, Memory v2.2, Task Ledger v1.2, and domain application corpus
- gap_statement: The corpus lacks a shared branch model for internal mutation, memory, ledger, tools, communications, financial effects, and external-world actions.
- current_loci: [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.14](constitutional-runtime-computation-v5.14.md), [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [Memory v2.2](companions/constitutional-memory-v2.2.md), [Constitutional Task Ledger v1.4](companions/constitutional-task-ledger-v1.4.md)
- dependency_relationships: OAR-F005
- current_authority: internal and external branch topology closure is complete. Internal governed mutation, external actuation, external occurrence before admission, external success, external failure, external partial effect, external unknown result, externally occurred but inadmissible effect, accounting movement, obligation movement, rollback, compensation, branch convergence, audit durability, binding relationship, and continuation treatment are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- unresolved_questions: none.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public branch-architecture evidence and moves OAR-X004 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-X004 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-X004 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

### OAR-X005

- register_id: OAR-X005
- title: Tools specialization relationship
- entry_class: architecture_issue
- status: RESOLVED
- discovered_in: F-5 architecture analysis
- discovery_version: Tools v1.1, Core v5.12, and CRC-SSR v1.4 active corpus
- gap_statement: The corpus must determine how ToolInvocationProposal, ToolResultRecord, and ToolResultAdmissible conform to or specialize generalized Core actuation apparatus.
- current_loci: [Constitutional Tools v1.2](companions/constitutional-tools-v1.2.md), [Constitutional Actuation and Effect Admission v1.0](companions/constitutional-actuation-and-effect-admission-v1.0.md), [Core v5.14](constitutional-runtime-computation-v5.14.md), [CRC-SSR v1.6](shared-schema-registry-v1.6.md)
- dependency_relationships: OAR-F005, OAR-A001, OAR-A002, OAR-P001
- current_authority: Tools specialization closure is complete. Tools v1.2 specialization of generalized F-5, ToolInvocationProposal remaining a proposal, ToolInvocationReachable not issuing commands, ToolResultRecord specializing ActuationResult, ToolResultAdmissible specializing generalized admission, tool admission mapping to ActuationAdmissionRecord, tool-caused state change mapping to GovernedStateMutationRecord, final binding using Core BindingRecord, Tools not owning generic command, result, admission, mutation, or BindingRecord, and absence of a hidden tool-only authority path are settled.
- required_resolution: complete.
- closure_conditions: satisfied.
- registry_implications: not itself a registry object unless later formalized as shared load-bearing apparatus.
- unresolved_questions: none.
- history: created in CRC-OAR v1.0 as OPEN; v1.1 records public Tools-specialization evidence and moves OAR-X005 from `OPEN` to `SPECIFYING`; v1.3 moves OAR-X005 from `SPECIFYING` to `SPECIFIED`; v1.4 moves OAR-X005 from `SPECIFIED` to `RESOLVED` after closure evidence verification.

## v1.4 Cross-Entry Closure

All ten candidate entries independently satisfy their closure conditions. No
apparatus entry requires another apparatus entry to be `RESOLVED` first. F-3
closure relies on published BindingRecord and F-5 evidence, not apparatus
terminal status. Apparatus closure relies on already published doctrine and
registrations. No circular closure dependency exists. Closure in one package is
an administrative grouping of independently justified transitions. OAR-F005
remains resolved from v1.3.

## Residual F-3/F-5 Workstream State

After v1.4, the F-3/F-5 workstream state is:

- OAR-F003: `RESOLVED`
- OAR-F005: `RESOLVED`
- OAR-A001: `RESOLVED`
- OAR-A002: `RESOLVED`
- OAR-P001: `RESOLVED`
- OAR-A003: `RESOLVED`
- OAR-X001: `RESOLVED`
- OAR-X002: `RESOLVED`
- OAR-X003: `RESOLVED`
- OAR-X004: `RESOLVED`
- OAR-X005: `RESOLVED`

No `OPEN` entry remains in this workstream. No `BLOCKED` entry remains in this
workstream. No `SPECIFYING` entry remains in this workstream. No `SPECIFIED`
entry remains in this workstream. No additional F-3/F-5 lifecycle package is
required. Later correction, reopening, supersession, or newly discovered residue
would require a separate governed package. This statement does not claim that
all CRC-OAR entries globally are resolved.

## Version History

*v1.4. Formal closure package for F-3 BindingRecord reconciliation and the F-5
apparatus architecture. Status transitions: OAR-F003 `SPECIFIED` to `RESOLVED`;
OAR-A001 `SPECIFIED` to `RESOLVED`; OAR-A002 `SPECIFIED` to `RESOLVED`;
OAR-P001 `SPECIFIED` to `RESOLVED`; OAR-A003 `SPECIFIED` to `RESOLVED`;
OAR-X001 `SPECIFIED` to `RESOLVED`; OAR-X002 `SPECIFIED` to `RESOLVED`;
OAR-X003 `SPECIFIED` to `RESOLVED`; OAR-X004 `SPECIFIED` to `RESOLVED`;
OAR-X005 `SPECIFIED` to `RESOLVED`. Exactly ten entries are newly `RESOLVED`.
OAR-F005 remains `RESOLVED` from v1.3. No lifecycle state was skipped. No
unrelated entry changed status. No doctrine or schema artifact changed. The
F-3/F-5 workstream is lifecycle-closed.*

*v1.3. Bounded lifecycle-only transition package after F-3 BindingRecord
reconciliation and F-5 closure review. Status transitions: OAR-F003
`SPECIFYING` to `SPECIFIED`; OAR-F005 `SPECIFIED` to `RESOLVED`; OAR-A001
`SPECIFYING` to `SPECIFIED`; OAR-A002 `SPECIFYING` to `SPECIFIED`; OAR-P001
`SPECIFYING` to `SPECIFIED`; OAR-A003 `SPECIFYING` to `SPECIFIED`; OAR-X001
`SPECIFYING` to `SPECIFIED`; OAR-X002 `SPECIFYING` to `SPECIFIED`; OAR-X003
`SPECIFYING` to `SPECIFIED`; OAR-X004 `SPECIFYING` to `SPECIFIED`; OAR-X005
`SPECIFYING` to `SPECIFIED`. OAR-F005 is the only newly `RESOLVED` entry.
OAR-F003 remains not `RESOLVED`. All apparatus entries remain not `RESOLVED`.
No doctrine or schema artifact changed. No lifecycle state was skipped.*

*v1.2. F-3 BindingRecord restart and first lawful transition package. Moves
OAR-F003 from `BLOCKED` to `SPECIFYING`. Records that F-3 specification work
restarted, Core v5.14 published BindingRecord and BindingRecordValid, Standing
v1.7 aligned standing applicability and historical validation doctrine, Task
Ledger v1.4 aligned Bind outcome lineage, and CRC-SSR v1.6 registered
BindingRecord. No F-5 entry advanced. No entry became newly `RESOLVED`. F-3 is
not `SPECIFIED` and not `RESOLVED`. Potential later CRC-OAR v1.3 transitions,
after separate ratification, include OAR-F003 `SPECIFYING` to `SPECIFIED`,
OAR-F005 `SPECIFIED` to `RESOLVED`, and OAR-A001, OAR-A002, OAR-P001, OAR-A003,
and OAR-X001 through OAR-X005 `SPECIFYING` to `SPECIFIED`. Potential CRC-OAR
v1.4 or later transitions include OAR-F003 `SPECIFIED` to `RESOLVED` and
apparatus entries `SPECIFIED` to `RESOLVED` when their closure conditions pass.
These future transitions are not pre-authorized by v1.2.*

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
