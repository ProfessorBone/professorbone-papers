# Using CRC-SSR

**Artifact type:** Explanatory artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.0
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.10 Appendix B and CRC-SSR v1.1
**Normative scope:** Explanation of public corpus entry practice only
**Does not:** Override Core, CRC-SSR, or any defining paper


CRC-SSR v1.1 is the active registry of record by pointer for shared load-bearing objects. It records canonical location and operative version. It does not hold schema text.

## Object Resolution

To resolve a shared object:

1. Read [CRC-SSR v1.1](../shared-schema-registry-v1.1.md).
2. Locate the object's registry entry.
3. Read `defining_paper`, `operative_version`, and `defining_anchor`.
4. Follow that pointer to the defining paper and read the canonical definition there.

## Registry Status Values

REGISTERED means the pointer is settled. AMBIGUOUS, DIVERGENT, and AMENDMENT_PENDING record unresolved states and must not be treated as settled definitions. RESOLVED records a closure transition rather than a steady state. DEPRECATED records a retired object or element.

## B.7 Relationship

Core Appendix B B.7 is the archived inaugural divergence docket. Its seven historical rows remain unchanged and are not further updated. The going-forward registry of record is CRC-SSR.

## Limits

CRC-SSR does not create new runtime doctrine, does not relocate schema text, and does not resolve an AMBIGUOUS or DIVERGENT entry by naming it.
