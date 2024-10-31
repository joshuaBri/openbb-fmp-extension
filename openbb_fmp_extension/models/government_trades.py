"""Government Trades Model."""

import asyncio
import math
from datetime import date as dateType
from typing import Any, Dict, List, Optional
from warnings import warn

from pydantic import Field

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError

from openbb_fmp_extension.standard_models.government_trades import (
    GovernmentTradesData,
    GovernmentTradesQueryParams,
)
# from openbb_fmp.utils.helpers import create_url
# from openbb_core.provider.utils.helpers import amake_request


from openbb_fmp_extension.utils.helpers import create_url, get_jsonparsed_data


class FMPGovernmentTradesQueryParams(GovernmentTradesQueryParams):
    """Government Trades Query Parameters.

    Source: https://financialmodelingprep.com/api/v4/senate-trading?symbol=AAPL
    Source: https://financialmodelingprep.com/api/v4/senate-trading-rss-feed?page=0
    Source: https://financialmodelingprep.com/api/v4/senate-disclosure?symbol=AAPL
    Source: https://financialmodelingprep.com/api/v4/senate-disclosure-rss-feed?page=0
    """


class FMPGovernmentTradesData(GovernmentTradesData):
    """Government Trades Data Model."""

    __alias_dict__ = {
        "symbol": "ticker",
        "transaction_date": "transactionDate",
        "representative": "office",
    }
    link: Optional[str] = Field(
        default=None, description="Link to the transaction document."
    )
    transaction_date: Optional[str] = Field(
        default=None, description="Date of the transaction."
    )
    owner: Optional[str] = Field(
        default=None, description="Ownership status (e.g., Spouse, Joint)."
    )
    asset_type: Optional[str] = Field(
        default=None, description="Type of asset involved in the transaction."
    )
    asset_description: Optional[str] = Field(
        default=None, description="Description of the asset."
    )
    type: Optional[str] = Field(
        default=None, description="Type of transaction (e.g., Sale, Purchase)."
    )
    amount: Optional[str] = Field(
        default=None, description="Transaction amount range."
    )
    comment: Optional[str] = Field(
        default=None, description="Additional comments on the transaction."
    )


class FMPGovernmentTradesFetcher(
    Fetcher[
        GovernmentTradesQueryParams,
        List[GovernmentTradesData],
    ]
):
    """Fetches and transforms data from the Government Trades endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> GovernmentTradesQueryParams:
        """Transform the query params."""
        return GovernmentTradesQueryParams(**params)

    @staticmethod
    async def aextract_data(
            query: FMPGovernmentTradesQueryParams,
            credentials: Optional[Dict[str, str]] = None,
            **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Government Trades endpoint."""
        symbols = []
        if query.symbol:
            symbols = query.symbol.split(",")
        results: List[Dict] = []
        chamber_url_dict = {
            "house": ["senate-disclosure"],
            "senate": ["senate-trading"],
            "all": ["senate-disclosure", "senate-trading"],
        }

        async def get_one(url):
            # 指定要移除的键
            keys_to_remove = ["comment", "district", "capitalGainsOver200USD", "disclosureYear"]
            # 指定要重命名的键，格式为 {原键: 新键}
            keys_to_rename = {
                "dateRecieved": "date",
                "disclosureDate": "date"
            }
            """Get data for the given symbol."""
            # api_key = credentials.get("fmp_api_key") if credentials else ""
            # result = await amake_request(url, **kwargs)
            result = get_jsonparsed_data(url)
            # 处理数据
            processed_list = []
            for entry in result:
                # 创建新的字典用于存储处理后的数据
                new_entry = {k: v for k, v in entry.items() if k not in keys_to_remove}
                # 重命名指定的键
                for old_key, new_key in keys_to_rename.items():
                    if old_key in new_entry:
                        new_entry[new_key] = new_entry.pop(old_key)
                processed_list.append(new_entry)
            if not processed_list or len(processed_list) == 0:
                warn(f"Symbol Error: No data found for {url}")
            if processed_list:
                results.extend(processed_list)

        if symbols:
            urls_list = []
            for symbol in symbols:
                query.symbol = symbol
                url = [create_url(4, f"{i}", query=query, exclude=["chamber", "limit"]) for i in
                       chamber_url_dict[query.chamber]]
                urls_list.extend(url)
            await asyncio.gather(*[get_one(url) for url in urls_list])
        else:
            urls_list = []
            pages = math.ceil(query.limit / 100)
            for page in range(pages):
                query.page = page
                url = [create_url(4, f"{i}-rss-feed", query=query, exclude=["chamber", "limit"]) for i in
                       chamber_url_dict[query.chamber]]
                urls_list.extend(url)
            await asyncio.gather(*[get_one(url) for url in urls_list])

        if not results:
            raise EmptyDataError("No data returned for the given symbol.")

        return results

    @staticmethod
    def transform_data(
            query: FMPGovernmentTradesQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[GovernmentTradesData]:
        """Return the transformed data."""
        return [FMPGovernmentTradesData(**d) for d in data]
