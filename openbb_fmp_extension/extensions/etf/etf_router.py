"""Etf Router."""
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

router = Router(prefix="/etf")


@router.command(
    model="EtfSearch",
    examples=[
        APIEx(
            parameters={
                "provider": "fmp",
            }
        ),
    ],
)
async def search(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the income statement for a given company."""
    return await OBBject.from_query(Query(**locals()))


@router.command(
    model="EtfHoldings",
    examples=[
        APIEx(
            parameters={
                "symbol": "SPY",
                "provider": "fmp",
            }
        ),
    ],
)
async def holdings(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the income statement for a given company."""
    return await OBBject.from_query(Query(**locals()))
