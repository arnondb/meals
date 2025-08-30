def prime_check(number):
    if number < 2:  # Prime numbers must be greater than 1
        print('No, it is not a prime number')
        return

    a = number ** (1/2)  
    b = round(a + 1)  

    for i in range(2, b):
        if number % i == 0:  # If divisible by any number, it's not prime
            print('No, it is not a prime number')
            return  # Stop checking once we confirm it's not prime

    print('Yes, it is a prime number')  # If no divisors were found, it's prime

# Get user input and check for prime
number = int(input('Please type a number and I will check if it is prime or not: '))
prime_check(number)
