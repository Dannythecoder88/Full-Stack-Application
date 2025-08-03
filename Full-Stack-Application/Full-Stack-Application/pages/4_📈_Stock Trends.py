import streamlit as st
from api import STOCK
from api import GRAPH
from auth import require_login, sign_out

require_login()  

with st.sidebar:
    if st.button("Logout"):
        sign_out()

st.set_page_config(
    page_title="Currency & Stock Conversion App"
)

#________________________________________________________________________________________________


st.title = ("Stock Trends")
# Creates a subheader called 'Stock Trends'
graph = GRAPH()
stock = STOCK()
# Creates a variable that calls the GRAPH class freom the backend

stock_selection = st.text_input("Enter a stock", value = "AAPL", key="shared3")

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
