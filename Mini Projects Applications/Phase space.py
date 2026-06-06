import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2],[2,1]])

x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X,Y = np.meshgrid(x, y)

X_der = A[0,0] * X + A[0,1] * Y
Y_der = A[1,0] * X + A[1,1] * Y

plt.quiver(X, Y, X_der, Y_der, color='b')
plt.title("Phase Space")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()