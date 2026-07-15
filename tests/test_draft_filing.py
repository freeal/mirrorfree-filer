from __future__ import annotations

from pathlib import Path

from mirrorfree_filer.draft_filing import DraftFilingService
from mirrorfree_filer.models import LLPAccounts


def test_draft_xml_file_is_created(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)

    llp_accounts = LLPAccounts(
        llp_name="Mirror Free LLP",
        company_number="OC123456",
        accounting_period_start="2024-01-01",
        accounting_period_end="2024-12-31",
        dormant=True,
    )

    service = DraftFilingService(llp_accounts)
    saved_path = service.create_draft("draft.xml")

    saved_file = Path(saved_path)
    assert saved_file.exists()
    assert saved_file.parent == tmp_path / "drafts"
    assert "Mirror Free LLP" in saved_file.read_text(encoding="utf-8")


def test_service_uses_existing_modules_for_orchestration(monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)

    calls: list[str] = []

    class FakeDormantAccounts:
        def __init__(self, llp_accounts):
            calls.append("dormant")
            self._llp_accounts = llp_accounts

        def summary(self):
            return {"llp_name": "Mirror Free LLP", "company_number": "OC123456", "accounting_period_start": "2024-01-01", "accounting_period_end": "2024-12-31", "dormant": True}

    class FakeBuilder:
        def __init__(self, dormant_accounts):
            calls.append("builder")
            self._dormant_accounts = dormant_accounts

        def build_string(self):
            return "<DormantAccounts><llp_name>Mirror Free LLP</llp_name></DormantAccounts>"

    def fake_save_xml(xml_document, filename):
        calls.append("save")
        assert xml_document == "<DormantAccounts><llp_name>Mirror Free LLP</llp_name></DormantAccounts>"
        assert filename == "draft.xml"
        path = tmp_path / "drafts" / filename
        path.parent.mkdir(exist_ok=True)
        path.write_text(xml_document, encoding="utf-8")
        return str(path.resolve())

    import mirrorfree_filer.draft_filing as draft_filing_module

    monkeypatch.setattr(draft_filing_module, "DormantAccounts", FakeDormantAccounts)
    monkeypatch.setattr(draft_filing_module, "DormantAccountsXmlBuilder", FakeBuilder)
    monkeypatch.setattr(draft_filing_module, "save_xml", fake_save_xml)

    service = DraftFilingService(
        LLPAccounts(
            llp_name="Mirror Free LLP",
            company_number="OC123456",
            accounting_period_start="2024-01-01",
            accounting_period_end="2024-12-31",
            dormant=True,
        )
    )
    saved_path = service.create_draft("draft.xml")

    assert saved_path == str((tmp_path / "drafts" / "draft.xml").resolve())
    assert calls == ["dormant", "builder", "save"]
