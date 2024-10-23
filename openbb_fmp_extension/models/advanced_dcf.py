"""FMP Advanced Dcf Model."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import to_snake_case

from openbb_fmp_extension.standard_models.advanced_dcf import (
    AdvancedDcfData,
    AdvancedDcfQueryParams,
)
from openbb_fmp_extension.utils.helpers import create_url, get_jsonparsed_data


class FMPAdvancedDcfQueryParams(AdvancedDcfQueryParams):
    """Advanced Dcf Query Parameters.

    Source: https://fmp.a.pinggy.link/api/v3/discounted-cash-flow
    """


class FMPAdvancedDcfData(AdvancedDcfData):
    """Advanced Dcf Data Model."""
    __alias_dict__ = {"symbol": "ticker"}


class FMPAdvancedDcfFetcher(
    Fetcher[
        AdvancedDcfQueryParams,
        List[AdvancedDcfData],
    ]
):
    """Fetches and transforms data from the House Disclosure endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> AdvancedDcfQueryParams:
        """Transform the query params."""
        return AdvancedDcfQueryParams(**params)

    @staticmethod
    async def aextract_data(
            query: FMPAdvancedDcfQueryParams,
            credentials: Optional[Dict[str, str]] = None,
            **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the House Disclosure endpoint."""
        symbols = query.symbol.split(",")
        results: List[Dict] = []
        async def get_one(symbol):
            """Get data for the given symbol."""
            url = create_url(
                4, f"advanced_discounted_cash_flow", query
            )
            result = get_jsonparsed_data(url)
            if not result or len(result) == 0:
                warn(f"Symbol Error: No data found for symbol {symbol}")
            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(symbol) for symbol in symbols])

        if not results:
            raise EmptyDataError("No data returned for the given symbol.")
        results = [{to_snake_case(key): value for key, value in d.items()} for d in results]

        return results

    @staticmethod
    def transform_data(
            query: FMPAdvancedDcfQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[AdvancedDcfData]:
        """Return the transformed data."""
        return [FMPAdvancedDcfData(**d) for d in data]
