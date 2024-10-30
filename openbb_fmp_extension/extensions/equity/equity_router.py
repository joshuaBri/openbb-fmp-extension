"""Equity Router."""
from openbb_core.app.router import Router
from .ownership.ownership_router import router as ownership_router

router = Router(prefix="", description="Derivatives market data.")
router.include_router(ownership_router)
