import datetime
import json
import os
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# --- Load configuration for authentication ---
if os.path.exists('config.yaml'):
    with open('config.yaml', 'r') as file:
        config = yaml.load(file, Loader=SafeLoader)
else:
    try:
        config = yaml.load(st.secrets['config'], Loader=SafeLoader)
    except KeyError:
        st.error("Configuration not found. Please ensure config.yaml exists locally or secrets are set in Streamlit Cloud.")
        st.stop()

# --- Initialize authenticator ---
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# --- LOGIN ---
authenticator.login(location='main')

# --- LOGIN OUTCOME ---
if st.session_state["authentication_status"]:
    # ✅ Logged in successfully
    username = st.session_state["username"]
    name = st.session_state["name"]

    # --- Initialize meals state ---
    if 'meals' not in st.session_state:
        st.session_state.meals = {}

    # --- Load existing meals ---
    def load_meals():
        if os.path.exists('meals.json'):
            try:
                with open('meals.json', 'r') as f:
                    loaded_meals = json.load(f)
                    if isinstance(loaded_meals, dict):
                        st.session_state.meals = loaded_meals
                    else:
                        st.session_state.meals = {}
            except json.JSONDecodeError:
                st.session_state.meals = {}
        if username not in st.session_state.meals:
            st.session_state.meals[username] = []

    # --- Save meals ---
    def save_meals():
        try:
            with open('meals.json', 'w') as f:
                json.dump(st.session_state.meals, f)
        except Exception as e:
            st.error(f"Failed to save meals: {e}")

    load_meals()

    # --- Prepared meals ---
    prepared_meals = [
        "Cornflakes and milk",
        "Pita with Cheese and pastrame",
        "Shnitzl with rice",
        "Nature valley and Choco",
        "Pizza",
        "Pizza-pita"
    ]

    # --- Main app ---
    st.title(f"Meal Tracker - Welcome, {name}")
    authenticator.logout('Logout', 'sidebar')

    menu_choice = st.sidebar.selectbox("Menu", ["Add Meal", "View Summary", "Edit/Delete Meal"])

    # --- Add Meal ---
    if menu_choice == "Add Meal":
        st.header("Add Meal")
        if 'meal_type' not in st.session_state:
            st.session_state.meal_type = "Prepared"
        
        st.session_state.meal_type = st.selectbox("Meal Type", ["Prepared", "Other"], key="meal_type_select")
        
        with st.form(key="add_form"):
            date = st.text_input("Enter date (DD-MM-YY)")
            time = st.time_input("Enter time (HH:MM)")
            
            if st.session_state.meal_type == "Prepared":
                meal = st.selectbox("Select Prepared Meal", prepared_meals, key="prepared_meal")
            else:
                meal = st.text_input("Enter meal description", key="other_meal")
            
            submit = st.form_submit_button("Add Meal")
            
            if submit:
                try:
                    datetime.datetime.strptime(date, '%d-%m-%y')
                    if st.session_state.meal_type == "Other" and not meal.strip():
                        st.error("Meal description cannot be empty.")
                    else:
                        st.session_state.meals[username].append(
                            {'date': date, 'time': str(time), 'meal': meal}
                        )
                        save_meals()
                        st.success("Meal added successfully!")
                except ValueError:
                    st.error("Invalid date format. Use DD-MM-YY.")

    # --- View Summary ---
    elif menu_choice == "View Summary":
        st.header("View Summary")
        start_date = st.text_input("Enter start date (DD-MM-YY, or leave blank for all)")
        end_date = st.text_input("Enter end date (DD-MM-YY, or leave blank for same as start)")
        
        start_dt, end_dt = None, None
        if start_date:
            try:
                start_dt = datetime.datetime.strptime(start_date, '%d-%m-%y')
                if end_date:
                    end_dt = datetime.datetime.strptime(end_date, '%d-%m-%y')
                    if end_dt < start_dt:
                        st.error("End date must be on or after start date.")
                        end_dt = None
                else:
                    end_dt = start_dt
            except ValueError:
                st.error("Invalid date format. Use DD-MM-YY.")
        
        filtered_meals = st.session_state.meals.get(username, [])
        if start_dt and end_dt:
            filtered_meals = [
                m for m in st.session_state.meals.get(username, [])
                if start_dt <= datetime.datetime.strptime(m['date'], '%d-%m-%y') <= end_dt
            ]
        
        if not filtered_meals:
            st.info("No meals found.")
        else:
            if st.button("Download Meals as JSON"):
                json_data = json.dumps(st.session_state.meals.get(username, []))
                st.download_button("Download JSON", json_data, f"{username}_meals.json", "application/json")
            
            df = pd.DataFrame(filtered_meals)
            df = df.sort_values(by=['date', 'time'])
            st.dataframe(df, use_container_width=True)

    # --- Edit/Delete Meal ---
    elif menu_choice == "Edit/Delete Meal":
        st.header("Edit/Delete Meal")
        if not st.session_state.meals.get(username, []):
            st.info("No meals to edit or delete.")
        else:
            df = pd.DataFrame(st.session_state.meals.get(username, []))
            edited_df = st.data_editor(df, num_rows="dynamic", key="editor")
            
            if st.button("Save Changes"):
                st.session_state.meals[username] = edited_df.to_dict('records')
                save_meals()
                st.success("Changes saved!")

# --- WRONG PASSWORD ---
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")

# --- NO LOGIN YET ---
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
