"""FMP Levered Dcf Model."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import to_snake_case

from openbb_fmp_extension.standard_models.levered_dcf import (
    LeveredDcfData,
    LeveredDcfQueryParams,
)
from openbb_fmp_extension.utils.helpers import create_url, get_jsonparsed_data


class FMPLeveredDcfQueryParams(LeveredDcfQueryParams):
    """Levered Dcf Query Parameters.

    Source: https://fmp.a.pinggy.link/api/v4/advanced_levered_discounted_cash_flow?symbol=AAPL
    """


class FMPLeveredDcfData(LeveredDcfData):
    """Levered Dcf Data Model."""

    __alias_dict__ = {"symbol": "ticker"}


class FMPLeveredDcfFetcher(
    Fetcher[
        LeveredDcfQueryParams,
        List[LeveredDcfData],
    ]
):
    """Fetches and transforms data from the House Disclosure endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> LeveredDcfQueryParams:
        """Transform the query params."""
        return LeveredDcfQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: FMPLeveredDcfQueryParams,
        credentials: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the House Disclosure endpoint."""
        api_key = credentials.get("fmp_api_key") if credentials else ""
        symbols = query.symbol.split(",")
        results: List[Dict] = []
        async def get_one(symbol):
            """Get data for the given symbol."""
            url = create_url(
                4, f"advanced_levered_discounted_cash_flow",query
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
        query: FMPLeveredDcfQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[LeveredDcfData]:
        """Return the transformed data."""
        return [FMPLeveredDcfData(**d) for d in data]
