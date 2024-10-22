"""openbb_fmp_extension router command example."""

import requests
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel

router = Router(prefix="")


@router.command(methods=["GET"], model="DiscountedCashflow")
async def discounted_cashflow(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(methods=["GET"], model="AdvancedDcf")
async def advanced_dcf(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(methods=["GET"], model="CompanyRating")
async def company_rating(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(methods=["GET"], model="HistoricalRating")
async def historical_rating(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(methods=["GET"], model="LeveredDcf")
async def levered_dcf(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
    return await OBBject.from_query(Query(**locals()))


@router.command(methods=["GET"], model="EquityHistorical")
async def equity_historical(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject[BaseModel]:
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
