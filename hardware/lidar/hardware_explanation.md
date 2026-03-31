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
*   **Hardware:** 1x 2D X2 360° LiDAR (mid-range mapping/SLAM) + 1x Stepper Motor (with Slip Ring for continuous 360-degree 3D articulation without wire tangling).
*   **Cost:** ~296k IDR (LiDAR) + ~100k IDR (34k Stepper Motor + Slip Ring) = **~396k IDR**.

### Sensor Fusion Total Cost
By merging the 3 IP cameras (900k IDR) with the centrally articulating 3D LiDAR setup (~396k IDR), **the total hardware cost drops drastically to just ~1.3 million IDR** for full, uncompromised room tracking, compared to the 8.8 million IDR Kinect setup.

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
2.  1x **[X2 360° Lidar (Laser Radar Scanning)](https://www.tokopedia.com/yodatech/laser-radar-scanning-360-degree-8526-1734250510598506271?utm_source=salinlink&utm_medium=share&utm_campaign=pdp-127btgvfv30x-102955591624-0)** (~296k IDR)
3.  1x **[Stepper Motor 42 Nema17 17HS3401](https://www.tokopedia.com/dw-store/stepper-motor-42-nema17-nema-17-stepping-cnc-3d-printer-17hs3401?extParam=ivf%3Dfalse%26keyword%3Dsteper+motor%26search_id%3D2026031105165011B9842E0A271F1190NJ%26src%3Dsearch&t_id=1773206234855&t_st=2&t_pp=search_result&t_efo=search_pure_goods_card&t_ef=goods_search&t_sm=&t_spt=search_result)** (~34k IDR) + **Slip Ring** (To continuously articulate the 2D LiDAR for full 360x360 3D scanning without snapping cables)
4.  1x **Raspberry Pi 5 (8GB, 1.4GHz, WiFi)** (Host Processing Unit for YOLO, LiDAR fusion, and Epipolar geometry math)
5.  Standard networking/power cables for the camera placements.

---

## 5. X2 LiDAR (8526) Technical Specifications

Based on the official Yodatech listing, here are the core hardware specifications of the chosen LiDAR unit:

*   **Model:** X2 Lidar (360 Degree Scanning)
*   **Operating Voltage:** DC 5V
*   **Data Interface:** Serial UART (TTL Level - 3.3V compatible)
*   **Baud Rate:** 115200
*   **Working Principle:** Laser Triangulation Radar
*   **Protocol:** Camsense X1 Clone Protocol (36-byte packets starting with `0x55 0xAA 0x03 0x08`, requiring a `0xA000` angle offset for correct computation rather than the standard YDLidar protocol)
*   **Connection wires:** 4 Wires (VCC, GND, TX, RX/PWM Motor Control)

---

## 6. References & Technical Context

### The Catalyst for the Pivot
This custom multi-camera and LiDAR sensor fusion architecture was heavily influenced by the fundamental constraint that Apple Silicon (M3/M4) Macs cannot natively run the open-source `libfreenect2` drivers required to extract Kinect v2 depth video. The USB driver segmentation faults on modern macOS, combined with the 4.5m physical limitation of the Kinect's Time-of-Flight sensor, forced the strategic shift to lightweight IP cameras and standard robotic LiDARs.

### Inspiration & Open Source Mocap
A primary reference and inspiration for achieving accurate spatial tracking across a wide area without traditional Kinect arrays is the **Open Source Motion Capture for Autonomous Drones** framework.
*   **Reference Video:** [Open Source Motion Capture for Autonomous Drones](https://www.youtube.com/watch?v=0ql20JKrscQ&t=212s)

In the referenced video, the creator successfully executes motion location capture across a room using an array of **four inexpensive PS3 Eye cameras**. This drone mocap philosophy—using distributed external cameras to identify a target and cross-referencing spatial positioning—perfectly mirrors our Trinocular IP Camera + central LiDAR approach for tracking human shoppers.