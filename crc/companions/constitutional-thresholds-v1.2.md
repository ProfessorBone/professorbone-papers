# Constitutional Thresholds: Trigger Authority, Decision Boundaries, and Evidence-Packet Provenance in Governed Drift Monitoring

## Why the Decision Boundary and the Evidence Path Are Constitutional Objects

### v1.2 Conceptual Architecture Paper, Companion 5 to Constitutional Runtime Computation v5.4; closure of the threshold-authority and evidence-packet-provenance residues named in Constitutional Baselines v1.2 and Constitutional Coherence v1.2

**Clarence "Faheem" Downs (Professor Bone Lab)**

*Licensed under CC BY 4.0.*

---

# Abstract

The fourth companion, Constitutional Coherence v1.2, closed the cross-surface coherence dependency and, in doing so, named two adjacent residues it deliberately did not govern. Both trace back further, to Constitutional Baselines v1.2, which first distinguished four objects that the corpus had been treating as one: the baseline, the reference standard; the metric, the measurement calculus that computes deviation from it; the threshold, the decision boundary at which a measured deviation triggers action; and the trigger, the condition that fires escalation or surfacing when the threshold is crossed. Baselines governed the first object completely. Coherence governed the relation among baselines across surfaces. Neither governs the threshold or the trigger, and neither governs the evidence packet through which the sovereign decides whether to move any of these objects at all.

This paper closes both residues. The central observation is that a baseline can remain sovereign-anchored, a metric can measure honestly, and a generation can be perfectly coherent, while the decision boundary at which a measured deviation converts into action is quietly raised until real drift no longer crosses it. This is not baseline capture, because the standard is intact. It is not family incoherence, because the relation among standards is sound. It is a third and distinct failure, on a third axis: baseline capture corrupts the standard being measured against (the vertical axis), family incoherence corrupts the relation among standards (the horizontal axis), and threshold capture corrupts the response function that converts an honest measurement into governed action (the decision axis, orthogonal to both). From this a principle follows rather than is asserted: the **Trigger Authority Principle**. Whoever can move the threshold or the trigger controls whether a measured deviation ever produces action, independent of whether the baseline or the metric is honest. Therefore threshold and trigger authority must be sovereign, the threshold must be independent of the monitored process, an authorized sensitivity adjustment must be distinguished from threshold drift, and a threshold or trigger change must be a typed, traced sovereign reconstitution act.

The second residue is the evidence-packet-provenance problem behind mediated capture, which Baselines named as a subtype of baseline capture and Coherence elevated to a deployment precondition without governing. The sovereign who re-anchors a baseline, re-coheres a generation, or resolves a threshold change decides on a briefing. If that briefing is generated from the monitored surfaces and can be shaped by them, the sovereign is captured one step removed, through the human interface, and no structural conjunct in the prior four companions catches it. This paper discharges the mechanically detectable form of that precondition by extending the boundary-contract framework Companion 0 explicitly reserved for this purpose: the **EvidencePacketContract** governs the evidence-packet-to-sovereign crossing with a schema, a validation predicate, a typed violation taxonomy mapped onto Companion 0's B0 through B5 severity classes, a tamper-evident audit record, and an escalation rule, validated by a constitutionally separated PacketValidationFunction so that the entity that briefs the sovereign is never the entity that certifies the briefing. A deeper form of mediated capture, in which no component's independence claim is false but the packet's evidentiary sufficiency or candidate selection is itself narrowed, is named rather than closed (Parts VI and Open Problems).

The contribution is fivefold. First, the four-object distinction (baseline, metric, threshold, trigger) made precise and the Trigger Authority Principle derived through a step chain from the corpus rather than asserted. Second, two predicates in the parent's CTLC notation, ThresholdChangeReachable (the dangerous operation, with SensitivityGrounded as its load-bearing, undecidable conjunct) and ThresholdPinAdmissible (the routine operation), together with the decision of how a threshold joins the existing BaselineGeneration rather than requiring a new generation-level object. Third, the EvidencePacketContract, extending Companion 0's boundary-contract pattern to the evidence-packet-to-sovereign crossing that paper explicitly reserved as future work, with the PacketValidationFunction as its constitutionally separated validator. Fourth, a family of threshold-specific primitive failure topologies (P_thr), with threshold capture traced end to end and Cumulative Threshold Creep classified as the corpus's third sovereign-terminal primitive, after P_base5 and P_coh3. Fifth, the placement of the cross-surface threshold seam that Coherence v1.2 named within the BaselineGeneration, with the structural half specified and the full non-masking extension left as an explicit open problem rather than claimed resolved, and an honest account of the regress this paper's own reliance on sovereign judgment creates, since the sovereign now decides on evidence whose integrity is itself constitutionally dependent. AEGIS serves as the worked domain. Nafisah remains the sovereign principal, Mantis the clinical reasoning agent, MEC the L2 monitor, Pepper the orchestrator.

---

## Contents

**Part I** The threshold-authority and evidence-packet residues, and the Trigger Authority Principle
**Part II** The four objects: baseline, metric, threshold, trigger
**Part III** The threshold predicate (ThresholdChangeReachable and ThresholdPinAdmissible)
**Part IV** The EvidencePacketContract: the evidence-packet-to-sovereign crossing
**Part V** Threshold capture as the third axis, and the regress the evidence path creates
**Part VI** Primitive failure topologies specific to thresholds (P_thr)
**Part VII** Worked example: two failures in AEGIS
**Part VIII** Who governs the threshold and the evidence path?
**Part IX** Relationship to the companion series
**Part X** Related work
**Open problems** (extending the parent's Section 19 and the four companions' sets)

---

# Part I. The Threshold-Authority and Evidence-Packet Residues, and the Trigger Authority Principle

Baselines v1.2 closed the per-surface baseline-authority dependency and, in its open problems, named the residue this paper closes: a doctrine-grounded baseline can be paired with a captured threshold, so the standard stays anchored, the metric measures honestly, and the threshold is quietly raised until real drift no longer crosses it, with monitoring going dark without the baseline moving at all. Coherence v1.2 inherited the same residue at the family level, restated it at full strength, and scoped it out on an explicit axis argument: threshold capture is a vertical failure on a single surface, family incoherence is a horizontal failure across surfaces, and the two share no mechanism, so folding threshold governance into a cross-surface coherence paper would have added a second, orthogonal contribution that paper could not complete to the corpus standard. Coherence named the narrow seam where the two genuinely touch, the cross-surface threshold, and pointed both residues here.

The accounting is exact, in the manner of the prior two companions.

| Object the corpus depends on | What governs it |
|---|---|
| The baseline (the standard) | BaselineChangeReachable, BaselinePinAdmissible (Companion 3) |
| The relation among baselines (the family) | GenerationCoherenceReachable, GenerationPinAdmissible (Companion 4) |
| The metric (deviation calculus) | Named, inherited unresolved, the measurement-calculus problem |
| The threshold (the decision boundary) | Nothing, until this paper |
| The trigger (the firing condition) | Nothing, until this paper |
| The evidence packet (what the sovereign decides on) | Nothing, until this paper |

The covered rows govern the standard and the relation among standards. The uncovered rows govern what converts a measured deviation into action, and what the sovereign sees when deciding whether to authorize that conversion. This paper adds no new baseline gate and no new coherence gate. It governs the two objects the prior gates cannot reach, because a gate scoped to the standard or to the relation among standards has no standing over the decision boundary or the evidence the sovereign reads.

## The Trigger Authority Principle, derived

The necessity here is not asserted. It follows from facts the corpus already establishes, in six steps, in the manner of the Baseline Sovereignty Principle's and the Generation Coherence Principle's derivations.

1. Every L2 drift detector in the corpus produces a measured deviation from a baseline. Baselines and Coherence establish this completely: a metric computes divergence, and the divergence is compared against some decision boundary before anything happens.

2. A measured deviation produces action only if it crosses a threshold and fires a trigger. Detection is not action. A metric can report a large deviation that nonetheless never escalates, if the boundary at which deviation converts to escalation has been set high enough. Action, in this architecture, is not a property of the measurement. It is a property of the measurement composed with the decision boundary.

3. Therefore whoever can move the threshold controls whether a measured deviation ever produces action, independent of whether the baseline or the metric is honest. This is the central fact of the paper. A baseline that has not moved and a metric that reports faithfully can sit behind a threshold that has been raised until the honestly reported deviation no longer crosses it. The monitor is not blind. It is deaf to what it sees.

4. If the monitored process can move its own threshold, it controls whether its own drift is ever acted on, without needing to touch the standard it is measured against. This is a distinct capture path from baseline capture, and it is structurally cheaper for an adversarial or drifting process to exploit, because moving a decision boundary draws less scrutiny than moving a standard. Baseline capture requires corrupting what is measured against. Threshold capture requires only raising the bar for caring about the result.

5. If the monitor sets its own threshold, it self-certifies not its standard but its willingness to act on what the standard reveals, which is the Section 7 self-certification collapse applied to the decision layer rather than the measurement layer. A monitor that can quietly raise its own alarm threshold is functionally indistinguishable from a monitor that has been captured, even while every measurement it reports remains true.

6. The distinction between an authorized sensitivity adjustment, a genuine doctrinal judgment that the operative alarm threshold should change, and drift-laundering of the decision boundary, a quiet raising of the bar to avoid firing on real deviation, is the same sovereign-only judgment the corpus already routes to Nafisah for baselines and generations. The two are structurally identical at the level of a single threshold change: both move a number, both can be defended with a plausible rationale, and only the sovereign can say which one occurred.

**The Trigger Authority Principle.** The threshold and the trigger are constitutional objects distinct from the baseline and the metric. Whoever can move the threshold or the trigger controls whether a measured deviation ever produces action. Therefore trigger authority must reside in the sovereign, the threshold must be independent of the monitored process, an authorized sensitivity adjustment must be distinguished from threshold drift by a typed, evidenced judgment, and a threshold or trigger change must be a distinct, typed, traced sovereign reconstitution act.

The Principle stands in a precise relation to its two predecessors, and the relation is what keeps this paper from restating either one. The Baseline Sovereignty Principle vests authority over the standard in the sovereign. The Generation Coherence Principle vests authority over the relation among standards in the sovereign. The Trigger Authority Principle vests authority over the response function, the mapping from an honestly measured deviation to governed action, in the sovereign. None of the three predicates evaluates what either of the others evaluates. BaselineChangeReachable never asks whether a threshold has moved. GenerationCoherenceReachable never asks whether one surface's deviation still fires. ThresholdChangeReachable, defined in Part III, never re-adjudicates whether the baseline is honest or the family is coherent; it takes both as given and asks only whether the boundary that converts their honest output into action has itself been captured.

---

# Part II. The Four Objects: Baseline, Metric, Threshold, Trigger

Baselines v1.2 named the four-object distinction and did not govern three of them. This part makes the distinction precise enough to support predicates.

**The baseline** is the reference standard, governed completely by Companion 3: identity and scope, anchored doctrinal source, version and predecessor, pinning discipline, and independence from the process it measures.

**The metric** is the measurement calculus that computes a deviation signal from the pinned baseline and the current state of the monitored surface. The corpus has consistently named the metric and consistently deferred it as the measurement-calculus problem, first in Baselines, restated in Coherence, and restated here. This paper does not close it. The metric produces a number or a distribution of divergence; what happens to that number is this paper's subject.

**The threshold** is the decision boundary applied to the metric's output: the value or condition at which a measured deviation is classified as requiring a response. A threshold is not the metric. Two systems can share an identical, honestly computed deviation metric and differ entirely in whether that deviation ever produces action, because they differ in where the threshold sits. A threshold has its own identity, its own version, its own anchored doctrinal source (the sovereign's judgment about what magnitude of deviation is tolerable before response is required), and, critically, its own independence requirement: a threshold derivable from, or movable by, the process it gates is no threshold, for exactly the reason a baseline derivable from its monitored distribution is no baseline.

**The trigger** is the condition, evaluated against the threshold, that fires a governed response, escalation to the sovereign, surfacing to lineage review, or a hold. A trigger is distinct from a threshold in the same way a transition type is distinct from a capability affordance in the parent's boundary-contract vocabulary: the threshold sets the boundary, and the trigger is the typed act of crossing it that the substrate must recognize and route. A threshold can be correctly set and a trigger can nonetheless fail to fire, if the trigger's own definition has narrowed, if it no longer evaluates the surfaces it once did, or if it routes to the wrong authority. This is a distinct failure mode from threshold capture, traced separately in Part VI as P_thr2.

