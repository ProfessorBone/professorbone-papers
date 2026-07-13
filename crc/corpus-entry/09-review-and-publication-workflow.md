# Review and Publication Workflow

**Artifact type:** Governance artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.1
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.12 Appendix B, CRC-SSR v1.4, and CRC-OAR v1.0
**Normative scope:** Process governance for public corpus entry only
**Does not:** Override Core, CRC-SSR, or any defining paper


This workflow governs movement from private need to public artifact.

## Sequence

1. Need for new artifact identified.
2. Artifact class determined using [02-corpus-authority-model.md](02-corpus-authority-model.md).
3. Public Artifact Declaration drafted.
4. Authority and dependency analysis completed.
5. Path, version, and lifecycle designed.
6. Registry and navigation impacts identified.
7. Artifact drafted.
8. Coherence review completed.
9. Hygiene review completed.
10. Validation or receipt completed if required.
11. Human ratification obtained.
12. Authorized apply pass performed without staging.
13. Unstaged changed-file set and full diff reviewed.
14. Exact-path staging separately authorized.
15. Only the authorized paths staged.
16. Staged changed-file set and cached diff reviewed.
17. Commit separately authorized and performed.
18. Push separately authorized and performed.
19. `state.md` updated in the maintained workspace after publication.

## Review Gates

Coherence review checks authority, source discipline, and scope. Hygiene review checks links, filenames, em dashes, public navigation, and stale references. Candidate-package review checks the private package before any public apply pass. Unstaged public-apply diff review checks the changed-file set and full diff before staging. Staged cached-diff review checks the exact staged paths and cached diff before commit. Commit authorization and push authorization remain separate.

## Open Architecture Dependency Gate

Before staging authorization, reviewers must answer:

1. Does the artifact introduce or rely on an object without a canonical owner?
2. Does it contain a field referencing an undefined object, record, predicate, enumeration, or mechanism?
3. Are competing definitions present elsewhere in the corpus?
4. Does every referenced OAR identifier exist?
5. Is each unresolved dependency classified as blocking, non-blocking, or informational?
6. Can the artifact remain coherent, valid, and non-misleading without resolving every non-blocking dependency?
7. Is every blocking dependency treated as a stop condition?
8. Does any OAR reference accidentally imply canonicality or implementation permission?
9. Are raw Obsidian wikilinks absent from canonical citations?

See [figures/public-artifact-admission-flow.svg](figures/public-artifact-admission-flow.svg).
