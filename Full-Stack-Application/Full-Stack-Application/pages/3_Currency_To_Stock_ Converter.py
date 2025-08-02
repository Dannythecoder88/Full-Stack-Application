import streamlit as st
from api import API
from api import STOCK
from api import LOGIC




stock = STOCK()
logic = LOGIC()
api = API()

st.title = ("Stock To Currency")
# Subheader

stock_selection = st.text_input("Enter a stock", value = "AAPL", key="shared2")

conversion_rates = api.get_conversion_rates()  

currency_selection2 = st.selectbox("Choose a currency", list(conversion_rates.keys()), key ='3')
# Allows you to select the currency you want so that you can convert it to shares of the stock you chose
company_name = stock.get_company_name(stock_selection)
# Fetches from the STOCK class in the backend and gets the name of the company, rather than just the ticker
stock_amount_currency = st.number_input(f"Enter amount in {currency_selection2} to convert to shares of {company_name}:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_3")
# Box allowing you to enter the amount of the currency you selected (currency_selection2) to convert to shares of the company you chose and uses the (company_name) function because it converted the ticker (ex.AAPL) to its actual name.
# Ex of use. 600 AED to 1 share of apple inc. (Enter amount in AED to convert to shares of APPLE INC.)

if stock_selection:
# For the stock selected do the following as seen below:
    price2 = stock.get_stock_price_usd(stock_selection)
# Fetches from the STOCK class in the backend and gets the stock price of one stock of the stock you selected 
    #1 stock of Apple Inc. = $209
    rate2 = conversion_rates[currency_selection2]
# Gets the variable from the API class that gets conversion rates and uses it to get the covnersion rate of the currency you chose
    # Conversion from USD to currency - 3.7 is conversion from dollars to AED

    overall = logic.usd_to_currency(price2, rate2)

# Multiples the price of one stock in USD by the conversion rate, thus getting the cost of one stock share in the new currency you chose
    # Price of stock in currency = 209*3.7 = 770 AED/1 apple stock 

    if price2:
# For the price of one stock of the stock chose do the following as seen below:
        shares2 = logic.stock_to_shares(stock_amount_currency, overall)
# Uses the amount of the currency you selected (ex. 600AED) and divides it by the cost of one stock share in that given currency, thus giving you how many shares you have of a stock using a different currency to buy those shares 
        #2200/770 = shares of a stock you have (2200 AED / 770 AED (1 share) = how many shares you have) 
        st.write(f" ${stock_amount_currency:.2f} {currency_selection2} = {shares2:.5f} shares of {company_name} (1 share = ${overall:.2f})")
# Writes that the amount of the currency you chose (stock_amount_currency)(ex. 600AED) is equal to however many shares was calculated that you have (shares2) of the company you chose, but gives the company name because it was fetched from the STOCK class before and put into a variable (company_name) and then in parenthesis gives how much one share of a stock costs in the new currency you chose (ex. 1 share = 771 AED)
    else:
        st.error("Failed to retrieve stock price")
# Error if it didn't work