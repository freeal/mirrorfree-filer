"""Internal business logic for dormant LLP account summaries."""

from __future__ import annotations

from typing import Any

from .models import LLPAccounts


class DormantAccounts:
    """Simple internal wrapper around LLP account metadata."""

    def __init__(self, llp_accounts: LLPAccounts) -> None:
        if not llp_accounts.dormant:
            raise ValueError("LLPAccounts must be marked as dormant")
        self._llp_accounts = llp_accounts

    @property
    def llp_accounts(self) -> LLPAccounts:
        return self._llp_accounts

    def confirm_dormant(self) -> bool:
        """Return whether the LLP is marked as dormant."""
        return bool(self._llp_accounts.dormant)

    def summary(self) -> dict[str, Any]:
        """Return a simple summary mapping of the LLP account fields."""
        return {
            "llp_name": self._llp_accounts.llp_name,
            "company_number": self._llp_accounts.company_number,
            "accounting_period_start": self._llp_accounts.accounting_period_start,
            "accounting_period_end": self._llp_accounts.accounting_period_end,
            "dormant": self._llp_accounts.dormant,
        }
