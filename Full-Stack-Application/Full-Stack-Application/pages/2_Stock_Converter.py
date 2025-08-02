import streamlit as st
from api import STOCK
from api import LOGIC




st.title = ("Stock Conversion")
# Subheader

logic= LOGIC()
stock = STOCK()
# Calls from the STOCK class in the backend

stock_selection = st.text_input("Enter a stock", value = "AAPL", key="shared1")
# Box allowing you to enter a stock you want to convert from USD to amount of shares using its ticker (ex. AAPL, MSFT)

stock_amount_usd = st.number_input("Enter amount in USD to convert to shares:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_2")
# Box allowing you to input the amount you want to convert to shares of a stock

company_name = stock.get_company_name(stock_selection)
# Fetches from the STOCK class what the company you chose's name is

if stock_selection:
# For the stock selected do the following as seen below:
    price1 = stock.get_stock_price_usd(stock_selection)
# Fetches from the STOCK class in the backend and pulls the stock price in USD of one stock of the company selected
    if price1:
# For the price of one stock of the given company, do the following as shown below:
        shares1 = logic.stock_to_shares(stock_amount_usd, price1)
# Divides the amount of money in USD youy want to convert to stocks (ex.250), by the price of a single stock (ex.250/220 for an apple stock), thus giving you how many shares of a single company you have
        st.write(f"${stock_amount_usd: .2f} = {shares1: .5f} shares of {company_name} (1 share = ${price1: .2f})")
# Writes that the amount of money you inputted (stock_amount_usd) is equivalent to however many shares (shares1) it converted to as seen above, then gives the name of the company (company_name) (ex. 0.1 SHARES OF APPLE INC.), then gives you the price of a single stock from the get_stock_price_usd that was fetched from the backend STOCK class (price1) (ex. 1 share = $200)
# Ex of use. $200 = 1 share of Apple Inc. (1 share = $200)
    else:
        st.error("No stock entered/Stock entered incorrectly")
# Error if it didn't work