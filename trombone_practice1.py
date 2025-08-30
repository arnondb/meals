try:
	total = 0	
	divide = 0
	days_practiced = int(input('How many days did you practice trombone? Please enter a number between 1 and 25 '))
	if  days_practiced <= 0:
		raise ValueError ('Number of days must be positive')
	if days_practiced > 25:
		raise ValueError ('Too many days, please enter a number between 1 to 25')
	for i in range(1,days_practiced+1):
		max_tries = 30
		current_try = 0
		while True:
			current_try += 1
			if current_try >= max_tries:
					print("Maximum attempts reached. Exiting loop")
					break
			try:
				minutes_practiced = int(input(f'Enter practice minutes for day {i}: '))
				if minutes_practiced < 0: 
					raise ValueError ('Minutes must be non-negative')
				if minutes_practiced > 1440:
					raise ValueError ('There are only 1440 minutes in a day, please enter a number smaller then 1441')
				total += minutes_practiced 
				if minutes_practiced % 5 == 0:
					divide += 1	
				break
			except ValueError as e:
				if str(e).startswith("Minutes"):
					print(f'Error: {e}')
				elif str(e).startswith("There"):
					print(f'Error: {e}')
				else:
					print('Please enter a valid integer')
	average_minutes = total / days_practiced
	print(f'Average minutes per day {average_minutes}')
	print(f'Total practice minutes: {total}')
	print(f'Days with minutes divisible by 5: {divide}')
except ValueError as e:
	if str(e).startswith("Number"):	
		print(f"Error: {e}")
	elif str(e).startswith("Too"):
		print(f"Error: {e}")
	else:
		print("Error: Please enter a valid integer.")
