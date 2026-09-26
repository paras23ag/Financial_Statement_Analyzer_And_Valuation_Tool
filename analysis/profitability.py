def gross_profit(revenue, cogs):
    return revenue - cogs


def gross_margin(revenue, cogs):
    return gross_profit(revenue, cogs) / revenue


def operating_profit(revenue, cogs, operating_expenses):
    return revenue - cogs - operating_expenses


def operating_margin(revenue, cogs, operating_expenses):
    return operating_profit(
        revenue,
        cogs,
        operating_expenses
    ) / revenue


def net_margin(net_income, revenue):
    return net_income / revenue


def roe(net_income, shareholders_equity):
    return net_income / shareholders_equity


def roa(net_income, total_assets):
    return net_income / total_assets