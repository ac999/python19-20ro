from math import gcd,sqrt
from random import uniform
from itertools import combinations
def isPrime(x):
	if x>1:
		for i in range(2,int(sqrt(x))+1):
			if (x%i)==0:
				return False
				break
		return True
	return False

def calc(x,y,c):
	a = int(uniform(0,100))
	b=(0-c-a*x)/y

	return (a,b,c)


def fib(n):
	n=int(n)
	x=[1,1,2]
	for i in range(n-3):
		x.append(x[-1]+x[-2])
	return x[n-1]

def ex2(nrlist):
	return list(filter(lambda element: isPrime(element),nrlist))

def ex3(listaPuncte):
	c = [i+1 for i in range(-len(listaPuncte)//2,len(listaPuncte)//2)]
	x,y=zip(*listaPuncte)
	return list(map(calc, x, y, c))

def ex4(listaA, listaB):
	U = list(set(listaA)
		| set(listaB))
	V= list(filter(lambda x: list(listaA+listaB).count(x)>1, list(set(listaA+listaB))))
	AmB = list(filter(lambda y: listaB.count(y)==0, listaA))
	BmA = list(filter(lambda y: listaA.count(y)==0, listaB))
	return (U, V, AmB, BmA)

def ex5(lista, r):
	return list(combinations(lista,r))

def ex6(*lists, x):
	_new = []
	ap={}
	for i in range(len(lists)):
		for j in range(len(lists[i])):
			ap[lists[i][j]]=ap.get(lists[i][j],0)+1
	for each in ap:
		if ap[each] == x:
			_new.append(each)
	return _new

def ex7(x=1, *strings, flag=True):
	_return=[]
	if flag==True:
		for string in strings:
			_return.append(list(filter(lambda y: ord(y)%x==0, string)))
	else:
		for string in strings:
			_return.append(list(filter(lambda y: ord(y)%x!=0, string)))
	return tuple(_return)

def ex8(*lists):
	return list(map(lambda x: list(zip(*x)), lists))[0]

def ex9(list_):
	list_.sort(key = lambda x: x[1][2])
	return list_

print(fib(5))
print(ex2([1,2,3,4,5,6,7,8,9]))
print(ex3([(3,4),(-10,11),(25,-100)]))
print(ex4([1,2,3,4,5,6],[4,5,6,7,8,9]))
print(ex5([1,2,3,4],3))
print(ex6([1,2,3],[2,3,4],[4,5,6],[4,1,"test"], x=2))
print(ex7(2, "test", "hello", "lab0002", flag=False))
print(ex8([[1,2,3],[5,6,7],["a","b","c"]]))
print(ex9([('abc','bcd'),('abc','zza')]))