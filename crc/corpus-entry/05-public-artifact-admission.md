# Public Artifact Admission

**Artifact type:** Governance artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.1
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.12 Appendix B, CRC-SSR v1.4, and CRC-OAR v1.0
**Normative scope:** Process governance for public corpus entry only
**Does not:** Override Core, CRC-SSR, or any defining paper


This file carries the Public Artifact Admission Protocol. New-paper admission is one case beneath this umbrella rule.

## Umbrella Rule

No file becomes a tracked public artifact merely because it is useful, complete, or already present in a working directory. Before admission, its role, authority, ownership, dependencies, lifecycle, navigation placement, validation burden, and relationship to existing corpus artifacts must be declared and reviewed.

## Necessity Test

Before creating a public file, ask whether the need belongs in a new artifact, an existing artifact, a private workspace note, an excluded audit artifact, a temporary spec, or a template. Public admission is appropriate only when the role is durable, public, and clear.

## Private Versus Public

Private working artifacts support deliberation. Public tracked artifacts represent the corpus to readers and therefore require admission. A private spec can be useful without being doctrine.

## Route Selection

Public admission now distinguishes three routes.

- Canonical corpus entry: material enters the appropriate public artifact with
  the ownership, authority, definition, anchors, dependencies, and validation
  required by that artifact class.
- Open-architecture entry: a live corpus dependency lacking a settled owner,
  schema, predicate, event sequence, cross-paper relationship,
  implementation-safe architecture, or evidence surface enters CRC-OAR as
  recognized unresolved dependency lineage only.
- Research-only treatment: speculative, desirable, exploratory, or unused
  material remains in working notes, drafts, issues, or private research
  surfaces until it becomes a corpus dependency.

See [10-open-architecture-admission.md](10-open-architecture-admission.md).

OAR admission is mandatory when a public artifact depends on an object without a
canonical owner or locus, a named field references an undefined object, multiple
papers publish competing definitions, architecture review identifies missing
apparatus blocking another object, a required predicate lacks an owner, or lawful
publication or implementation cannot proceed without missing architecture.

CRC-OAR is not a general research backlog, a list of desirable improvements, a
catalog of every undefined term, or a substitute for private design notes.

## Public Artifact Declaration

Every proposed public artifact has a declaration covering identity, purpose, authority, corpus relationships, public-surface effects, lifecycle, and validation. Use [templates/public-artifact-declaration.md](templates/public-artifact-declaration.md).

Every proposed public artifact, including governance, evidentiary, navigational,
explanatory, and operational-template artifacts, must include the Open
Architecture Dependencies field.

## Identity and Status Block

Every significant public artifact admitted after this guide becomes operative carries a compact identity-and-status block near the top. The block states at least the artifact type, identifier if any, version if any, status, ratifying authority, governance context, normative scope, and what the artifact does not do. An artifact may omit the block only when its Public Artifact Declaration records and justifies the exception.

This requirement is prospective. This admission pass does not retrofit existing public artifacts. Adding an identity-and-status block to an existing artifact requires a separate governed change under that artifact's applicable authority, versioning, and validation rules.

## Worked First Declaration

<!-- BEGIN GUIDE PUBLIC ARTIFACT DECLARATION -->
artifact_title: How to Enter the CRC Corpus
primary_artifact_class: governance artifact
secondary_functions: navigational, explanatory, operational-template-bearing
authority_effect: after ratification by Faheem Downs, governs admission procedure for future tracked public artifacts; does not derive authority from CRC-SSR and does not override Core, CRC-SSR, or defining papers
proposed_path: crc/corpus-entry/
public_identifier: CRC-CORPUS-ENTRY
initial_version: v1.0
owning_authority: Professor Bone Lab
ratifying_authority: Faheem Downs
relevant_governance_context:
  - Constitutional Runtime Computation v5.10 Appendix B
  - CRC-SSR v1.1
status_at_admission: ratified by Faheem Downs on 2026-07-12 and published through reviewed public apply pass
purpose: Provide the public entry point for corpus orientation, public artifact admission, new-paper integration, amendment discipline, validation, publication, and corpus-engineering methodology.
authority: Owned by Professor Bone Lab and ratified by Faheem Downs. Existing artifacts provide governance context but do not delegate authority to this guide.
corpus_relationships: Explains admission procedure for future tracked public artifacts. Does not define runtime doctrine, canonical schema text, or shared-object operative versions.
public_surface_effects: Future apply pass creates crc/corpus-entry/ and adds bounded crc/README.md navigation plus a Public Artifacts and Corpus Admission section.
lifecycle: Versioned in the guide identity block. Version changes are substantive when the admission protocol changes. Historical versions remain part of the public record after publication.
validation: Package completeness, link checks, SVG XML checks, em-dash checks, candidate-status inventory, and Faheem ratification were completed before public copy.
<!-- END GUIDE PUBLIC ARTIFACT DECLARATION -->

## Admission Result

The declaration records and structures the authority decision. It is not itself the source of authority. The guide becomes operative only after explicit ratification by Faheem Downs and publication through a reviewed apply pass.
