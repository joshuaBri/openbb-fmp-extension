"""Form 13f Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS, DATA_DESCRIPTIONS


class Form13fQueryParams(QueryParams):
    """Form 13f Query Parameters."""

    cik: str = Field(..., description="Central Index Key (CIK) for the requested entity.")
    date: Optional[dateType] = Field(
        default=None,
        description=QUERY_DESCRIPTIONS.get("date", ""),
    )
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class Form13fData(Data):
    """Form 13f Data Model."""
    date: Optional[str] = Field(
        default=None, description="Filing date of the SEC document."
    )
    filling_date: Optional[str] = Field(
        default=None, description="Date when the filing was submitted."
    )
    accepted_date: Optional[str] = Field(
        default=None, description="Date when the SEC accepted the filing."
    )
    cik: Optional[str] = Field(
        default=None, description="Central Index Key (CIK) of the issuer."
    )
    cusip: Optional[str] = Field(
        default=None, description="CUSIP identifier for the issuer's securities."
    )
    tickercusip: Optional[str] = Field(
        default=None, description="Ticker or CUSIP symbol of the issuer."
    )
    name_of_issuer: Optional[str] = Field(
        default=None, description="Name of the issuer."
    )
    shares: Optional[int] = Field(
        default=None, description="Number of shares."
    )
    title_of_class: Optional[str] = Field(
        default=None, description="Class title of the securities."
    )
    value: Optional[int] = Field(
        default=None, description="Value of the shares in USD."
    )
    link: Optional[str] = Field(
        default=None, description="Link to the SEC filing document."
    )
    final_link: Optional[str] = Field(
        default=None, description="Link to the final SEC filing XML document."
    )
