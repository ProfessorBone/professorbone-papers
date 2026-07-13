# Validation, Publication, and Activation

**Artifact type:** Explanatory artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.0
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.10 Appendix B and CRC-SSR v1.1
**Normative scope:** Explanation of public corpus entry practice only
**Does not:** Override Core, CRC-SSR, or any defining paper


Publication and activation are distinct. Publishing an artifact can make it visible without making it active. Activation requires the gate specified for that artifact class.

## Validation Receipts

A receipt records evidence that a gate was checked. Receipts bind to exact commits and, where needed, exact blob identities. A receipt is evidentiary, not doctrinal authority by itself.

## CRC-SSR Worked Example

CRC-SSR v1.0 was first published as the candidate seed. Core v5.10 B.9 supplied the authorization route for registry activation but did not itself make the registry active. The seed was then validated against commit 2691d3f and the required blob identities, with the result recorded in [the activation-validation receipt](../registry-receipts/crc-ssr-v1.0-activation-validation-receipt.md). Core v5.10 B.10 subsequently recorded the activation transition by making CRC-SSR v1.1 the active registry of record.

## Two-Commit Pattern

When activation depends on validation, publish and activate in separate governed changes. The first commit publishes the candidate. The second carries the receipt and activation transition after the gate passes.
