# Architecture Selection and the Scope of Constitutional Governance
## Choosing Ordinary Execution, Constitutional Runtime, or a Certified Hybrid, and Why the Choice Fails Closed

**Author:** Faheem Downs
**Institutional attribution:** Professor Bone Lab
**Short identifier:** ASC
**Version:** v1.0
**Artifact class:** Normative artifact
**Secondary function:** Methodology and architecture-selection doctrine
**Corpus:** Constitutional Runtime Computation
**Status:** Ratified
**Ratifying authority:** Faheem Downs
**Canonical scope:** Upstream doctrine for selecting the governance architecture an application is justified in using, and the bounded finding that no general scope-certification procedure is currently established
**Predecessor:** None
**Supersedes:** None
**Open Architecture Dependencies:** None for the doctrine established here. The candidate constructive Hybrid class discussed later is illustrative only and is not a construction claim. Any concrete certified Hybrid may depend on architecture the corpus does not yet own and must be pursued through a separate governed workstream.
**CRC-SSR impact:** None
**CRC-CORPUS-ENTRY impact:** None
**Publication state:** Ratified for governed publication; not public or active until committed and pushed

This paper establishes upstream doctrine. It answers a question the operative corpus does not currently answer: given an application, which governance architecture is justified?

It does not define runtime objects. It does not amend Core. It does not alter CRC-OAR, CRC-SSR, or CRC-CORPUS-ENTRY. It does not weaken complete mediation. It references canonical CRC architecture as evidence that governed boundaries, binding discipline, and effect admission already exist. It does not operationally consume, validate, subtype, or extend any canonical runtime schema.

A note on Invariant I1 is required at the outset because this paper sits directly upstream of it.

Complete mediation requires that all consequential transitions pass through mandatory mediation. Complete mediation ranges over the class of consequential transitions. Direct inspection of the [operative Core](../constitutional-runtime-computation-v5.14.md) establishes that the corpus states its mediation requirement over consequential transitions, does not define the universe of all system transitions, does not provide a general membership rule for the consequential class, and does not equate every system transition with a TransitionProposal. All consequential transitions remain subject to complete mediation. This paper addresses the separate, upstream problem of determining membership in the consequential class, which is the unresolved outer boundary. It does not alter the mediation requirement Core owns.

Where complete mediation applies, it continues to apply in full.

This paper supplies a doctrine for selecting scope. It does not amend the guarantee that governs what happens once that scope has been established.

# Abstract

The Constitutional Runtime Computation corpus defines how constitutional governance works once a system has entered constitutional scope. It does not provide a general doctrine for deciding when an application requires Constitutional Runtime, when ordinary execution is sufficient, or when routine and constitutional execution may be composed within one application.

This paper establishes that upstream architecture-selection doctrine.

The central claim is that the choice among ordinary execution, Hybrid architecture, and Full Constitutional Runtime is not settled by stakes, by counting consequential transitions, by capability identity, or by actuator identity.

The architecture-selection procedure has two stages. First, whether constitutional guarantees are required is supplied as a prior sovereign determination, authored by the constitutional principal and not computed by the system being evaluated. Where guarantees are not required, ordinary execution is eligible. Where they are required, affirmative scope certification distinguishes Hybrid eligibility from the Full Constitutional Runtime governance baseline.

Ordinary execution is justified where the application requires no constitutional guarantee. Hybrid architecture is available only where constitutional scope can be positively certified while preserving a non-empty routine execution domain. Full Constitutional Runtime is justified where constitutional guarantees are required but the boundary of constitutional scope cannot be affirmatively certified.

The procedure fails closed. Failure to certify a narrower Hybrid boundary is not architecture failure. It is an architecture-selection result. Where constitutional guarantees are required and no narrower Hybrid boundary has been affirmatively certified, Full Constitutional Runtime is the required governance baseline.

The paper further establishes a bounded negative result. The operative corpus currently provides no general scope-certification procedure, and the candidate procedures examined during this work do not generalize beyond restricted structural classes. This is not an impossibility theorem. The paper does not claim that no general certification procedure can exist. It establishes only that none is currently available, that several natural candidates fail on structural features of general agentic systems, and that Hybrid therefore carries an affirmative proof burden rather than a presumption of availability.

A restricted gate-then-optimize class is discussed as evidence that the Hybrid branch may be non-vacuous. That class is illustrative only. This paper does not claim to have constructed a certified Hybrid architecture.

