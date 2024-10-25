"""FMP Index Historical Constituents Model."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import to_snake_case

from openbb_fmp_extension.standard_models.index_historical_constituents import (
    IndexHistoricalConstituentsData,
    IndexHistoricalConstituentsQueryParams,
)
from openbb_fmp_extension.utils.helpers import create_url, get_jsonparsed_data


class FMPIndexHistoricalConstituentsQueryParams(IndexHistoricalConstituentsQueryParams):
    """Index Historical Constituents Query Parameters.

    Source: https://fmp.a.pinggy.link/api/v3/historical/nasdaq_constituent
    """


class FMPIndexHistoricalConstituentsData(IndexHistoricalConstituentsData):
    """Index Historical Constituents Data Model."""

    __alias_dict__ = {
        "date_added": "dateAdded",
        "added_security": "addedSecurity",
        "removed_ticker": "removedTicker",
        "removed_security": "removedSecurity"
    }


class FMPIndexHistoricalConstituentsFetcher(
    Fetcher[
        IndexHistoricalConstituentsQueryParams,
        List[IndexHistoricalConstituentsData],
    ]
):
    """Fetches and transforms data from the House Disclosure endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IndexHistoricalConstituentsQueryParams:
        """Transform the query params."""
        return IndexHistoricalConstituentsQueryParams(**params)

    @staticmethod
    async def aextract_data(
            query: IndexHistoricalConstituentsQueryParams,
            credentials: Optional[Dict[str, str]],
            **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        url = create_url(3, f"historical/{query.symbol}_constituent")

        data = get_jsonparsed_data(url)
        if not data:
            raise EmptyDataError("No data returned for the given symbol.")

        return data

    @staticmethod
    def transform_data(
        query: FMPIndexHistoricalConstituentsQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[IndexHistoricalConstituentsData]:
        """Return the transformed data."""
        return [FMPIndexHistoricalConstituentsData(**d) for d in data]
