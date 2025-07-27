#treamlit Frontend
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_API")