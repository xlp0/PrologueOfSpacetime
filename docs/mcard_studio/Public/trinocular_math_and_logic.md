# Trinocular Vision System: Mathematical Foundations & Logic

## 1. How the System Works (Conceptual Overview)
The proposed system uses three identical cameras (Left, Center, Right) rigidly mounted in a straight line. The objective is to calculate the precise distance (Z-axis) of any object in the room, specifically shoppers detected by YOLO.

By computing the positional difference (disparity) of the exact same pixel across multiple cameras, we can mathematically triangulate how far away that pixel is in the real physical world, completely eliminating the need for expensive infrared lasers like the Kinect.

## 2. The Core Mathematics: Triangulation
The fundamental formula for calculating distance in stereo vision relies on the geometry of similar triangles. 

**The Depth Formula:**
`Z = (f * B) / d`

**Where:**
*   **Z (Depth):** The absolute distance from the camera array to the object (in meters or millimeters).
*   **f (Focal Length):** The mathematical curvature of the camera lens, measured in pixels. This is extracted during the Intrinsic Calibration phase using a printed checkerboard.
*   **B (Baseline):** The physical distance between the cameras (e.g., the distance from Center to Left). *You mentioned you will provide this exact mechanical measurement later.*
*   **d (Disparity):** The difference in the X-coordinate of the exact same object between two different camera views. If a shopper's nose is at pixel `X=500` on the Center camera, but at `X=450` on the Left camera, the disparity `d` is `50`.

*Rule of Thumb:* The larger the Disparity (`d`), the closer the object is. As an object moves infinitely far away, the disparity approaches zero.

## 3. Why Trinocular? (Solving Occlusion)
A standard stereo camera system (like human eyes) only uses two cameras. However, in a crowded retail environment, a physical shelf or another person might block the Left camera's view of a shopper. If the Left camera cannot see the shopper, standard stereo vision instantly fails and creates a "black hole" in the depth map (returning distance `Z = 0`).

**The Trinocular Advantage:**
By using three cameras (L, C, R), we run two parallel mathematical depth calculations simultaneously frame-by-frame:
1.  **Pair 1:** Left <-> Center
2.  **Pair 2:** Center <-> Right

If the Left camera is blocked by a shelf, Pair 1 fails. However, Pair 2 (Center <-> Right) will critically still have a clear view and successfully calculate the depth. We synthesize both mathematical passes into a single, flawless, occlusion-proof 3D depth map.

## 4. Identifying Real-World Coordinates (X, Y, Z)
Once the Trinocular Semi-Global Block Matching algorithm generates the master Depth Map, every single pixel on the screen is assigned a Z-distance. Here is how the full software pipeline identifies the shopper's location relative to the store layout:

1.  **Object Detection (YOLO API):** We feed the Center Camera's RGB image into YOLOv11. YOLO draws a bounding box around a shopper and gives us their center pixel coordinate on the screen: `(u, v)`.
2.  **Depth Extraction:** We look at the exact same `(u, v)` pixel on our synthesized Trinocular Depth Map to find the calculated depth `Z`. We now know exactly how far away the shopper is from the sensor rig.
3.  **Real-World Projection:** Knowing a pixel's `(u, v)` and its absolute depth `Z`, we reverse the camera projection matrix to find their exact physical location in the room relative to the center camera:
    *   `X_real = (u - cx) * Z / fx` (Horizontal physical position in the room)
    *   `Y_real = (v - cy) * Z / fy` (Vertical physical position / height)
    *   `Z_real = Z` (Physical distance out from the camera array)

*(Note: `cx`, `cy`, `fx`, and `fy` are mathematical constants unique to your specific camera lenses, extracted automatically during the checkerboard calibration step).*

## Next Steps for Implementation
1.  **Mounting:** Firmly lock the three cameras into their rigid physical rail. Measure and define the Baseline `B`.
2.  **Checkerboard Calibration:** We will write a Python script (using OpenCV) to take overlapping photos of a physical checkerboard to extract `f` (focal length) and mathematically correct the cheap plastic lens distortion.
3.  **Driver Initialization:** Ingest all three feeds concurrently and align them into a single synthesized depth matrix.

## 5. Sensor Fusion: Combining the Trinocular Array with the 3D LiDAR
You recently built a custom 3D LiDAR scanning rig. If we rigidly mount this LiDAR at a known, fixed physical distance from the Trinocular camera array (for example, exactly 10cm directly above the Center camera), we unlock **Sensor Fusion**.

**Why your hypothesis is exactly correct:**
By knowing the exact physical offset between the two sensors (called an *Extrinsic Translation Vector*), we can mathematically overlap their two coordinate systems into one single "Master Map". 

*   **The LiDAR** scans the absolute, millimeter-perfect static architecture of the room (the walls, the shelves, the boundaries).
*   **The Trinocular Cameras** run YOLO to track the dynamic, moving shoppers in real-time.

Because we know the exact mathematical distance between the LiDAR and the cameras, we don't have to guess where the humans are relative to the room. We simply take the human's Trinocular 3D coordinate, apply the offset, and drop them perfectly inside the LiDAR's architectural 3D point cloud. This makes the system profoundly more accurate, as the cameras no longer need to calculate the depth of the room itself—they only need to focus on tracking the humans inside it!
