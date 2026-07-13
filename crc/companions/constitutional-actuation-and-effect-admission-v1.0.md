# Constitutional Actuation and Effect Admission

## Commands, Results, Admission, and Governed Mutation in ORSR

### v1.0 Conceptual Architecture Paper, Companion 10 to Constitutional Runtime Computation v5.13
### Short identifier: C10
### Alias: Constitutional Actuation

**Clarence "Faheem" Downs (Professor Bone Lab)**

**Artifact name:** Constitutional Actuation and Effect Admission
**Identifier:** Companion 10
**Short identifier:** C10
**Version:** v1.0
**Artifact class:** normative companion paper within its declared actuation and effect-admission scope
**Corpus:** Constitutional Runtime Computation
**Ratifying authority:** Faheem Downs
**Relationship:** companion to Constitutional Runtime Computation v5.13

---

# 1. Abstract

Substrate-owned actuation is the constitutional bridge between adjudicative authorization and governed causal force. A result acquires force only through validation, admission, valid governed mutation, and binding finalization.

This paper is normative within its declared actuation and effect-admission scope and is Core-bound. It does not own Core sovereignty, the final BindingRecord schema, Tools, Task Ledger, Standing, Memory, or domain semantics. It supplies branch mechanics, failure topology, retry and idempotency doctrine, compensation treatment, audit reconstruction requirements, and conformance rules for companions that specialize Core v5.13's generic F-5 apparatus.

Open Architecture Dependencies:

- oar_id: OAR-F003
  status: BLOCKED
  relationship: consumer_dependency
  materiality: non-blocking
  effect: BindingRecord reconciliation consumes the F-5 dependency contract, but F-5 may publish without resolving or restarting F-3.

Source OAR Entry:

- oar_id: OAR-F005
  status: SPECIFYING
  role: governing source finding

F-5 Closure Targets:

- OAR-A001
- OAR-A002
- OAR-P001
- OAR-A003
- OAR-X001
- OAR-X002
- OAR-X003
- OAR-X004
- OAR-X005

These closure targets are not Open Architecture Dependencies and do not introduce any new corpus-entry relationship value.

# 2. Problem Statement

Before F-5, the corpus separated proposal from Resolution, and Tools separated invocation authorization from result admission, but no generic constitutional layer connected Resolution(Emit) to substrate-owned actuation, result observation, admission, governed mutation, binding dependency, cycle recording, Task Ledger update, ContinuationState, and the next AgentObservation.

The missing layer created risks of collapsing authorization into execution, execution into admission, admission into mutation, and mutation into binding. This paper closes that generic architecture without completing F-3 BindingRecord reconciliation.

# 3. Constitutional Scope

This paper governs the constitutional mechanics of actuation after adjudicative authorization. It applies to internal and external effects, including deterministic internal mutation, memory mutation, task-state mutation, read-only retrieval or tool result use, external reversible and irreversible effects, communication, financial transaction, notification, human-directed action, and sovereign-directed action.

It does not replace Core v5.13's canonical object schemas. It elaborates branch rules and conformance obligations for those Core-owned objects.

# 4. Authority Boundary

The agent may propose. The substrate resolves. Only the substrate may issue an ActuationCommand. The agent cannot transform a proposal into a command, attempt an effect, admit a result, apply a governed mutation, or finalize binding.

Tools, memory stores, task ledgers, and external systems may be endpoints or specialized surfaces. They are not sovereign sources of generic actuation authority unless the substrate role completely mediates command issuance, attempt, result capture, admission, mutation, audit, and continuation.

# 5. Generalized Actuation Model

The constitutional sequence is:

1. proposal nomination
2. adjudicative authorization
3. ActuationCommand issuance
4. actuation attempt
5. ActuationResult
6. result validation
7. ActuationAdmissionRecord
8. GovernedStateMutationRecord
9. binding finalization
10. CycleRecord
11. Task Ledger update
12. ContinuationState
13. AgentObservation

Some deterministic internal branches may perform several post-command stages atomically. Atomic execution does not erase the distinctions. The audit and records must reconstruct each constitutional fact.

# 6. Actuation Commands

An ActuationCommand is the substrate-issued command that scopes actuation authority. C10 does not own the canonical schema; Core v5.13 does. C10 supplies branch conformance.

Branch conformance requires:

- command scope may narrow but never expand authorized scope
- target selection must be within authorized scope
- raw proposal text is not executable authority
- command constraints must identify branch-specific limits
- command expiry must be enforced
- one-use status must be enforced before attempt
- idempotency policy must be known where retry or duplication risk exists

# 7. Actuation Attempts and Results

An attempt begins when a substrate-owned actuator starts execution of a valid ActuationCommand. No separate canonical ActuationAttemptRecord is created. Attempt identity is carried by attempt_id, command reference, actuator identity, audit lineage, and ActuationResult provenance.

An ActuationResult records what was attempted, what was observed, what may have occurred, and what uncertainty remains. A valid ActuationResult does not prove admission.

