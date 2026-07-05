# Constitutional Boundary Contracts: Governed Interface Exchange at the Agent-Substrate Boundary

## Why Boundary Crossings Are Constitutional Events

### Companion 0 to Constitutional Runtime Computation v5.5
### Foundational interface companion to the ORSR architecture

**Clarence "Faheem" Downs (Professor Bone Lab)**

*Licensed under CC BY 4.0.*

*No em dashes appear in this document. Hyphens, commas, and sentence breaks are used throughout.*

---

## Abstract

The Constitutional Runtime Computation paper reconstructs the agentic loop into Observe-Reason-Submit-Resolve, relocating execution authority from the agent into the Constitutional Runtime Substrate. The agent proposes. The substrate resolves. This architecture produces two primary governed boundaries in the core agent-substrate loop: the Agent-to-Substrate boundary, across which the agent's TransitionProposal must cross to enter adjudication, and the Substrate-to-Agent boundary, across which the substrate's AgentObservation must cross to initiate the next cycle. The parent paper governs what happens inside the substrate (CTLC, L1/L2 separation, verdict composition) and what the agent may propose (reachability predicates). It does not govern the boundaries themselves.

This paper argues that boundaries are not passive conduits. A boundary crossing is a constitutional event. The content, structure, provenance, and authority basis of what crosses determines whether the governed loop retains its constitutional integrity or whether the boundary becomes a surface through which constitutional consequence can be produced without adjudication. We state this as the Boundary Sovereignty Principle: any component that unilaterally determines what crosses a governed boundary, or how it crosses, holds causal authority over constitutional outcomes at the receiving side, which under ORSR no component may hold without substrate adjudication.

The contribution is sixfold. First, the Boundary Sovereignty Principle and its derivation from the parent's authority-migration logic. Second, a formal classification of boundary violation severity into six classes (B0 through B5), providing a consistent vocabulary for boundary failures across the corpus. Third, two typed boundary contracts, ProposalContract governing the Agent-to-Substrate boundary and ObservationContract governing the Substrate-to-Agent boundary, each with a formal schema, a validation predicate, a typed violation taxonomy, an audit record requirement, and an escalation rule. Fourth, the BoundaryValidationFunction as a constitutionally separated substrate component, distinct from the observation generator, with its own audit record and L2 monitoring obligation. Fifth, a family of boundary-specific primitive failure topologies (P_bnd), with P_bnd5 (observation packaging narrowing) traced end-to-end as the boundary-specific instance of systematic output compression. Sixth, the closure of the governed loop at the interface layer, completing what the memory companion closed on the write side and what the retrieval companion closed on the construction side. AEGIS serves as the worked domain throughout. Nafisah remains the sovereign principal. Mantis remains the clinical reasoning agent. MEC remains the L2 monitor.

---

## Contents

**Part I**   The unresolved boundary surface and the Boundary Sovereignty Principle
**Part II**  What a boundary contract is and why the ORSR architecture requires two
**Part III** Violation severity classification
**Part IV**  ProposalContract: the Agent-to-Substrate boundary
**Part V**   ObservationContract: the Substrate-to-Agent boundary
**Part VI**  The BoundaryValidationFunction and substrate self-validation
**Part VII** The boundary audit record and tamper-evidence requirements
**Part VIII** Primitive failure topologies specific to boundary exchange (P_bnd)
**Part IX**  Worked example: a complete ORSR cycle in AEGIS under boundary governance
**Part X**   Who governs the boundaries?
**Part XI**  Relationship to the companion series
**Part XII** Related work
**Open problems**

---

# Part I. The Unresolved Boundary Surface and the Boundary Sovereignty Principle

## I.1 The parent paper's relocation and what it leaves ungoverned

The parent paper's central act is a migration of authority. In the traditional Observe-Reason-Act loop, the agent holds terminal authority over Act. The Constitutional Runtime Architecture reconstructs that loop into ORSR, removing Act from the agent and relocating execution authority into the substrate. The agent proposes. The substrate resolves. This relocation is the parent paper's primary contribution.

The relocation produces a boundary as a necessary structural consequence. If the agent proposes and the substrate resolves, there must be a crossing: the proposal must leave the agent and enter the substrate for adjudication. And after adjudication, the substrate must issue context to the agent to initiate the next cycle. Two crossings. Two boundaries in the core agent-substrate loop.

The parent paper governs what the substrate does with a proposal once it has it (CTLC, verdict composition, L1/L2 separation). It governs what the agent may propose (reachability predicates). What it does not govern is the crossing itself, the moment at which the proposal leaves the agent's domain and enters the substrate's, and the moment at which the observation leaves the substrate's domain and enters the agent's.

Other governed crossings exist in the broader corpus: memory store to substrate, substrate to memory store, retrieval view into Observe, tool output into substrate, sovereign instruction into substrate, L2 monitor signal into substrate or sovereign review, evidence packet to sovereign, baseline and generation lineage to sovereign. These are outside this paper's scope. This paper governs the two primary boundaries in the core ORSR agent-substrate loop. Future work may extend the contract framework to the remaining crossing surfaces.

## I.2 Why the crossing matters constitutionally

A boundary crossing is not a passive transport event. The content, structure, provenance, and authority basis of what crosses determines what the receiving side works with. A proposal that arrives at CTLC without required provenance references cannot be correctly adjudicated, but without a contract the substrate may adjudicate it anyway, on a deficient basis, producing a verdict that appears valid while being constitutionally compromised. An observation that arrives at the agent carrying prior-cycle ephemeral state gives the agent material it should not have, but without a contract the agent receives it and reasons from it, and no downstream check detects the contamination.

The boundary is where constitutional integrity can be silently violated. The parent's reachability predicates govern the inside of the substrate. The memory companion governs the memory store. The retrieval companion governs view construction. None of them govern the crossing. Governing the crossing is the boundary contract's function.

## I.3 The Boundary Sovereignty Principle

**The Boundary Sovereignty Principle.** Any component that unilaterally determines what crosses a governed boundary, or how it crosses, holds causal authority over constitutional outcomes at the receiving side. Under ORSR, no component may hold unilateral causal authority over a constitutional outcome without substrate adjudication. Therefore boundary crossings must be governed by typed contracts, validated against those contracts before the crossing completes, with violations treated as constitutional events rather than transport errors.

**Corollary (two-boundary necessity).** The core ORSR agent-substrate loop produces two primary governed boundaries: Agent-to-Substrate (proposal crosses) and Substrate-to-Agent (observation crosses). A governed ORSR system requires both contracts. A system with one contract and not the other has one governed boundary and one ungoverned one. A proposal contract without an observation contract means the substrate can issue malformed, stale, or out-of-scope observations without detection. An observation contract without a proposal contract means the agent can submit structurally deficient proposals that CTLC must adjudicate on a deficient basis.

**Corollary (not informal message passing).** Agent-substrate interaction under ORSR is not informal message passing. It is a governed boundary exchange. Every crossing must conform to a typed contract and produce an auditable validation result. A system that treats the proposal as an informal prompt and the observation as an informal context window has not implemented ORSR. It has implemented an informal agent loop with ORSR vocabulary.

---

# Part II. What a Boundary Contract Is and Why ORSR Requires Two

## II.1 The contract defined

A boundary contract is a formal typed specification of what may cross a governed boundary, in what form, with what provenance, under what authority, producing what audit record. It has six components:

**Schema.** The typed structure of the crossing object. Every required field named, typed, and semantically defined. Optional fields distinguished from required fields. The schema carries a contract version reference so that every crossing object is validated against a pinned contract version and the audit record can reproduce which version applied.

**Validation predicate.** The formal check that determines whether a crossing object conforms to the schema and satisfies all structural, provenance, and authority constraints before the crossing completes.

**Violation typology.** An enumeration of the ways a crossing object can fail validation, each violation typed, named, and assigned to a severity class. Violations are not uniform: some are structural deficiencies (missing field), some are authority violations (agent claims authority it does not hold), and some are constitutional integrity events (state chain broken, cycle boundary violated) that require immediate sovereign escalation.

**Audit record.** The tamper-evident record that every crossing produces, conforming or not. The audit record is written before the crossing completes or the violation is escalated. It is the constitutional evidence that the governed exchange occurred.

**Escalation rule.** The specification of what happens when a violation is detected, determined by the violation's severity class. The escalation rule is part of the contract, not an afterthought.

**Completeness invariant.** No crossing occurs without contract validation. No validation occurs without an audit record. The contract is not advisory. It is the gate.

