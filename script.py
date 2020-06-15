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

# ex. 5
def ex5(_list):
	return list(filter(lambda x: isinstance(x,int) or isinstance(x, float), _list))

print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))

# ex. 6

def line(a, b):
	m = (a[1]-b[1])/(a[0]-b[0])
	return (a[0],a[1],m)

def ex6a(_list1, _list2):
	return list(map(lambda x,y: line(x,y), _list1, _list2))

def ex6b(_list1, _list2):
	return [line(element[0], element[1]) for element in zip(_list1, _list2)]

print(ex6a([(1,2),(3,4),(5,6)], [(3,-10),(-9,10),(20,10)]))
print(ex6b([(1,2),(3,4),(5,6)], [(3,-10),(-9,10),(20,10)]))

# ex. 7

def ex7(integers):
	return [element for element in zip(sorted(integers, key = lambda x: x%2!=0)
	, sorted(integers, key = lambda x: x%2==0))][:len(integers)//2]

print( ex7([1, 3, 5, 2, 8, 7, 4, 10, 9, 2, 15, 12]) )

# ex. 8

def sum_digits(x):
	return sum(map(int, str(x)))

def ex8(**kwargs):
		_list=[0,1,1]
		for i in range(3,1000):
				_list.append(_list[i-1]+_list[i-2])
		_filters = kwargs.get("filters",None)
		_limit = kwargs.get("limit",None)
		_offset = kwargs.get("offset",None)
		if _filters!=None:
				for _filter in _filters:
						_list=list(filter(_filter, _list))
		if isinstance(_offset, int):
				if _offset>=0:
						_list=_list[_offset:]
		if isinstance(_limit, int):
				if _limit>=0:
						_list=_list[:_limit]

		return _list

print(ex8(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20]
	,limit=2
	,offset=2)
	)

# ex. 9

from functools import reduce

def multiply_by_two(x):

    return x * 2


def add_numbers(a, b):

    return a + b

def print_arguments(function):
	def new_function(*args, **kwargs):
		print(f"Arguments are: {args}, {kwargs}")
		return function(*args, **kwargs)
	return new_function

augmented_multiply_by_two = print_arguments(multiply_by_two)
x = augmented_multiply_by_two(10)
print(x)

augmented_add_numbers = print_arguments(add_numbers)
x = augmented_add_numbers(3, 4)
print(x)

def multiply_by_three(x):

    return x * 3

def multiply_output(function):
	def new_function(*args, **kwargs):
		return 2*function(*args, **kwargs)
	return new_function

augmented_multiply_by_three = multiply_output(multiply_by_three)

x = augmented_multiply_by_three(10)

print(x)

def add_numbers(a, b):

    return a + b

def augment_function(function, decorators):
	def new_function(*args, **kwargs):
		# result = function
		# for f in decorators:
		# 	result = f(result)
		# return result(*args, **kwargs)
		return reduce(lambda f1, f2: f2(f1), [function]+decorators)(*args, **kwargs)

	return new_function

decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])

x = decorated_function(3, 4)

print(x)
