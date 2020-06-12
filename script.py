# ex. 2
def ex2(*arguments):
	return sum(arguments)

ex2a = lambda *arguments: sum(arguments)

print(ex2(1, 2, 3, 4, 5))
print(ex2a(1, 2, 3, 4, 5))

# ex. 3
def ex3a(string):
	return list(filter(lambda x: x in "aeiou", string))

ex3b = lambda string: list(filter(lambda x: x in "aeiou", string))

def ex3c(string):
	return [vowel for vowel in filter(lambda x: x in "aeiou", string)]

print(ex3a("Programming in Python is fun"))
print(ex3b("Programming in Python is fun"))
print(ex3c("Programming in Python is fun"))

# ex. 4

def process_dict(dictionary):
	if len(dictionary.keys()) < 2:
		return False
	if len(list(filter(lambda x: isinstance(x, str) and len(x)>2, dictionary.keys()))) == 0:
		return False
	return True

def ex4(*args, **kwargs):
	result = []
	for arg in args:
		if isinstance(arg, dict):
			if process_dict(arg):
				result.append(arg)
	for arg in kwargs.items():
		if isinstance(arg[1], dict):
			if process_dict(arg[1]):
				result.append(arg[1])
	return result

print(ex4( {1: 2, 3: 4, 5: 6},

 {'a': 5, 'b': 7, 'c': 'e'},

 {2: 3},

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}))
