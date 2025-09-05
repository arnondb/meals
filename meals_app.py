# meals_app.py
import streamlit as st
import streamlit_authenticator as stauth
import copy
import pandas as pd
from supabase import create_client, Client
from datetime import datetime

# --- AUTH SETUP ---
try:
    credentials = copy.deepcopy(st.secrets["credentials"])
    cookie = copy.deepcopy(st.secrets["cookie"])
except Exception as e:
    st.error(f"Failed to load configuration from secrets: {e}")
    st.stop()

authenticator = stauth.Authenticate(
    credentials,
    cookie["name"],
    cookie["key"],
    cookie["expiry_days"]
)

# --- LOGIN ---
name, authentication_status, username = authenticator.login(location="main")

if authentication_status is False:
    st.error("Username/password is incorrect")
    st.stop()
elif authentication_status is None:
    st.warning("Please enter your username and password")
    st.stop()

authenticator.logout("Logout", "sidebar")
st.sidebar.write(f"Welcome *{name}*")

# --- SUPABASE SETUP ---
SUPABASE_URL = st.secrets["SUPABASE"]["url"]
SUPABASE_KEY = st.secrets["SUPABASE"]["key"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# --- APP UI ---
st.title("Meals Tracker")

with st.form("meal_form"):
    meal = st.text_input("Meal")
    date = st.text_input("Date (YYYY-MM-DD)", value=datetime.today().strftime("%Y-%m-%d"))
    time = st.text_input("Time (HH:MM)", value=datetime.now().strftime("%H:%M"))
    submitted = st.form_submit_button("Add Meal")

    if submitted:
        if not meal.strip() or not date.strip() or not time.strip():
            st.error("All fields are required.")
        else:
            data = {
                "meal": meal,
                "date": date,
                "time": time
            }
            response = supabase.table("meals").insert(data).execute()
            if response.error:
                st.error(f"Failed to add meal: {response.error.message}")
            else:
                st.success(f"Meal '{meal}' added!")

# --- SHOW MEALS ---
st.subheader("All Meals")
response = supabase.table("meals").select("*").order("date", ascending=False).order("time", ascending=False).execute()
if response.error:
    st.error(f"Failed to fetch meals: {response.error.message}")
else:
    meals_df = pd.DataFrame(response.data)
    if meals_df.empty:
        st.info("No meals recorded yet.")
    else:
        st.dataframe(meals_df)
