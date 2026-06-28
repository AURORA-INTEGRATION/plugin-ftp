"""FTP connector — Upload operation."""
from __future__ import annotations

from aurora_engine.connector_helper import get_connector_config

from connectors.ftp.client import upload


def run(input: dict, context: dict) -> dict:
    config = get_connector_config("ftp", input["ftp_alias"])
    return upload(config, local_path=input["local_path"], remote_path=input["remote_path"])
