"""openbb_fmp_extension router command example."""

import requests
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="/price")


@router.command(
    model="DiscountedCashflow",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "fmp"})],
)
async def discounted_cashflow(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="AdvancedDcf",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "fmp"})],
)
async def advanced_dcf(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CompanyRating",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "fmp"})],
)
async def company_rating(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="HistoricalRating",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "fmp"})],
)
async def historical_rating(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="LeveredDcf",
    examples=[APIEx(parameters={"symbol": "AAPL", "provider": "fmp"})],
)
async def levered_dcf(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EquityHistorical",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
        APIEx(parameters={"symbol": "AAPL", "interval": "1d", "provider": "intrinio"}),
    ],
)
async def equity_historical(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="BalanceSheet",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
        APIEx(
            parameters={
                "symbol": "AAPL",
                "period": "annual",
                "limit": 5,
                "provider": "intrinio",
            }
        ),
    ],
)
async def balance(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the balance sheet for a given company."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="CashFlowStatement",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
        APIEx(
            parameters={
                "symbol": "AAPL",
                "period": "annual",
                "limit": 5,
                "provider": "intrinio",
            }
        ),
    ],
)
async def cash(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the cash flow statement for a given company."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="IncomeStatement",
    examples=[
        APIEx(parameters={"symbol": "AAPL", "provider": "fmp"}),
        APIEx(
            parameters={
                "symbol": "AAPL",
                "period": "annual",
                "limit": 5,
                "provider": "intrinio",
            }
        ),
    ],
)
async def income(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the income statement for a given company."""
    return await OBBject.from_query(Query(**locals()))


@router.command(methods=["POST"])
async def post_example(
        data: dict,
        bid_col: str = "bid",
        ask_col: str = "ask",
) -> OBBject[dict]:
    """Calculate mid and spread."""
    bid = data[bid_col]
    ask = data[ask_col]
    mid = (bid + ask) / 2
    spread = ask - bid

    return OBBject(results={"mid": mid, "spread": spread})


# pylint: disable=unused-argument
@router.command(model="Example")
async def model_example(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    """Example Data."""
    return await OBBject.from_query(Query(**locals()))
