import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Travel Budget App",
    page_icon="✈️",
    layout="wide"
)

# Application title
st.title("✈️ Travel Budget Application")

st.write("Welcome! Plan your travels and manage your budget baffah.")

st.divider()

# Welcome section
st.header("Welcome to Your Travel Dashboard")

st.write(
    "Your personal assistant for planning trips tracking expenses and managing travel budgets."
)
st.subheader("Plan Your Trip")

col1, col2= st.columns(2)

with col1:
    destination = st.text_input(
        "Where are you travelling to?",
        placeholder="e.g London,United kingdom"
    )
with col2:
    departure_date = st.date_input(
        "Departure Date"
    )
if st.button("Save Trip"):
    if destination:
        st.success(f"Your Trip to{destination} has been saved")
    else:
        st.warning("Please enter your destination")            

# Dashboard metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Budget", "$0")

with col2:
    st.metric("Total Expenses", "$0")

with col3:
    st.metric("Remaining Balance", "$0")

st.divider()

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

st.header(menu)

if menu == "Home":
    st.success("Welcome to your Travel Budget baffa!")

elif menu == "Currency Converter":
    st.info("Currency Converter module coming soon.")

elif menu == "Budget Calculator":
    st.info("Budget Calculator module coming soon.")

elif menu == "Expense Tracker":
    st.info("Expense Tracker module coming soon.")

elif menu == "Country Comparison":
    st.info("Country Comparison module coming soon.")

elif menu == "Public Holiday Checker":
    st.info("Public Holiday Checker module coming soon.")

elif menu == "AI Travel Adviser":
    st.info("AI Travel Adviser module coming soon.")
    