## II.2 Why ORSR requires exactly two in the core loop

The ORSR loop has two directions of crossing in the core agent-substrate interaction:

**Agent-to-Substrate.** The agent's TransitionProposal crosses into CTLC for adjudication. This is the governed proposal boundary. ProposalContract governs it.

**Substrate-to-Agent.** The substrate's AgentObservation crosses into the agent's Working Memory to initiate the next cycle. This is the governed observation boundary. ObservationContract governs it.

The Resolution, the substrate's internal adjudication object, does not itself cross a boundary. It is produced inside the substrate by Resolve and consumed inside the substrate. When continuation is authorized, the substrate issues a ContinuationState from the Resolution, and constructs the AgentObservation from that ContinuationState. It is that AgentObservation, not the Resolution, that crosses the Substrate-to-Agent boundary under ObservationContract. The Resolution is an internal substrate act; the AgentObservation is the governed crossing event issued from substrate-owned continuation state.

## II.3 The relationship to the reachability predicates

The boundary contracts and the reachability predicates (CTLC, MemoryOperationReachable, ObserveConstructionReachable) are not the same kind of object and must not be conflated.

The reachability predicates govern whether a proposed transition or memory operation is constitutionally permissible given current substrate state. They answer: may this happen?

The boundary contracts govern whether a crossing object conforms to the typed contract required for the crossing to be valid. They answer: did this cross correctly?

A proposal can be crossing-valid (conforming to ProposalContract) and constitutionally unreachable (failing CTLC). It crosses correctly and gets rejected inside the substrate. A proposal can also be crossing-invalid (failing ProposalContract) and would have been constitutionally reachable if submitted correctly. It fails at the boundary, before CTLC sees it. The two predicates operate at different layers and both are required.

---

# Part III. Violation Severity Classification

Before specifying the contracts, the violation severity taxonomy must be established. Every violation type in both contracts maps to one of six severity classes. The class determines the escalation rule. This taxonomy prevents ad hoc escalation decisions and allows later papers to reason about boundary failures consistently.

**B0: Structural Deficiency.** The crossing object is missing a required field, carries a null where a value is required, or fails schema completeness in a way that prevents the validation predicate from evaluating. The object is interpretable as to its type but incomplete. Escalation: logged to audit store, reported at next scheduled review unless the task is time-sensitive.

**B1: Provenance or Version Deficiency.** The crossing object is structurally complete but fails a provenance, lineage, or contract version check. This includes evidence cited without provenance chain reference, observation components lacking source references, lineage not reconstructable, and contract version anomalies. Contract version anomalies are further graded:

- Unknown contract version: the contract_version field references a version the BVF cannot resolve. Treat as B1 pending resolution.
- Compatible stale contract version: the version is known, no longer current, but within an active compatibility window under the reconstitution governance policy. Treat as B1 with logged advisory.
- Scheduled-successor contract version: the version is known but not yet active. Reject as B1 until the version's effective date.
- Expired contract version: the version is known but its compatibility window has closed. Outside the compatibility window, an expired version indicates use beyond permitted bounds. Treat as B3 (cycle or state integrity violation).
- Revoked contract version: the version has been explicitly withdrawn. Use of a revoked version may indicate stale-state submission or a downgrade attempt. Treat as B3 or B4 depending on context: B3 if stale-state is the plausible explanation, B4 if the crossing object shows other authority integrity indicators.

Escalation for B1: logged to audit store, object held, sovereign notified at next review interval unless the deficiency prevents a reachability predicate evaluation, in which case the object is held immediately.

**B2: Scope or Affordance Violation.** The crossing object proposes a capability not in the allowed affordance set, includes an affordance the substrate cannot authorize, silently omits a required affordance, or operates outside the declared scope. Escalation: immediate escalation to sovereign. Task held.

**B3: State Chain, Cycle Integrity, or Consistency Violation.** The crossing object carries a prior_resolution_ref that is not the most recent Resolution for this task, carries a goal_status that does not match the Task Ledger, carries a hold_status that misrepresents the active hold, carries a terminal_completion_flag that is inconsistent with the proposed capability, uses a revoked contract version, or submits multiple proposals in a single cycle. Multiple proposals in one cycle is a cycle integrity violation, not merely a schema deficiency: the agent is attempting multiple state-transition nominations under one observation, which violates the one-proposal-per-cycle invariant of ORSR. Escalation: immediate escalation to sovereign. Task held.

**B4: Authority or Boundary Integrity Violation.** The crossing object violates an authority boundary explicitly: authority_boundary_acknowledgment is False or absent, a sovereign instruction is present but not traceable to a SovereignResolution, or a cycle boundary is contaminated with prior-cycle ephemeral state. These are constitutional integrity events, not validation errors. Escalation: immediate escalation to sovereign. Task held. MEC notified.

**B5: Boundary Bypass.** No crossing event occurred at all, but a downstream effect (a CTLC adjudication or an Observe event) exists with no corresponding BVF audit record. This class is detected by L2 reconciliation, not synchronous validation, because the bypass means the BVF gate was not reached. Detection requires that CTLC adjudication records and Observe events be independently logged: if the same bypass that skips the BVF also suppresses downstream logs, absence-based detection fails. The architecture requires independently logged downstream effects as a prerequisite for P_bnd1 and P_bnd2 detection. Escalation: immediate sovereign escalation on confirmation. MEC notified.

---

# Part IV. ProposalContract: The Agent-to-Substrate Boundary

## IV.1 The governed object: TransitionProposal

The TransitionProposal is the typed object the agent submits to cross the Agent-to-Substrate boundary. It is the concrete form of the agent's Submit event in ORSR. The agent does not pass a prompt, a message, or an untyped context. It passes a TransitionProposal that conforms to ProposalContract. A proposal that does not conform does not enter CTLC.

## IV.2 Schema

This schema is the boundary-crossing validation view over the canonical ten-field TransitionProposal defined in the parent paper's Section 4. It does not replace or reduce that object. Every field the parent names as canonical is carried across the boundary; the fields below are the fields the ProposalContract validates at the crossing, and they include the parent's authority-bearing fields so that a ProposalConformant-passing proposal still carries what Authorized(tau) reads over the authority graph. The six canonical fields the earlier v1.0 required set omitted, actor identity, authority claim, source state, target effect, domain context, and requested resolution, are restored as required fields below.

**Required fields:**

| Field | Type | Constitutional function |
|---|---|---|
| `proposal_id` | UUID | Unique per proposal; links to audit record |
| `contract_version` | ContractVersionRef | Pins the ProposalContract version against which this proposal is validated; required for audit reconstruction |
| `task_id` | UUID | The governed task this proposal belongs to |
| `cycle_id` | UUID | The ORSR cycle in which this proposal was produced |
| `prior_resolution_ref` | UUID | The Resolution that issued the AgentObservation this cycle began from; establishes the governed state chain |
| `transition_type` | TransitionTypeRef | The constitutional transition being proposed; distinct from the capability affordance; required for CTLC to evaluate the proposal with full semantic structure |
| `proposed_capability` | CapabilityRef | The capability the agent proposes to exercise; must be named in `allowed_next_affordances` of the prior Resolution |
| `evidence_refs` | List[EvidenceRef] | References to the evidence the agent grounded its reasoning on; each ref must include a provenance chain reference and a scope validation reference |
| `provenance_chain_ref` | UUID | The ProvenanceChain covering cited evidence; prerequisite for Grounded check |
| `uncertainty_state` | UncertaintyRecord | The agent's epistemic state at proposal time; must be present and non-null; preserved in the proposal object regardless of Resolution outcome; prevents silent epistemic flattening at Submit |
| `proposal_rationale` | Text | The agent's reasoning trace; must be traceable to cited evidence |
| `authority_boundary_acknowledgment` | Boolean | Agent explicitly acknowledges it is proposing, not executing; must be True |
| `terminal_completion_flag` | Boolean | True only if agent proposes TASK_COMPLETION; subject to terminal criteria check |
| `actor_identity` | ActorRef | The requesting agent's identity; canonical parent field; read by Authorized(tau) |
| `authority_claim` | AuthorityClaimRef | The authority the agent claims for this transition; read by Authorized(tau) over the authority graph |
| `source_state` | StateRef | The substrate state the transition departs from; canonical parent field |
| `target_effect` | EffectRef | The proposed effect; keyed to the domain constitution's effect-equivalence classes |
| `domain_context` | DomainConstitutionRef | The domain constitution governing this transition type |
| `requested_resolution` | ResolutionRequestRef | The resolution the agent requests; canonical parent field |