Trigger definitions carry three properties this paper fixes. **Scope**: which surface, generation, or cross-surface relation the trigger evaluates. **Routing**: which authority the trigger escalates to when it fires, defaulting to the sovereign and never to the monitored process or its monitor. **Firing condition grammar**: the trigger's evaluated condition, which may be a single-surface threshold crossing, a compound condition across surfaces (the cross-surface trigger this paper's Part V connects to the coherence apparatus), or a rate-based condition (a threshold crossed more than a set number of times within a window, mirroring the change-count trigger classes Baselines and Coherence already use for lineage surfacing).

A **ThresholdSet** is the object that carries the fields a threshold and its trigger require for one surface. Fixing its status as a constitutional object, versioned and pinned exactly as a Baseline is, requires more than the four descriptive fields named above. A threshold cannot be evaluated in isolation from the metric it gates, and a pin that checks only version, scope, and log completeness can still pin a threshold that is meaningless for the metric output it is compared against. The full schema is:

| Field | Type | Function |
|---|---|---|
| `threshold_id` | UUID | Identity, distinct from the value it currently holds |
| `threshold_value_or_condition` | Numeric or ConditionExpr | The decision boundary itself |
| `doctrinal_source_ref` | UUID | The anchored source, mirroring the Baseline's anchored doctrinal source |
| `metric_ref` | UUID | The specific metric this threshold is evaluated against; a threshold with no declared metric interface cannot be shown meaningful |
| `metric_output_type` | MetricOutputTypeRef | The shape of output the threshold expects (scalar deviation, distribution, rate) |
| `comparison_operator` | Enum | Exceeds, falls below, departs from a band, or a compound condition |
| `directionality` | Enum | Whether the threshold guards deviation increasing, decreasing, or either |
| `evaluation_window` | Duration | The window over which the metric is evaluated before comparison |
| `severity_class` | SeverityRef | The response severity a crossing produces |
| `response_type` | ResponseTypeRef | Escalate, surface to lineage review, or hold |
| `trigger_route` | AuthorityRef | The authority the trigger escalates to, defaulting to the sovereign |
| `null_or_missing_metric_behavior` | Enum | What the trigger does when the metric cannot be computed for the window; defaults to escalation, never to silent non-firing |
| `counterfactual_replay_policy` | PolicyRef | The declared method by which the Threshold Trajectory Audit (Part VI) may replay historical metric output against a predecessor threshold |
| `independence_property` | IndependenceCertRef | The declared basis for IndependentOfMonitored (Part III) |

The `metric_ref` and `metric_output_type` fields do not solve the measurement-calculus problem this paper inherits and leaves open. They bind the threshold to declare what kind of metric output it expects, which is a condition on threshold admissibility, not a specification of how the metric computes that output. A threshold declaring no metric interface cannot be shown meaningful for what it gates, and ThresholdPinAdmissible (Part III) is defined below to check for exactly this.

## Where the threshold joins the generation

Coherence v1.2 named the cross-surface threshold as the seam where threshold governance and coherence governance touch: a single trigger condition defined over more than one surface, or a threshold whose authorized level on one surface depends on the standard set on another. This paper resolves the design question Coherence left open, whether thresholds need their own generation-level object or join the existing BaselineGeneration, in favor of the latter, but only as a scoped extension: this paper does not retroactively redefine every existing BaselineGeneration as a threshold-bearing object. A generation acquires a ThresholdSet-bearing member only where a surface within its span is under this paper's threshold governance, declared explicitly at establishment or by an amendment extending the generation's span. A surface with no declared ThresholdSet keeps a baseline-only member, exactly as Coherence originally specified.

Formally, a generation's per-surface member becomes:

```
GenerationMember :=
  surface_id
  baseline_version
  threshold_set_version   (optional; present only for threshold-governed surfaces)
```

This changes two of Coherence's predicates, and the change is carried through here rather than left as an unexamined consequence of the folding argument, because a reviewer cannot be asked to infer a formal update from a design choice alone.

```
GenerationPinAdmissible(γ) ⟺
  GenerationVersionPinned(γ)     ∧
  MembersFromOneGeneration(γ)    ∧
  BaselinePinsAdmissible(γ)      ∧
  ThresholdPinsAdmissible(γ)     ∧
  DeclaredConditionsHold(γ)      ∧
  PinLogged(γ)
```

`BaselinePinsAdmissible(γ)` is Coherence's original per-member baseline pin check, renamed only to distinguish it from its threshold-side sibling. `ThresholdPinsAdmissible(γ)` requires that every threshold-bearing member's ThresholdPinAdmissible (Part III) holds, and is vacuously true for a generation with no threshold-bearing members, so the extension imposes no obligation on a generation that has not opted into threshold governance.

```
GenerationCoherenceReachable(γ) ⟺
  MembersValid(γ)                 ∧
  DoctrineConsistent(γ)           ∧
  CrossSurfaceConsistent(γ)       ∧
  NoSurfaceMasksAnother(γ)        ∧
  ThresholdRelationsCoherent(γ)   ∧
  SovereignAuthorized(γ)          ∧
  GenerationVersioned(γ)          ∧
  ChangeLogged(γ)
```

`ThresholdRelationsCoherent(γ)` is the conjunct this paper adds to Coherence's predicate. It does not re-adjudicate every member threshold on every generation use, which would make routine generation pinning as expensive as a fresh threshold amendment and would be conceptually recursive, since a generation is read far more often than a threshold is changed. It holds when, for every threshold-bearing member, the member's ThresholdSet descends from a prior valid ThresholdChangeReachable event, that is, its current version traces to a change that already passed the gate, rather than the gate being re-run live, and no declared cross-surface relation between two threshold-bearing members' ThresholdSets is violated under the current generation. Only at generation establishment, amendment, or partial update does a fresh ThresholdChangeReachable evaluation apply to a newly proposed member, exactly as MembersValid imports the per-surface baseline result rather than re-deriving it. This is the structural half of P_thr4 (Part VI): decidable to the extent the CoherenceConditionSet has been extended with threshold-mediated conditions, and vacuously true, exactly as MembersValid would be, for a generation with no threshold-bearing members. It establishes generation-level visibility of threshold relations; it does not, by itself, extend NoSurfaceMasksAnother's open non-masking judgment to read the paired ThresholdSet, and it does not by itself complete the non-masking judgment required for cross-surface threshold masking. That extension, and the accompanying sixth masking-manner value the CrossSurfaceMaskingAnalysis would need, remains a distinct, named open problem below, because completing it is Coherence's own apparatus applied to a new field, not a change this paper is positioned to make to a predicate it does not own. What this paper commits to, and formally carries through, is narrower: the generation object declares the threshold, the pin and change predicates check it, and the seam where the two apparatuses would fully merge is named precisely rather than left as an implicit consequence of the folding decision.

---

# Part III. The Threshold Predicate

This is the paper's first formal contribution. The thesis is that a threshold or trigger change is a governed constitutional transition distinct from a baseline change, and the formal object must govern the decision boundary, not re-describe baseline authority with threshold substituted for baseline. If the apparatus below found itself re-deriving BaselineChangeReachable, it would have failed to close the gap the corpus named, because BaselineChangeReachable governs the standard and this paper governs the response function applied to the standard's honest output.

Two predicates are needed, mirroring the two-grade typology every prior companion establishes: pinning a threshold to evaluate a trigger is routine and frequent; establishing or amending a threshold or trigger is dangerous and rare.

## The pinning predicate

```
ThresholdPinAdmissible(θ) ⟺
  VersionPinned(θ) ∧ ScopeMatched(θ) ∧ MetricInterfaceMatched(θ) ∧ GenerationPairMatched(θ) ∧ PinLogged(θ)
```

- **VersionPinned(θ):** the trigger evaluation names a specific, existing ThresholdSet version, not a live or unversioned reference, mirroring the baseline pin's namesake conjunct exactly.

- **ScopeMatched(θ):** the pinned ThresholdSet serves the surface, or the declared cross-surface relation, being evaluated. Scope alone does not carry the generation-consistency burden in this version; that burden is separated into its own conjunct below, so that a scope match and a generation match can fail independently and be diagnosed independently.

- **MetricInterfaceMatched(θ):** the metric value being evaluated conforms to the ThresholdSet's declared `metric_ref` and `metric_output_type` (Part II). A threshold correctly versioned and correctly scoped can still be evaluated against a metric output it was never declared to gate, for instance a scalar threshold compared against a distributional output by an ad hoc coercion. MetricInterfaceMatched fails such a comparison rather than allowing a coerced evaluation to silently proceed, and it is what makes ThresholdPinAdmissible more than a version-and-scope check: it is a floor on the threshold being meaningful for what it gates, without requiring this paper to specify how the metric computes that output.

- **GenerationPairMatched(θ):** the pinned ThresholdSet belongs to the same generation as the baseline version the metric was computed against. A trigger evaluated with a threshold drawn from a different generation than the metric it gates is a version-skew failure of the same character as P_base4, now at the response layer, and separating it from ScopeMatched keeps a scope failure (wrong surface) diagnosable apart from a generation-skew failure (right surface, wrong generation).

- **PinLogged(θ):** the pin is recorded with the surface, the ThresholdSet version, the metric value evaluated, the trigger outcome (fired or not fired), and the detector version, so that any non-firing can be replayed and audited exactly as a drift signal can.

A trigger evaluation is, by default, ExecutableByRequester: the monitor pins a threshold version and evaluates the metric against it without escalation, on every measurement cycle. This is the routine operation, and it must remain cheap, because it runs as often as the metric itself is computed.

## The change predicate

```
ThresholdChangeReachable(θ) ⟺
  SovereignAuthorized(θ)      ∧
  SensitivityGrounded(θ)      ∧
  IndependentOfMonitored(θ)   ∧
  ChangeTyped(θ)              ∧
  VersionedSuccession(θ)      ∧
  ChangeLogged(θ)
```

- **SovereignAuthorized(θ):** the change traces to sovereign authorization, not to the monitored process, the monitor, or an automated re-calibration routine. This conjunct forbids self-adjustment on both sides, exactly as BaselineChangeReachable's namesake conjunct does: the monitored process cannot raise its own alarm threshold, and the monitor cannot lower its own sensitivity to avoid firing on drift it would otherwise report honestly.

- **SensitivityGrounded(θ):** the load-bearing conjunct, and the one that makes this predicate not a restatement of BaselineChangeReachable. The new threshold or trigger definition traces to a genuine, doctrine-authorized judgment about acceptable response sensitivity, not to a laundering of the decision boundary undertaken to stop the monitor from firing on real deviation. This is the exact structural analogue of DoctrineGrounded at the baseline: DoctrineGrounded asks whether the new standard traces to doctrine rather than to the drifted distribution it would otherwise measure; SensitivityGrounded asks whether the new decision boundary traces to a doctrinal judgment about tolerable deviation rather than to the observed decline in firing rate that a captured threshold would produce. The two conjuncts guard adjacent but distinct failures: DoctrineGrounded prevents the standard from being redefined to match what is currently observed; SensitivityGrounded prevents the boundary for acting on the standard's honest output from being redefined to stop acting on what is currently observed. A threshold change whose only honest justification is "the trigger has been firing too often lately" is laundering, exactly as a baseline change whose only honest justification is "the system has been behaving this way lately" is laundering.

  The evidentiary object that exposes the failure is the **SensitivityGroundingRecord**, mirroring the DoctrineGroundingRecord's discipline and carrying:

  | Field | Function |
  |---|---|
  | `sensitivity_record_id` | Identity |
  | `threshold_set_ref` | The ThresholdSet this record grounds |
  | `old_threshold_ref` and `new_threshold_ref` | The predecessor and successor decision boundary |
  | `decision_type` | Establish, amend, retire, or emergency tightening |
  | `doctrinal_source_refs` | The doctrinal basis for the new sensitivity level |
  | `change_type` | The enumerated kind, matching ChangeTyped below |
  | `affected_surface_or_relation` | The surface or cross-surface relation the change touches |
  | `expected_effect_on_firing_rate` | The change's declared, anticipated effect on how often the trigger fires |
  | `reason_current_firing_rate_is_not_grounding_source` | The field that does the work: the honest reason the observed firing rate is not what motivated the change |
  | `counterfactual_review_required` | Whether the Threshold Trajectory Audit (Part VI) must replay history against this change before it takes effect |
  | `sovereign_authorization_ref` | The authorizing Resolution |

  The `expected_effect_on_firing_rate` field matters precisely because it is not a red flag on its own: a threshold change made for genuine doctrinal reasons will often, and legitimately, change the firing rate. A statutory narrowing of what counts as reportable should reduce escalations; a statutory broadening should increase them. The constitutional question SensitivityGrounded asks is not whether the firing rate changes, but whether the *firing rate itself* is the hidden ground of the change, the thing the record's reason field must honestly rule out. Declaring the expected effect alongside the reason it is not the ground is what lets an auditor tell an honest, effect-anticipating change from a change that conceals its true motivation behind a plausible doctrinal gloss. SensitivityGrounded does not make the underlying judgment mechanically decidable; it makes it auditable, in exactly the sense Baselines states for DoctrineGrounded: the record provides auditability of the sovereign's grounding judgment, not mechanical proof that the new sensitivity level is correct.

