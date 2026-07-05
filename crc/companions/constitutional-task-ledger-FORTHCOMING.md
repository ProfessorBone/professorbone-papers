# Constitutional Task Ledger: Task State, Continuation, and Terminal Criteria in Governed Agentic Systems

## Why Task Continuity Cannot Live in Agent Memory

**Status: FORTHCOMING.** This stub fixes the title, the Companion 8 position,
the scope, and the required reading for this paper. It does not contain the
paper itself. Do not cite this stub as a completed contribution. It is retired
once the reviewed v1.0 lands, matching how every prior FORTHCOMING stub in
this series (Thresholds, Tools) was retired only after its own review cycle
completed, not at first draft.

---

## Position in the series

Companion 8, following directly after Constitutional Tools v1.1 in the
reading order. Constitutional Standing v1.2 introduced ContinuationState,
ContinuationIssued, OperationalClosure, PriorResolutionMatched, TaskActive,
and CycleCurrent, but specified them as the vocabulary a continuation
pipeline needs, not as a fully governed task-state object in its own right.
Constitutional Memory v2.2's Part IV-A now depends on cycle closure, on
promotion at the cycle boundary, and on a Task Ledger carrying pending
obligations forward, without that Ledger itself being specified anywhere in
the corpus. Standing and Memory both presuppose the object this paper
defines. It is no longer an open problem footnote. It is a missing substrate
object two existing companions already build on.

## Scope

**Core doctrine, not to be softened:** the agent does not own the task. The
agent does not decide what remains. The agent does not decide when the task
is complete. The agent does not carry task continuity in private reasoning.
The substrate owns task state. The substrate records task progress. The
substrate issues continuation. The substrate defines terminal criteria.

This paper answers, and closes as constitutional questions rather than
implementation questions: what is the authoritative substrate record of task
state; who decides whether a task is active, complete, abandoned, paused,
escalated, or reconstituted; what counts as a cycle; what obligations carry
forward after a Hold, an Escalate, an Emit, a NonFormation, a StandingFailure,
or a ToolResultHold; what terminal criteria determine task completion; what
prevents the agent from privately deciding what remains to be done; and how
`allowed_next_affordances` get issued, narrowed, expanded, or retired across
a task's lifetime rather than within a single cycle.

AEGIS remains the worked domain, continuing the corpus's running cast:
Nafisah sovereign principal, Mantis clinical reasoning agent, MEC the L2
monitor, Pepper the orchestrator.

## Required reading

Read each in full before drafting the outline.

- **Constitutional Runtime Computation v5.4.** Core. Especially section 4 (the
  ORSR loop and the Resolution object), section 6 (the four-conjunct
  Reachable(τ) predicate; do not reopen it), and section 6a (HOLD verdict
  completeness: the HoldRecord's pinned-reference schema, non-formation,
  non-replayability, non-bypassability). This paper's terminal-criteria and
  obligation-carrying apparatus should cite section 6a's pinned-reference
  discipline directly rather than re-deriving it, the way every companion
  since Tools has.

- **Constitutional Standing v1.2.** The paper this one extends most directly.
  Read closely: the five-stage pipeline (Formation, Standing, Reachability,
  Binding, Continuation), the ContinuationState and ContinuationIssued
  objects, OperationalClosure, PriorResolutionMatched, TaskActive and
  CycleCurrent as the vocabulary already named but not yet formalized into a
  governed task-state object, and Cumulative Standing Creep as the corpus's
  fourth sovereign-terminal primitive, the precedent this paper's own
  sovereign-terminal evaluation (see Likely Primitives, below) must be
  measured against with the same rigor, not assumed by analogy.

- **Constitutional Memory v2.2.** Especially Part IV (the Memory Governance
  Boundary and its cycle-closure model, which this paper's own TaskLedger
  must not duplicate) and Part IV-A (Failure-Derived Learning and the
  Constitutional Feedback Loop), which already depends on cycle closure,
  LearningCandidate tier targeting across cycles, and FeedbackObservation's
  own `continuation_state_ref` and `issued_in_cycle` fields, added on
  first-pass review specifically because nothing yet formalized what a cycle
  or a task's continuation record actually is. This paper supplies that
  missing object; Memory's own Part IV-A should not be re-opened to do it.

- **Constitutional Boundary Contracts v1.0.** The six-component pattern
  (schema, validation predicate, typed violation taxonomy mapped to B0-B5,
  a constitutionally separated validator, a tamper-evident audit record, an
  escalation rule) that both the Memory Governance Boundary and the Tool
  Governance Boundary already extend as a third and fourth instance,
  respectively. If this paper's own TaskLedger needs a governed crossing
  (an open question, see below), it should extend the same pattern rather
  than invent a new one.

