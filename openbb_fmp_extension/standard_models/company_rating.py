"""House Disclosure Standard Model."""

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
    symbol: str = Field(description="The symbol of the company.")
    date: str = Field(description="The date of the rating.")
    rating: str = Field(description="Overall rating symbol.")
    ratingScore: int = Field(description="Overall rating score.")
    ratingRecommendation: str = Field(description="Overall rating recommendation.")
    ratingDetailsDCFScore: int = Field(description="Discounted Cash Flow (DCF) rating score.")
    ratingDetailsDCFRecommendation: str = Field(description="Discounted Cash Flow (DCF) rating recommendation.")
    ratingDetailsROEScore: int = Field(description="Return on Equity (ROE) rating score.")
    ratingDetailsROERecommendation: str = Field(description="Return on Equity (ROE) rating recommendation.")
    ratingDetailsROAScore: int = Field(description="Return on Assets (ROA) rating score.")
    ratingDetailsROARecommendation: str = Field(description="Return on Assets (ROA) rating recommendation.")
    ratingDetailsDEScore: int = Field(description="Debt to Equity (DE) rating score.")
    ratingDetailsDERecommendation: str = Field(description="Debt to Equity (DE) rating recommendation.")
    ratingDetailsPEScore: int = Field(description="Price to Earnings (PE) rating score.")
    ratingDetailsPERecommendation: str = Field(description="Price to Earnings (PE) rating recommendation.")
    ratingDetailsPBScore: int = Field(description="Price to Book (PB) rating score.")
    ratingDetailsPBRecommendation: str = Field(description="Price to Book (PB) rating recommendation.")