"""Form 13f Model."""

import asyncio
from datetime import date as dateType
from typing import Any, Dict, List, Optional
from warnings import warn

from pydantic import Field

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError

from openbb_core.provider.standard_models.form_13FHR import (
    Form13FHRData,
    Form13FHRQueryParams,
)
from openbb_fmp_extension.utils.helpers import create_url, get_jsonparsed_data


class FMPForm13FHRQueryParams(Form13FHRQueryParams):
    """Form 13f Query Parameters.

    Source: https://fmp.a.pinggy.link/api/v3/form-thirteen/0001388838?date=2021-09-30
    """


class FMPForm13FHRData(Form13FHRData):
    """Form13 FHR Data Model."""

    __alias_dict__ = {
        "period_ending": "date",
        "issuer": "nameOfIssuer",
        "principal_amount": "shares",
        "asset_class": "titleOfClass",
        "filling_date": "fillingDate",
        "accepted_date": "acceptedDate",
        "ticker_cusip": "tickercusip",
        "final_link": "finalLink",
    }
    filling_date: dateType = Field(
        default=None, description="Date when the filing was submitted to the SEC."
    )
    accepted_date: dateType = Field(
        default=None, description="Date when the filing was accepted by the SEC."
    )
    ticker_cusip: Optional[str] = Field(
        default=None, description="Ticker symbol associated with the CUSIP."
    )
    link: Optional[str] = Field(
        default=None, description="URL link to the SEC filing on the SEC website."
    )
    final_link: Optional[str] = Field(
        default=None, description="URL link to the XML information table of the SEC filing."
    )


class FMPForm13FHRFetcher(
    Fetcher[
        Form13FHRQueryParams,
        List[Form13FHRData],
    ]
):
    """Fetches and transforms data from the Form 13f endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> Form13FHRQueryParams:
        """Transform the query params."""
        return Form13FHRQueryParams(**params)

    @staticmethod
    async def aextract_data(
            query: FMPForm13FHRQueryParams,
            credentials: Optional[Dict[str, str]] = None,
            **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the House Disclosure endpoint."""
        symbols = query.symbol.split(",")
        results: List[Dict] = []

        async def get_one(symbol):
            """Get data for the given symbol."""
            url = create_url(
                3, f"form-thirteen/{query.symbol}", query, exclude=["symbol"]
            )
            result = get_jsonparsed_data(url)
            if not result or len(result) == 0:
                warn(f"Symbol Error: No data found for symbol {symbol}")
            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data returned for the given symbol.")

        return results

    @staticmethod
    def transform_data(
            query: FMPForm13FHRQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[Form13FHRData]:
        """Return the transformed data."""
        return [FMPForm13FHRData(**d) for d in data]
