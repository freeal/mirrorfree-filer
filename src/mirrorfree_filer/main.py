"""Simple application entry module for mirrorfree-filer."""

from __future__ import annotations


def build_message() -> str:
    """Return the simple application banner text."""
    return (
        "Application name: Mirror Free LLP Filer\n"
        "LLP name: Mirror Free LLP\n"
        "LLP number: OC444103"
    )


def run() -> str:
    """Return the simple banner text for the application."""
    return build_message()


def main() -> None:
    """Print the basic application information."""
    print(build_message())