# 8. Result Validation

Result validation checks authenticity, actuator source, command identity, attempt identity, scope conformance, timestamp ordering, duplicate status, uncertainty, partiality, external-effect evidence where applicable, and provenance.

No result may be synthesized silently by the agent. A result produced by an actuator may still be structurally valid and constitutionally inadmissible.

# 9. Effect Admission

Admission is a separate constitutional adjudication. The generic status vocabulary is:

- PENDING_ADMISSION
- ADMITTED
- PARTIALLY_ADMITTED
- REJECTED
- ADMISSION_HELD
- ADMISSION_ESCALATED
- VERIFICATION_REQUIRED

Bare HELD and ESCALATED are not generic AdmissionStatus values. They remain Resolution or local terminology where explicitly scoped.

Admission-stage routing is not the original Resolution verdict. ADMISSION_ESCALATED requires sovereign or domain authority engagement, but does not pre-establish authority conclusion. PARTIALLY_ADMITTED is lawful only when admitted and rejected scopes are explicit.

# 10. Governed State Mutation

Governed mutation applies admitted effect scope to governed state through an authorized mutation engine. Mutation may not exceed admitted scope. Rejected intended movement produces no intended mutation. Obligation creation and external-effect accounting may be governed mutations when separately admitted and applied.

Append-only stores may represent prior and resulting state through positions, roots, or hashes. Audit append is not automatically a governed mutation. Failed mutation attempts do not produce successful GovernedStateMutationRecords.

# 11. Binding Interface

Binding occurs when an authorized and admitted movement acquires governed causal force through a valid governed-state mutation. Binding may be atomic with mutation or recorded immediately after mutation, but binding must never precede mutation.

F-3 remains responsible for final BindingRecord owner reconciliation, canonical schema, BindingRecordValid, Standing alignment, and registry settlement. C10 supplies the dependency contract: future BindingRecord must be able to reference or reconstruct Resolution, command, result, admission, mutation, task, cycle, authority context, standing basis where applicable, domain constitution, admitted effect scope, binding time, provenance, and audit identity.

# 12. Internal and External Branches

| Branch | Command | Attempt identity | Result | Admission | Mutation | Binding point | Compensation | Verification |
|---|---|---|---|---|---|---|---|---|
| deterministic internal mutation | required | required | required | required, may be atomic | required | valid mutation | rollback possible | usually mechanical |
| memory mutation | required | required | required | required | required | admitted memory mutation | branch-specific | memory policy |
| task-state mutation | required for substantive change | required | required | required | required | admitted task-state mutation | possible | task policy |
| read-only retrieval or tool result | required if actuator-mediated | required | required | required if used downstream | optional evidence mutation | admitted downstream use | usually no | source integrity |
| external reversible effect | required | required | required | required | accounting or state mutation | admitted accounting or state update | possible | often required |
| external irreversible effect | required | required | required | required and strict | accounting mutation | admitted accounting or state update | compensation only | often required |
| communication | required | required | required | required | accounting mutation | admitted communication record | possible | target verification |
| financial transaction | required | required | required | required and strict | accounting mutation | admitted transaction record | domain-specific | required |
| notification | required | required | required | required | accounting mutation | admitted notification record | possible | target verification |
| human-directed action | required | required | required or verification record | required | accounting mutation | admitted human-action record | possible | usually required |
| sovereign-directed action | required or sovereign command route | required | required | required | required | admitted sovereign-directed mutation | domain-specific | sovereign or delegate |

Ordinary audit append is supporting evidence, not an actuation branch, unless the audit store itself is the governed target.

# 13. Failure and Partial Effects

| Case | Treatment |
|---|---|
| actuator unavailable | intended movement does not bind; obligation or no_obligation_reason required |
| invalid command | no attempt; no binding; audit and hold or correction route |
| stale command | no attempt; fresh authority required |
| used command | duplicate or replay violation; no second binding |
| failure before occurrence | failure result recorded; no intended binding |
| partial occurrence | partial result, explicit admission split, obligations for unresolved scope |
| timeout | result is TIMED_OUT or RESULT_UNKNOWN; no silent retry |
| unknown result | admission held or verification required; fresh authority required for retry unless ratified idempotency applies |
| duplicate attempt | duplicate status recorded; no second binding unless idempotency proves no duplicate effect |
| duplicate effect | accounting and possible compensation obligation |
| effect beyond scope | inadmissible beyond scope; escalation or rejection |
| valid but inadmissible result | no governed causal force |
| external occurrence that cannot be admitted | accounting obligation; intended movement does not bind |
| mutation failure | no completed binding; remedial obligation or escalation |
| partial mutation | explicit partial mutation; rollback, compensation, or escalation |
| rollback success | rollback may bind as its own admitted mutation |
| rollback failure | compensation or sovereign review obligation |
| compensation success | compensation binds separately |
| compensation failure | obligation and escalation |
| verification requirement | no mutation or binding until verification route completes |
| sovereign review | admission escalated; conclusion remains open |

