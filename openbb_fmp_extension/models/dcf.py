"""Dcf Model."""

import asyncio
from datetime import date as dateType
from typing import Any, Dict, List, Optional
from warnings import warn

from pydantic import Field

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError

from openbb_fmp_extension.standard_models.dcf import (
    DcfData,
    DcfQueryParams,
)
# from openbb_fmp.utils.helpers import create_url
from openbb_core.provider.utils.helpers import amake_request


from openbb_fmp_extension.utils.helpers import create_url, get_jsonparsed_data


class FMPDcfQueryParams(DcfQueryParams):
    """Dcf Query Parameters.

    Source: https://financialmodelingprep.com/api/v3/form-thirteen/0001388838?date=2021-09-30
    """


class FMPDcfData(DcfData):
    """Dcf Data Model."""

    __alias_dict__ = {
        "stock_price": "Stock Price",
    }
    stock_price: Optional[float] = Field(
        default=None, description="Stock Price."
    )


class FMPDcfFetcher(
    Fetcher[
        DcfQueryParams,
        List[DcfData],
    ]
):
    """Fetches and transforms data from the Form 13f endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> DcfQueryParams:
        """Transform the query params."""
        return DcfQueryParams(**params)

    @staticmethod
    async def aextract_data(
            query: FMPDcfQueryParams,
            credentials: Optional[Dict[str, str]] = None,
            **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the House Disclosure endpoint."""
        symbols = query.symbol.split(",")
        results: List[Dict] = []

        async def get_one(symbol):
            """Get data for the given symbol."""
            # api_key = credentials.get("fmp_api_key") if credentials else ""
            # url = create_url(
            #     3, f"discounted-cash-flow/{query.symbol}", api_key , query,exclude=["symbol"]
            # )
            url = create_url(
                3, f"discounted-cash-flow/{symbol}", query, exclude=["symbol"]
            )
            result = await amake_request(url, **kwargs)
            # result = get_jsonparsed_data(url)
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
            query: FMPDcfQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[DcfData]:
        """Return the transformed data."""
        return [FMPDcfData(**d) for d in data]
