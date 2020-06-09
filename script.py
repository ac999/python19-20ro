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

def findDiff(d1, d2, l=[]):
	for k in d1:
		if (k not in d2):
			l.append(f"{k} not found in one of the dictionaries")
		else:
			if type(d1[k]) is dict:
				findDiff(d1[k],d2[k], l)
			else:
				if d1[k] != d2[k]:
					l.append(f"{d1[k]} != {d2[k]}")
	return l

def ex3(dict1, dict2):
	return findDiff(dict1,dict2) and findDiff(dict2, dict1)

def build_xml_element(tag, content, **kwargs):
	result = f"<{tag}"
	if len(kwargs) == 0:
		result += f">{content}</{tag}>"
		return result
	for key, value in kwargs.items():
		result += f" {key}=\\\"{value}\\\""
	result += f">{content}</{tag}>"
	return result

def ex4():
	return build_xml_element ("a", "Hello there", href =" http://python.org "
	, _class =" my-link ")

def validate_dict(rules, dictionary):
	for key in dictionary.keys():
		if key not in [element[0] for element in rules]:
			return False
	for rule in rules:
		if rule[0] not in dictionary.keys():
			return False
		string = dictionary.get(rule[0]).strip().split()
		if len(string)==1:
			if rule[1]!=rule[2]!=rule[3]:
				return False
		if rule[1] != string[0]:
			return False
		if rule[2] == string[0] or rule[2] == string[len(string)-1]:
			return False
		if rule[3] != string[len(string)-1]:
			return False
		return True



def ex5():
	rules = {("key1", "", "inside", ""), ("key3", "this", "not", "valid")}
	dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
	return validate_dict(rules, dictionary)

def ex6(_set):
	return(len(_set), 0)

def ex7(*sets):
	_dict = dict()
	for set1, set2 in zip(sets[0::2],sets[1::2]):
		_dict[f"{set1} | {set2}"] = set1 | set2
		_dict[f"{set1} & {set2}"] = set1 & set2
		_dict[(f"{set1} - {set2}")] = set1 - set2
		_dict[(f"{set2} - {set1}")] = set2 - set1
	return _dict


print(ex1([1,2,3,4],[3,4,5,6]))
print(ex2("Ana are mere."))

d1= {'a':{'b':{'cs':10},'d':{'cs':20}}}
d2= {'a':{'b':{'cs':30} ,'d':{'cs':20}},'n_e_w_a':{'q':{'cs':50}}}
print (ex3(d1,d2))

print(ex4())
print(ex5())
print(ex6({1,1,2,2,3,3,4,4,5,5,6,6,7,7}))
print(ex7({1,2}, {2,3}))
