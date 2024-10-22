"""The FMP Senate Disclosure endpoint provides a list of all the financial disclosures that have been made by US Senators. This information is also required to be disclosed by the STOCK Act. The Senate disclosure endpoint includes information on the Senator's assets, liabilities, income, and expenditures. It also includes information on any gifts or travel that the Senator has received. Investors can use the Senate disclosure endpoint to learn more about the financial interests of US Senators and to identify potential conflicts of interest. For example, an investor may want to be aware of any investments that a Senator has in a company that they are considering investing in."""

import asyncio
from typing import Any, Dict, List, Optional
from warnings import warn
from urllib.request import urlopen
import certifi
import json
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.utils.errors import EmptyDataError
from openbb_core.provider.utils.helpers import amake_request
from openbb_fmp.utils.helpers import create_url, response_callback

from openbb_fmp_extension.standard_models.levered_dcf import (
    LeveredDcfData,
    LeveredDcfQueryParams,
)


class FMPLeveredDcfQueryParams(LeveredDcfQueryParams):
    """Discounted Cashflow Query Parameters.

    Source: https://financialmodelingprep.com/api/v4/advanced_levered_discounted_cash_flow?symbol=AAPL
    """


class FMPLeveredDcfData(LeveredDcfData):
    """House Disclosure Data Model."""

    __alias_dict__ = {
        "year": "year",
        "symbol": "symbol",
        "revenue": "revenue",
        "revenue_percentage": "revenuePercentage",
        "capital_expenditure": "capitalExpenditure",
        "capital_expenditure_percentage": "capitalExpenditurePercentage",
        "price": "price",
        "beta": "beta",
        "diluted_shares_outstanding": "dilutedSharesOutstanding",
        "cost_of_debt": "costOfDebt",
        "tax_rate": "taxRate",
        "after_tax_cost_of_debt": "afterTaxCostOfDebt",
        "risk_free_rate": "riskFreeRate",
        "market_risk_premium": "marketRiskPremium",
        "cost_of_equity": "costOfEquity",
        "total_debt": "totalDebt",
        "total_equity": "totalEquity",
        "total_capital": "totalCapital",
        "debt_weighting": "debtWeighting",
        "equity_weighting": "equityWeighting",
        "wacc": "wacc",
        "operating_cash_flow": "operatingCashFlow",
        "pv_lfcf": "pvLfcf",
        "sum_pv_lfcf": "sumPvLfcf",
        "long_term_growth_rate": "longTermGrowthRate",
        "free_cash_flow": "freeCashFlow",
        "terminal_value": "terminalValue",
        "present_terminal_value": "presentTerminalValue",
        "enterprise_value": "enterpriseValue",
        "net_debt": "netDebt",
        "equity_value": "equityValue",
        "equity_value_per_share": "equityValuePerShare",
        "free_cash_flow_t1": "freeCashFlowT1",
        "operating_cash_flow_percentage": "operatingCashFlowPercentage"
    }


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
        def get_jsonparsed_data(url):
            response = urlopen(url, cafile=certifi.where())
            data = response.read().decode("utf-8")
            return json.loads(data)
        async def get_one(symbol):
            """Get data for the given symbol."""
            url = f"https://fmp.a.pinggy.link/api/v4/advanced_levered_discounted_cash_flow?symbol={symbol}"
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
        query: FMPLeveredDcfQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[LeveredDcfData]:
        """Return the transformed data."""
        return [FMPLeveredDcfData(**d) for d in data]
