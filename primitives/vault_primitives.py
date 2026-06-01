#!/usr/bin/env python3
"""
vault_primitives.py (caitlin-brain side)

Machine-readable models for the personal memory system's core invariants.

These classes are the foundation for deep architectural integration (Option D):
agents should consume and respect these as *native constraints* during reasoning,
planning, and analogical teleportation, not just as flat text.

This file mirrors (and should stay reasonably in sync with) the version in the
Screenpipe-to-Obsidian repository.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


class MemoryClass(str, Enum):
    MEMORY_CORE = "MemoryCore"
    INBOX = "Inbox"
    ACTIVE = "Active"
    COLD = "Cold"
    ARCHIVE = "Archive"


@dataclass
class MemoryClassPolicy:
    max_size_mb: Optional[int] = None
    max_files: Optional[int] = None
    priority_for_agents: int = 50
    description: str = ""


class OpenLoopStatus(str, Enum):
    ACTIVE = "active"
    EVAPORATING = "evaporating"
    KILLED = "killed"
    PROMOTED = "promoted"


@dataclass
class OpenLoop:
    fingerprint: str
    text: str
    first_seen: datetime
    last_seen: datetime
    status: OpenLoopStatus = OpenLoopStatus.ACTIVE
    source_note: Optional[str] = None
    tags: List[str] = field(default_factory=list)

    @property
    def age_days(self) -> int:
        return (datetime.now() - self.first_seen).days

    @property
    def is_evaporating(self) -> bool:
        return self.age_days >= 14 and self.status == OpenLoopStatus.ACTIVE

    def to_agent_dict(self) -> Dict[str, Any]:
        return {
            "fingerprint": self.fingerprint,
            "text": self.text,
            "age_days": self.age_days,
            "status": self.status.value,
            "is_evaporating": self.is_evaporating,
            "source": self.source_note,
            "tags": self.tags,
        }


@dataclass
class Guardrail:
    name: str
    description: str
    severity: str = "hard"
    category: str = "anti_bloat"


@dataclass
class VaultPolicySnapshot:
    """
    The primary object agents should consume when they want to respect the user's
    explicit cognitive architecture.
    """
    timestamp: datetime
    memory_classes: Dict[str, MemoryClassPolicy]
    active_open_loops: List[OpenLoop]
    evaporating_open_loops: List[OpenLoop]
    guardrails: List[Guardrail]
    notes: str = ""

    def to_agent_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp.isoformat(),
            "memory_classes": {k: v.__dict__ for k, v in self.memory_classes.items()},
            "active_open_loops": [o.to_agent_dict() for o in self.active_open_loops],
            "evaporating_open_loops": [o.to_agent_dict() for o in self.evaporating_open_loops],
            "guardrails": [g.__dict__ for g in self.guardrails],
            "notes": self.notes,
        }
