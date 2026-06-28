"""FTP connector — Delete operation."""
from __future__ import annotations

from aurora_engine.connector_helper import get_connector_config

from connectors.ftp.client import delete


def run(input: dict, context: dict) -> dict:
    config = get_connector_config("ftp", input["ftp_alias"])
    return delete(
        config,
        remote_path=input["remote_path"],
        ignore_missing=bool(input.get("ignore_missing")),
    )
