from math import sqrt
def process_item(x):
    n = x+1
    prime = False
    while(prime==False):
        prime = True
        for i in range(2, int(sqrt(x)+1)):
            if n%i == 0:
                prime = False
                break
        n += 1
    return n-1

if __name__ == "__main__":
    print(process_item(int(input())))
