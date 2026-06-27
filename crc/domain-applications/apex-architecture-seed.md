# Apex — Architecture Seed Document

**Project:** Apex — Governed Agentic Bug Bounty Hunter
**Author:** Clarence "Faheem" Downs (Professor Bone Lab)
**Status:** Ideation / Pre-Architecture
**Date:** 2026-06-10
**Machine:** Hannibal (MacBook Pro M4 Max)

---

## 1. What Is Apex?

Apex is a constitutionally governed agentic system designed for bug bounty hunting. It is not simply an automated vulnerability scanner. It is a red team agent — an offensive security system that operates inside a constitutional governance substrate that controls its behavior, enforces scope boundaries, and produces audit trails for every action it takes.

The name "Apex" reflects the system's architectural position: it sits at the top of a layered intelligence stack, coordinating graph traversal, vulnerability signature classification, and retrieval — all governed by constitutional runtime architecture derived from the AEGIS/CTLC framework.

**What makes Apex different from existing automated security tools:**

Most automated bug hunters work linearly — file by file, function by function. They read code like a book. Apex works topologically. It maps the entire codebase as a knowledge graph first, then reasons about the full attack surface simultaneously. It sees not just individual vulnerable functions but the paths between them — multi-hop vulnerability chains that are invisible to linear analysis.

And it does all of this under constitutional governance. An ungoverned offensive agent operating at Apex's speed is a legal and ethical liability. The constitutional layer is not a feature. It is what makes Apex operable in a real bug bounty context.

---

## 2. Origin of the Idea

This architecture emerged from a conversation on 2026-06-10 connecting three threads:

1. **Bug bounty programs** — companies like Apple paying researchers $1M–$2M+ for critical vulnerability disclosures. Apple recently raised its maximum bounty to $2M (announced at Hexacon 2025), with bonus structures potentially exceeding $5M.

2. **KGCompass** — a research system that maps codebases as knowledge graphs and uses multi-hop traversal to find bugs that pure LLMs cannot locate.

3. **Professor Bone Lab's constitutional governance architecture** — the CTLC/ORSR/CRA framework developed through AEGIS, formalized in the Constitutional Runtime Computation paper (v5.3) and its companion paper "The Knowledge Graph as Constitutional Substrate."

The convergence: KGCompass uses graph traversal to find where bugs live in a codebase. The constitutional substrate uses graph traversal to determine whether an agent transition is constitutionally reachable. The traversal logic is structurally identical. The difference is what the graph encodes. Apex unifies both in a single system.

---

## 3. Three-Layer Architecture (Initial Sketch)

```
┌─────────────────────────────────────────────────────┐
│           LAYER 3 — Constitutional Substrate         │
│  CTLC governs what Apex is allowed to do with        │
│  findings. Enforces bug bounty scope. Routes         │
│  escalations. Produces constitutional audit trails.  │
│  Sovereign: Faheem (or designated principal)         │
└─────────────────────┬───────────────────────────────┘
                      │ adjudicates all transitions
┌─────────────────────▼───────────────────────────────┐
│           LAYER 2 — Vulnerability Signature Model    │
│  ML model trained on known vulnerability datasets.  │
│  Exposed as a callable tool. Classifies code         │
│  patterns by CWE type. Operates at the semantic      │
│  level (what code does, not just what it looks like).│
│  New vulnerabilities have similar signatures to      │
│  known classes — the model generalizes.              │
└─────────────────────┬───────────────────────────────┘
                      │ classifies nodes during traversal
┌─────────────────────▼───────────────────────────────┐
│           LAYER 1 — Knowledge Graph Engine           │
│  KGCompass-style graph maps the target codebase:     │
│  files, classes, functions, call chains,             │
│  dependencies, issues, PRs. Graph is language-       │
│  agnostic and incrementally updatable.               │
│  Multi-hop traversal finds what LLMs cannot.         │
└─────────────────────────────────────────────────────┘
```

**How the layers interact:**

- The graph (Layer 1) tells Apex *where to look* — it identifies the topology of the target codebase and surfaces candidate locations.
- The signature model (Layer 2) tells Apex *what it's looking at* — it classifies each candidate node against known CWE patterns.
- The constitutional substrate (Layer 3) governs *what Apex does next* — it determines whether a proposed action (reporting, escalating, further probing) is within authorized scope and constitutionally reachable.

