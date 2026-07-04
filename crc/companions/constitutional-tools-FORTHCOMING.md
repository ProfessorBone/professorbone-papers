# Constitutional Tools: Capability Invocation, External Effects, and Tool-Result Admission in Governed Agentic Systems

**Status:** FORTHCOMING. Reserved slot, Companion 7 to Constitutional Runtime Computation v5.4.

**Position:** Companion 7. Sits alongside Constitutional Memory v2.1 as the other major agent-capability surface ORSR cannot leave ungoverned. Follows Constitutional Standing v1.2 in the reading order.

## Scope (fixed)

This paper argues that tool invocation is a constitutional transition surface, not a neutral capability call. If the substrate owns terminal execution authority, the parent paper's central claim, that authority cannot stop at Act while tool invocation remains agent-owned, because a tool can retrieve or fabricate evidence, mutate substrate or external state, shape future Observe, and produce real-world effects, all without ever passing through an Act event the parent's own apparatus was built to gate. A system in which the agent may call tools directly reintroduces agent sovereignty through the capability surface even where terminal actions are nominally governed.

The paper's central doctrine, stated plainly: the agent does not call tools, the agent submits ToolInvocationProposals; the substrate resolves tool reachability, invokes or refuses, admits or holds the result, and decides what downstream state the tool result may affect. A tool result has no constitutional force merely because a tool produced it, exactly as a favorable verdict has no causal force until bound (Constitutional Standing v1.2).

## What this paper is expected to introduce, subject to drafting and review

- The **Tool Sovereignty Principle**, derived in the manner of the corpus's other sovereignty principles (Baseline Sovereignty, Generation Coherence, Trigger Authority, Constitutional Standing), with a reference-monitor-equivalence corollary in the style of Constitutional Memory v2.1: complete mediation of tool use is substrate ownership, whatever a tool gateway's physical location.
- **ToolInvocationReachable(κ)**, governing whether a proposed tool invocation may occur, built from conjuncts including tool registration, operation typing, capability authorization, effect scoping, input grounding, side-effect admissibility, and result-boundary governance.
- A **tool-operation typology by constitutional effect, not implementation**: observation tools, evidence-producing tools, state-mutating tools, external-effect tools, authority-bearing tools, meta-tools, and composite tools, each with its own admissibility family, in the pattern Constitutional Memory v2.1 established for memory operation classes.
- **ToolResultRecord** and **ToolResultAdmissible(ρ)**, separating "the tool call emitted" from "the result may bind," the tool-layer analogue of the Binding/Continuation separation Constitutional Standing v1.2 establishes: a tool invocation can Emit while its result is independently Held.
- The **Tool Governance Boundary** as a stateful object mediating agent-to-tool invocation and tool-to-substrate result admission, extending the boundary-contract pattern Constitutional Boundary Contracts v1.0 establishes to this new crossing.
- A **P_tool primitive family**, expected to include at minimum tool invocation sovereignty violation, tool bypass through an alternate capability route (a direct tool-layer instance of v5.4 §6a's non-bypassability), tool-result laundering, evidence instrument overreach, capability escalation drift, tool registry drift, composite tool laundering, and tool-conditioned false stability (the tool-specific analogue of P_mem5).

## Required reading before drafting

- **Constitutional Runtime Computation v5.4** (core), especially §4's ORSR loop, §6a's HOLD completeness and non-bypassability apparatus, and the four-conjunct Reachable(τ) predicate this paper must not reopen.
- **Constitutional Boundary Contracts v1.0**, the boundary-contract pattern (schema, validation predicate, typed violation taxonomy, constitutionally separated validator, audit record, escalation rule) this paper is expected to extend to the tool-invocation and result-admission crossings.
- **Constitutional Memory v2.1**, the sibling capability-surface companion this paper is explicitly modeled against: its operation typology, its reference-monitor-equivalence argument, and its four authority statuses (ProposalWellFormed, AuthorityRouteable, ExecutableByRequester, SovereignAuthorizationRequired) are the direct precedent for this paper's own tool-operation classes and CapabilityAuthorized conjunct.
- **Constitutional Standing v1.2**, since a ToolInvocationProposal is itself a transition proposal subject to the Formation, Standing, Reachability, Binding, and Continuation pipeline that paper establishes; the AEGIS mandated-reporting worked example is expected to tie Tools directly to Standing and to §6a's HOLD completeness, not to re-derive them.

## Not yet resolved, to be settled during drafting

- The exact placement of MCP-server capability exposure within the meta-tool family, flagged as directly relevant to the Apex domain-application documents (a tool is not reachable merely because an MCP server exposes it; it becomes reachable only once registered, contracted, scoped, and authorized).
- Whether ToolCapabilityContract is its own object or a specialization of Companion 0's ProposalContract and ObservationContract pattern.
- Whether SLM-boundary enforcement in multi-small-language-model systems, evals at the boundary, enforced boundary contracts analogous to a MAS but for MSLMs, belongs in this paper's Open Problems or is deferred to a later companion.
- The paper is directed to close with three Open Problems, not the five to seven the working outline sketches; which three are the most load-bearing is a drafting decision, not fixed here.

---

*This is a reserved slot, not a draft. No content beyond this scope note has been written. See the series README for the current companion list and reading order.*
