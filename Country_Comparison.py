import streamlit as st

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
    return sum(expenses.values())


def country_comparison():
    st.title("🌍 Country Travel Cost Comparison")
    st.write("Compare estimated travel expenses for Ghana and Kenya.")

    ghana_total = calculate_total(ghana)
    kenya_total = calculate_total(kenya)

    st.subheader("Travel Expense Breakdown")

    st.table({
        "Expenses": list(ghana.keys()),
        "Ghana (₦)": list(ghana.values()),
        "Kenya (₦)": list(kenya.values())
    })

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Ghana Total", f"{CURRENCY}{ghana_total:,.2f}")

    with col2:
        st.metric("Kenya Total", f"{CURRENCY}{kenya_total:,.2f}")

    st.subheader("Travel Cost Analysis")

    if ghana_total < kenya_total:
        savings = kenya_total - ghana_total
        percentage = (savings / kenya_total) * 100

        st.success("Ghana is the more affordable destination.")
        st.write(f"Choosing Ghana saves {CURRENCY}{savings:,.2f}.")
        st.write(f"Ghana is approximately {percentage:.2f}% cheaper than Kenya.")

    elif kenya_total < ghana_total:
        savings = ghana_total - kenya_total
        percentage = (savings / ghana_total) * 100

        st.success("Kenya is the more affordable destination.")
        st.write(f"Choosing Kenya saves {CURRENCY}{savings:,.2f}.")
        st.write(f"Kenya is approximately {percentage:.2f}% cheaper than Ghana.")

    else:
        st.info("Both destinations have the same estimated travel cost.")

    st.caption(
        "Note: These are illustrative estimates for one traveller "
        "and three nights. They are not confirmed booking prices."
    )