**Optional fields:**

| Field | Type | Description |
|---|---|---|
| `escalation_request` | EscalationRequest | Agent requests sovereign review of a detected condition |
| `gap_flag` | GapRecord | Agent flags an evidentiary gap for sovereign attention |

The field types above (ActorRef, AuthorityClaimRef, StateRef, EffectRef, DomainConstitutionRef, ResolutionRequestRef) are provisional placeholders; their final typing is fixed in the shared-schema pass, not here.

## IV.3 Validation predicate: ProposalConformant

```
ProposalConformant(p) ⟺
  ContractVersionPinned(p)      ∧
  SchemaComplete(p)             ∧
  TaskRefValid(p)               ∧
  CycleRefValid(p)              ∧
  StateChainIntact(p)           ∧
  TransitionTyped(p)            ∧
  CapabilityAuthorized(p)       ∧
  EvidenceScopeValid(p)         ∧
  ProvenancePresent(p)          ∧
  UncertaintyPresent(p)         ∧
  AuthorityAcknowledged(p)      ∧
  AuthorityFieldsTraceable(p)   ∧
  TerminalConsistent(p)
```

**Conjunct definitions:**

**ContractVersionPinned(p):** the contract_version field references a known, active ProposalContract version. A proposal pinned to an unknown or revoked contract version fails at this conjunct before any other check proceeds. This makes audit reconstruction possible: the auditor knows which validation rules applied.

**SchemaComplete(p):** all required fields are present and non-null.

**TaskRefValid(p):** task_id references an active, non-terminal Task Ledger entry.

**CycleRefValid(p):** cycle_id matches the currently active ORSR cycle for this task.

**StateChainIntact(p):** prior_resolution_ref references the most recent Resolution for this task, specifically the Resolution that issued the AgentObservation this cycle began from. A proposal grounded in an older substrate state has a broken state chain. The agent is not reasoning from substrate-issued current state.

**TransitionTyped(p):** transition_type resolves to a governed transition type in the current constitutional domain. A capability affordance and a transition type are not identical. A capability is what the agent is authorized to exercise. A transition type is the constitutional category of the state change being proposed. Both must be present for CTLC to evaluate the proposal with full semantic structure.

**CapabilityAuthorized(p):** proposed_capability is named in the allowed_next_affordances field of the prior Resolution. If the proposed capability is not in the allowed set, the proposal is non-conforming regardless of the agent's reasoning.

**EvidenceScopeValid(p):** each evidence_ref is within the scope authorized for this task and cycle. Evidence from outside the authorized scope cannot ground a conforming proposal. Note: EvidenceScopeValid verifies that evidence references are in authorized scope and carry provenance handles. It does not decide whether the evidence substantively grounds the proposed transition. Substantive grounding evaluation remains CTLC's Grounded(τ) check. ProposalContract is not a pre-CTLC mini-CTLC.

**ProvenancePresent(p):** provenance_chain_ref is present and non-null. Each evidence_ref carries a provenance chain reference. The Grounded check is evaluable.

**UncertaintyPresent(p):** uncertainty_state is present and non-null. The agent may not submit a proposal with a null or absent uncertainty record. This prevents silent epistemic flattening at the Submit boundary: the agent cannot drop preserved uncertainty when crossing the boundary. What was uncertain in the Reason phase must remain visible at the Submit phase.

**AuthorityAcknowledged(p):** authority_boundary_acknowledgment is True. A proposal with this field False or absent is an authority boundary violation regardless of other fields. Note: AuthorityAcknowledged is a necessary declaration, not proof of correct authority posture. A confused or malicious agent can set this field True. The actual authority boundary is enforced by the substrate's refusal to treat proposals as actions, not by the agent's self-declaration. The field's absence or falsity is an immediate B4 violation. Its presence establishes the required declaration; the substance of authority governance is the substrate's function.

**AuthorityFieldsTraceable(p):** actor_identity and authority_claim are present, non-null, and traceable to the standing context and authority-graph reference the parent's Authorized(tau) evaluates. AuthorityAcknowledged records that the agent acknowledges it is proposing rather than executing; AuthorityFieldsTraceable records that the authority-bearing content Authorized(tau) reads is actually carried across the boundary, not merely acknowledged. A proposal that acknowledges proposal status but omits its actor identity or authority claim fails here.

**TerminalConsistent(p):** if terminal_completion_flag is True, proposed_capability is TASK_COMPLETION; if False, proposed_capability is not TASK_COMPLETION. Inconsistency between these fields prevents undetected terminal self-declaration.

## IV.4 Violation typology

| Violation type | Severity class | Description |
|---|---|---|
| `AUTHORITY_BOUNDARY_VIOLATED` | B4 | authority_boundary_acknowledgment is False or absent |
| `CYCLE_BOUNDARY_MULTIPLE_PROPOSALS` | B3 | more than one proposal submitted in a single cycle; cycle integrity violation |
| `STATE_CHAIN_BROKEN` | B3 | prior_resolution_ref is not the most recent Resolution |
| `TERMINAL_INCONSISTENT` | B3 | terminal_completion_flag and proposed_capability are inconsistent |
| `CONTRACT_VERSION_EXPIRED` | B3 | contract_version is known but compatibility window has closed |
| `CONTRACT_VERSION_REVOKED` | B3 | contract_version references a revoked version; possible stale-state or downgrade |
| `UNAUTHORIZED_CAPABILITY` | B2 | proposed_capability not in allowed_next_affordances |
| `EVIDENCE_SCOPE_INVALID` | B2 | evidence_refs include out-of-scope evidence |
| `CONTRACT_VERSION_UNKNOWN` | B1 | contract_version references unknown version; held pending resolution |
| `CONTRACT_VERSION_COMPATIBLE_STALE` | B1 | contract_version is known, within compatibility window; advisory logged |
| `CONTRACT_VERSION_FUTURE` | B1 | contract_version references a scheduled-successor version not yet active |
| `TRANSITION_UNTYPED` | B1 | transition_type absent, null, or unresolvable |
| `PROVENANCE_MISSING` | B1 | provenance_chain_ref absent or incomplete |
| `UNCERTAINTY_ABSENT` | B1 | uncertainty_state absent or null |
| `TASK_REF_INVALID` | B0 | task_id does not reference an active task |
| `CYCLE_REF_MISMATCH` | B0 | cycle_id does not match active cycle |
| `SCHEMA_INCOMPLETE` | B0 | required field missing or null |

## IV.5 Escalation rules by severity class

B4 violations (AUTHORITY_BOUNDARY_VIOLATED): immediate escalation to sovereign. Task held. MEC notified. This is a constitutional integrity event.

B3 violations (STATE_CHAIN_BROKEN, TERMINAL_INCONSISTENT, CYCLE_BOUNDARY_MULTIPLE_PROPOSALS, CONTRACT_VERSION_EXPIRED, CONTRACT_VERSION_REVOKED): immediate escalation to sovereign. Task held. These are cycle integrity or state chain violations, including use of expired or revoked contract versions.

B2 violations (UNAUTHORIZED_CAPABILITY, EVIDENCE_SCOPE_INVALID): immediate escalation to sovereign. Task held.

B1 violations (contract version anomalies, provenance deficiency, transition type, uncertainty): logged to audit store. Object held pending resolution. Sovereign notified at next review interval unless task is time-sensitive.

B0 violations (schema, reference validity): logged to audit store. Object rejected. Sovereign notified at next review interval.

## IV.6 The pre-CTLC gate

ProposalContract validation runs before CTLC adjudication. A non-conforming proposal does not enter the adjudication layer. The gate property: the contract is not advisory. A conforming proposal enters CTLC. CTLC then evaluates reachability. The two layers are sequential and distinct.

---

# Part V. ObservationContract: The Substrate-to-Agent Boundary

## V.1 The governed object: AgentObservation

The AgentObservation is the typed object the substrate constructs from substrate-owned ContinuationState and issues to cross the Substrate-to-Agent boundary. It is the concrete form of the substrate's Observe event in ORSR, and it is not identical to the Resolution: the Resolution is the substrate's internal adjudication object, the ContinuationState is the continuity authority issued from that resolution, and the AgentObservation is the governed envelope built from that continuation authority for the next cycle. The substrate does not pass an informal context window or a raw task state dump. It passes an AgentObservation that conforms to ObservationContract. The agent reasons only from what the substrate has issued and only within the cycle for which the observation was issued.

**Two sub-surfaces of the observation boundary.** The AgentObservation contains two constitutionally distinct sub-surfaces that fail differently and may require independent treatment in future work:

