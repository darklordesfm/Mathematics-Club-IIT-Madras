import numpy as np

def funct(r,x):
    return r*x*(1-x)

def storing(x0,r,n):
    map = [x0]
    for i in range(n-1):
        x_next = funct(r,map[-1])
        map.append(x_next)
    return map

def find_limiting_values(x0, r, n, transient=100):
    map = storing(x0, r, n)
    stabilized_part = map[transient:]
    limiting_values = np.unique(np.round(stabilized_part, decimals=6))
    return limiting_values

r = 3.56
x0 = 0.01
n = 500
transient = 100

limiting_values = find_limiting_values(x0, r, n, transient)
print(len(limiting_values))