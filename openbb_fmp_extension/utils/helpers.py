"""FMP Helpers Module."""
from typing import Optional, Any, List

from openbb_core.provider.utils.helpers import get_querystring


def create_url(
        version: int,
        endpoint: str,
        query: Optional[Any] = None,
        exclude: Optional[List[str]] = None,
) -> str:
    """Return a URL for the FMP API.

    Parameters
    ----------
    version: int
        The version of the API to use.
    endpoint: str
        The endpoint to use.
    api_key: str
        The API key to use.
    query: Optional[BaseModel]
        The dictionary to be turned into a querystring.
    exclude: List[str]
        The keys to be excluded from the querystring.

    Returns
    -------
    str
        The querystring.
    """
    # pylint: disable=import-outside-toplevel
    from pydantic import BaseModel

    the_dict = {}
    if query:
        the_dict = query.model_dump() if isinstance(query, BaseModel) else query
    query_string = get_querystring(the_dict, exclude or [])
    base_url = f"https://fmp.a.pinggy.link/api/v{version}/"
    return f"{base_url}{endpoint}?{query_string}"
