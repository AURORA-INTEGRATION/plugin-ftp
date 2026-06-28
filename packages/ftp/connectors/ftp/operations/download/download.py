"""FTP connector — Download operation."""
from __future__ import annotations

from aurora_engine.connector_helper import get_connector_config

from connectors.ftp.client import download


def run(input: dict, context: dict) -> dict:
    config = get_connector_config("ftp", input["ftp_alias"])
    return download(config, remote_path=input["remote_path"], local_path=input["local_path"])
