# First Caitlin Leap: Maximal-Novelty Optimization as First-Class Primitive for AI Scientists

**Date:** 2026-06 (manual v0 council run on meta-seed)
**Seed Source:** The caitlin-brain founding vision + plan + PROJECT_CHARTER (this repo's own origin story treated as the 'personal clues' pack) + public record of Sakana AI Scientist (Nature 2026), Google DeepMind Co-Scientist, and FutureHouse Robin (Nature 2026).
**Grounding Papers (traceable):**
- Lu et al. (2026). Towards end-to-end automation of AI research. *Nature*. https://www.nature.com/articles/s41586-026-10265-5 (Sakana AI Scientist lineage)
- Yamada et al. (2025/2026). The AI Scientist-v2. arXiv:2504.08066 (first fully AI-generated peer-reviewed-accepted workshop paper)
- Gottweis et al. (2026). Accelerating scientific discovery with Co-Scientist. *Nature*.
- Ghareeb et al. (2026). A multi-agent system for automating scientific discovery (Robin). *Nature*.

---

## The Leap

Current AI Scientist systems (Sakana v1/v2, DeepMind Co-Scientist, Robin) are extraordinary engineering achievements in *autonomous execution* within a domain. They generate ideas, run experiments (or code), write papers, and in Robin's case have already produced a real validated therapeutic candidate for dry age-related macular degeneration.

They are still fundamentally **incremental optimizers** of the existing scientific process.

The non-obvious recombination visible from the personal clues (our own founding charter + the vision's explicit rejection of 'more data / more simulation / safe incrementalism') is this:

**Make 'analogical teleportation' — deliberate, forced, high-distance cross-field structural mapping — a first-class, early-stage primitive in the agent architecture, on equal footing with (or prior to) within-domain ideation and experimentation.**

Personal research context packs (the Screenpipe-to-Obsidian / memcore clue layer) become the grounding 'minimal visible L' that makes the teleportation personal and non-generic instead of another broad literature sweep.

---

## Why This Structural Similarity Exists (The Pattern)

- Sakana's systems are optimized for *open-ended ML research* inside the ML distribution.
- Robin is optimized for *experimental biology loop closure* (hypothesis → experiment proposal → interpretation → new hypothesis).
- Co-Scientist is the most general multi-agent formulation so far.

All three still treat cross-domain analogy as an occasional happy accident or a human-provided prompt, not as an explicit, aggressively sampled, critic-enforced operation early in the tree search / ideation phase.

Our charter and vision contain the exact missing primitive: "high-risk, high-reward intuitive leaps", "analogical teleportation", "Caitlin-style from minimal clues", and ruthless rejection of conservative 'more data first' paths.

---

## Concrete, Falsifiable Hypothesis

An AI Scientist architecture that inserts a dedicated **Distant Analogy Scout + Critic** stage *before* heavy within-domain experiment planning will produce a higher rate of genuinely novel, high-impact research directions (as judged by expert humans 6-12 months later) than current within-paradigm tree-search or supervisor-agent systems, even when total compute is held constant or lower.

**Falsification test (cheap, <2 weeks for a motivated researcher):**
1. Take an existing open problem the user actually cares about (e.g. a gap surfaced in their own Unfinished Work Dashboard).
2. Run two parallel 20-idea generation passes with identical base model budget:
   - Condition A (baseline): standard Co-Scientist / AI-Scientist-v2 style ideation + tree search inside the problem's native field(s).
   - Condition B (leap): Force the first 40% of ideation budget through an explicit 'distant analogy' operator (sample papers from maximally different s2FieldsOfStudy via S2 API + SPECTER2 proximity to the user's personal literature notes + citation-chain jumps). Then run the normal critic + refinement on the recombined set.
3. Blind expert raters (or the user + 2 colleagues) score all 40 ideas on (a) non-obviousness, (b) technical plausibility, (c) potential impact if true.
4. Measure: fraction of B ideas that are both high-novelty *and* survive the plausibility filter vs A. Also track 6-month follow-through rate.

If B does not materially outperform A on the combined novelty × follow-through metric, the hypothesis is weakened or falsified for this architecture family.

---

## Residual Doubts (Critic Lens)

- Current systems already do some literature search; the marginal gain from aggressive distant sampling may be small if the base models are already good at long-context synthesis.
- Personal context packs may be too narrow or noisy to serve as reliable anchors for high-distance jumps.
- Evaluation is extremely hard (the real test is whether anyone actually pursues and publishes the direction 6-18 months later).

These doubts are exactly why the first 5 real runs must be manually validated before we declare victory or add scheduling.

---

## Provenance

- Personal clues: founding vision query + full session plan.md + PROJECT_CHARTER.md (ADR-001) in this repo + the Screenpipe-to-Obsidian post-mortem discipline.
- External grounding: the four Nature/arXiv sources listed above (all 2025-2026, publicly discussed).
- No private vault data used. Fully reproducible from public sources + the documents in this repository.

**Generated via manual v0 council-style debate** (Generator + Contradiction/Gap Hunter + multiple Critic personas) on the meta-seed. This is the shape the automated loop in Phase 1-3 must replicate and improve.

---

*This is the first visible output. The brain has produced its first 'I've got a good feeling about this' candidate.*

Next: wire the real S2 Scout + SPECTER proximity + automated council loop so the next leap costs one command instead of a human thinking session.
