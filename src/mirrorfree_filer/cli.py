"""Command-line entry points for mirrorfree-filer."""

from __future__ import annotations

import argparse

from .main import main as print_banner


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="mirrorfree-filer")
    parser.add_argument("--version", action="version", version="mirrorfree-filer 0.1.0")
    return parser


def main() -> int:
    parser = build_parser()
    parser.parse_args()
    print_banner()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
