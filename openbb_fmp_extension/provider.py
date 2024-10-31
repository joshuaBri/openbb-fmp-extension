"""openbb_guru OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider

from openbb_fmp_extension.models.form_13f import FMPForm13FHRFetcher
from openbb_fmp_extension.models.government_trades import FMPGovernmentTradesFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="fmp",
    website="https://financialmodelingprep.com",
    description="""Financial Modeling Prep is a new concept that informs you about
    senate trading and house disclosure trading and RSS feed.""",
    credentials=["api_key"],
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Form13FHR": FMPForm13FHRFetcher,
        "GovernmentTrades": FMPGovernmentTradesFetcher,
    },
    repr_name="Financial Modeling Prep (FMP)",
    deprecated_credentials={"API_KEY_FINANCIALMODELINGPREP": "fmp_api_key"},
    instructions='Go to: https://site.financialmodelingprep.com/developer/docs\n\n![FinancialModelingPrep](https://user-images.githubusercontent.com/46355364/207821920-64553d05-d461-4984-b0fe-be0368c71186.png)\n\nClick on, "Get my API KEY here", and sign up for a free account.\n\n![FinancialModelingPrep](https://user-images.githubusercontent.com/46355364/207822184-a723092e-ef42-4f87-8c55-db150f09741b.png)\n\nWith an account created, sign in and navigate to the Dashboard, which shows the assigned token. by pressing the "Dashboard" button which will show the API key.\n\n![FinancialModelingPrep](https://user-images.githubusercontent.com/46355364/207823170-dd8191db-e125-44e5-b4f3-2df0e115c91d.png)',
)
