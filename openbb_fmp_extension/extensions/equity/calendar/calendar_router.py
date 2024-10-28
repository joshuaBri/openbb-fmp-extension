"""Calendar Router."""
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.example import APIEx
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.provider_interface import (ExtraParams, ProviderChoices,
                                                StandardParams)
from openbb_core.app.query import Query
from openbb_core.app.router import Router

router = Router(prefix="/calendar")


@router.command(
    model="CalendarDividend",
    examples=[
        APIEx(
            parameters={
                "start_date": "2023-01-01",
                "end_date": "2023-01-10",
                "provider": "fmp",
            }
        ),
    ],
)
async def dividend(
        cc: CommandContext,
        provider_choices: ProviderChoices,
        standard_params: StandardParams,
        extra_params: ExtraParams,
) -> OBBject:
    """A list of upcoming dividend payments for publicly traded companies, including the date of the dividend payment, the ex-dividend date, and the dividend per share."""
    return await OBBject.from_query(Query(**locals()))
