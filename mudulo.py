# Drill 1
total_minutes = int(input('How many minutes did you play the trombone last week? '))
num_days = int(input('Over how many days? '))
avg_minutes = total_minutes/num_days
reminder_mins = total_minutes%num_days
print(f'You practices an average of {avg_minutes} minutes per day')
print(f'You have {reminder_mins} not evenly divided')
# Drill 2
total_push_ups = int(input('How many push ups did you do in total? '))
push_ups_per_set = int(input('How many push ups in a set? '))
full_sets = total_push_ups//push_ups_per_set
extra_push_ups = total_push_ups%push_ups_per_set
print(f'You completed {full_sets} full sets')
print(f'You have {extra_push_ups} extra push-ups')
# Drill 3
total_laps = int(input('How many laps did you bike in total? '))
num_races = int(input('Over how many races? '))
average_laps = total_laps/num_races
rem_laps = total_laps%num_races
bonus_laps = total_laps+5
print(f'You biked an average of {average_laps} laps per race')
print(f'You have {rem_laps} not evenly divided')
print(f'With a 5-lap bonus, your total is {bonus_laps} laps!')
# Drill 4
total_reps = int(input('How many note repititions did you do? '))
reps_per_session = int(input('How many repititions per session? '))
full_sessions = total_reps//reps_per_session
extra_reps = total_reps%reps_per_session
double_sessions = full_sessions*2
print(f'You completed {full_sessions} full sessions')
print(f'You have {extra_reps} extra repititions')
print(f'With double credit, you earned {double_sessions} session points!')
# Drill 5 
total_kgs = int(input('How many total Kilograms did you lift? '))
kgs_per_plate = int(input('How many kilograms per plate? '))
plates_per_side = (total_kgs//kgs_per_plate)/2
extra_kgs = total_kgs%(kgs_per_plate*plates_per_side*2)
weight_without_bar = total_kgs-20
print(f'You used {plates_per_side} plates per side')
print(f'you have {extra_kgs} extra Kilograms')
print(f'Without the 20-Kgs bar, you lifetd {weight_without_bar} kilograms!')
