"""The FMP Senate Disclosure endpoint provides a list of all the financial disclosures that have been made by US Senators. This information is also required to be disclosed by the STOCK Act. The Senate disclosure endpoint includes information on the Senator's assets, liabilities, income, and expenditures. It also includes information on any gifts or travel that the Senator has received. Investors can use the Senate disclosure endpoint to learn more about the financial interests of US Senators and to identify potential conflicts of interest. For example, an investor may want to be aware of any investments that a Senator has in a company that they are considering investing in."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_fmp.utils.helpers import create_url

from openbb_fmp_extension.standard_models.discounted_cashflow import (
    DiscountedCashflowData,
    DiscountedCashflowQueryParams,
)
from openbb_fmp_extension.utils.helpers import get_jsonparsed_data, create_url


class FMPDiscountedCashflowQueryParams(DiscountedCashflowQueryParams):
    """Discounted Cashflow Query Parameters.

    Source: https://fmp.a.pinggy.link/api/v3/discounted-cash-flow
    """


class FMPDiscountedCashflowData(DiscountedCashflowData):
    """Discounted Cashflow Data Model."""

    __alias_dict__ = {
        "stock_price": "Stock Price"
    }


class FMPDiscountedCashflowFetcher(
    Fetcher[
        DiscountedCashflowQueryParams,
        List[DiscountedCashflowData],
    ]
):
    """Fetches and transforms data from the House Disclosure endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> DiscountedCashflowQueryParams:
        """Transform the query params."""
        return DiscountedCashflowQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPDiscountedCashflowQueryParams,
        credentials: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the House Disclosure endpoint."""
        symbols = query.symbol.split(",")
        results: List[Dict] = []
        async def get_one(symbol):
            """Get data for the given symbol."""
            url = create_url(
                3, f"discounted-cash-flow/{query.symbol}"
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
        query: FMPDiscountedCashflowQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[DiscountedCashflowData]:
        """Return the transformed data."""
        return [FMPDiscountedCashflowData(**d) for d in data]
