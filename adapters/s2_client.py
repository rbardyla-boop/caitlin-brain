"""
Semantic Scholar Academic Graph API client for caitlin-brain.

Phase 1 foundation: on-demand only, rate-limit respecting, SPECTER2 embeddings.

Design principles (from PROJECT_CHARTER + plan):
- Never bulk download.
- Respect published rate limits and ToS.
- Every result carries full provenance.
- SPECTER2 vectors preferred when available (via embedding.specterv2 field).
"""

from __future__ import annotations

import os
import time
import logging
from typing import Any, Dict, List, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


class S2Client:
    BASE = "https://api.semanticscholar.org/graph/v1"

    def __init__(self, api_key: Optional[str] = None, max_rps: float = 0.9):
        self.api_key = api_key or os.getenv("S2_API_KEY")
        self.session = requests.Session()

        # Polite, resilient session
        retries = Retry(
            total=5,
            backoff_factor=1.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

        self.max_rps = max_rps
        self._last_request = 0.0

        self.headers = {
            "User-Agent": "caitlin-brain/0.1 (https://github.com/rbardyla-boop/caitlin-brain)"
        }
        if self.api_key:
            self.headers["x-api-key"] = self.api_key

    def _throttle(self):
        """Simple client-side rate limiting."""
        now = time.time()
        elapsed = now - self._last_request
        min_interval = 1.0 / self.max_rps
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        self._last_request = time.time()

    def _get(self, url: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        self._throttle()
        resp = self.session.get(url, headers=self.headers, params=params, timeout=30)
        if resp.status_code == 429:
            # Respect Retry-After if present
            retry_after = int(resp.headers.get("Retry-After", 5))
            logger.warning(f"Rate limited. Sleeping {retry_after}s")
            time.sleep(retry_after)
            return self._get(url, params)
        resp.raise_for_status()
        return resp.json()

    def search_papers(
        self,
        query: str,
        limit: int = 20,
        fields: Optional[List[str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Search papers. Returns list of paper objects with requested fields.
        """
        if fields is None:
            fields = [
                "paperId", "title", "abstract", "year", "fieldsOfStudy",
                "s2FieldsOfStudy", "citationCount", "influentialCitationCount",
                "tldr", "embedding.specterv2", "url", "openAccessPdf"
            ]

        params = {
            "query": query,
            "limit": min(limit, 100),
            "fields": ",".join(fields),
        }

        url = f"{self.BASE}/paper/search"
        data = self._get(url, params)
        return data.get("data", [])

    def get_papers_batch(
        self,
        paper_ids: List[str],
        fields: Optional[List[str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Batch fetch paper details (up to 500 recommended by S2).
        """
        if fields is None:
            fields = [
                "paperId", "title", "abstract", "year", "fieldsOfStudy",
                "s2FieldsOfStudy", "citationCount", "tldr", "embedding.specterv2", "url"
            ]

        url = f"{self.BASE}/paper/batch"
        payload = {"ids": paper_ids}
        params = {"fields": ",".join(fields)}

        self._throttle()
        resp = self.session.post(
            url, headers=self.headers, params=params, json=payload, timeout=60
        )
        if resp.status_code == 429:
            retry_after = int(resp.headers.get("Retry-After", 5))
            time.sleep(retry_after)
            return self.get_papers_batch(paper_ids, fields)
        resp.raise_for_status()
        return resp.json().get("data", [])

    def get_paper_with_embedding(self, paper_id: str) -> Optional[Dict[str, Any]]:
        """Convenience: fetch one paper with SPECTER2 embedding."""
        papers = self.get_papers_batch([paper_id])
        return papers[0] if papers else None


# Convenience factory
def get_client() -> S2Client:
    return S2Client()
