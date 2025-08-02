import streamlit as st
from api import STOCK
from api import TABLE

st.title = ("Company Info")
# This creates a subheader called 'Company Info'
table = TABLE()
stock = STOCK()
# This calls from the TABLE class in the backend and stores it in the variable 'table'

stock_selection = st.text_input("Enter a stock", value = "AAPL", key="shared4")


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