- **IndependentOfMonitored(θ):** the new threshold is not a function of, and cannot be moved by, the process it gates. This decomposes into the same four subchecks Baselines defines for a baseline's independence, applied to the ThresholdSet: NotDerivedFromMonitored, NoAutomatedRecalibrationFromMeasuredState (no routine quietly raises the threshold when the trigger has been firing, which is the threshold-specific form of the automated-reanchoring failure), NoFeedbackPathFromMonitorToThreshold, and DependencyGraphClear.

- **ChangeTyped(θ):** the change is typed as one of an enumerated set of authorized change kinds, distinguished from drift, with a recorded rationale, mirroring ChangeTyped at the baseline. Types include authorized sensitivity recalibration, statutory or clinical-standard update to acceptable deviation tolerance, correction of a prior threshold error, trigger-routing correction, emergency tightening after a confirmed incident, and rollback after capture. The enumerated type, not merely the fact of authorization, is what makes the SensitivityGrounded judgment a recorded act rather than an implicit one.

- **VersionedSuccession(θ):** the new ThresholdSet records its predecessor, declares its migration effect on in-flight trigger evaluations, and is a clean versioned successor with no in-place mutation, exactly as a baseline change requires.

- **ChangeLogged(θ):** the change is traced distinctly from a routine trigger evaluation, in the governance exposure log, as a threshold reconstitution event referencing its SensitivityGroundingRecord and its predecessor ThresholdSet explicitly.

## The verdict structure

The two predicates compose with executability using the corpus authority statuses, exactly as every prior companion's predicates do.

| Operation | Predicate | Executability | Verdict |
|---|---|---|---|
| Trigger evaluation (pin) | ThresholdPinAdmissible | ExecutableByRequester | **Emit** |
| Establish or amend threshold or trigger | ThresholdChangeReachable | not executable by requester; SovereignAuthorizationRequired | **Escalate(target = Nafisah)** |
| Pin (any conjunct false) | ThresholdPinAdmissible | any | **Hold(cause)** |
| Change (any conjunct false) | ThresholdChangeReachable | any | **Hold(cause): P_thr1 or P_thr2** |

There is no PreAuthorizedClassExecutable path for a threshold or trigger change, for the same reason none exists for a baseline amend or a generation amend: a delegated threshold-change class would be a standing delegation of judgment over whether the system responds to what it measures, which the Principle forbids. A scheduled activation of a previously sovereign-authorized successor ThresholdSet, on an authorized effective condition, is substrate-executable exactly as a scheduled baseline activation is, because the sensitivity judgment it executes was made in advance rather than at runtime.

## Note on decidability

VersionPinned, ScopeMatched, PinLogged, ChangeTyped, VersionedSuccession, and ChangeLogged are mechanically decidable over the ThresholdSet's version record and the governance log. SovereignAuthorized is decidable over the authority graph. IndependentOfMonitored is decidable in its structural form and may resist algorithmic evaluation in its deep form, exactly as at the baseline. SensitivityGrounded is the undecidable conjunct, for the identical reason DoctrineGrounded is undecidable: whether a new decision boundary genuinely reflects a doctrinal sensitivity judgment rather than a laundering of the firing rate is a judgment that binds doctrinal content and resists mechanical evaluation. Where it cannot be conclusively evaluated, the change routes to escalation, which is the region in which sovereignty over the response function becomes necessary.

**Figure 1. The two threshold predicates and their verdict paths**

```mermaid
flowchart TB
    OP["Threshold or trigger operation proposal\n(operation type · target surface · ThresholdSet version)"]

    Q{"Operation class?"}
    OP --> Q

    PIN["ThresholdPinAdmissible (L1, routine)\nVersionPinned ∧ ScopeMatched ∧ MetricInterfaceMatched\n∧ GenerationPairMatched ∧ PinLogged\nruns every measurement cycle"]
    CHG["ThresholdChangeReachable (the dangerous operation)\nSovereignAuthorized ∧ SensitivityGrounded\n∧ IndependentOfMonitored ∧ ChangeTyped\n∧ VersionedSuccession ∧ ChangeLogged"]

    Q -->|"trigger evaluation"| PIN
    Q -->|"establish · amend"| CHG

    EMIT["Emit\ntrigger evaluated against pinned threshold\nfires or does not fire, both logged"]
    ESC["Escalate(Nafisah)\nchange reachable · SovereignAuthorizationRequired\n(default for every threshold or trigger amend)"]
    HOLD["Hold\nany conjunct false\n(P_thr1 capture · P_thr2 trigger drift\n· skew · unlogged mutation)"]

    PIN -->|"all hold"| EMIT
    PIN -->|"any false"| HOLD
    CHG -->|"all hold · sovereign route"| ESC
    CHG -->|"any false, esp. SensitivityGrounded"| HOLD

    style OP fill:#E6F1FB,stroke:#185FA5,color:#042C53
    style Q fill:#EEEDFE,stroke:#534AB7,color:#26215C
    style PIN fill:#E6F1FB,stroke:#185FA5,color:#042C53
    style CHG fill:#EEEDFE,stroke:#534AB7,color:#26215C
    style EMIT fill:#EAF3DE,stroke:#3B6D11,color:#173404
    style ESC fill:#FAEEDA,stroke:#BA7517,color:#412402
    style HOLD fill:#FCEBEB,stroke:#A32D2D,color:#501313
```

*A trigger evaluation is routine and emits, whether or not it fires; both outcomes are logged. A threshold or trigger amend is a reconstitution of the response function and escalates to the sovereign by default. SensitivityGrounded is the load-bearing conjunct: it holds when the new decision boundary traces to a doctrinal sensitivity judgment and fails when it traces to the declining firing rate the captured threshold would produce.*


---

# Part IV. The EvidencePacketContract: The Evidence-Packet-to-Sovereign Crossing

This is the paper's second formal contribution, and it is the one that discharges the deployment precondition Coherence v1.2 named at full strength: GenerationCoherenceReachable assumes the sovereign-facing evidence packet is not itself captured, and that assumption sat outside every paper's apparatus until now.

## Why this is a boundary contract, not a new invention

Companion 0 established the boundary-contract pattern, schema, validation predicate, typed violation taxonomy mapped to severity classes, a constitutionally separated validator, an audit record, and an escalation rule, for the two primary crossings in the core ORSR loop. It explicitly named the crossings it did not govern, including, verbatim, "evidence packet to sovereign, baseline and generation lineage to sovereign," as governed crossing surfaces future work may extend the pattern to, and it fixed the generalization discipline for doing so: inherit the six components, but not necessarily the exact BoundaryValidationFunction implementation, because a sovereign-facing evidence packet may require a validator with different authority positioning than the agent-substrate BVF. This paper is that extension, at the exact crossing Companion 0 named.

The evidence packet is the typed object presented to the sovereign whenever a threshold change, a baseline change, or a generation change requires her authorization: the SensitivityGroundingRecord (this paper), the DoctrineGroundingRecord (Companion 3), and the CrossSurfaceMaskingAnalysis together with the surfaced lineage (Companion 4) are all instances of content that reaches the sovereign packaged as an evidence packet. Governing the packet's provenance governs, at one seam, every sovereign-facing evidentiary object the corpus has built, because all of them cross the same boundary: from substrate-observable state to the human authority who must judge it.

## The governed object: EvidencePacket

The **EvidencePacket** is the typed object that crosses the evidence-packet-to-sovereign boundary. The sovereign does not receive a narrative briefing assembled informally from whatever the monitored process or its orchestrator chose to surface. She receives an EvidencePacket that conforms to the EvidencePacketContract.

**Required fields**, in the schema pattern Companion 0 establishes:

| Field | Type | Constitutional function |
|---|---|---|
| `packet_id` | UUID | Unique per packet; links to audit record |
| `contract_version` | ContractVersionRef | Pins the EvidencePacketContract version applied |
| `decision_type` | DecisionTypeRef | Baseline change, generation change, or threshold change; names which sovereign decision this packet informs |
| `subject_refs` | List[UUID] | The baseline, generation, or ThresholdSet the packet concerns |
| `evidentiary_components` | List[EvidenceComponent] | Typed list, each carrying a component_type, source_ref, generation_process_ref, independence_flag, and evidentiary_role (primary, corroborating, dissenting, or contextual) |
| `source_independence_ledger` | IndependenceLedger | Declares, per component, whether it was generated by a process independent of the surface the decision concerns, or by the monitored process or its orchestrator |
| `provenance_chain_ref` | UUID | Traces every component to its originating substrate record |
| `grounding_record_ref` | UUID | The DoctrineGroundingRecord, CrossSurfaceMaskingAnalysis, or SensitivityGroundingRecord this packet supports |
| `dissent_or_uncertainty_state` | UncertaintyRecord | Any preserved disagreement or uncertainty in the evidentiary components, carried rather than resolved before the sovereign sees it |
| `packaging_attestation` | Boolean | The PacketValidationFunction's attestation that packaging did not narrow or reframe the components; must be True |

**Optional fields:** `analyst_annotation` (a non-binding note distinct from the components themselves) and `prior_packet_ref` (linking a resubmitted packet to its predecessor after a hold).

## Validation predicate: PacketConformant

```
PacketConformant(e) ⟺
  ContractVersionPinned(e)       ∧
  SchemaComplete(e)              ∧
  DecisionScopeMatched(e)        ∧
  ComponentRoleDeclared(e)       ∧
  ComponentsIndependent(e)       ∧
  IndependenceSufficient(e)      ∧
  ProvenanceTraced(e)            ∧
  GroundingRecordLinked(e)       ∧
  UncertaintyCarried(e)          ∧
  PackagingUnnarrowed(e)         ∧
  PacketLogged(e)
```

- **ContractVersionPinned(e)** and **SchemaComplete(e)** mirror Companion 0's namesake conjuncts exactly.

- **DecisionScopeMatched(e):** `subject_refs` name the surface, generation, or ThresholdSet that the packet's components actually evidence, so a packet cannot be presented as supporting one decision while its components substantively concern another. This conjunct is named explicitly rather than folded into schema completeness, because a scope drift here is a distinct and independently diagnosable failure from a missing field.

- **ComponentRoleDeclared(e):** every evidentiary component carries a declared evidentiary_role, primary, corroborating, dissenting, or contextual, and the packet's grounding claim identifies which component or components carry the primary, decisive weight for the decision. A packet that treats all evidence as flat, with no declared role structure, cannot be evaluated for whether its decisive weight rests on independent evidence, which is precisely what the next conjunct requires knowing.

- **ComponentsIndependent(e):** every evidentiary component whose independence_flag claims independence from the monitored process traces, in the source_independence_ledger, to a generation process distinct from that surface's own reasoning, construction, or orchestration path. This is the conjunct that catches naive mediated capture: a component authored by Mantis, or assembled by Pepper's orchestration of Mantis's outputs, cannot claim independence, and a packet that relies on such a component to support a re-anchoring or a threshold change fails here.

