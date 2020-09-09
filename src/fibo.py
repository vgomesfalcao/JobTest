def fibo(n1:int, n2:int, lis:list,iterations:int):
    if len(lis) == iterations:
        return 0
    else:
        lis.append(n1+n2)
        fibo(lis[-1], lis[-2], lis, iterations)
        
        
def fibonacci(n:int):
    fibo_list = []
    fibo_list.append(1)
    fibo_list.append(1)
    fibo(1, 1, fibo_list, n)
    return fibo_list