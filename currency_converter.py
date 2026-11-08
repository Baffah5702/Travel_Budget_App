import streamlit as st
import requests


def get_exchange_rate(from_currency, to_currency):

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url, timeout=10)
    data = response.json()

    if data["result"] == "success":
        return data["rates"].get(to_currency)

    return None


def currency_converter():

    st.subheader("💱 Currency Converter")

    amount = st.number_input(
        "Enter amount",
        min_value=0.0,
        value=1.0
    )

    currencies = {
        "US Dollar (USD)": "USD",
        "Nigerian Naira (NGN)": "NGN",
        "British Pound (GBP)": "GBP",
        "Euro (EUR)": "EUR",
        "Canadian Dollar (CAD)": "CAD",
        "Ghanaian Cedi (GHS)": "GHS"
    }

    col1, col2 = st.columns(2)

    with col1:
        from_currency = st.selectbox(
            "From",
            list(currencies.keys())
        )

    with col2:
        to_currency = st.selectbox(
            "To",
            list(currencies.keys()),
            index=1
        )

    if st.button("Convert Currency"):

        from_code = currencies[from_currency]
        to_code = currencies[to_currency]

        try:
            rate = get_exchange_rate(from_code, to_code)

            if rate is not None:
                converted_amount = amount * rate

                st.success(
                    f"{amount:,.2f} {from_code} = "
                    f"{converted_amount:,.2f} {to_code}"
                )

                st.caption(
                    f"Exchange rate: 1 {from_code} = {rate:.4f} {to_code}"
                )

            else:
                st.error("Unable to get exchange rate.")

        except requests.exceptions.RequestException:
            st.error("Connection failed. Please check your internet.")