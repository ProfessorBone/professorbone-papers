# Publication Checklist Template

**Artifact type:** Operational template
**Identifier:** CRC-CORPUS-ENTRY
**Version:** v1.1
**Status:** Current
**Ratifying authority:** Faheem Downs
**Ratification state:** Ratified by Faheem Downs on 2026-07-12
**Governance context:** Constitutional Runtime Computation v5.12 Appendix B, CRC-SSR v1.4, and CRC-OAR v1.0
**Normative scope:** Work standardization only
**Does not:** Settle substantive doctrine or override governing artifacts

## 1. Pre-Apply Review

- declaration_reviewed: [yes or no]
- package_ratified: [yes or no]
- apply_scope_authorized: [yes or no]
- open_architecture_dependencies_field_present: [yes or no]
- open_architecture_dependencies_none_explicit_if_no_oar_dependency: [yes or no]
- every_oar_id_resolves: [yes, no, or not applicable]
- relationship_values_valid: [yes, no, or not applicable]
- materiality_values_valid: [yes, no, or not applicable]
- every_blocking_dependency_stopped_publication: [yes, no, or not applicable]
- every_non_blocking_dependency_passed_materiality_test: [yes, no, or not applicable]
- informational_dependencies_confer_no_authority: [yes, no, or not applicable]
- no_raw_wikilink_used_as_canonical_citation: [yes or no]
- no_oar_entry_represented_as_canonical_or_implementation_permission: [yes or no]
- crc_ssr_treatment_evaluated_separately: [yes or no]

## 2. Unstaged Apply Review

- changed_file_set_confirmed: [yes or no]
- `git diff --stat`: [result]
- `git diff --check`: [result]
- full_unstaged_diff_reviewed: [yes or no]
- no_unrelated_files_changed: [yes or no]

## 3. Staging Authorization

- staging_authorized_by: [name]
- exact_paths_authorized: [paths]

## 4. Staged Review

- exact_paths_staged: [paths]
- no_broad_staging_used: [yes or no]
- `git diff --cached --stat`: [result]
- `git diff --cached --check`: [result]
- full_staged_diff_reviewed: [yes or no]
- staged_set_matches_authorization: [yes or no]

## 5. Commit Authorization and Execution

- commit_authorized_by: [name]
- commit_performed: [yes or no]
- commit_identifier: [hash]

## 6. Push Authorization and Execution

- push_authorized_by: [name]
- push_performed: [yes or no]
- origin_alignment_verified: [yes or no]

## 7. Maintained-Workspace State Update

- state_md_updated_after_publication_where_applicable: [yes or no]
