# The Cognitive Horizon of an Agent
## A Structural Model of Operative Cognition in Agentic Systems

**Clarence "Professor Bone" Downs**
Professor Bone Lab | Johns Hopkins University, Agentic AI Certificate Program
Draft v6, Revised

---

## Abstract

This paper introduces the **Cognitive Horizon** as a structural framework for diagnosing a failure mode that is common in production agentic systems but rarely formalized: an agent fails to act on information that was technically available to it, not because retrieval failed, but because the information never became behaviorally operative.

The central contribution is a distinction between *latent state*, information present in the agent's context, and *operative state*, information actively shaping behavior. This distinction reframes many apparent knowledge failures as gating failures: structural suppressions of information the agent already possessed.

The paper develops a control model of operative cognition:

> **Cognition ≈ State × Attention × Policy**

It presents a three-question diagnostic protocol for isolating the layer at which a gating failure occurred, illustrates the model through a concrete logistics scenario drawn from distributed decision-making under operational constraints, examines temporal desynchronization as a source of instability across control layers, and connects the framework to second-order governance risks in multi-agent systems.

The model is offered as a working abstraction, intended for empirical stress-testing and refinement across complex decision environments.

---

## 1. Motivation: A Failure That Gets Misdiagnosed

Production agentic systems fail in a particular way that is both common and consistently misunderstood.

An agent is tasked with a decision. The relevant information was retrieved. The retrieval logs confirm it entered the context window. The agent even surfaces it during intermediate reasoning. Yet when the decision point arrives, the agent acts as though the information was never there.

The standard diagnosis attributes this to memory failure. The standard remediation is improved retrieval, expanded context windows, or additional memory indexing. These interventions address the wrong layer. The information was present. Retrieval was not the failure.

This paper proposes that such cases are better understood as gating failures: situations in which information was technically present but structurally prevented from becoming operative. The Cognitive Horizon framework provides the vocabulary and the diagnostic structure to investigate them precisely.

Practitioners working in complex decision environments, including autonomous logistics systems, multi-agent planning architectures, and distributed AI-assisted command support, will recognize this failure pattern immediately. Formalizing it enables more targeted diagnosis and more effective remediation.

---

## 2. Framing: Latent vs. Operative State

Before introducing the full control model, it is useful to establish the core distinction that motivates it. Doing so early allows the reader to interpret everything that follows through the right lens.

**Latent state** refers to information that is present in an agent's active context but not actively shaping its planning, tool selection, or decisions. The information is there. It is accessible in principle. It is not working.

**Operative state** refers to the subset of an agent's active context that is simultaneously salient to the attention mechanism and permitted by the policy layer to influence action. This is the information the agent is actually reasoning from.

These two categories are not the same. The difference between them is where most production failures live.

The Cognitive Horizon framework is built around this distinction. The sections that follow develop its formal structure, identify the mechanisms by which information becomes stranded in latent state, and provide a concrete diagnostic protocol for locating the failure layer.

---

## 3. The Boundary Condition

The foundational claim of the Cognitive Horizon model is straightforward.

Let S(t) represent the active state of an agent at time t: everything in its context window, working memory, and immediately accessible buffers at that moment.

**Claim:** If information x is not present in S(t), then x cannot influence cognition at time t.

Formally:

```
x ∉ S(t) → x ∉ C(t)
```

Where C(t) denotes the cognitive space: the set of information capable of shaping reasoning and action at time t.

This claim follows directly from the computational structure of language model inference. The model attends only to what is in its context. Long-term memory systems, whether episodic stores, vector databases, or semantic indexes, represent stored potential. They hold information that could be relevant. Potential is not cognition. Information becomes cognitively relevant only when retrieved and injected into active state.

State defines the outer boundary of the Cognitive Horizon. Nothing outside that boundary can influence behavior at time t.

This boundary condition is necessary and well-established. It is not, however, sufficient to explain the failure pattern described in Section 1. An agent that has retrieved the relevant information has crossed the outer boundary. The failure lies inside it.

---

## 4. The Control Model: From Boundary to Operative Cognition

The boundary model explains failures at retrieval. It does not explain failures that occur after successful retrieval.