**The critical insight — multi-hop vulnerability chains:**

The signature model doesn't just run on individual functions in isolation. It runs *along graph traversal paths*. When Apex finds a function that scores high on a CWE signature, it traverses the graph: who calls this function? What data flows into it? Where does untrusted input enter the call chain? The signature model fires on the node. The graph reveals the blast radius.

This combination catches multi-hop vulnerability chains — cases where no single function is independently vulnerable but the *path through them* creates the vulnerability. Those are the high-value findings.

---

## 4. Key Research and Repositories

### 4.1 KGCompass — Knowledge Graph Enhanced Software Repair

**What it is:** Repository-level software repair framework that builds a knowledge graph of the codebase (files, classes, functions, issues, PRs) and uses multi-hop path-guided traversal to localize bugs and generate patches.

**Why it matters to Apex:** The graph construction and multi-hop traversal logic is the engine for Layer 1. Apex repurposes it offensively — mapping attack surface instead of bug locations for repair.

**Key numbers:**
- 58.3% resolve rate on SWE-bench Lite (state-of-the-art for open-source single-LLM approaches)
- 69.7% of successfully localized bugs required multi-hop traversal — pure LLMs cannot find them
- 89.7% of successfully localized bugs had no explicit location hint in the issue
- $0.20 per repair on a 27,000-function codebase
- Lifts resolved rate by 50.8% on Claude Sonnet 4 over pure-LLM baseline
- Graph is language-agnostic and incrementally updatable
- Uses Neo4j as the graph database backend
- Uses `jina-embeddings-v2-base-code` for mixed natural language / code embeddings

