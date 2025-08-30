import datetime
import json
from tabulate import tabulate

# Initialize meals list
meals = []

# Load existing meals
def load_meals():
    global meals
    try:
        with open('meals.json', 'r') as f:
            meals = json.load(f)
    except FileNotFoundError:
        meals = []

# Save meals to file
def save_meals():
    with open('meals.json', 'w') as f:
        json.dump(meals, f)

# Add a meal
def add_meal():
    prepared_meals = ["Cornflakes and milk", "Pita with Cheese and pastrame", "Shnitzl with rice", 
                      "Nature valley and Choco", "Pizza", "Pizza-pita"]
    
    while True:
        date = input("Enter date (DD-MM-YY, or 'q' to quit): ")
        if date.lower() == 'q':
            print("Cancelled. Returning to menu.")
            return
        try:
            datetime.datetime.strptime(date, '%d-%m-%y')
            break
        except ValueError:
            print("Invalid date format. Use DD-MM-YY or 'q' to quit.")
    
    while True:
        time = input("Enter time (HH:MM, 24-hour, or 'q' to quit): ")
        if time.lower() == 'q':
            print("Cancelled. Returning to menu.")
            return
        try:
            datetime.datetime.strptime(time, '%H:%M')
            break
        except ValueError:
            print("Invalid time format. Use HH:MM or 'q' to quit.")
    
    while True:
        meal_type = input("Prepared meal (p), other (o), or 'q' to quit? ").lower()
        if meal_type == 'q':
            print("Cancelled. Returning to menu.")
            return
        if meal_type in ['p', 'o']:
            break
        print("Please enter 'p', 'o', or 'q'.")
    
    if meal_type == 'p':
        if not prepared_meals:
            print("No prepared meals available. Please choose 'o' for other.")
            return
        print("Prepared meals:")
        for i, meal in enumerate(prepared_meals, 1):
            print(f"{i}. {meal}")
        while True:
            choice = input("Choose a meal (number, or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Cancelled. Returning to menu.")
                return
            try:
                choice = int(choice)
                if 1 <= choice <= len(prepared_meals):
                    meal = prepared_meals[choice - 1]
                    break
                print(f"Please enter a number between 1 and {len(prepared_meals)} or 'q'.")
            except ValueError:
                print("Please enter a valid number or 'q'.")
    else:
        while True:
            meal = input("Enter meal description (or 'q' to quit): ")
            if meal.lower() == 'q':
                print("Cancelled. Returning to menu.")
                return
            if meal.strip():
                break
            print("Meal description cannot be empty.")
    
    meals.append({'date': date, 'time': time, 'meal': meal})
    save_meals()
    print("Meal added successfully!")

# View summary with date range filter
def view_summary():
    if not meals:
        print("No meals recorded.")
        return
    
    # Prompt for start date
    start_dt = None
    while True:
        start_date = input("Enter start date (DD-MM-YY, or Enter for all): ")
        if not start_date:
            filtered_meals = meals
            break
        try:
            start_dt = datetime.datetime.strptime(start_date, '%d-%m-%y')
            break
        except ValueError:
            print("Invalid date format. Use DD-MM-YY or Enter.")
    
    # Prompt for end date only if start date was provided
    end_dt = None
    if start_date:
        while True:
            end_date = input("Enter end date (DD-MM-YY, or Enter for same as start): ")
            if not end_date:
                end_dt = start_dt  # Use start date as end date for single-day filter
                break
            try:
                end_dt = datetime.datetime.strptime(end_date, '%d-%m-%y')
                if end_dt >= start_dt:
                    break
                print("End date must be on or after start date.")
            except ValueError:
                print("Invalid date format. Use DD-MM-YY or Enter.")
    
    # Filter meals based on dates
    if start_dt and end_dt:
        filtered_meals = [
            m for m in meals
            if start_dt <= datetime.datetime.strptime(m['date'], '%d-%m-%y') <= end_dt
        ]
    else:
        filtered_meals = meals  # No filtering if no dates or only start date and end date is same
    
    if not filtered_meals:
        print("No meals found" + (f" for range {start_date} to {end_date}" if start_date and end_date else f" for {start_date}" if start_date else "."))
        return
    
    # Sort and display
    sorted_meals = sorted(filtered_meals, key=lambda x: (datetime.datetime.strptime(x['date'], '%d-%m-%y'), x['time']))
    table_data = [[e['date'], e['time'], e['meal']] for e in sorted_meals]
    print("\nMeal Summary")
    print(tabulate(table_data, headers=['Date', 'Time', 'Meal'], tablefmt='grid'))

