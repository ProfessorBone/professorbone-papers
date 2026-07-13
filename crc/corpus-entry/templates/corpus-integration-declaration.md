# Corpus Integration Declaration Template

**Artifact type:** Operational template
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.1
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.12 Appendix B, CRC-SSR v1.4, and CRC-OAR v1.0
**Normative scope:** Work standardization only
**Does not:** Settle substantive doctrine or override governing artifacts

This paper declaration specializes the general Public Artifact Declaration. It does not replace or weaken that declaration.

## Identity and Status

- paper_title: [paper title]
- proposed_public_path: [path]
- identifier: [identifier or none]
- initial_version: [version or none]
- status_at_admission: [proposed status]
- primary_artifact_class: [one primary class]
- secondary_functions: [secondary functions]
- authority_effect: [bounded description of the authority, doctrine, evidence, navigation, or explanation the paper creates or carries]

## Authority

- owning_authority: [owner]
- ratifying_authority: [ratifier]
- relevant_governance_context: [Core, CRC-SSR, defining paper, companion, or none]
- delegated_authority: [delegated authority, or none]

## Purpose and Relationships

- purpose: [purpose]
- relationship_to_core: [relationship]
- relationship_to_defining_papers_or_companions: [relationship]
- dependencies: [dependencies]
- objects_defined: [objects defined]
- objects_consumed: [objects consumed]
- objects_amended: [objects amended]
- objects_superseded: [objects superseded]
- objects_relocated: [objects relocated]

## Open Architecture Dependencies

Use one of the following forms.

```text
Open Architecture Dependencies: none
```

or:

```text
Open Architecture Dependencies:
- oar_id: [active OAR ID]
  status: [current OAR status]
  relationship: [prerequisite | adjacent_dependency | consumer_dependency | candidate_successor | evidence_dependency | informational]
  materiality: [blocking | non-blocking | informational]
  effect: [effect statement]
  coherence_effect: [effect on the new paper's coherence]
  schema_completeness_effect: [effect on schema completeness]
  implementation_readiness_effect: [effect on implementation readiness]
  non_blocking_rationale: [why non-blocking is genuine, or not applicable]
```

The `oar_id` must resolve in active CRC-OAR. Blocking materiality stops canonical
paper admission.

## Public-Surface Effects

- crc_ssr_impact: [new entry, update, no impact]
- crc_readme_impact: [impact]
- reading_order_impact: [impact]
- inbound_reference_impact: [impact]
- changelog_impact: [impact]
- filename_or_path_impact: [impact]

## Lifecycle

- versioning_rule: [rule]
- version_bump_triggers: [triggers]
- deprecation_or_supersession_treatment: [treatment]
- historical_record_treatment: [treatment]

## Validation

- live_anchors_checked: [yes or no]
- links_checked: [yes or no]
- em_dash_check: [yes or no]
- registry_consistency_check: [yes or no]
- validation_receipt_requirement: [required or not required]
- final_changed_file_set: [paths]
- unresolved_findings: [findings or none]
