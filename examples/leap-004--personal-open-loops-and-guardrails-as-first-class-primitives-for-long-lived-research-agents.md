---
title: "Leap #4: Treating Explicit Open Loops, Evaporating Tasks, and Anti-Bloat Guardrails as First-Class Architectural Primitives for Long-Lived Personal Research Agents"
date: "2026-06"
seed: "Personal knowledge management + AI agents for scientific discovery (using Screenpipe-to-Obsidian / memcore context as the personal literature pack)"
version: "C (strong) — Early analogical teleportation + personal structured memory primitives as steering mechanism"
status: "High-fidelity council execution using project artifacts as the personal context pack"
---

# Leap #4: Make Explicit Open-Loop Tracking and Anti-Bloat Guardrails Native Primitives in Long-Lived Research Agents

**Seed Context (Personal Literature Pack):** The Screenpipe-to-Obsidian + memcore project — specifically its ruthless focus on unfinished work / open loops, evaporating tasks, directory-class policies, vault_guard anti-bloat enforcement, pre-mortems, and the locked scope discipline after the 2026 48 GB incident.

**Core Hypothesis:**

Long-lived personal research agents will significantly outperform generic "AI Scientist" style systems (even advanced multi-agent ones) if they treat the user’s explicit structures for managing cognitive failure modes — open loops, evaporating items, sacred vs. archive boundaries, and active guardrails — as first-class, queryable, and decision-influencing memory primitives, rather than as just another bag of notes for RAG.

---

## The Leap

Current approaches to personal AI research assistants and long-term agents largely treat the user’s notes, papers, and history as a retrieval corpus. Even sophisticated systems (Co-Scientist, Robin, various memory-augmented agents) primarily optimize for better retrieval, summarization, or simulation within that corpus.

The non-obvious structural insight from this specific personal memory prosthetic project is:

**The highest-leverage signal for a truly personal, long-horizon research agent is not the raw content of the notes, but the user’s explicit, battle-tested machinery for fighting their own cognitive failure modes.**

In this case:
- The Unfinished Work Dashboard and EVAPORATING items (14+ days unseen)
- The distinction between sacred MemoryCore vs. Inbox vs. Active vs. Cold/Archive
- The ruthless guard that actively refuses toxic inputs and enforces size/policy boundaries
- Pre-mortem discipline and locked scope as architectural invariants
- The promote workflow that turns vague open loops into Projects / Concepts / Literature

These are not UI features. They are high-signal, low-entropy representations of what the user actually struggles with and has decided is worth protecting over years.

A research agent that has native, first-class access to these structures (instead of having to rediscover them through noisy embeddings) can make dramatically better decisions about:
- When to perform analogical teleportation vs. deep local work
- Which open problems are genuinely alive vs. sentimental
- How aggressively to push for synthesis or contradiction detection
- When to say "No" to new directions (mirroring the guard philosophy)

This turns the personal memory system from a passive data source into an active cognitive exoskeleton for the agent.

---

## Why This Is the Caitlin Move

The conservative path is: "Give the agent more notes, better embeddings, longer context, more retrieval tools."

The bold recognition (consistent with the founding philosophy of both repositories): the user has already done the extremely hard, high-leverage work of distilling their own failure modes into enforceable structures. Reusing those structures directly is far more powerful than asking the agent to reverse-engineer the user’s psychology from raw text.

This is the equivalent of giving the agent the single visible 'L' *plus* the lifetime of pattern recognition that let Caitlin Burke solve the puzzle.

---

## Grounding Literature (2025–2026)

- Pan et al. (2026). *A Survey of Continual Reinforcement Learning*. arXiv:2506.21872 — highlights the difficulty of maintaining coherent long-term behavior in non-stationary settings.
- Bell et al. and related work on "The Future of Continual Learning in the Era of Foundation Models" (2025) — emphasizes that continual learning remains essential even (especially) for large models, and that structured approaches beyond naive replay are needed.
- Work on long-term memory systems for agents (Mem0, Zep, and various "personal AI companion" papers 2025–2026) — most still treat user data as unstructured or lightly structured retrieval, with limited success at true personalization over multi-year horizons.
- The mental models and pre-mortem literature in software and research tooling (including the explicit use of pre-mortems and locked scopes in this project) as high-signal artifacts for decision-making under uncertainty.

The gap: Very few agent architectures treat the user’s *explicit anti-failure machinery* as privileged, first-class state.

---

## Concrete Falsifiable Test (Cheap, < 3 weeks)

1. Build two versions of a simple long-horizon research agent on the same base model:
   - Version A: Standard RAG + tool use over a user’s research notes + literature.
   - Version B: Same system, but with explicit access to structured open-loop state, directory-class policies, and guardrail rules as first-class inputs to planning, prioritization, and when to trigger analogical teleportation.

2. Give both agents the same sequence of 8–12 research tasks over a simulated 6–12 month "research lifetime," with injected new information and deliberate distraction tasks.

3. Measure:
   - How often the agent works on genuinely high-value open loops vs. low-signal or abandoned ones.
   - Quality and novelty of hypotheses generated (blind human rating).
   - Frequency of "scope creep" or low-value rabbit holes pursued.
   - User preference after reviewing the agent’s activity log.

If Version B does not show clear superiority on at least two of these metrics, especially on long-horizon coherence and resistance to bloat, the hypothesis is weakened.

---

## Residual Doubts (Critic Lens)

- Encoding rich personal guardrail logic into agent state may be brittle or hard to maintain as the user’s own practices evolve.
- Over-reliance on the user’s explicit structures could make the agent too conservative or too narrowly tuned to one person’s historical failure modes.
- Most researchers do not have (or maintain) this level of explicit structure in their personal systems, limiting generalizability.
- There is implementation cost and complexity in making these structures truly first-class rather than just additional context.

---

## Provenance

**Personal context pack source:** The full design history and current implementation of the Screenpipe-to-Obsidian project, including:
- SCOPED_VISION.md and MENTAL_MODELS_ANALYSIS.md (locked memcore direction)
- POST_MORTEM_RUTHLESS_FIX_2026-05-28.md (the 48 GB incident)
- vault_guard.py, vault_intelligence.py (gaps + evaporating items logic)
- .claude/rules/ and mental models discipline
- The ongoing co-development of this caitlin-brain repository as the external discovery layer

**External grounding:** The papers and surveys cited above.

**Method:** High-fidelity manual council execution (Generator + Contradiction Hunter + multi-persona Critic) using the exact philosophy and artifacts from the personal memory system as the steering context pack.

---

*Leap #4 complete. The personal memory prosthetic is no longer just fuel for retrieval — it is now treated as a source of privileged, high-signal cognitive architecture for the agent itself.*

This is the natural next tightening of the loop between the two systems.