# Edit or delete a meal
def edit_delete_meal():
    if not meals:
        print("No meals to edit or delete.")
        return
    
    print("\nSelect a meal to edit or delete:")
    print(f"{'#':<4} {'Date':<10} {'Time':<8} {'Meal':<30}")
    print("=" * 52)
    for i, entry in enumerate(meals, 1):
        meal_display = (entry['meal'][:27] + "...") if len(entry['meal']) > 27 else entry['meal']
        print(f"{i:<4} {entry['date']:<10} {entry['time']:<8} {meal_display:<30}")
    
    while True:
        choice = input("Enter meal number (or 'q' to quit): ")
        if choice.lower() == 'q':
            print("Cancelled. Returning to menu.")
            return
        try:
            choice = int(choice)
            if 1 <= choice <= len(meals):
                break
            print(f"Please enter a number between 1 and {len(meals)} or 'q' to quit.")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
    
    while True:
        action = input("Edit (e) or Delete (d)? ").lower()
        if action in ['e', 'd']:
            break
        print("Please enter 'e' or 'd'.")
    
    if action == 'd':
        meals.pop(choice - 1)
        save_meals()
        print("Meal deleted successfully!")
        return
    
    prepared_meals = ["Cornflakes and milk", "Pita with Cheese and pastrame", "Shnitzl with rice", 
                      "Nature valley and Choco", "Pizza", "Pizza-pita"]
    while True:
        date = input(f"Enter new date (DD-MM-YY, or Enter to keep {meals[choice-1]['date']}): ")
        if not date:
            date = meals[choice-1]['date']
        else:
            try:
                datetime.datetime.strptime(date, '%d-%m-%y')
                break
            except ValueError:
                print("Invalid date format. Use DD-MM-YY or Enter to keep current.")
    
    while True:
        time = input(f"Enter new time (HH:MM, or Enter to keep {meals[choice-1]['time']}): ")
        if not time:
            time = meals[choice-1]['time']
        else:
            try:
                datetime.datetime.strptime(time, '%H:%M')
                break
            except ValueError:
                print("Invalid time format. Use HH:MM or Enter to keep current.")
    
    while True:
        meal_type = input("Prepared meal (p), other (o), or Enter to keep current? ").lower()
        if not meal_type:
            meal = meals[choice-1]['meal']
            break
        if meal_type in ['p', 'o']:
            break
        print("Please enter 'p', 'o', or Enter.")
    
    if meal_type == 'p':
        if not prepared_meals:
            print("No prepared meals available. Keeping current meal.")
            meal = meals[choice-1]['meal']
        else:
            print("Prepared meals:")
            for i, meal in enumerate(prepared_meals, 1):
                print(f"{i}. {meal}")
            while True:
                choice_meal = input("Choose a meal (number, or 'q' to keep current): ")
                if choice_meal.lower() == 'q' or not choice_meal:
                    meal = meals[choice-1]['meal']
                    break
                try:
                    choice_meal = int(choice_meal)
                    if 1 <= choice_meal <= len(prepared_meals):
                        meal = prepared_meals[choice_meal - 1]
                        break
                    print(f"Please enter a number between 1 and {len(prepared_meals)} or 'q'.")
                except ValueError:
                    print("Please enter a valid number or 'q'.")
    elif meal_type == 'o':
        while True:
            meal = input("Enter new meal description (or Enter to keep current): ")
            if not meal:
                meal = meals[choice-1]['meal']
                break
            if meal.strip():
                break
            print("Meal description cannot be empty.")
    
    meals[choice-1] = {'date': date, 'time': time, 'meal': meal}
    save_meals()
    print("Meal updated successfully!")

# Main menu
def main():
    load_meals()
    while True:
        print("\nMenu: 1. Add meal, 2. View summary, 3. Exit, 4. Edit/Delete meal")
        choice = input("Choose: ")
        if choice == '1':
            add_meal()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            save_meals()
            print("Goodbye!")
            break
        elif choice == '4':
            edit_delete_meal()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()