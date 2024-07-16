hour = 0
mins = 1
dura = 2939
# find a total of all minutes
total_mins = mins + dura
# find a number of hours hidden in minutes and update the hour
hour = hour + total_mins//60
# correct minutes to fall in the (0..59) range
mins = total_mins%60
# correct hours to fall in the (0..23) range
hour = hour%24
print(hour, mins)
# print(hour, ":", mins, sep='')

