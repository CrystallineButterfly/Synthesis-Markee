"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "Repo Steward Agent",
  "track": "Markee",
  "pitch": "A repo-stewarding agent that drafts updates, messages, and build-story artifacts for public codebases while maintaining a verifiable audit trail.",
  "overlap_targets": [
    "OpenServ",
    "Filecoin",
    "ENS",
    "Bankr Gateway",
    "Octant",
    "Ampersend"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
