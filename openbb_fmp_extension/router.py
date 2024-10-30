"""openbb_fmp_extension Router."""

from openbb_core.app.router import Router
from openbb_fmp_extension.extensions.equity.equity_router import router as equity
from openbb_fmp_extension.extensions.etf.etf_router import router as etf
from openbb_fmp_extension.extensions.index.index_router import router as index

etf_router = Router(prefix="", description="Derivatives market data.")
equity_router = Router(prefix="", description="Derivatives market data.")
index_router = Router(prefix="", description="Derivatives market data.")

etf_router.include_router(etf)
equity_router.include_router(equity)
index_router.include_router(index)