Careful observation of production systems reveals a second class of failure: information enters state, is confirmed present, and remains behaviorally inert. The agent does not suppress it deliberately. It simply does not use it. This class of failure requires a more granular model.

Operative cognition at time t can be approximated as a nested function of three interacting factors:

```
C(t) ≈ P(t)( A(t)( S(t) ) )
```

Where:
- **S(t)** defines what information is feasible: the outer boundary
- **A(t)** determines what is salient: what the attention mechanism weights and surfaces
- **P(t)** determines what is permitted to influence action: the policy layer

This formulation is not additive. It is nested. Attention operates on state. Policy operates on the output of attention. Each layer is a filter. Information that survives the first filter can still be blocked by the second.

### 4.1 What Each Layer Does

**State** is the container. It defines the maximum possible cognitive horizon at any given moment. Schema design, retrieval quality, and context window management all determine what enters this layer.

**Attention** is the selector. Within state, not all information receives equal weight. Recency, relevance scoring, salience signals, and positional effects within the context window all influence which information rises to the surface of active reasoning. Information that is low-ranked by the attention mechanism may be present in state but functionally invisible during decision execution.

**Policy** is the governor. Even information that is both present and salient can be blocked from influencing action by the policy layer: governance constraints, cost functions, behavioral guardrails, or role-specific restrictions that define what the agent is permitted to do with what it knows.

The transition from latent to operative requires clearing all three layers. Failure at any one of them produces a gating failure.

### 4.2 A Worked Example: Forward Logistics Resupply

To make this concrete, consider a forward logistics element operating an AI-assisted resupply planning agent in a contested environment.

The agent has been tasked with generating a resupply route recommendation for an element that has reported critically low ammunition stocks. The agent's state contains:

- A current route database updated four hours ago
- An intelligence summary flagging Route BLUE as contested based on a report from six hours ago
- A real-time sensor feed showing Route BLUE has been clear for the past two hours
- A standard operating procedure (SOP) mandating avoidance of any route flagged as contested within the past twelve hours

The agent recommends Route GREEN, a longer and more exposed alternative. The commander asks why Route BLUE was not selected given the recent sensor data.

The answer is a gating failure, and the model identifies exactly where it occurred.

**State:** All relevant information was present. The sensor feed showing Route BLUE clear entered state successfully. Retrieval did not fail.

**Attention:** The sensor feed was salient. The agent surfaced it during intermediate reasoning and noted the discrepancy with the intelligence summary.

**Policy:** The SOP governing route selection flagged Route BLUE as ineligible. The twelve-hour avoidance window was still active. The policy layer blocked the sensor data from influencing the final recommendation, not because the agent failed to see it, but because the governance constraint prevented it from acting on it.

This is a policy-layer gating failure. The sensor data was operative at the attention layer and inert at the policy layer. The fix is not improved retrieval. It is not better attention design. It is a policy review: whether the twelve-hour avoidance window is appropriately calibrated for the rate at which battlefield conditions evolve, and whether the agent's policy layer should include a mechanism for escalating conflicting sensor data to human review rather than silently suppressing it.

This distinction has direct operational consequences. Diagnosing the failure correctly determines where the intervention goes.

---

## 5. Gating Failures: A Structural Taxonomy

A gating failure occurs when an agent possesses relevant information but is structurally prevented from acting on it. The failure is architectural. The agent is not missing knowledge. It is suppressing knowledge through mechanisms that, from the agent's internal perspective, are operating correctly.

Four structural causes appear most frequently in production systems.

**Attention suppression.** A relevant signal is present in state but ranked below the salience threshold necessary to surface during decision execution. High-frequency, high-recency, or high-confidence signals crowd it out. The agent does not ignore the information deliberately. The attention mechanism simply never elevates it above competing content.

**Policy blocking.** The information is salient but constrained by governance rules, cost functions, or behavioral guardrails that prevent the agent from acting on what it knows. When policy is well-calibrated, this suppression is intentional and correct. When policy is outdated or miscalibrated relative to current operating conditions, it silently suppresses valid reasoning with no visible error signal.

**Spurious signal dominance.** Attention is captured by noise: irrelevant but high-weighted information that crowds out the signal that matters. The agent is not reasoning poorly. It is reasoning well over the wrong subset of its state.

