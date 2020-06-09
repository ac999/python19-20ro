def ex1(A, B):
	A=set(A)
	B=set(B)
	_set=list()
	_set.append(A | B)
	_set.append(A& B)
	_set.append(A-B)
	_set.append(B-A)
	return set(map(frozenset, _set))

def ex2(_String):
	_dict=dict()
	for l in _String:
		_dict[l]=_dict.get(l,0)+1
	return _dict

def findDiff(d1, d2):
	for k in d1:
		if (k not in d2):
			return False
		else:
			if type(d1[k]) is dict:
				findDiff(d1[k],d2[k])
			else:
				if d1[k] != d2[k]:
					return False
	return True

def ex3(dict1, dict2):
	return findDiff(dict1,dict2) and findDiff(dict2, dict1)


print(ex1([1,2,3,4],[3,4,5,6]))
print(ex2("Ana are mere."))

d1= {'a':{'b':{'cs':10},'d':{'cs':20}}}
d2= {'a':{'b':{'cs':30} ,'d':{'cs':20}},'n_e_w_a':{'q':{'cs':50}}}
print (ex3(d1,d2))
