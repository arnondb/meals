def prime_check(number):
  a = number ** (1/2)
  b = round(a+1)
  for i in range(2, b):
    if number % i == 0:
      print('No, it is not a prime number')
    else:
      print('Yes, it is a prime number')
number = int(input('Please type a number and I will check if it is a prime or not '))
prime_check(number)