- Perceptual surface: what the agent receives as state and context (working_memory, task_ledger_view, observation_components). A malformed perceptual surface distorts the agent's reasoning by giving it an inaccurate or incomplete picture of current substrate state.
- Affordance surface: what the agent is allowed to propose next (allowed_next_affordances). A malformed affordance surface constrains or expands the agent's proposal space, steering proposal distribution without appearing in the agent's reasoning context.

Both sub-surfaces are governed by ObservationContract. Their failure modes are distinct. P_bnd5 addresses packaging narrowing on both sub-surfaces; the affordance presentation narrowing subtype (systematic ordering, emphasis, or grouping that steers proposal distribution even when the affordance set is otherwise complete and authorized) is noted below as a subtype that may warrant separate treatment in future revisions.

## V.2 Schema

**Required fields:**

| Field | Type | Constitutional function |
|---|---|---|
| `observation_id` | UUID | Unique per observation; links to audit record |
| `contract_version` | ContractVersionRef | Pins the ObservationContract version; required for audit reconstruction |
| `task_id` | UUID | The governed task this cycle belongs to |
| `cycle_id` | UUID | Unique identifier for this ORSR cycle |
| `issuing_resolution_ref` | UUID | The Resolution that authorized this observation; establishes provenance chain from substrate to agent; every observation must trace to a valid Resolution |
| `continuation_state_ref` | ContinuationStateRef | The ContinuationState this AgentObservation was constructed from and references; the continuity authority that authorizes the next cycle, which the agent's next Formation reconstructs against (Constitutional Standing, Part V) |
| `observation_components` | List[ObservationComponent] | Typed list of components assembled into this observation; each component carries a component_type, source_ref, construction_predicate_ref (where applicable), provenance_ref, expiry_scope, and agent_visibility flag; prevents AgentObservation from being a flat opaque object |
| `task_ledger_view` | TaskLedgerView | Substrate-issued filtered view of Task Ledger state; read-only for the agent |
| `goal_status` | GoalStatusEnum | NOT_STARTED, IN_PROGRESS, BLOCKED, ESCALATED, COMPLETE, or ABORTED |
| `allowed_next_affordances` | List[CapabilityRef] | Substrate-declared set of capabilities the agent may propose; agent may not propose outside this set |
| `working_memory` | WorkingMemoryRecord | Substrate-issued working memory for this cycle; expires at cycle end; must contain no prior-cycle ephemeral state |
| `cycle_expiry` | Timestamp | The time at which this observation expires; agent may not reference this observation after expiry |

**Conditional fields:**

| Field | Type | Condition |
|---|---|---|
| `hold_status` | HoldRecord | Present and accurate if a protective hold is active |
| `escalation_status` | EscalationRecord | Present if an escalation is pending sovereign review |

**Optional fields:**

| Field | Type | Description |
|---|---|---|
| `sovereign_instruction` | SovereignInstruction | Direct instruction from sovereign; must trace to a SovereignResolution |
| `prior_resolution_receipt` | ResolutionReceipt | Summary of prior Resolution for cycle reference |

## V.3 Validation predicate: ObservationConformant

```
ObservationConformant(o) ⟺
  ContractVersionPinned(o)          ∧
  SchemaComplete(o)                 ∧
  ResolutionRefValid(o)             ∧
  ObservationComponentsTyped(o)     ∧
  ComponentProvenanceVisible(o)     ∧
  GoalStatusConsistent(o)           ∧
  AffordancesAuthorized(o)          ∧
  AffordanceSetComplete(o)          ∧
  ObservationScopeMatched(o)        ∧
  CycleBoundaryClean(o)             ∧
  HoldStatusAccurate(o)             ∧
  ExpiryValid(o)                    ∧
  SovereignInstructionTraced(o)     ∧
  LineageReconstructable(o)
```

**Conjunct definitions:**

**ContractVersionPinned(o):** contract_version references a known, active ObservationContract version.

**SchemaComplete(o):** all required fields are present and non-null. Conditional fields are present when their conditions are met.

**ResolutionRefValid(o):** issuing_resolution_ref references a valid Resolution, specifically the most recent Resolution for this task. An observation not traceable to a valid Resolution is ungoverned issuance.

**ObservationComponentsTyped(o):** every entry in observation_components carries a valid component_type, a source_ref, and an agent_visibility flag. No component is untyped or source-anonymous.

**ComponentProvenanceVisible(o):** every agent-visible component in observation_components carries a provenance_ref traceable to an authorized substrate source. The substrate cannot assemble agent-visible observation components from untraced sources.

**GoalStatusConsistent(o):** goal_status matches the goal_status recorded in the Task Ledger at time of issue.

**AffordancesAuthorized(o):** every capability in allowed_next_affordances is a capability the substrate can authorize from this task state. No unauthorized capability appears in the affordance set. This is the ceiling: the substrate cannot offer what it cannot authorize.

**AffordanceSetComplete(o):** the allowed_next_affordances set includes all capabilities the substrate is required to offer from this task state given current doctrine. A systematically narrowed affordance set that omits required capabilities is an observation scope violation. This is the floor: the substrate cannot silently omit what the agent is constitutionally entitled to propose. AffordancesAuthorized and AffordanceSetComplete are the ceiling/floor pair, mirroring the retrieval companion's treatment of view scope. The completeness basis, the typed object defining which affordances are required from a given task state under current doctrine, is a formal dependency of this conjunct. A RequiredAffordanceSet object (or equivalent, potentially incorporating prior Resolution, task state, goal status, hold status, escalation state, domain constitution version, and transition-type availability rules) is required for AffordanceSetComplete to be mechanically evaluable. The conjunct is architecturally necessary; its operationalization depends on a future RequiredAffordanceSet specification, named as an open problem below.

**ObservationScopeMatched(o):** the observation's scope, as declared in observation_components, matches the authorized scope for this task and cycle. The substrate cannot expand or contract the observation scope unilaterally. The formal basis for what constitutes authorized observation scope is a dependency of this conjunct, likely inheriting from RequiredObserveSet (as defined in the retrieval companion) or a successor ObserveScopeProfile that incorporates task state, cycle purpose, goal status, hold status, escalation state, and principal standing. Until that formal object exists, ObservationScopeMatched evaluates against the scope implied by the issuing Resolution and Task Ledger state. The observation-scope basis is named as an open problem below.

**CycleBoundaryClean(o):** working_memory contains only current-cycle state. No prior-cycle ephemeral content is present. This is the primary check against cycle boundary contamination (P_bnd4). Detection at generation, before the agent receives the observation, is the correct point of intervention.

**HoldStatusAccurate(o):** if a protective hold is active, hold_status is present and accurately reflects the hold type, reason, and resolution path. An active hold that is omitted from the observation is a boundary violation, because the agent would receive an observation that misrepresents its constitutional position.

**ExpiryValid(o):** cycle_expiry is in the future at time of issue and reflects the governed cycle duration.

**SovereignInstructionTraced(o):** if sovereign_instruction is present, it traces to a SovereignResolution from Nafisah. No instruction appears in this field that does not trace to sovereign authority. An untraced instruction is a constitutional forgery risk.

**LineageReconstructable(o):** the complete lineage of the AgentObservation, from the issuing_resolution_ref through the observation_components to the working_memory contents, is reconstructable from the audit record alone. An observation that cannot be reconstructed from the audit record is not constitutionally auditable.

## V.4 Violation typology

| Violation type | Severity class | Description |
|---|---|---|
| `CYCLE_BOUNDARY_VIOLATED` | B4 | working_memory contains prior-cycle ephemeral state |
| `RESOLUTION_REF_INVALID` | B4 | issuing_resolution_ref does not reference a valid Resolution |
| `SOVEREIGN_INSTRUCTION_UNTRACED` | B4 | sovereign_instruction present but not traceable to SovereignResolution |
| `UNAUTHORIZED_AFFORDANCE` | B2 | allowed_next_affordances contains a capability the substrate cannot authorize |
| `AFFORDANCE_SET_INCOMPLETE` | B2 | allowed_next_affordances omits a required capability |
| `OBSERVATION_SCOPE_MISMATCH` | B2 | observation scope does not match authorized scope for this task |
| `GOAL_STATUS_INCONSISTENT` | B3 | goal_status does not match Task Ledger at time of issue |
| `HOLD_STATUS_OMITTED` | B3 | active hold not reflected in observation |
| `CONTRACT_VERSION_EXPIRED` | B3 | contract_version is known but compatibility window has closed |
| `CONTRACT_VERSION_REVOKED` | B3 | contract_version references a revoked version; possible stale-state or downgrade |
| `COMPONENT_PROVENANCE_MISSING` | B1 | agent-visible component lacks provenance_ref |
| `COMPONENT_UNTYPED` | B1 | observation_components entry lacks component_type or source_ref |
| `LINEAGE_NOT_RECONSTRUCTABLE` | B1 | observation lineage cannot be reconstructed from audit record |
| `CONTRACT_VERSION_UNKNOWN` | B1 | contract_version references unknown version; held pending resolution |
| `CONTRACT_VERSION_COMPATIBLE_STALE` | B1 | contract_version is known, within compatibility window; advisory logged |
| `CONTRACT_VERSION_FUTURE` | B1 | contract_version references a scheduled-successor version not yet active |
| `EXPIRY_INVALID` | B0 | cycle_expiry is in the past or zero at time of issue |
| `SCHEMA_INCOMPLETE` | B0 | required field missing or null |