**Links:**
- GitHub: https://github.com/GLEAM-Lab/KGCompass
- Paper (arXiv): https://arxiv.org/abs/2503.21710
- PDF: https://arxiv.org/pdf/2503.21710
- Organization: GLEAM-Lab (GitHub: https://github.com/GLEAM-Lab)

**Citation:**
```
@article{yang2025enhancing,
  title={Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs},
  author={Yang, Boyang and Ren, Jiadong and Jin, Shunfu and Liu, Yang and Liu, Feng and Le, Bach and Tian, Haoye},
  journal={arXiv preprint arXiv:2503.21710},
  year={2025}
}
```

**Infrastructure requirements:** Docker + Docker Compose, NVIDIA GPU, NVIDIA Container Toolkit, Neo4j with plugins.

---

### 4.2 Harness-1 — Stateful Search Agent

**What it is:** A 20B retrieval subagent trained with reinforcement learning inside a stateful search harness. The harness maintains environment-side working memory (candidate pool, curated evidence set, evidence graph, verification records). The policy makes semantic search decisions. The harness handles all bookkeeping. The authors call this principle "stateful cognitive offloading."

**Why it matters to Apex:** Harness-1 is the retrieval layer — it searches for external knowledge (CVE records, exploit patterns, security advisories, prior findings) and feeds that intelligence into Apex's reasoning. It does not fix code and it does not build codebase graphs. It is a companion to KGCompass, not a replacement.

**Key connection to constitutional architecture:** Harness-1's principle of separating semantic decisions from state management is structurally analogous to ORSR's separation of agent inference from substrate adjudication. The harness is a lightweight form of what the constitutional substrate does at a governance level. This is not coincidental — it reflects a deeper principle: when you separate cognitive labor from state management, both become more tractable.

**Key numbers:**
- 0.730 average curated recall across 8 benchmarks
- Beats next open subagent (Tongyi DeepResearch 30B) by 11.4 points
- Second only to Opus-4.6 among all systems tested (including frontier models)
- +17.0 points on held-out benchmarks vs +7.9 on source-family (2.2x transfer gap — domain-general)
- Trained on only 4,352 unique items (899 SFT + 3,453 RL)
- Removing harness mechanisms drops recall 12.2% relative

**Links:**
- GitHub: https://github.com/pat-jj/harness-1
- Paper (arXiv): https://arxiv.org/abs/2606.02373
- PDF: https://arxiv.org/pdf/2606.02373
- Model weights (HuggingFace): https://huggingface.co/pat-jj/harness-1
- HuggingFace paper page: https://huggingface.co/papers/2606.02373

**Citation:**
```
@article{jiang2026harness,
  title={Harness-1: Reinforcement Learning for Search Agents with State-Externalizing Harnesses},
  author={Jiang, Pengcheng and Shi, Zhiyi and Hong, Kelly and Xu, Xueqiang and Sun, Jiashuo and Sun, Jimeng and Bashir, Hammad and Han, Jiawei},
  journal={arXiv preprint arXiv:2606.02373},
  year={2026}
}
```

**Infrastructure:** Servable via vLLM, SGLang, or Transformers. Requires CUDA-compatible NVIDIA GPU. Python 3.11+.

---

## 5. Vulnerability Signature Model — Training Data Sources

The signature model (Layer 2) requires training on labeled vulnerability datasets. The following are the most established and widely cited public datasets in this domain:

### Big-Vul
- 3,754 CVEs from 348 open-source C/C++ projects
- 91 CWE types, spanning 2002–2019
- Contains both vulnerable code and fixed versions (paired — critical for training)
- 10,547 vulnerable functions, 168,752 non-vulnerable functions
- Widely used as the standard benchmark in vulnerability detection research
- GitHub: https://github.com/ZeoVan/MSR_20_Code_vulnerability_CSV_Dataset

### CVEFixes
- 5,365 vulnerabilities across 1,754 projects
- 180 CWE types, spanning 1999–2021
- Automatically fetches CVE records from NVD with corresponding source-level fixes
- Complements Big-Vul for broader language coverage

### SARD (Software Assurance Reference Dataset)
- NIST-maintained dataset of synthetic vulnerable code samples
- Tagged by weakness type (CWE-based)
- Useful for rare CWE classes underrepresented in real-world corpora
- Link: https://samate.nist.gov/SARD/

### NVD (National Vulnerability Database)
- 200,000+ documented vulnerabilities with CWE classifications
- The authoritative upstream source — most datasets are derived from it
- Link: https://nvd.nist.gov/

### DiverseVul
- Broader language coverage than Big-Vul
- Built from CVEFixes, BigVul, and CrossVul
- Designed specifically for deep learning–based vulnerability detection
- Paper: https://surrealyz.github.io/files/pubs/raid23-diversevul.pdf

### Key training consideration
The signature model must operate at the **semantic level** — understanding what code does, not just what it looks like. A model trained purely on code text will be fooled by variable renaming, reformatting, or language-specific idioms. The embedding layer should use a code-semantic model (e.g., `jina-embeddings-v2-base-code`, which KGCompass already uses) rather than surface-level tokenization.

---

## 6. Professor Bone Lab Constitutional Papers (Governing Layer)

The constitutional substrate for Apex is derived from the governance architecture developed through AEGIS. The two directly relevant papers:

### Constitutional Runtime Computation (v5.3)
**Author:** Clarence "Faheem" Downs (Professor Bone Lab)
**Location in vault:** `Projects/_Learning/Constitutional-Runtime-Computation-v5.3.md`

Establishes the CTLC framework, ORSR loop, L1/L2 separation, Q/P ontology, and constitutional reachability as the governing architecture. The central claim: governance should define the topology of reachable state transitions, not merely constrain behavior after the fact. The governing question changes from "is this output good?" to "may this transition constitutionally occur from current substrate state?"

For Apex, this means: every offensive action the system proposes — probing a function, traversing a dependency, generating a report, escalating a finding — is a typed transition that must pass constitutional adjudication before execution.

### The Knowledge Graph as Constitutional Substrate
**Author:** Faheem Downs (Professor Bone Lab)
**Location in vault:** `Projects/_Learning/The-Knowledge-Graph-as-Constitutional-Substrate.md`

Companion paper arguing that the constitutional substrate's natural implementation is a knowledge graph. Constitutional reachability IS graph traversal. CTLC inputs are relationships, not flat data. The Prior Graph is structurally a knowledge graph.

**The convergence for Apex:** This paper was written about clinical governance (AEGIS). But its structural claim transfers directly: the codebase knowledge graph (Layer 1) and the constitutional governance graph (Layer 3) are the same computational form. A single graph architecture can encode both the target codebase topology AND the governance rules that constrain how Apex operates within it. This is not an analogy. It is the same data structure serving two functions.

---

## 7. Legal and Ethical Constraints (Non-Negotiable)

Bug bounty programs operate under strict legal boundaries. Apex must be constitutionally governed from the ground up — not as a feature, but as a legal requirement.

**Relevant law:** The Computer Fraud and Abuse Act (CFAA) criminalizes unauthorized access to computer systems. An agent operating outside the defined scope of a bug bounty program crosses from ethical hacking into federal criminal territory, regardless of intent.

**Constitutional scope enforcement:** Apex's CTLC layer must encode the specific scope of each bug bounty program as constitutional constraints. Out-of-scope targets are constitutionally unreachable — not just filtered by policy, but structurally unavailable as valid transitions. This is the road topology distinction from the CRC paper: the road to the out-of-scope target simply does not exist in the constitutional graph.

**Audit trails:** Every action Apex takes must produce a constitutional trace entry. Bug bounty programs require disclosure of methodology. The CTLC audit trail is not just governance infrastructure — it is the disclosure artifact.

**Faith constraint:** All Apex operations remain under the same Islamic ethical framework that governs Professor Bone Lab work broadly. This is a top-level constraint, not a policy layer.

---

## 8. Efficiency Profile (Initial Estimate)

Based on KGCompass benchmarks and the architectural analysis:

- **Cost:** Sub-dollar per full codebase vulnerability sweep (KGCompass is $0.20 per repair on a 27,000-function codebase; Apex's search operation is cheaper than repair)
- **Speed:** Sub-millisecond graph traversal for 3–5 hop queries; full sweep in minutes for large codebases
- **Coverage:** Multi-hop traversal finds 69.7% of bugs that pure LLMs miss entirely
- **Blast radius detection:** Graph traversal automatically surfaces all dependent functions when a vulnerability node is found — single finding becomes full cascade report
- **Consistency:** Constitutional governance ensures the same rigor applies to the 10,000th function as to the first

**Current limitation — novel exploit classes:** The signature model generalizes across known CWE classes and their variants. Genuinely novel exploit classes (new attack paradigms with no prior CWE analog) remain outside the model's reliable detection range. This is an active research problem in the security community, not a fixable gap at this stage.

**Current limitation — business logic vulnerabilities:** Vulnerabilities that only make sense with knowledge of what the software is *supposed* to do are harder to catch through structural traversal alone. Graph topology can identify structural anomalies; it cannot substitute for domain understanding of business intent.

---

## 9. Next Steps

- [ ] Deep study of KGCompass repo — Step 2 (clone and read README)
- [ ] Step 3: Identify the graph builder module in KGCompass
- [ ] Step 4: Trace one full repair end-to-end through KGCompass pipeline
- [ ] Step 5: Document what KGCompass does NOT do that a red team agent needs
- [ ] Explore Harness-1 integration as the retrieval layer
- [ ] Research existing vulnerability signature models (SecureFalcon, MoEVD) as starting points for Layer 2
- [ ] Draft the constitutional scope specification format for bug bounty programs
- [ ] Design the Apex ORSR loop — how CTLC adjudicates offensive transitions
- [ ] Identify first target bug bounty program for proof-of-concept scoping

---

## 10. Open Questions

1. **Graph unification:** Can the codebase topology graph and the constitutional governance graph be unified in a single Neo4j instance, or do they need to be separate graphs with cross-references?

2. **Scope encoding:** What is the right formal representation for bug bounty scope rules as constitutional constraints in the CTLC framework?

3. **Signature model architecture:** Fine-tune an existing code model (e.g., CodeBERT, StarCoder) on Big-Vul/CVEFixes, or build from a security-specific base like SecureFalcon?

4. **Multi-language support:** KGCompass is language-agnostic at the graph level. Does the signature model need language-specific variants, or can a unified semantic embedding handle cross-language classification?

5. **Sovereign designation:** Who is the sovereign principal for Apex? Faheem as researcher/operator? Or does the bug bounty program itself become a constitutional authority that Apex must recognize?

---

*Document status: Seed — initial architecture capture from ideation session 2026-06-10*
*Next revision: After KGCompass deep study (Steps 2–5)*
*Series: Apex Architecture Documents*
