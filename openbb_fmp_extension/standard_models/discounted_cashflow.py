"""Discounted Cashflow Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS, DATA_DESCRIPTIONS


class DiscountedCashflowQueryParams(QueryParams):
    """Discounted Cashflow Query Parameters."""

    symbol: str = Field(..., description=QUERY_DESCRIPTIONS.get("symbol", "The symbol of the company."))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class DiscountedCashflowData(Data):
    """Discounted Cashflow Data Model."""
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company."))
    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", "The date of the data."))
    dcf: float = Field(default=None, description="The DCF valuation")
    stock_price: float = Field(default=None, description="The DCF valuation")