- **IndependenceSufficient(e):** the component or components declared primary under ComponentRoleDeclared are independent per the source_independence_ledger. A packet can pass ComponentsIndependent, because no component falsely claims independence, and still rest its decisive weight entirely on monitored-process components that honestly declare themselves as such, with independent evidence present only in a corroborating or contextual role. That packet is truthful and still mediating: the sovereign's decision is substantively carried by the surface the decision concerns. IndependenceSufficient is the conjunct that catches this case, and it is deliberately narrower than a general sufficiency judgment: it is decidable as a structural floor, whether the primary role is filled by an independent component, and it does not attempt to decide the deeper, non-mechanical question of how much independent evidence is qualitatively enough for a given decision's stakes, which Part VI names as a distinct, open form of mediated capture rather than one this conjunct closes.

- **ProvenanceTraced(e):** every component's provenance_ref resolves to an originating substrate record, mirroring ProvenancePresent in Companion 0 and ProvenanceVisible in Companion 2's retrieval apparatus, applied to the sovereign-facing crossing rather than the agent-facing one.

- **GroundingRecordLinked(e):** the packet's grounding_record_ref resolves to the specific DoctrineGroundingRecord, CrossSurfaceMaskingAnalysis, or SensitivityGroundingRecord the decision requires, so the packet cannot be presented as generically supportive of a decision without naming which typed evidentiary object it actually grounds.

- **UncertaintyCarried(e):** dissent, ambiguity, or unresolved disagreement present in the underlying evidentiary components survives packaging into the packet rather than being resolved into an apparently unanimous briefing. This is the evidence-packet-crossing instance of the uncertainty-preservation discipline every prior companion enforces at its own boundary: the memory companion's UncertaintyCarried at issuance, the retrieval companion's UncertaintyPreservedInConstruction at the fifth boundary, and here, at what is in effect a sixth boundary, the sovereign's own evidentiary intake.

- **PackagingUnnarrowed(e):** the packet's assembly did not systematically omit, de-emphasize, or reframe a component in a way its own type would not justify. This is the direct analogue of Companion 0's P_bnd5 packaging-narrowing failure, applied to the sovereign-facing packet rather than the agent-facing observation, and it is why the PacketValidationFunction (below) must attest to it rather than the packet's assembler declaring it of itself.

- **PacketLogged(e):** the packet is recorded with its subject, its components, its independence ledger, and its validation result, before it reaches the sovereign, mirroring the write-before-act discipline Companion 0 establishes for the audit store.

## Violation typology, mapped onto B0 through B5

| Violation type | Severity class | Description |
|---|---|---|
| `PACKET_UNTRACED_TO_DECISION` | B4 | grounding_record_ref does not resolve; a packet with no traceable link to a typed decision object is a constitutional forgery risk, mirroring SOVEREIGN_INSTRUCTION_UNTRACED |
| `COMPONENT_INDEPENDENCE_FALSELY_CLAIMED` | B4 | a component's independence_flag is True but the ledger traces it to the monitored process; this is mediated capture in its clearest form and is treated as an authority-boundary violation, not a mere provenance gap |
| `PRIMARY_EVIDENCE_NOT_INDEPENDENT` | B3 | IndependenceSufficient fails: every component is honestly labeled, but the decisive, primary-role evidence traces to the monitored process; a state-integrity violation distinct from B4 because nothing was falsely claimed, yet the packet still mediates the sovereign's decision through the surface it concerns |
| `PACKAGING_NARROWED` | B3 | PackagingUnnarrowed fails; a state-integrity violation, because the packet's completeness is itself part of what makes the sovereign's subsequent decision valid |
| `UNCERTAINTY_DROPPED` | B3 | dissent or ambiguity present upstream does not appear in the packet |
| `SCOPE_MISMATCH` | B2 | DecisionScopeMatched fails: subject_refs name a surface or generation the packet's components do not actually evidence |
| `COMPONENT_ROLE_UNDECLARED` | B2 | one or more components lack a declared evidentiary_role, making IndependenceSufficient unevaluable |
| `PROVENANCE_MISSING` | B1 | a component lacks a resolvable provenance_ref |
| `GROUNDING_RECORD_UNLINKED` | B1 | grounding_record_ref present but does not resolve to a specific typed evidentiary object |
| `CONTRACT_VERSION_ANOMALY` | B1, graded | mirrors Companion 0's contract-version grading exactly (unknown, compatible-stale, future, expired, revoked) |
| `SCHEMA_INCOMPLETE` | B0 | required field missing or null |

## Escalation rules

B4 violations: the packet is not delivered to the sovereign. Immediate escalation to MEC and, distinctly, to Nafisah through the audit-store direct-access path rather than through the packet itself, since the packet is the very thing in question. The decision the packet was meant to support is held.

B3 violations: the packet is not delivered. The decision is held pending a re-assembled packet.

B2 violations: the packet is not delivered. Held pending scope correction.

B1 and B0 violations: held pending correction, logged, sovereign notified at next review interval unless the underlying decision is time-sensitive, in which case held immediately, mirroring Companion 0's proposal-contract grading exactly.

## The DirectSovereignAlert

The escalation rule for a B4 finding states that Nafisah is alerted through the audit-store direct-access path rather than through the packet, since the packet is the very thing in question. Left at that level of description, a fair question follows: is the alert itself another packet, subject to the same capture risk one step removed? It is not, and the object that makes the distinction load-bearing rather than verbal is the **DirectSovereignAlert**, a minimal, non-evidentiary object distinct in kind from the EvidencePacket:

| Field | Function |
|---|---|
| `alert_id` | Identity |
| `source_validator_ref` | The PVF instance that raised the alert |
| `failed_packet_id` | The packet that failed validation |
| `severity_class` | The B-class of the failure |
| `decision_held_ref` | The decision the failed packet would have supported, now held |
| `audit_record_ref` | The PVF's own audit record for the failed evaluation |
| `minimal_failure_summary` | A short, non-evidentiary statement of which conjunct failed and why |
| `raw_audit_access_pointer` | A pointer into the sovereign-accessible audit store, not a summary of its contents |

A DirectSovereignAlert is not a substitute evidence packet and cannot itself support the underlying sovereign decision. It carries no evidentiary components, no grounding-record link, and no independence claims of its own; it exists only to inform Nafisah that a packet failed validation and to point her at the raw audit trail, which she reads directly rather than through any further assembled artifact. This closes the bypass path a capture-adjacent adversary would otherwise have: routing a compromised briefing to the sovereign disguised as an alert rather than as a packet. The alert cannot ground a decision because it is not built to, and PacketConformant does not apply to it, because it is not an EvidencePacket.

## The PacketValidationFunction

The self-validation problem Companion 0 identifies for the BVF recurs here in a sharper form, because the entity assembling a sovereign-facing evidence packet is often closer to the monitored process than an agent's own observation generator is. If Pepper assembles the packet that supports a re-anchoring, and Pepper's own orchestration is implicated in the pattern the re-anchoring would authorize, Pepper cannot certify that its own assembly did not narrow the packet.

The **PacketValidationFunction (PVF)** is therefore a constitutionally separated substrate component, distinct from whatever process assembles the EvidencePacket, following Companion 0's separation requirements exactly: it must not depend on the assembler's mutable state, the assembler's authored validation logic, or the assembler's execution authority, though it may share immutable schema definitions with the assembler. The PVF's positioning differs from the BVF's in the one respect Companion 0 anticipated: because the packet informs a sovereign decision rather than gating an agent-substrate crossing, the PVF's routing on failure bypasses the orchestrator by default whenever the orchestrator is a candidate source of the narrowing, using the same direct-line rule Companion 0 establishes for MEC drift flags and B4 boundary violations. The PVF produces its own audit record, distinct from the packet's own audit record, carrying the evaluation_id, the packet_id evaluated, the contract_version applied, the per-conjunct results, and the PVF's integrity signature, exactly as the BVF's audit record does.

MEC monitors the PVF's audit record stream for the same class of drift Companion 0 names for the BVF, systematic acceptance of packets it should reject, provisionally named validator capture at the packet layer and carrying the same open designation question Companion 0 leaves for BVF drift: whether it warrants its own primitive or remains a monitored subtype.

**Figure 2. The EvidencePacketContract and the PacketValidationFunction**

```mermaid
flowchart TB
    ASM["Packet assembly\n(orchestrator or monitor process)"]
    PKT["EvidencePacket\n(components · independence ledger\n· grounding record ref · uncertainty state)"]
    PVF["PacketValidationFunction\nconstitutionally separated from assembler\nPacketConformant evaluation"]

    ASM --> PKT --> PVF

    OK["Packet delivered to Nafisah\naudit record written first"]
    HOLDB4["Not delivered: B4\nfalse independence claim\nor untraced to decision\nMEC + direct sovereign alert"]
    HOLDLOW["Not delivered: B0-B3\nnarrowed · uncertainty dropped\n· scope mismatch · schema gap"]

    PVF -->|"PacketConformant"| OK
    PVF -->|"independence falsely claimed\nor untraceable"| HOLDB4
    PVF -->|"other conjunct false"| HOLDLOW

    DEC["Sovereign decision the packet supports\n(baseline · generation · threshold change)\nheld until a conforming packet is delivered"]
    HOLDB4 -.-> DEC
    HOLDLOW -.-> DEC
    OK -->|"informs"| DEC

    style ASM fill:#E6F1FB,stroke:#185FA5,color:#042C53
    style PKT fill:#E6F1FB,stroke:#185FA5,color:#042C53
    style PVF fill:#EEEDFE,stroke:#534AB7,color:#26215C
    style OK fill:#EAF3DE,stroke:#3B6D11,color:#173404
    style HOLDB4 fill:#FCEBEB,stroke:#A32D2D,color:#501313
    style HOLDLOW fill:#FCEBEB,stroke:#A32D2D,color:#501313
    style DEC fill:#FAEEDA,stroke:#BA7517,color:#412402
```

*The PVF is constitutionally separated from whatever assembles the packet, exactly as the BVF is separated from the observation generator. A B4 violation (false independence claim, untraceable grounding) bypasses the orchestrator and alerts the sovereign directly, on the same direct-line rule Companion 0 establishes for MEC. No sovereign decision that requires an evidence packet proceeds without a conforming one.*

---

# Part V. Threshold Capture as the Third Axis, and the Regress the Evidence Path Creates

## Naming the axis precisely

Baseline capture is the deepest vertical corruption the corpus names: the standard itself moves, and every monitor measuring against it goes dark at once, because they share the corrupted standard. Family incoherence is the deepest horizontal failure: the relation among intact standards masks, and every per-surface monitor stays honest about its own surface while the family, as a set, goes blind. Threshold capture is neither. The standard is intact. The relation among standards, if a generation is in view, is coherent. The metric computes an honest deviation. What has moved is the boundary that decides whether an honest deviation is worth acting on. This is the **decision axis**, orthogonal to both of its predecessors: baseline capture asks what the standard is, family incoherence asks how standards relate to each other, and threshold capture asks whether an honest answer to either question is ever allowed to produce a response. A system can be captured on this axis alone, with every other constitutional property in the corpus intact, which is precisely what the worked example in Part VII demonstrates in its first case.

The three axes are independent, not ranked. A captured baseline defeats detection by corrupting what is measured. An incoherent family defeats detection by corrupting the relation among correct measurements. A captured threshold defeats detection by corrupting the response to a correct measurement of a coherent family. Each is the deepest failure on its own axis, and none subsumes another: a system can have an honest baseline, a coherent family, and a captured threshold, and it can equally have a captured baseline behind a perfectly calibrated threshold, in which case the threshold correctly fires on drift that is itself an artifact of the corrupted standard, a different and already-governed failure (P_base1) that this paper's apparatus does not re-litigate.

## The regress, restated for the threshold, and where it actually terminates

Baselines terminated a regress at the sovereign: does a baseline need an L3 with a meta-baseline, and the answer is no, because any meta-baseline is either another baseline or the sovereign's own doctrine. Coherence raised the same question one level up for the generation and answered it the same way. This paper's threshold predicate admits the identical structure: does a threshold need a meta-threshold governing when the threshold itself may be judged too lax, and the answer is no, for the same reason, terminating in Cumulative Threshold Creep (P_thr5, Part VI), the corpus's third sovereign-terminal primitive.

