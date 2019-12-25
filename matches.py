help='''Write a program called matches.py that receives 3 parameters ( all file
paths ) and generates a match schedule. 

The first and second parameter represent file paths to lists of team names
( one team name of each line).

The third parameter contains a list of timestamps on each line.

When called, matches.py will generate random pairs of teams ( from the two
input files ) and for each pair of teams will randomly choose a match date.

At the end the program will output The date and time of the match and the
teams playing:

2020-02-20 21:45:00 Team1 - Team2.

The program will generate only one match for a team and will use a match date
only once.It will terminate when one of the 3 lists ( team list1, team list2,
match date list) is empty.
'''

import sys,random

if len(sys.argv)!=4:
	print(help)
	exit()
try:
	t1f = open(sys.argv[1],"r")
except:
	exit()
try:
	t2f = open(sys.argv[2],"r")
except:
	exit()
try:
	df = open(sys.argv[3],"r")
except:
	exit()

team1= t1f.read().splitlines()
team2= t2f.read().splitlines()
date = df.read().splitlines()
random.shuffle(team1)
random.shuffle(team2)

t1f.close()
t2f.close()
df.close()

group = list(zip(team1, team2))

for i in range(min(len(team1),len(team2),len(date))):
	print("{} {} - {}.".format(date[i],group[i][0],group[i][1]))