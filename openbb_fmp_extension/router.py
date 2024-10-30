"""openbb_fmp_extension Router."""

from openbb_core.app.router import Router
from openbb_fmp_extension.extensions.equity.equity_router import router as equity

equity_router = Router(prefix="", description="Derivatives market data.")

equity_router.include_router(equity)
