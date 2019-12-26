# Custom Modules , Packages, Dynamic Code

https://sites.google.com/site/fiipythonprogramming/laboratories/lab-10

## Exercise 1

Write a program calc.py which takes 4 arguments from the command line.

The first and third arguments will be numbers (let's call them a and b ), the second one will be an operation: +,-,/,% and the forth an output file path.

When called the program will write the result of a op b at the standard output and at the end of the output file, prefixed with a human readable timestamp.

Example: 

python calc.py 1 + 1 a.txt 

will output 2019-12-01 14:00:00 1 + 1 = 2  ( at the standard output and at the end of the file)


## Exercise 2

Write a program called lottery.py which takes 3 arguments, all numbers and simulates a lottery extraction. 

The first argument, max_nr, is the maximum number in the lottery. Min is 1, max is 49.

The second argument, draw_size, represents how many numbers a player needs to choose. Min is 3, max is 10.

The third argument is the number of players. Min is 2, max is 10.

When called the program will first draw a winning combination of numbers ( draw_size )

and will randomly allocate draw_size numbers to each player.

At the end lottery.py will output, on separate lines, the winning combination and for each

player how many and the numbers they "guessed".


## Exercise 3

Write a program called matches.py that receives 3 parameters ( all file paths ) and generates a match schedule. 

The first and second parameter represent file paths to lists of team names ( one team name of each line).

The third parameter contains a list of timestamps on each line.

When called, matches.py will generate random pairs of teams ( from the two input files ) and for each pair of teams will randomly choose a match date.

At the end the program will output The date and time of the match and the teams playing:

2020-02-20 21:45:00 Team1 - Team2.

The program will generate only one match for a team and will use a match date only once.It will terminate when one of the 3 lists ( team list1, team list2, match date list) is empty.


## Exercise 4

Write a program called santa.py which prints to the standard output the time remaining ( in seconds ) until Santa Clauss will arrive. An arbitrary arrival time of 25 dec 2019 03:33:33 will be considered. For example if the time right now is 2019-01-01 00:00:00 the program will output 2086413


## Exercise 5

Write a script that writes the day of the week for the New Year Day, for the last x years (x is given as command line argument).


## Exercise 6

Write two functions to check if a number is prime, and check which of them is more time-efficient.


## Exercise 7

Write a program that will write the minutes run from the start, every x seconds, where x is random chosen at each iteraton (from the inteval [a, b] , where a, b are arguments). The program will run in an infinite loop.
