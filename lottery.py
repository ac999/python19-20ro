help='''Write a program called lottery.py which takes 3 arguments, all numbers
and simulates a lottery extraction. 

The first argument, max_nr, is the maximum number in the lottery. Min is 1,
max is 49.

The second argument, draw_size, represents how many numbers a player needs to
choose. Min is 3, max is 10.

The third argument is the number of players. Min is 2, max is 10.

When called the program will first draw a winning combination of numbers
( draw_size ) and will randomly allocate draw_size numbers to each player.

At the end lottery.py will output, on separate lines, the winning combination
and for each player how many and the numbers they "guessed".
'''

import sys, random

help1='''The first argument, max_nr, is the maximum number in the lottery.
		Min is 1,max is 49.'''

help2='''The second argument, draw_size, represents how many numbers a player
needs to choose. Min is 3, max is 10.'''

help3="The third argument is the number of players. Min is 2, max is 10."

if len(sys.argv)!=4:
	print(help)
	exit()
try:
	max_nr = int(sys.argv[1])
except:
	print(help1)
	exit()
if max_nr<1 or max_nr>49:
	print(help1)
	exit()

try:
	draw_size = int(sys.argv[2])
except:
	print(help2)
	exit()
if draw_size<3 or draw_size>10:
	print(help2)
	exi()
try:
	no_players = int(sys.argv[3])
except:
	print(help3)
	exit()
if no_players<2 or no_players>10:
	print(help3)
	exit()

win = set(random.sample(range(1,max_nr),draw_size))
print("Winning combination: {}".format(win))
player=[set(random.sample(range(1,max_nr),draw_size))
for p in range(no_players)]
for i in range(no_players):
	print("\nPlayer{}'s' combination: {}\n{} numbers match."
		.format(i
			, player[i]
			, len(win.intersection(player[i]))
			)
		)
