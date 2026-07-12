"""Utilities for saving draft XML documents to disk."""

from __future__ import annotations

from pathlib import Path
from typing import Union
from xml.etree import ElementTree as ET


def save_xml(xml_document: Union[str, ET.Element], filename: str) -> str:
    """Save an XML document string or element to a local drafts folder.

    The function creates a drafts directory if needed, writes the document as UTF-8,
    and raises FileExistsError if the destination file already exists.
    """
    drafts_dir = Path("drafts")
    drafts_dir.mkdir(exist_ok=True)

    destination = drafts_dir / filename
    if destination.exists():
        raise FileExistsError(f"File already exists: {destination}")

    if isinstance(xml_document, ET.Element):
        xml_text = ET.tostring(xml_document, encoding="unicode")
    else:
        xml_text = xml_document

    destination.write_text(xml_text, encoding="utf-8")
    return str(destination.resolve())
