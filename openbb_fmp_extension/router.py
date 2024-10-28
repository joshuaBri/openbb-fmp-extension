"""openbb_fmp_extension Router."""

from openbb_core.app.router import Router
from openbb_fmp_extension.extensions.equity.equity_router import router as equity_router
from openbb_fmp_extension.extensions.etf.etf_router import router as etf_router
from openbb_fmp_extension.extensions.index.index_router import router as index_router

router = Router(prefix="", description="Derivatives market data.")
router.include_router(equity_router)
router.include_router(etf_router)
router.include_router(index_router)
