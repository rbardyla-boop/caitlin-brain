# caitlin-brain

**The one brain for automated serendipity in science.**

Caitlin Burke solved the Wheel of Fortune puzzle with one visible 'L'.
Eric Weinstein named the move: make the intuitive leap from minimal structured clues to the full elegant solution.

This is that engine — for the entire scientific literature.

It swallows open, high-quality sources (Semantic Scholar + arXiv first), finds distant analogies across fields via SPECTER2 embeddings and citation structure, spots contradictions and gaps, generates aggressively novel hypotheses, and subjects them to a ruthless multi-persona Critic loop until the output feels like "I've got a good feeling about this."

Not summarization. Not search. **Automated Caitlin moments at scale.**

## The Leap That Created This Repo

The visible 'L' was the locked personal memory prosthetic in [Screenpipe-to-Obsidian](https://github.com/thebackhand/Screenpipe-to-Obsidian) (post 48 GB bloat disaster).

Instead of expanding that sacred narrow surface, we made the structural recognition: the discovery brain needed its own clean canvas.

This repo was born in one move via that exact philosophy.

## Core Contract

- **Personal vault** (Screenpipe-to-Obsidian / future memcore) stays the high-signal, anti-bloat clue provider.
- **This brain** does the global firehose traversal and recombination.
- They meet at clean, portable, read-only "research context packs" (Literature/ notes + gaps + synthesis summaries). See `vault_export.py` in the source repo as the existing bridge.

## Current Status

- Phase 0 complete: Architectural decision recorded in [docs/PROJECT_CHARTER.md](docs/PROJECT_CHARTER.md) (ADR-001).
- Reusable patterns from the source repo's `.claude/` (llm-council, truth_seeker, research-evidence discipline) are explicitly designed to be vendored here with attribution.
- MIT licensed for maximum idea velocity.

## Philosophy (Non-Negotiable)

- On-demand only. Never bulk local mirrors of millions of papers.
- Every hypothesis must carry traceable provenance (S2 paper IDs, user's source notes, embedding distances or rationale).
- The Critic is ruthless. Weak ideas die here.
- First 5 real outputs must be manually validated by a human before any scheduling or "roam freely" mode.
- We optimize for the subjective "good feeling" + real follow-through, not automated novelty scores.

## Quick Start (First Caitlin Leap)

```bash
git clone https://github.com/rbardyla-boop/caitlin-brain
cd caitlin-brain
# (Coming in Phase 1)
python -m caitlin_brain discover --seed-pack examples/seed-pack.json
```

A minimal working dogfood (S2 client + basic analogy finder + council-style Generator/Critic) is the immediate next target.

## First Real Seed (Dogfood)

The meta seed is already in the room:

> Building AI systems that perform Caitlin/Weinstein-style intuitive leaps across scientific literature using open structured sources + agentic debate.

We will run the first traceable leap on this exact topic using the plan + charter as the personal clue pack. Output will be a single, fully-provenanced hypothesis note with S2 citations and a falsification test.

Want to feed it your real Literature/ cluster instead? Export a small pack (or paste 3–5 notes) and we run it live.

## License

MIT — see [LICENSE](LICENSE).

Reusable ECC patterns (council, truth-seeker, evidence discipline) included with attribution per the source repo's charter.

## The Move

We saw the single visible 'L' and jumped straight to the full board.

Now the firehose starts.

Your move. What's the first literature pack or seed topic this brain should Caitlin?
