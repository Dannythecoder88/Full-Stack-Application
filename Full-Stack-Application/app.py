# Frontend Streamlit

# ALL ANNOTATIONS TO LOOK BACK ON AND STUDY IF NEEDED

import streamlit as st
# Imports from streamlit, allowing for a frontend to be built more easily and a simple UI to be made
from api import API
# Imports the class called API from the api.py file
from api import STOCK
# Imports from the cass called STOCK from the api.py file
from api import GRAPH

from api import TABLE

from api import LOGIC

from api import AI

from supabase import create_client, Client

from dotenv import load_dotenv

import os

st.set_page_config(
    page_title="Currency & Stock Conversion App"
)
st.title = ("Currency Converter")

#_____________________________________________________________________

st.title("Currency & Stock Converter")
# Tite


st.subheader("Currency Conversion")
# Subheader

amount = st.number_input("Enter amount in USD:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_1")
# Enter amt of USD you want to convert from USD to a diff currency

api = API()
# Calls from backend API class
logic = LOGIC()

load_dotenv()


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

st.subheader("Stock Conversion")
# Subheader

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

#____________________________________________________________________

st.subheader("Stock To Currency")
# Subheader

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

#________________________________________________________________________
st.subheader("Stock Trends")
# Creates a subheader called 'Stock Trends'
graph = GRAPH()
# Creates a variable that calls the GRAPH class freom the backend

time = st.selectbox("Select time range:", ['1d', '5d', '1mo', '6mo', '1Y', '5Y' ] )
# Creates a dropdown selection box so that you can select the time range you want the graph to go up to

graph_type = st.selectbox("Select graph type:", ['Standard', 'CandleStick'] )
# Creates a dropdown allowing you to select the type of graph you want

if stock_selection:
# For the stock selected do the following as seen below:
    history = graph.get_company_history(stock_selection, time)
# Creates a dataframe that is stored in the variable history, and this datafram calls from the graph class in the backend, allowing you to acess the history of the company, and the time range you want this history to go up to
    if history.empty:
# If the yfinance library does not contain info on this stock selected, do the following:
        st.warning("No data available for this stock")
# Displays a warning explaining there is no data available for the stock you chose
    else: 
# Else, if there is data on the stock you selected, do the following:
        company_name = stock.get_company_name(stock_selection)
# Creates a variable called company_name that calls on the stock class in the backend and gets the full name of the stock you selected by calling on the get_company_name method within the stock class
        chart_title = f"{company_name} Stock Trends" 
# Allows the chart title to be set to the full name of the company, follow by the text 'Stock Trends' (Ex. if AAPL was the stock you selected, the title of the graph would be 'Apple Inc. Stock Info')
        fig = graph.generate_chart(history, graph_type, title = chart_title)
# Creates a variable called fig that calls from the graph class from the backend and uses the method generate_chart, allowing a chart to be made based on the company you chose, type of graph you chose, and also gets info from the company so that the graph can have the name of the company within it as the title (these are the 3 arguments that are inputted when calling the generate_graph method)
        st.plotly_chart(fig)
# This allows you to call the variable above in streamlit, so that it can be viewed in streamlit itself

#____________________________________________________________________
st.subheader("Company Info")
# This creates a subheader called 'Company Info'
table = TABLE()
# This calls from the TABLE class in the backend and stores it in the variable 'table'

if stock_selection:
# For the stock selected do the following as seen below:
        company_name = stock.get_company_name(stock_selection)
# Creates a variable called company_name that calls on the stock class in the backend and gets the full name of the stock you selected by calling on the get_company_name method within the stock class
        table_title = f"{company_name} Info" 
# Allows the chart title to be set to the full name of the company, follow by the text 'Info' (Ex. if AAPL was the stock you selected the title of the graph would be 'Apple Inc. Info')
        fig = table.generate_table(stock_selection, title = table_title)
# Creates a variable called fig that calls from the table class from the backend and uses the method within it called generate_table, allowing a chart to be made based on the company you chose by accessing the company info using the yfinanace library and logic in the backend, and also gets info from the company so that the graph can have the name of the company within it as the title (Ex. Apple Inc. Info) (these are the 2 arguments that are inputted when calling the generate_graph method)
        st.plotly_chart(fig)
# This allows you to call the variable above in streamlit, so that it can be viewed in streamlit itself

#____________________________________________________________________
st.subheader("Stock, Currency, and Business Chatbot")

ai = AI()

user_input = st.text_input("Ask me something about stocks, businesses, or currencies:")


if user_input:
    response = ai.get_ai_response(user_input)
    st.write(response)

#____________________________________________________________________

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

def sign_up(email, password):
    try:
        user = supabase.auth.sign_up({"email": email, "password": password })
        return user
    except Exception as e:
        st.error(f"Registration failed: {e}")

def sign_in(email, password):
    try:
        user = supabase.auth.sign_in_with_password({"email": email, "password": password })
        return user
    except Exception as e:
        st.error(f"Login failed: {e}")

def sign_out():
    try:
        supabase.auth.sign_out()
        st.session_state.user_email = None
        st.rerun()
    except Exception as e:
        st.error(f"Logout failed {e}")

def main_app(user_email):
    st.title("🎉 Welcome Page")
    st.success(f"Welcome, {user_email}! 👋")
    if st.button("Logout"):
        sign_out()

def auth_screen():
    st.subheader("Sign In/ Sign Up")
    option = st.selectbox("Choose an action:", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if option == "Sign Up" and st.button("Register"):
        user = sign_up(email, password)
        if user and user.user:
            st.success("Registration successful. Please log in.")

    if option == "Login" and st.button("Login"):
        user = sign_in(email, password)
        if user and user.user:
            st.session_state.user_email = user.user.email
            st.success(f"Welcome back, {email}!")
            st.rerun()

if "user_email" not in st.session_state:
    st.session_state.user_email = None

if st.session_state.user_email:
    main_app(st.session_state.user_email)
else:
    auth_screen()