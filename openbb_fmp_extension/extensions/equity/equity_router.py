"""Equity Router."""
from openbb_core.app.router import Router
from .estimates.estimates_router import router as estimates_router
from .fundamental.fundamental_router import router as fundamental_router
from .ownership.ownership_router import router as ownership_router
from .price.price_router import router as price_router

router = Router(prefix="", description="Derivatives market data.")
router.include_router(fundamental_router)
router.include_router(estimates_router)
router.include_router(ownership_router)
router.include_router(price_router)