# 1. The Upstream Selection Problem

The CRC corpus answers the runtime governance question with increasing precision.

Once a system is operating as a Constitutional Runtime, the corpus specifies how transitions are formed, how standing is established, how reachability is resolved, how effects are admitted, how binding occurs, how continuation is issued, how memory is governed, how Observe is constructed, how tools are mediated, and how governed state acquires authorized effect.

What the corpus does not generally answer is the question that precedes all of those mechanisms:

> Which parts of an application require constitutional governance at all?

A builder must answer that question before selecting an architecture.

The possibilities are not equivalent.

One application may require no constitutional governance and may operate safely under ordinary execution.

Another may require constitutional governance across its entire transition surface.

A third may appear to permit a partition in which some execution remains routine while constitutionally reserved transitions are mediated through a Constitutional Runtime.

Without an explicit scope doctrine, the corpus can explain what happens inside constitutional governance but cannot generally justify where constitutional governance begins and ends.

That omission was difficult to see while the corpus was concerned primarily with systems already presumed to be constitutional.

The corpus developed through an inclusion practice.

Memory was brought under constitutional governance because persistence conditions future retrieval and future reasoning.

Retrieval was brought under constitutional governance because Observe construction conditions the reasoning that produces future proposals.

Tool invocation was brought under constitutional governance because tools can manufacture evidence, mutate state, condition future Observe, and produce external effects.

Boundary crossings were governed because what crosses a boundary determines the basis on which the receiving side reasons or adjudicates.

Each companion identified another surface through which unilateral control could acquire constitutional significance and brought that surface under governance.

This is a powerful method for discovering what must be inside constitutional scope.

It is not, by itself, a method for determining what may safely remain outside.

The architecture-selection problem is therefore an outer-boundary problem.

It asks not only:

> What must constitutional governance include?

It also asks:

> Under what conditions may the remainder be excluded?

This paper establishes the doctrine for answering that second question.

# 2. The Selection Doctrine

The architecture-selection rule is:

> **Hybrid carries the proof burden.**

The builder does not begin by assuming that an application can be divided into constitutional and routine partitions.

The builder must affirmatively justify that division.

The selection doctrine has three branches.

## 2.1 Ordinary Execution

Ordinary execution is justified where the application requires no constitutional guarantees.

This does not mean the application is risk-free, unimportant, or unconstrained. It means that the guarantees supplied by Constitutional Runtime are not required for the application's declared authority, accountability, provenance, binding, or consequence model.

Where there is no reserved constitutional consequence, no constitutional partition is required.

### 2.1.1 Prior Sovereign Requirement Determination

Whether constitutional guarantees are required is a prior sovereign determination supplied to this doctrine as an authoritative input. That determination is authored by the constitutional principal or other duly authorized governance authority; it is not computed by the executing system, the routine domain, or the candidate architecture being evaluated. This paper does not define the procedure, evidentiary standard, or institutional process by which that prior determination is made. It begins after the determination has been established. This boundary follows the same sovereignty principle that prevents a governed system from authoring the constitution under which its own authority is evaluated: the architecture-selection procedure may consume a legitimate requirement determination, but it may not manufacture the premise that decides whether constitutional governance is required.

## 2.2 Certified Hybrid

Hybrid architecture is available only where constitutional scope can be affirmatively certified.

A Hybrid contains both:

1. a constitutional domain in which reserved transitions and decisions are governed; and
2. a non-empty routine domain that retains direct execution authority over activity demonstrated to lie outside the constitutional scope.

Hybrid is therefore not justified by intuition, convenience, or a rough judgment that "most of the application is routine."

It is justified only when the boundary itself can be defended.

## 2.3 Full Constitutional Runtime

Full Constitutional Runtime is justified where:

1. the application requires constitutional guarantees; and
2. the boundary separating constitutional from routine execution cannot be affirmatively certified.

This is the fail-closed branch.

An inability to certify Hybrid does not establish that Hybrid is impossible.

It establishes that Hybrid is not justified.

Where constitutional guarantees are required and no narrower Hybrid boundary has been affirmatively certified, Full Constitutional Runtime is the required governance baseline.

This distinction is central.

> **Certificate failure is not architecture failure. It is an architecture-selection result.**

# 3. Why Proxy Selection Criteria Fail

Several criteria appear intuitively suitable for choosing among architectures.

