import streamlit as st
from supabase import create_client, Client
import os
from auth import require_login, sign_out
from api import STOCK, GRAPH, TABLE

require_login()
# Makes sure user is logged in before accessing this page

# Set up database connection
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

# Get the current user's email
user_email = st.session_state.get("user_email")

# Logout button in sidebar
with st.sidebar:
    if st.button("Logout"):
        sign_out()

# Create API objects
stock = STOCK()
graph = GRAPH()
table = TABLE()

#________________________________________________________________________________________________

st.subheader("My Stock Watchlist")
# Page title

st.subheader("Search and Add a Stock")
# Section for adding new stocks

ticker_input = st.text_input("Enter a stock ticker (ex. AAPL, TSLA)")
# Text box for user to enter stock ticker

if ticker_input:
# If user entered a ticker, do the following:
    company_name = stock.get_company_name(ticker_input)
    # Get the company name for the ticker
    
    if company_name:
    # If we found a valid company:
        st.write(f"Found: {company_name}")
        # Show the company name
        
        if st.button("Add to Watchlist"):
        # If user clicks add button:
            # Check if stock is already in watchlist
            existing = supabase.table("watchlist").select("*").eq("user_email", user_email).eq("ticker", ticker_input.upper()).execute()
            
            if existing.data:
            # If stock already exists:
                st.info("Already in watchlist.")
                # Tell user it's already added
            else:
            # If stock doesn't exist, add it:
                supabase.table("watchlist").insert({"user_email": user_email, "ticker": ticker_input.upper()}).execute()
                # Add stock to database
                st.success(f"Added {ticker_input.upper()} to your watchlist!")
                # Show success message
    else:
    # If we couldn't find the company:
        st.error("Couldn't find stock info. Try a valid ticker.")
        # Show error message

st.divider()
# Add a line separator

st.subheader("Your Watchlist")
# Section for viewing saved stocks

# Get all stocks from user's watchlist
watchlist_data = supabase.table("watchlist").select("*").eq("user_email", user_email).execute().data
if not watchlist_data:
    watchlist_data = []
# Make list of just the ticker symbols
watchlist = []
for item in watchlist_data:
    watchlist.append(item["ticker"])

if not watchlist:
# If user has no stocks saved:
    st.info("No stocks pinned yet.")
    # Tell them they have no stocks
else:
# If user has stocks saved:
    selected_ticker = st.selectbox("Select a stock to view", watchlist)
    # Let them pick which stock to view

    if selected_ticker:
    # If they selected a stock:
        company_name = stock.get_company_name(selected_ticker)
        # Get company name
        st.subheader(f"{company_name} ({selected_ticker})")
        # Show company name and ticker

        # Show stock information table
        info_table = table.generate_table(selected_ticker)
        st.plotly_chart(info_table)

        # Let user pick time period and chart type
        time_period = st.selectbox("Time Period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"])
        chart_type = st.selectbox("Chart Type", ["Standard", "CandleStick"])
        
        # Get stock history and create chart
        history = graph.get_company_history(selected_ticker, time_period)
        chart = graph.generate_chart(history, chart_type, title=f"{selected_ticker} Price Chart")
        st.plotly_chart(chart)

    st.divider()
    # Add separator line
    
    st.write("Delete Stocks from Your Watchlist")
    # Section for deleting stocks
    
    for item in watchlist_data:
    # For each stock in watchlist:
        ticker = item["ticker"]
        # Get the ticker symbol
        
        if st.button(f"Delete {ticker}", key=f"delete-{ticker}"):
        # If user clicks delete button for this stock:
            supabase.table("watchlist").delete().eq("user_email", user_email).eq("ticker", ticker).execute()
            # Delete it from database
            st.success(f"Deleted {ticker}")
            # Show success message