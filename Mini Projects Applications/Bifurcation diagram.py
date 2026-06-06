import numpy as np
import matplotlib.pyplot as plt

r_values = np.linspace(2.5, 4.0, 10000)
iterations = 1000
last = 100

x = 0.5
bifurcation_x = []
bifurcation_r = []

for r in r_values:
    trajectory = []
    for i in range(iterations):
        x = r * x * (1 - x)
        if i >= (iterations - last):
            trajectory.append(x)
    bifurcation_r.extend([r] * len(trajectory))
    bifurcation_x.extend(trajectory)

plt.figure(figsize=(10, 6))
plt.scatter(bifurcation_r, bifurcation_x, s=0.1, color="black")
plt.title("Bifurcation Diagram of the Logistic Map")
plt.xlabel("r")
plt.ylabel("x")
plt.grid(alpha=0.3)
plt.show()