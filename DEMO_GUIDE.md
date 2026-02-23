# 🎤 Presenter's Demo Guide

> **Theme**: How to build custom agents, skills, and instructions to maximise agentic AI for research acceleration.
>
> This project — a semantic retrieval system over Microsoft Quantum research papers — is the **running example**. The audience leaves knowing how to replicate this pattern on their own research domain.
>
> Estimated total time: 45–60 minutes.

---

## Pre-Demo Checklist

- [ ] GitHub account with Copilot access (Enterprise or Individual with Copilot Chat)
- [ ] Codespace created from this repo (click the badge in README)
- [ ] Codespace fully built (dependencies installed)
- [ ] Verify Copilot extension is active in VS Code (check status bar)
- [ ] Run `streamlit run src/demo/app.py` and confirm it opens on port 8501
- [ ] Open a terminal and run `pytest tests/ -v` to confirm tests pass
- [ ] Have `.github/copilot-instructions.md` open in an editor tab — you will reference it repeatedly

---

## Part 1: Setting the Stage — Why Agentic AI for Research? (5 min)

### What to show:
1. Open the **Streamlit demo** (`streamlit run src/demo/app.py`) and navigate to the **Research Papers** tab
2. Walk the audience through the four indexed Microsoft Quantum papers and what they cover
3. Ask the audience: *"If you had to answer a question that spans all four papers, how would you do it today?"*

### Talking points:
- Researchers spend 30–50 % of their time locating, reading, and cross-referencing literature
- Agentic AI — an AI that can plan, use tools, and remember context — can act as a domain-aware research assistant
- But the key is **customisation**: a generic agent knows nothing about your papers, your domain vocabulary, or your workflow
- The goal of this demo is to show the three layers of customisation: **instructions → skills → agents**

---

## Part 2: Layer 1 — Custom Instructions (10 min)

> **File to show:** `.github/copilot-instructions.md`

### Concept:
Instructions are the *always-on context* that shape every Copilot interaction in your repo. They tell the agent:
- What the project is about (domain, goal)
- What terminology matters (Tetron qubits, QPE, Majorana zero modes, Floquet codes…)
- What coding conventions to follow
- What data sources exist (Azure AI Search index, four quantum PDFs)

### Steps:
1. Open `.github/copilot-instructions.md` — read the first paragraph aloud
2. Open Copilot Chat (`Ctrl+Shift+I`) and ask **without** mentioning the topic:
   - **"What research papers are covered in this project?"**
   - **"What is a tetron qubit?"**
   - **"How should I structure a new Python module in this repo?"**
3. Point out that Copilot answers using the exact concepts from the instructions file — it knows the domain without being asked

### Live demonstration:
- Temporarily remove the "Key Research Domain Concepts" section from the instructions
- Ask the same questions again — the answers are generic
- Restore the section

### Key message:
> *"Instructions are a one-time investment. Every team member, every chat session, every agent automatically inherits this domain knowledge."*

### Checklist — what good instructions cover:

| Section | Purpose |
|---|---|
| Project context | What problem is being solved, what data exists |
| Domain vocabulary | Key terms with one-line definitions |
| Coding conventions | Language version, style, patterns |
| Architecture overview | Module map so the agent can navigate files |
| Data sources | Where to look for information (index names, file paths) |

---

## Part 3: Layer 2 — Custom Skills (12 min)

> **Location in VS Code:** User-level skills live in `~/.copilot/skills/`; repo-level skills live in `.github/` or the workspace.

### Concept:
A **skill** packages a *repeatable workflow* into a reusable file (`SKILL.md`). When the agent detects the user is performing a known task, it loads the skill and follows its proven steps. Skills are domain-specific best practices made machine-readable.

### Anatomy of a SKILL.md:
```markdown
---
name: quantum-literature-review
description: Step-by-step workflow for reviewing a new quantum research paper...
applyTo: "**/*.py, **/*.md"
---

# Quantum Literature Review Skill

## When to use this skill
When the user asks to summarise, compare, or integrate a new paper into the corpus.

## Workflow
1. Extract the paper's core claim and experimental method
2. Identify which of the four existing papers it most closely relates to
3. List the new terminology introduced
4. Suggest new entries for copilot-instructions.md
5. Draft a SAMPLE_DOCUMENTS entry for sample_data.py
```

### Steps:
1. Navigate to the **🤖 Agentic AI Guide** tab in the Streamlit app — it shows a skill template for this exact project
2. Open the skill template, read the workflow steps aloud
3. Ask Copilot Chat: **"Follow the quantum literature review skill for the tetron roadmap paper"**
4. Show how the output maps onto the skill's numbered steps

