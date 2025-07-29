# Frontend Streamlit
import streamlit as st
from api import API

st.title("Currency Converter")

amount = st.number_input("Enter amount in USD:", min_value=0.0, format="%.2f")

currency_selection = st.text_input(
    "Choose a currency to convert to:"
)

api = API()
conversion_rates = api.get_conversion_rates()  

if currency_selection in conversion_rates:
    rate = conversion_rates[currency_selection]
    converted_amount = amount * rate

    st.subheader("Conversion")
    st.write(f"{amount:} USD = {converted_amount:} {currency_selection}")
else:
    st.error("Selected currency is not available")