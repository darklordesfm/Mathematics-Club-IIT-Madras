import numpy as np
import matplotlib.pyplot as plt
from skimage import color, data, io
from skimage.util import img_as_float

# Load the image with proper escaping for the path
image_path = "C:\\Users\\Saravanan\\Downloads\\1.jpeg"  # Use double backslashes for Windows paths
image = io.imread(image_path)

# Convert to grayscale (optional, modify if working with color images)
gray_image = color.rgb2gray(image)

# Perform Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(gray_image, full_matrices=False)

# Function to reconstruct image with k singular values
def reconstruct_image(U, S, Vt, k):
    S_reduced = np.diag(S[:k])  # Take the top-k singular values
    U_reduced = U[:, :k]       # Corresponding k columns of U
    Vt_reduced = Vt[:k, :]     # Corresponding k rows of Vt
    return np.dot(U_reduced, np.dot(S_reduced, Vt_reduced))

# Values of k to visualize compression levels
k_values = [5, 20, 50, 100, 200, 500]

# Create subplots
fig, axes = plt.subplots(1, len(k_values) + 1, figsize=(20, 10))

# Display the original image
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title("Original")
axes[0].axis('off')

# Display reconstructed images with varying k
for i, k in enumerate(k_values):
    compressed_image = reconstruct_image(U, S, Vt, k)
    axes[i + 1].imshow(compressed_image, cmap='gray')
    axes[i + 1].set_title(f"k = {k}")
    axes[i + 1].axis('off')

plt.tight_layout()
plt.show()

plt.imsave('original_image.png', gray_image, cmap='gray')

# Save the reconstructed images with varying k
for i, k in enumerate(k_values):
    compressed_image = reconstruct_image(U, S, Vt, k)
    plt.imsave(f'compressed_image_{k}.png', compressed_image, cmap='gray')