"""openbb_guru OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider

from openbb_fmp_extension.models.cash_flow import FMPCashFlowStatementFetcher
from openbb_fmp_extension.models.discounted_cashflow import FMPDiscountedCashflowFetcher
from openbb_fmp_extension.models.advanced_dcf import FMPAdvancedDcfFetcher
from openbb_fmp_extension.models.company_rating import FMPCompanyRatingFetcher
from openbb_fmp_extension.models.etf_holdings import FMPEtfHoldingsFetcher
from openbb_fmp_extension.models.form_13f import FMPForm13fFetcher
from openbb_fmp_extension.models.historical_rating import FMPHistoricalRatingFetcher
from openbb_fmp_extension.models.income_statement import FMPIncomeStatementFetcher
from openbb_fmp_extension.models.index_historical import FMPIndexHistoricalFetcher
from openbb_fmp_extension.models.index_constituents import FMPIndexConstituentsFetcher
from openbb_fmp_extension.models.index_historical_constituents import FMPIndexHistoricalConstituentsFetcher
from openbb_fmp_extension.models.levered_dcf import FMPLeveredDcfFetcher
from openbb_fmp_extension.models.equity_historical import FMPEquityHistoricalFetcher
from openbb_fmp_extension.models.balance_sheet import FMPBalanceSheetFetcher
from openbb_fmp_extension.models.calendar_dividend import FMPCalendarDividendFetcher
from openbb_fmp_extension.models.etf_search import FMPEtfSearchFetcher


# mypy: disable-error-code="list-item"

provider = Provider(
    name="fmp_extension",
    website="https://financialmodelingprep.com",
    description="""Financial Modeling Prep is a new concept that informs you about
    senate trading and house disclosure trading and RSS feed.""",
    credentials=["api_key"],
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "DiscountedCashflow": FMPDiscountedCashflowFetcher,
        "AdvancedDcf": FMPAdvancedDcfFetcher,
        "CompanyRating": FMPCompanyRatingFetcher,
        "HistoricalRating": FMPHistoricalRatingFetcher,
        "LeveredDcf": FMPLeveredDcfFetcher,
        "EquityHistorical": FMPEquityHistoricalFetcher,
        "BalanceSheet": FMPBalanceSheetFetcher,
        "CashFlowStatement": FMPCashFlowStatementFetcher,
        "IncomeStatement": FMPIncomeStatementFetcher,
        "Form13f": FMPForm13fFetcher,
        "CalendarDividend": FMPCalendarDividendFetcher,
        "EtfSearch": FMPEtfSearchFetcher,
        "EtfHoldings": FMPEtfHoldingsFetcher,
        "IndexHistorical": FMPIndexHistoricalFetcher,
        "IndexConstituents": FMPIndexConstituentsFetcher,
        "IndexHistoricalConstituents": FMPIndexHistoricalConstituentsFetcher,
    },
    repr_name="Financial Modeling Prep (FMP)",
    deprecated_credentials={"API_KEY_FINANCIALMODELINGPREP": "fmp_api_key"},
    instructions='Go to: https://site.financialmodelingprep.com/developer/docs\n\n![FinancialModelingPrep](https://user-images.githubusercontent.com/46355364/207821920-64553d05-d461-4984-b0fe-be0368c71186.png)\n\nClick on, "Get my API KEY here", and sign up for a free account.\n\n![FinancialModelingPrep](https://user-images.githubusercontent.com/46355364/207822184-a723092e-ef42-4f87-8c55-db150f09741b.png)\n\nWith an account created, sign in and navigate to the Dashboard, which shows the assigned token. by pressing the "Dashboard" button which will show the API key.\n\n![FinancialModelingPrep](https://user-images.githubusercontent.com/46355364/207823170-dd8191db-e125-44e5-b4f3-2df0e115c91d.png)',
)
