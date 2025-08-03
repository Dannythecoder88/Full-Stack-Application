import streamlit as st
from supabase import create_client, Client
import os

supabase_url = os.getenv("SUPABASE_URL")
# Creates a variabe that stores the actual supabase url that is taken from the .env file
supabase_key = os.getenv("SUPABASE_KEY")
# Creates a variabe that stores the actual supabase key that is taken from the .env file

supabase: Client = create_client(supabase_url, supabase_key)
# Creates a supabase client with two attributes, which are the suoabse key and url from the .env
def sign_up(email, password):
#A function for signing up, which has two attributes (email and password), which are self explanitory
    try:
#Starts a try block, which tells Python: "Attempt to run the next lines of code. If any error occurs, it doesn't crash, but instead, jumps to the except block
        user = supabase.auth.sign_up({"email": email, "password": password })
# Signs up a new user with Supabase Auth using the provided email and password
        return user
# Returns the user data if signup was successful
    except Exception as e:
#If an error happened in the try block (e.g. email already in use, bad password, no internet), Python jumps here instead of crashing. The Exception as e part stores the error in the variable e, so we can access its message later.        
        st.error(f"Registration failed: {e}")
# Displays an error message in the Streamlit app if signup fails, in which e is replaced by the actual error

def sign_in(email, password):
#Creates a function called sign_in with two attributes (email and password)
    try:
#Starts a try block, which tells Python: "Attempt to run the next lines of code. If any error occurs, it doesn't crash, but instead, jumps to the except block
        user = supabase.auth.sign_in_with_password({"email": email, "password": password })
# Signs in a user with Supabase Auth using the provided email and password
        return user
# Returns the user data if sign in was successful

    except Exception as e:
#If an error happened in the try block (e.g. email already in use, bad password, no internet), Python jumps here instead of crashing. The Exception as e part stores the error in the variable e, so we can access its message later.        
        st.error(f"Login failed: {e}")
# Displays an error message in the Streamlit app if signup fails, in which e is replaced by the actual error

def sign_out():
# Creates a function called sign_out, allowing users to sign out
    try:
#Starts a try block, which tells Python: "Attempt to run the next lines of code. If any error occurs, it doesn't crash, but instead, jumps to the except block
        supabase.auth.sign_out()
# Signs out a user with Supabase Auth 
        st.session_state.user_email = None
# clears the local memory of the user's email, thus allowing the user to sign out freely
        st.rerun()
#Reruns the app once a user logs out
    except Exception as e:
#If an error happened in the try block (e.g. email already in use, bad password, no internet), Python jumps here instead of crashing. The Exception as e part stores the error in the variable e, so we can access its message later.
        st.error(f"Logout failed {e}")
# Displays an error message in the Streamlit app if signup fails, in which e is replaced by the actual error
def main_app(user_email):
# Creates a function with the attribute user_email
    st.success(f"Welcome, {user_email}! 👋")
#When user logs in, creates a success pop up that welcomes them 
    if st.button("Logout"):
#Creates a logout button for users to logout
        sign_out()
#signs out user after button is pressed

def auth_screen():
# Creates a function called auth_screen which displays the authencitcation screen for signing in / signing up
    st.subheader("Sign In/Sign Up")
# Makea a subheader called 'Sign In/Sign Up'
    option = st.selectbox("Choose an action:", ["Login", "Sign Up"])
#Creates a selectbox allowing you to choose whether you are logging in or signing up for an account
    email = st.text_input("Email")
# Creates a text input so that you can eneter your email
    password = st.text_input("Password", type="password")
#Creates a text input so you can enter you password
    if option == "Sign Up" and st.button("Register"):
# If you chose sign up, and clicked the register button (register button appears when sign up is chosen, because this code above made the register button), do the following:
        user = sign_up(email, password)
# Creates a variable that calls the sign_up function and puts in your email and password, thus allowing it to access Supabse Auth and sign you up, after email is confirmed
        if user and user.user:
# If user authentication is passed, and user is now a user in the database, do the followingL
            st.success("Registration successful. Please log in.")
# Success is shown, now you have to login, and to do so go back to the selectbox and choose the login feature, and logiun with your email and password you put in when you signed up

    if option == "Login" and st.button("Login"):
# If you chose Login and clicked the login button, do the following (Login button made with the line above):
        user = sign_in(email, password)
# Creates a variable called user that accesses the sign_in function, thus allowing you to access Supabase Auth and login
        if user and user.user:
# If the user is in the database, do the following:
            st.session_state.user_email = user.user.email
# This line stores the logged-in user's email in Streamlit's session so the app knows they're logged in and can show them the main app content.
            st.success(f"Welcome back, {email}!")
# Shows a success field and says 'Welcome back', follow by the users email
            st.rerun()
# Reruns the appliocation, as logged in


def require_login():
# Creates a function callewd require_login
    if "user_email" not in st.session_state or not st.session_state.user_email:
# If the users email is not entered when the app is open, then it makes you do the following:
        auth_screen()   
# Forces the user to sign in before entering he page
        st.stop() 
# Stops the execution of the streamlit scrip, thus blocking the user from accessing the page
if "user_email" not in st.session_state:
# Creates and initializes user_email to None if it’s not already there, so your app has a clear way to know “no one’s logged in yet.

    st.session_state.user_email = None
# What above said

require_login()  

main_app(st.session_state.user_email)

    