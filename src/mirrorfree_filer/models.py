"""Simple data models for LLP account information."""

from __future__ import annotations

from datetime import date

from pydantic import BaseModel, ConfigDict, Field, model_validator


class LLPAccounts(BaseModel):
    """Represents basic dormant LLP account details."""

    model_config = ConfigDict(str_strip_whitespace=True)

    llp_name: str = Field(..., min_length=1)
    company_number: str = Field(..., min_length=1)
    accounting_period_start: date
    accounting_period_end: date
    dormant: bool = False

    @model_validator(mode="after")
    def validate_period(self) -> "LLPAccounts":
        if self.accounting_period_start > self.accounting_period_end:
            raise ValueError("accounting_period_start cannot be after accounting_period_end")
        return self
