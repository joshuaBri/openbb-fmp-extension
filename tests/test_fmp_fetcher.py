import pytest
from openbb_core.app.service.user_service import UserService
from datetime import date
from openbb_fmp_extension.models.form_13f import FMPForm13FHRFetcher
from openbb_fmp_extension.models.government_trades import FMPGovernmentTradesFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


def test_fmp_form_13f_fetcher(credentials=test_credentials):
    """Test FMP form 13f fetcher."""
    params = {
        "symbol": "0001388838",
        "date": "2021-09-30",
    }
    fetcher = FMPForm13FHRFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


def test_fmp_government_trades_fetcher(credentials=test_credentials):
    """Test FMP government trades fetcher.
    params limit only functions when there is no parameter symbol
    """
    params = {
        "chamber": "all",
        "symbol": "AAPL",
        "limit": 500,
    }
    fetcher = FMPGovernmentTradesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
    params = {
        "chamber": "all",
        "limit": 300,
    }
    fetcher = FMPGovernmentTradesFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
