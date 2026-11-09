
import streamlit as st
import requests

from trip_budget import TripBudget

st.set_page_config(
    page_title="Trip Budget Calculator",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ Trip Budget Calculator")
st.write("Calculate your total travel budget and daily spending limits.")

st.subheader("Enter Your Travel Details")

# User inputs
home_currency = st.selectbox(
    "Select Home Currency",
    ["NGN", "USD", "GBP", "EUR"]
)

destination_currency = st.selectbox(
    "Select Destination Currency",
    ["USD", "GBP", "EUR", "NGN"]
)

total_budget = st.number_input(
    "Enter Your Total Budget",
    min_value=0.0,
    value=100000.0
)

duration = st.number_input(
    "Travel Duration (Days)",
    min_value=1,
    value=7,
    step=1
)

amount_spent = st.number_input(
    "Amount Already Spent (Home Currency)",
    min_value=0.0,
    value=0.0
)


# Function to get exchange rate
def get_exchange_rate(home, destination):
    try:
        if home == destination:
            return 1.0

        url = f"https://open.er-api.com/v6/latest/{home}"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if data.get("result") != "success":
            raise ValueError("Exchange rate service failed.")

        rate = data["rates"].get(destination)

        if rate is None:
            raise ValueError("Exchange rate not available.")

        return float(rate)

    except requests.exceptions.RequestException:
        raise ValueError("Unable to connect to exchange rate service.")

    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(f"Exchange rate error: {error}")


# Calculate budget
if st.button("Calculate Travel Budget"):

    if total_budget <= 0:
        st.error("Please enter a valid travel budget.")

    elif amount_spent > total_budget:
        st.error("Amount spent cannot exceed your total budget.")

    else:
        try:
            exchange_rate = get_exchange_rate(
                home_currency,
                destination_currency
            )

            budget = TripBudget(
                total_budget,
                duration,
                exchange_rate
            )

            summary = budget.get_budget_summary(amount_spent)

            st.success("Your travel budget has been calculated!")

            st.subheader("Travel Budget Summary")

            st.metric(
                "Total Budget",
                f"{home_currency} {total_budget:,.2f}"
            )

            st.metric(
                "Daily Spending Limit",
                f"{home_currency} {summary['Daily Spending Limit']:,.2f}"
            )

            st.metric(
                "Destination Budget",
                f"{destination_currency} {summary['Destination Budget']:,.2f}"
            )

            st.metric(
                "Daily Destination Limit",
                f"{destination_currency} {summary['Daily Destination Limit']:,.2f}"
            )

            st.metric(
                "Remaining Budget",
                f"{home_currency} {summary['Remaining Budget']:,.2f}"
            )

            st.write(
                f"**Exchange Rate:** 1 {home_currency} = "
                f"{exchange_rate:.4f} {destination_currency}"
            )

        except ValueError as error:
            st.error(str(error))

        except Exception as error:
            st.error(f"An unexpected error occurred: {error}")
