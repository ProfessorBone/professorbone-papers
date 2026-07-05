"""
Appendix A Full ORSR Continuation Loop POC.

This script is a minimal executable design trace showing that ORSR is a governed
continuation loop, not a one-shot Submit/Resolve handoff.

It demonstrates substrate-issued AgentObservation, typed TransitionProposal,
Resolve, BindingRecord / HoldRecord / NonFormationReceipt / replay rejection /
escalation handling, TaskLedger update, AllowedNextAffordanceSet issuance, and
ContinuationState issuance across chained cycles.

It is not a production runtime, a full CTLC implementation, a full AEGIS clinical
workflow, a MEC/L2 implementation, or empirical validation of the full CRC corpus.
It uses in-memory stubs for unresolved corpus dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple


# STUB: full DomainConstitution schema is not implemented in this POC.
# STUB: full authority graph is reduced to an in-memory authorization table.
# STUB: full provenance frontier is represented by a single pinned string.
# STUB: full RequiredAffordanceSet is represented by deterministic affordance lists.
# STUB: full audit store is represented by in-memory AdjudicationRecord objects.
# STUB: full L2/MEC trajectory audits are not implemented.
# STUB: full reconstitution grammar is represented by an authority-context update.
# STUB: effect-equivalence classes are not fully implemented here.
# This POC uses exact proposal signature comparison only for unchanged replay.


class Outcome(str, Enum):
    EMIT = "EMIT"  # Reserved for reachability-only traces; this POC binds favorable outcomes.
    HOLD = "HOLD"
    ESCALATE = "ESCALATE"
    NON_FORMATION = "NON_FORMATION"
    BIND = "BIND"
    REPLAY_REJECTED = "REPLAY_REJECTED"
    PRIVATE_CONTINUATION_REJECTED = "PRIVATE_CONTINUATION_REJECTED"


class TaskStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    BLOCKED = "BLOCKED"
    ESCALATED = "ESCALATED"
    COMPLETE = "COMPLETE"


@dataclass(frozen=True)
class TransitionProposal:
    proposal_id: str
    cycle_id: str
    task_id: str
    requesting_agent: str
    from_state: str
    to_state: str
    standing_class: str
    claimed_authority: str
    payload_type: str
    payload_summary: str
    continuation_state_ref: Optional[str]
    prior_resolution_ref: Optional[str]
    lineage_ref: Optional[str]
    risk_signal: str = "none"


@dataclass
class Resolution:
    resolution_id: str
    outcome: Outcome
    reason: str
    proposal_id: Optional[str]
    cycle_id: str
    task_id: str
    binding_record_id: Optional[str] = None
    hold_record_id: Optional[str] = None
    nonformation_receipt_id: Optional[str] = None
    replay_record_id: Optional[str] = None
    pending_obligation_id: Optional[str] = None
    continuation_state_id: Optional[str] = None
    allowed_next_affordance_set_id: Optional[str] = None


@dataclass
class HoldRecord:
    hold_record_id: str
    proposal_id: str
    failed_conjunct: str
    cause: str
    state_ref: str
    authority_context_ref: str
    domain_constitution_ref: str
    provenance_frontier_ref: str
    cycle_id: str


@dataclass
class BindingRecord:
    binding_record_id: str
    proposal_id: str
    from_state: str
    to_state: str
    resolution_id: str
    cycle_id: str


@dataclass
class NonFormationReceipt:
    nonformation_receipt_id: str
    proposal_id: Optional[str]
    failed_check: str
    cause: str
    cycle_id: str
    task_id: str


@dataclass
class PendingObligation:
    obligation_id: str
    task_id: str
    source_cycle_id: str
    source_event_type: str
    source_event_ref: str
    obligation_type: str
    status: str
    blocking_status: str


@dataclass
class AllowedNextAffordanceSet:
    affordance_set_id: str
    task_id: str
    cycle_id: str
    affordances: List[str]
    reason: str


@dataclass
class ContinuationState:
    continuation_state_id: str
    task_id: str
    cycle_id: str
    state_ref: str
    prior_resolution_ref: Optional[str]
    allowed_next_affordance_set_id: str
    authority_context_ref: str
    domain_constitution_ref: str
    provenance_frontier_ref: str


@dataclass
class AgentObservation:
    observation_id: str
    task_id: str
    cycle_id: str
    state_ref: str
    continuation_state_ref: str
    prior_resolution_ref: Optional[str]
    allowed_next_affordances: List[str]


@dataclass
class ReplayAdmissibilityRecord:
    replay_record_id: str
    proposal_id: str
    original_proposal_id: str
    state_ref: str
    authority_context_ref: str
    domain_constitution_ref: str
    provenance_frontier_ref: str
    reason: str


@dataclass
class AdjudicationRecord:
    adjudication_record_id: str
    proposal_id: Optional[str]
    resolution_id: str
    outcome: Outcome
    reason: str
    cycle_id: str
    task_id: str


@dataclass
class TaskLedger:
    task_id: str
    status: TaskStatus
    current_state: str
    current_cycle_id: str
    latest_continuation_state_id: Optional[str] = None
    latest_resolution_id: Optional[str] = None
    pending_obligations: List[PendingObligation] = field(default_factory=list)
    adjudications: List[AdjudicationRecord] = field(default_factory=list)
    binding_records: List[BindingRecord] = field(default_factory=list)
    hold_records: List[HoldRecord] = field(default_factory=list)
    nonformation_receipts: List[NonFormationReceipt] = field(default_factory=list)
    replay_records: List[ReplayAdmissibilityRecord] = field(default_factory=list)


@dataclass
class ResolutionPackage:
    resolution: Resolution
    task_ledger: TaskLedger
    allowed_next_affordance_set: AllowedNextAffordanceSet
    continuation_state: ContinuationState
    binding_record: Optional[BindingRecord] = None
    hold_record: Optional[HoldRecord] = None
    nonformation_receipt: Optional[NonFormationReceipt] = None
    replay_record: Optional[ReplayAdmissibilityRecord] = None
    pending_obligation: Optional[PendingObligation] = None


class SubstrateRuntime:
    def __init__(self, task_id: str = "task-001") -> None:
        self.task_id = task_id
        self.ledger = TaskLedger(
            task_id=task_id,
            status=TaskStatus.NOT_STARTED,
            current_state="initial",
            current_cycle_id="cycle-001",
        )
        self._counters: Dict[str, int] = {"authctx": 1}
        self.allowed_authorities: Dict[Tuple[str, str], set[str]] = {
            ("mantis", "clinical_reasoner"): {"draft_note", "submit_for_review"}
        }
        self.authority_context_ref = "authctx-001"
        self.domain_constitution_ref = "domain-constitution-001"
        self.provenance_frontier_ref = "prov-frontier-001"
        self.continuation_states: Dict[str, ContinuationState] = {}
        self.affordance_sets: Dict[str, AllowedNextAffordanceSet] = {}
        self._proposal_context_by_signature: Dict[
            Tuple[str, str, str, str, str, str, str, str], Tuple[str, Tuple[str, str, str, str]]
        ] = {}

    def _id(self, prefix: str) -> str:
        self._counters[prefix] = self._counters.get(prefix, 0) + 1
        return f"{prefix}-{self._counters[prefix]:03d}"

    def issue_initial_observation(self) -> AgentObservation:
        affordances = self._create_affordances(
            cycle_id=self.ledger.current_cycle_id,
            affordances=["draft_note", "submit_for_review"],
            reason="initial substrate-issued affordance set",
        )
        continuation = self._create_continuation(
            cycle_id=self.ledger.current_cycle_id,
            state_ref=self.ledger.current_state,
            prior_resolution_ref=None,
            allowed_next_affordance_set_id=affordances.affordance_set_id,
        )
        self.ledger.status = TaskStatus.IN_PROGRESS
        return AgentObservation(
            observation_id=self._id("obs"),
            task_id=self.task_id,
            cycle_id=continuation.cycle_id,
            state_ref=continuation.state_ref,
            continuation_state_ref=continuation.continuation_state_id,
            prior_resolution_ref=continuation.prior_resolution_ref,
            allowed_next_affordances=list(affordances.affordances),
        )

    def observe_from_continuation(self, continuation_state_id: str) -> AgentObservation:
        continuation = self.continuation_states.get(continuation_state_id)
        if continuation is None or continuation_state_id != self.ledger.latest_continuation_state_id:
            raise ValueError("next observe requires latest substrate-issued ContinuationState")
        affordances = self.affordance_sets[continuation.allowed_next_affordance_set_id]
        return AgentObservation(
            observation_id=self._id("obs"),
            task_id=continuation.task_id,
            cycle_id=continuation.cycle_id,
            state_ref=continuation.state_ref,
            continuation_state_ref=continuation.continuation_state_id,
            prior_resolution_ref=continuation.prior_resolution_ref,
            allowed_next_affordances=list(affordances.affordances),
        )

    def update_authority_context(self, authority: str, agent: str = "mantis", standing_class: str = "clinical_reasoner") -> None:
        self.allowed_authorities.setdefault((agent, standing_class), set()).add(authority)
        self.authority_context_ref = self._id("authctx")

    def resolve(self, proposal: TransitionProposal) -> ResolutionPackage:
        if not self._proposal_has_required_fields(proposal):
            return self._nonformation(proposal, "ProposalWellFormed", "missing required proposal references")

        continuation = self.continuation_states.get(proposal.continuation_state_ref or "")
        if continuation is None or proposal.continuation_state_ref != self.ledger.latest_continuation_state_id:
            return self._private_continuation_rejected(
                proposal,
                "proposal continuation must reference latest substrate-issued state",
            )

        if proposal.cycle_id != continuation.cycle_id or proposal.prior_resolution_ref != continuation.prior_resolution_ref:
            return self._private_continuation_rejected(
                proposal,
                "proposal cycle/prior resolution do not match substrate-issued ContinuationState",
            )

        replay_context = self._pinned_context()
        signature = self._proposal_signature(proposal)
        previous = self._proposal_context_by_signature.get(signature)
        if previous and previous[1] == replay_context:
            return self._replay_rejected(proposal, previous[0], replay_context)

        if not self._is_authorized(proposal):
            package = self._hold(proposal, "Authorized", "standing class or claimed authority does not authorize transition")
            self._proposal_context_by_signature[signature] = (proposal.proposal_id, replay_context)
            return package

        if proposal.risk_signal == "sovereign_review_required":
            package = self._escalate(proposal, "risk signal requires sovereign review")
            self._proposal_context_by_signature[signature] = (proposal.proposal_id, replay_context)
            return package

        package = self._bind(proposal)
        self._proposal_context_by_signature[signature] = (proposal.proposal_id, replay_context)
        return package

    def _proposal_has_required_fields(self, proposal: TransitionProposal) -> bool:
        required = [
            proposal.proposal_id,
            proposal.cycle_id,
            proposal.task_id,
            proposal.requesting_agent,
            proposal.from_state,
            proposal.to_state,
            proposal.standing_class,
            proposal.claimed_authority,
            proposal.payload_type,
            proposal.payload_summary,
            proposal.continuation_state_ref,
            proposal.lineage_ref,
        ]
        return all(required) and proposal.task_id == self.task_id

    def _is_authorized(self, proposal: TransitionProposal) -> bool:
        return proposal.claimed_authority in self.allowed_authorities.get(
            (proposal.requesting_agent, proposal.standing_class),
            set(),
        )

    def _proposal_signature(self, proposal: TransitionProposal) -> Tuple[str, str, str, str, str, str, str, str]:
        return (
            proposal.requesting_agent,
            proposal.from_state,
            proposal.to_state,
            proposal.standing_class,
            proposal.claimed_authority,
            proposal.payload_type,
            proposal.payload_summary,
            proposal.risk_signal,
        )

    def _pinned_context(self) -> Tuple[str, str, str, str]:
        return (
            self.ledger.current_state,
            self.authority_context_ref,
            self.domain_constitution_ref,
            self.provenance_frontier_ref,
        )

    def _next_cycle_id(self) -> str:
        current = int(self.ledger.current_cycle_id.split("-")[1])
        return f"cycle-{current + 1:03d}"

    def _create_affordances(self, cycle_id: str, affordances: List[str], reason: str) -> AllowedNextAffordanceSet:
        allowed = AllowedNextAffordanceSet(
            affordance_set_id=self._id("aff"),
            task_id=self.task_id,
            cycle_id=cycle_id,
            affordances=affordances,
            reason=reason,
        )
        self.affordance_sets[allowed.affordance_set_id] = allowed
        return allowed

    def _create_continuation(
        self,
        cycle_id: str,
        state_ref: str,
        prior_resolution_ref: Optional[str],
        allowed_next_affordance_set_id: str,
    ) -> ContinuationState:
        continuation = ContinuationState(
            continuation_state_id=self._id("cont"),
            task_id=self.task_id,
            cycle_id=cycle_id,
            state_ref=state_ref,
            prior_resolution_ref=prior_resolution_ref,
            allowed_next_affordance_set_id=allowed_next_affordance_set_id,
            authority_context_ref=self.authority_context_ref,
            domain_constitution_ref=self.domain_constitution_ref,
            provenance_frontier_ref=self.provenance_frontier_ref,
        )
        self.continuation_states[continuation.continuation_state_id] = continuation
        self.ledger.latest_continuation_state_id = continuation.continuation_state_id
        self.ledger.current_cycle_id = continuation.cycle_id
        return continuation

    def _finalize(
        self,
        resolution: Resolution,
        affordances: List[str],
        affordance_reason: str,
        status: TaskStatus,
        binding_record: Optional[BindingRecord] = None,
        hold_record: Optional[HoldRecord] = None,
        nonformation_receipt: Optional[NonFormationReceipt] = None,
        replay_record: Optional[ReplayAdmissibilityRecord] = None,
        pending_obligation: Optional[PendingObligation] = None,
    ) -> ResolutionPackage:
        next_cycle_id = self._next_cycle_id()
        allowed = self._create_affordances(next_cycle_id, affordances, affordance_reason)
        continuation = self._create_continuation(
            cycle_id=next_cycle_id,
            state_ref=self.ledger.current_state,
            prior_resolution_ref=resolution.resolution_id,
            allowed_next_affordance_set_id=allowed.affordance_set_id,
        )
        resolution.continuation_state_id = continuation.continuation_state_id
        resolution.allowed_next_affordance_set_id = allowed.affordance_set_id
        self.ledger.status = status
        self.ledger.latest_resolution_id = resolution.resolution_id
        self.ledger.adjudications.append(
            AdjudicationRecord(
                adjudication_record_id=self._id("adj"),
                proposal_id=resolution.proposal_id,
                resolution_id=resolution.resolution_id,
                outcome=resolution.outcome,
                reason=resolution.reason,
                cycle_id=resolution.cycle_id,
                task_id=resolution.task_id,
            )
        )
        return ResolutionPackage(
            resolution=resolution,
            task_ledger=self.ledger,
            allowed_next_affordance_set=allowed,
            continuation_state=continuation,
            binding_record=binding_record,
            hold_record=hold_record,
            nonformation_receipt=nonformation_receipt,
            replay_record=replay_record,
            pending_obligation=pending_obligation,
        )

    def _bind(self, proposal: TransitionProposal) -> ResolutionPackage:
        resolution = Resolution(
            resolution_id=self._id("res"),
            outcome=Outcome.BIND,
            reason="proposal reachable; BindingRecord formed before state update",
            proposal_id=proposal.proposal_id,
            cycle_id=proposal.cycle_id,
            task_id=proposal.task_id,
        )
        binding = BindingRecord(
            binding_record_id=self._id("bind"),
            proposal_id=proposal.proposal_id,
            from_state=proposal.from_state,
            to_state=proposal.to_state,
            resolution_id=resolution.resolution_id,
            cycle_id=proposal.cycle_id,
        )
        resolution.binding_record_id = binding.binding_record_id
        self.ledger.binding_records.append(binding)
        self.ledger.current_state = proposal.to_state
        return self._finalize(
            resolution,
            affordances=["draft_note", "submit_for_review"],
            affordance_reason="binding formed; ordinary next proposals allowed",
            status=TaskStatus.IN_PROGRESS,
            binding_record=binding,
        )

    def _hold(self, proposal: TransitionProposal, failed_conjunct: str, cause: str) -> ResolutionPackage:
        resolution = Resolution(
            resolution_id=self._id("res"),
            outcome=Outcome.HOLD,
            reason=cause,
            proposal_id=proposal.proposal_id,
            cycle_id=proposal.cycle_id,
            task_id=proposal.task_id,
        )
        hold = HoldRecord(
            hold_record_id=self._id("hold"),
            proposal_id=proposal.proposal_id,
            failed_conjunct=failed_conjunct,
            cause=cause,
            state_ref=self.ledger.current_state,
            authority_context_ref=self.authority_context_ref,
            domain_constitution_ref=self.domain_constitution_ref,
            provenance_frontier_ref=self.provenance_frontier_ref,
            cycle_id=proposal.cycle_id,
        )
        resolution.hold_record_id = hold.hold_record_id
        self.ledger.hold_records.append(hold)
        return self._finalize(
            resolution,
            affordances=["revise_proposal", "request_authority_review"],
            affordance_reason="hold restricts continuation to repair or review",
            status=TaskStatus.BLOCKED,
            hold_record=hold,
        )

    def _escalate(self, proposal: TransitionProposal, reason: str) -> ResolutionPackage:
        resolution = Resolution(
            resolution_id=self._id("res"),
            outcome=Outcome.ESCALATE,
            reason=reason,
            proposal_id=proposal.proposal_id,
            cycle_id=proposal.cycle_id,
            task_id=proposal.task_id,
        )
        obligation = PendingObligation(
            obligation_id=self._id("obl"),
            task_id=proposal.task_id,
            source_cycle_id=proposal.cycle_id,
            source_event_type="Escalate",
            source_event_ref=resolution.resolution_id,
            obligation_type="awaiting_sovereign_review",
            status="OPEN",
            blocking_status="continuation",
        )
        resolution.pending_obligation_id = obligation.obligation_id
        self.ledger.pending_obligations.append(obligation)
        return self._finalize(
            resolution,
            affordances=["await_sovereign_review", "submit_clarifying_evidence"],
            affordance_reason="escalation restricts continuation to review-compatible actions",
            status=TaskStatus.ESCALATED,
            pending_obligation=obligation,
        )

    def _nonformation(self, proposal: TransitionProposal, failed_check: str, cause: str) -> ResolutionPackage:
        cycle_id = proposal.cycle_id or self.ledger.current_cycle_id
        resolution = Resolution(
            resolution_id=self._id("res"),
            outcome=Outcome.NON_FORMATION,
            reason=cause,
            proposal_id=proposal.proposal_id,
            cycle_id=cycle_id,
            task_id=proposal.task_id or self.task_id,
        )
        receipt = NonFormationReceipt(
            nonformation_receipt_id=self._id("nf"),
            proposal_id=proposal.proposal_id,
            failed_check=failed_check,
            cause=cause,
            cycle_id=cycle_id,
            task_id=proposal.task_id or self.task_id,
        )
        resolution.nonformation_receipt_id = receipt.nonformation_receipt_id
        self.ledger.nonformation_receipts.append(receipt)
        return self._finalize(
            resolution,
            affordances=["repair_proposal_schema"],
            affordance_reason="non-formation permits only schema repair",
            status=TaskStatus.BLOCKED,
            nonformation_receipt=receipt,
        )

    def _private_continuation_rejected(self, proposal: TransitionProposal, reason: str) -> ResolutionPackage:
        resolution = Resolution(
            resolution_id=self._id("res"),
            outcome=Outcome.PRIVATE_CONTINUATION_REJECTED,
            reason=reason,
            proposal_id=proposal.proposal_id,
            cycle_id=proposal.cycle_id or self.ledger.current_cycle_id,
            task_id=proposal.task_id or self.task_id,
        )
        return self._finalize(
            resolution,
            affordances=["use_latest_substrate_continuation"],
            affordance_reason="private continuation is rejected; substrate state remains authoritative",
            status=TaskStatus.BLOCKED,
        )

    def _replay_rejected(
        self,
        proposal: TransitionProposal,
        original_proposal_id: str,
        context: Tuple[str, str, str, str],
    ) -> ResolutionPackage:
        state_ref, authority_context_ref, domain_constitution_ref, provenance_frontier_ref = context
        reason = (
            "unchanged replay rejected: state_ref, authority_context_ref, "
            "domain_constitution_ref, and provenance_frontier_ref are unchanged"
        )
        resolution = Resolution(
            resolution_id=self._id("res"),
            outcome=Outcome.REPLAY_REJECTED,
            reason=reason,
            proposal_id=proposal.proposal_id,
            cycle_id=proposal.cycle_id,
            task_id=proposal.task_id,
        )
        replay = ReplayAdmissibilityRecord(
            replay_record_id=self._id("replay"),
            proposal_id=proposal.proposal_id,
            original_proposal_id=original_proposal_id,
            state_ref=state_ref,
            authority_context_ref=authority_context_ref,
            domain_constitution_ref=domain_constitution_ref,
            provenance_frontier_ref=provenance_frontier_ref,
            reason=reason,
        )
        resolution.replay_record_id = replay.replay_record_id
        self.ledger.replay_records.append(replay)
        return self._finalize(
            resolution,
            affordances=["change_context_or_revise_proposal", "request_authority_review"],
            affordance_reason="unchanged replay rejected; only changed context or revision may proceed",
            status=TaskStatus.BLOCKED,
            replay_record=replay,
        )


def make_proposal(
    runtime: SubstrateRuntime,
    proposal_id: str,
    to_state: str,
    claimed_authority: str = "draft_note",
    risk_signal: str = "none",
    continuation_ref: Optional[str] = None,
    prior_resolution_ref: Optional[str] = None,
    cycle_id: Optional[str] = None,
    lineage_ref: Optional[str] = "lineage-001",
    from_state: Optional[str] = None,
) -> TransitionProposal:
    continuation = runtime.continuation_states[runtime.ledger.latest_continuation_state_id]  # type: ignore[index]
    return TransitionProposal(
        proposal_id=proposal_id,
        cycle_id=cycle_id or continuation.cycle_id,
        task_id=runtime.task_id,
        requesting_agent="mantis",
        from_state=from_state or runtime.ledger.current_state,
        to_state=to_state,
        standing_class="clinical_reasoner",
        claimed_authority=claimed_authority,
        payload_type="state_transition",
        payload_summary=f"move to {to_state}",
        continuation_state_ref=continuation_ref if continuation_ref is not None else continuation.continuation_state_id,
        prior_resolution_ref=prior_resolution_ref if prior_resolution_ref is not None else continuation.prior_resolution_ref,
        lineage_ref=lineage_ref,
        risk_signal=risk_signal,
    )


def print_trace(name: str, package: ResolutionPackage) -> None:
    resolution = package.resolution
    print(f"\n{name}")
    print(f"  cycle_id: {resolution.cycle_id}")
    print(f"  proposal_id: {resolution.proposal_id}")
    print(f"  outcome: {resolution.outcome.value}")
    print(f"  reason: {resolution.reason}")
    print(f"  task_id: {resolution.task_id}")
    print(f"  task_status: {package.task_ledger.status.value}")
    print(f"  pending_obligations: {[o.obligation_id for o in package.task_ledger.pending_obligations]}")
    print(f"  allowed_next_affordances: {package.allowed_next_affordance_set.affordances}")
    print(f"  continuation_state_id: {package.continuation_state.continuation_state_id}")
    print(f"  prior_resolution_ref: {package.continuation_state.prior_resolution_ref}")
    print(f"  binding_record_id: {resolution.binding_record_id}")
    print(f"  hold_record_id: {resolution.hold_record_id}")
    print(f"  nonformation_receipt_id: {resolution.nonformation_receipt_id}")
    print(f"  replay_record_id: {resolution.replay_record_id}")


def run_demo() -> None:
    runtime = SubstrateRuntime()
    initial = runtime.issue_initial_observation()
    print("Initial substrate-issued AgentObservation")
    print(f"  observation_id: {initial.observation_id}")
    print(f"  cycle_id: {initial.cycle_id}")
    print(f"  continuation_state_ref: {initial.continuation_state_ref}")
    print(f"  allowed_next_affordances: {initial.allowed_next_affordances}")

    valid = runtime.resolve(make_proposal(runtime, "proposal-001", "draft_created"))
    print_trace("Scenario 1: Valid transition binds", valid)

    unauthorized = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-002",
            "report_filed",
            claimed_authority="file_mandated_report",
        )
    )
    print_trace("Scenario 2: Invalid transition Holds", unauthorized)

    private = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-003",
            "report_filed",
            claimed_authority="file_mandated_report",
            continuation_ref="private-continuation-ref",
            prior_resolution_ref="private-resolution-ref",
            cycle_id="cycle-private",
        )
    )
    print_trace("Scenario 3: Private continuation blocked", private)

    replay = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-004",
            "report_filed",
            claimed_authority="file_mandated_report",
            from_state="draft_created",
        )
    )
    print_trace("Scenario 4: Unchanged replay blocked", replay)

    runtime.update_authority_context("file_mandated_report")
    changed = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-005",
            "report_filed",
            claimed_authority="file_mandated_report",
            from_state="draft_created",
        )
    )
    print_trace("Scenario 5: Changed condition allows new proposal", changed)

    escalation = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-006",
            "sovereign_review_needed",
            claimed_authority="submit_for_review",
            risk_signal="sovereign_review_required",
        )
    )
    print_trace("Scenario 6: Escalation creates pending obligation", escalation)

    malformed = runtime.resolve(
        make_proposal(
            runtime,
            "proposal-007",
            "note_finalized",
            claimed_authority="draft_note",
            lineage_ref=None,
        )
    )
    print_trace("Scenario 7: Malformed proposal produces NonFormationReceipt", malformed)

    next_observation = runtime.observe_from_continuation(malformed.continuation_state.continuation_state_id)
    print("\nNext Observe from substrate-issued ContinuationState")
    print(f"  observation_id: {next_observation.observation_id}")
    print(f"  cycle_id: {next_observation.cycle_id}")
    print(f"  continuation_state_ref: {next_observation.continuation_state_ref}")
    print(f"  prior_resolution_ref: {next_observation.prior_resolution_ref}")
    print(f"  allowed_next_affordances: {next_observation.allowed_next_affordances}")


if __name__ == "__main__":
    run_demo()
