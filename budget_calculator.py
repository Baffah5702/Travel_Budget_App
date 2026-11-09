import streamlit as st


def budget_calculator():

    st.subheader("💰 Travel Budget Calculator")

    st.write(
        "Plan your travel expenses and manage your "
        "money with this budget calculator."
    )

    st.divider()

    # Travel information
    st.subheader("Enter Your Travel Information")

    with st.form("budget_calculator_form"):

        currency = st.selectbox(
            "Select Currency",
            ["NGN", "USD", "GBP", "EUR", "CAD", "GHS"]
        )

        total_budget = st.number_input(
            "Total Travel Budget",
            min_value=0.0,
            value=100000.0,
            step=10000.0
        )

        travellers = st.number_input(
            "Number of Travellers",
            min_value=1,
            value=1,
            step=1
        )

        days = st.number_input(
            "Duration of Trip (Days)",
            min_value=1,
            value=5,
            step=1
        )

        calculate = st.form_submit_button(
            "Calculate Budget"
        )

    # Calculate budget
    if calculate:

        if total_budget <= 0:
            st.warning("Please enter a valid travel budget.")

        else:

            # Budget allocation
            transport = total_budget * 0.30
            accommodation = total_budget * 0.25
            food = total_budget * 0.20
            activities = total_budget * 0.15
            emergency = total_budget * 0.10

            # Calculate totals
            per_person = total_budget / travellers
            per_day = total_budget / days

            st.divider()

            st.success("Your travel budget has been calculated!")

            # Display total budget
            st.subheader("📊 Budget Summary")

            st.metric(
                "Total Travel Budget",
                f"{currency} {total_budget:,.2f}"
            )

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Budget Per Person",
                    f"{currency} {per_person:,.2f}"
                )

            with col2:
                st.metric(
                    "Budget Per Day",
                    f"{currency} {per_day:,.2f}"
                )

            st.divider()

            # Display budget breakdown
            st.subheader("📋 Budget Breakdown")

            budget_items = {
                "Transport (30%)": transport,
                "Accommodation (25%)": accommodation,
                "Food (20%)": food,
                "Activities (15%)": activities,
                "Emergency Savings (10%)": emergency
            }

            for category, amount in budget_items.items():

                st.write(
                    f"**{category}:** "
                    f"{currency} {amount:,.2f}"
                )

                st.progress(
                    int((amount / total_budget) * 100)
                )

            st.divider()

            # Final advice
            st.subheader("💡 Budget Advice")

            st.write(
                "1. Keep track of your daily expenses."
            )

            st.write(
                "2. Avoid spending more than your planned budget."
            )

            st.write(
                "3. Keep your emergency savings for unexpected costs."
            )

            st.write(
                "4. Compare transport and accommodation prices "
                "before making payments."
            )