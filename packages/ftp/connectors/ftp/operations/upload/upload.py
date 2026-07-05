"""FTP connector — Upload operation."""
from __future__ import annotations

from typing import TypedDict

from aurora_engine.connector_helper import get_connector_config
from aurora_engine.service_types import ServiceContext

from connectors.ftp.client import UploadResult, upload


class UploadInput(TypedDict):
    """Flow input of ``common.connectors.ftp.upload`` (see upload.yml)."""

    ftp_alias: str
    local_path: str
    remote_path: str


def run(input: UploadInput, context: ServiceContext) -> UploadResult:
    config = get_connector_config("ftp", input["ftp_alias"])
    return upload(config, local_path=input["local_path"], remote_path=input["remote_path"])
