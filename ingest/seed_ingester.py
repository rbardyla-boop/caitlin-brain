"""
Seed ingester for caitlin-brain (Phase 1 stub).

Accepts either:
- A portable context pack (future: tar.gz from vault_export.py)
- Raw markdown excerpts or a list of note dicts

Outputs chunks with provenance ready for vector storage + council.

This is intentionally minimal. Real vector DB (Chroma, FAISS, etc.) can be swapped in later.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class SeedChunk:
    text: str
    source: str                    # e.g. "user-literature:Memory/Literature/foo.md" or "s2:paperId:xxx"
    metadata: Dict[str, Any] = field(default_factory=dict)
    embedding: Optional[List[float]] = None


class SeedIngester:
    def __init__(self):
        self.chunks: List[SeedChunk] = []

    def ingest_markdown_notes(self, notes: List[Dict[str, str]]) -> List[SeedChunk]:
        """
        notes: list of {"path": str, "content": str}
        """
        new_chunks = []
        for note in notes:
            path = note.get("path", "unknown")
            content = note.get("content", "")
            # Very simple chunking for v1 (later: better semantic chunking)
            chunk = SeedChunk(
                text=content[:4000],   # keep it reasonable
                source=f"user-literature:{path}",
                metadata={"type": "personal_note"}
            )
            new_chunks.append(chunk)
        self.chunks.extend(new_chunks)
        return new_chunks

    def ingest_s2_papers(self, papers: List[Dict[str, Any]]) -> List[SeedChunk]:
        """Turn S2 paper dicts (with embeddings) into SeedChunks."""
        new_chunks = []
        for p in papers:
            text = f"{p.get('title', '')}\n\n{p.get('abstract', '')}"
            if p.get('tldr'):
                text += f"\n\nTL;DR: {p['tldr'].get('text', '')}"

            chunk = SeedChunk(
                text=text,
                source=f"s2:{p.get('paperId')}",
                metadata={
                    "type": "s2_paper",
                    "year": p.get("year"),
                    "fields": p.get("fieldsOfStudy", []),
                    "citation_count": p.get("citationCount"),
                    "url": p.get("url"),
                },
                embedding=p.get("embedding", {}).get("specterv2"),
            )
            new_chunks.append(chunk)
        self.chunks.extend(new_chunks)
        return new_chunks

    def get_personal_chunks(self) -> List[SeedChunk]:
        return [c for c in self.chunks if "user-literature" in c.source]

    def get_external_chunks(self) -> List[SeedChunk]:
        return [c for c in self.chunks if c.source.startswith("s2:")]