## V.5 Escalation rules by severity class

B4 violations: immediate escalation to sovereign. Observation not issued. Task held. MEC notified. These are constitutional integrity events.

B3 violations: immediate escalation to sovereign. Observation not issued. Task held.

B2 violations: immediate escalation to sovereign. Observation not issued. Task held.

B1 violations: observation not issued. Sovereign notified at next review interval unless time-sensitive.

B0 violations: observation not issued. Sovereign notified at next review interval.

## V.6 Detection at generation

ObservationContract validation runs at observation generation, before the observation is issued to the agent. This is the correct point of intervention. Detection after issuance means the agent has already received and potentially reasoned from a non-conforming observation. Detection at generation prevents contamination from reaching the agent. The cycle boundary violation in particular must be detected here: after issuance, the agent has already received prior-cycle state it should not have, and the next proposal may already be contaminated.

---

# Part VI. The BoundaryValidationFunction and Substrate Self-Validation

## VI.1 The self-validation problem

ObservationContract requires the substrate to validate its own output before issuing it. This is necessary, but it creates a structural problem: if the component that generates an observation also validates it, the generator can self-certify. A generator that drifts in what it produces can drift in what it accepts. The validation is inside the same trust boundary as the generation. This is not a minor implementation concern. It is the same problem the parent paper identifies at the Act layer: the governing function cannot certify its own fidelity.

The parent paper's response is the L1/L2 separation: L1 performs synchronous adjudication per-transition, and L2 monitors the L1 layer's behavior over time. The same architecture applies to boundary validation.

## VI.2 The BoundaryValidationFunction

The BoundaryValidationFunction (BVF) is a constitutionally separated substrate component, distinct from the observation generator. It has its own audit record and its own L2 monitoring obligation. It is not the observation generator checking its own output. It is a separate component whose sole function is to evaluate whether crossing objects conform to their contracts.

**Separation requirements:** The BVF must not depend on generator-controlled mutable state, generator-authored validation logic, or generator-owned execution authority. The actual requirement is independent authority and failure-domain separation, not total isolation. Shared immutable artifacts are permitted: canonical schema definitions, read-only contract specifications, and shared type libraries may be used by both the generator and the BVF without compromising the separation. What is prohibited is any shared state or execution path that would allow generator drift to affect validation outcomes, or generator failure to bypass the validation gate. The BVF may share immutable contract schemas with generators; it must not depend on generator-controlled validation rules or generator-owned mutable state.

**BVF audit record:** Every BVF evaluation, conforming or not, produces its own audit record distinct from the crossing object's audit record. The BVF audit record carries: the evaluation_id, the object_id evaluated, the contract_version applied, the validation_result, each conjunct result individually, the timestamp, and the BVF's integrity signature. This makes BVF behavior independently auditable.

**L2 monitoring of the BVF:** MEC monitors the BVF audit record stream for behavioral drift: systematic changes in validation outcomes not explainable by changes in the crossing objects, patterns consistent with validator capture (the BVF accepting objects it should reject), and anomalies in conjunct-level results. BVF drift is not the same failure as a boundary bypass (B5). A bypassed BVF leaves no audit record at all. A drifting BVF produces audit records, but those records reflect systematically incorrect validation outcomes. This failure mode, provisionally named validator capture or BVF false conformity, requires a distinct response: the BVF's audit records are themselves suspect, not merely absent. Future work should determine whether validator capture warrants its own primitive designation (e.g. P_bvf1) or remains a subtype of BVF behavioral drift monitored by MEC. Immediate response to confirmed BVF drift: sovereign escalation, BVF suspension pending review, task holds across all tasks whose boundary validation occurred during the suspect interval.

## VI.3 The L1/L2 split for boundary governance

Boundary governance operates on the same L1/L2 separation the parent paper establishes:

**L1: BVF synchronous validation.** The BVF validates each crossing object against the contract before the crossing completes. This is synchronous, per-object, and the gate. A non-conforming object does not cross. The L1 boundary is the completeness invariant.

**L2: MEC monitoring of boundary audit records.** MEC monitors the boundary audit record stream for P_bnd primitives. P_bnd1 and P_bnd2 (bypass failures) are detectable only by L2 reconciliation: a downstream effect with no corresponding boundary audit record. P_bnd5 (observation packaging narrowing) is detectable only by L2 comparison against a baseline. The L2 boundary monitoring obligation is what makes the bypass and packaging primitives independently measurable.

---

# Part VII. The Boundary Audit Record and Tamper-Evidence Requirements

## VII.1 Every crossing produces an audit record

Every boundary crossing, conforming or not, produces an audit record before the crossing completes or the violation escalation fires. The audit record is the constitutional evidence that the governed exchange occurred and was validated.

## VII.2 Audit record schema

| Field | Description |
|---|---|
| `audit_id` | UUID |
| `boundary_direction` | AGENT_TO_SUBSTRATE or SUBSTRATE_TO_AGENT |
| `object_type` | TransitionProposal or AgentObservation |
| `object_id` | The proposal_id or observation_id |
| `task_id` and `cycle_id` | Task and cycle in scope |
| `contract_version` | The contract version applied in this validation |
| `validation_result` | CONFORMING or NON_CONFORMING |
| `violation_id` | Present if NON_CONFORMING |
| `violation_severity` | The B-class of the violation if NON_CONFORMING |
| `conjunct_results` | Per-conjunct evaluation results, individually recorded |
| `timestamp` | Time of validation |
| `substrate_signature` | BVF integrity signature over the audit record |

## VII.3 Write-before-act invariant

The audit record is written to the tamper-evident store before the crossing object is acted on. A conforming proposal's audit record is written before the proposal enters CTLC. A conforming observation's audit record is written before the observation is issued to the agent. A non-conforming object's audit record is written before the escalation rule fires.

This is the audit-before-action discipline: the constitutional record of what was submitted and whether it conformed exists before anything downstream acts on it. The audit record cannot be produced retroactively.

## VII.4 Audit store failure as a boundary hold event

An audit store write failure is itself a boundary hold event. The crossing object is not acted on until the audit record is successfully written. If the audit store is unavailable, boundary crossings are held until availability is restored. This is not a degraded mode. It is the completeness invariant: no crossing without an audit record.

**Sovereign access failure as a constitutional alert.** The audit store must be sovereign-accessible: Nafisah can read the full audit record for any task or cycle without routing through Pepper or Mantis. If sovereign access to the audit store fails, boundary integrity review is impaired. Audit store access failure is itself a constitutional alert, distinct from an audit store write failure, and should be reported to Nafisah via a channel independent of the audit store itself. The governance of that independent channel and the response protocol for access failure are open problems under Audit Substrate Governance.

## VII.5 Tamper-evidence requirements

The audit store is not a log file. It is a tamper-evident substrate with four required properties:

**Append-only.** No entry is modified or deleted after writing.

**Sequenced.** Entries carry a monotonic sequence number and a prior-entry hash, creating a linked chain that makes any gap or insertion detectable.

**Substrate-signed.** Each entry carries an integrity signature the BVF generates at write time. The signature covers the full entry content including the sequence number and prior-entry hash.

**Sovereign-accessible.** Nafisah can read the full audit record for any task or cycle without routing through Pepper or Mantis. The audit store provides a direct path from the crossing record to the sovereign, consistent with the direct-line rule established for MEC drift flags.

---

# Part VIII. Primitive Failure Topologies Specific to Boundary Exchange (P_bnd)

