# Frontend Streamlit

# ALL ANNOTATIONS TO LOOK BACK ON AND STUDY IF NEEDED
import streamlit as st
# Imports from streamlit, allowing for a frontend to be built more easily and a simple UI to be made
from api import API
# Imports the class called API from the api.py file
from api import LOGIC
from supabase import create_client, Client


st.set_page_config(
    page_title="Currency & Stock Conversion App"
)
st.title = ("Currency Converter")
st.sidebar.success("Select a page above:")

amount = st.number_input("Enter amount in USD:", min_value=0.0, format="%.2f", step=1.0, key="usd_input_1")
# Enter amt of USD you want to convert from USD to a diff currency

api = API()
# Calls from backend API class
logic = LOGIC()

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

# supabase_url = os.getenv("SUPABASE_URL")
# supabase_key = os.getenv("SUPABASE_KEY")
# supabase: Client = create_client(supabase_url, supabase_key)

# def sign_up(email, password):
#     try:
#         user = supabase.auth.sign_up({"email": email, "password": password })
#         return user
#     except Exception as e:
#         st.error(f"Registration failed: {e}")

# def sign_in(email, password):
#     try:
#         user = supabase.auth.sign_in_with_password({"email": email, "password": password })
#         return user
#     except Exception as e:
#         st.error(f"Login failed: {e}")

# def sign_out():
#     try:
#         supabase.auth.sign_out()
#         st.session_state.user_email = None
#         st.rerun()
#     except Exception as e:
#         st.error(f"Logout failed {e}")

# def main_app(user_email):
#     st.title("🎉 Welcome Page")
#     st.success(f"Welcome, {user_email}! 👋")
#     if st.button("Logout"):
#         sign_out()

# def auth_screen():
#     st.subheader("Sign In/ Sign Up")
#     option = st.selectbox("Choose an action:", ["Login", "Sign Up"])
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")

#     if option == "Sign Up" and st.button("Register"):
#         user = sign_up(email, password)
#         if user and user.user:
#             st.success("Registration successful. Please log in.")

#     if option == "Login" and st.button("Login"):
#         user = sign_in(email, password)
#         if user and user.user:
#             st.session_state.user_email = user.user.email
#             st.success(f"Welcome back, {email}!")
#             st.rerun()

# if "user_email" not in st.session_state:
#     st.session_state.user_email = None

# if st.session_state.user_email:
#     main_app(st.session_state.user_email)
# else:
#     auth_screen()