"""Index Historical Constituents Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS, DATA_DESCRIPTIONS


class IndexHistoricalConstituentsQueryParams(QueryParams):
    """Index Historical Constituents Query Parameters."""

    symbol: str = Field(..., description=QUERY_DESCRIPTIONS.get("symbol", "The symbol of the company."))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class IndexHistoricalConstituentsData(Data):
    """Index Historical Constituents Data Model."""
    date_added: Optional[str] = Field(
        default=None, description="Date when the security was added."
    )
    added_security: Optional[str] = Field(
        default=None, description="Name of the security that was added."
    )
    removed_ticker: Optional[str] = Field(
        default=None, description="Ticker symbol of the security that was removed."
    )
    removed_security: Optional[str] = Field(
        default=None, description="Name of the security that was removed."
    )
    date: Optional[str] = Field(
        default=None, description="Date of the portfolio change event."
    )
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", ""))
    reason: Optional[str] = Field(
        default=None, description="Reason for the portfolio change."
    )
