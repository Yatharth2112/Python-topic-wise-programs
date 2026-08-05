from time import time

def timer(func):
    def wrapper(n):
        t1 = time()
        func(n)
        t2 = time()
        print("Time taken by function is", t2 - t1)
    return wrapper    

@timer
def sum_1million(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1
    return sum

a = sum_1million(1000000)    
