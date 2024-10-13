import cv2
import os
import numpy as np

def preprocess_frame(frame):
    """
    Preprocess the frame by converting it to grayscale, normalizing pixel values, and flattening it.
    :param frame: The input frame (color image).
    :return: Flattened grayscale frame with pixel values between 0 and 1.
    """
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Normalize pixel values to the range [0, 1]
    normalized_frame = gray_frame / 255.0

    # Flatten the grayscale frame
    flattened_frame = normalized_frame.flatten()

    return flattened_frame

def extract_frames_and_flatten(video_path, output_folder, flattened_data_path, target_fps=15, target_width=224, target_height=224):
    # Open the video file specified by video_path for reading
    cap = cv2.VideoCapture(video_path)

    # Get the original frames per second (fps) of the video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f'fps: {fps}')  # Print the fps for debugging purposes

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Initialize a list to store the flattened frames
    flattened_frames = []

    # Loop through the video frames until all are processed
    while cap.isOpened():
        ret, frame = cap.read()  # Read the next frame

        if not ret:
            break  # Exit the loop if no frame is returned (end of video)

        # Resize the frame to the target dimensions (224x224 by default)
        resized_frame = cv2.resize(frame, (target_width, target_height))

        # Preprocess the resized frame: grayscale, normalize, and flatten
        flattened_frame = preprocess_frame(resized_frame)

        # Append the flattened frame to the list
        flattened_frames.append(flattened_frame)

    # Convert the list of flattened frames into a NumPy array for easier storage and manipulation
    flattened_frames_array = np.array(flattened_frames)

    # Save the flattened data to a .npy file
    np.save(flattened_data_path, flattened_frames_array)

    # Release resources: video capture
    cap.release()
    cv2.destroyAllWindows()

    print(f"Flattened data saved to {flattened_data_path}")


# Example usage
if __name__ == '__main__':
    video_path = './how do i clip.mp4'
    output_folder = 'output_frames'
    flattened_data_path = './output_frames/flattened_data.npy'
    extract_frames_and_flatten(video_path, output_folder, flattened_data_path)
