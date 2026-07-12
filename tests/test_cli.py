from mirrorfree_filer.cli import build_parser


def test_build_parser_generates_parser() -> None:
    parser = build_parser()
    assert parser is not None
