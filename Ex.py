def division(number):
    try: 
        outcome = 100 / number  # Perform the division
    except ZeroDivisionError:
        print('You cannot divide by 0!')
    else:
        print(f"The result is: {outcome}")

# Wrap input handling in a try-except block for ValueError
try:
    number = float(input('Please type a number: '))
    division(number)
except ValueError:
    print('Invalid input! Please type a number.')