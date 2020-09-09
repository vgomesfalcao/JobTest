def fibonacci(n1:int, n2:int, lis:list,iterations:int):
    if len(lis) == iterations:
        return 0
    else:
        lis.append(n1+n2)
        fibonacci(lis[-1], lis[-2], lis, iterations)
        
        
def init_fibo(n:int):
    fibo = []
    fibo.append(1)
    fibo.append(1)
    fibonacci(1, 1, fibo, n)
    return fibo