# New Paper Admission

**Artifact type:** Governance artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.1
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.12 Appendix B, CRC-SSR v1.4, and CRC-OAR v1.0
**Normative scope:** Process governance for public corpus entry only
**Does not:** Override Core, CRC-SSR, or any defining paper


New paper admission is a specialized case of public artifact admission. A paper can carry doctrine, extend the corpus, change reading order, or create new dependency surfaces, so its review burden is higher than an ordinary explanatory artifact.

## Corpus Integration Declaration

Before drafting a new paper as a public artifact, the author prepares a Corpus Integration Declaration using [templates/corpus-integration-declaration.md](templates/corpus-integration-declaration.md). The declaration records purpose, primary class, authority effect, relationship to the Core, relationship to CRC-SSR, reading-order placement, dependencies, versioning, and validation checks.

Every Corpus Integration Declaration must include Open Architecture
Dependencies. The field may be:

```text
Open Architecture Dependencies: none
```

or:

```text
Open Architecture Dependencies:
- oar_id: OAR-F003
  relationship: adjacent_dependency
  materiality: non-blocking
  effect: BindingRecord remains unresolved through CycleRecord outcome lineage.
```

Allowed relationship values are exactly `prerequisite`,
`adjacent_dependency`, `consumer_dependency`, `candidate_successor`,
`evidence_dependency`, and `informational`. Allowed materiality values are
exactly `blocking`, `non-blocking`, and `informational`. Free prose is allowed
only in `effect`. Every referenced `oar_id` must exist in active CRC-OAR.

## Reading Order and Navigation

A new paper may require `crc/README.md` navigation changes. It may also affect the recommended reading order, but that is a public interpretive claim and must be justified.

## Version and Citation Discipline

A version header or changelog change is a substantive claim. A filename or markdown-path update is navigation hygiene. Companion alignment citations move only when the companion text earns that claim. Option Y remains in force: narrow, non-breaking Core changes do not require mass updates to companion Core-alignment citations when the definitions consumed by those companions have not changed. The reading-order Core citation remains at v5.5 unless separately ruled.

## Registry Impacts

If the paper defines, consumes, amends, or relocates a shared load-bearing object, the declaration must state whether CRC-SSR needs a new entry or update.

## Undefined References and OAR Dependencies

When proposed corpus text depends on an object, predicate, record, enumeration,
or architectural mechanism without a canonical owner or defining anchor, the
dependency must either be resolved before publication or entered into CRC-OAR and
explicitly labeled unresolved, provisional, blocked, illustrative, or outside
scope. The OAR identifier must accompany the label.

A blocking dependency stops canonical paper admission. A non-blocking dependency
may proceed only if the paper remains coherent, valid, and non-misleading without
resolution. An informational dependency does not affect the paper's coherence or
implementation viability. An OAR entry cannot cure an otherwise incomplete paper.
