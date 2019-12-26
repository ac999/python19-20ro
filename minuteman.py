_help='''Write a program that will write the minutes run from the start, every
x seconds, where x is random chosen at each iteraton (from the inteval [a, b] ,
where a, b are arguments). The program will run in an infinite loop.'''

def helper():
	print(_help)
	exit()

import sys,random,time
from datetime import datetime as dttm

def choose(a,b):
	return random.randint(a,b)

def getMinute(start):
	return int((start-dttm.now()).total_seconds()/60)

if len(sys.argv)!=3:
	helper()
try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
except:
	helper()

start = dttm.now()

while(1):
	x=choose(a,b)
	time.sleep(x)
	print("{} seconds passed: current minute is {}".format(x,getMinute(start)))