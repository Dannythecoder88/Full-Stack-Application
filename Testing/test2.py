#Streamlit Frontend
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("Exchange_Rate_API")

st.title("Currency Converter")