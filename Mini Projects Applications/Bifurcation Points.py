import numpy as np

r_values = np.linspace(2.5, 4.0, 10000)
iterations = 1000
last = 100

def find_bifurcation_points(x0=0.1):
    bifurcation_points = []
    last_r = None
    last_period = None
    for r in r_values:
        trajectory = []
        x = x0  # Start with the user-defined initial value
        for i in range(iterations):
            x = r * x * (1 - x)
            if i >= (iterations - last):
                trajectory.append(x)
        unique_points = np.unique(np.round(trajectory, decimals=4))
        period = len(unique_points)

        if period in [2, 4, 8, 16] and (last_r is None or abs(r - last_r) > 0.1) and (last_period is None or period > last_period):
            bifurcation_points.append((r, period))
            last_r = r
            last_period = period
    return bifurcation_points

bifurcation_points = find_bifurcation_points()
for r, period in bifurcation_points:
    print(f"Bifurcation at r = {r:.4f} with period {period}")