None is sufficient.

## 3.1 Stakes

The selection is not determined by whether an application is "high stakes."

A high-stakes consequence may be structurally isolable.

A lower-stakes system may contain deeply entangled effect paths that cannot be separated without leaving unmediated authority.

Magnitude does not establish topology.

Stakes may affect whether constitutional guarantees are required. They do not establish whether those guarantees can be confined to a partition.

## 3.2 Transition Count

The selection is not determined by counting consequential transitions.

A system in which only one percent of transitions are constitutionally significant is not thereby a Hybrid candidate.

If the remaining ninety-nine percent can alter, compose into, bypass, or capture the one percent, the apparent numerical separation is meaningless.

The relevant question is not:

> How many consequential transitions exist?

It is:

> Can constitutional scope be structurally isolated from the remainder?

## 3.3 Capability Identity

The selection is not determined by the name or identity of a capability.

The same general capability can occupy different constitutional roles depending on how it is used.

A communication capability can transmit an advisory in one context and create a contractual commitment in another.

A calculation can remain internal cognition in one path and become admitted evidence in another.

Constitutional significance therefore cannot be assigned solely by capability identity.

## 3.4 Actuator Identity

The selection is not determined by the physical actuator.

The same underlying email service can carry both a routine ETA message and a legally consequential commitment.

The same authenticated browser session can perform an informational lookup or a binding transaction.

The physical mechanism is not the constitutional boundary.

The relevant question concerns the authorized effect space reachable through that mechanism.

These failed criteria point toward the actual problem.

Constitutional significance is not reliably established by examining a component in isolation.

It depends on how that component participates in paths to reserved authority and reserved outcomes.

That is why the architecture-selection problem becomes a scope-certification problem.

# 4. Hybrid Soundness Requires Two Proof Obligations

A Hybrid architecture must satisfy two distinct obligations.

They are related but not interchangeable.

## 4.1 Authority Non-Bypass

No component outside constitutional governance may acquire or exercise authority reserved to the constitutional domain without crossing the governed boundary.

This obligation concerns sovereignty.

It asks whether routine execution can become authoritative without adjudication.

The principle is:

> Influence may cross. Sovereignty may not.

A routine component may calculate, observe, propose, nominate, or supply evidence.

It may not unilaterally convert those activities into reserved authority.

## 4.2 Outcome Integrity

Authority non-bypass is necessary but insufficient.

A routine component may lack formal authority and still effectively determine the result of a constitutional decision.

Outcome integrity therefore asks a different question:

> Can a routine component control the conditions of a reserved decision so completely that the constitutional side retains formal authority but no meaningful independence over the result?

This is the distinction between authority and control.

Authority is the entitlement to decide or bind.

Control is the ability to constrain or reshape the decision environment so that the result becomes effectively determined.

The two are not identical.

A constitutional actor may retain authority while another actor controls the outcome.

This is the central reason Hybrid cannot be certified solely by proving that routine components lack reserved authority.

# 5. Authority Is Not Control

Consider a reserved dispatch decision.

Assume, for purposes of the example, that ordinary driver assignment has already been validly classified outside constitutional scope, while the reserved dispatch decision remains constitutional. The world-denial attack does not depend on proving that classification correct. It asks whether outcome integrity survives even after the partition is granted.

The constitutional side alone is authorized to make the reserved dispatch decision.

A routine subsystem has no authority over that reserved decision.

Suppose, however, that the routine subsystem legitimately assigns every available driver except Driver A to other ordinary tasks before the reserved dispatch decision occurs.

When the constitutional process begins, the world is accurately represented.

Only Driver A is available.

The constitutional process chooses Driver A freely, lawfully, and on true information.

Formal authority was preserved.

The outcome was nevertheless determined upstream.

No routine component seized the reserved dispatch authority.

No false state crossed a boundary.

No parameter was forged.

No unauthorized actuator fired.

If the routine domain can legitimately consume all alternatives but one through actions already certified as routine, the constitutional side may retain full authority while losing meaningful independence over the result.

This example exposes the limit of the slogan:

> Influence may cross. Sovereignty may not.

The slogan remains valid for authority non-bypass.

It is not sufficient for outcome integrity.

A sound Hybrid must therefore show both:

\[
\text{Authority Non-Bypass}
\]

and

\[
\text{Outcome Integrity}
\]