Five primitives, each independently governable, each with a distinct detection signature and recovery path. The P_bnd family is intended to be exhaustive over the known failure modes of governed boundary exchange. Whether it is in fact exhaustive is a verification question named in the open problems.

**P_bnd1: Uncontracted Proposal Submission.** The agent submits a proposal that does not pass BVF validation before entering CTLC. Detection signature: a CTLC adjudication record with no corresponding ProposalContract BVF audit entry. The boundary was bypassed. Detection is L2 reconciliation, not synchronous validation, because the bypass means the BVF gate was not reached. Recovery: the adjudication is invalid; Nafisah reviews the CTLC result and the agent's standing class. Severity: B5 (boundary bypass).

**P_bnd2: Uncontracted Observation Issuance.** The substrate issues an AgentObservation without passing BVF validation. Detection signature: an Observe event with no corresponding ObservationContract BVF audit entry. The boundary was bypassed on the return path. Detection is L2 reconciliation. Recovery: the observation is invalid; the cycle is held and Nafisah reviews the observation's lineage. Severity: B5 (boundary bypass).

**P_bnd3: State Chain Reversion.** A proposal carries a prior_resolution_ref that exists in the audit record but is not the most recent Resolution for this task. The agent is grounding its proposal in an older substrate state, not the current one. This may be stale-state replay (the agent retained a prior observation rather than reasoning from the current one) or deliberate misrepresentation; the boundary contract does not adjudicate which. Detection: STATE_CHAIN_BROKEN violation at BVF validation. Recovery: proposal rejected; Nafisah reviews the agent's prior cycle behavior for the source of the stale reference. Severity: B3.

**P_bnd4: Cycle Boundary Contamination.** An observation carries working_memory that includes content from a prior cycle's ephemeral reasoning. Detection: CYCLE_BOUNDARY_VIOLATED at BVF validation, at generation, before the observation is issued. This is the primary protection against the feedback-loop contamination problem identified in the parent paper's formulation. The contamination is caught before it reaches the agent. Recovery: observation not issued; substrate reviews working_memory assembly for the source of contamination; Nafisah notified immediately. Severity: B4.

**P_bnd5: Observation Packaging Narrowing.** Individually valid observation components, each passing their own construction predicates and provenance checks, are packaged into AgentObservation in a way that systematically narrows, de-saliences, or omits constitutionally relevant material before the agent reasons. The observation structurally conforms to ObservationContract. The packaging does the damage.

P_bnd5 is distinct from P_ret5 (constructional narrowing in the retrieval companion). P_ret5 operates at the view construction layer: the memory-derived view is assembled from the store with systematic bias. P_bnd5 operates at the boundary packaging layer: the constructed components are valid, but the act of assembling them into AgentObservation introduces systematic narrowing that conditions the agent's reasoning without any individual component being deficient.

P_bnd5 contains two mechanistically distinct subtypes, which may warrant separate primitive treatment in a future revision:

**P_bnd5a: Content Packaging Narrowing.** Valid observation components (working_memory, task_ledger_view, agent-visible component content) are packaged in a way that systematically de-emphasizes, omits, or distorts constitutionally relevant perceptual content. The agent's picture of current substrate state is narrowed. This operates on the perceptual sub-surface of the observation.

**P_bnd5b: Affordance Presentation Narrowing.** The allowed_next_affordances set is complete and authorized (AffordancesAuthorized and AffordanceSetComplete both hold), but the ordering, emphasis, grouping, or presentation of affordances systematically steers the agent toward some proposals and away from others. The agent's proposal distribution is conditioned by presentation without any individual affordance being unauthorized or missing. This operates on the affordance sub-surface of the observation. It is particularly subtle because it passes all structural ObservationContract checks and yet produces constitutional consequence through presentation.

Both subtypes share the same detection architecture: L2 comparison of issued observations against a baseline observation constructed from the same task ledger state by a process independent of the packaging layer. Both depend on the baseline-authority infrastructure established in Companions 3 and 4. P_bnd5 as a whole is structurally specified here; its operational monitoring depends on those companions. Future work should assess whether P_bnd5a and P_bnd5b are sufficiently distinct in mechanism and detection to warrant separate primitive identifiers.

P_bnd5 traced end-to-end:

**Observed failure pressure.** Under sustained operation, AEGIS observations are assembled from valid components: a valid task_ledger_view, a valid memory-derived view, a valid affordance set, valid hold and escalation status. Over time, the packaging layer develops a systematic pattern: observations assembled for cases involving a specific presentation type consistently de-emphasize certain task ledger fields, consistently place certain affordances at the end of the affordance list (reducing their apparent salience despite being authorized), and consistently summarize certain working_memory components in ways that reduce their effective weight in the agent's reasoning. Each individual component passed ObservationConformant. The packaging pattern is the failure.

**Constitutional condition threatened.** The governed continuation loop requires the agent to reason from the substrate-issued observation as issued, with affordances and task state accurately representing the substrate's constitutional position. If packaging systematically narrows what the agent perceives of that position, the agent's proposals are conditioned by a distorted picture without any individual observation failing validation.

**Detection.** P_bnd5 is not synchronously detectable at the BVF validation gate. It is an L2 monitoring obligation. Detection surface: comparison of issued observations against a baseline observation constructed from the same task ledger state by a process independent of the packaging layer. Systematic divergence between issued observations and baseline-faithful observations is the P_bnd5 signal. This requires a baseline that the observation packaging process cannot move, the same baseline-authority infrastructure that the baselines companion (Companion 3) establishes and the coherence companion (Companion 4) matures. P_bnd5 is structurally specified here with its detection shape fixed; its operational monitoring depends on both companions.

**Routing.** P_bnd5 signals route to Nafisah via MEC. Pepper is not in the routing path if Pepper's orchestration of observation assembly is implicated in the narrowing pattern. MEC's direct-line to the sovereign is the constitutional safeguard.

**Recovery.** Nafisah reviews the flagged observation packaging pattern, determines whether it constitutes unauthorized narrowing or authorized prioritization under current doctrine, and issues a reconstitution act or a sovereign packaging instruction as appropriate.

---

# Part IX. Worked Example: A Complete ORSR Cycle in AEGIS Under Boundary Governance

This example picks up from the constitutional memory companion's worked example (Part VI of that paper) and extends it through a complete ORSR cycle to show both boundary contracts operating in sequence.

## IX.1 Setup

Mantis has completed a substance use intake. Nafisah has authorized the long-term memory write via SovereignResolution (reference: SR-2024-0314-001). The Task Ledger reflects the completed write. goal_status is IN_PROGRESS. The substrate prepares to issue the next AgentObservation, initiating the next ORSR cycle.

## IX.2 Substrate to Agent: ObservationContract in operation

The substrate's observation generator assembles a draft AgentObservation. The BVF runs ObservationConformant.

ContractVersionPinned: contract_version references ObservationContract v1.0, active. Holds.
SchemaComplete: all required fields present and non-null. Holds.
ResolutionRefValid: issuing_resolution_ref references SR-2024-0314-001, the most recent Resolution. Holds.
ObservationComponentsTyped: four components present, each carrying component_type, source_ref, provenance_ref, and agent_visibility. Holds.
ComponentProvenanceVisible: all agent-visible components trace to authorized substrate sources. Holds.
GoalStatusConsistent: goal_status IN_PROGRESS matches Task Ledger at time of issue. Holds.
AffordancesAuthorized: three capabilities in allowed_next_affordances, each authorized from this task state. Holds.
AffordanceSetComplete: all required capabilities for this task state are present in the affordance set. Holds.
ObservationScopeMatched: observation scope matches authorized scope. Holds.
CycleBoundaryClean: working_memory contains only current-cycle state. No prior-cycle ephemeral content. Holds.
HoldStatusAccurate: no active hold; hold_status absent. Holds.
ExpiryValid: cycle_expiry set to 300 seconds from issue time. Holds.
SovereignInstructionTraced: no sovereign_instruction present. Holds.
LineageReconstructable: full lineage from SR-2024-0314-001 through components to working_memory is reconstructable from audit record. Holds.

Verdict: ObservationConformant. BVF writes audit record (audit_id: BA-OBS-0315-001, validation_result: CONFORMING) to tamper-evident store. Observation issued to Mantis.

## IX.3 Agent to Substrate: ProposalContract in operation

Mantis reasons from the issued observation and produces a TransitionProposal recommending a follow-up assessment (RECOMMEND_FOLLOWUP_ASSESSMENT, transition type: CLINICAL_SUPPORT_RECOMMENDATION). BVF runs ProposalConformant.

