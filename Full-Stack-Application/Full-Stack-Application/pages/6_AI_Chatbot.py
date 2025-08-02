import streamlit as st
from api import AI


st.title = ("Stock, Currency, and Business Chatbot")

ai = AI()

user_input = st.text_input("Ask me something about stocks, businesses, or currencies:")


if user_input:
    response = ai.get_ai_response(user_input)
    st.write(response)
