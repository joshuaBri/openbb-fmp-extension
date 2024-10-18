import pytest
from openbb_core.app.service.user_service import UserService

from openbb_fmp_extension.models.discounted_cashflow import FMPDiscountedCashflowFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.mark.record_http
def test_fmp_discounted_cashflow_fetcher(credentials=test_credentials):
    """Test discounted cashflow fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPDiscountedCashflowFetcher()
    result = fetcher.test(params, credentials)
    assert result is None