"""Draft XML builder for dormant LLP account summaries."""

from __future__ import annotations

from xml.etree import ElementTree as ET

from .accounts import DormantAccounts


class DormantAccountsXmlBuilder:
    """Build a simple draft XML document from DormantAccounts data."""

    def __init__(self, dormant_accounts: DormantAccounts) -> None:
        self._dormant_accounts = dormant_accounts

    def build(self) -> ET.Element:
        """Return an XML element tree containing the draft account details."""
        summary = self._dormant_accounts.summary()

        root = ET.Element("DormantAccounts")
        ET.SubElement(root, "llp_name").text = summary["llp_name"]
        ET.SubElement(root, "company_number").text = summary["company_number"]
        ET.SubElement(root, "accounting_period_start").text = str(summary["accounting_period_start"])
        ET.SubElement(root, "accounting_period_end").text = str(summary["accounting_period_end"])
        ET.SubElement(root, "dormant").text = str(summary["dormant"]).lower()
        return root

    def build_string(self) -> str:
        """Return the XML document as a string."""
        root = self.build()
        return ET.tostring(root, encoding="unicode")