The second obligation is harder because control can be exercised through the surrounding decision environment rather than through the reserved decision itself.

# 6. Authority Non-Bypass and Dominated Paths

Authority non-bypass admits a comparatively clear structural formulation.

A routine domain may influence constitutional outcomes if every path by which that influence could acquire reserved authority crosses a non-bypassable constitutional boundary before authority is acquired.

Conceptually:

\[
\forall p \in Paths(R,A_c), \quad p \cap B \neq \varnothing
\]

where:

- \(R\) is the routine domain;
- \(A_c\) is reserved constitutional authority;
- \(B\) is the set of mandatory constitutional boundaries.

The routine domain need not be causally disconnected from the constitutional domain.

That would make useful composition impossible.

The requirement is that its influence be dominated by the constitutional cut before that influence becomes authoritative.

This principle is already implicit in the agent-substrate division of ORSR.

Agent reasoning affects what is proposed.

Yet reasoning does not bind state merely because it influenced a proposal.

The proposal crosses a governed boundary, after which the substrate independently resolves formation, standing, reachability, binding, continuation, and effect admission.

The reasoning is influential.

It is not sovereign.

A larger Hybrid attempts to generalize this structural property.

That generalization requires care.

Routine authority can leak through at least four positive software paths:

1. routine-authored state becomes authoritative constitutional input;
2. routine effect closure directly or compositionally reaches a reserved consequence;
3. routine routing or decomposition determines which constitutional decision is formed;
4. routine-authored parameters carry constitutionally decisive content into an otherwise confined capability.

These paths are not presented here as a complete universal taxonomy of all possible outcome control.

They are the principal positive routes by which routine-authored software influence can acquire reserved authority.

Closing them is necessary for authority non-bypass.

It is not sufficient for outcome integrity.

# 7. Outcome Integrity and the Limits of Enforcement

The forms below are not derived from first principles and are not claimed to be exhaustive. They are the outcome-control channels that remained after authority non-bypass was satisfied in the cases examined during this work.

A failure of outcome integrity can arise even when authority non-bypass is sound. The specific channels through which it arises are described here as forms of capture.

Three broad forms matter.

## 7.1 Input Capture

A routine component can control what the constitutional decision sees or may consider.

This can occur through:

- omission of an owed fact;
- selective disclosure of true facts;
- dependence on timing, ordering, existence, or other metadata not intended to carry constitutional meaning;
- admission of features the decision should not consider.

These attacks can survive perfect provenance.

Every fact presented may be authentic.

The manipulation may reside in the fact that was not presented, or in metadata that was never intended to become a decision variable.

A closed decision-input discipline can address this class.

The constitutional decision should operate over a positively specified input surface.

Required facts must be affirmatively satisfied.

Silence must not become consent or negative evidence unless silence itself has been constitutionally admitted as a signal.

Only admitted features should enter the adjudicative view.

Metadata needed for audit does not automatically become metadata the decision may use.

This is an enforcement problem.

## 7.2 Feasibility Capture

A routine component can alter which options or valid transitions remain available.

This can occur through:

- option depletion;
- resource exhaustion;
- world-denial;
- invalidation of a checked precondition before binding.

These attacks are not necessarily input defects.

The constitutional side may receive a complete and accurate representation of the world.

The problem is that the world has already been changed.

Protection against this class may require preservation of required options, resources, or preconditions across the decision interval.

The corpus does not currently define a general reservation or check-to-bind primitive for this purpose.

A concrete Hybrid that requires such protection cannot claim to have solved the problem merely by naming it.

This paper therefore treats the required protection as a certification condition, not as architecture defined here.

## 7.3 Valuation and Decision-Landscape Capture

The most difficult case arises when:

- all information is true and complete;
- all required options remain available;
- all preconditions remain valid;
- the constitutional process retains full formal authority;

yet the routine domain has changed the decision-relevant properties of the available options so that the constitutional decision predictably collapses toward one result.

A routine process may change:

- cost;
- quality;
- risk;
- urgency;
- expected utility;
- reliability;
- relative ranking.

This is not necessarily corruption.

It may be the routine domain doing useful work.

The difficulty is that the same variables the routine domain must legitimately manipulate may also be variables the constitutional decision uses.

The natural response is to protect every decision-relevant variable.

That response fails.

Almost every useful routine action changes some variable a future decision may consider.

