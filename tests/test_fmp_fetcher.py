import pytest
from openbb_core.app.service.user_service import UserService
from datetime import date
from openbb_fmp_extension.models.form_13f import FMPForm13fFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.mark.record_http
def test_fmp_form_13f_fetcher(credentials=test_credentials):
    """Test FMP form 13f fetcher."""
    params = {
        "cik": "0001388838",
        "date": date(2023, 9, 30),
    }

    fetcher = FMPForm13fFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
