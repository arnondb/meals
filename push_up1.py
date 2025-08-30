try:
	set_count=1
	push_ups_per_set=int(input('Enter number of push ups per set (1-50): '))
	if push_ups_per_set <= 0:
		raise ValueError ('Push ups per set must be non negative')
	if push_ups_per_set > 50:
		raise ValueError ('Number of push ups per set must be smaller then 51')
	full_set=0
	while True:
		try:
			push_ups_count = input(f"Enter push ups for set number {set_count}, when done print 'q': ")
	
			if push_ups_count == 'q':
					print(f'Number of sets is {set_count -1}')
					break
			push_ups_count = int(push_ups_count)
			if push_ups_count <= 0:
				raise ValueError ('Number of push ups must be positive')
			if push_ups_count >= push_ups_per_set:
				full_set +=1
			set_count += 1
		except ValueError as e:	
			if str(e).startswith ('Number of push ups'):
				print(f'Error: {e}')
			else:
				print("Error: Please enter a valid integer or 'q' for termination.")
	print(f'Number of full sets is {full_set}')	
except ValueError as e:
	if str(e).startswith ('Push ups'):
		print(f'Error: {e}')
	if str(e).startswith ('Number of push ups'):
		print(f'Error: {e}')	
	else:
		print("Error: Please enter a valid integer.")	