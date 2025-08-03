import streamlit as st
from api import AI
from auth import require_login, sign_out
require_login()  

with st.sidebar:
    if st.button("Logout"):
        sign_out()

st.set_page_config(
    page_title="Currency & Stock Conversion App"
)

#________________________________________________________________________________________________

st.title = ("Stock, Currency, and Business Chatbot")
# Titles the page 'Stock, Currency, and Business Chatbot'
ai = AI()
# Creates a variable called 'ai' that calls the AI class from the backend

user_input = st.text_input("Ask me something about stocks, businesses, or currencies:")
# Creates a text box allowing the user to input something related to stock, business, or currencies and puts it in a variable so it can be sent to the backend and sent to GPT to answer

if user_input:
# For user_input do the following:
    response = ai.get_ai_response(user_input)
# creates a variable called response that calls the AI class in the backend and uses the method get_ai_response to call GPT and get its response to what was inputted by the user (user_input)
    st.write(response)
# Writes the response that GPT gave