Protecting every potentially decision-relevant variable recreates the original inclusion practice without an exclusion rule.

The routine domain collapses toward empty.

Outcome integrity therefore cannot, in general, be reduced to a rule that freezes everything capable of influencing a constitutional choice.

# 8. Decision-Rule Pivotality

The problem becomes clearer when the decision rule itself is examined.

Suppose a constitutional decision rule selects the lowest-risk eligible option.

Cost is declared constitutionally irrelevant and is left under routine control.

The decision rule then states:

> If two options have equal risk, choose the lower-cost option.

Cost was correctly excluded from the protected set under the claim that the constitution was indifferent to it.

Yet cost becomes decisive precisely in the tie region.

The routine domain can control cost and therefore control the result whenever risk ties.

Nothing about the variable itself changed.

The decision rule conferred pivotality upon it.

This yields an important result:

> **A scope-certification procedure that classifies protected variables alone is incomplete.**

An excluded variable can become constitutionally pivotal through:

- tie-breaks;
- defaults;
- fallback logic;
- threshold transitions;
- branch conditions;
- runtime scoping functions.

Pivotality is therefore not merely a property of a variable.

It is a property of a variable under the behavior of a decision procedure.

The relevant certification target is consequently not reducible to:

\[
P_D \subseteq X
\]

where \(P_D\) is a protected set and \(X\) is the set of decision-relevant variables.

The certification question must account for the relationship among at least:

\[
D,\ f,\ X,\ R
\]

where:

- \(D\) is the reserved decision;
- \(f\) is the decision procedure;
- \(X\) is its decision-relevant state;
- \(R\) is the routine-controlled domain.

The critical question is whether routine-controlled influence can become constitutionally pivotal under \(f\) without the required adjudication.

This paper does not define a formal certification predicate for that question.

It establishes that any sound scope-certification procedure must account for it.

# 9. The Scope-Certification Gap

The recurring problem across transitions, capabilities, effects, and decision dependencies is the same.

Enforcing a declared boundary is not the hardest part.

The hard part is justifying the boundary.

A sound scope-certification procedure would need to establish at least two properties.

First, completeness.

Everything requiring constitutional protection must be inside the certified scope.

Second, exclusion soundness.

The routine domain left outside must be shown not to violate the constitutional guarantee being claimed.

This second property is what distinguishes scope certification from ordinary inclusion.

It is not enough to show why a surface belongs inside.

The certification must justify why the remainder may remain outside.

The problem is complicated further by decision-rule behavior.

A surface or variable that appears outside scope under one static classification may become pivotal under the behavior of the rule that consumes it.

The certificate must therefore apply to the decision procedure and execution topology, not merely to a list of protected components.

This paper uses the term **scope certification** for that methodological requirement.

It does not define a `ScopeCertificate` runtime object.

No such object is introduced here.

The operative corpus currently contains no general procedure for producing such a certification.

# 10. The Bounded Negative Result

The bounded negative result of this paper is:

> **The operative corpus currently establishes no general scope-certification procedure, and the candidate procedures examined during this work do not generalize beyond restricted structural classes.**

This statement must not be strengthened into an impossibility theorem.

The paper does not establish that no general certification procedure can exist.

It establishes that none is currently present in the corpus and that several natural candidates fail to generalize.

The failures are structural.

Static transition classification fails because consequential significance can depend on path and composition.

Capability classification fails because the same capability can occupy different consequence classes depending on use.

Actuator classification fails because the same physical actuator can expose different authorized effect spaces.

Protected-variable classification fails because the decision rule can make an excluded variable pivotal.

Design-time scope classification can fail where decisiveness emerges only at runtime.

Per-decision analysis can fail to bound accumulated influence across a trajectory.

These are not isolated implementation mistakes.

They are recurring features of general agentic systems.

The result therefore shifts a burden.

A claim that Hybrid is justified must produce affirmative evidence that constitutional scope is certifiable for the application being designed.

Hybrid is not presumed safe merely because a plausible partition can be described.

> **Hybrid carries the proof burden.**

The bounded negative result does not close the possibility of future certification methods.

A later procedure that successfully handles composition, decision-rule pivotality, runtime context, and trajectory effects would advance the corpus rather than contradict this paper.

The present claim is only that no such general procedure is currently established.

# 11. Fail-Closed Architecture Selection

The absence of a general certification procedure does not make the selection doctrine unusable.