### Skills to highlight for a research project:

| Skill name | What it does |
|---|---|
| `literature-review` | Summarises a paper and proposes corpus additions |
| `query-formulation` | Converts a research question into Azure AI Search queries |
| `hypothesis-to-code` | Turns a research hypothesis into a testable implementation |
| `paper-to-sample-data` | Extracts 3–5 representative excerpts from a PDF for `sample_data.py` |
| `evaluation-design` | Designs a retrieval evaluation benchmark for a new domain |

### Key message:
> *"Skills let you capture how your team's best expert approaches a problem — and replay that approach on demand, at scale, in every chat session."*

---

## Part 4: Layer 3 — Custom Agents (12 min)

> **Format:** `.agent.md` files (user-level: `~/.copilot/agents/`; repo-level in workspace)

### Concept:
A **custom agent** combines:
- A **persona** (name, role, tone)
- A **set of instructions** (which may include or extend the base instructions)
- A **tool policy** (which MCP servers, file operations, or terminal commands the agent may use)
- An optional **skill set** (which skills it automatically applies)

This lets you create a named, purpose-built AI collaborator for a specific research role.

### Anatomy of an `.agent.md`:
```markdown
---
name: QuantumPaperAssistant
description: Research assistant specialised in Microsoft Quantum literature retrieval.
tools:
  - azure-ai-search
  - file_search
  - semantic_search
skills:
  - quantum-literature-review
  - query-formulation
---

# Quantum Paper Assistant

You are a research assistant with deep expertise in topological quantum computing,
quantum chemistry workflows, and quantum error correction.

You have access to an Azure AI Search index containing four Microsoft Quantum papers.
Always cite the source paper and section when answering questions.

## Your primary workflows
1. Answer research questions by querying the Azure AI Search index first
2. When asked to compare papers, structure your answer around shared concepts
3. When asked to extend the corpus, follow the `quantum-literature-review` skill
```

### Steps:
1. Show the agent template in the **🤖 Agentic AI Guide** tab of the Streamlit app
2. Explain: "This agent *knows* it has Azure AI Search as a tool — it will call it automatically"
3. Demo in Copilot Chat — use the agent mode selector to switch to a custom agent if available
4. Ask: **"Compare how QPE is used in QDK/Chemistry versus the tetron roadmap"**
5. Show the agent searching the index, citing papers, and structuring its answer

### The three-layer stack summarised:

```
┌────────────────────────────────────────────┐
│           Custom Agent (.agent.md)         │
│   persona + tool policy + skill set        │
├────────────────────────────────────────────┤
│           Custom Skills (SKILL.md)         │
│   repeatable domain workflows              │
├────────────────────────────────────────────┤
│     Custom Instructions (instructions.md)  │
│   always-on domain context                 │
└────────────────────────────────────────────┘
```

### Key message:
> *"The agent is the interface your researchers interact with. Instructions are its memory. Skills are its playbook. Together they turn a generic LLM into a domain expert that works your way."*

---

## Part 5: Interactive Demo — The Quantum Research Explorer (8 min)

### Steps:
1. Open the Streamlit app: `streamlit run src/demo/app.py`
2. Walk through each tab:

   | Tab | What to show |
   |---|---|
   | 📄 Document Chunking | Adjust chunk size — explain why chunk granularity affects retrieval quality |
   | 🔍 Semantic Search | Run *"How does QPE extract molecular ground state energies?"* — connect to Azure AI Search as the production backend |
   | 📖 Research Papers | Show the metadata per paper — this is what feeds the instructions and sample data |
   | 🤖 Agentic AI Guide | Walk through the instructions/skills/agents templates live |

3. In the **Semantic Search** tab, show one of the example queries, then ask:
   - "What would happen if we asked this question *without* the domain instructions?"
   - Answer: the retrieval pipeline is the same, but the **Copilot agent interpreting the results** would lose context

### What to highlight:
- The demo app *is* the evidence: it took a generic RAG pipeline and made it domain-specific through instructions and sample data
- Audience can fork the repo, replace the PDF corpus and `copilot-instructions.md`, and have this running for their own research in under an hour

---

## Part 5b: Agent + MCP Data — The Reasoning Loop (8 min)

> **Tab to show:** 🔌 Agent + MCP Data

This part is the most impactful for technical audiences. It shows **why an agent needs a data source** by walking through the full tool-call pipeline — from question to answer — using real data from the Azure AI Search MCP server indexed in this project.

