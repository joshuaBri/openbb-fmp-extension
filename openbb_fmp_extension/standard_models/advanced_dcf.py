"""House Disclosure Standard Model."""

from datetime import date as dateType
from typing import Optional

from pydantic import Field, field_validator

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from openbb_core.provider.utils.descriptions import QUERY_DESCRIPTIONS, DATA_DESCRIPTIONS


class AdvancedDcfQueryParams(QueryParams):
    """Advanced Dcf Query Parameters."""

    symbol: str = Field(..., description=QUERY_DESCRIPTIONS.get("symbol", "The symbol of the company."))

    @field_validator("symbol", mode="before", check_fields=False)
    @classmethod
    def to_upper(cls, v: str) -> str:
        """Convert field to uppercase."""
        return v.upper()


class AdvancedDcfData(Data):
    """Advanced Dcf Data Model."""
    symbol: str = Field(description=DATA_DESCRIPTIONS.get("symbol", "The symbol of the company."))
    price: float = Field(description="Current price of the stock.")
    beta: float = Field(description="Beta value of the stock.")
    final_tax_rate: float = Field(description="Final tax rate applied.")
    total_debt: int = Field(description="Total debt of the company.")
    total_equity: int = Field(description="Total equity of the company.")
    total_capital: int = Field(description="Total capital of the company.")
    diluted_shares_outstanding: int = Field(description="Number of diluted shares outstanding.")
    debt_weighting: float = Field(description="Weighting of debt in capital structure.")
    equity_weighting: float = Field(description="Weighting of equity in capital structure.")
    year: str = Field(description="The financial year.")
    period: str = Field(description="The financial reporting period.")
    revenue: int = Field(description="Total revenue generated.")
    ebitda: int = Field(description="Earnings before interest, taxes, depreciation, and amortization.")
    operating_cash_flow: int = Field(description="Cash flow from operating activities.")
    ebit: int = Field(description="Earnings before interest and taxes.")
    weighted_average_shs_out_dil: int = Field(description="Weighted average shares outstanding, diluted.")
    net_debt: int = Field(description="Net debt of the company.")
    inventories: int = Field(description="Total inventories held.")
    receivables: int = Field(description="Total receivables.")
    payable: int = Field(description="Total payables.")
    capital_expenditure: int = Field(description="Capital expenditures.")
    previous_revenue: int = Field(description="Revenue from the previous year.")
    revenue_percentage: float = Field(description="Percentage change in revenue.")
    tax_rate: float = Field(description="The applicable tax rate.")
    ebitda_percentage: float = Field(description="EBITDA as a percentage of revenue.")
    receivables_percentage: float = Field(description="Receivables as a percentage of revenue.")
    inventories_percentage: float = Field(description="Inventories as a percentage of revenue.")
    payable_percentage: float = Field(description="Payables as a percentage of revenue.")
    ebit_percentage: float = Field(description="EBIT as a percentage of revenue.")
    capital_expenditure_percentage: float = Field(description="Percentage of capital expenditure.")
    operating_cash_flow_percentage: float = Field(description="Percentage of operating cash flow.")
    after_tax_cost_of_debt: float = Field(description="After-tax cost of debt.")
    market_risk_premium: float = Field(description="Market risk premium.")
    long_term_growth_rate: float = Field(description="Expected long-term growth rate.")
    cost_of_equity: float = Field(description="Cost of equity capital.")
    wacc: float = Field(description="Weighted average cost of capital.")
    tax_rate_cash: int = Field(description="Cash tax rate.")
    ebiat: int = Field(description="Earnings before interest after tax.")
    ufcf: int = Field(description="Unlevered free cash flow.")
    risk_free_rate: float = Field(description="Risk-free rate of return.")
    sum_pv_ufcf: float = Field(description="Sum of present values of unlevered free cash flow.")
    terminal_value: int = Field(description="Terminal value of the company.")
    present_terminal_value: int = Field(description="Present value of the terminal value.")
    enterprise_value: int = Field(description="Enterprise value of the company.")
    equity_value: int = Field(description="Equity value of the company.")
    equity_value_per_share: float = Field(description="Equity value per share.")
    free_cash_flow_t1: int = Field(description="Free cash flow for the next period.")
    cost_of_debt: float = Field(description="Cost of debt capital.")
    depreciation: int = Field(description="Depreciation expense.")
    total_cash: int = Field(description="Total cash available.")
    depreciation_percentage: float = Field(description="Depreciation as a percentage of revenue.")
    total_cash_percentage: float = Field(description="Total cash as a percentage of revenue.")
