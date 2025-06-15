import cv2
import time

def find_and_open_camera():
    """
    Attempts to open a camera by iterating through common indices.
    Returns the VideoCapture object if successful, None otherwise.
    """
    max_cameras_to_check = 5  # Check indices from 0 up to 4

    for i in range(max_cameras_to_check):
        print(f"Attempting to open camera with index {i}...")
        cap = cv2.VideoCapture(i)

        if cap.isOpened():
            print(f"Successfully opened camera with index {i}.")
            return cap
        else:
            print(f"Failed to open camera with index {i}.")
            cap.release() # Release if not opened to clean up

    print("Error: Could not open any camera. Please check camera connections, permissions, or if another application is using the camera.")
    return None

def main():
    try:
        # Find and open the camera
        cap = find_and_open_camera()

        if cap is None:
            # If no camera was opened, exit
            return

        print("Camera stream started. Press 'q' to quit.")

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            if not ret:
                print("Error: Could not read frame. Exiting...")
                break

            print("Frame captured successfully.")
            time.sleep(1)

        # Release the camera and close all OpenCV windows
        cap.release()
        print("Camera released and windows closed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Script finished. Keeping container alive...")
        while True:
            time.sleep(100000)

if __name__ == "__main__":
    main()
    while True:
        time.sleep(100000)