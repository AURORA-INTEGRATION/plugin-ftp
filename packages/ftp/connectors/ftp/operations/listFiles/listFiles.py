"""FTP connector — List Files operation."""
from __future__ import annotations

from typing import NotRequired, TypedDict

from aurora_engine.connector_helper import get_connector_config
from aurora_engine.service_types import ServiceContext

from connectors.ftp.client import ListFilesResult, list_files


class ListFilesInput(TypedDict):
    """Flow input of ``common.connectors.ftp.listFiles`` (see listFiles.yml)."""

    ftp_alias: str
    remote_path: NotRequired[str]


def run(input: ListFilesInput, context: ServiceContext) -> ListFilesResult:
    config = get_connector_config("ftp", input["ftp_alias"])
    return list_files(config, remote_path=input.get("remote_path") or "")
