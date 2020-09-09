import math
def func(x):
    body = ( math.exp(4*(x**2)) + math.sin(x)**2 )/ ( (3*(x**2)) + (x**4) )
    solution = body**(1/2)
    return solution
    
if __name__ == '__main__':
    print(func(2))