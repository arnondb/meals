try:
  total_minutes = int(input('Enter total minutes: '))
  if total_minutes < 0: 
    raise ValueError ('Total minutes must be non-negative')
  total_hours = total_minutes // 60
  remainder_minutes = total_minutes % 60
  print(f'{total_minutes} minutes is {total_hours} hours and {remainder_minutes} minutes')
except ValueError as e:
  if str(e).startswith("Total"):
    print(f"Error: {e}")
  else:
    print("Error: Please enter a valid integer.")
 