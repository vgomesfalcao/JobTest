from fibo import fibonacci
from functions import func

#x = 0.3
#y = 0.8
#n = 8
x = input('Type value of x: ')
y = input('Type value of y: ')
n = input('Type value of n: ')

fibo_sequence = fibonacci(n)

i = [y - x ,]
i.append((fibo_sequence[-2]/fibo_sequence[-1]) * i[0])

print(i)
print(i[1])
u = x + i[1]
v = y - i[1]

a = func(u)
b = func(v)


k = 1


while(True):
    
    i.append( (fibo_sequence[n-k-1]*i[-1])/fibo_sequence[n-k] )
    
    if (b>=a):
        x = v
        v = u
        u = x + i[-1]
        b = a
        a = func(u)
    else:
        y = u
        u = v
        v = y - i[-1]
        a = b 
        b = func(v)
        
    fu = func(u)
    fv = func(v)
    print('\033[31m'+ f'x = {x}'+' \033[0;0m',
            '\033[32m' + f'y = {y}' + ' \033[0;0m',
            '\033[33m' + f'u = {u}' + ' \033[0;0m',
            '\033[34m' + f'u = {u}' + ' \033[0;0m', 
            '\033[35m' + f'v = {v}' + ' \033[0;0m',
            '\033[41m' + f'k = {k}' + ' \033[0;0m',
            '\033[42m' + f'f(u) = {fu}' + ' \033[0;0m',
            '\033[44m' + f'f(v) = {fv}' + ' \033[0;0m')
    

    
    if ((k == n-2)and (u > v)):
        xs = u
        fs = func(xs)
        print( '\033[32m' + f'xs = {xs}' + ' \033[0;0m', '\033[34m' + f'fs = {fs}' + ' \033[0;0m')
        break
    
    k += 1