Cycle closure is possible only when the terminal bind or non-bind outcome is recorded and obligations are accounted for. Continuation may issue only from substrate-owned continuation authority.

# 14. Replay, Retry, and Idempotency

Commands are one-use. Idempotency keys are substrate-owned. Retry is lawful only under explicit safe-retry authority or fresh authority. Unknown results must not be silently retried. External idempotency guarantees are evidence, not constitutional proof. Duplicate detection must exist in result, mutation, and audit layers.

Invariant: an effect with unknown result must not be retried unless fresh authority or an explicitly ratified idempotency rule accounts for possible prior occurrence.

# 15. Compensation and Rollback

Compensation is normally a distinct constitutional movement. Compensation may use fresh Resolution, bounded pre-authorized remedial authority, or sovereign-directed authority. Compensation does not erase historical occurrence.

Rollback after binding is a new governed mutation and may form a separate binding event. Rollback attempted but not applied remains evidence only. Compensation failure creates obligation and escalation.

# 16. Audit Durability and Reconstruction

Before any externally consequential progression, the substrate must durably capture the relevant audit event in a substrate-controlled, tamper-evident, reconstructable form. Central audit-store replication may occur after progression only under a ratified degraded-mode rule that preserves ordering, substrate signature, later replication, and an explicit audit-repair obligation. In-memory logging alone is never sufficient. If no durable audit capture is available, actuation, admission, mutation, and binding progression must halt unless an explicit sovereign emergency rule authorizes a narrower action with mandatory post-event reconstruction. Audit capture proves lineage; it does not itself create binding.

Durable capture is required before each downstream progression: command before attempt, result before admission, admission before mutation, mutation before binding finalization, and BindingRecord before CycleRecord and Task Ledger closure. Delayed central replication creates an audit-repair obligation. Domain constitutions may impose stricter synchronous requirements.

# 17. Specialization Contract

A specialization may narrow actuation types, add fields, add predicates, impose stricter durability, impose stricter standing, and impose stricter domain authorization.

A specialization may not remove generic required fields, weaken command validity, convert result validity into admission, bypass mutation, bind on external occurrence alone, expand authority, bypass audit durability, or bypass ContinuationState.

Tools v1.2 specializes the generic model for tool invocation and result admission. Task Ledger v1.3 specializes obligation and cycle-recording consequences. Memory and other companions may remain unchanged under Option Y unless they revise their owned schemas.

# 18. Security and Abuse Cases

Primary abuse cases include agent command forgery, actuator self-authorization, result synthesis, admission laundering, mutation beyond admitted scope, external occurrence treated as binding, silent retry after unknown result, compensation erasure, audit bypass, private-continuation restart, and sovereign conclusion pretense after escalation.

Each abuse case is governed by the non-collapse invariants in this paper and by Core v5.13's canonical predicates.

# 19. Formal Invariants

1. No actuation without valid substrate-issued command.
2. Command scope may narrow but never expand authorized scope.
3. Attempt does not prove completion.
4. Valid result does not prove admissibility.
5. Admission does not prove mutation.
6. External occurrence does not create governed causal force.
7. Mutation may not exceed admitted effect scope.
8. Binding never precedes valid governed mutation.
9. Unknown result forbids silent retry.
10. Compensation does not erase historical occurrence.
11. Admission routing does not pre-establish sovereign conclusion.
12. Audit capture is evidentiary and required for reconstructability, but not itself binding.
13. No private continuation bypass may restart failed or unresolved movement.

# 20. Conformance Requirements

A conforming F-5 specialization must cite Core v5.13's canonical schemas, preserve the generic sequence, map local records to the generic object family, preserve the admission vocabulary or provide an explicit mapping, keep audit durability intact, account for failed and partial effects, and identify whether any branch requires stricter domain or sovereign authority.

Conformance does not grant implementation permission for unresolved objects. F-3 BindingRecord remains blocked until separately restarted.

# 21. Open Architecture Closure Targets

This paper specifies the architecture needed to move the following OAR entries through later lawful OAR status transitions: OAR-F005, OAR-A001, OAR-A002, OAR-P001, OAR-A003, OAR-X001, OAR-X002, OAR-X003, OAR-X004, and OAR-X005. CRC-OAR v1.0 is unchanged by this paper. Status transitions require a later versioned OAR package.

# 22. Version History

*v1.0. Initial publication. Companion 10 to Constitutional Runtime Computation v5.13. Defines branch mechanics and conformance doctrine for Core v5.13's F-5 apparatus: substrate-owned ActuationCommand issuance, actuation attempt and ActuationResult recording, result validation, ActuationAdmissionRecord, GovernedStateMutationRecord, binding dependency contract, failure and partial-effect topology, replay and idempotency, compensation and rollback, audit durability, and specialization rules. Aligns with Constitutional Tools v1.2 and Constitutional Task Ledger v1.3. Does not complete F-3 BindingRecord reconciliation, change CRC-OAR status, or settle `crc-ssr:binding-record`. No em dashes.*
