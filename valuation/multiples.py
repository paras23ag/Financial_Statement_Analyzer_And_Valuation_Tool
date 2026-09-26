def earnings_per_share(net_income, shares_outstanding):
    return net_income / shares_outstanding


def pe_ratio(market_price, eps):
    return market_price / eps


def enterprise_value(
    market_cap,
    total_debt,
    cash
):
    return market_cap + total_debt - cash


def ev_ebitda(enterprise_value_value, ebitda):
    return enterprise_value_value / ebitda