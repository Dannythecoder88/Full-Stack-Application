from auth import require_login, sign_out
import streamlit as st

st.set_page_config(page_title="Main App", layout="centered")
require_login()

st.title(f"🎉 Welcome, {st.session_state.user_email}")
st.write("You now have access to the full app.")

if st.button("Logout"):
    sign_out()