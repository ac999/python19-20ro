'''
Write a program called santa.py which prints to the standard output the time
remaining ( in seconds ) until Santa Clauss will arrive. An arbitrary arrival
time of 25 dec 2019 03:33:33 will be considered.
For example if the time right now is 2019-01-01 00:00:00 the program will
output 2086413.
'''

import datetime

time_remaining=datetime.datetime(2020,12,25,3,33,33)-datetime.datetime.now()

print("Santa will come in {} seconds.".format(str(
	time_remaining.total_seconds()
	).split(".")[0])
)