**Policy-state misalignment.** The policy was calibrated for a prior state configuration. State has since evolved, but the policy has not been updated. The agent applies correct rules to an incorrect model of the current situation. The Route BLUE example in Section 4.2 is an instance of this failure type.

In every case, the system possesses the knowledge. The failure is in the gating architecture that separates latent from operative. The remediation is not more data. It is better gating design.

---

## 6. Temporal Desynchronization

State, attention, and policy do not evolve at the same rate. This asymmetry is a structural property of any system with layered governance, and it produces a distinct class of instability that deserves careful treatment.

**State** is highly reactive. It changes when new inputs arrive, when environmental signals shift, or when tools return unexpected output. In a dynamic operational environment, state can update continuously.

**Attention** reallocates fluidly in response to state changes. It is fast relative to policy, though not instantaneous, and it can be manipulated by salience-boosting inputs that may or may not reflect genuine operational priority.

**Policy** is designed to be stable. Governance constraints, institutional guardrails, and cost functions are intentionally resistant to rapid change. Stability is a feature: it prevents the agent from overreacting to noise, maintains consistency across similar situations, and ensures that behavioral boundaries remain predictable. But stability has a cost when the environment changes faster than the policy layer can track.

When these three layers update at mismatched rates, a specific form of instability emerges.

### 6.1 The Lagging Policy Scenario

Consider a sustained operation in which the ground situation evolves significantly over a twelve-hour period. State updates continuously as sensor feeds, intelligence reports, and communication logs flow in. Attention reallocates appropriately as new priorities emerge. The policy layer, however, is based on a threat model from the operation's initial planning phase.

By hour eight, the policy layer is governing decisions based on a threat picture that no longer reflects conditions on the ground. Novel signals, including indicators of changed route viability, altered resupply windows, and shifted asset availability, are present in state and surfaced by attention. The policy layer suppresses them because they conflict with constraints derived from an outdated operational model.

From outside the system, the agent appears to underreact. It seems to be ignoring information that is clearly relevant. It may even surface that information in intermediate reasoning while failing to incorporate it into its final recommendation. The behavior appears irrational.

From inside the system, everything is consistent. The agent is applying its policy correctly. The policy is simply calibrated for a situation that no longer exists.

This is temporal desynchronization: the control layers are operating on different clocks, and the misalignment is producing systematically degraded output.

### 6.2 The Overreactive Attention Scenario

The reverse failure is equally consequential. A high-salience signal arrives, perhaps an urgent message from a forward element or an anomalous sensor reading, and the attention layer reallocates aggressively before the policy layer can apply appropriate constraints. The agent abandons prior reasoning in favor of the most recent high-priority input, even when that input is noise or represents an edge case that the policy layer would have correctly deprioritized.

The agent appears to overreact: inconsistent, volatile, easily distracted from its primary task.

### 6.3 Diagnostic Implication

An agent that behaves inconsistently over time without any change in its underlying model or configuration may be experiencing temporal desynchronization rather than capability degradation. The distinction matters operationally.

Capability degradation is addressed through model updates, retraining, or replacement. Temporal desynchronization is addressed through policy recalibration: updating the governance layer to reflect current operating conditions rather than the conditions that existed when the policy was originally designed.

Stability, in this framework, is not merely output accuracy. It is alignment across control-layer time constants. Systems operating in rapidly changing environments require mechanisms for detecting and correcting policy lag before it produces mission-significant errors.

---

## 7. Diagnostic Protocol: Three Questions

The practical value of this framework lies in the precision it brings to failure investigation.

The standard diagnostic question when an agent behaves unexpectedly is: did it remember? This question leads to retrieval investigations, context window audits, and memory system reviews. These investigations are appropriate when the failure occurred at the retrieval layer. They are counterproductive when the failure occurred inside the Cognitive Horizon, after successful retrieval.

The Cognitive Horizon framework replaces that single question with three, asked in sequence. This protocol is signposted here because it is the paper's most operationally useful contribution. The sections above develop its theoretical basis. This section states it plainly.