- **Constitutional Tools v1.1.** Read primarily for method, not content: the
  ToolInvocationReachable / ToolResultAdmissible separation (invocation
  emission is not the same event as result admission) is the closest
  structural precedent in the corpus for how this paper should treat
  continuation issuance versus task closure as two independently
  governable events, and Tools' own four-part sovereign-terminal test
  applied to P_tool5 and P_tool6, concluding neither qualified, is the
  precedent this paper's own primitive evaluation must match in rigor,
  not merely gesture at.

## Things intentionally left open for the outline to decide

1. **Whether TaskContinuationReachable(ν) and TaskClosureValid(ω) are one
   composed predicate or two independently evaluated ones.** Continuation
   (a task remaining open across a cycle boundary) and closure (a task
   ending) are not obviously the same event gated by the same conjuncts;
   Tools' own Emit/Admit separation is a candidate precedent for treating
   them as two stages of one pipeline rather than two unrelated predicates,
   but the outline should derive this rather than assume it.

2. **Whether PendingObligation is a first-class typed object with its own
   lifecycle, or a structured field within TaskLedger.** The working object
   list names both TaskLedger and PendingObligation separately, which may
   overspecify; an obligation arising from a Hold, an Escalate, or a
   ToolResultHold may need enough independent structure (its own audit
   trail, its own resolution state, its own expiry) to justify a typed
   object of its own, the way LearningCandidate earned separate status from
   HoldRecord in Memory v2.2, or it may not.

3. **Whether Task-State False Stability (the candidate P_task8) is this
   paper's own sovereign-terminal primitive, or fails the four-part test the
   way every candidate in Tools and Memory did.** Unlike those two papers,
   this is a genuinely open question here, not a foregone conclusion: a task
   ledger that silently and individually-authorizedly accumulates a false
   picture of what remains to be done, across many small pending-obligation
   resolutions each locally defensible, has real structural similarity to
   Cumulative Standing Creep (the corpus's fourth sovereign-terminal
   primitive). The outline must apply the four-part test explicitly
   (undetectable at a single local event; lineage surfacing required; no
   higher authority settles it without regress; sovereign review rather
   than a computed verdict) rather than assume the answer either way from
   the pattern of the two most recent papers.

## Working material (Faheem's own seed, not yet an outline)

Working title: *Constitutional Task Ledger: Task State, Continuation, and
Terminal Criteria in Governed Agentic Systems.* Subtitle: *Why Task
Continuity Cannot Live in Agent Memory.*

Candidate core objects: TaskLedger, TaskState, CycleRecord, ContinuationState
(extended, not re-derived, from Standing's own object), PendingObligation,
TerminalCriteria, TaskClosureRecord, ReconstitutionRecord,
AllowedNextAffordanceSet, TaskProgressRecord.

Candidate core predicates:

```
TaskContinuationReachable(ν) ⟺
  TaskActive(ν)
  ∧ PriorResolutionMatched(ν)
  ∧ CycleCurrent(ν)
  ∧ PendingObligationsAccounted(ν)
  ∧ TerminalCriteriaEvaluated(ν)
  ∧ AllowedNextAffordancesIssued(ν)
  ∧ ContinuationLogged(ν)
```

```
TaskClosureValid(ω) ⟺
  TerminalCriteriaSatisfied(ω)
  ∧ PendingObligationsResolvedOrCarried(ω)
  ∧ RequiredArtifactsRecorded(ω)
  ∧ SovereignReviewSatisfiedWhereRequired(ω)
  ∧ ClosureLogged(ω)
  ∧ NextStateIssued(ω)
```

Candidate primitives: P_task1 Private Task Continuation; P_task2 Premature
Task Closure; P_task3 Orphaned Escalation; P_task4 Affordance Drift; P_task5
Pending Obligation Loss; P_task6 Terminal Criteria Substitution; P_task7
Reconstitution Without Ledger Migration; P_task8 Task-State False Stability.
Faheem's own judgment, recorded here for the outline to test rather than
assume: P_task1 is probably the most load-bearing (it is this paper's own
instance of the private-continuation doctrine Standing already established,
now applied to task state rather than a single verdict), but P_task5 may be
the most dangerous, since a system can appear fully governed while
escalations, Holds, unresolved tool results, or memory promotions silently
disappear from the task state one small loss at a time.

## Recommended sequence

1. Detailed outline for Constitutional Task Ledger (the next task).
2. First-pass review of the outline.
3. Draft v0.1 from the reviewed outline.
4. First-pass review of v0.1.
5. Targeted revision to v1.0.
6. Only then, revisit whether Constitutional Feedback should be extracted as
   Companion 9. It becomes stronger, and better scoped, once the Task Ledger
   exists to give it somewhere to land.
