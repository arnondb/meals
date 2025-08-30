#drill 1
yesterday_minutes = input('How many minutes did you practice the trombone yesterday? ')
today_minutes = input('How many minutes did you practice the trombone today? ')
a = int(yesterday_minutes)
b = int(today_minutes)
total_minutes = a + b
print(f"Your total trombone practice time for today and yesterday is {total_minutes} ")
#drill 2
push_ups_done = input('How many push ups did you already do? ')
push_ups_goal = input('How many push ups is your goal? ')
push_ups_done = int(push_ups_done)
push_ups_goal = int(push_ups_goal)
push_ups_needed = push_ups_goal - push_ups_done
print(f'Great! You have only {push_ups_needed} push ups more to go!')
#drill 3
race1_laps = input('How many laps did you bike in the first race? ')
race2_laps = input('How many laps did you bike in the second race? ')
race1_laps = int(race1_laps)
race2_laps = int(race2_laps)
average_laps = (race1_laps + race2_laps)/2
print(f'Your average laps in a race is {average_laps}')
#drill 4
reps_per_note = input('How many times did you repeat each note? ')
num_notes = input('How many notes are in the song? ')
reps_per_note = int(reps_per_note)
num_notes = int(num_notes)
total_reps = reps_per_note * num_notes
print(f'The total number of notes played is {total_reps}')
#drill 5
total_reps = input('How many reps did you do in total? ')
num_sets = input('How many sets did you do? ')
total_reps = int(total_reps)
num_sets = int(num_sets)
reps_per_set = total_reps/num_sets
print(f'You did {reps_per_set} reps per set!')
