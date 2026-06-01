# PROJECT_CHARTER.md

## ADR-001: Architecture Decision - Separate Caitlin Brain Repo

**Status**: Approved & Implemented (Phase 0 complete)

**Context**: The personal vault repo must remain narrow, ruthless, and high-signal as a memory prosthetic. Forcing the full discovery brain into it would violate invariants and create bloat.

**Decision**: New standalone repo `caitlin-brain` for the 'one brain' firehose system.

**Rationale (Caitlin/Weinstein alignment)**: The visible 'L' is the personal vault's structured exports. We leap directly to the full solution — a dedicated engine that turns literature (and vault packs) into novel insights without grinding through safe incrementalism.

**Bridge Contract**: Use existing `vault_export.py` for portable Memory/ tar.gz context packs (Literature + gaps + synthesis). No code changes needed in source repo.

**Reusable Assets**: Vendored excerpts from truth_seeker/instructions.md, llm-council/llm-council.md, rules/research-evidence.md with attribution. Mental models remain referenced.

**Pre-mortem & Falsifiers**: Documented risks around scope creep, legal data access, hallucination. Success metric: Generates bold, evidence-grounded novel hypotheses that feel like 'I've got a good feeling about this.'

**Next**: Phase 1 MVP vertical slice per session plan.

This is the single source-of-truth artifact. Carry it forward.