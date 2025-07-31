# Frontend Streamlit

# ALL ANNOTATIONS TO LOOK BACK ON AND STUDY IF NEEDED

import streamlit as st
# Imports from streamlit, allowing for a frontend to be built more easily and a simple UI to be made
from api import API
# Imports the class called API from the api.py file
from api import STOCK
# Imports from the cass called STOCK from the api.py file
from api import GRAPH
import plotly.express as px

import pandas as pd


#_____________________________________________________________________

st.title("Currency & Stock Converter")
# Tite


st.subheader("Currency Conversion")
# Subheader

amount = st.number_input("Enter amount in USD:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_1")
# Enter amt of USD you want to convert from USD to a diff currency

api = API()
# Calls from backend API class
conversion_rates = api.get_conversion_rates()  
# Gets the conversion rates function from the backend API class

currency_selection = st.selectbox("Choose a currency", list(conversion_rates.keys()), key = '4')
# .keys = the name of the currency Ex: AED: 26, so AED is the key, and 26 is the conversion rate stored within the key


if currency_selection in conversion_rates:
# Of the currency I selected (AED) is a valid currency that can be fethxed from the api then do as follows below:
    rate = conversion_rates[currency_selection]
# Gets the conversion rate of the currency I selected
    converted_amount = amount * rate
# Multiplies the amount I chose in USD by the conversion rate, thus converting to the other currency
    st.write(f"{amount: }USD = {converted_amount: } {currency_selection }")
# Gives the output response for how many USD you chose converted to the other currency
else:
    st.error("Selected currency is not available")
# Error if it didn't work

#____________________________________________________________________

st.subheader("Stock Conversion")
# Subheader

stock = STOCK()
# Calls from the STOCK class in the backend

stock_selection_usd = st.text_input("Choose a stock", value="AAPL", key="1")
# Box allowing you to enter a stock you want to convert from USD to amount of shares using its ticker (ex. AAPL, MSFT)

stock_amount_usd = st.number_input("Enter amount in USD to convert to shares:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_2")
# Box allowing you to input the amount you want to convert to shares of a stock

company_name = stock.get_company_name(stock_selection_usd)
# Fetches from the STOCK class what the company you chose's name is

if stock_selection_usd:
# For the stock selected do the following as seen below:
    price1 = stock.get_stock_price_usd(stock_selection_usd)
# Fetches from the STOCK class in the backend and pulls the stock price in USD of one stock of the company selected
    if price1:
# For the price of one stock of the given company, do the following as shown below:
        shares1 = stock_amount_usd / price1
# Divides the amount of money in USD youy want to convert to stocks (ex.250), by the price of a single stock (ex.250/220 for an apple stock), thus giving you how many shares of a single company you have
        st.write(f"${stock_amount_usd: .2f} = {shares1: .5f} shares of {company_name} (1 share = ${price1: .2f})")
# Writes that the amount of money you inputted (stock_amount_usd) is equivalent to however many shares (shares1) it converted to as seen above, then gives the name of the company (company_name) (ex. 0.1 SHARES OF APPLE INC.), then gives you the price of a single stock from the get_stock_price_usd that was fetched from the backend STOCK class (price1) (ex. 1 share = $200)
# Ex of use. $200 = 1 share of Apple Inc. (1 share = $200)
    else:
        st.error("No stock entered/Stock entered incorrectly")
# Error if it didn't work

#____________________________________________________________________

st.subheader("Stock To Currency")
# Subheader
stock_selection_currency = st.text_input("Enter a stock", value = "AAPL", key="2")
# Box allowing you to enter the ticker (ex. AAPL, MSFT) for the stock you want
currency_selection2 = st.selectbox("Choose a currency", list(conversion_rates.keys()), key ='3')
# Allows you to select the currency you want so that you can convert it to shares of the stock you chose
company_name = stock.get_company_name(stock_selection_currency)
# Fetches from the STOCK class in the backend and gets the name of the company, rather than just the ticker
stock_amount_currency = st.number_input(f"Enter amount in {currency_selection2} to convert to shares of {company_name}:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_3")
# Box allowing you to enter the amount of the currency you selected (currency_selection2) to convert to shares of the company you chose and uses the (company_name) function because it converted the ticker (ex.AAPL) to its actual name.
# Ex of use. 600 AED to 1 share of apple inc. (Enter amount in AED to convert to shares of APPLE INC.)

if stock_selection_currency:
# For the stock selected do the following as seen below:
    price2 = stock.get_stock_price_usd(stock_selection_currency)
# Fetches from the STOCK class in the backend and gets the stock price of one stock of the stock you selected 
    #1 stock of Apple Inc. = $209
    rate2 = conversion_rates[currency_selection2]
# Gets the variable from the API class that gets conversion rates and uses it to get the covnersion rate of the currency you chose
    # Conversion from USD to currency - 3.7 is conversion from dollars to AED
    overall = price2*rate2
# Multiples the price of one stock in USD by the conversion rate, thus getting the cost of one stock share in the new currency you chose
    # Price of stock in currency = 209*3.7 = 770 AED/1 apple stock 

    if price2:
# For the price of one stock of the stock chose do the following as seen below:
        shares2 = stock_amount_currency/overall
# Uses the amount of the currency you selected (ex. 600AED) and divides it by the cost of one stock share in that given currency, thus giving you how many shares you have of a stock using a different currency to buy those shares 
        #2200/770 = shares of a stock you have (2200 AED / 770 AED (1 share) = how many shares you have) 
        st.write(f" ${stock_amount_currency:.2f} {currency_selection2} = {shares2:.5f} shares of {company_name} (1 share = ${overall:.2f})")
# Writes that the amount of the currency you chose (stock_amount_currency)(ex. 600AED) is equal to however many shares was calculated that you have (shares2) of the company you chose, but gives the company name because it was fetched from the STOCK class before and put into a variable (company_name) and then in parenthesis gives how much one share of a stock costs in the new currency you chose (ex. 1 share = 771 AED)
    else:
        st.error("Failed to retrieve stock price")
# Error if it didn't work

#________________________________________________________________________
st.subheader("Stock Trends")

graph = GRAPH()
stock_selection_trends = st.text_input("Enter a stock", value = "AAPL", key="6")

time = st.selectbox("Select time range:", ['1d', '5d', '1mo', '6mo', '1Y', '5Y' ] )

graph_type = st.selectbox("Select graph type:", ['Standard', 'CandleStick'] )


if stock_selection_trends:
    history = graph.get_company_history(stock_selection_trends, time)
    if history.empty:
        st.warning("No data available for this stock")
    else: 
        fig = graph.generate_chart(history, graph_type)
        st.plotly_chart(fig)

# pd.options.plotting.backend = "plotly"

# df = pd.DataFrame(dict(history))
# fig = df.plot.line()
# st.plotly_chart(fig)
