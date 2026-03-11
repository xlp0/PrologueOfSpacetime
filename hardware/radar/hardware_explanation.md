# Custom Shopper Analytics Hardware Plan: LiDAR & Trinocular Vision Pivot

## 1. Executive Summary
This document outlines the pivot from our initial Microsoft Kinect v2 strategy to a custom **Trinocular Stereo Vision + 2D Spinning LiDAR** sensor fusion setup for Shopper Analytics. 

Our initial objective was to use Kinect v2 sensors for 3D/2D distance mapping. However, because the Kinect v2 is strictly limited to an accurate distance of 4.5 meters, covering our target 6x4m room would require up to 4 Kinects. At 2.2 million IDR each, this scales absurdly to **8.8 million IDR**.

To drastically reduce hardware costs while comprehensively covering the entire space, we are pivoting to a custom system consisting of three IP cameras for vision and a central 360-degree LiDAR for accurate spatial mapping.

---

## 2. The New Architecture: Sensor Fusion

### A. Trinocular Stereo Vision (Identification)
Instead of relying on heavy compute for RGB-D arrays, we will utilize three separate IP cameras placed across the room.
*   **Purpose:** Shopper identification, YOLO bounding box generation, and behavioral tracking.
*   **Hardware:** 3x IP Cameras.
*   **Cost:** ~300k IDR each (Total: 900k IDR).

### B. 2D Spinning LiDAR (Spatial Mapping & Distance)
To solve the Z-axis distance problem that the Kinect typically handles, we will deploy a single, centrally located 2D spinning LiDAR.
*   **Purpose:** Achieving the ability to scan the whole room simultaneously. The LiDAR will spin 360 degrees, providing a flawless 2D architectural map and pinpointing exactly where dynamic obstacles (shoppers) are standing up to a 12-meter range.
*   **Hardware:** 1x Custom 3D, 360-degree LiDAR (12-meter range).
*   **Cost:** ~1.75 million IDR.

### Sensor Fusion Total Cost
By merging the 3 IP cameras (900k IDR) with the central spinning LiDAR (1.75 million IDR), **the total hardware cost drops drastically to just 2.65 million IDR** for full, uncompromised room tracking, compared to the 8.8 million IDR Kinect setup.

---

## 3. How the Sensor Fusion Works

1.  **LiDAR Mapping:** The central LiDAR spins continuously, updating a 2D topographical map of the room multiple times a second. It extracts the X/Z coordinates of all legs/objects on the floor plan.
2.  **Vision Tracking:** The three IP cameras stream video to the host computer. A model like YOLOv11 processes the streams to identify shoppers and draw bounding boxes.
3.  **Synthesis:** The host machine synchronizes the LiDAR point cloud with the Trinocular vision feeds. When YOLO identifies a person in the camera feed, the system cross-references the LiDAR's sweeping angle at that exact millisecond to assign definitive spatial coordinates.

---

## 4. Procurement & Next Steps

*   **Communication:** I have drafted updates for Charli regarding this pivot to save costs and improve tracking coverage.
*   **Sourcing:** I have asked Duwi to help source these new sensors (the 3 IP cameras and the 12m LiDAR) for next week.

### Updated Shopping List
1.  3x **Standard IP Cameras** (~300k IDR each)
2.  1x **360-degree Spinning LiDAR (12m range)** (~1.75m IDR)
3.  1x **Host Processing Unit** (Existing PC / Mac for YOLO + LiDAR fusion)
4.  Standard networking/power cables for the camera placements.

### Implementation Timeline
1.  **Week 1:** Procure the LiDAR and IP Cameras (via Duwi). Mount the LiDAR in the center of the room and read the raw 360-degree distance array into Python.
2.  **Week 2:** Mount the 3 IP cameras. Calibrate the camera angles to the LiDAR's coordinate space.
3.  **Week 3:** Synchronize the YOLO RGB streams with the 2D LiDAR array to synthesize exact Shopper Analytics coordinates.
