# Hardware Specification: SPC Smart Series BC1

## 1. Overview
The second component of the visual tracking array utilizes the **SPC Smart Series BC1**, a 3-Megapixel smart network camera. 
Unlike the static Hikvision bullet cameras, the SPC BC1 features a **motorized Pan & Tilt (PTZ)** mechanism. This fundamentally changes how it can be utilized in the Shopper Analytics pipeline, allowing for dynamic, active tracking rather than just passive static observation.

---

## 2. Core Technical Specifications

| Feature | Specification | Impact on Analytics System |
| :--- | :--- | :--- |
| **Max Resolution** | 3 MP (approx. 2304 x 1296) | Higher base resolution than the Hikvision (2MP), allowing for slightly better digital zoom clarity when analyzing smaller objects (e.g., barcode scanning on shelves). |
| **Lens** | 3.6mm Fixed Lens | Typically yields an ~80° to 85° horizontal Field of View. Slightly more "zoomed in" than the Hikvision 4mm, providing excellent detail at medium ranges (3-5 meters). |
| **Mechanics** | Pan: 355° <br> Tilt: 120° | **Critical Advantage:** The camera can physically rotate to look around the room. It has virtually zero blind spots. |
| **Connectivity** | WiFi & LAN (RJ45) | For AI tracking, the hardwired LAN port MUST be used. WiFi introduces latency jitter which severely degrades real-time bounding box accuracy. |
| **Night Vision** | IR + Full Color Dual Light | Allows tracking in pitch black, with the option to trigger a white LED spotlight upon detecting motion to capture color footage. |
| **Power** | 12V DC | Identical power requirement to the Hikvision cameras and the LiDAR stepper motor. Extremely convenient for a unified power supply. |

---

## 3. Deployment Strategy: The "Active Tracker"

Because the SPC camera has **Pan and Tilt capabilities**, it should NOT be used as part of the rigid Stereo Vision baseline. (If a stereo camera moves independently, the math instantly breaks).

Instead, the system should be deployed in a **Master/Slave** architecture:

1.  **The "Global Mapper" (Master):** The two static 2MP Hikvision cameras sit rigidly on the wall. They constantly monitor the entire aisle, calculating 3D depth and identifying where anonymous "Shopper A" is standing.
2.  **The "Active Tracker" (Slave):** The 3MP SPC camera is mounted on the ceiling in the center of the zone. 
    *   When the Hikvision cameras detect Shopper A exhibiting "high-interest behavior" (e.g., stopping at an endcap display for more than 10 seconds), the Python Master script sends a PTZ command to the SPC camera over the network.
    *   The SPC camera physically rotates to point directly at Shopper A, using its 3-Megapixel sensor to get a high-quality, close-up shot of exactly what product the shopper is picking up.

---

## 4. Hardware Integration Checklist
*   **Network Protocol:** We need to verify if the SPC camera outputs a standard RTSP stream or an ONVIF profile. Many "Smart Home" cameras lock their streams to proprietary mobile apps. If it supports ONVIF/RTSP, OpenCV can ingest it easily.
*   **PTZ Control:** If ONVIF is supported, we can use the `python-onvif-zeep` library to programmatically send Pan/Tilt commands to the camera from our main tracking loop.
