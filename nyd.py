_help='''Write a script that writes the day of the week for the New Year Day,
for the last x years (x is given as command line argument).'''

import sys,datetime

if len(sys.argv)!=2:
	print(_help)
	exit()
try:
	x=int(sys.argv[1])
except:
	exit()
today = datetime.date.today()
print( [ datetime.datetime(today.year-i-1,12,31)
	.strftime("%Y : %A")
	for i in range(x)
	] )