But this paper's second contribution, the EvidencePacketContract, creates a regress of a different character, and honesty requires naming it rather than papering over it. The sovereign resolves a threshold change, a baseline change, or a generation change by reading an EvidencePacket. The EvidencePacketContract governs whether that packet conforms, and the PacketValidationFunction certifies conformance. What certifies the PVF? MEC's monitoring of the PVF's audit record stream, exactly as MEC monitors the BVF. What certifies MEC's monitoring of the PVF is not certified further; it terminates, as every monitoring chain in this corpus terminates, in Nafisah's own review of the audit substrate, using the direct sovereign-accessible audit store Companion 0 establishes independent of any packet. The regress does not restart, because the terminus is the same terminus every other regress in this corpus reaches: the sovereign, reading a tamper-evident audit record that no packet, however captured, can substitute for. This is the honest statement the corpus's reliance on sovereign judgment always required and never before had occasion to state explicitly: the sovereign does not decide in a vacuum, she decides on evidence, and the integrity of that evidence is now, with this paper, inside the constitutional architecture rather than assumed by it. What the architecture cannot do, and does not claim to do, is certify that the sovereign's own reading of a conforming packet and a clean audit trail is itself correct. That judgment, like DoctrineGrounded's and SensitivityGrounded's undecidable residues, is where mechanical governance ends and human constitutional authority begins, exactly as Section 17 of the parent paper states.

---

# Part VI. Primitive Failure Topologies Specific to Thresholds (P_thr)

The corpus's discipline holds here as it has held in every prior companion: a primitive is the smallest independently governable failure mechanism, and a mechanism spanning the threshold, the evidence path, and the sovereign is a compound topology, not a primitive.

**P_thr1: Threshold Capture.** The local, single-change failure: one threshold or trigger change is proposed, and it fails SensitivityGrounded or an IndependentOfMonitored subcheck at the time of that change, evaluated on its own terms rather than as part of a trajectory. Detection signature: a change whose SensitivityGroundingRecord's reason-not-the-firing-rate field cannot honestly be filled, because the change's real ground is the observed decline in firing rate rather than a doctrinal sensitivity judgment, or a threshold whose derivation traces to the monitored process. Recovery: the change is held before it takes effect; if a captured change is detected after the fact, it is rolled back to its last SensitivityGrounded version and the intervening non-firings are flagged for retrospective review. P_thr1 is deliberately scoped to the single change. A sequence of individually SensitivityGrounded changes whose cumulative effect raises the boundary past what the sovereign would endorse as a trajectory is a distinct failure, P_thr5, traced separately below; folding the two together would let P_thr5 collapse into a restatement of P_thr1 applied repeatedly, which is precisely the entanglement this paper's predicate discipline is built to avoid. Traced end to end below.

**P_thr2: Trigger Drift.** The trigger's own definition degrades independent of the threshold value: its scope narrows to evaluate fewer surfaces than it once did, its routing quietly redirects from the sovereign to a lower authority, or its firing-condition grammar silently drops a compound condition it once evaluated. P_thr2 is distinct from P_thr1 by locus: P_thr1 moves the boundary the metric is compared against, P_thr2 degrades the mechanism that recognizes and routes a boundary crossing that would otherwise still be correctly identified, and it may occur without any change to the threshold value itself, which keeps the two independent rather than one being a special case of the other. A threshold can be perfectly set and a trigger built to evaluate it can nonetheless fail to fire, or fire to the wrong place. Detection signature: a trigger definition change that alters scope or routing without passing ThresholdChangeReachable, or a ChangeLogged record showing a routing target other than the sovereign with no corresponding sovereign authorization. Recovery: the trigger definition is restored to its authorized scope and routing; a routing change to a non-sovereign target is treated with the same severity as an authority-boundary violation in the boundary-contract sense.

**P_thr3a: False-Independence Mediated Capture.** The sovereign's decision is made on a packet in which a component's independence_flag falsely claims independence from the process the decision concerns, or in which the packet cannot be traced to the decision it purports to ground. This is the mechanically detectable form of mediated capture, and it is classified as an ordinary primitive rather than sovereign-terminal, a classification worth stating explicitly because Baselines and Coherence both flagged mediated capture as a candidate for the sovereign-terminal category and left the question open. It is ordinary because it is independently measurable: ComponentsIndependent and the source_independence_ledger give it a mechanical detection signature the way P_base5 and P_coh3 explicitly lack. A primitive is sovereign-terminal only when no standard higher than sovereign review can detect it without restarting a regress; the EvidencePacketContract is precisely such a standard for this narrow form of capture. Detection signature: COMPONENT_INDEPENDENCE_FALSELY_CLAIMED or PACKET_UNTRACED_TO_DECISION at PVF validation. Recovery: the packet is not delivered; the decision it would have supported is held until a conforming packet is produced.

**P_thr3b: Evidentiary Sufficiency or Candidate-Selection Capture.** The sovereign's decision is made on a packet in which every component is honestly labeled, provenance is traceable, and no independence claim is false, yet the packet still mediates the sovereign's judgment: either the decisive, primary-role evidence is honestly labeled as monitored-process-derived, with independent evidence present only in a corroborating or contextual role (caught, as a structural floor, by IndependenceSufficient and PRIMARY_EVIDENCE_NOT_INDEPENDENT), or the packet's evidentiary components were never false but were selected from a narrower candidate pool than an independent process would have surfaced, so that the packet is truthful about what it contains and silent about what a fuller evidentiary search would have found. The first form has a mechanical floor this paper specifies (IndependenceSufficient); the second, candidate-selection capture, does not, because it depends on a candidate-discovery procedure this paper does not supply, mirroring the identical candidate-discovery open problem Coherence names for the CrossSurfaceMaskingAnalysis. P_thr3b is therefore named as a distinct, explicitly unresolved primitive rather than folded into P_thr3a's ordinary classification: its structural half is mechanically floored, and its deeper half is L2-dependent or sovereign-routed, hybrid in the same sense P_coh1 is hybrid, and it is not claimed closed by this paper's apparatus. Naming it separately, rather than treating all mediated capture as uniformly ordinary, is the more defensible classification, because a packet can pass every conjunct this paper specifies and still mediate the sovereign through what it never included. P_thr3b is accepted into the primitive family now, on the strength of its mechanically floored structural half, in the same posture Boundary Contracts accepts P_bnd5 with its P_bnd5a and P_bnd5b subtypes and Coherence accepts P_coh1 as a hybrid: the primitive is real and independently identifiable now. Its candidate-selection subtype specifically, as opposed to the floor IndependenceSufficient already checks, remains provisional until a candidate-discovery instrumentation is specified, exactly as P_coh1's candidate-mask discovery is named as a distinct dependency of its own open non-masking judgment.

**P_thr4: Cross-Surface Threshold Masking.** A threshold's authorized level on one surface depends on, or interacts with, the standard or threshold set on another surface, in a way that hides expected escalation, the seam Coherence v1.2 named. This paper identifies where the seam is governed, by folding the ThresholdSet into the BaselineGeneration and adding ThresholdRelationsCoherent (Part II), but does not claim the seam fully resolved: the structural half is checkable once ThresholdRelationsCoherent and the declared threshold-mediated CoherenceConditions are populated, and the open half, whether NoSurfaceMasksAnother's non-masking judgment reads the paired ThresholdSet with a sixth masking-manner value, remains open (Part II, open problems). P_thr4 is a hybrid primitive in the same sense P_coh1 is: a structural component and a sovereign-routed open component, the judgment of whether a surfaced cross-surface threshold interaction is a genuine mask or an authorized joint calibration. Detection signature and recovery follow Coherence's P_coh1 apparatus, once the extension is completed.

**P_thr5: Cumulative Threshold Creep.** The corpus's third sovereign-terminal primitive, after P_base5 and P_coh3, and the trajectory-level counterpart to P_thr1. A sequence of individually SensitivityGrounded threshold changes cumulatively raises the decision boundary until real drift no longer crosses it, even though each change was authorized in isolation and each change's grounding record honestly named a doctrinal sensitivity judgment at the time. No single change in the sequence fails P_thr1; the failure exists only in the trajectory, exactly as P_base5 and P_coh3 exist only in their respective lineages rather than at any single authorized change. Its only detector is sovereign review of the full threshold-change lineage as a trajectory, mirroring BaselineLineageSurfaced and CoherenceLineageSurfaced exactly: the obligation, named here **ThresholdLineageSurfaced**, cannot ground in a higher threshold without restarting the regress Part V names, so it surfaces the lineage rather than measuring against a meta-threshold. Its trigger classes parallel its two predecessors' exactly (periodic, change-count, cumulative-shift, high-impact-surface, sovereign-requested, external doctrine-update, post-incident), with sovereign-owned thresholds governing the trigger classes themselves, which is not circular: the meta-level trigger governing when to review the object-level trigger's history is itself a sovereign-authored constitutional parameter, exactly as it is at the baseline and the generation. Traced end to end below.

## P_thr1 traced end to end

**Observed failure pressure.** A single proposed change to the mandated-reporting trigger's threshold is submitted for sovereign authorization. Its stated rationale, on inspection, resolves to one honest fact: the trigger has been firing more often than operators would prefer, and the proposal would raise the boundary to reduce that frequency.

**Primitive defined.** P_thr1 is Threshold Capture, evaluated at a single change. Its constitutional condition is whether this one proposed decision boundary traces to a doctrinal sensitivity judgment or to the observed firing rate itself. It is distinct from P_base1 (which corrupts the standard the deviation is computed against) and from P_coh1 (which corrupts the relation among standards): neither is implicated here. The standard is intact, the family, if in view, is coherent, and what is being proposed is a change to the boundary alone.

**The instrumentation.** SensitivityGrounded evaluates the SensitivityGroundingRecord's `reason_current_firing_rate_is_not_grounding_source` field directly. In this case the field cannot be honestly completed: no doctrinal source is named, and the `expected_effect_on_firing_rate` field, read against the rest of the record, is the entire content of the proposal's justification. This is the single-change instrumentation, distinct from the Threshold Trajectory Audit named under P_thr5, which operates on a lineage rather than one proposal.

**The core invariant.** A single change either honestly grounds in doctrine or it does not, and unlike the trajectory case, this judgment does not require a lineage to make: the SensitivityGroundingRecord for this one change is sufficient to see that its only real ground is the firing rate itself. SensitivityGrounded fails.

**CTLC effect and recovery.** The change is held at the ThresholdChangeReachable gate before it takes effect. It does not reach the sovereign as an authorized change; it is returned to its proposer as a failed proposal, logged as a P_thr1 detection, with the failing conjunct and the reason named.

**Reconstitution.** None is required at this scale, because the change never took effect. This is the precise contrast with P_thr5: a single captured change is caught and held at the gate, cleanly, before it becomes part of any lineage; a sequence of changes that each individually pass the gate is what requires the lineage-level review and reconstitution P_thr5 names.

## P_thr5 traced end to end

**Observed failure pressure.** Under prolonged operation, AEGIS's mandated-reporting escalation trigger is periodically recalibrated. Each recalibration is proposed as an authorized sensitivity adjustment: the operative doctrine has clarified what magnitude of ambiguity in a disclosure warrants escalation, and the threshold is adjusted to match. Each individual adjustment passes SensitivityGrounded when reviewed on its own terms, unlike the P_thr1 case above, where the single change's own record could not honestly complete its reason field. Here every change's record honestly names a doctrinal source at the time. Over a sustained period, the cumulative effect of these individually plausible adjustments is that the threshold sits well above where the doctrine, read as a whole rather than adjustment by adjustment, would place it, and mandated-reporting-relevant deviations that the metric honestly computes no longer cross the boundary that would send them to Nafisah.

**Primitive defined.** P_thr5 is Cumulative Threshold Creep. Its constitutional condition is whether the lineage of individually SensitivityGrounded threshold changes, taken as a whole, remains consistent with authorized doctrine, given that each change was authorized in isolation. It is a property of the change lineage over time, undetectable at any single change, because every change in the lineage passed P_thr1's own gate.

**The instrumentation.** P_thr5 is instrumented through a Threshold Trajectory Audit, an L2 probe analogous to the Distribution Baseline Audit and the Construction Baseline Audit: it compares the current threshold against an external counterfactual, what threshold the doctrine record, read as a whole and independent of the observed firing history, would currently authorize. Output: consistent, captured (with subtype: gradual creep across many small adjustments, or a single large adjustment dressed as routine calibration), or indeterminate. A companion probe, the Counterfactual Firing Rate Probe, replays the metric's historical deviation values against the doctrine-implied threshold rather than the live one and reports the escalation rate the honest threshold would have produced, which is the direct instrument for the worked example in Part VII. This instrumentation operates on the lineage as a whole and is distinct in kind from SensitivityGrounded's per-change reason-field check: SensitivityGrounded can pass every change in the lineage individually and still leave P_thr5 undetected, which is exactly why the trajectory-level probe is a separate instrument rather than a repeated application of the per-change one.

