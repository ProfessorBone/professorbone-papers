import pytest

from appendix_a_full_orsr_loop_poc import (
    Outcome,
    SubstrateRuntime,
    TaskStatus,
    make_proposal,
)


def new_runtime():
    runtime = SubstrateRuntime()
    runtime.issue_initial_observation()
    return runtime


def test_valid_transition_binds():
    runtime = new_runtime()

    package = runtime.resolve(make_proposal(runtime, "proposal-001", "draft_created"))

    assert package.resolution.outcome == Outcome.BIND
    assert package.binding_record is not None
    assert package.resolution.binding_record_id == package.binding_record.binding_record_id
    assert runtime.ledger.current_state == "draft_created"
    assert package.continuation_state.prior_resolution_ref == package.resolution.resolution_id


def test_hold_issues_restricted_continuation():
    runtime = new_runtime()

    package = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-001",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )

    assert package.resolution.outcome == Outcome.HOLD
    assert package.hold_record is not None
    assert runtime.ledger.current_state == "initial"
    assert runtime.ledger.status == TaskStatus.BLOCKED
    assert package.allowed_next_affordance_set.affordances == [
        "revise_proposal",
        "request_authority_review",
    ]
    assert package.continuation_state.continuation_state_id == runtime.ledger.latest_continuation_state_id


def test_private_continuation_rejected():
    runtime = new_runtime()
    runtime.resolve(
        make_proposal(
            runtime,
            "proposal-001",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )

    package = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-002",
            "report_filed",
            claimed_authority="file_mandated_report",
            continuation_ref="private-continuation",
            prior_resolution_ref="private-resolution",
            cycle_id="cycle-private",
        )
    )

    assert package.resolution.outcome == Outcome.PRIVATE_CONTINUATION_REJECTED
    assert package.binding_record is None
    assert runtime.ledger.current_state == "initial"
    assert "substrate-issued" in package.resolution.reason


def test_unchanged_replay_rejected():
    runtime = new_runtime()
    runtime.resolve(
        make_proposal(
            runtime,
            "proposal-001",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )

    package = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-002",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )

    assert package.resolution.outcome == Outcome.REPLAY_REJECTED
    assert package.replay_record is not None
    assert package.replay_record.original_proposal_id == "proposal-001"
    assert "state_ref" in package.resolution.reason
    assert "authority_context_ref" in package.resolution.reason
    assert "domain_constitution_ref" in package.resolution.reason
    assert "provenance_frontier_ref" in package.resolution.reason


def test_changed_condition_allows_resubmission():
    runtime = new_runtime()
    runtime.resolve(
        make_proposal(
            runtime,
            "proposal-001",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )
    runtime.update_authority_context("file_mandated_report")

    package = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-002",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )

    assert package.resolution.outcome == Outcome.BIND
    assert package.replay_record is None
    assert package.binding_record is not None
    assert runtime.ledger.current_state == "report_filed"


def test_escalation_creates_pending_obligation():
    runtime = new_runtime()

    package = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-001",
            "sovereign_review_needed",
            claimed_authority="submit_for_review",
            risk_signal="sovereign_review_required",
        )
    )

    assert package.resolution.outcome == Outcome.ESCALATE
    assert package.pending_obligation is not None
    assert package.pending_obligation in runtime.ledger.pending_obligations
    assert runtime.ledger.status == TaskStatus.ESCALATED
    assert package.allowed_next_affordance_set.affordances == [
        "await_sovereign_review",
        "submit_clarifying_evidence",
    ]


def test_malformed_proposal_produces_nonformation():
    runtime = new_runtime()

    package = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-001",
            "draft_created",
            lineage_ref=None,
        )
    )

    assert package.resolution.outcome == Outcome.NON_FORMATION
    assert package.nonformation_receipt is not None
    assert package.resolution.nonformation_receipt_id == package.nonformation_receipt.nonformation_receipt_id
    assert package.nonformation_receipt in runtime.ledger.nonformation_receipts
    assert runtime.ledger.current_state == "initial"
    assert runtime.ledger.status == TaskStatus.BLOCKED
    assert package.continuation_state.continuation_state_id == runtime.ledger.latest_continuation_state_id
    assert package.allowed_next_affordance_set.affordances == ["repair_proposal_schema"]


def test_task_ledger_updated_after_every_resolution():
    runtime = new_runtime()
    packages = [
        runtime.resolve(make_proposal(runtime, "proposal-001", "draft_created")),
        runtime.resolve(
            make_proposal(
                runtime,
                "proposal-002",
                "report_filed",
                claimed_authority="file_mandated_report",
            )
        ),
        runtime.resolve(
            make_proposal(
                runtime,
                "proposal-003",
                "private_state",
                continuation_ref="private-continuation",
            )
        ),
    ]

    assert len(runtime.ledger.adjudications) == len(packages)
    assert runtime.ledger.latest_resolution_id == packages[-1].resolution.resolution_id
    assert all(record.resolution_id for record in runtime.ledger.adjudications)


def test_allowed_next_affordances_present_after_every_resolution():
    runtime = new_runtime()
    first = runtime.resolve(make_proposal(runtime, "proposal-001", "draft_created"))
    second = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-002",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )
    third = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-003",
            "sovereign_review_needed",
            claimed_authority="submit_for_review",
            risk_signal="sovereign_review_required",
        )
    )

    for package in [first, second, third]:
        assert package.allowed_next_affordance_set.affordances
        assert package.resolution.allowed_next_affordance_set_id == package.allowed_next_affordance_set.affordance_set_id
        assert package.continuation_state.allowed_next_affordance_set_id == package.allowed_next_affordance_set.affordance_set_id


def test_next_cycle_requires_latest_continuation_state():
    runtime = new_runtime()
    initial_continuation = runtime.ledger.latest_continuation_state_id
    first = runtime.resolve(make_proposal(runtime, "proposal-001", "draft_created"))

    assert first.continuation_state.continuation_state_id != initial_continuation
    with pytest.raises(ValueError, match="latest substrate-issued ContinuationState"):
        runtime.observe_from_continuation(initial_continuation)  # type: ignore[arg-type]

    observation = runtime.observe_from_continuation(first.continuation_state.continuation_state_id)
    assert observation.continuation_state_ref == first.continuation_state.continuation_state_id
    assert observation.prior_resolution_ref == first.resolution.resolution_id
