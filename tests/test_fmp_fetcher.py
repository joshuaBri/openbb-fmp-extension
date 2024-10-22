import pytest
from openbb_core.app.service.user_service import UserService
from datetime import date
from openbb_fmp_extension.models.discounted_cashflow import FMPDiscountedCashflowFetcher
from openbb_fmp_extension.models.advanced_dcf import FMPAdvancedDcfFetcher
from openbb_fmp_extension.models.company_rating import FMPCompanyRatingFetcher
from openbb_fmp_extension.models.historical_rating import FMPHistoricalRatingFetcher
from openbb_fmp_extension.models.levered_dcf import FMPLeveredDcfFetcher
from openbb_fmp_extension.models.equity_historical import FMPEquityHistoricalFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)



def test_fmp_discounted_cashflow_fetcher(credentials=test_credentials):
    """Test discounted cashflow fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPDiscountedCashflowFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_fmp_advanced_dcf_fetcher(credentials=test_credentials):
    """Test discounted cashflow fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPAdvancedDcfFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_fmp_company_rating_fetcher(credentials=test_credentials):
    """Test company rating fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPCompanyRatingFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_fmp_historical_rating_fetcher(credentials=test_credentials):
    """Test historical rating fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPHistoricalRatingFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

def test_fmp_levered_dcf_fetcher(credentials=test_credentials):
    """Test levered dcf fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPLeveredDcfFetcher()
    result = fetcher.test(params, credentials)
    assert result is None

@pytest.mark.record_http
def test_fmp_equity_historical_fetcher(credentials=test_credentials):
    """Test FMP equity historical fetcher."""
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
        "interval": "1d",
    }

    fetcher = FMPEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None