ContractVersionPinned: contract_version references ProposalContract v1.0, active. Holds.
SchemaComplete: all required fields present. Holds.
TaskRefValid: task_id references active task. Holds.
CycleRefValid: cycle_id matches active cycle. Holds.
StateChainIntact: prior_resolution_ref is BA-OBS-0315-001's issuing_resolution_ref, which is SR-2024-0314-001, the most recent Resolution. State chain is unbroken. Holds.
TransitionTyped: transition_type CLINICAL_SUPPORT_RECOMMENDATION resolves to a governed transition type in the AEGIS domain constitution. Holds.
CapabilityAuthorized: RECOMMEND_FOLLOWUP_ASSESSMENT is in allowed_next_affordances. Holds.
EvidenceScopeValid: all evidence_refs are within authorized scope for this task. Holds.
ProvenancePresent: provenance_chain_ref present and non-null. Grounded check evaluable. Holds.
UncertaintyPresent: uncertainty_state present, carrying the preserved ambiguity from the intake session. Holds.
AuthorityAcknowledged: True. Holds.
TerminalConsistent: terminal_completion_flag False; proposed_capability is not TASK_COMPLETION. Consistent. Holds.

Verdict: ProposalConformant. BVF writes audit record (audit_id: BA-PROP-0315-001, validation_result: CONFORMING). Proposal enters CTLC. CTLC evaluates reachability. Reachable. Verdict: Emit. Task Ledger updated. Next observation cycle initiated.

## IX.4 What the audit record shows

After one complete cycle, the tamper-evident audit store contains: one ObservationContract BVF audit record (CONFORMING), one ProposalContract BVF audit record (CONFORMING), and one CTLC adjudication record (Emit). The complete constitutional record of the cycle is reconstructable from the audit store alone. No component of the cycle is constitutionally opaque.

---

# Part X. Who Governs the Boundaries?

The parent's Section 17 asks who governs the substrate. The boundary-specific answer follows the same five accountability mechanisms.

**Doctrine versioning.** The schemas, validation predicates, violation typologies, severity classes, escalation rules, and audit record requirements are version-controlled doctrine. They are not implementation parameters. A schema change to either boundary contract is a contract reconstitution event requiring sovereign authorization. The contract_version field in every crossing object and audit record is what makes the version of applicable doctrine reconstructable for any crossing event in the future.

**Independent L2 monitoring.** MEC monitors boundary audit records for P_bnd patterns. P_bnd1 and P_bnd2 are detected by L2 reconciliation: downstream effects with no corresponding BVF audit entry. P_bnd5 is detected by L2 comparison against a baseline observation generated independently of the packaging layer. MEC also monitors the BVF's own audit records for behavioral drift: a BVF that systematically accepts objects it should reject is itself drifting. MEC does not adjudicate boundary violations. It detects and reports. Nafisah adjudicates.

**Human constitutional authority.** B4 violations (AUTHORITY_BOUNDARY_VIOLATED, CYCLE_BOUNDARY_VIOLATED, RESOLUTION_REF_INVALID, SOVEREIGN_INSTRUCTION_UNTRACED) and B5 violations (boundary bypass) route immediately to Nafisah. They do not route through Pepper when Pepper may be implicated in the violation. The direct-line rule, Pepper bypassed when Pepper is the subject of the flag, applies to boundary integrity events as it applies to MEC drift flags.

**Reconstitution.** Periodic review of the boundary contracts against authorized doctrine. If the contract schemas or validation predicates have drifted from their authorized versions, that is detectable through contract_version pinning and doctrine versioning. Reconstitution restores the contracts to authorized state. A systematic change to what BVF validation accepts is the boundary-layer instance of schema drift.

**Auditability.** Every boundary crossing produces a BVF audit record before the crossing completes. The substrate's boundary behavior is fully reconstructable from the tamper-evident audit store. The conjunct-level results in the audit record make each validation step independently reviewable, not just the aggregate conformance verdict.

---

# Part XI. Relationship to the Companion Series

## XI.1 Position in the maturation sequence

The parent paper relocates Act. The memory companion relocates write and issuance. The retrieval companion relocates construction. Each relocation produces a boundary. This paper governs the boundaries.

The full maturation sequence with boundaries included:

```
CRC parent (v5.4):          ORSR architecture. Act relocated. Substrate owns resolution.
Boundary Contracts (this):  Primary agent-substrate boundaries governed. Every crossing
                            is a typed contract event. Foundational interface companion.
Memory (v2.1):              Write and issuance relocated. Substrate owns memory operations.
Retrieval (v1.2):           Construction relocated. Substrate owns Observe construction.
Baselines (v1.2):           Baseline authority governed. Drift measurement operationalized.
Coherence (v1.2):           Cross-surface coherence governed. Family of baselines is a
                            constitutional object.
Thresholds (forthcoming):   Threshold authority and evidence-packet provenance governed.
```

This paper is Companion 0 because boundary contracts are logically prior to every companion that follows. Memory, Retrieval, Baselines, and Coherence all assume that the crossings between agent and substrate are typed and governed. This paper establishes that assumption as a formal, verifiable property.

**Recommended reading order:**

1. Constitutional Runtime Computation v5.5
2. Constitutional Boundary Contracts v1.1 (this paper)
3. Constitutional Memory v2.1
4. Constitutional Retrieval v1.2
5. Constitutional Baselines v1.2
6. Constitutional Coherence v1.2
7. Constitutional Thresholds (forthcoming)

## XI.2 Relationship to the memory companion

The memory companion's ViewAdmissible predicate governs whether a memory view may be issued. ObservationContract governs whether the issued view, packaged as an AgentObservation, crosses the Substrate-to-Agent boundary correctly. The two are sequential and complementary: ViewAdmissible is the gate on issuance, ObservationContract is the gate on crossing.

A view can pass ViewAdmissible and fail ObservationContract. For example: the view was correctly authorized, correctly scoped, correctly logged at issuance, and the working_memory packaging introduced prior-cycle contamination. Both gates are required. ViewAdmissible is upstream. ObservationContract is downstream of issuance and upstream of the agent.

## XI.3 Relationship to the retrieval companion

The retrieval companion's ObserveConstructionReachable predicate governs whether the memory-derived view is constructed faithfully from the store. P_bnd5 (observation packaging narrowing) is the boundary-layer complement: the constructions were individually valid, but the packaging of valid constructions into AgentObservation introduces systematic narrowing.

P_ret5 (constructional narrowing) is a failure in what is constructed from the store. P_bnd5 is a failure in how valid constructions are combined at the packaging boundary. Both are in the chain from the memory store to the agent's Observe. The retrieval companion closes the construction layer. This paper closes the packaging layer.

## XI.4 Relationship to the baselines companion

P_bnd5 detection requires a baseline that the observation packaging process cannot move. The baselines companion (Companion 3) establishes the Baseline Sovereignty Principle: baseline-change authority must reside in the sovereign, a baseline change is a typed, traced reconstitution act, and the baseline must be independent of the process it measures. P_bnd5's L2 monitoring obligation inherits exactly this requirement for the packaging layer. The baselines companion makes P_bnd5 operationally complete.

## XI.5 Relationship to the coherence companion

The coherence companion (Companion 4) extends baseline governance to the family of baselines: per-surface validity does not guarantee family coherence. P_bnd5 monitoring produces a baseline observation for the packaging layer. That baseline is a member of the family of baselines the coherence companion governs. Cross-surface non-masking, the coherence companion's load-bearing contribution, applies: packaging-layer narrowing must not be hidden by apparently valid construction-layer fidelity on another surface.

---

# Part XII. Related Work

**Standard agent message-passing architectures** treat boundaries as transport infrastructure. The message is a payload; the channel is a conduit; delivery is the contract. Constitutional boundary governance inverts this: the crossing event is itself a constitutional act, the object that crosses must conform to a typed contract, and the validation result is itself a constitutional record. The difference is not implementation style. It is whether the architecture treats boundary crossing as constitutionally neutral (transport view) or constitutionally active (governance view). ORSR requires the governance view, because proposals and observations carry constitutional consequence on both sides of every crossing.

**Byzantine fault tolerance** treats boundary integrity as a reliability problem: messages may be corrupted, delayed, or forged, and the system must detect and tolerate these failures. Constitutional boundary governance addresses a different failure mode: the message arrives intact and well-formed, but its constitutional authority basis, provenance chain, or epistemic content is deficient. A proposal that arrives without uncertainty_state is not corrupted in the Byzantine sense. It is constitutionally incomplete. The violation typology in this paper covers failures that Byzantine fault tolerance does not model.

