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
    symbol: str = Field(description="The symbol of the company.")
    revenue: int = Field(description="Total projected revenue.")
    revenuePercentage: float = Field(description="Percentage change in revenue.")
    capitalExpenditure: int = Field(description="Capital expenditures.")
    capitalExpenditurePercentage: float = Field(description="Percentage of capital expenditure.")
    price: float = Field(description="Current stock price.")
    beta: float = Field(description="Beta value of the stock.")
    dilutedSharesOutstanding: int = Field(description="Number of diluted shares outstanding.")
    costofDebt: float = Field(description="Cost of debt capital.")
    taxRate: float = Field(description="Applicable tax rate.")
    afterTaxCostOfDebt: float = Field(description="After-tax cost of debt.")
    riskFreeRate: float = Field(description="Risk-free interest rate.")
    marketRiskPremium: float = Field(description="Market risk premium.")
    costOfEquity: float = Field(description="Cost of equity capital.")
    totalDebt: int = Field(description="Total debt of the company.")
    totalEquity: int = Field(description="Total equity of the company.")
    totalCapital: int = Field(description="Total capital of the company.")
    debtWeighting: float = Field(description="Weighting of debt in capital structure.")
    equityWeighting: float = Field(description="Weighting of equity in capital structure.")
    wacc: float = Field(description="Weighted average cost of capital.")
    operatingCashFlow: int = Field(description="Operating cash flow.")
    pvLfcf: float = Field(description="Present value of free cash flow.")
    sumPvLfcf: float = Field(description="Sum of present values of free cash flows.")
    longTermGrowthRate: float = Field(description="Expected long-term growth rate.")
    freeCashFlow: int = Field(description="Free cash flow.")
    terminalValue: int = Field(description="Terminal value of the company.")
    presentTerminalValue: int = Field(description="Present value of the terminal value.")
    enterpriseValue: int = Field(description="Enterprise value of the company.")
    netDebt: int = Field(description="Net debt of the company.")
    equityValue: int = Field(description="Equity value of the company.")
    equityValuePerShare: float = Field(description="Equity value per share.")
    freeCashFlowT1: int = Field(description="Free cash flow for the next period.")
    operatingCashFlowPercentage: float = Field(description="Percentage of operating cash flow.")