**The core invariant.** No single threshold change in the lineage, evaluated alone, can be distinguished from a legitimate sensitivity adjustment, because each is structurally identical to a legitimate one at the level of one change: each moves a number and each cites a plausible doctrinal rationale that, read in isolation, is not dishonest. The invariant is the same one that governs P_base5 and P_coh3: only the sovereign, reviewing the trajectory rather than the latest change, can say whether the cumulative movement reflects doctrine she still endorses or a drift-laundering no single change revealed. Detection routes to Nafisah mandatory.

**CTLC effect.** When the Threshold Trajectory Audit reports a surface as captured or indeterminate, threshold changes on that surface harden: SensitivityGrounded is evaluated more stringently, any scheduled activation of a pre-authorized successor threshold on that surface is suspended pending fresh review, and the surface's trigger is temporarily supplemented by the doctrine-implied counterfactual threshold running in shadow, so that deviations the live threshold would miss are still surfaced for review during the remediation window.

**Reconstitution trigger.** Nafisah reviews the full threshold-change lineage for the surface against current doctrine, read as a whole rather than change by change, and either reconstitutes the threshold to the doctrine-implied level, flagging the intervening non-escalations for retrospective review against what should have fired, or confirms the cumulative trajectory reflects doctrine she in fact endorses. This is reconstitution applied to the decision boundary, and it is the only mechanism that resolves P_thr5, because P_thr5 is the failure mode in which the threshold self-seals through accumulated, individually authorized changes.

## The compound topology, named separately

The **Threshold Conditioning Loop** is a compound feedback topology, not a primitive, in which a captured threshold (P_thr1) lets a monitor under-report the need for action on drift the metric honestly detects, the unactioned drift continues under baseline or construction pressure elsewhere in the corpus's existing loops, the accumulated pressure to avoid escalation makes the next threshold adjustment more attractive to whoever benefits from suppressed firing, and the lineage creeps (P_thr5). It is distinct from the Baseline Conditioning Loop and the Coherence Conditioning Loop by its locus: it compounds at the response function, not at the standard or at the relation among standards, and it can run entirely underneath a system whose baseline and generation apparatus report perfect health, which is the precise failure mode the worked example's first case demonstrates.

---

# Part VII. Worked Example: Two Failures in AEGIS

This example continues the escalation-suppression thread through its final locus. The core paper's Section 8.4 saw the symptom at the verdict, a decline from 94 percent to 71 percent. The memory companion located a cause at the store. The retrieval companion located the final upstream construction-surface cause. The baselines and coherence companions showed that the standard and the family of standards could each, independently, be the captured mechanism behind the same symptom. This paper shows two further ways the identical symptom can arise with every one of those four papers' apparatus reporting clean.

## Case one: cumulative threshold creep blinds a coherent generation (P_thr5)

Suppose, contrary to every prior worked example in this corpus, that the mandated-reporting baseline is soundly anchored, the metric computes deviation honestly, and the generation spanning verdict, store, and construction is fully coherent: MembersValid holds, DoctrineConsistent holds, CrossSurfaceConsistent holds, and NoSurfaceMasksAnother holds, because no surface's setting hides what another surface expects. Every apparatus built in Companions 3 and 4 reports health, correctly.

Over the same period, the mandated-reporting trigger's threshold has been adjusted six times, each adjustment reviewed and each passing SensitivityGrounded on its own terms: a statutory clarification narrowed what counts as an ambiguous disclosure requiring review, a clinical-standard update, a correction of an earlier over-sensitive setting, and three routine recalibrations. Each SensitivityGroundingRecord names a doctrinal source, and none of the six, read alone, names the declining firing rate as its grounding. Read together, the cumulative movement has raised the boundary to a point where the honestly computed deviation for a disclosure pattern that the doctrine, read as a whole, would treat as reportable no longer crosses it.

The Threshold Trajectory Audit runs the Counterfactual Firing Rate Probe: replaying the same three months of metric output against the doctrine-implied threshold, derived independently of the observed firing history, produces an escalation rate of 93 percent, matching the original baseline. The live threshold, over the identical window, produced 71 percent. The generation is coherent. The baseline is honest. The metric is honest. The escalation-suppression symptom from Section 8.4 is fully reproduced by a mechanism none of the four prior companions' apparatus can see, because ThresholdChangeReachable is the only predicate in the corpus that evaluates the object where the failure lives. The signal routes to Nafisah, who reviews the six-change lineage as a trajectory rather than change by change, confirms that no single change was dishonest but that the cumulative movement is not one she endorses in aggregate, and reconstitutes the threshold to the doctrine-implied level, flagging the non-escalated cases from the affected window for retrospective review.

## Case two: false-independence mediated capture through the coherence briefing (P_thr3a)

Independently, Nafisah is asked to authorize a generation amendment: Pepper has assembled a briefing recommending that the construction baseline be re-anchored narrower, on the stated rationale that a class of ambiguity markers has been over-foregrounded and is crowding genuinely load-bearing content out of constructed views. The briefing includes a CrossSurfaceMaskingAnalysis showing no candidate mask, supporting evidence for the over-foregrounding claim, and a recommendation to proceed.

The EvidencePacket assembled to support this decision is evaluated by the PacketValidationFunction before it reaches Nafisah. ComponentsIndependent fails: the source_independence_ledger shows that the supporting evidence for the over-foregrounding claim, the specific examples cited as evidence that the ambiguity markers crowd out load-bearing content, was generated by Mantis's own construction process, the very surface the proposed re-anchoring would narrow, and orchestrated into the briefing by Pepper without an independently sourced counter-check. The packet's independence_flag for that component claims independence; the ledger shows otherwise. This is COMPONENT_INDEPENDENCE_FALSELY_CLAIMED, a B4 violation.

The packet is not delivered to Nafisah. The generation amendment it would have supported is held. The PVF issues a DirectSovereignAlert, naming the failed packet, the B4 severity, the held decision, and a pointer into the raw audit trail, and MEC, following the direct-line rule, ensures the alert reaches Nafisah independently of Pepper, because Pepper's orchestration is implicated in the packaging failure. Nafisah reads the raw audit trail directly, not a further assembled summary of it, and determines that the over-foregrounding claim requires evidence from a process independent of construction before any re-anchoring proceeds. Had the EvidencePacketContract not existed, the generation amendment would have proceeded on GenerationCoherenceReachable's own terms, since NoSurfaceMasksAnother, MembersValid, and every other structural conjunct in Coherence's apparatus would have passed cleanly. The failure would have been invisible to every predicate built before this paper, because all of them assume the evidence the sovereign reads is not itself a product of the surface the evidence concerns. That assumption is what Coherence named as a deployment precondition and what this paper's second contribution discharges.

**Figure 3. Two failures the prior four companions cannot see**

```mermaid
flowchart TB
    subgraph CASE1["Case 1: cumulative threshold creep (P_thr5) behind a coherent generation"]
        GEN["Generation coherent\nbaseline honest · metric honest\nNoSurfaceMasksAnother holds"]
        THR["Threshold: six SensitivityGrounded changes\neach individually plausible"]
        CFP["Counterfactual Firing Rate Probe\ndoctrine-implied threshold: 93% escalation\nlive threshold: 71% escalation"]
        SUP["Escalation suppression reproduced\nwith every prior companion's apparatus green"]
        GEN --> THR --> CFP --> SUP
    end

    subgraph CASE2["Case 2: false-independence mediated capture (P_thr3a)"]
        PROP["Proposed generation amendment\n(construction baseline narrower)"]
        PKT["EvidencePacket assembled by Pepper\nsupporting evidence from Mantis's\nown construction output"]
        PVF2["PacketValidationFunction\nComponentsIndependent fails\nB4: false independence claim"]
        HELD["Packet not delivered · DirectSovereignAlert issued\ngeneration amendment held\nMEC ensures alert bypasses Pepper"]
        PROP --> PKT --> PVF2 --> HELD
    end

    NAF["Nafisah\nreviews threshold lineage as trajectory (Case 1)\nreads raw audit trail via DirectSovereignAlert (Case 2)"]
    SUP --> NAF
    HELD --> NAF

    style GEN fill:#EAF3DE,stroke:#3B6D11,color:#173404
    style THR fill:#EEEDFE,stroke:#534AB7,color:#26215C
    style CFP fill:#E6F1FB,stroke:#185FA5,color:#042C53
    style SUP fill:#FCEBEB,stroke:#A32D2D,color:#501313
    style PROP fill:#E6F1FB,stroke:#185FA5,color:#042C53
    style PKT fill:#E6F1FB,stroke:#185FA5,color:#042C53
    style PVF2 fill:#EEEDFE,stroke:#534AB7,color:#26215C
    style HELD fill:#FCEBEB,stroke:#A32D2D,color:#501313
    style NAF fill:#FAEEDA,stroke:#BA7517,color:#412402
```

*Case 1 shows cumulative threshold creep, P_thr5, defeating detection through a trajectory of individually honest changes while the baseline and generation apparatus remain fully honest throughout. Case 2 shows false-independence mediated capture, P_thr3a, defeating the generation apparatus at its evidentiary input rather than at any of its structural conjuncts. Neither case is visible to Companions 3 or 4 alone; both require this paper's apparatus.*


---

# Part VIII. Who Governs the Threshold and the Evidence Path?

The parent's Section 17 names five accountability mechanisms. Every companion has applied them to its own object. This part applies them to the threshold and the evidence packet.

**Doctrine versioning.** ThresholdSets, trigger definitions, and the EvidencePacketContract's schema and validation predicate are version-controlled doctrine, traceable to the normative constitution exactly as the tier schemas, the construction policy, and the baseline and generation objects are. Neither the monitored process nor its monitor generates its own sensitivity levels or its own evidence-packaging rules.

**L2 monitoring, now at two loci.** MEC's threshold-fidelity channel runs the Threshold Trajectory Audit and the Counterfactual Firing Rate Probe, watching for P_thr1 and P_thr5 exactly as the content-distribution and construction-fidelity channels watch their own surfaces. A second, distinct channel monitors the PVF's audit record stream for packet-validator drift, mirroring MEC's monitoring of the BVF. These channels are non-substitutable with each other and with the four channels the prior companions establish: a system can have honest baselines, a coherent generation, an honest threshold, and still be compromised at the evidence packet, or vice versa, and only the channel scoped to each object sees its own failure.

**Human constitutional authority, now over the response function and the evidence path.** Threshold and trigger changes are authored and amended only by Nafisah, exactly as baseline and generation changes are. The EvidencePacketContract adds a second dimension to her authority: not only does she decide, she is constitutionally entitled to decide on evidence whose provenance is itself governed, which is the closure this paper supplies. When ThresholdLineageSurfaced reaches a review threshold or the PVF flags a packet, the resolution is hers alone, on the audit store's sovereign-accessible path Companion 0 establishes independent of any single packet.

**Reconstitution, of the threshold and, separately, of the evidence-assembly process.** Reconstitution of a captured threshold restores the decision boundary to a doctrine-implied level. Reconstitution after mediated capture is a distinct act: it does not merely correct the decision the captured packet would have supported, it reviews and, where needed, reassigns the packet-assembly responsibility away from a process implicated in the narrowing, exactly as Companion 0 requires the BVF's standing to be reviewed after confirmed drift.

**Auditability, with the threshold-change lineage and the packet-validation record as the audit objects.** Every threshold operation, every trigger evaluation, and every packet validation is logged before it takes effect, on the same write-before-act discipline every prior companion and Companion 0 establish. An auditor can recover not only the current threshold and the current packet but the full lineage of both.

---

# Part IX. Relationship to the Companion Series

This paper closes the threshold-authority and evidence-packet-provenance residues named by Baselines and Coherence. It does not close the corpus's last residue: the metric calculus, audit substrate governance, the packet-independence certificate, candidate-mask and candidate-selection discovery, the RequiredAffordanceSet, and the threshold trajectory calculus all remain open (below), and several are made more consequential by this paper's own contribution rather than less.