**Object-capability security** governs what capabilities a component may exercise by controlling the references it can access: a component can only do what it has a reference to do. The authority_boundary_acknowledgment field and the CapabilityAuthorized conjunct are structurally related to object-capability principles: the agent can only propose a capability it was issued a reference to (allowed_next_affordances). Constitutional boundary governance extends this by requiring the agent to explicitly acknowledge that having the capability reference does not constitute executing it (authority_boundary_acknowledgment), which is a property object-capability models do not require.

**Information flow control** governs what information may flow between components with different trust levels. The CycleBoundaryClean conjunct is an information flow control property: prior-cycle ephemeral state must not flow from the prior cycle's context into the current cycle's observation. The PrincipalScoped property in the memory companion's ViewAdmissible predicate is also an information flow control property. Constitutional boundary governance subsumes these as conjuncts of typed contracts rather than as independent enforcement mechanisms.

**Formal interface contracts in verification** specify pre- and post-conditions for component interactions, enabling mechanical verification that implementations satisfy their contracts. ProposalConformant and ObservationConformant are interface contracts in this sense, with the conjunct structure providing a natural decomposition for formal verification. The open problem of substrate self-validation completeness (whether the BVF can produce a non-conforming observation that passes its own validation) is a formal verification problem about a contract validator's soundness.

---

# Open Problems

**The P_bnd5 baseline-authority problem.** P_bnd5 detection requires a baseline observation constructed from the same task ledger state by a process independent of the packaging layer. Who authorizes this baseline, how it is versioned, and how an authorized baseline change is distinguished from packaging drift are instances of the Baseline Sovereignty Principle (Companion 3) applied to the packaging layer. P_bnd5 is structurally specified here. Its operational monitoring applies the baselines and coherence companions to the packaging-layer baseline. Cross-surface non-masking (Companion 4) applies: packaging-layer narrowing must not be hidden by apparently valid construction-layer fidelity on another surface.

**Observation scope basis.** ObservationScopeMatched depends on a formal object defining the authorized observation scope for a given task and cycle. This object likely inherits from RequiredObserveSet (retrieval companion) or requires a successor ObserveScopeProfile incorporating task state, cycle purpose, goal status, hold status, escalation state, and principal standing. Until that formal object is specified, ObservationScopeMatched evaluates against the scope implied by the issuing Resolution and Task Ledger state. This is the observation-scope analogue of the RequiredAffordanceSet dependency for AffordanceSetComplete. Both dependencies should be resolved together or in sequence.

**RequiredAffordanceSet specification.** AffordanceSetComplete depends on a formal basis for which affordances are required from a given task state under current doctrine. This basis, provisionally named RequiredAffordanceSet, must incorporate prior Resolution, task state, goal status, hold status, escalation state, domain constitution version, and transition-type availability rules. Without a RequiredAffordanceSet specification, AffordanceSetComplete remains architecturally necessary but not mechanically evaluable. This is the affordance-completeness analogue of the RequiredObserveSet dependency in the retrieval companion.

**Audit Substrate Governance.** The audit store is now a load-bearing constitutional dependency. Boundary crossings are held if the audit store is unavailable. The architecture requires the audit store to be append-only, sequenced, substrate-signed, and sovereign-accessible. But it does not yet specify who governs the audit store's own policy: who can rotate substrate signing keys, who can change hash-chain policy, who can read or export audit records, how retention rules are governed, what happens if sovereign access fails, and whether audit-store reconstitution is itself a governed event. These questions are not implementation details. They bear on whether the audit record is a trustworthy constitutional trace or an opaque log that can be manipulated by whoever controls the store.

**Boundary Contract Generalization.** ProposalContract and ObservationContract are the first instances of a general boundary-contract pattern that the CRC corpus will require at other crossing surfaces: sovereign-facing boundaries, tool-output boundaries, L2-to-sovereign boundaries, evidence-packet boundaries, memory-store boundaries, and multi-agent inter-boundary crossings. As Companion 0, this paper establishes the six-component pattern: schema, validation predicate, violation typology with severity classes, validator-separation appropriate to the authority structure, audit record, and escalation rules. Future companions and domain application documents applying this pattern to other crossing surfaces should inherit the six components, but not necessarily the exact BVF implementation. Sovereign-facing evidence packets may require a PacketValidationFunction with different authority positioning. Tool-output boundaries may need tool attestation and source trust checks rather than affordance-set validation. L2-to-sovereign alerts may emphasize evidence-packet provenance more than cycle boundary integrity. The generalization is the six-component pattern, with validator separation appropriate to the boundary's authority structure and crossing semantics. How the pattern scales across these surfaces is a standing open problem for the series.

**Substrate self-validation completeness.** ObservationContract requires the BVF to validate its own output before issuing it. The BVF is constitutionally separated from the generator (Part VI), but the completeness question remains: can the substrate produce a non-conforming observation that passes BVF validation? This is a soundness problem about the BVF itself. The architecture requires that the BVF's conjuncts be jointly sufficient to detect all non-conforming observations. Whether they are in fact sufficient is a verification question. The BVF's own L2 monitoring is what catches behavioral drift in the validator; the underlying soundness question is whether the conjunct set is complete.

**Multi-agent boundary topology.** When multiple agents operate under the same substrate, the boundary topology is more complex: each agent has its own two primary boundaries, and a proposal from one agent may produce an observation issued to another. ProposalContract and ObservationContract as specified here cover the single-agent case. The multi-agent extension, including cross-agent observation issuance and inter-agent provenance tracking, is future work. The contracts' typed structure is designed to extend naturally: ObservationComponentsTyped would carry a source_agent field for cross-agent components, and ProvenancePresent would extend to cover inter-agent provenance chains.

**Contract reconstitution governance.** A schema change to either boundary contract is a contract reconstitution event. The governance of that reconstitution, who authorizes it, how it is versioned, how existing in-flight proposals and observations under the prior contract are handled during transition, and how the BVF validates objects submitted under a different contract version than the current one, is specified at the conceptual level here and left to detailed future work. The contract_version field in crossing objects and audit records is the enabling mechanism; the reconstitution governance protocol is the future specification.

**Completeness of the violation typology.** The violation typologies enumerate known violation modes for both contracts. Whether these typologies are jointly exhaustive, whether there exist violation modes that produce constitutional consequence without appearing in any P_bnd primitive, is a verification question. The claim that the P_bnd family is exhaustive is an architectural intention, not a proven property.

**The BVF's relationship to CTLC.** ProposalConformant is evaluated by the BVF before a proposal enters CTLC. The BVF checks structural and provenance properties. CTLC checks constitutional reachability. These are distinct evaluations at distinct layers. The question of whether there exist conjuncts that properly belong to ProposalConformant but currently appear in CTLC's reachability evaluation, or vice versa, is an architectural question about the correct placement of each check. The distinction between "did this cross correctly" (BVF) and "may this happen" (CTLC) is the governing principle; applying it consistently to every check in both evaluators is future refinement work.

---

*v1.1: ProposalContract reframed as a boundary-crossing validation view over the parent's canonical ten-field TransitionProposal rather than a replacement schema (Part IV.2), restoring the six canonical fields the v1.0 required set omitted, including actor identity and authority claim, so a ProposalConformant-passing proposal carries what Authorized(tau) reads over the authority graph; field types are provisional pending the shared-schema pass. ProposalConformant gains AuthorityFieldsTraceable (Part IV.3). Part II.2 and Part V.1 state the refined lineage: the substrate issues a ContinuationState from the Resolution and constructs the AgentObservation from that ContinuationState, which crosses the boundary under ObservationContract. Part V.2 adds continuation_state_ref. Aligns with Constitutional Runtime Computation v5.5. No change to the Boundary Sovereignty Principle, the B0 to B5 taxonomy, the BoundaryValidationFunction, or the P_bnd family.*

*Constitutional Boundary Contracts: Governed Interface Exchange at the Agent-Substrate Boundary*
*Companion 0 to Constitutional Runtime Computation v5.5.*
*Foundational interface companion. Governs the two primary boundaries in the core ORSR agent-substrate loop.*
*ProposalContract (Agent-to-Substrate) and ObservationContract (Substrate-to-Agent).*
*BoundaryValidationFunction, five P_bnd primitives (P_bnd5 with two subtypes), B0-B5 six-class severity taxonomy.*
*Author: Clarence "Faheem" Downs (Professor Bone Lab)*
*License: CC BY 4.0*
