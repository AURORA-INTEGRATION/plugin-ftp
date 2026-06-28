"""FTP connector — List Files operation."""
from __future__ import annotations

from aurora_engine.connector_helper import get_connector_config

from connectors.ftp.client import list_files


def run(input: dict, context: dict) -> dict:
    config = get_connector_config("ftp", input["ftp_alias"])
    return list_files(config, remote_path=input.get("remote_path") or "")
