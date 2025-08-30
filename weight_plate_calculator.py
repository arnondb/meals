#weight_plate_calculator
try:
  total_weight = int(input('Enter total weight lifted(kg, including 20-kg bar) '))
  if total_weight < 20:
    raise ValueError ('Weight must be higher then 20')
  plate_weight = int(input('Enter weight per plate (kg) '))
  if plate_weight <= 0:
    raise ValueError ('Plate weight must be positive')
  bar = 20
  plates_per_side = (total_weight - bar) // (2 * plate_weight)
  extra_kilograms = (total_weight - bar) % (2 * plate_weight)
  print(f'Plates per side {plates_per_side}')
  print(f'Extra kilograms {extra_kilograms}')
except ValueError as e:
  if str(e).startswith("Weight") or str(e).startswith("Plate"):
    print(f"Error: {e}")
  else:
    print("Error: Please enter a valid integer.")
