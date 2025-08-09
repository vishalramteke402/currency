pip install streamlit forex-python

import streamlit as st
from forex_python.converter import CurrencyRates, RatesNotAvailableError

# Create CurrencyRates instance
c = CurrencyRates()

# App title
st.title("💱 Currency Converter App")

# Input fields
amount = st.number_input("Enter Amount", min_value=0.0, format="%.2f")
from_currency = st.text_input("From Currency (e.g., USD, INR, EUR)").upper()
to_currency = st.text_input("To Currency (e.g., USD, INR, EUR)").upper()

# Convert button
if st.button("Convert"):
    try:
        if from_currency and to_currency:
            result = c.convert(from_currency, to_currency, amount)
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            st.error("Please enter both currency codes.")
    except RatesNotAvailableError:
        st.error("Currency rate not available or invalid currency code.")
    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.caption("Powered by forex-python | Created with Streamlit")
