from __future__ import annotations

# Security-log-analysis mainline integration models.

from pydantic import BaseModel


class BitdefenderConnectionRequest(BaseModel):
    api_key: str | None = None
    base_url: str = "https://cloud.gravityzone.bitdefender.com/api/v1.0/jsonrpc"
    parent_id: str | None = None


class WhiteboxAppSecRequest(BaseModel):
    repo_path: str
    target_url: str | None = None
    config_path: str | None = None
    mode: str = "standard"