### Concept to establish first:
> *"An agent without data is like a doctor who never read a textbook after medical school. Training data has a cutoff date, a general scope, and no knowledge of your specific papers. Connect the agent to your data via MCP and it becomes a domain expert that improves every time you index a new paper."*

### Steps:
1. Navigate to the **🔌 Agent + MCP Data** tab in the Streamlit app
2. Select **"How does quantum phase estimation extract molecular ground state energies?"**
3. Walk through each step in the **Agent Reasoning Loop** panel:

   | Step | What to show |
   |---|---|
   | Agent formulates tool call | The YAML — `tool: hybrid_search`, the query string |
   | MCP returns raw results | Expand each chunk — show `id`, `@search.score`, `content` |
   | Agent reasoning trace | Each bullet — how the agent decides what to keep and combine |
   | Side-by-side answers | Left column (no MCP) vs right column (with MCP) |

4. Point out the **qualitative difference**:
   - Without MCP: correct but generic — no pipeline detail, no code structure, no paper attribution
   - With MCP: cites the paper, gives the exact workflow steps, mentions `Structure` object, Jordan-Wigner mapping, QPE as CASCI solver

5. Select a second scenario: **"What is a tetron qubit and how does it protect quantum information?"**
6. Show how the agent **cross-references two papers** (roadmap + parity paper) because the retrieval scores surface chunks from both

### Key message for each column:

| Without MCP | With MCP |
|---|---|
| Frozen training data | Live, versioned indexed papers |
| No source citations | Every claim linked to a chunk and paper |
| Generic explanation | Specific numbers: SNR, error rate, dimensions |
| Static — never updates | Improves when new papers are indexed |

### The single configuration line that enables this:
```yaml
# In your .agent.md tool policy:
tools:
  - azure-ai-search   # gives the agent all indexed paper chunks
```

### What to highlight:
- The MCP protocol is what makes the tool call possible — the agent doesn't scrape the web, it calls a controlled, curated, organisational data source
- Every chunk returned has a `@search.score` — the agent can decide how much to trust each result
- Adding a fifth paper to the Azure AI Search index immediately makes the agent smarter — **zero retraining**

---

## Part 6: Build Your Own — Live Workshop (8 min)

> Give the audience time to apply the pattern to their own domain.

### Prompt cards (hand out or display):

**Card A — Instructions**
```
1. Open .github/copilot-instructions.md in your fork
2. Replace the "Key Research Domain Concepts" section with 5 terms from your field
3. Ask Copilot: "What is [one of your terms]?" — verify it uses your definition
```

**Card B — Skill**
```
1. Create a new file .github/skills/my-review-skill.md
2. Add a YAML frontmatter block with name + description
3. Write 4–6 numbered workflow steps for a task you do repeatedly
4. Ask Copilot Chat: "Follow the my-review-skill for [topic]"
```

**Card C — Agent**
```
1. Create .github/agents/my-agent.md
2. Add a persona, a tools list, and 3 primary workflows
3. In VS Code, switch the Copilot Chat mode to your agent
4. Ask a cross-paper research question and note the difference in answer quality
```

---

## Closing (3 min)

### Key takeaways:

| Layer | File | Purpose |
|---|---|---|
| **Instructions** | `.github/copilot-instructions.md` | Always-on domain context — shapes every interaction |
| **Skills** | `SKILL.md` | Reusable workflows — captures expert know-how |
| **Agent** | `.agent.md` | Named AI collaborator — persona + tools + skills |

1. **Start with instructions** — highest ROI, least effort, immediate effect
2. **Add skills** when you spot yourself explaining the same workflow to Copilot more than twice
3. **Define an agent** when your team needs a consistent, named AI collaborator with a specific tool set
4. **Connect real data** — the Azure AI Search backend here is the difference between a toy and a production research accelerator
5. **Iterate** — treat your instructions and skills like living documentation; update them as the project evolves

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Copilot not reflecting instructions | Check the file is at `.github/copilot-instructions.md`; ensure file is saved |
| Skill not being applied | Confirm the `description` field in SKILL.md frontmatter matches the task wording |
| Agent not appearing in mode selector | Confirm VS Code Copilot extension is on a recent version; reload window |
| Import errors in demo app | Run `pip install -r requirements.txt` |
| Streamlit not loading | Check port 8501 is forwarded: `streamlit run src/demo/app.py --server.port 8501` |
| Azure AI Search not responding | Verify the MCP server `azure-ai-search` is connected in VS Code settings |
| FAISS import error | Run `pip install faiss-cpu` |