**Question 1: Was the information retrieved into state?**
If no, this is a retrieval failure. The information never crossed the outer boundary of the Cognitive Horizon. The intervention belongs in the retrieval mechanism: indexing, query formulation, or memory architecture.

**Question 2: Was the information made salient by the attention mechanism?**
If yes to Question 1 but no to Question 2, this is an attention failure. The information entered state but was ranked below the salience threshold necessary to surface during decision execution. The intervention belongs in attention design: salience scoring, positional weighting, or retrieval re-ranking.

**Question 3: Was the information permitted by the policy layer to influence action?**
If yes to Questions 1 and 2 but no to Question 3, this is a policy failure. The information was present and salient, but governance constraints blocked it from influencing the final decision. The intervention belongs in policy review: threshold calibration, conflict escalation mechanisms, or human-in-the-loop routing for cases where policy and evidence diverge.

Only when all three questions return yes should the agent be expected to have acted on the information. Failure despite all three being satisfied is a reasoning failure, and a distinct investigation.

This protocol reframes agent evaluation from memory accuracy to structural operability. The question is not what the agent knew. It is what the agent was structurally capable of using.

That distinction produces more targeted diagnoses and more effective interventions.

---

## 8. Multi-Agent Extension

In a single-agent system, the Cognitive Horizon is one agent's problem to manage.

In a multi-agent system, each agent maintains its own State × Attention × Policy configuration. Those configurations interact across agent boundaries. And the interactions produce failure modes that no individual agent's Cognitive Horizon can diagnose or prevent.

The central risk in governed multi-agent systems is that an orchestrator, the policy engine sitting above all agents, introduces a higher-order policy layer that shapes the Operative State of every agent it governs. The orchestrator determines what agents are permitted to reflect on, what information propagates across boundaries, and what gets committed to long-term memory.

This creates a structural vulnerability: if the orchestrator's policy layer develops systematic biases through continuous exposure to the agents it governs, it begins to distort the Cognitive Horizon of every agent in the system simultaneously. Not by altering their state. Not by manipulating their attention. By reshaping their policy layer from above.

Each agent continues to function correctly within its individual Horizon. The Horizons themselves have been corrupted by the governance layer they depend on.

This failure mode, Orchestrator Epistemic Capture, is the multi-agent analog of the policy-layer gating failure described in Section 5. Its detection and remediation require governance mechanisms that sit outside the orchestrator's own epistemic frame: independent Meta-evaluation, shadow policy comparison, and ground truth reconciliation against real-world outcomes.

The full architectural treatment of Orchestrator Epistemic Capture is developed in a companion document. Its connection to the Cognitive Horizon model is direct: epistemic capture is what happens when the P(t) component of the master governance layer drifts, and no mechanism exists to audit it from outside.

This multi-agent extension is offered as a research direction rather than a completed analysis. The interaction between individual agent Cognitive Horizons and orchestrator-level policy layers warrants formal treatment that exceeds the scope of this paper.

> **PACS Implementation Note (2026-03-05):** The argument developed in this section directly governed a structural decision in the PACS architecture. The Meta-Evaluation Checkpoint — the component that governs the Managing Orchestrator's three protected injection points — was specified as one unified component rather than three separate validators. The reasoning: policy is one function with one authority. P(t) is a single governance layer. Splitting the Checkpoint into three separate components would risk exactly the temporal desynchronization failure described in Section 6 of this paper, where independent validators diverge in calibration, threshold semantics, and enforcement strength until the governance model loses coherence from the outside. One Checkpoint. One epistemic frame. Three internal validation pathways differentiated by logic, not by authority.

---

## 9. Connections to Related Work

**SOAR and ACT-R.** Classical cognitive architectures distinguished between working memory and long-term memory in ways that anticipate the Latent/Operative State distinction developed here. SOAR's central claim, that working memory is not merely a buffer but the space in which reasoning occurs, aligns with the argument that presence in state does not guarantee operability. ACT-R's buffer-mediated architecture anticipates the multi-layer gating model: each buffer represents a filtering and selection step between stored knowledge and active reasoning.

