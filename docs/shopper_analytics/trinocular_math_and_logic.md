# Tracking Math & Logic: Homography in a 12m x 3.5m Store

## 1. Physical Layout (The Security Triangle)
The retail monitoring space is a **12 meters by 3.5 meters** rectangular floor plan. Instead of securely placing three cameras side-by-side to act as "stereo eyes," we actively utilize the natural architectural scale to create a wide visual tracking triangle:

*   **Camera 1 (Entrance):** Mounted at a height of **2.9 meters**, viewing the 12-meter length of the room.
*   **Camera 2 & Camera 3 (Back Wall):** Spaced **3 meters apart**, mounted at a height of **2.7 meters**, pointing towards the entrance.

This triangle guarantees that almost every square inch of the 12m x 3.5m floor plane is visually covered by at least one optical device, effectively ending physical occlusions (shelving/signs).

## 2. The Core Mathematics: Inverse Perspective Mapping (IPM)
Because the cameras are 12 meters apart, classic stereo-vision triangulation (`Z = f*B/d`) is mathematically impossible. We cannot match disparities. 

Instead, we use **Homography (Inverse Perspective Mapping)**. Homography is a technique that takes an angled camera lens (like a security camera looking down at the store) and mathematically distorts the pixels until it looks exactly like a flat, 2D architectural blueprint (Bird's Eye View).

### Calibration (`cv2.getPerspectiveTransform`)
To initialize the mathematics, we do a one-time setup:
1. We mark 4 known physical points on the floor (e.g., the corners of the 12m x 3.5m room).
2. We map those exact metric coordinates to the pixel coordinates on the camera.
3. The software generates a 3x3 **Homography Transformation Matrix (`H`)** unique to that camera's angle and 2.7m/2.9m height.

### Tracking execution:
1.  **Object Detection:** We stream the Hikvision RTSP feed into **YOLOv11** (e.g., `yolo11n.pt`). YOLO instantly draws a bounding box around a shopper.
2.  **Point Extraction:** By extracting the Bottom-Center pixel of that bounding box, we know exactly where the shopper's feet are touching the floor in the image. Let this pixel be `(u, v)`.
3.  **The Warp:** We multiply the foot pixel `[u, v, 1]` by the camera's Homography Transformation Matrix `H`.
4.  **Result:** The math instantly outputs the shopper's true physical coordinate `(X_meters, Y_meters)` on the 12x3.5m grid. 

## 3. Resolving the Multi-Camera Space
Since we have three cameras feeding into three different Homography matrices, we combine all outputs into a single digital "Master Floor Plan."

If Camera 1 (Entrance) sees someone walking in, their `(X, Y)` projection begins tracing a line into the store. When they walk 6 meters in, Camera 2 at the back wall might also detect them. Because both cameras are projecting mathematically translated Homography coordinates onto the exact same virtual 12x3.5 meter grid, Camera 1 and Camera 2 will both put a dot on the exact same physical coordinates. We use a clustering algorithm (Non-Maximum Suppression) to merge dots that are physically within ~30cm of each other, seamlessly "handing off" the shopper's ID from one camera to another as they walk through the store.

## 4. Sensor Fusion & 3D WebGL LiDAR Mapping
The reason this camera system perfectly complements the sweeping LiDAR hardware is that BOTH sensory streams are fundamentally ingested and fused using advanced trigonometric projections locally on the GPU inside our Three.js engine.

### The Physics of the Hardware Sweep
Instead of sweeping at a linear, constant velocity (which introduces violent mechanical jitter and positional inaccuracy at the arc edges), the ESP32 utilizes a **FreeRTOS Native Sine-Wave Pendulum Harmonic**.
The hardware smoothly maps `0°-180°` tied directly to the `millis()` clock using a floating-point phase mapping mapping `sin(phase * 2.0 * PI)`. By organically decelerating at exactly the left and right peaks of the physical sweep, the LiDAR hardware physically absorbs massively denser optical reads exactly at the edges of the room automatically without sacrificing structural momentum!

### Spherical to Cartesian Dimensional Mapping (Math)
The Camsense hardware transmits raw 3D spherical polar coordinates over the WebSocket stream as:
`distance_mm`, `raw_lidar_angle`, `currentServoAngle`.

Inside the Three.js 3D Engine, we project these arrays instantaneously back into Cartesian format `[x, y, z]` using:
1.  **Radius:** `r = distance_mm / 1000.0`
2.  **Elevation / Pitch (LiDAR Spin Axis):** `elevationRad = LidarAngle * (PI / 180)`
3.  **Azimuth / Yaw (Servo Mechanical Axis):** `azimuthRad = (ServoAngle + offset + 90) * (PI / 180)`

$$P_x = r \cdot \cos(E) \cdot \cos(A)$$
$$P_y = r \cdot \sin(E)$$
$$P_z = r \cdot \cos(E) \cdot \sin(A)$$

This places each particle exactly in a massive `THREE.Points` `BufferGeometry` matrix, constructing an absolute structurally flawless visual representation of the store completely independently of Ray-Tracing overheads natively on the browser GPU!
