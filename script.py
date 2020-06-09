from math import gcd
from functools import reduce

def ex1():
    try:
        numbersGCD = reduce(gcd
            , list(
                map(int
                    , input(
                        "GCD of the following numbers: "
                        ).split()
                )
            )
        )
        return numbersGCD
    except Exception as e:
        return e

def ex2():
    text = "Numarul de vocale este 9. tst"
    return reduce(lambda x,y: x+y, list(map(text.lower().count, "aeiou")))

def ex3():
    string2 = "Acesta este al doilea string. string. strig, stringg, stric"
    string1 = "string"
    return string2.count(string1)

def ex4():
    text = "UpperCamelCase"
    result = text[0].lower()
    text = text[1:];
    for c in text:
        if c == c.lower():
            result+=c
        else:
            result+=f"_{c.lower()}"
    return result

def ex5():
    matrix = [ ["f","i","r","s"]
              ,["n","_","l","t"]
              ,["o","b","a","_"]
              ,["h","t","y","p"]
            ]
    result = ""
    start_row = 0
    end_row = len(matrix[0])
    start_col = 0
    end_col = len(matrix)
    
    while start_row < end_row and start_col < end_col:
        for i in range(start_row, end_row):
            result+=matrix[start_col][i]
        for i in range(start_col, end_col):
            result+=matrix[i][end_row-1]
        break
    return result
print (ex1())
print (ex2())
print (ex3())
print (ex4())
print (ex5())
