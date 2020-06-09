from math import sqrt
def isVowel(_char):
	return _char.lower() in 'aeiou'

def ex3(_String):
	return list(filter(isVowel, _String))

def filter_rule_ex4(dict_):
	for key in dict_:
		if len(str(key))>=3:
			return True
	return False

def ex4(*args, **kwargs):
	_dict=list(filter(lambda x: isinstance(x,dict), args))
	
	_list=list(filter(lambda x: isinstance(x,dict),[kwargs[k] for k in kwargs]))
	for el in _list:
		_dict.append(el)
	return list(filter(filter_rule_ex4,_dict))

def ex5(_list):
	return list(filter(lambda x: isinstance(x,int) or isinstance(x,float), _list))

def ex6(Point1, Point2):
	return tuple(map(lambda x,y: sqrt(pow(y[0]-x[0],2)+pow(y[1]-x[1],2)) ,Point1,Point2))

def ex7(_list):
	x = list(sorted(_list,key = lambda z: z%2))
	y = list(sorted(_list, key = lambda z: not z%2))
	return [(x[i],y[i]) for i in range(len(x)//2)]

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
	

print(ex3("Programming in Python is fun"))
print(ex4( {1: 2, 3: 4, 5: 6}, 

 {'a': 5, 'b': 7, 'c': 'e'}, 

 {2: 3}, 

 [1, 2, 3],

 {'abc': 4, 'def': 5},

 3764,

 dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

 test={1: 1, 'test': True}) )

print(ex5([1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]))
print(ex6([(2,-4),(4,3)],[(-2,3),(-3,-4)]))
print(ex7([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
print(ex8(
	filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],

    limit=2,

    offset=2
    )
)