It makes the doctrine fail closed.

The process is:

## 11.1 No Constitutional Guarantee Required

If the application requires no reserved constitutional guarantee, ordinary execution is justified.

## 11.2 Constitutional Guarantee Required and Scope Certified

If constitutional guarantees are required and the application can affirmatively certify a non-empty routine domain outside constitutional scope, Hybrid becomes available.

The certificate must establish the relevant guarantee across the actual execution and decision topology.

A plausible partition is not enough.

## 11.3 Constitutional Guarantee Required and Scope Not Certified

Where constitutional guarantees are required and Hybrid has not been affirmatively certified, Full Constitutional Runtime is the required governance baseline.

This may occur because:

- certification has not been attempted;
- the required evidence is unavailable;
- the application exhibits runtime-emergent decisiveness;
- routine and constitutional paths are too entangled;
- the certification method cannot establish exclusion soundness;
- the application falls outside the structural class the available method can certify.

The reason does not change the selection result.

Failure to certify Hybrid removes Hybrid from the justified architecture set.

It does not weaken any constitutional guarantee.

That is the central safety property of the doctrine.

The penalty for certification failure is architectural overhead.

The penalty is not lost constitutional protection.

## 11.4 Fail-Closed Governance Baseline Versus Realized Sufficiency

Where constitutional guarantees have been authoritatively determined to be required and a narrower Hybrid boundary has not been affirmatively certified, Full Constitutional Runtime is the required governance baseline. This is a governance-selection result, not a proof that a conformant Full Constitutional Runtime can be successfully instantiated for every application or that every required guarantee has thereby been technically realized. If the required governance baseline cannot be validly implemented, the result is an unresolved feasibility or implementation condition; it is not authorization to reduce governance to an uncertified Hybrid or to Ordinary execution. The fail-closed claim therefore concerns the minimum justified governance regime, not universal sufficiency. It does not claim that Full Constitutional Runtime eliminates the residual outcome-control surfaces expressly left outside the present doctrine, including trajectory-level accumulation and human-mediated influence.

# 12. A Candidate Certifiable Class, Illustrative Only

The Hybrid branch should not be treated as presumptively available.

It also should not be treated as necessarily empty.

One restricted class appears capable, in principle, of supporting affirmative certification.

This paper presents the class as illustrative evidence only.

It does not claim to have constructed a certified Hybrid instance.

Consider a gate-then-optimize structure.

A constitutional process first resolves eligibility.

Only options that have satisfied the governed eligibility conditions enter the admissible set.

A routine process then optimizes among those options using variables over which the constitution is genuinely indifferent.

That indifference must hold across the entire admissible region.

It must also hold under:

- ties;
- defaults;
- fallback behavior;
- threshold branches.

Otherwise the decision rule can confer pivotality on a supposedly unprotected optimization variable.

The class also requires decisiveness to be statically characterizable rather than dependent on a runtime scoping computation controlled by routine input.

The evaluator implementing the reserved decision must itself remain constitutionally protected.

If those conditions could be fully established for a given application, the required separation would in principle leave a meaningful routine optimization domain while keeping constitutional eligibility and decision authority governed. Whether they can be established for any concrete application is exactly what this paper does not claim to have shown.

This is not a construction claim.

This paper does not establish that all of the architecture needed to instantiate such a Hybrid exists in the operative corpus.

A concrete implementation may require, among other things:

- temporal or reservation protection for preconditions and option availability;
- governed inter-partition boundary semantics beyond the current agent-substrate boundary apparatus.

Those are matters for a separate governed architecture workstream.

The purpose of this section is narrower.

It shows the shape of a restricted class for which affirmative certification appears plausible enough to keep the Hybrid branch from being merely rhetorical.

# 13. Limits of the Present Claim

The doctrine established here carries explicit boundaries.

## 13.1 Per-Decision, Not Per-Trajectory

The analysis of outcome integrity is primarily per-decision.

It does not establish trajectory-level integrity.

Routine influences that are individually acceptable may accumulate across a sequence of decisions and alter long-run outcome distributions.

This paper does not claim to bound that accumulation.

## 13.2 Runtime-Emergent Decisiveness

Where constitutional pivotality cannot be determined at design time and emerges only through runtime combinations of state, the present doctrine does not certify a dynamic scope-selection procedure.

It classifies the case as uncertified.

The fail-closed selection result is Full Constitutional Runtime.

