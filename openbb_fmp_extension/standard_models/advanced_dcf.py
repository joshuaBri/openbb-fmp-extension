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
    year: Optional[str] = Field(
        default=None, description="Year of the projection data."
    )
    symbol: Optional[str] = Field(
        default=None, description=DATA_DESCRIPTIONS.get("symbol", "")
    )
    revenue: Optional[int] = Field(
        default=None, description="Total revenue in USD."
    )
    revenue_percentage: Optional[float] = Field(
        default=None, description="Revenue percentage change."
    )
    ebitda: Optional[int] = Field(
        default=None, description="Earnings Before Interest, Taxes, Depreciation, and Amortization (EBITDA) in USD."
    )
    ebitda_percentage: Optional[float] = Field(
        default=None, description="EBITDA percentage change."
    )
    ebit: Optional[int] = Field(
        default=None, description="Earnings Before Interest and Taxes (EBIT) in USD."
    )
    ebit_percentage: Optional[float] = Field(
        default=None, description="EBIT percentage change."
    )
    depreciation: Optional[int] = Field(
        default=None, description="Depreciation amount in USD."
    )
    depreciation_percentage: Optional[float] = Field(
        default=None, description="Depreciation percentage change."
    )
    total_cash: Optional[int] = Field(
        default=None, description="Total cash in USD."
    )
    total_cash_percentage: Optional[float] = Field(
        default=None, description="Total cash percentage change."
    )
    receivables: Optional[int] = Field(
        default=None, description="Total receivables in USD."
    )
    receivables_percentage: Optional[float] = Field(
        default=None, description="Receivables percentage change."
    )
    inventories: Optional[int] = Field(
        default=None, description="Total inventories in USD."
    )
    inventories_percentage: Optional[float] = Field(
        default=None, description="Inventories percentage change."
    )
    payable: Optional[int] = Field(
        default=None, description="Total payable in USD."
    )
    payable_percentage: Optional[float] = Field(
        default=None, description="Payable percentage change."
    )
    capital_expenditure: Optional[int] = Field(
        default=None, description="Capital expenditure in USD."
    )
    capital_expenditure_percentage: Optional[float] = Field(
        default=None, description="Capital expenditure percentage change."
    )
    price: Optional[float] = Field(
        default=None, description="Stock price in USD."
    )
    beta: Optional[float] = Field(
        default=None, description="Beta value."
    )
    diluted_shares_outstanding: Optional[int] = Field(
        default=None, description="Diluted shares outstanding."
    )
    cost_of_debt: Optional[float] = Field(
        default=None, description="Cost of debt in percentage."
    )
    tax_rate: Optional[float] = Field(
        default=None, description="Tax rate in percentage."
    )
    after_tax_cost_of_debt: Optional[float] = Field(
        default=None, description="After-tax cost of debt."
    )
    risk_free_rate: Optional[float] = Field(
        default=None, description="Risk-free rate in percentage."
    )
    market_risk_premium: Optional[float] = Field(
        default=None, description="Market risk premium in percentage."
    )
    cost_of_equity: Optional[float] = Field(
        default=None, description="Cost of equity in percentage."
    )
    total_debt: Optional[int] = Field(
        default=None, description="Total debt in USD."
    )
    total_equity: Optional[int] = Field(
        default=None, description="Total equity in USD."
    )
    total_capital: Optional[int] = Field(
        default=None, description="Total capital in USD."
    )
    debt_weighting: Optional[float] = Field(
        default=None, description="Debt weighting in percentage."
    )
    equity_weighting: Optional[float] = Field(
        default=None, description="Equity weighting in percentage."
    )
    wacc: Optional[float] = Field(
        default=None, description="Weighted Average Cost of Capital (WACC) in percentage."
    )
    tax_rate_cash: Optional[int] = Field(
        default=None, description="Tax rate cash amount."
    )
    ebiat: Optional[int] = Field(
        default=None, description="Earnings Before Interest After Taxes (EBIAT) in USD."
    )
    ufcf: Optional[int] = Field(
        default=None, description="Unlevered Free Cash Flow (UFCF) in USD."
    )
    sum_pv_ufcf: Optional[int] = Field(
        default=None, description="Sum of present value of UFCF in USD."
    )
    long_term_growth_rate: Optional[float] = Field(
        default=None, description="Long-term growth rate in percentage."
    )
    terminal_value: Optional[int] = Field(
        default=None, description="Terminal value in USD."
    )
    present_terminal_value: Optional[int] = Field(
        default=None, description="Present terminal value in USD."
    )
    enterprise_value: Optional[int] = Field(
        default=None, description="Enterprise value in USD."
    )
    net_debt: Optional[int] = Field(
        default=None, description="Net debt in USD."
    )
    equity_value: Optional[int] = Field(
        default=None, description="Equity value in USD."
    )
    equity_value_per_share: Optional[float] = Field(
        default=None, description="Equity value per share in USD."
    )
    free_cash_flow_t1: Optional[int] = Field(
        default=None, description="Free cash flow in USD at time t1."
    )
