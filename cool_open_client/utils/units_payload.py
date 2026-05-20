"""Shared helpers for parsing the `UnitsResponse` payload shape.

Lifted from `HVACUnitsFactory` so both the factory (setup-time) and the
client's bulk update method (poll-time) parse the API response with the
same defensive logic.
"""
from __future__ import annotations

from typing import Any, Dict


def extract_units_mapping(payload: Any) -> Dict[str, Any]:
    """Return a `{unit_id: payload}` mapping from a `UnitsResponse.data` value."""
    if payload is None:
        return {}
    if isinstance(payload, dict):
        return payload
    additional = getattr(payload, "additional_properties", None)
    if isinstance(additional, dict):
        return additional
    if hasattr(payload, "to_dict"):
        dumped = payload.to_dict()
        if isinstance(dumped, dict):
            return dumped
    return {}


def ensure_dict(payload: Any) -> Dict[str, Any]:
    """Coerce a single-unit payload into a plain dict."""
    if isinstance(payload, dict):
        return payload
    if hasattr(payload, "model_dump"):
        dumped = payload.model_dump(by_alias=True, exclude_none=True)
        if isinstance(dumped, dict):
            return dumped
    if hasattr(payload, "to_dict"):
        dumped = payload.to_dict()
        if isinstance(dumped, dict):
            return dumped
    return {}
