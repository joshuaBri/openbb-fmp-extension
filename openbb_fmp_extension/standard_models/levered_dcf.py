"""House Disclosure Standard Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS, DATA_DESCRIPTIONS


class LeveredDcfQueryParams(QueryParams):
    """Levered Dcf Query Parameters."""

    symbol: str = Field(..., description=QUERY_DESCRIPTIONS.get("symbol", "The symbol of the company."))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class LeveredDcfData(Data):
    """Levered  Dcf Data Model."""
    year: str = Field(description="The financial year.")
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company."))
    revenue: int = Field(description="Total projected revenue.")
    revenue_percentage: float = Field(description="Percentage change in revenue.")
    capital_expenditure: int = Field(description="Capital expenditures.")
    capital_expenditure_percentage: float = Field(description="Percentage of capital expenditure.")
    price: float = Field(description="Current stock price.")
    beta: float = Field(description="Beta value of the stock.")
    diluted_shares_outstanding: int = Field(description="Number of diluted shares outstanding.")
    cost_of_debt: float = Field(description="Cost of debt capital.")
    tax_rate: float = Field(description="Applicable tax rate.")
    after_tax_cost_of_debt: float = Field(description="After-tax cost of debt.")
    risk_free_rate: float = Field(description="Risk-free interest rate.")
    market_risk_premium: float = Field(description="Market risk premium.")
    cost_of_equity: float = Field(description="Cost of equity capital.")
    total_debt: int = Field(description="Total debt of the company.")
    total_equity: int = Field(description="Total equity of the company.")
    total_capital: int = Field(description="Total capital of the company.")
    debt_weighting: float = Field(description="Weighting of debt in capital structure.")
    equity_weighting: float = Field(description="Weighting of equity in capital structure.")
    wacc: float = Field(description="Weighted average cost of capital.")
    operating_cash_flow: int = Field(description="Operating cash flow.")
    pv_lfcf: float = Field(description="Present value of free cash flow.")
    sum_pv_lfcf: float = Field(description="Sum of present values of free cash flows.")
    long_term_growth_rate: float = Field(description="Expected long-term growth rate.")
    free_cash_flow: int = Field(description="Free cash flow.")
    terminal_value: int = Field(description="Terminal value of the company.")
    present_terminal_value: int = Field(description="Present value of the terminal value.")
    enterprise_value: int = Field(description="Enterprise value of the company.")
    net_debt: int = Field(description="Net debt of the company.")
    equity_value: int = Field(description="Equity value of the company.")
    equity_value_per_share: float = Field(description="Equity value per share.")
    free_cash_flow_t1: int = Field(description="Free cash flow for the next period.")
    operating_cash_flow_percentage: float = Field(description="Percentage of operating cash flow.")
