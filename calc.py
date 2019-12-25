help = '''Write a program calc.py which takes 4 arguments from the command line.

The first and third arguments will be numbers (let's call them a and b ), the
second one will be an operation: +,-,/,% and the forth an output file path.

When called the program will write the result of a op b at the standard output
and at the end of the output file, prefixed with a human readable timestamp.

Example: 

python calc.py 1 + 1 a.txt 

will output 2019-12-01 14:00:00 1 + 1 = 2  ( at the standard output and at the
end of the file)
'''
import sys, datetime

if len(sys.argv)!=5: print(help)
try:
	a = int(sys.argv[1])
	b = int(sys.argv[3])
except:
	print("Check first and third argument.")
	# print(help)
op = sys.argv[2]
_operator={
	"+": lambda x,y: x+y,
	"-": lambda x,y: x-y,
	"/": lambda x,y: x/y,
	"%": lambda x,y: x%y
}
curr_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
	out = "{} {} {} {} = {}\n".format( curr_time
			, a
			, op
			, b
			, _operator[op](a,b)
			)
except:
	print("The second argument must be an operation: +,-,/,%")
	# print(help)
try:
	file = open(sys.argv[4], "a")
	file.write(out)
	file.close()
	print(out)
except:
	print("Error handling file.")