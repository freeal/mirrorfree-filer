from datetime import date
from xml.etree import ElementTree as ET

from mirrorfree_filer.accounts import DormantAccounts
from mirrorfree_filer.models import LLPAccounts
from mirrorfree_filer.xml_builder import DormantAccountsXmlBuilder


def test_dormant_accounts_can_be_converted_to_xml() -> None:
    llp_accounts = LLPAccounts(
        llp_name="Mirror Free LLP",
        company_number="OC444103",
        accounting_period_start=date(2024, 11, 1),
        accounting_period_end=date(2025, 10, 31),
        dormant=True,
    )
    builder = DormantAccountsXmlBuilder(DormantAccounts(llp_accounts))

    xml_element = builder.build()
    xml_string = builder.build_string()

    assert xml_element.tag == "DormantAccounts"
    assert ET.fromstring(xml_string).tag == "DormantAccounts"
    assert xml_element.findtext("llp_name") == "Mirror Free LLP"
    assert xml_element.findtext("company_number") == "OC444103"
    assert xml_element.findtext("accounting_period_start") == "2024-11-01"
    assert xml_element.findtext("accounting_period_end") == "2025-10-31"
    assert xml_element.findtext("dormant") == "true"
