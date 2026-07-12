from mirrorfree_filer.cli import build_parser
from mirrorfree_filer.main import main, run


EXPECTED_BANNER = (
    "Application name: Mirror Free LLP Filer\n"
    "LLP name: Mirror Free LLP\n"
    "LLP number: OC444103"
)


def test_run_returns_ready_message() -> None:
    assert run() == EXPECTED_BANNER


def test_main_prints_banner(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == EXPECTED_BANNER


def test_build_parser_creates_parser() -> None:
    parser = build_parser()
    assert parser.prog == "mirrorfree-filer"
