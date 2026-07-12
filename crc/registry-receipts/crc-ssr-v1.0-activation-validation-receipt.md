# CRC-SSR v1.0 Activation Validation Receipt

This receipt records validation only. It does not activate CRC-SSR. The B.7 inaugural registry in Core Appendix B remains the active registry of record until a later Core-carried archival transition activates CRC-SSR. This pass edited no paper and no registry entry; it read them and recorded the verdict. No check was repaired; validation observes, it does not fix.

No em dashes are used in this receipt.

## Receipt header

- registry_version: v1.0
- validated_commit: 2691d3f97e5c4cf373a556be287134b9073fd870 (2691d3f)
- registry_path: crc/shared-schema-registry-v1.0.md
- core_path: crc/constitutional-runtime-computation-v5.9.md
- registry_blob_oid: e9e750d1d769c54c1a0b03e7b35d00b10a6ee4f6
- core_blob_oid: e0f064055f4637ff97c1444bc9e6cfec8e0a2924
- validation_date: 2026-07-11
- validated_against: activation package spec Section 5 checklist and Section 6 seed scope; Core Appendix B B.9 authority and pointer rules; B.7 remains active
- live corpus at validation: Core v5.9, C0 v1.2, C1 v2.2, C2 v1.2, C3 v1.2, C4 v1.4, C5 v1.4, C6 v1.5, C7 v1.1, C8 v1.2, C9 v1.0

### validated_schema_ids (twelve)

1. crc-ssr:transition-proposal
2. crc-ssr:resolution
3. crc-ssr:continuation-state
4. crc-ssr:agent-observation
5. crc-ssr:binding-record
6. crc-ssr:task-ledger
7. crc-ssr:pending-obligation
8. crc-ssr:non-formation-receipt
9. crc-ssr:generation-member
10. crc-ssr:goal-status-enum
11. crc-ssr:authority-context-ref
12. crc-ssr:proposal-conformant

## Gate verdict

**gate_verdict: PASS.** Every check passes for every one of the twelve seed entries. Nine REGISTERED entries pass all pointer-bearing checks; three AMBIGUOUS lineage entries pass under the ambiguous special rule as honest unresolved records. No entry was reconciled; F-1 through F-4 remain open by design.

## Roll-up results

- pointer_resolution_result: PASS. Every REGISTERED pointer triple resolves to a live anchor at the pinned version; every AMBIGUOUS entry's candidate loci resolve.
- version_consistency_result: PASS. Every REGISTERED operative_version matches the live defining paper; the three AMBIGUOUS entries carry operative_version unresolved by design, which is consistent.
- back_reference_result: PASS. The two present back-references (generation-member R6, goal-status-enum R4) exist in the live papers; every not_applicable entry has no live extension requiring an omitted back-reference.
- duplicate_entry_result: PASS. Twelve distinct schema_ids, no schema_id appears twice.
- orphan_entry_result: PASS. Every one of the twelve seed objects has an entry; no entry names an object outside the seed scope.
- status_honesty_result: PASS. No AMBIGUOUS entry asserts a settled pointer or version; every entry carries all sixteen fields plus an append-only history block; every history block reads created at v1.0 publication.

## Per-object results

Each REGISTERED entry is scored on pointer_resolution (PR), version_consistency (VC), back_reference (BR), duplicate_entry (DUP), orphan_entry (ORPH), status_honesty (SH). Each AMBIGUOUS entry is scored on the four special-rule conditions plus DUP, ORPH, and SH.

### 1. crc-ssr:transition-proposal (REGISTERED, core_owned, core_bound)

- PR: PASS. Anchor "This ten-field object is the canonical TransitionProposal for the corpus" located in Core v5.9 Section 4.
- VC: PASS. operative_version v5.9 matches live Core v5.9.
- BR: PASS. back_reference_status not_applicable; the Tools and Memory subtypes are new objects, not amendments, so no back-reference is owed. Confirmed no amendment of this object in the live corpus.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history present; history reads created at v1.0 publication, REGISTERED.

### 2. crc-ssr:resolution (REGISTERED, core_owned, core_bound)

- PR: PASS. Anchor "A resolution carries a Resolution object" located in Core v5.9 Section 4.
- VC: PASS. v5.9 matches live Core.
- BR: PASS. not_applicable; no divergent definition, no amendment owed.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, REGISTERED.

### 3. crc-ssr:continuation-state (AMBIGUOUS, F-1)

- Special rule condition 1, all candidate loci resolve: PASS. Core Section 4 "the substrate issues a substrate-owned ContinuationState" located; Appendix A POC construction present (ContinuationState appears through the POC); Constitutional Standing v1.5 Part V "A ContinuationState is the substrate-issued continuity authority" located.
- Special rule condition 2, ambiguity stated honestly, no candidate presented as settled: PASS. Notes name the two forms and state they are not joined by a B.3 amendment.
- Special rule condition 3, no canonical pointer asserted: PASS. operative_version unresolved; defining_anchor unset as canonical; defining_paper marked unsettled pending F-1.
- Special rule condition 4, reconciliation dependency named: PASS. Entry names finding F-1.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, AMBIGUOUS.

### 4. crc-ssr:agent-observation (AMBIGUOUS, F-2)

- Special rule condition 1: PASS. Core Section 4 "constructs the next AgentObservation" located; Appendix A POC builds it; the ObservationContract field schema at Constitutional Boundary Contracts V.2 located.
- Special rule condition 2: PASS. Notes state the Core publishes no field list beneath the C0 view; no candidate presented as settled.
- Special rule condition 3: PASS. operative_version unresolved; defining_anchor unset as canonical; defining_paper marked unsettled pending F-2.
- Special rule condition 4: PASS. Entry names finding F-2.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, AMBIGUOUS.

