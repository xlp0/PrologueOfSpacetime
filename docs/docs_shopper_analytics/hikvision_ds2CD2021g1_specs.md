# Hardware Specification: Hikvision DS-2CD2021G1 

## 1. Overview
For the Shopper Analytics tracking array, we are utilizing **two Hikvision DS-2CD2021G1-I (4mm)** IP Bullet Cameras. These are professional-grade, 2-Megapixel fixed-lens network cameras designed for 24/7 continuous surveillance. 

Given their specific lens and sensor combination, they are highly optimized for feeding clear, low-bandwidth video streams directly into AI tracking models like YOLOv11.

---

## 2. Core Technical Specifications

| Feature | Specification | Impact on Analytics System |
| :--- | :--- | :--- |
| **Max Resolution** | 2 MP (1920 × 1080) @ 30fps | 1080p is the sweet spot for AI. It provides enough pixel density to track small objects (like hands interacting with shelves) without permanently maxing out the GPU processing limits. |
| **Lens** | 4mm Fixed Lens | Provides a focused, tighter shot than a standard 2.8mm wide-angle lens. Perfect for looking down grocery aisles without severe fish-eye distortion. |
| **Field of View** | Horizontal: ~86° to 91.5°<br>Vertical: ~46° | The 86-degree horizontal sweep allows a single camera to comfortably cover a 6-meter-wide tracking zone from 4 meters away. |
| **Compression** | H.265+ / H.264 | H.265+ vastly reduces network bandwidth. Running 2 concurrent 1080p streams will not crash or lag the local network switch. |
| **WDR (Wide Dynamic)**| 120 dB True WDR | Crucial for retail environments. If the camera points towards a bright glass storefront window, shoppers walking inside won't turn into black silhouettes. |
| **Night Vision** | 30m IR Range (0.005 Lux Color) | Ensures the analytics system can still track motion or potential theft after the store lights are turned off for the night. |

---

## 3. Power Architecture (12V DC)

The cameras support both standard PoE (Power over Ethernet) and **12V DC**.

**Deployment Strategy:**
By utilizing the **12V DC** barrel jack input on the camera pigtail, we can significantly reduce the cost of the hardware array. 
*   **No PoE Switch Required:** Standard 8-port gigabit switches are extremely cheap. PoE switches are highly expensive. 
*   **Centralized Power:** We can run a single industrial 12V DC Power Supply Unit (PSU) and daisy-chain 12V splitter cables to power both Hikvision cameras, the 12V 3D LiDAR motor, and the main computer logic board simultaneously from one wall plug. 

---

## 4. Performance in the Shopper Analytics Pipeline: The "Global Mapper"

The Hikvision cameras serve as the foundational **"Master"** sensors in our **Master/Slave Tracking Architecture**.

### 4.1. The "Global Mapper" (Master) Role
By placing two of these identical 4mm Hikvision cameras side-by-side on a rigid mount, we establish a highly accurate **Stereo Vision** baseline.
*   Because they share identical CMOS sensors, fixed 4mm lenses, and never physically move, OpenCV can perfectly align their feeds to generate a 3D depth map of the entire environment.
*   Their primary job is to constantly identify *where* shoppers are standing in the aisle (X, Y, Z coordinates).
*   **Triggering the Slave:** When these Hikvision "Master" cameras detect a shopper interacting with a shelf, the system sends a command to the secondary "Slave" camera (the motorized SPC BC1 PTZ camera) to physically rotate and zoom in on that exact shopper's hands to capture high-definition product interaction data.

### 4.2. RTSP Stream Ingestion
The analytics software will tap into the cameras using the RTSP (Real-Time Streaming Protocol). 
*   **Primary Stream (1080p):** Fed directly into the YOLO AI for bounding box detection and to act as the spatial trigger system for the secondary PTZ camera.
*   **Sub-Stream (640x480):** Fed into the UI Dashboard to display the heatmaps and visual overlays, keeping CPU rendering costs low.
