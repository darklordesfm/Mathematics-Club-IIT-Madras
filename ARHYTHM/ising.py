import numpy as np
import matplotlib.pyplot as plt

T_val = [1.1, 2.6, 4.9]
N = 2**12
p = 32
def initial_array(p):
    return np.random.choice([-1, 1], size=(p, p)).astype(np.int8)

def delta_energy(lattice, i, j):
    spin = lattice[i, j]
    neighbors = lattice[(i+1)%p, j] + lattice[i, (j+1)%p] + lattice[(i-1)%p, j] + lattice[i, (j-1)%p]
    return 2 * spin * neighbors

def metropolis_step(lattice, T):
    for _ in range(p * p):
        i, j = np.random.randint(0, p, size=2)
        dE = delta_energy(lattice, i, j)
        if dE <= 0 or np.random.rand() < np.exp(-dE / T):   lattice[i, j] *= -1

for T in T_val:
    lattice = initial_array(p)
    for _ in range(N):      metropolis_step(lattice, T)

    plt.figure()
    plt.imshow(lattice, cmap='binary', interpolation='nearest')
    plt.title(f"Ising Model at T = {T}")
    plt.colorbar(label="Spin")
    plt.savefig(f"ising_T_{T}.png", dpi=300)
    plt.show()
    plt.close()

del lattice