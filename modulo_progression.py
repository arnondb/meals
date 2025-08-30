# While True block:
try:
	max_tries = 3
	current_try = 0
	while True:
		current_try += 1
		if current_try >= max_tries:
			print("Maximum attempts reached. Exiting loop")
		try:
			n = int(input('Type the number "n" that you want to check. The range is 1 - 100: '))
			if n < 1 or n > 100 :
				raise ValueError("Allowed range is 1-100")
			else:
				print('Please enter a valid integer')
			divisor = int(input('Type a divisor between 1 and n: '))
			if divisor < 1 or divisor > n:
				raise ValueError("Allowed divisor range is 1-n")
		except ValueError as e:
			if str(e).startswith("Allowed"):
				print(f"Error {e}")
			else:
				print("Please enter a valid integer")
		break
	for i in range(1,n+1):
		if i % divisor == 0:
			print(f"{i} is a diviser")
		else:
			print(i)
# End primary while True
except ValueError as e:
	if str(e).startswith("Maximum"):
		print(f"Error {e}")
	else:
		print("Please enter a valid integer")
