def ex1(_list):
	return list(sorted(_list, key = lambda x: x[1]>x[0]))

def ex2(_list, first_name):
	return first_name in map(lambda x: x[1], _list)

def ex3(operator, a, b):

	operators = {    

    "+": lambda a, b: a + b,     

    "*": lambda a, b: a * b,

    "/": lambda a, b: a / b,

    "%": lambda a, b: a % b

	}

	return operators[operator](a,b)

def ex4(function, *a, **k):
	functions = {

    "print_all": lambda *a, **k: print(a, k),

    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),

    "print_only_args": lambda *a, **k: print(a),

    "print_only_kwargs": lambda *a, **k: print(k)

	}

	functions[function](a,k)

def ex5(*args):
	_ndict={}
	for _dict in args:
		for i in _dict:
			if _ndict.get(i,None) == None:
				_ndict[i]=_dict[i]
			else:
				if isinstance(_ndict.get(i),list):
					_ndict[i].append(_dict[i])
				else:
					_ndict[i]=[_ndict[i],_dict[i]]
	return _ndict


def ex6(_dict, path="-"):
	for key in _dict:
		if not isinstance(_dict.get(key),dict):
			print (str(path)[3:]+" - "+str(key)+" - "+str(_dict.get(key)))
		else:
			ex6(_dict.get(key),path+" - "+key)




print(ex1([("Lazar", "Ion"), ("Mincu","Maria")]))
print(ex2([("Lazar", "Ion"), ("Mincu","Maria")], "Ion"))
print(ex3("+",5,10))
ex4("print_all", "x", 2, mama="ta", tata="tau")
print(ex5({1: 10, 2: 20}, {3:30, 4:40, 5:50}, {6:60, 1:70, 4:80}))
ex6({

   'a': 1,

   'b':

   {

       'c': 3,

       'd':

       {

           'e': 5,

           'f': 6

       }

   }

})