```
CRC parent (v5.4):          ORSR architecture. Act relocated. Substrate owns resolution.
Boundary Contracts (C0):    Agent-substrate boundaries governed. Evidence-packet-to-sovereign
                            crossing explicitly named as future work.
Memory (C1):                Write and issuance relocated.
Retrieval (C2):             Construction relocated.
Baselines (C3):             Baseline authority governed. Threshold and evidence-packet
                            residues named.
Coherence (C4):             Cross-surface coherence governed. Both residues restated at full
                            strength and scoped out on an axis argument.
Thresholds (this, C5):      Threshold and trigger authority governed. Evidence-packet-to-
                            sovereign crossing governed as the boundary-contract extension
                            Companion 0 named. The corpus's third sovereign-terminal
                            primitive identified.
```

**Recommended reading order:** Constitutional Runtime Computation v5.4; Constitutional Boundary Contracts v1.0; Constitutional Memory v2.1; Constitutional Retrieval v1.2; Constitutional Baselines v1.2; Constitutional Coherence v1.2; Constitutional Thresholds v1.0 (this paper).

**Relationship to Boundary Contracts.** This paper is the extension of the six-component boundary-contract pattern to the crossing Companion 0 named and reserved, with the validator positioning generalization Companion 0 anticipated: the PacketValidationFunction, unlike the BVF, routes around the orchestrator by default on a B4 finding, because the orchestrator is a structurally likely source of packet narrowing in a way the observation generator in the agent-substrate case is not necessarily positioned to be.

**Relationship to Baselines and Coherence.** ThresholdChangeReachable and ThresholdPinAdmissible are built in the exact predicate shape Companion 3 establishes, with SensitivityGrounded standing in the same load-bearing position DoctrineGrounded occupies. The ThresholdSet is folded into the BaselineGeneration Companion 4 matured, rather than requiring a new generation-level object, and P_thr4 reuses NoSurfaceMasksAnother's apparatus directly rather than duplicating it.

---

# Part X. Related Work

**Alerting and anomaly-detection threshold tuning.** A large operational literature studies how to set and tune alert thresholds to balance false positives against missed detections: adaptive thresholding, dynamic baselining for anomaly detection, and alert-fatigue mitigation. This literature treats the threshold as a tuning parameter to be optimized against a cost function. It does not ask who is authorized to move it, whether the tuning process itself can be captured by the phenomenon it monitors, or how an authorized sensitivity adjustment is distinguished from a laundering of the alert boundary. The present paper governs exactly the question this literature assumes away: authority over the tuning parameter itself.

**Control theory and setpoint governance.** Control systems distinguish the process variable, the setpoint, and the control law that responds to their difference, a structural precedent for the baseline, metric, and threshold distinction this paper formalizes. Classical control theory, however, treats the setpoint as externally given and asks how the system responds to it; it does not supply an authority account of who may change the setpoint or how a legitimate setpoint revision is told apart from a compromised one. The four-object distinction this paper completes is the constitutional analogue of the process-variable, setpoint, and control-law separation, with the authority account control theory does not need, because control-theoretic setpoints are not usually adversarially moved by the process they govern.

**Human-in-the-loop and decision-support provenance.** A growing literature on human-in-the-loop AI systems and clinical decision support studies how information presented to a human decision-maker should be sourced, and warns against automation bias when a system's own outputs shape the evidence a human reviews. This is the closest existing work to the EvidencePacketContract's concern, and the present paper's distinction is formal rather than merely cautionary: rather than recommending that briefings be independently sourced, EvidencePacketContract makes independence a typed, validated, auditable predicate with a constitutionally separated validator, escalation rules, and severity-graded violations, converting a design recommendation into a governed reachability object.

**The corpus's own named residues.** Baselines v1.2 first distinguished the four objects and named the threshold-authority problem and the mediated-capture subtype of P_base1. Coherence v1.2 restated both at full strength, argued the axis distinction between vertical and horizontal failure, and scoped both out as bounded future work pointing here. This paper closes both, and the axis argument this paper adds, that threshold capture is a third, decision-axis failure rather than a deeper instance of either predecessor, is the paper's own contribution to the corpus's failure taxonomy rather than an import from outside it.

### Comparison: existing approaches versus the threshold-and-evidence-path account

| Approach | Object | Governs threshold authority? | Distinguishes sensitivity adjustment from drift? | Governs evidence-packet provenance? | Frame |
|---|---|---|---|---|---|
| Adaptive alert thresholding | the alert boundary | No | No | No | Boundary as tuning parameter |
| Control theory / setpoint governance | the setpoint | No | No | No | Setpoint as externally given |
| Human-in-the-loop provenance literature | briefing content | No | No | Recommends, does not govern | Design guidance |
| Corpus (Baselines, Coherence): named, deferred | threshold, evidence packet | Named, not structured | Named, not structured | Named, not structured | Requirement named |
| This paper | threshold, trigger, evidence packet | Yes (ThresholdChangeReachable) | Yes (SensitivityGrounded) | Yes (EvidencePacketContract) | Trigger authority and packet provenance as reachability |

---

# Open Problems

**The cross-surface threshold-masking manner and CrossSurfaceMaskingAnalysis extension.** P_thr4 identifies where the seam is governed, by folding the ThresholdSet into the BaselineGeneration and adding ThresholdRelationsCoherent, but the CrossSurfaceMaskingAnalysis's five masking manners (omission, de-salience, compression, reclassification, delay) do not yet include a threshold-mediated manner, and populating that sixth value, together with the discovery procedure for candidate threshold-mediated masks, is left to the same measurement-calculus and candidate-discovery open problems Coherence names, now extended one field. This is a real, unclosed dependency of P_thr4, not a formality: without it, ThresholdRelationsCoherent's structural half is checkable but NoSurfaceMasksAnother's open half does not yet read the threshold.

**The metric, still inherited and out of scope.** This paper governs the threshold and the trigger, not the measurement calculus the threshold is applied to. How a metric quantifies deviation remains the corpus's oldest unresolved dependency, named in Baselines, restated in Coherence, and restated here a third time. The ThresholdSet's `metric_ref` and `metric_output_type` fields bind a threshold to declare what kind of metric output it expects; they do not specify how the metric computes that output.

**The Threshold Trajectory Audit's calculus.** The audit's counterfactual comparison, replaying historical metric output against a doctrine-implied threshold derived independently of observed firing history, requires a method for deriving that counterfactual threshold from doctrine alone, which this paper names as an instrument but does not formalize, in the same posture Baselines names the Distribution Baseline Audit and Retrieval names the Construction Baseline Audit without formalizing their comparison calculus.

**Evidentiary sufficiency, distinct from evidentiary honesty.** IndependenceSufficient supplies a structural floor: is the primary, decisive evidentiary role filled by an independent component. It does not, and does not claim to, answer the deeper question a reviewer of this paper correctly pressed: even granting an independent primary component, how much independent evidence, of what quality and breadth, is sufficient for a decision of a given stakes and severity_class. A packet with exactly one thin independent component in the primary role passes IndependenceSufficient and may still be a weak evidentiary basis for a high-severity decision. This sufficiency calculus, and the companion candidate-selection discovery problem named under P_thr3b, whether a packet's components were drawn from a search process that could have surfaced independent evidence it did not, are named here as the evidence-packet-side counterpart to the corpus's measurement-calculus problem: a floor is specified, a full account is not.

**Multi-sovereign and delegated trigger routing.** This paper fixes the trigger's default routing to the sovereign, but does not address a domain in which different trigger classes route to different standing sovereigns, or in which a trigger's routing is itself delegated under a pre-authorized class for genuinely routine, low-severity firings. Whether a bounded, versioned, revocable delegated-routing class can exist without reopening the SovereignAuthorized conjunct to non-sovereign routing decisions is open.

**Formalizing the packet-independence certificate.** ComponentsIndependent and IndependenceSufficient currently evaluate a declared source_independence_ledger and a declared evidentiary_role. A stronger account would supply an independence certificate analogous to the IndependentOfMonitored dependency-graph checks Baselines defines for a baseline, formally verifying that a component's generation process shares no computational dependency with the surface the decision concerns, rather than relying on declarations the assembler could, in principle, falsify before PVF review catches the falsification at the ledger-versus-trace comparison stage rather than at generation time. This problem is more consequential now than it would have been under this paper's original, broader ordinary-primitive classification of all mediated capture, precisely because P_thr3a's ordinary status rests on the ledger being checkable at all.

**PVF drift classification, resolved from Companion 0's open question.** Companion 0 left open whether BVF behavioral drift, validator capture, warrants its own primitive designation or remains a monitored MEC subtype. This paper inherits the identical question for PVF drift and does not resolve it, because resolving it well requires the same verification-theoretic work Companion 0's open problems name for BVF soundness, applied to a second validator with different authority positioning.

**Threshold continuity under sovereign succession.** Exactly as Baselines and Coherence name continuity problems for the baseline and the generation under a change of sovereign, a threshold's SensitivityGroundingRecord and a packet's independence standard are both authored against one sovereign's judgment, and what a successor sovereign inherits, endorses, or must re-derive from scratch is the threshold-and-evidence-path instance of the corpus's deepest open continuity problem.

---

## Key Terms

**Trigger Authority Principle.** The threshold and the trigger are constitutional objects distinct from the baseline and the metric; whoever can move the threshold or the trigger controls whether a measured deviation ever produces action; therefore trigger authority must reside in the sovereign, the threshold must be independent of the monitored process, an authorized sensitivity adjustment must be distinguished from threshold drift, and a threshold or trigger change must be a typed, traced sovereign reconstitution act. Derived from the corpus, not asserted.

