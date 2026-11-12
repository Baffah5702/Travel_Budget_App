from currency_converter import currency_converter
from expense_tracker import expense_tracker
from app import main as ai_travel_adviser
from budget_calculator import budget_calculator
from Country_Comparison import country_comparison
import streamlit as st


# Page configuration
st.set_page_config(
    page_title="Travel Budget App",
    page_icon="✈️",
    layout="wide"
)


# Navigation
st.sidebar.title("✈️ Travel Menu")

menu = st.sidebar.selectbox(
    "Choose a feature",
    [
        "Home",
        "Currency Converter",
        "Budget Calculator",
        "Expense Tracker",
        "Country Comparison",
        "Public Holiday Checker",
        "AI Travel Adviser"
    ]
)


# Application title
st.title("✈️ Travel Budget Application")

st.write("Welcome! Plan your travels and manage your budget easily.")

st.divider()

st.header(menu)


# HOME DASHBOARD
if menu == "Home":

    st.success("Welcome to your Travel Budget!")

    st.write(
        "Your personal assistant for planning trips, "
        "tracking expenses and managing travel budgets."
    )

    st.subheader("Plan Your Trip")

    col1, col2 = st.columns(2)

    with col1:
        destination = st.text_input(
            "Where are you travelling to?",
            placeholder="e.g. London, United Kingdom"
        )

    with col2:
        departure_date = st.date_input(
            "Departure Date"
        )

    if st.button("Save Trip"):
        if destination:
            st.success(f"Your trip to {destination} has been saved!")
        else:
            st.warning("Please enter your destination.")

    st.divider()

    # Get saved budget
    total_budget = st.session_state.get("total_budget", 0)

    # Get budget currency
    budget_currency = st.session_state.get("budget_currency", "NGN")

    # Get saved expenses
    expenses = st.session_state.get("expenses", [])

    # Calculate expenses in the budget currency
    total_expenses = sum(
        expense.amount
        for expense in expenses
        if expense.currency == budget_currency
    )

    # Calculate remaining balance
    remaining_balance = total_budget - total_expenses

    # Display dashboard metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Budget",
            f"{budget_currency} {total_budget:,.2f}"
        )

    with col2:
        st.metric(
            "Total Expenses",
            f"{budget_currency} {total_expenses:,.2f}"
        )

    with col3:
        st.metric(
            "Remaining Balance",
            f"{budget_currency} {remaining_balance:,.2f}"
        )


# CURRENCY CONVERTER
elif menu == "Currency Converter":
    currency_converter()


# BUDGET CALCULATOR
elif menu == "Budget Calculator":
    budget_calculator()


# EXPENSE TRACKER
elif menu == "Expense Tracker":
    expense_tracker()


# COUNTRY COMPARISON
elif menu == "Country Comparison":
    country_comparison()


# PUBLIC HOLIDAY CHECKER
elif menu == "Public Holiday Checker":
    st.info("Public Holiday Checker module coming soon.")


# AI TRAVEL ADVISER
elif menu == "AI Travel Adviser":
    ai_travel_adviser()