from pathlib import Path

import pytest

from mirrorfree_filer.filing_file import save_xml


def test_xml_document_can_be_saved(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)

    path = save_xml("<root><value>ok</value></root>", "draft.xml")

    saved_path = Path(path)
    assert saved_path.exists()
    assert saved_path.read_text(encoding="utf-8") == "<root><value>ok</value></root>"


def test_drafts_folder_is_created_automatically(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)

    save_xml("<root></root>", "draft.xml")

    assert (tmp_path / "drafts").exists()
    assert (tmp_path / "drafts" / "draft.xml").exists()


def test_existing_files_are_not_silently_overwritten(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    drafts_dir = tmp_path / "drafts"
    drafts_dir.mkdir()
    existing_file = drafts_dir / "draft.xml"
    existing_file.write_text("existing", encoding="utf-8")

    with pytest.raises(FileExistsError):
        save_xml("<root></root>", "draft.xml")
