# How to Enter the CRC Corpus

**Artifact type:** Governance artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.1
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.12 Appendix B, CRC-SSR v1.4, and CRC-OAR v1.0
**Normative scope:** Process governance for public corpus entry only
**Does not:** Override Core, CRC-SSR, or any defining paper


This directory is the public entry point for adding, reading, and maintaining tracked public artifacts in the CRC corpus. It governs corpus entry procedure. It does not define runtime doctrine, does not hold canonical schema text, and does not replace the Core, CRC-SSR, or defining papers.

## Tracking Is a Governance Act

A tracked file becomes part of the public corpus surface. It can shape interpretation, navigation, dependency, maintenance, and authority. Admission is therefore governed even when the artifact is not doctrinal.

## How to Read Public Artifacts in This Repository

Not every tracked file is doctrinal authority. Read the artifact type, status, version, and authority statement before treating a file as operative. Normative authority remains in the Core and the defining papers. CRC-SSR records canonical location and operative version, not schema text. Receipts record evidence. Guides explain process. README navigation improves discoverability but does not override an artifact's internal authority statement. Historical files may remain available without remaining operative.

## Public Artifact Admission Protocol

No file becomes a tracked public artifact merely because it is useful or complete. Before admission, its role, authority, ownership, dependencies, lifecycle, navigation placement, validation burden, and relationship to existing corpus artifacts must be declared and reviewed. The complete protocol is in [05-public-artifact-admission.md](05-public-artifact-admission.md).

Initial routing question: Is the proposed material settled doctrine, a recognized
unresolved corpus dependency, or exploratory research?

The guide recognizes three treatment routes:

- Canonical corpus entry: for material with the ownership, authority,
  definition, anchors, dependencies, and validation appropriate to its artifact
  class.
- Open-architecture entry: for a live corpus dependency that lacks a settled
  owner, schema, predicate, event sequence, cross-paper relationship,
  implementation-safe architecture, or evidence surface. The destination is
  CRC-OAR. The only authority acquired is recognized unresolved status and
  dependency lineage.
- Research-only treatment: for speculative, desirable, exploratory, or unused
  material not yet relied upon by a live corpus artifact. The destination is
  working notes, drafts, issues, or private research surfaces.

## Artifact Classes

Each artifact receives exactly one primary class: normative artifact, governance artifact, evidentiary artifact, navigational artifact, explanatory artifact, or operational template. Secondary functions and authority effects are declared separately. See [02-corpus-authority-model.md](02-corpus-authority-model.md).

Significant public artifacts admitted after this guide becomes operative carry an identity-and-status block near the top unless their declaration justifies an exception. Existing artifacts are not retrofitted by this admission pass. See [05-public-artifact-admission.md](05-public-artifact-admission.md).

## Governed Admission Sequence

The sequence is: identify need, assign class, draft declaration, analyze authority and dependencies, design path and lifecycle, identify registry and navigation impacts, draft artifact, review coherence, review hygiene, validate, ratify, apply without staging, review the unstaged diff, authorize exact-path staging, review the staged diff, authorize and perform the commit, authorize and perform the push, and update state where applicable. See [09-review-and-publication-workflow.md](09-review-and-publication-workflow.md) and [figures/public-artifact-admission-flow.svg](figures/public-artifact-admission-flow.svg).

## Necessity Test

Before creating a public file, ask whether the function belongs in a new artifact, an existing artifact, a private workspace note, an excluded audit artifact, a temporary spec, or a template. A file enters the tracked corpus only when its durable public role is clear.

## Guide Files

- [01 Orientation and Source of Truth](01-orientation-and-source-of-truth.md)
- [02 Corpus Authority Model](02-corpus-authority-model.md)
- [03 Using CRC-SSR](03-using-crc-ssr.md)
- [04 New Paper Admission](04-new-paper-admission.md)
- [05 Public Artifact Admission](05-public-artifact-admission.md)
- [06 Amendments and Versioning](06-amendments-and-versioning.md)
- [07 Validation, Publication, and Activation](07-validation-publication-and-activation.md)
- [08 Corpus Engineering Methodology](08-corpus-engineering-methodology.md)
- [09 Review and Publication Workflow](09-review-and-publication-workflow.md)
- [10 Open Architecture Admission](10-open-architecture-admission.md)
  The authoritative guide section for OAR admission triggers, research boundary,
  undefined references, dependency materiality, OAR citations, promotion, and
  closure.

## Templates

- [Public Artifact Declaration](templates/public-artifact-declaration.md)
- [Corpus Integration Declaration](templates/corpus-integration-declaration.md)
- [Orientation Report](templates/orientation-report.md)
- [Publication Checklist](templates/publication-checklist.md)

## Version History

*v1.1. Adds the three-route admission model: canonical corpus entry,
open-architecture entry through CRC-OAR, and research-only treatment. Adds the
CRC-OAR entry route for recognized unresolved corpus dependencies, dependency
materiality review, and the Open Architecture Dependencies declaration field. No
CRC-OAR or CRC-SSR authority changes.*

*v1.0. Initial ratified public entry guide for corpus orientation, artifact
admission, new-paper integration, amendment discipline, validation, publication,
and corpus-engineering methodology.*
