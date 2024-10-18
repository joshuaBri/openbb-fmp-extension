"""openbb_fmp_extension OpenBB Platform Provider."""

from openbb_core.provider.abstract.provider import Provider
from openbb_fmp_extension.models.example import ExampleFetcher

# mypy: disable-error-code="list-item"

provider = Provider(
    name="openbb_fmp_extension",
    description="Data provider for openbb_fmp_extension.",
    # Only add 'credentials' if they are needed.
    # For multiple login details, list them all here.
    # credentials=["api_key"],
    website="https://fmp_extension.com",
    # Here, we list out the fetchers showing what our provider can get.
    # The dictionary key is the fetcher's name, used in the `router.py`.
    fetcher_dict={
        "Example": ExampleFetcher,
    }
)
