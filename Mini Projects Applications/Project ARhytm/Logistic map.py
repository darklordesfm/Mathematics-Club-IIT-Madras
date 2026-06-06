import matplotlib.pyplot as plt

def funct(r,x):
    return r*x*(1-x)

def storing(x0,r,n):
    map = [x0]
    for i in range(n-1):
        x_next = funct(r,map[-1])
        map.append(x_next)
    return map

def plot(map, r):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(map)), map, marker='o', linestyle='-')
    plt.title(f"Logistic Map Sequence for r = {r} , x0 = {x0}")
    plt.xlabel("n (Iterations)")
    plt.ylabel("x_n (Population)")
    plt.grid()
    plt.show()

r = 0.5
x0 = 0.75
n = 100
map = storing(x0, r, n)
plot(map,r)