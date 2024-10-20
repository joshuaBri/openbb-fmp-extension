"""House Disclosure Standard Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS, DATA_DESCRIPTIONS


class HistoricalRatingQueryParams(QueryParams):
    """Historical Rating Query Parameters."""

    symbol: str = Field(..., description=QUERY_DESCRIPTIONS.get("symbol", "The symbol of the company."))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class HistoricalRatingData(Data):
    """Historical Rating Data Model."""
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company."))
    date: str = Field(description="The date of the rating.")
    rating: str = Field(description="Overall rating of the stock.")
    rating_score: int = Field(description="Score associated with the overall rating.")
    rating_recommendation: str = Field(description="Recommendation based on the overall rating.")
    rating_details_dcf_score: int = Field(description="DCF (Discounted Cash Flow) score.")
    rating_details_dcf_recommendation: str = Field(description="Recommendation based on DCF score.")
    rating_details_roe_score: int = Field(description="ROE (Return on Equity) score.")
    rating_details_roe_recommendation: str = Field(description="Recommendation based on ROE score.")
    rating_details_roa_score: int = Field(description="ROA (Return on Assets) score.")
    rating_details_roa_recommendation: str = Field(description="Recommendation based on ROA score.")
    rating_details_de_score: int = Field(description="Debt to Equity score.")
    rating_details_de_recommendation: str = Field(description="Recommendation based on Debt to Equity score.")
    rating_details_pe_score: int = Field(description="P/E (Price to Earnings) score.")
    rating_details_pe_recommendation: str = Field(description="Recommendation based on P/E score.")
    rating_details_pb_score: int = Field(description="P/B (Price to Book) score.")
    rating_details_pb_recommendation: str = Field(description="Recommendation based on P/B score.")