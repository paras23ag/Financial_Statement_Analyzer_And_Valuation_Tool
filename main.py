import pandas as pd
import tkinter as tk
from tkinter import filedialog

from analysis.profitability import (
    gross_margin,
    operating_margin,
    net_margin,
    roe,
    roa
)

from analysis.liquidity import (
    current_ratio,
    working_capital
)

from analysis.leverage import (
    debt_to_equity,
    debt_to_assets
)

from analysis.cash_flow import (
    free_cash_flow
)

from valuation.dcf import (
    project_fcf,
    dcf_value
)

from reports.report import (
    print_section,
    print_ratio,
    print_number
)


# =========================================================
# 1. SELECT COMPANY FINANCIALS CSV
# =========================================================

root = tk.Tk()
root.withdraw()

print("Please select your company financials CSV file...")

file_path = filedialog.askopenfilename(
    title="Select Company Financials CSV",
    filetypes=[
        ("CSV files", "*.csv"),
        ("All files", "*.*")
    ]
)

# User cancelled file selection
if not file_path:
    print("\nNo file selected. Program stopped.")
    exit()


print("\nSelected file:")
print(file_path)


# =========================================================
# 2. READ CSV
# =========================================================

try:

    df = pd.read_csv(file_path)

except Exception as e:

    print(f"\nCould not read the CSV file: {e}")
    exit()


# =========================================================
# 3. DISPLAY DATA
# =========================================================

print("\nCompany financial data:")
print(df)


# =========================================================
# 4. CHECK REQUIRED COLUMNS
# =========================================================

required_columns = [
    "Year",
    "Revenue",
    "COGS",
    "Operating_Expenses",
    "Interest_Expense",
    "Tax",
    "Net_Income",
    "Total_Assets",
    "Current_Assets",
    "Current_Liabilities",
    "Total_Debt",
    "Shareholders_Equity",
    "Cash",
    "CAPEX",
    "Depreciation",
    "Shares_Outstanding"
]


missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]


if missing_columns:

    print("\nERROR: Your CSV is missing these columns:")

    for column in missing_columns:
        print(f"- {column}")

    print("\nColumns found in your CSV:")
    print(df.columns.tolist())

    exit()


# =========================================================
# 5. SORT BY YEAR
# =========================================================

df = df.sort_values(
    by="Year"
).reset_index(drop=True)


# =========================================================
# 6. SELECT MOST RECENT YEAR
# =========================================================

latest = df.iloc[-1]

print(
    f"\nAnalyzing financial year: "
    f"{latest['Year']}"
)


# =========================================================
# 7. EXTRACT FINANCIAL DATA
# =========================================================

revenue = latest["Revenue"]
cogs = latest["COGS"]
operating_expenses = latest["Operating_Expenses"]
net_income = latest["Net_Income"]

assets = latest["Total_Assets"]

current_assets = latest["Current_Assets"]
current_liabilities = latest["Current_Liabilities"]

debt = latest["Total_Debt"]
equity = latest["Shareholders_Equity"]

cash = latest["Cash"]

capex = latest["CAPEX"]
depreciation = latest["Depreciation"]

shares = latest["Shares_Outstanding"]


# =========================================================
# 8. PROFITABILITY ANALYSIS
# =========================================================

print_section("PROFITABILITY ANALYSIS")


gross_margin_value = gross_margin(
    revenue,
    cogs
)

operating_margin_value = operating_margin(
    revenue,
    cogs,
    operating_expenses
)

net_margin_value = net_margin(
    net_income,
    revenue
)

roe_value = roe(
    net_income,
    equity
)

roa_value = roa(
    net_income,
    assets
)


print_ratio(
    "Gross Margin",
    gross_margin_value
)

print_ratio(
    "Operating Margin",
    operating_margin_value
)

print_ratio(
    "Net Margin",
    net_margin_value
)

print_ratio(
    "ROE",
    roe_value
)

print_ratio(
    "ROA",
    roa_value
)


# =========================================================
# 9. LIQUIDITY ANALYSIS
# =========================================================

print_section("LIQUIDITY ANALYSIS")


current_ratio_value = current_ratio(
    current_assets,
    current_liabilities
)

working_capital_value = working_capital(
    current_assets,
    current_liabilities
)


print_number(
    "Current Ratio",
    current_ratio_value
)

print_number(
    "Working Capital",
    working_capital_value
)


# =========================================================
# 10. LEVERAGE ANALYSIS
# =========================================================

print_section("LEVERAGE ANALYSIS")


debt_equity_value = debt_to_equity(
    debt,
    equity
)

debt_assets_value = debt_to_assets(
    debt,
    assets
)


print_number(
    "Debt / Equity",
    debt_equity_value
)

print_number(
    "Debt / Assets",
    debt_assets_value
)


# =========================================================
# 11. FREE CASH FLOW
# =========================================================

print_section("CASH FLOW ANALYSIS")


fcf = free_cash_flow(
    net_income,
    depreciation,
    capex
)


print_number(
    "Free Cash Flow",
    fcf
)


# =========================================================
# 12. DCF VALUATION
# =========================================================

print_section("DCF VALUATION")


growth_rate = float(
    input(
        "\nEnter expected annual FCF growth rate "
        "(e.g. 8 for 8%): "
    )
) / 100


discount_rate = float(
    input(
        "Enter discount rate "
        "(e.g. 12 for 12%): "
    )
) / 100


terminal_growth = float(
    input(
        "Enter terminal growth rate "
        "(e.g. 3 for 3%): "
    )
) / 100


# Project FCF for 5 years

projected_fcf = project_fcf(
    fcf,
    growth_rate,
    5
)


# Calculate DCF value

enterprise_value = dcf_value(
    projected_fcf,
    discount_rate,
    terminal_growth
)


print_number(
    "DCF Enterprise Value",
    enterprise_value
)


# =========================================================
# 13. FINISHED
# =========================================================

print("\n==============================================")
print("        FINANCIAL ANALYSIS COMPLETE")
print("==============================================")