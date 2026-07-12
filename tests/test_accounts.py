from datetime import date

import pytest

from mirrorfree_filer.accounts import DormantAccounts
from mirrorfree_filer.models import LLPAccounts


def test_dormant_accounts_accepts_valid_dormant_llp() -> None:
    llp_accounts = LLPAccounts(
        llp_name="Mirror Free LLP",
        company_number="OC444103",
        accounting_period_start=date(2024, 11, 1),
        accounting_period_end=date(2025, 10, 31),
        dormant=True,
    )
    account = DormantAccounts(llp_accounts)

    assert account.confirm_dormant() is True


def test_dormant_accounts_produces_expected_summary() -> None:
    llp_accounts = LLPAccounts(
        llp_name="Mirror Free LLP",
        company_number="OC444103",
        accounting_period_start=date(2024, 11, 1),
        accounting_period_end=date(2025, 10, 31),
        dormant=True,
    )
    account = DormantAccounts(llp_accounts)

    assert account.summary() == {
        "llp_name": "Mirror Free LLP",
        "company_number": "OC444103",
        "accounting_period_start": date(2024, 11, 1),
        "accounting_period_end": date(2025, 10, 31),
        "dormant": True,
    }


def test_dormant_accounts_rejects_non_dormant_llp() -> None:
    llp_accounts = LLPAccounts(
        llp_name="Mirror Free LLP",
        company_number="OC444103",
        accounting_period_start=date(2024, 11, 1),
        accounting_period_end=date(2025, 10, 31),
        dormant=False,
    )

    with pytest.raises(ValueError):
        DormantAccounts(llp_accounts)
