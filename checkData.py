import numpy as np

# Path to your .npy file
file_path = './output_frames/flattened_data.npy'

# Load the .npy file
data = np.load(file_path)

# Print the shape and content of the loaded data
print(f"Data shape: {data.shape}")
print(data)