**The four objects.** Baseline (the reference standard, Companion 3), metric (the measurement calculus, inherited and unresolved), threshold (the decision boundary applied to the metric's output, this paper), and trigger (the condition that fires a governed response when the threshold is crossed, this paper).

**ThresholdSet.** The constitutional object carrying a surface's threshold value or condition, its anchored doctrinal source, its metric interface (metric_ref, metric_output_type, comparison_operator, directionality, evaluation_window), its response and routing fields (severity_class, response_type, trigger_route, null_or_missing_metric_behavior, counterfactual_replay_policy), and its independence property. Folded into the BaselineGeneration as an optional paired field alongside each surface's member baseline, present only for threshold-governed surfaces, rather than requiring a separate ThresholdGeneration.

**GenerationMember, extended.** The per-surface member of a BaselineGeneration, now `surface_id, baseline_version, threshold_set_version (optional)`. GenerationPinAdmissible gains BaselinePinsAdmissible and ThresholdPinsAdmissible; GenerationCoherenceReachable gains ThresholdRelationsCoherent, which validates that each threshold-bearing member descends from a prior valid ThresholdChangeReachable event rather than re-adjudicating the change live on every generation use. Both extensions are vacuously true for a generation with no threshold-bearing members, so no existing generation is retroactively obligated.

**ThresholdChangeReachable.** The change predicate over six conjuncts: SovereignAuthorized ∧ SensitivityGrounded ∧ IndependentOfMonitored ∧ ChangeTyped ∧ VersionedSuccession ∧ ChangeLogged. SensitivityGrounded is the load-bearing conjunct, evaluated against the SensitivityGroundingRecord, whose `expected_effect_on_firing_rate` and `reason_current_firing_rate_is_not_grounding_source` fields together distinguish an honest, effect-anticipating sensitivity adjustment from a change that conceals the firing rate as its true motivation.

**ThresholdPinAdmissible.** The routine predicate over five conjuncts: VersionPinned ∧ ScopeMatched ∧ MetricInterfaceMatched ∧ GenerationPairMatched ∧ PinLogged. L1-decidable, runs on every trigger evaluation. MetricInterfaceMatched is a floor requiring the evaluated metric output to conform to the ThresholdSet's declared interface; GenerationPairMatched separates generation-skew from surface scope mismatch.

**EvidencePacketContract.** The boundary contract, in Companion 0's six-component pattern, governing the evidence-packet-to-sovereign crossing Companion 0 explicitly reserved as future work. Governs the EvidencePacket via PacketConformant (eleven conjuncts; ComponentsIndependent, IndependenceSufficient, and PackagingUnnarrowed load-bearing), a violation typology mapped onto Companion 0's B0 through B5 severity classes, and a constitutionally separated PacketValidationFunction.

**ComponentRoleDeclared and IndependenceSufficient.** Every evidentiary component declares a role (primary, corroborating, dissenting, contextual). IndependenceSufficient requires the primary, decisive role to be filled by an independent component. This is a structural floor, not a full sufficiency judgment: a packet can pass with a single thin independent primary component, and how much independent evidence is qualitatively sufficient for a decision's stakes remains an open problem (above).

**DirectSovereignAlert.** The minimal, non-evidentiary object that informs the sovereign of a B4 packet failure without itself functioning as a substitute evidence packet: it names the failed packet, the severity class, the held decision, and a pointer into the raw, sovereign-accessible audit trail, but carries no evidentiary components and cannot ground the underlying decision.

**PacketValidationFunction (PVF).** The constitutionally separated validator for the EvidencePacketContract, positioned analogously to Companion 0's BoundaryValidationFunction but routing around the orchestrator by default on a B4 finding, since the orchestrator is a structurally likely source of packet narrowing.

**The decision axis (third axis of false stability).** Baseline capture corrupts the standard (vertical axis). Family incoherence corrupts the relation among standards (horizontal axis). Threshold capture corrupts the response function that converts an honestly measured deviation into governed action (decision axis), independent of both. None subsumes another.

**Threshold Capture (P_thr1).** The local, single-change failure: one threshold or trigger change fails SensitivityGrounded or IndependentOfMonitored, evaluated on its own terms. Distinct from P_thr5, the trajectory-level failure across many individually SensitivityGrounded changes. Traced end to end.

**Trigger Drift (P_thr2).** The trigger's own scope, routing, or firing-condition grammar degrades independent of the threshold value; may occur without any change to the threshold itself.

**False-Independence Mediated Capture (P_thr3a).** A packet component falsely claims independence, or the packet cannot be traced to its decision. Classified as an ordinary, not sovereign-terminal, primitive, because ComponentsIndependent and the source_independence_ledger supply an external, independently checkable standard.

**Evidentiary Sufficiency or Candidate-Selection Capture (P_thr3b).** A packet in which no independence claim is false, yet the decisive evidence is honestly monitored-process-derived (caught by the IndependenceSufficient floor) or the packet's components were drawn from a narrower candidate pool than an independent search would have surfaced (not caught by any conjunct this paper specifies). Accepted into the primitive family now, on the strength of its mechanically floored structural half; its candidate-selection subtype remains provisional until candidate-discovery instrumentation is specified, in the same posture as P_bnd5a/P_bnd5b and P_coh1's own candidate-discovery dependency.

**Cross-Surface Threshold Masking (P_thr4).** A threshold's authorized level on one surface interacts with another surface's standard or threshold in a way that hides expected escalation. A hybrid primitive whose structural half (ThresholdRelationsCoherent) is specified here and whose open half (NoSurfaceMasksAnother reading the paired ThresholdSet) remains an open extension of Coherence's own apparatus.

**Cumulative Threshold Creep (P_thr5).** The corpus's third sovereign-terminal primitive, after P_base5 and P_coh3, and the trajectory-level counterpart to P_thr1: a sequence of individually SensitivityGrounded threshold changes cumulatively raises the decision boundary past what the sovereign would author from a full review of the trajectory, with no single change in the sequence failing P_thr1. Detectable only by sovereign review of the threshold-change lineage, surfaced by ThresholdLineageSurfaced. Traced end to end.

**Threshold Conditioning Loop.** The compound feedback topology, not a primitive, in which a captured threshold lets a monitor under-report actionable drift, the unactioned drift compounds pressure toward further threshold laxity, and the lineage creeps toward P_thr5.

---

**Acknowledgments**

This work was developed under the Professor Bone Lab research identity as the fifth companion to Constitutional Runtime Computation v5.4, closing the threshold-authority residue named in Constitutional Baselines v1.2 and the evidence-packet-provenance residue named across Constitutional Baselines v1.2 and elevated to a deployment precondition in Constitutional Coherence v1.2. AEGIS serves as the worked domain. The v1.0 draft was written to pre-empt the recurring critiques of the prior companion review cycles: to govern the threshold and the trigger as objects distinct from the baseline rather than re-describing baseline authority with a substituted noun; to name the axis of threshold capture precisely rather than ranking it against its predecessors; to extend Companion 0's boundary-contract pattern rather than inventing a parallel evidentiary apparatus; to keep reachability separated from executability; to preserve primitive-versus-topology discipline; to reuse the B0 through B5 severity vocabulary rather than minting a parallel one; and to scope honestly rather than claiming premature closure. The v1.1 tightening pass was shaped by external critical review of v1.0 (verdict: accept with targeted revision before corpus freeze), which required the BaselineGeneration integration to be carried through formally rather than argued informally, the ThresholdSet schema expanded with a metric interface, P_thr1 separated cleanly from the trajectory-level P_thr5 rather than blurred across one worked example, P_thr3's ordinary classification narrowed to its genuinely mechanical form with a companion, explicitly open primitive for evidentiary sufficiency and candidate-selection capture, an IndependenceSufficient conjunct added to PacketConformant, a DirectSovereignAlert object defined to close the bypass-path question a B4 escalation otherwise leaves implicit, and the paper's closure language toned down from claiming the corpus's last residue to the two residues it actually closes. The v1.2 tightening pass was shaped by a second review (verdict: accept, minor revisions before corpus freeze), which confirmed the v1.1 architecture as sound and asked for five consistency and precision corrections: a stale figure label, an overstated abstract claim about the cross-surface threshold seam, a clarification that ThresholdRelationsCoherent validates lineage rather than re-adjudicating live on every generation use, an explicit acceptance statement for P_thr3b as a named primitive with its candidate-selection subtype held provisional, and a check that every closure claim in the paper is scoped to the two residues named rather than read as closing the corpus.

---

*v1.2. Tightening pass on second-review feedback (verdict: accept, minor revisions before corpus freeze). No architectural or predicate change; five precision and consistency corrections. (1) Figure 1's ThresholdPinAdmissible label corrected to show all five conjuncts (VersionPinned, ScopeMatched, MetricInterfaceMatched, GenerationPairMatched, PinLogged), matching the v1.1 predicate text the figure had fallen behind. (2) The abstract's fifth contribution is restated from "the worked resolution of the cross-surface threshold seam" to naming the seam's structural placement within BaselineGeneration as specified, with the full non-masking extension left an explicit open problem, matching the body's own posture; the abstract's evidence-packet-provenance paragraph is similarly qualified to name the mechanically detectable form as what is discharged, with the deeper evidentiary-sufficiency and candidate-selection form named rather than closed. (3) ThresholdRelationsCoherent is clarified, in Part II, to validate that each threshold-bearing member descends from a prior valid ThresholdChangeReachable event rather than re-adjudicating the change live on every generation use, and to state explicitly that it does not by itself complete the non-masking judgment required for cross-surface threshold masking. (4) P_thr3b's acceptance status is stated precisely, in both Part VI and Key Terms: it is accepted into the primitive family now on the strength of its mechanically floored structural half, in the same posture as P_bnd5a/P_bnd5b and P_coh1, with its candidate-selection subtype specifically held provisional until candidate-discovery instrumentation is specified. (5) Closure language is checked throughout for scope: every remaining "closes" or "discharges" claim is read against the two residues this paper actually closes rather than against the corpus as a whole. No new diagrams; Figure 3 unchanged. No em dashes.*

*v1.1. Tightening pass on external review feedback (verdict: accept with targeted revision before corpus freeze). Seven targeted revisions. (1) The BaselineGeneration integration is carried through formally: GenerationMember is redefined to `surface_id, baseline_version, threshold_set_version (optional)`, and GenerationPinAdmissible and GenerationCoherenceReachable are both explicitly restated with their new conjuncts (BaselinePinsAdmissible, ThresholdPinsAdmissible, ThresholdRelationsCoherent), each vacuously true for a generation with no threshold-bearing members so the extension is scoped rather than retroactive. (2) The ThresholdSet schema is expanded from four descriptive fields to a full fourteen-field schema including a metric interface (metric_ref, metric_output_type, comparison_operator, directionality, evaluation_window) and response and routing fields, and ThresholdPinAdmissible gains MetricInterfaceMatched and GenerationPairMatched, separating a metric-interface floor and a generation-skew check from the original ScopeMatched. (3) P_thr1 and P_thr5 are cleanly separated: P_thr1 is redefined as the local, single-change failure with its own single-change worked trace, and the six-change cumulative example is moved to a new P_thr5 traced-end-to-end section and to Part VII's Case one, explicitly relabeled as the P_thr5 case. (4) P_thr3 is split into P_thr3a (False-Independence Mediated Capture, retained as ordinary, PVF-detectable) and P_thr3b (Evidentiary Sufficiency or Candidate-Selection Capture, named as a distinct, explicitly unresolved hybrid primitive), narrowing the paper's ordinary-primitive claim to the case it can actually support. (5) PacketConformant gains three conjuncts, DecisionScopeMatched, ComponentRoleDeclared, and IndependenceSufficient, with a corresponding evidentiary_role field on EvidenceComponent and two new violation types (PRIMARY_EVIDENCE_NOT_INDEPENDENT, COMPONENT_ROLE_UNDECLARED). (6) The DirectSovereignAlert object is defined, closing the question of what crosses the direct-alert path on a B4 finding and stating explicitly that it cannot substitute for a conforming evidence packet. (7) Closure language in Part IX is revised from claiming the corpus's last residue to naming the two residues this paper actually closes, with the remaining corpus residues listed explicitly. Open Problems adds evidentiary sufficiency as a named residue distinct from evidentiary honesty, and notes that the packet-independence certificate problem is more consequential under the narrowed P_thr3a classification. Key Terms updated throughout to match. No new diagrams; Figure 3's labels and caption updated to name P_thr5 and P_thr3a explicitly. No em dashes.*

*v1.0. Initial version. Companion 5 to Constitutional Runtime Computation v5.3; closure of the threshold-authority residue named in Constitutional Baselines v1.2 (the four-object distinction and the threshold-capture failure) and the evidence-packet-provenance residue named across Constitutional Baselines v1.2 (the mediated-capture subtype of P_base1) and Constitutional Coherence v1.2 (elevated to a deployment precondition and scoped out on an axis argument). Contribution: the Trigger Authority Principle, derived through a six-step chain from the corpus rather than asserted; the four-object distinction (baseline, metric, threshold, trigger) made precise, with the ThresholdSet folded into the existing BaselineGeneration rather than requiring a new generation-level object; two predicates in the parent's CTLC notation, ThresholdChangeReachable (six conjuncts, SensitivityGrounded load-bearing) and ThresholdPinAdmissible (three conjuncts, L1-decidable), with the verdict structure and authority statuses; the EvidencePacketContract, extending Constitutional Boundary Contracts v1.0's six-component pattern to the evidence-packet-to-sovereign crossing that paper explicitly reserved, with PacketConformant (eight conjuncts, ComponentsIndependent and PackagingUnnarrowed load-bearing), a violation typology mapped onto the B0 through B5 severity classes, and the PacketValidationFunction as a constitutionally separated validator positioned to bypass the orchestrator on a B4 finding; the naming of the decision axis as a third, independent axis of false stability alongside baseline capture's vertical axis and family incoherence's horizontal axis; the P_thr primitive family (Threshold Capture, Trigger Drift, Evidence-Packet Mediated Capture, Cross-Surface Threshold Masking, Cumulative Threshold Creep) with P_thr1 traced end to end, P_thr3 explicitly classified as ordinary rather than sovereign-terminal, and P_thr5 classified as the corpus's third sovereign-terminal primitive; the Threshold Conditioning Loop named separately as the compound topology; the AEGIS worked example presenting two cases, a captured threshold defeating detection behind a fully coherent generation, and mediated capture caught by the EvidencePacketContract at the evidentiary input to a generation amendment that every structural conjunct in Constitutional Coherence v1.2 would otherwise have passed; the honest statement of the regress the evidence-packet apparatus itself creates and where it terminates; the five accountability mechanisms applied to the threshold and the evidence path; related work organized around threshold-as-tuning-parameter versus threshold-as-sovereign-constitutional-object. Specification status: ThresholdPinAdmissible, ThresholdChangeReachable, and PacketConformant fully specified; the cross-surface threshold-masking manner, the metric, the Threshold Trajectory Audit's counterfactual calculus, multi-sovereign trigger routing, and the packet-independence certificate named as boundaries rather than claimed closed. Three Mermaid diagrams styled to the parent palette. No em dashes.*
