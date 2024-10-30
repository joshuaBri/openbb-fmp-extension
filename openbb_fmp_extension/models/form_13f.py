"""Form 13f Model."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import to_snake_case

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
    """Company Rating Data Model."""

    __alias_dict__ = {"symbol": "ticker"}


class FMPForm13fFetcher(
    Fetcher[
        Form13FHRQueryParams,
        List[Form13FHRData],
    ]
):
    """Fetches and transforms data from the House Disclosure endpoints."""

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
        ciks = query.cik.split(",")
        results: List[Dict] = []

        async def get_one(symbol):
            """Get data for the given symbol."""
            url = create_url(
                3, f"form-thirteen/{query.cik}", query, exclude=["cik"]
            )
            result = get_jsonparsed_data(url)
            if not result or len(result) == 0:
                warn(f"Symbol Error: No data found for symbol {symbol}")
            if result:
                results.extend(result)

        await asyncio.gather(*[get_one(cik) for cik in ciks])

        if not results:
            raise EmptyDataError("No data returned for the given symbol.")
        results = [{to_snake_case(key): value for key, value in d.items()} for d in results]

        return results

    @staticmethod
    def transform_data(
            query: FMPForm13FHRQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[Form13FHRData]:
        """Return the transformed data."""
        return [FMPForm13FHRData(**d) for d in data]
