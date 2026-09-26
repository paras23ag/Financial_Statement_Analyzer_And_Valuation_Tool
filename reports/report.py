def print_ratio(name, value):

    print(
        f"{name}: {value:.2%}"
    )


def print_number(name, value):

    print(
        f"{name}: {value:,.2f}"
    )


def print_section(title):

    print("\n")
    print("=" * 50)
    print(title)
    print("=" * 50)