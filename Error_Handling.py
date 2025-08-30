#Modulo_Division_Checker
try:
  numerator = int(input('Please type the numerator number: '))
  if numerator < 0:
    raise ValueError('Numerator must be positive')
  denominator = int(input('Please type the denominator number: '))
  if denominator < 0:
    raise ValueError('Denominator must be positive')
  quotient = numerator/denominator
  remainder = numerator%denominator
  print(f'Quotient:{quotient:.2f}') 
  print(f'Remainder:{remainder}')
except ValueError as e:
  if str(e).startswith("Numerator") or str(e).startswith("Denominator"):
    print(f"Error: {e}")
  else:
    print("Error: Please enter a valid integer.")
except ZeroDivisionError:
  print('Divission by 0 is not allowed')

    