**CoALA (Sumers et al., 2024).** The Cognitive Architectures for Language Agents framework established working memory as the organizing construct for language agent design. This paper accepts that foundation and extends it. Working memory defines the outer boundary of the Cognitive Horizon. Operative cognition requires the additional conditions of attention salience and policy permission, which CoALA does not fully theorize.

**Reflexion (Shinn et al., 2023).** Reflexion's verbal reinforcement loop assumes that retrieved reflections will influence future agent behavior. The Cognitive Horizon model identifies an implicit vulnerability in that assumption. Reflections that enter state as latent, present but not operative, do not improve agent behavior. They accumulate without effect or generate noise that crowds out more salient signals. The framework developed here predicts specific conditions under which Reflexion-style self-improvement will fail silently.

**Generative Agents (Park et al., 2023).** The memory stream architecture distinguishes between comprehensive experience logging and selective memory activation through retrieval and reflection. This is the Latent/Operative distinction operating under a different name. Their retrieval mechanism, which weights memories by recency, importance, and relevance, is an attention mechanism: a system for moving information from latent to operative based on contextual priority.

---

## 10. Limitations and Future Directions

This model is a working abstraction. Several limitations require acknowledgment.

The formulation C(t) ≈ P(t)(A(t)(S(t))) is conceptual rather than mathematical. Attention and policy are treated as abstract filters rather than formally specified functions. Future work should ground these in measurable constructs: attention weight distributions, policy constraint graphs, and state coverage metrics that can be instrumented in production systems.

The temporal desynchronization claim is theoretically coherent but empirically unvalidated in the agentic AI context. The claim that misaligned update rates across control layers produce systematically degraded output requires controlled experimental validation. Designing studies that isolate this effect from other sources of instability is a meaningful near-term research direction.

The multi-agent extension is sketched rather than fully developed. The interaction between individual agent Cognitive Horizons and orchestrator-level governance deserves formal treatment as a first-class research problem. This is particularly relevant for high-stakes decision environments where the consequences of orchestrator-level bias are significant and potentially irreversible.

The three-question diagnostic protocol is a practitioner framework, not a validated instrument. Its utility should be tested against documented production failure cases to determine whether it reliably distinguishes retrieval failures from attention failures from policy failures, and whether the distinctions reliably predict effective interventions.

---

## 11. Conclusion

Many agent failures that present as knowledge deficits are, on closer examination, gating failures: structural suppressions of information the system already possessed.

The Cognitive Horizon framework provides the vocabulary to make this distinction, the formal model to locate the failure layer, and the diagnostic protocol to guide intervention.

State defines what is possible. Attention shapes what is noticed. Policy determines what is permitted. Operative cognition requires alignment across all three. When that alignment breaks down, the failure is architectural, and the remediation must be architectural as well.

This matters most in environments where the consequences of misdiagnosis are significant: where adding more memory to a system with a policy-layer failure wastes resources and leaves the underlying problem intact, and where recalibrating attention in a system with retrieval failure misses the problem entirely.

The model is offered as a working tool for practitioners engaged in building, evaluating, and debugging complex agentic systems. It is intended to invite refinement, empirical testing, and extension into domains where the stakes of getting this right are high.

---

## References

Anderson, J. R. (1996). ACT: A simple theory of complex cognition. *American Psychologist, 51*(4), 355-365.

Anderson, J. R., & Lebiere, C. (1998). *The atomic components of thought.* Lawrence Erlbaum Associates.

Kotseruba, I., & Tsotsos, J. K. (2020). 40 years of cognitive architectures: Core cognitive abilities and practical applications. *Artificial Intelligence Review, 53*(1), 17-94.

Laird, J. E., Newell, A., & Rosenbloom, P. S. (1987). SOAR: An architecture for general intelligence. *Artificial Intelligence, 33*(1), 1-64.

Laird, J. E. (2022). *The Soar cognitive architecture.* MIT Press.

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *Proceedings of UIST 2023.*

Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 2023.* arXiv:2303.11366.

Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024). Cognitive architectures for language agents. *Transactions on Machine Learning Research.*

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). ReAct: Synergizing reasoning and acting in language models. *ICLR 2023.*

---

*Professor Bone Lab*
*Draft v6, Revised*
*Classification: Working paper, empirical validation and peer review invited*
