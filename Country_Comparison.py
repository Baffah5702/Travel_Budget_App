"""
COUNTRY COMPARISON PROJECT
Topic: Comparing the Estimated Travel Costs of Ghana and Kenya
Name: Nentapomwa Wakjissa

This program compares estimated travel expenses for one traveller
visiting Ghana or Kenya. All amounts are expressed in Nigerian Naira.
"""

CURRENCY = "₦"

ghana = {
    "Return Flight": 450_000,
    "Accommodation (3 nights)": 180_000,
    "Feeding": 90_000,
    "Local Transportation": 45_000,
    "Tourist Activities": 60_000,
}

kenya = {
    "Return Flight": 1_300_000,
    "Accommodation (3 nights)": 210_000,
    "Feeding": 105_000,
    "Local Transportation": 60_000,
    "Tourist Activities": 80_000,
}


def calculate_total(expenses):
    """Return the total cost of all expenses in a dictionary."""
    return sum(expenses.values())


def display_comparison(ghana_costs, kenya_costs):
    """Display the expense breakdown and total for both destinations."""
    print("=" * 72)
    print("             TRAVEL COST COMPARISON: GHANA VS KENYA")
    print("=" * 72)

    print(
        f"\n{'EXPENSES':<32}"
        f"{'GHANA (' + CURRENCY + ')':>18}"
        f"{'KENYA (' + CURRENCY + ')':>18}"
    )
    print("-" * 68)

    for expense in ghana_costs:
        ghana_amount = ghana_costs[expense]
        kenya_amount = kenya_costs[expense]
        print(f"{expense:<32}{ghana_amount:>18,}{kenya_amount:>18,}")

    ghana_total = calculate_total(ghana_costs)
    kenya_total = calculate_total(kenya_costs)

    print("-" * 68)
    print(f"{'TOTAL':<32}{ghana_total:>18,}{kenya_total:>18,}")

    return ghana_total, kenya_total


def compare_destinations(ghana_total, kenya_total):
    """Compare totals and print a conclusion that adjusts to the figures."""
    print("\nTRAVEL COST ANALYSIS")
    print("-" * 45)

    if ghana_total < kenya_total:
        savings = kenya_total - ghana_total
        percentage = (savings / kenya_total) * 100
        print("Ghana is the more affordable destination.")
        print(f"Choosing Ghana saves {CURRENCY}{savings:,}.")
        print(f"Ghana is approximately {percentage:.2f}% cheaper than Kenya.")

    elif kenya_total < ghana_total:
        savings = ghana_total - kenya_total
        percentage = (savings / ghana_total) * 100
        print("Kenya is the more affordable destination.")
        print(f"Choosing Kenya saves {CURRENCY}{savings:,}.")
        print(f"Kenya is approximately {percentage:.2f}% cheaper than Ghana.")

    else:
        print("Both destinations have the same estimated travel cost.")

    print("\nCONCLUSION")
    print("-" * 45)
    print(f"Ghana Total: {CURRENCY}{ghana_total:,}")
    print(f"Kenya Total: {CURRENCY}{kenya_total:,}")

    if ghana_total < kenya_total:
        print("Based on these estimates, Ghana is the better option")
        print("for a traveller whose main priority is spending less.")
    elif kenya_total < ghana_total:
        print("Based on these estimates, Kenya is the better option")
        print("for a traveller whose main priority is spending less.")
    else:
        print("Based on these estimates, both destinations cost the same.")


def main():
    """Run the travel cost comparison."""
    # Check that both countries use the same expense categories.
    if ghana.keys() != kenya.keys():
        raise ValueError("The expense categories for both countries must match.")

    # Check that all estimated costs are non-negative numbers.
    for country_name, expenses in (("Ghana", ghana), ("Kenya", kenya)):
        for expense, amount in expenses.items():
            if not isinstance(amount, (int, float)) or amount < 0:
                raise ValueError(
                    f"Invalid cost for {country_name} - {expense}: {amount}"
                )

    ghana_total, kenya_total = display_comparison(ghana, kenya)
    compare_destinations(ghana_total, kenya_total)

    print("\nIMPORTANT NOTE")
    print("-" * 45)
    print("These figures are illustrative estimates, not confirmed booking prices.")
    print("Actual costs may change depending on travel dates and service providers.")
    print("The estimates cover one traveller and three nights of accommodation.")
    print("Entry permit fees, travel insurance, shopping and personal expenses")
    print("are excluded.")
    print("=" * 72)


if __name__ == "__main__":
    main()
