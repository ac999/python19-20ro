# Regular expressions

https://sites.google.com/site/fiipythonprogramming/laboratories/lab-11

# Exercise 1
Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of alpha-numeric characters.

# Exercise 2
Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns those long-length x substrings that match the regular expression.

# Exercise 3
Write a function that receives as a parameter a string of text characters and a list of regular expressions and returns a list of strings that match on at least one regular expression given as a parameter.

# Exercise 4
Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those elements that have as attributes all the keys in the dictionary and values ​​the corresponding values. For example, the elements that have the attributes: class = "url" and name = "url", "name": "url-form", " "url-form" and date-id = "item".

# Exercise 5
Write another variant of the function from the previous exercise that returns those elements that have at least one attribute that corresponds to a key-value pair in the dictionary.

# Exercise 6
Write a function that, for a text given as a parameter, censures words that begin and end with voices. Censorship means replacing characters from odd positions with *.

# Exercise 7
Verify using a regular expression whether a string is a valid CNP.

# Exercise 8
Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression given as a parameter or contains a string that matches the same expression. Files that satisfy both conditions will be prefixed with ">>"

# Exercise 9
Write a function that receives a directory as argument and returns a list of dictionaries with data about all the files in that directory. For each file, the following information will be retrieved: file_name, md5 hash of file, sha256 hash of file, size_file (in bytes), time when the file was created (human-readable) and the absolute path to the file.

# Exercise 10
Write a function that finds all the duplicate files in a directory given as an argument. The function will return a list with the duplicate files and a number representing the run time.