### 5. crc-ssr:binding-record (AMBIGUOUS, F-3)

- Special rule condition 1: PASS. Core POC field set (binding_record_id and the POC construction) located in Core Appendix A; the canonical BindingRecord field set including state_mutation_ref located in Constitutional Standing Part IV.
- Special rule condition 2: PASS. Notes state two typed forms with no amendment joining them; no candidate presented as settled.
- Special rule condition 3: PASS. operative_version unresolved; defining_anchor unset as canonical; defining_paper marked unsettled pending F-3.
- Special rule condition 4: PASS. Entry names finding F-3.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, AMBIGUOUS.

### 6. crc-ssr:task-ledger (REGISTERED, companion_owned, not_core_bound)

- PR: PASS. Anchor "The central substrate-owned object" located in C8 v1.2 III.1.
- VC: PASS. v1.2 matches live C8 v1.2.
- BR: PASS. not_applicable; the Core POC ledger is explicitly illustrative, a latent drift note, not an amendment, so no back-reference is owed.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, REGISTERED.

### 7. crc-ssr:pending-obligation (REGISTERED, companion_owned, not_core_bound)

- PR: PASS. Anchor "retained as a first-class typed object, not a structured field" located in C8 v1.2 III.2.
- VC: PASS. v1.2 matches live C8 v1.2.
- BR: PASS. not_applicable; C8 owns the canonical object, the Core POC names it without a field list, no amendment owed.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, REGISTERED.

### 8. crc-ssr:non-formation-receipt (REGISTERED, companion_owned, not_core_bound)

- PR: PASS. Locus resolves: NonFormationReceipt is defined in C6 v1.5 Part II as a typed object with exactly twelve fields (receipt_id, candidate_ref, failed_check, cause, submitted_by, cycle_id, state_ref, boundary_contract_ref, schema_ref, continuation_state_ref, authority_context_ref, created_at). The "twelve-field typed object list" anchor is truthful.
- VC: PASS. v1.5 matches live C6 v1.5.
- BR: PASS. not_applicable; C6 owns the schema, Core POC names it without a competing field list, no amendment owed.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, REGISTERED.

### 9. crc-ssr:generation-member (REGISTERED, companion_owned, not_core_bound)

- PR: PASS. Anchor, C4 v1.4 Part II member concept "remains this paper's", located.
- VC: PASS. operative_version v1.4 with a Constitutional Thresholds v1.4 compatible extension; both base (C4 v1.4) and extended (C5 v1.4) versions match the live papers.
- BR: PASS. back_reference_status present. The R6 compatible extension (threshold_set_version) is declared in Constitutional Thresholds and the Constitutional Coherence back-reference is present in live C4 (the member note and Key Terms carry it). extension_or_amendment_refs (R6) agree with the live papers.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history reads created at v1.0 publication, REGISTERED, with the prior RESOLVED R6 closure preserved append-only.

### 10. crc-ssr:goal-status-enum (REGISTERED, companion_owned, not_core_bound)

- PR: PASS. Anchor "Boundary Contracts owns the GoalStatusEnum value set" located in C0 v1.2 V.3.
- VC: PASS. v1.2 matches live C0 v1.2.
- BR: PASS. back_reference_status present. R4 RECONSTITUTED admitted as a seventh value in live C0 v1.2, coupled with the B.6 projection in live Core; extension_or_amendment_refs (R4) agree with the live papers.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, REGISTERED, with the prior RESOLVED R4 closure preserved.

### 11. crc-ssr:authority-context-ref (REGISTERED, core_owned, core_bound)

- PR: PASS. Anchor "a pinned reference to the authority context A, the requester's standing and the authority graph, at evaluation time" located in Core v5.9 Section 6a.
- VC: PASS. v5.9 matches live Core.
- BR: PASS. not_applicable. R5 was resolved by withdrawal under B.4; Constitutional Standing v1.4 withdrew its in-text rebinding and no amendment declaration was required, so no back-reference is owed. Consistent with the live corpus.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, REGISTERED, with the prior RESOLVED-by-withdrawal R5 closure preserved.

### 12. crc-ssr:proposal-conformant (REGISTERED, companion_owned, not_core_bound)

- PR: PASS. Anchor, the proposal-crossing validator, located at C0 v1.2 "## IV.3 Validation predicate: ProposalConformant".
- VC: PASS. v1.2 matches live C0 v1.2.
- BR: PASS. not_applicable. R7 was a naming reconciliation of the Standing alias to the operative ProposalConformant name; the live C6 v1.5 changelog states a naming correction is not an amendment, so no back-reference is owed. Consistent with the live corpus.
- DUP: PASS. ORPH: PASS. SH: PASS. Sixteen fields plus history; history created at v1.0 publication, REGISTERED, with the prior RESOLVED R7 closure preserved.

## Structural integrity summary

- Entry count: twelve entry headers, twelve schema_id lines, all distinct.
- Field completeness: 204 field lines across twelve entries, that is sixteen fields plus one history block per entry, with no entry missing a field.
- History discipline: twelve history blocks, each reading created at v1.0 publication; the four entries with prior closures (R4, R5, R6, R7) preserve those RESOLVED closures append-only rather than overwriting.

## Scope statement

This receipt records validation only. CRC-SSR is not activated by it. B.7 remains the active registry of record until a later Core-carried archival transition. The three AMBIGUOUS lineage entries were validated as honest unresolved records, not resolved; F-1, F-2, F-3, and F-4 are untouched. No registry entry, Core section, README, or companion was edited during this pass.
