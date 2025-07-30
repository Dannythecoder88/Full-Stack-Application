# Frontend Streamlit
import streamlit as st
from api import API
from api import STOCK

#_____________________________________________________________________

st.title("Currency & Stock Converter")

st.subheader("Currency Conversion")
amount = st.number_input("Enter amount in USD:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_1")
# currency_selection = st.text_input(
#     "Choose a currency to convert to:"
# )


api = API()
conversion_rates = api.get_conversion_rates()  

currency_selection = st.selectbox("Choose a currency", list(conversion_rates.keys()), key = '4')



if currency_selection in conversion_rates:
    rate = conversion_rates[currency_selection]
    converted_amount = amount * rate

    st.write(f"{amount: }USD = {converted_amount: } {currency_selection }")
else:
    st.error("Selected currency is not available")

#____________________________________________________________________

st.subheader("Stock Conversion")

stock = STOCK()

stock_selection_usd = st.text_input("Choose a stock", value="AAPL", key="1")

stock_amount_usd = st.number_input("Enter amount in USD to convert to shares:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_2")

company_name = stock.get_company_name(stock_selection_usd)

if stock_selection_usd:
    price1 = stock.get_stock_price_usd(stock_selection_usd)
    if price1:
        shares1 = stock_amount_usd / price1
        st.write(f"${stock_amount_usd: .2f} = {shares1: .5f} shares of {company_name} (1 share = ${price1: .2f})")
    else:
        st.error("No stock entered/Stock entered incorrectly")

#____________________________________________________________________

st.subheader("Stock To Currency")
stock_selection_currency = st.text_input("Enter a stock", value = "AAPL", key="2")

currency_selection2 = st.selectbox("Choose a currency", list(conversion_rates.keys()), key ='3')

company_name = stock.get_company_name(stock_selection_currency)

stock_amount_currency = st.number_input(f"Enter amount in {currency_selection2} to convert to shares of {company_name}:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_3")



if stock_selection_currency:
    price2 = stock.get_stock_price_usd(stock_selection_currency)
    #US stock price - 209
    rate2 = conversion_rates[currency_selection2]
    #conversion from USD to currency - 3.7 AED
    overall = price2*rate2
    #price of stock in currency - 209*3.7 = 770 AED/1 apple stock
    #2200/770 = amount 

    if price2:
        shares2 = stock_amount_currency/overall
        #2200/770 = amount 
        st.write(f" ${stock_amount_currency:.2f} = {shares2:.5f} shares of {company_name} (1 share = ${overall:.2f})")
    else:
        st.error("Failed to retrieve stock price")
