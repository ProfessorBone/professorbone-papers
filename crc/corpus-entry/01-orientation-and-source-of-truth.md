# Orientation and Source of Truth

**Artifact type:** Explanatory artifact
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.0
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.10 Appendix B and CRC-SSR v1.1
**Normative scope:** Explanation of public corpus entry practice only
**Does not:** Override Core, CRC-SSR, or any defining paper


The repository is the source of truth. Private coordination files can help a maintained local workspace, but every claim must be checked against live repository bytes, current git state, and the relevant public files.

## Maintained Project Workspace

Repository-writing agents operating in the maintained project workspace begin with this guide, then read `system-prompt.md` and `state.md` where those private files are available. They run read-only git checks before drafting or editing:

```bash
git status --short
git log --oneline -5
git branch --show-current
```

Read-only git inspection does not alter repository state. Staging, committing, and pushing are distinct governed actions, each requiring explicit authorization. Staging prepares an exact local change set, committing records it in repository history, and pushing publishes that history to the remote repository.

## Public Readers and External Contributors

Public readers and external contributors should treat the tracked repository as the complete public source. `system-prompt.md` and `state.md` are private local control files. Their absence from the public corpus does not make the public corpus incomplete and does not authorize reconstructing or inferring their contents.

## Source Priority

If summaries, handoffs, prompts, or private notes disagree with tracked files, the tracked files win. If tracked files appear inconsistent, report the inconsistency and route it through the admission or amendment workflow rather than silently resolving it.

## Entry Rule

After this guide is published, every repository-writing session in the maintained project workspace must begin by reading [README.md](README.md) and following this orientation sequence before drafting or editing.
