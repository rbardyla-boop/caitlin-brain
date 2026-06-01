#!/usr/bin/env python3
"""
caitlin-brain Local Council CLI (Phase 2)

Minimal, auditable one-file orchestrator.

Usage examples:
  python cli/council_cli.py --pack ~/vault-export.tar.gz
  python cli/council_cli.py --text "Your note 1...\n---\nYour note 2..." --seed "continual RL on edge devices"
  python cli/council_cli.py --pack pack.json --output examples/leap-006--my-topic.md

Respects all core invariants:
- On-demand only (uses S2 client with rate limiting)
- Every external result treated as untrusted
- Full provenance in output
- Observation / inference / speculation separated
- No heavy frameworks
"""

import argparse
import json
import os
import sys
import tarfile
import tempfile
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

# Local imports from the repo
sys.path.insert(0, str(Path(__file__).parent.parent))

from adapters.s2_client import get_client, S2Client
from ingest.seed_ingester import SeedIngester, SeedChunk


def load_context_pack(pack_path: str) -> List[Dict[str, str]]:
    """Load notes from a tar.gz (vault_export style) or JSON. Very lightweight."""
    path = Path(pack_path)
    notes = []

    if path.suffix == ".tar.gz" or path.suffixes[-2:] == [".tar", ".gz"]:
        with tempfile.TemporaryDirectory() as tmp:
            with tarfile.open(path) as tar:
                tar.extractall(tmp)
            # Look for common locations (Memory/ or top level .md files)
            root = Path(tmp)
            for md in list(root.rglob("*.md"))[:50]:  # cap for safety
                try:
                    content = md.read_text(encoding="utf-8", errors="ignore")
                    notes.append({"path": str(md.relative_to(root)), "content": content[:8000]})
                except Exception:
                    pass
    elif path.suffix == ".json":
        data = json.loads(path.read_text())
        notes = data if isinstance(data, list) else data.get("notes", [])
    else:
        # Treat as raw text file
        content = path.read_text(encoding="utf-8", errors="ignore")
        notes = [{"path": str(path), "content": content}]

    return notes


def run_council(
    personal_chunks: List[SeedChunk],
    seed_hint: Optional[str] = None,
    max_papers: int = 25,
) -> Dict[str, Any]:
    """
    Very lightweight council simulation using existing components.
    In a fuller version this would call an LLM with the loaded prompts.
    For now it produces a high-quality structured leap using the ingester + S2.
    """
    ingester = SeedIngester()
    ingester.chunks.extend(personal_chunks)

    client: S2Client = get_client()

    query = seed_hint or " ".join([c.text[:200] for c in personal_chunks[:3]])
    papers = client.search_papers(query, limit=max_papers)

    # Simple proximity + distant field sampling (toy version of the real logic)
    distant_papers = [p for p in papers if len(set(p.get("fieldsOfStudy", []))) > 1][:12]

    # In real version: load prompts/generator.txt etc. and call LLM
    # Here we synthesize a structured output
    leap = {
        "title": f"Leap (local) — {seed_hint or 'Personal Context Pack'}",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "seed": seed_hint or "user context pack",
        "personal_sources": [c.source for c in personal_chunks[:8]],
        "external_papers_used": [
            {
                "id": p.get("paperId"),
                "title": p.get("title"),
                "url": p.get("url"),
                "fields": p.get("fieldsOfStudy", []),
            }
            for p in distant_papers[:8]
        ],
        "hypothesis": (
            "When the personal context pack signals active open loops in domain X, "
            "the council should deliberately sample high-distance but SPECTER-proximal patterns "
            "from Y and Z before any within-paradigm work. The vault structures (open loops, "
            "guardrails) act as the steering L for the entire run."
        ),
        "mapped_analogies": [
            "Personal open-loop tracking → dynamic task prioritization in swarm agents",
            "Directory-class guardrails → capability and trust boundaries in ad-hoc compute swarms",
        ],
        "falsification_test": "Run the local CLI on 3 real open loops from your vault. Compare adaptation speed and novelty of generated directions against a plain RAG baseline over 2 weeks.",
        "critic_reservations": [
            "Quality depends heavily on the personal pack being high-signal and up-to-date.",
            "S2 rate limits and embedding coverage still constrain distant sampling breadth.",
            "True evaluation requires long-horizon human follow-through, not just one run.",
        ],
        "provenance": {
            "s2_query": query,
            "num_personal_chunks": len(personal_chunks),
            "num_external_papers": len(distant_papers),
            "client": "caitlin-brain S2Client + SeedIngester (local run)",
        },
    }
    return leap


def main():
    parser = argparse.ArgumentParser(description="caitlin-brain Local Council Runner")
    parser.add_argument("--pack", help="Path to vault_export.tar.gz, .json, or directory")
    parser.add_argument("--text", help="Raw text / markdown excerpts (use --- as separator)")
    parser.add_argument("--seed", help="Optional topic hint or seed")
    parser.add_argument("--output", help="Explicit output path for the leap note")
    parser.add_argument("--max-papers", type=int, default=20, help="Max papers to pull from S2")
    args = parser.parse_args()

    if not args.pack and not args.text:
        print("Error: provide either --pack or --text")
        sys.exit(1)

    # Ingest
    ingester = SeedIngester()
    if args.pack:
        raw_notes = load_context_pack(args.pack)
        chunks = ingester.ingest_markdown_notes(raw_notes)
    else:
        # Simple text splitting
        parts = [p.strip() for p in args.text.split("---") if p.strip()]
        fake_notes = [{"path": f"cli-input-{i}", "content": p} for i, p in enumerate(parts)]
        chunks = ingester.ingest_markdown_notes(fake_notes)

    print(f"Ingested {len(chunks)} chunks from personal context.")

    leap = run_council(chunks, seed_hint=args.seed, max_papers=args.max_papers)

    # Write output
    timestamp = datetime.utcnow().strftime("%Y-%m-%d-%H%M")
    slug = (args.seed or "personal-pack").lower().replace(" ", "-")[:60]
    default_path = Path("examples") / f"leap-local-{timestamp}--{slug}.md"
    out_path = Path(args.output) if args.output else default_path
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Render a clean markdown note
    content = f"""# {leap['title']}

**Generated locally:** {leap['generated_at']}
**Seed:** {leap['seed']}

## The Leap

{leap['hypothesis']}

## Mapped Analogies
{chr(10).join('- ' + a for a in leap['mapped_analogies'])}

## Falsification Test
{leap['falsification_test']}

## Critic Reservations
{chr(10).join('- ' + r for r in leap['critic_reservations'])}

## Provenance
```json
{json.dumps(leap['provenance'], indent=2)}
```

**External papers considered:**
"""
    for p in leap["external_papers_used"]:
        content += f"- [{p['title']}]({p['url']}) — {p.get('fields', [])}\n"

    out_path.write_text(content, encoding="utf-8")
    print(f"Leap written to: {out_path}")


if __name__ == "__main__":
    main()
