import datetime
import json
import os
import pandas as pd
import streamlit as st

# Initialize session state for meals
if 'meals' not in st.session_state:
    st.session_state.meals = []

# Load existing meals from JSON
def load_meals():
    if os.path.exists('meals.json'):
        with open('meals.json', 'r') as f:
            st.session_state.meals = json.load(f)

# Save meals to JSON
def save_meals():
    with open('meals.json', 'w') as f:
        json.dump(st.session_state.meals, f)

# Load on app start
load_meals()

# Prepared meals list
prepared_meals = ["Cornflakes and milk", "Pita with Cheese and pastrame", "Shnitzl with rice", 
                  "Nature valley and Choco", "Pizza", "Pizza-pita"]

# Main app
st.title("Meal Tracker")

# Sidebar menu
menu_choice = st.sidebar.selectbox("Menu", ["Add Meal", "View Summary", "Edit/Delete Meal"])

if menu_choice == "Add Meal":
    st.header("Add Meal")
    with st.form(key="add_form"):
        date = st.text_input("Enter date (DD-MM-YY)")
        time = st.time_input("Enter time (HH:MM)")
        meal_type = st.selectbox("Meal Type", ["Prepared", "Other"])
        
        if meal_type == "Prepared":
            meal = st.selectbox("Select Prepared Meal", prepared_meals)
        else:
            meal = st.text_input("Enter meal description")
        
        submit = st.form_submit_button("Add Meal")
        
        if submit:
            # Validate date
            try:
                datetime.datetime.strptime(date, '%d-%m-%y')
                if meal_type == "Other" and not meal.strip():
                    st.error("Meal description cannot be empty.")
                else:
                    st.session_state.meals.append({'date': date, 'time': str(time), 'meal': meal})
                    save_meals()
                    st.success("Meal added successfully!")
            except ValueError:
                st.error("Invalid date format. Use DD-MM-YY.")

elif menu_choice == "View Summary":
    st.header("View Summary")
    # Date range filter
    start_date = st.text_input("Enter start date (DD-MM-YY, or leave blank for all)")
    end_date = st.text_input("Enter end date (DD-MM-YY, or leave blank for same as start)")
    
    start_dt = None
    end_dt = None
    if start_date:
        try:
            start_dt = datetime.datetime.strptime(start_date, '%d-%m-%y')
            if end_date:
                end_dt = datetime.datetime.strptime(end_date, '%d-%m-%y')
                if end_dt < start_dt:
                    st.error("End date must be on or after start date.")
                    end_dt = None
            else:
                end_dt = start_dt  # Single day
        except ValueError:
            st.error("Invalid date format. Use DD-MM-YY.")
    
    # Filter meals
    filtered_meals = st.session_state.meals
    if start_dt and end_dt:
        filtered_meals = [
            m for m in st.session_state.meals
            if start_dt <= datetime.datetime.strptime(m['date'], '%d-%m-%y') <= end_dt
        ]
    
    if not filtered_meals:
        st.info("No meals found.")
    else:
        # Download button for all meals
        if st.button("Download Meals as JSON"):
            json_data = json.dumps(st.session_state.meals)
            st.download_button("Download JSON", json_data, "meals.json", "application/json")
        
        # Sort and display
        df = pd.DataFrame(filtered_meals)
        df = df.sort_values(by=['date', 'time'])  # Sort by date and time
        st.dataframe(df, use_container_width=True)

elif menu_choice == "Edit/Delete Meal":
    st.header("Edit/Delete Meal")
    if not st.session_state.meals:
        st.info("No meals to edit or delete.")
    else:
        # Display editable dataframe
        df = pd.DataFrame(st.session_state.meals)
        edited_df = st.data_editor(df, num_rows="dynamic", key="editor")
        
        if st.button("Save Changes"):
            st.session_state.meals = edited_df.to_dict('records')
            save_meals()
            st.success("Changes saved!")