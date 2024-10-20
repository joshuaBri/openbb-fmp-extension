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


@router.command(methods=["GET"])
async def discounted_cash_flow(symbol: str = "AAPL") -> OBBject[dict]:
    """Get The DCF valuation data."""
    base_url = f"https://fmp.a.pinggy.link/api/v3/discounted-cash-flow/{symbol}"

    response = requests.get(base_url, timeout=5).json()
    return OBBject(results=response["details"])


@router.command(methods=["GET"])
async def advanced_dcf(symbol: str = "AAPL") -> OBBject[dict]:
    """Get The advanced_dcf valuation data."""
    base_url = f"https://fmp.a.pinggy.link/api/v4/advanced_discounted_cash_flow?symbol={symbol}"

    response = requests.get(base_url, timeout=5).json()
    return OBBject(results=response["details"])

@router.command(methods=["GET"])
async def company_rating(symbol: str = "AAPL") -> OBBject[dict]:
    """Get The company_rating valuation data."""
    base_url = f"https://fmp.a.pinggy.link//api/v3/rating/{symbol}"

    response = requests.get(base_url, timeout=5).json()
    return OBBject(results=response["details"])


@router.command(methods=["GET"])
async def historical_rating(symbol: str = "AAPL") -> OBBject[dict]:
    """Get The historical_rating valuation data."""
    base_url = f"https://fmp.a.pinggy.link/api/v3/historical-rating/{symbol}"

    response = requests.get(base_url, timeout=5).json()
    return OBBject(results=response["details"])


@router.command(methods=["GET"])
async def levered_dcf(symbol: str = "AAPL") -> OBBject[dict]:
    """Get The levered_dcf data."""
    base_url = f"https://fmp.a.pinggy.link/api/v4/advanced_levered_discounted_cash_flow?symbol={symbol}"

    response = requests.get(base_url, timeout=5).json()
    return OBBject(results=response["details"])


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