This is a classification result, not a solution to runtime scope determination.

## 13.3 Human-Mediated Influence

The software Constitutional Runtime governs machine-mediated authority and effect paths.

A routine component may emit true, permitted information to a human who independently holds constitutional authority.

The selection, timing, or framing of that information may influence the human's decision.

This paper does not claim to govern that surface.

Human sovereign action informed by system outputs is a human-governance problem unless separately brought under an explicit governed protocol.

## 13.4 No General Impossibility Claim

The absence of a general certification procedure in the operative corpus is not evidence that no such procedure can ever exist.

This paper does not make that claim.

# 14. Relationship to the CRC Corpus

This paper is upstream of the runtime architecture defined elsewhere in the corpus.

It does not modify that runtime architecture.

It establishes the prior architecture-selection determination the runtime architecture otherwise assumes.

Invariant I1 remains intact.

All consequential transitions remain subject to complete mediation.

Nothing in this paper creates a class of consequential transition that may bypass mediation.

A certified Hybrid would not weaken complete mediation.

It would establish that a non-empty routine domain satisfies the relevant exclusion conditions while reserved constitutional transitions remain within the governed domain.

The paper defines no shared runtime object.

It consumes no [CRC-SSR](../shared-schema-registry-v1.6.md) object.

It references [Core](../constitutional-runtime-computation-v5.14.md), [Boundary Contracts](../companions/constitutional-boundary-contracts-v1.3.md), the [actuation and effect-admission apparatus](../companions/constitutional-actuation-and-effect-admission-v1.0.md), and the [standing and continuation apparatus](../companions/constitutional-standing-v1.7.md) as evidence that the corpus already possesses governed boundaries, binding discipline, and effect-admission mechanisms.

It does not validate, subtype, extend, or amend their schemas.

The paper therefore creates no CRC-SSR impact in its present form.

The requirement for affirmative scope certification is established here as doctrine.

It is not instantiated as a runtime `ScopeCertificate` object.

Likewise, the requirement that certification account for pivotality induced by the decision procedure is a doctrinal requirement.

It is not defined here as an operational predicate or registry object.

The paper also declares limitations concerning runtime-emergent scope and trajectory effects.

Those limitations are not open architecture dependencies of the doctrine established here.

They are explicit boundaries on its claim.

# 15. Conclusion

The CRC corpus knew how to govern a Constitutional Runtime before it had a general doctrine for deciding when one was warranted.

This paper supplies that upstream selection doctrine.

The choice among ordinary execution, Hybrid architecture, and Full Constitutional Runtime proceeds in two stages.

Whether constitutional guarantees are required is supplied as a prior sovereign determination, authored by the constitutional principal and not computed by the system being evaluated.

Where guarantees are not required, ordinary execution is eligible.

Where guarantees are required, affirmative scope certification distinguishes Hybrid eligibility from the Full Constitutional Runtime governance baseline.

Hybrid is available only where constitutional scope can be affirmatively certified while preserving a non-empty routine domain.

Where constitutional guarantees are required and no narrower Hybrid boundary has been affirmatively certified, Full Constitutional Runtime is the required governance baseline.

The doctrine therefore places the burden where it belongs.

> **Hybrid carries the proof burden.**

The paper further establishes that the operative corpus currently provides no general scope-certification procedure and that the candidate procedures examined fail to generalize beyond restricted structural classes.

That result is bounded.

It is not an impossibility theorem.

The deepest reason a static scope classification is insufficient is that constitutional pivotality can emerge from path composition and from the behavior of the decision procedure itself.

A variable or capability that appears nonconstitutional in isolation can become decisive through a tie-break, default, runtime branch, or composed effect path.

Scope certification must therefore justify the behavior of the relevant decision and execution topology, not merely classify a set of parts.

The Hybrid branch remains conditionally available.

A restricted gate-then-optimize class illustrates one structure in which affirmative certification may be possible, but this paper does not claim a completed construction.

The construction of a certified Hybrid is separate work.

The result established here is the selection rule that tells a builder when such work is justified.

Failure to certify a narrower Hybrid boundary is not failure of the architecture-selection process.

Where constitutional guarantees have been authoritatively determined to be required, the absence of an affirmative Hybrid certification leaves Full Constitutional Runtime as the required governance baseline.

This is a governance-selection result, not proof of successful implementation or realized guarantee satisfaction.
