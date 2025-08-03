# Frontend Streamlit

# ALL ANNOTATIONS TO LOOK BACK ON AND STUDY IF NEEDED
import streamlit as st
# Imports from streamlit, allowing for a frontend to be built more easily and a simple UI to be made
from api import API
# Imports the class called API from the api.py file
from api import LOGIC
# Imports from the class LOGIC from the api.py file
from auth import require_login, sign_out
# Imports the functions 'require_login, and sign_out from the auth.py file
require_login()  
# Calls the require_login function, thus forcing us to login

with st.sidebar:
    if st.button("Logout"):
        sign_out()
# Creates a button in the sidebar, allowing us to logout when pressed because it acesses the sign_out function from auth.py

st.set_page_config(
    page_title="Currency & Stock Conversion App"
)
# Makes the page title (like in the little bar, not the actual website page), to be set to Currency & Stock Conversion App

#__________________________________________________________________________________________

st.title = ("Currency Converter")
# Titles the page 'Currency Converter'

amount = st.number_input("Enter amount in USD:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_1")
# Enter amt of USD you want to convert from USD to a diff currency

api = API()
# Calls from backend API class
logic = LOGIC()

conversion_rates = api.get_conversion_rates()  
# Gets the conversion rates function from the backend API class

currency_selection = st.selectbox("Choose a currency", list(conversion_rates.keys()), key = '4')
# .keys = the name of the currency Ex: AED: 26, so AED is the key, and 26 is the conversion rate stored within the key


if currency_selection in conversion_rates:
# Of the currency I selected (AED) is a valid currency that can be fethxed from the api then do as follows below:
    rate = conversion_rates[currency_selection]
# Gets the conversion rate of the currency I selected
    converted_amount = logic.usd_to_currency(amount, rate)
# Multiplies the amount I chose in USD by the conversion rate, thus converting to the other currency
    st.write(f"{amount: }USD = {converted_amount: } {currency_selection }")
# Gives the output response for how many USD you chose converted to the other currency
else:
    st.error("Selected currency is not available")
# Error if it didn't work


#____________________________________________________________________
