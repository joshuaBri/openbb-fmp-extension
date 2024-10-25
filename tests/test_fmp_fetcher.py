import pytest
from openbb_core.app.service.user_service import UserService
from datetime import date
from openbb_fmp_extension.models.discounted_cashflow import FMPDiscountedCashflowFetcher
from openbb_fmp_extension.models.advanced_dcf import FMPAdvancedDcfFetcher
from openbb_fmp_extension.models.company_rating import FMPCompanyRatingFetcher
from openbb_fmp_extension.models.historical_rating import FMPHistoricalRatingFetcher
from openbb_fmp_extension.models.levered_dcf import FMPLeveredDcfFetcher
from openbb_fmp_extension.models.equity_historical import FMPEquityHistoricalFetcher
from openbb_fmp_extension.models.balance_sheet import FMPBalanceSheetFetcher
from openbb_fmp_extension.models.income_statement import FMPIncomeStatementFetcher
from openbb_fmp_extension.models.cash_flow import FMPCashFlowStatementFetcher
from openbb_fmp_extension.models.form_13f import FMPForm13fFetcher
from openbb_fmp_extension.models.calendar_dividend import FMPCalendarDividendFetcher
from openbb_fmp_extension.models.etf_search import FMPEtfSearchFetcher
from openbb_fmp_extension.models.etf_holdings import FMPEtfHoldingsFetcher
from openbb_fmp_extension.models.index_constituents import FMPIndexConstituentsFetcher

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


@pytest.mark.record_http
def test_fmp_advanced_dcf_fetcher(credentials=test_credentials):
    """Test discounted cashflow fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPAdvancedDcfFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_company_rating_fetcher(credentials=test_credentials):
    """Test company rating fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPCompanyRatingFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_historical_rating_fetcher(credentials=test_credentials):
    """Test historical rating fetcher."""
    params = {
        "symbol": "AAPL",
    }

    fetcher = FMPHistoricalRatingFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
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


@pytest.mark.record_http
def test_fmp_balance_sheet_fetcher(credentials=test_credentials):
    """Test FMP balance sheet fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FMPBalanceSheetFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_cash_flow_statement_fetcher(credentials=test_credentials):
    """Test FMP cash flow statement fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FMPCashFlowStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_income_statement_fetcher(credentials=test_credentials):
    """Test FMP income statement fetcher."""
    params = {"symbol": "AAPL"}

    fetcher = FMPIncomeStatementFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


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


@pytest.mark.record_http
def test_fmp_calendar_dividend_fetcher(credentials=test_credentials):
    """Test FMP calendar dividend fetcher."""
    params = {
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 1, 10),
    }

    fetcher = FMPCalendarDividendFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_etf_serach_fetcher(credentials=test_credentials):
    """Test etf serach fetcher."""
    params = {
    }

    fetcher = FMPEtfSearchFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_etf_holdings_fetcher(credentials=test_credentials):
    """Test etf holdings fetcher."""
    params = {
        "symbol": "SPY",
    }

    fetcher = FMPEtfHoldingsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_fmp_index_constituents_fetcher(credentials=test_credentials):
    """Test etf holdings fetcher."""
    params = {
        "symbol": "sp500",
    }

    fetcher = FMPIndexConstituentsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None
