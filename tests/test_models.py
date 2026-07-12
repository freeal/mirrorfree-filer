from datetime import date

import pytest
from pydantic import ValidationError

from mirrorfree_filer.models import LLPAccounts


def test_llp_accounts_can_be_created_with_requested_example() -> None:
    model = LLPAccounts(
        llp_name="Mirror Free LLP",
        company_number="OC444103",
        accounting_period_start=date(2024, 11, 1),
        accounting_period_end=date(2025, 10, 31),
        dormant=True,
    )

    assert model.llp_name == "Mirror Free LLP"
    assert model.company_number == "OC444103"
    assert model.accounting_period_start == date(2024, 11, 1)
    assert model.accounting_period_end == date(2025, 10, 31)
    assert model.dormant is True


def test_llp_accounts_rejects_invalid_dates() -> None:
    with pytest.raises(ValidationError):
        LLPAccounts(
            llp_name="Mirror Free LLP",
            company_number="OC444103",
            accounting_period_start=date(2025, 10, 31),
            accounting_period_end=date(2024, 11, 1),
            dormant=True,
        )
