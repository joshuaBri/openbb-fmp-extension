"""openbb_fmp_extension Router."""

from openbb_core.app.router import Router
from openbb_fmp_extension.extensions.equity.equity_router import router as equity_router

router_etf = Router(prefix="", description="Derivatives market data.")
router_equity = Router(prefix="", description="Derivatives market data.")

router_etf.include_router(router_etf)
router_equity.include_router(router_equity)
# router.include_router(index_router)
