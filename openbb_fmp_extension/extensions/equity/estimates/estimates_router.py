"""Estimates Router."""
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router
from pydantic import BaseModel
router = Router(prefix="/estimates")


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