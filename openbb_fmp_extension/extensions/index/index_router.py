"""Index Router."""
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

from openbb_fmp_extension.extensions.index.price.price_router import router as price_router

router = Router(prefix="")
router.include_router(price_router)


@router.command(
    model="IndexConstituents",
    examples=[
        APIEx(
            parameters={
                "symbol": "nasdaq",
                "provider": "fmp",
            }
        ),
    ],
)
async def constituents(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """Get the income statement for a given company."""
    return await OBBject.from_query(Query(**locals()))
