_help='''Write two functions to check if a number is prime, and check which of
them is more time-efficient.'''

import sys
from datetime import datetime
from math import sqrt

# https://beginnersbook.com/2018/01/python-program-check-prime-or-not/
def function1(x):
	if x > 1:
		for i in range(2,x):
			if(x%i) == 0:
				print("function1: {} is not prime".format(x) )
				break
		else:
			print("function1: {} is prime.".format(x))
	else:
		print("function1: {} is not prime".format(x) )



def function2(x):
	if x > 1:
		for i in range(2,int(sqrt(x))+1):
			if(x%i) == 0:
				print("function2: {} is not prime".format(x) )
				break
		else:
			print("function2: {} is prime.".format(x))
	else:
		print("function2: {} is not prime".format(x) )

if len(sys.argv)!=2:
	print(_help)
	print("\nMust give 1 number as parameter.")
try:
	number=int(sys.argv[1])
except:
	print(_help)
	print("\nMust give 1 number as parameter.")
	exit()

f1s = datetime.now()
function1(number)
f1s = (f1s-datetime.now()).total_seconds()

f2s=datetime.now()
function2(number)
f2s = (f2s-datetime.now()).total_seconds()

print("function1 time: {}\nfunction2 time: {}"
	.format(f1s,f2s)
	)
if (f1s-f2s>0):
	result="function1"
else:
	if(f1s==f2s):
		result="both"
	else:
		result="function2."
print("Winner is {}".format(result))