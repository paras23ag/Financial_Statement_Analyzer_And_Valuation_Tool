def project_fcf(
    current_fcf,
    growth_rate,
    years
):

    projected = []

    fcf = current_fcf

    for year in range(1, years + 1):

        fcf = fcf * (1 + growth_rate)

        projected.append(fcf)

    return projected


def present_value(
    cash_flow,
    discount_rate,
    year
):

    return cash_flow / (
        (1 + discount_rate) ** year
    )


def terminal_value(
    final_fcf,
    growth_rate,
    discount_rate
):

    return (
        final_fcf * (1 + growth_rate)
    ) / (
        discount_rate - growth_rate
    )


def dcf_value(
    projected_fcf,
    discount_rate,
    terminal_growth
):

    pv_fcf = 0

    for year, fcf in enumerate(
        projected_fcf,
        start=1
    ):

        pv_fcf += present_value(
            fcf,
            discount_rate,
            year
        )

    tv = terminal_value(
        projected_fcf[-1],
        terminal_growth,
        discount_rate
    )

    pv_terminal = present_value(
        tv,
        discount_rate,
        len(projected_fcf)
    )

    return pv_fcf + pv_terminal