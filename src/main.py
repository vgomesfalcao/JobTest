from fibo import fibonacci

x = 0.3
y = 0.8
n = 8

fibo_sequence = fibonacci(n)

i1 = y - x
i2 = (fibo_sequence[-2]/fibo_sequence[-1]) * i1
u = x + i2
v = y - i2