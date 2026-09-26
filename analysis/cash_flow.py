def free_cash_flow(
    net_income,
    depreciation,
    capex
):
    return net_income + depreciation - capex


def fcf_margin(free_cash_flow_value, revenue):
    return free_cash_flow_value / revenue