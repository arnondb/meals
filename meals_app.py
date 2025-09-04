import datetime
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from supabase import create_client

# --- Load config from secrets ---
try:
    config = {
        "credentials": st.secrets["credentials"],
        "cookie": st.secrets["cookie"],
        "preauthorized": st.secrets.get("preauthorized", []),
    }
except Exception as e:
    st.error(f"Failed to load configuration from secrets: {e}")
    st.stop()

# --- Initialize authenticator ---
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

# --- Supabase client ---
supabase_url = st.secrets["SUPABASE"]["url"]
supabase_key = st.secrets["SUPABASE"]["key"]
supabase = create_client(supabase_url, supabase_key)

# --- LOGIN FORM ---
authenticator.login(location="main")

# --- LOGIN OUTCOME ---
if st.session_state.get("authentication_status"):
    username = st.session_state.get("username")
    name = st.session_state.get("name")

    st.title(f"Meal Tracker - Welcome, {name}")
    authenticator.logout("Logout", "sidebar")

    # Sidebar menu
    menu_choice = st.sidebar.selectbox(
        "Menu", ["Add Meal", "View Summary", "Edit/Delete Meal"]
    )

    # --- Add Meal ---
    if menu_choice == "Add Meal":
        st.header("Add Meal")
        prepared_meals = [
            "Cornflakes and milk",
            "Pita with Cheese and Pastrami",
            "Schnitzel with rice",
            "Nature Valley and Choco",
            "Pizza",
            "Pizza-pita",
        ]

        meal_type = st.selectbox("Meal Type", ["Prepared", "Other"])
        with st.form(key="add_form"):
            date = st.text_input("Enter date (DD-MM-YY)")
            time = st.text_input("Enter time (HH:MM)")
            if meal_type == "Prepared":
                meal = st.selectbox("Select Prepared Meal", prepared_meals)
            else:
                meal = st.text_input("Enter meal description")

            submit = st.form_submit_button("Add Meal")

            if submit:
                try:
                    # validate date
                    datetime.datetime.strptime(date, "%d-%m-%y")
                    if meal_type == "Other" and not meal.strip():
                        st.error("Meal description cannot be empty.")
                    else:
                        data = {
                            "username": username,
                            "meal": meal,
                            "date": date,
                            "time": time,
                        }
                        supabase.table("meals").insert(data).execute()
                        st.success("Meal added successfully!")
                except ValueError:
                    st.error("Invalid date format. Use DD-MM-YY.")

    # --- View Summary ---
    elif menu_choice == "View Summary":
        st.header("View Summary")
        start_date = st.text_input("Enter start date (DD-MM-YY, or leave blank for all)")
        end_date = st.text_input("Enter end date (DD-MM-YY, or leave blank for same as start)")

        query = supabase.table("meals").select("*").eq("username", username)
        meals_response = query.execute()
        meals = meals_response.data if meals_response.data else []

        if start_date:
            try:
                start_dt = datetime.datetime.strptime(start_date, "%d-%m-%y")
                if end_date:
                    end_dt = datetime.datetime.strptime(end_date, "%d-%m-%y")
                else:
                    end_dt = start_dt
                meals = [
                    m
                    for m in meals
                    if start_dt
                    <= datetime.datetime.strptime(m["date"], "%d-%m-%y")
                    <= end_dt
                ]
            except ValueError:
                st.error("Invalid date format. Use DD-MM-YY.")

        if not meals:
            st.info("No meals found.")
        else:
            import pandas as pd
            df = pd.DataFrame(meals)
            df = df.sort_values(by=["date", "time"])
            st.dataframe(df, use_container_width=True)

            json_data = df.to_json(orient="records")
            st.download_button(
                "Download JSON",
                json_data,
                f"{username}_meals.json",
                "application/json",
            )

    # --- Edit/Delete Meal ---
    elif menu_choice == "Edit/Delete Meal":
        st.header("Edit/Delete Meal")
        meals_response = (
            supabase.table("meals").select("*").eq("username", username).execute()
        )
        meals = meals_response.data if meals_response.data else []

        if not meals:
            st.info("No meals to edit or delete.")
        else:
            import pandas as pd
            df = pd.DataFrame(meals)
            edited_df = st.data_editor(df, num_rows="dynamic", key="editor")

            if st.button("Save Changes"):
                try:
                    # Clear existing user meals
                    supabase.table("meals").delete().eq("username", username).execute()
                    # Insert updated meals
                    for record in edited_df.to_dict("records"):
                        supabase.table("meals").insert(record).execute()
                    st.success("Changes saved!")
                except Exception as e:
                    st.error(f"Error saving changes: {e}")

# --- LOGIN ERRORS ---
elif st.session_state.get("authentication_status") is False:
    st.error("Username/password is incorrect")
elif st.session_state.get("authentication_status") is None:
    st.warning("Please enter your username and password")
