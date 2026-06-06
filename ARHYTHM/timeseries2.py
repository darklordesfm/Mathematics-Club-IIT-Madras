import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label

data = np.load("C:/Users/Saravanan/Downloads/dataset_week_2_modified.npy")
data = data.squeeze()

num_frames = data.shape[0]
N = data.shape[1]
window_size = 50

M_list = []
sigma2_M_list = []
Rmax_list = []
R_mean_list = []

for t in range(num_frames):
    frame = data[t]  # 32x32 lattice at time t
    # 1. Magnetization (M)
    M_t = np.sum(frame) / (N ** 2)
    M_list.append(M_t)
    # 2. Magnetization Variance (σ²_M) using a sliding window
    if t >= window_size // 2 and t < num_frames - window_size // 2:
        window = M_list[t - window_size // 2:t + window_size // 2]
        sigma2_M_list.append(np.var(window))
    else:
        sigma2_M_list.append(0)  # Padding at start and end
    # 3. Cluster Analysis
    labeled_array, num_clusters = label(frame)  # Label connected clusters
    cluster_sizes = np.bincount(labeled_array.ravel())[1:]  # Ignore background count

    if len(cluster_sizes) > 0:
        Rmax_list.append(np.max(cluster_sizes) / (N ** 2))  # Largest cluster ratio
        R_mean_list.append(np.mean(cluster_sizes) / (N ** 2))  # Mean cluster size
    else:
        Rmax_list.append(0)
        R_mean_list.append(0)
 
# --- Plot Time-Series Graphs ---
time = np.arange(num_frames)

plt.figure(figsize=(12, 8))

# Magnetization
plt.subplot(2, 2, 1)
plt.plot(time, M_list, label="Magnetization (M)", color='b')
plt.xlabel("Time Step")
plt.ylabel("M")
plt.legend()

# Magnetization Variance
plt.subplot(2, 2, 2)
plt.plot(time, sigma2_M_list, label="Magnetization Variance (σ²_M)", color='r')
plt.xlabel("Time Step")
plt.ylabel("σ²_M")
plt.legend()

# Largest Cluster Ratio
plt.subplot(2, 2, 3)
plt.plot(time, Rmax_list, label="Largest Cluster Ratio (Rmax)", color='g')
plt.xlabel("Time Step")
plt.ylabel("Rmax")
plt.legend()

# Mean Cluster Size
plt.subplot(2, 2, 4)
plt.plot(time, R_mean_list, label="Mean Cluster Size (R̄)", color='purple')
plt.xlabel("Time Step")
plt.ylabel("R̄")
plt.legend()

plt.tight_layout()
plt.show()
