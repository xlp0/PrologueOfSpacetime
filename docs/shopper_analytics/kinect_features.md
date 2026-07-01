# Kinect Features for Shopper Analytics

To program the Xbox Kinect for Shopper Analytics, we need to leverage several key hardware and software features. Since you are on macOS, we will likely use open-source drivers like `libfreenect` or `libfreenect2`.

## 1. Depth Sensing (Key Feature)
*   **What it is**: The Kinect projects an infrared pattern to measure the distance of every pixel.
*   **Why we need it**: 
    *   **Privacy**: It allows tracking movement without necessarily recording identifiable facial features.
    *   **Background Subtraction**: Easily distinguish moving people from static shelves and displays based on distance, not just color.
    *   **3D Sizing**: Determine the approximate height and size of objects (e.g., adult vs. child, cart vs. person).

## 2. RGB Video Camera
*   **What it is**: Standard color video stream.
*   **Why we need it**:
    *   **Visualization**: To overlay analytics on a real-world view for the dashboard.
    *   **Stock Availability**: Using Computer Vision (AI) on the color image to detect gaps on shelves.
    *   **Re-identification**: (Optional) Matching color histograms to track a person if they temporarily get occluded.

## 3. Coordinate Mapping (Registration)
*   **What it is**: aligning the Depth camera's view with the RGB camera's view.
*   **Why we need it**: To know exactly *where* in the color image a depth object is. e.g., "The object at pixel (100,100) is 2 meters away."

## 4. Skeletal / Body Tracking (Software Layer)
*   **What it is**: Algorithms that interpret depth data to find "joints" (head, shoulders, arms).
*   **Why we need it**:
    *   **Traffic Flow**: Accurately counting distinct people and tracking their paths through the store.
    *   **Behavior Analysis**: Detecting if a person is reaching for a shelf (arm extension).
    *   *Note*: On macOS with open-source drivers, this often requires additional libraries (like NiTE, which is old, or modern CV/Deep Learning models like MediaPipe or OpenPose running on the RGB+Depth data).

## 5. Infrared (IR) Stream
*   **What it is**: The raw view of the infrared camera.
*   **Why we need it**: Useful for night-time or low-light analytics where the RGB camera fails.

## Summary of Programming Needs
To achieve the project goals, our software stack needs to:
1.  **Initialize the Kinect Driver** (connect to USB).
2.  **Poll for Frames**: Continuously grab Depth and RGB arrays (typically numpy arrays in Python).
3.  **Process Images**: Use OpenCV to analyze these arrays (background removal, blob tracking).
4.  **Store/Visualize**: Log the tracks to a database or draw them on a screen.
