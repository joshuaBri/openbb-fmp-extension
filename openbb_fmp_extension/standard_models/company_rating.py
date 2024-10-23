"""Company Rating Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS, DATA_DESCRIPTIONS


class CompanyRatingQueryParams(QueryParams):
    """Historical Rating Query Parameters."""

    symbol: str = Field(..., description=QUERY_DESCRIPTIONS.get("symbol", "The symbol of the company."))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class CompanyRatingData(Data):
    """Historical Rating Data Model."""
    symbol: Optional[str] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    date: Optional[str] = Field(
        default=None, description="Date of the rating."
    )
    rating: Optional[str] = Field(
        default=None, description="Overall rating (e.g., S, A, B)."
    )
    rating_score: Optional[int] = Field(
        default=None, description="Overall rating score (e.g., 5, 4)."
    )
    rating_recommendation: Optional[str] = Field(
        default=None, description="Overall recommendation (e.g., Strong Buy)."
    )

    rating_details_dcf_score: Optional[int] = Field(
        default=None, description="Discounted Cash Flow (DCF) rating score."
    )
    rating_details_dcf_recommendation: Optional[str] = Field(
        default=None, description="DCF rating recommendation."
    )

    rating_details_roe_score: Optional[int] = Field(
        default=None, description="Return on Equity (ROE) rating score."
    )
    rating_details_roe_recommendation: Optional[str] = Field(
        default=None, description="ROE rating recommendation."
    )

    rating_details_roa_score: Optional[int] = Field(
        default=None, description="Return on Assets (ROA) rating score."
    )
    rating_details_roa_recommendation: Optional[str] = Field(
        default=None, description="ROA rating recommendation."
    )

    rating_details_de_score: Optional[int] = Field(
        default=None, description="Debt to Equity (DE) rating score."
    )
    rating_details_de_recommendation: Optional[str] = Field(
        default=None, description="DE rating recommendation."
    )

    rating_details_pe_score: Optional[int] = Field(
        default=None, description="Price to Earnings (PE) rating score."
    )
    rating_details_pe_recommendation: Optional[str] = Field(
        default=None, description="PE rating recommendation."
    )

    rating_details_pb_score: Optional[int] = Field(
        default=None, description="Price to Book (PB) rating score."
    )
    rating_details_pb_recommendation: Optional[str] = Field(
        default=None, description="PB rating recommendation."
    )