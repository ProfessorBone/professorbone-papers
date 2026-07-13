# Open Architecture Admission

**Artifact type:** Governance artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.1
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.12 Appendix B, CRC-SSR v1.4, and CRC-OAR v1.0
**Normative scope:** Process governance for CRC-OAR admission only
**Does not:** Define runtime doctrine, settle architecture, authorize implementation, or override Core, CRC-OAR, CRC-SSR, or any defining paper

This section governs how a recognized unresolved dependency enters CRC-OAR
without entering canonical doctrine.

## Three-Route Decision

1. Does a live corpus artifact already rely on the concept?
   - No: research-only treatment.
   - Yes: continue.
2. Does it have a settled owner, lawful definition or schema, and versioned canonical anchor?
   - Yes: canonical corpus-entry process.
   - No: continue.
3. Does the unresolved condition affect lawful publication or implementation?
   - Yes: CRC-OAR admission with blocking materiality.
   - No, but it affects dependency lineage or interpretation: CRC-OAR admission with non-blocking materiality.
   - No material effect, but it provides useful governed orientation: informational.

Informational status does not justify creating an OAR entry by itself. The
referenced entry must already satisfy OAR admission rules.

## Authority Boundary

CRC-OAR recognizes unresolved dependency status. It does not define canonical
doctrine or schemas. It does not authorize implementation. Candidate ownership
remains unsettled. OAR recognition cannot be used to bypass artifact-completeness
requirements.

## Undefined-Reference Rule

When proposed corpus text depends on an object, predicate, record, enumeration,
or architectural mechanism without a canonical owner or defining anchor, the
dependency must either be resolved before publication or entered into CRC-OAR and
explicitly labeled unresolved, provisional, blocked, illustrative, or outside
scope. The OAR identifier must accompany the label.

## Dependency Materiality Test

Governing question: Can the proposed artifact remain coherent, valid, and
non-misleading without resolution of the open dependency?

`blocking`: the artifact cannot be lawfully completed, validated, published, or
implemented without resolving the dependency. Result: stop canonical admission.

`non-blocking`: the artifact remains coherent, valid, bounded, and
non-misleading while the dependency stays unresolved. Result: admission may
proceed with explicit declaration.

`informational`: the reference provides governed orientation or historical
context but does not affect coherence, validation, publication, or
implementation. Result: declare the reference without treating it as a
prerequisite.

## Required Declaration Shape

```text
Open Architecture Dependencies:
- oar_id: OAR-F003
  relationship: adjacent_dependency
  materiality: non-blocking
  effect: BindingRecord remains unresolved through CycleRecord outcome lineage.
```

Required fields are `oar_id`, `relationship`, `materiality`, and `effect`.

Allowed relationship values are exactly:

- `prerequisite`
- `adjacent_dependency`
- `consumer_dependency`
- `candidate_successor`
- `evidence_dependency`
- `informational`

Allowed materiality values are exactly:

- `blocking`
- `non-blocking`
- `informational`

## OAR Citation Rule

Canonical papers and public governance artifacts must cite OAR entries using a
normal Markdown link to the active OAR artifact, the entry identifier, the
current status, and one permitted label: unresolved, provisional, blocked,
illustrative, or outside scope. Raw Obsidian wikilinks must not be used as
canonical citations.

OAR references must not imply that OAR recognition creates canonicality,
validity, reachability, executability, admissibility, binding force, or
implementation permission.

## Examples

F-1, non-blocking adjacent dependency: ContinuationState could be settled while
BindingRecord remained unresolved because the canonical ContinuationState schema
excluded BindingRecord fields and preserved outcome lineage through Resolution,
CycleRecord, Task Ledger, and audit trace.

F-3, blocking prerequisite: BindingRecord could not be canonically settled while
state mutation, result admission, and binding finalization remained undefined.

F-5, open-architecture admission: Substrate Actuation and Effect Admission
entered CRC-OAR because it was a ratified load-bearing architectural gap, but had
not yet become canonical doctrine or implementation authority.

## Promotion Lifecycle

Research note -> recognized corpus dependency -> CRC-OAR entry -> specification
-> ratification -> Core, companion, or governance integration -> CRC-SSR
registration where applicable -> public publication -> CRC-OAR RESOLVED.

Not every item requires every stage. Governance issues may never require
CRC-SSR. Publication means successful public push. OAR status transition requires
a new OAR version. Closure occurs only after all applicable closure conditions
pass.

## Stop Conditions

Canonical entry must stop when:

- unresolved dependency materiality is blocking
- OAR is being used as implementation permission
- candidate schema text is being treated as canonical
- an undefined reference lacks an OAR entry where admission is mandatory
- a referenced OAR identifier does not exist
- dependency effects cannot be stated precisely
- the artifact would be misleading without the missing apparatus
