"""Service for creating draft dormant LLP filing XML documents."""

from __future__ import annotations

from .accounts import DormantAccounts
from .filing_file import save_xml
from .models import LLPAccounts
from .xml_builder import DormantAccountsXmlBuilder


class DraftFilingService:
    """Orchestrate draft XML generation for dormant LLP filings."""

    def __init__(self, llp_accounts: LLPAccounts) -> None:
        self._llp_accounts = llp_accounts

    def create_draft(self, filename: str) -> str:
        """Create a draft filing XML document and save it to disk."""
        dormant_accounts = DormantAccounts(self._llp_accounts)
        xml_builder = DormantAccountsXmlBuilder(dormant_accounts)
        xml_document = xml_builder.build_string()
        return save_xml(xml_document, filename)
