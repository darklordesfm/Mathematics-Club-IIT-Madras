import numpy as np
file_path = "C:/Users/Saravanan/Downloads/dataset_week_2_version_1.npy"
file = np.load(file_path)
file = file.astype(np.int8)
file[file == 255] = -1
new_file_path = "C:/Users/Saravanan/Downloads/dataset_week_2_modified.npy"
np.save(new_file_path, file)
print(file)
