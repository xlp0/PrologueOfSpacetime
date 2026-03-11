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

### B. 2D LiDAR + Spin Motor = 3D LiDAR (Spatial Mapping & Distance)
To solve the Z-axis distance problem that the Kinect typically handles, we will deploy a single, centrally located 2D LiDAR mounted on an auxiliary motor to achieve full 3D scanning.
*   **Purpose:** Achieving the ability to scan the whole room simultaneously. The LiDAR itself spins 360 degrees in 2D, and an auxiliary motor will articulate it across the remaining axis to construct a flawless 3D architectural point cloud, pinpointing exactly where dynamic obstacles (shoppers) are standing up to a 12-meter range.
*   **Hardware:** 1x 2D LiDAR (12-meter range) + 1x Auxiliary Motor (Servo/Stepper for 3D articulation).
*   **Cost:** ~1.75 million IDR (LiDAR) + ~150k IDR (Motor) = **~1.9 million IDR**.

### Sensor Fusion Total Cost
By merging the 3 IP cameras (900k IDR) with the centrally articulating 3D LiDAR setup (1.9 million IDR), **the total hardware cost drops drastically to just 2.8 million IDR** for full, uncompromised room tracking, compared to the 8.8 million IDR Kinect setup.

---

## 3. How the Sensor Fusion Works

1.  **LiDAR Mapping:** The central LiDAR spins continuously, updating a 2D topographical map of the room multiple times a second. It extracts the X/Z coordinates of all legs/objects on the floor plan.
2.  **Vision Tracking:** The three IP cameras stream video to the host Raspberry Pi. A model like YOLOv11 processes the streams to identify shoppers and draw bounding boxes.
3.  **Synthesis (Epipolar Geometry):** The system uses **Epipolar Geometry** as the core mathematical foundation to cross-reference the 2D visual perspectives from the multiple cameras. The Raspberry Pi synchronizes this epipolar visual data with the LiDAR's 2D floor-plan mapping arrays at the exact millisecond to synthesize precise 3D spatial coordinates.

---

## 4. Procurement & Next Steps

*   **Communication:** I have drafted updates for Charli regarding this pivot to save costs and improve tracking coverage.
*   **Sourcing:** I have asked Duwi to help source these new sensors (the 3 IP cameras and the 12m LiDAR) for next week.

### Updated Shopping List
1.  3x **Standard IP Cameras** (~300k IDR each)
2.  1x **[RPLidar A1M8 360-degree Laser Scanner (12m range)](https://www.tokopedia.com/eandc-electronics/rplidar-a1m8-r6-360-degree-laser-scanner-kit-12m-range-lidar-dfrobot?extParam=ivf%3Dfalse%26keyword%3Dlidar+scanner%26search_id%3D2026031014111494F6D7E04A4D453C4VX0%26src%3Dsearch)** (~1.75m IDR)
3.  1x **Auxiliary Motor (Servo/Stepper)** (~150k IDR) (To articulate the 2D LiDAR for full 3D scanning)
4.  1x **Raspberry Pi 5 (8GB, 1.4GHz, WiFi)** (Host Processing Unit for YOLO, LiDAR fusion, and Epipolar geometry math)
5.  Standard networking/power cables for the camera placements.

---

## 5. References & Technical Context

### The Catalyst for the Pivot
This custom multi-camera and LiDAR sensor fusion architecture was heavily influenced by the fundamental constraint that Apple Silicon (M3/M4) Macs cannot natively run the open-source `libfreenect2` drivers required to extract Kinect v2 depth video. The USB driver segmentation faults on modern macOS, combined with the 4.5m physical limitation of the Kinect's Time-of-Flight sensor, forced the strategic shift to lightweight IP cameras and standard robotic LiDARs.

### Inspiration & Open Source Mocap
A primary reference and inspiration for achieving accurate spatial tracking across a wide area without traditional Kinect arrays is the **Open Source Motion Capture for Autonomous Drones** framework.
*   **Reference Video:** [Open Source Motion Capture for Autonomous Drones](https://www.youtube.com/watch?v=0ql20JKrscQ&t=212s)

In the referenced video, the creator successfully executes motion location capture across a room using an array of **four inexpensive PS3 Eye cameras**. This drone mocap philosophy—using distributed external cameras to identify a target and cross-referencing spatial positioning—perfectly mirrors our Trinocular IP Camera + central LiDAR approach for tracking human shoppers.