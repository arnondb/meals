#Even_or_Odd_evaluator
try:
  number = int(input("Please type an integer "))
  if number%2 == 0:
    if number >= 0:
      print(f'{number} is even')
    else:
      print(f'{number} is even (negative)')
  else:
    if number >= 0:
      print(f'{number} is odd')
    else:
      print(f'{number} is odd (negative)')
except ValueError:
   print('Please enter an integer')