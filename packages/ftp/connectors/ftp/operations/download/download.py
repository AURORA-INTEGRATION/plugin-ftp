"""FTP connector — Download operation."""
from __future__ import annotations

from typing import TypedDict

from aurora_engine.connector_helper import get_connector_config
from aurora_engine.service_types import ServiceContext

from connectors.ftp.client import DownloadResult, download


class DownloadInput(TypedDict):
    """Flow input of ``common.connectors.ftp.download`` (see download.yml)."""

    ftp_alias: str
    remote_path: str
    local_path: str


def run(input: DownloadInput, context: ServiceContext) -> DownloadResult:
    config = get_connector_config("ftp", input["ftp_alias"])
    return download(config, remote_path=input["remote_path"], local_path=input["local_path"])
