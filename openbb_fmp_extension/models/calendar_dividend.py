"""FMP Dividend Calendar Model."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from dateutil.relativedelta import relativedelta
from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.calendar_dividend import (
    CalendarDividendData,
    CalendarDividendQueryParams,
)
from openbb_core.provider.utils.helpers import get_querystring
from openbb_fmp.utils.helpers import get_data_many
from pandas.errors import EmptyDataError
from pydantic import Field, field_validator

from openbb_fmp_extension.utils.helpers import get_jsonparsed_data, create_url


class FMPCalendarDividendQueryParams(CalendarDividendQueryParams):
    """FMP Dividend Calendar Query.

    Source: https://site.financialmodelingprep.com/developer/docs/dividend-calendar-api/

    The maximum time interval between the start and end date can be 3 months.
    """

    __alias_dict__ = {"start_date": "from", "end_date": "to"}


class FMPCalendarDividendData(CalendarDividendData):
    """FMP Dividend Calendar Data."""

    __alias_dict__ = {
        "amount": "dividend",
        "ex_dividend_date": "date",
        "record_date": "recordDate",
        "payment_date": "paymentDate",
        "declaration_date": "declarationDate",
        "adjusted_amount": "adjDividend",
    }

    adjusted_amount: Optional[float] = Field(
        default=None,
        description="The adjusted-dividend amount.",
    )
    label: Optional[str] = Field(
        default=None, description="Ex-dividend date formatted for display."
    )

    @field_validator(
        "ex_dividend_date",
        "record_date",
        "payment_date",
        "declaration_date",
        mode="before",
        check_fields=False,
    )
    @classmethod
    def date_validate(cls, v: str):  # pylint: disable=E0213
        """Return the date as a datetime object."""
        return datetime.strptime(v, "%Y-%m-%d") if v else None


class FMPCalendarDividendFetcher(
    Fetcher[
        FMPCalendarDividendQueryParams,
        List[FMPCalendarDividendData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPCalendarDividendQueryParams:
        """Transform the query params."""
        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now
        if params.get("end_date") is None:
            transformed_params["end_date"] = now + relativedelta(days=30)

        return FMPCalendarDividendQueryParams(**transformed_params)

    @staticmethod
    async def aextract_data(
        query: FMPCalendarDividendQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""
        url = create_url(
            3, f"stock_dividend_calendar", query, []
        )
        data = get_jsonparsed_data(url)
        if not data:
            raise EmptyDataError("No data returned for the given symbol.")

        return data

    @staticmethod
    def transform_data(
        query: FMPCalendarDividendQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[FMPCalendarDividendData]:
        """Return the transformed data."""
        return [FMPCalendarDividendData.model_validate(d) for d in data]
