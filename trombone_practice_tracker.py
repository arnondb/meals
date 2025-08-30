try:	
	days_practiced = int(input('How many days did you practice trombone? '))
	total_minutes = 0
	if  days_practiced <= 0:
		raise ValueError ('Number of days must be positive')
	for i in range(1,days_practiced+1):
		max_tries = 3
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
					raise ValueError ('There are only 1440 minutes in a day')
				total_minutes += minutes_practiced
				break
			except ValueError as e:
				if str(e).startswith("Minutes") or str(e).startswith('There'):
					print(f"Error: {e}")
				else:
					print("Error: Please enter a valid integer.")
		
			finally:
				average_minutes = total_minutes / days_practiced
	print(f'Total minutes practiced: {total_minutes}')
	print(f'Average minutes per day: {average_minutes}') 
except ValueError as e:
	if str(e).startswith("Number"):	
		print(f"Error: {e}")	
	else:
		print("Error: Please enter a valid integer.")