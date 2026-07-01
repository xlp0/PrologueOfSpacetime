# Custom Shopper Analytics Hardware Plan (Kinect v2 Replacement)

## 1. Executive Summary
This document outlines the hardware architecture options for building a custom, low-cost sensor array to replace the Microsoft Kinect v2 for Shopper Analytics. The objective is to achieve reliable human tracking and 3D/2D distance mapping up to **8 - 10 meters** using locally assembled components like microcontrollers (ESP32/Raspberry Pi) and RGB cameras combined with LiDAR/ToF distance sensors.

---

## 2. Current Architecture: Dual LiDAR & Servo System
Rather than using an MPU6050 and spinning a single LiDAR on a continuous stepper motor, we mount **two 2D LiDARs back-to-back on a single 180° sweeping servo motor**. 
This eliminates the need to rely heavily on complex IMU computations and continuous slip rings.

### Core Setup & Bill of Materials
*   **Hardware:** 2x 2D X2 360° LiDARs + 1x 180° Servo Motor + 1x ESP32-S + 1x External 5V 3A Power Supply
*   **Purpose:** The servo mechanism rotates the two LiDARs exactly 180 degrees back and forth. Because there are two LiDARs facing opposite directions, a 180° sweep covers a full 360° hemispherical 3D dome point cloud.
*   **Cost Efficiency:** While requiring a second LiDAR, we save on the A4988 driver, continuous stepper motor, custom slip ring, and MPU6050, resulting in roughly identical cost but a drastically simplified moving part assembly and zero IMU math.

**Bill of Materials (BoM) per Dual-LiDAR Module**
Based on current local Indonesian pricing (Tokopedia, March 2026):
*   **2x X2 360° LiDARs:** Rp 295,500 each = **Rp 591,000**
*   **1x MG996R 180° Metal Gear Servo:** **~Rp 45,000**
*   **1x ESP32 30-pin Microcontroller:** **~Rp 45,000**
*   **1x 5V 3A Power Supply:** **~Rp 40,000**
*   **Misc (Custom 3D OpenSCAD Mounts, Wires):** **~Rp 29,000**
*   **Total Estimated Cost:** **~Rp 750,000** (~$47 USD) per Dual-LiDAR array.
*(Note: Covering an entire 1,200m² store requires exactly 6 of these arrays—one per 200m² analytical zone—bringing the total LiDAR hardware footprint cost to exactly **Rp 4,500,000**).*

### How it works
1. **Sweeping Mechanism:** The ESP32's `ESP32Servo` library triggers an automated loop that sets the angle of the servo from 0 to 180, and then backwards. 
2. **Data Acquisition:** Both LiDAR streams are read simultaneously using ESP32 Hardware UART1 (remapped) and UART2.
3. **Point Cloud Generation:** Every distance/angle coordinate reported by the LiDARs is combined with the Servo's current angle parameter in real time to generate precise 3D (X, Y, Z) coordinates.

---

## 3. Hikvision IP Camera Integration

### Camera Specifications & Network Configuration

The system utilizes **Hikvision IP Cameras** for RGB video input, which are integrated with the LiDAR arrays to provide comprehensive shopper tracking capabilities.

#### Deployed Camera Information
- **Camera 1**: `192.168.100.24`
- **Camera 2**: `192.168.100.34`
- **Camera 3**: `192.168.100.26`

#### Network Access Requirements
The cameras are deployed on an isolated `192.168.100.0/24` subnet. Access requires:
- Direct connection to the camera network segment
- Proper routing configuration from hpserver (biznetmaster) if accessing remotely
- Network interface on the `192.168.100.0/24` subnet

**Important Network Limitation**: The hpserver does NOT have a direct interface on the camera subnet by default. While ICMP (ping) works, TCP connections (HTTP/RTSP) require proper network routing or access from a device on the same subnet.

#### Access Ports & Protocols
- **HTTP Web Interface**: Port 80 (default) or Port 8000 (alternative)
- **RTSP Stream**: Port 554

### RTSP Stream Integration

For real-time video processing and YOLO object detection, the cameras provide RTSP streams:

**RTSP URL Format**:
```
rtsp://admin:[password]@[camera-ip]:554/Streaming/Channels/[channel]
```

**Channel Options**:
- **Channel 101**: Main stream (high quality, recommended for analytics)
- **Channel 102**: Sub stream (lower quality, for bandwidth-constrained scenarios)

**Complete RTSP URLs for Deployed Cameras**:
```
rtsp://admin:[password]@192.168.100.24:554/Streaming/Channels/101
rtsp://admin:[password]@192.168.100.34:554/Streaming/Channels/101
rtsp://admin:[password]@192.168.100.26:554/Streaming/Channels/101
```

### Integration with Edge Computing

The Hikvision cameras serve as the RGB input source for the YOLOv11 object detection pipeline running on either:
- **Raspberry Pi 5** (for basic spatial mapping)
- **Nvidia Jetson Orin Nano** (for advanced on-device sensor fusion)

**Processing Workflow**:
1. RTSP stream is captured from Hikvision camera
2. YOLOv11 identifies shoppers and generates bounding boxes
3. LiDAR data provides precise distance measurements
4. Sensor fusion combines RGB detection with 3D spatial coordinates
5. Final `(X, Y, Z)` coordinates are transmitted to analytics server

### Camera Deployment for 1,200m² Store

Based on the 8-meter effective tracking radius, a standard **1,200 m²** retail space requires:
- **6 analytical zones** (200m² each)
- **3 IP Cameras per zone**
- **Total: 18 Hikvision IP Cameras** + 6 Dual-LiDAR arrays

This configuration ensures complete coverage with optimal overlap for continuous shopper tracking across the entire store.

### Security Considerations

**Important**:
- Cameras are on isolated network segment (192.168.100.0/24)
- RTSP credentials are transmitted in clear text
- Use VPN or secure tunneling when accessing remotely
- Video processing occurs locally on Edge devices (Jetson/Pi) - footage never leaves the store network
- Only anonymized coordinate data `(X, Y, Z)` is transmitted to cloud servers

---

## 4. The Core Problem: How the Kinect Works
The Microsoft Kinect v2 uses **Time-of-Flight (ToF)** technology. It essentially houses a **Flash LiDAR**, projecting a massive grid of 217,000 infrared lasers across the entire room simultaneously.
Building this exact hardware from scratch with off-the-shelf maker electronics is highly challenging because microcontrollers like the **ESP32** are too slow to process hundreds of thousands of distance points per second while simultaneously handling 1080p RGB video. Hence, the Dual LiDAR sweeping radar system (Architecture 2) was invented to achieve the goal of 8-10m tracking.

---
This option takes a cheap, single-point laser and physically sweeps it across the room to map it.

*   **Core Hardware:** 
    *   ESP32 Microcontroller
    *   TF-Luna LiDAR (or VL53L1X)
    *   Micro Servo Motor (e.g., SG90)
    *   Standard RGB USB Webcam (connected to host PC)
*   **How it Works:** The ESP32 rapidly rotates the servo 180 degrees back and forth. The TF-Luna laser pulses continuously as it spins, creating a 2D radar slice of the room. The host PC matches the radar blips to the YOLO bounding boxes provided by the webcam.
*   **Range:** Up to 8 Meters.
*   **Pros:** Extremely cheap (< $30). Runs perfectly on an ESP32.
*   **Cons:** Very slow refresh rate (the servo takes time to sweep). May miss fast-moving shoppers.

### Option B: The "2D Spinning LiDAR" (ESP32 / Pi + RPLidar)
This is the industry standard for 2D robotic mapping (SLAM), commonly seen on robot vacuums.

*   **Core Hardware:**
    *   ESP32 or Raspberry Pi
    *   RPLidar A1 or YDLidar X3
    *   Standard RGB USB Webcam (connected to host PC)
*   **How it Works:** The RPLidar has an internal motor that violently spins a laser 360 degrees 10 times a second. It automatically outputs a flawless 2D architectural map of the room and highlights exactly where pairs of dynamic legs (shoppers) are standing.
*   **Range:** Up to 12 Meters.
*   **Pros:** Outputs data automatically. 360-degree perfect tracking. Easy to mount on the ceiling for a perfect "floor plan" view.
*   **Cons:** Costs around $70-$100. It provides a 2D map, not a 3D point cloud.

### Option C: The "Mini Kinect" (Raspberry Pi + Flash ToF Array)
This is the closest 1:1 replacement for the original Kinect device.

*   **Core Hardware:**
    *   Raspberry Pi 4 or 5 (An ESP32 cannot handle this)
    *   Arducam ToF Camera Module (Time-of-Flight)
    *   Standard RGB USB Webcam
*   **How it Works:** The Arducam ToF module projects a grid of lasers and captures a raw 3D Depth Map (240x180 resolution) in a single flash, exactly like the Kinect.
*   **Range:** ~4 - 6 Meters (depends on lens specification; not ideal for 10m).
*   **Pros:** True 3D depth mapping (Z-axis). No moving parts.
*   **Cons:** Very compute-heavy. Requires upgrading from an ESP32 to an expensive Raspberry Pi 5. Laser intensity drastically degrades beyond 5 meters.

---

## 4. Recommended Procurement & Next Steps

If the goal is to specifically use an **ESP32** and achieve an **8 to 10-meter range**, the most robust and accurate engineering path is **Option B (2D Spinning LiDAR)**.

### Shopping List (For Option B)
1.  1x **ESP32 Development Board** (or standard Arduino/NodeMCU)
2.  1x **RPLidar A1** (or equivalent 360-degree 2D LiDAR scanner)
3.  1x **Standard 1080p RGB USB Webcam**
4.  Standard jumper wires for UART serial connection.

### Implementation Timeline
1.  **Week 1:** Wire the RPLidar to the host machine or ESP32 via UART. Read the raw 360-degree distance array into Python to prove the sensor works.
2.  **Week 2:** Synchronize the YOLOv11 RGB stream with the 2D LiDAR array. When YOLO identifies a person at pixel `X`, cross-reference the LiDAR's sweeping angle at that exact millisecond to extract the `Z` distance.
3.  **Week 3:** Render the newly synthesized X/Z coordinates onto the Shopper Analytics Top-Down dashboard.

---

## 5. Raspberry Pi vs. Nvidia Jetson for Edge AI

While the Raspberry Pi 5 is a phenomenal general-purpose single-board computer, the **Nvidia Jetson** series (specifically the Jetson Orin Nano) is explicitly designed as an embedded AI computer. 

### Key Differences
| Feature                  | Raspberry Pi 5 (8GB)                                                                                                                                                                   | Nvidia Jetson Orin Nano (8GB)                                        |
| :----------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| **Compute Focus**        | High-performance CPU tasks.                                                                                                                                                            | GPU-accelerated AI and Computer Vision.                              |
| **CPU Architecture**     | **4-core** Arm Cortex-A76 (2.4GHz)                                                                                                                                                     | **6-core** Arm Cortex-A78AE v8.2 64-bit                              |
| **GPU Architecture**     | VideoCore VII (basic graphics).                                                                                                                                                        | NVIDIA Ampere (**1024 CUDA Cores** / 32 Tensor Cores).               |
| **Raw Compute (TFLOPS)** | **~0.05 TFLOPS** (FP32)                                                                                                                                                                | **~1.28 to 2.08 TFLOPS** (FP32 depending on power profile/Super kit) |
| **AI Inference (TOPS)**  | Effectively **0 TOPS** natively (requires an M.2 expansion HAT and Hailo-8L accelerator attached to reach 13 TOPS).                                                                    | Up to **40 TOPS** (Sparse INT8 natively via Tensor Cores).           |
| **Memory Bandwidth**     | LPDDR4X.                                                                                                                                                                               | LPDDR5 (102 GB/s) - crucial for loading large AI models.             |
| **Software Stack**       | General Linux (Debian).                                                                                                                                                                | NVIDIA JetPack (TensorRT, CUDA, DeepStream).                         |
| **Target Workload**      | I/O manipulation, basic scripting, lightweight CV.                                                                                                                                     | Generative AI, YOLO object detection at high FPS, LLMs.              |
| **Estimated Price**      | **~$80** (~Rp 1,280,000) (Board only). To get any AI acceleration, you must buy the $70 Hailo-8L HAT + NVMe base pushing the total to **~$150 - $180** (~Rp 2,400,000 - Rp 2,880,000). | **$249** (~Rp 3,984,000) for the complete Developer Kit (8GB).       |

### Conclusion for Shopper Analytics
If the system only requires basic spatial mapping (Option A or B) and sending generic XY coordinates to a server, the **Raspberry Pi 5** (or an ESP32) is perfectly adequate and highly cost-effective.

However, if the system requires **on-device sensor fusion** (e.g., running YOLOv11 directly to identify demographics and matching it with the 3D LiDAR point cloud in real-time without extreme lag), the **Nvidia Jetson Orin Nano** is mandatory due to its massive CUDA superiority.

---

## 6. Edge Processing vs. Cloud Processing (Datacomm CLB)

To truly understand the value of our local **Edge Architecture** (Raspberry Pi 5 / Jetson Orin Nano), we must compare it to the traditional **Cloud Architecture** currently being utilized (and proven expensive) by other teams.

### 1,200 m² Store Deployment: Edge vs. Cloud Calculation
Other teams are deploying a heavy cloud-compute architecture hosted by **Datacomm (Datacomm CLB)**, a local cloud server provider in Indonesia, renting massive dual GPU instances to process video streams centrally.

To fairly compare architectures and prove the value of Local Edge, we must standardize the spatial requirement. Based on the 8-meter effective tracking radius of the LiDAR/Camera fusion, a standard **1,200 square meter** retail space is divided into exactly **six distinct 200m² analytical zones**. 
Each 200m² zone strictly requires **3 IP Cameras and 1 Dual-LiDAR array**.
*Total Minimum Hardware per 1,200m² store:* **18 Cameras + 6 LiDARs**.

#### Decentralized Compute Requirements (DeepStream Optimization)
While a basic Python script might only handle 2-3 cameras, deploying **NVIDIA DeepStream SDK** combined with **TensorRT INT8** quantization allows a single **Jetson Orin Nano 8GB (40 TOPS)** to effortlessly process **up to 10 to 12 simultaneous 4 MP camera streams** at 30fps. 

This completely collapses the hardware requirements. To cover an entire 1,200m² store featuring 18 IP cameras, we don't need one Jetson per zone. We only need **two Jetson Orin Nanos** to handle the entire building.

Here is the architectural comparison mapping out exactly what it takes to process a 1,200m² store via the Cloud vs. our proposed Edge setup:

| Metric / Parameter | Our Decentralized Edge (2x Jetson Orin Nanos) | Datacomm CLB Cloud (2x NVIDIA L40S GPUs) |
| :--- | :--- | :--- |
| **Compute Hardware Setup** | **2x** Jetson Orin Nano 8GB (Processing 9 streams each). | **2x** NVIDIA L40S GPUs (Running centrally in the cloud). |
| **CPU / GPU Cores** | **12 CPU Cores** (6 per unit) & **2,048 CUDA Cores** (1024 per unit) | Dedicated Cloud Server CPU & **36,352 CUDA Cores** (18,176 per L40S GPU) |
| **Combined Compute (TFLOPS)** | **~2.56 TFLOPS** (FP32 precision). | **~183.2 TFLOPS** (FP32 precision). |
| **Combined AI Inference (FP16)** | **34 TFLOPS** total (17 FP16 TFLOPS × 2 Units). | **1,466 TFLOPS** total (733 FP16 TFLOPS per L40S card). |
| **Architectural Efficiency** | **Perfectly Scaled.** DeepStream hardware batching maximizes the 17 FP16 TFLOPS per unit. | **Massively Over-provisioned.** Renting ~1,500 FP16 TFLOPS to process a maximum of 18-50 cameras in a store is catastrophic overkill. |
| **Bandwidth / Dependency** | **None.** Processes all 18 cameras locally. Only sends microscopic `(X,Y,Z)` coordinate logs containing shopper IDs to the server. | **Absolute.** Requires massive enterprise internet SLAs capable of uploading 18+ high-definition 4 MP video feeds flawlessly, 24/7. |
| **Privacy / Security** | Extreme. The video footage *never* leaves the physical store network. | Low. Shopper video is continuously streamed to a 3rd-party datacenter. |
| **Compute Deployment Cost** | **One-time compute CAPEX of $498** (~Rp 7.9M) for the 2 Jetson Nanos. | **Recurring compute OPEX of ~Rp 16,000,000 to Rp 20,000,000** every single month. |

---

### Scaling Projections (40 Cameras vs 80 Cameras)

To understand the long-term ROI of the Edge architecture, the following projections model what happens when the computer vision tracking is scaled up to **40 cameras** and **80 cameras**. 

*(Note: The Datacomm CLB cloud team is paying Rp 16-20M/mo for 2x L40S GPUs to handle up "to 100 cameras", so their monthly cloud rental cost remains fixed throughout these scaling phases).*

#### Scenario 1: Scaling to 40 Cameras
At 40 cameras, utilizing DeepStream's capacity to handle 10 streams per unit, we require exactly **4 Jetson Nanos**.

| Metric / Parameter | Our Decentralized Edge (4x Jetson Orin Nanos) | Datacomm CLB Cloud (2x NVIDIA L40S GPUs) |
| :--- | :--- | :--- |
| **Compute Hardware Setup** | **4x** Jetson Orin Nano 8GB | **2x** NVIDIA L40S GPUs |
| **Combined Compute (TFLOPS)** | **~5.12 TFLOPS** (FP32 precision). | **~183.2 TFLOPS** (FP32 precision). |
| **Combined AI Inference (FP16)** | **68 TFLOPS** total (17 FP16 TFLOPS × 4 Units). | **1,466 TFLOPS** total (733 FP16 TFLOPS per L40S card). |
| **Compute Deployment Cost** | **One-time CAPEX of $996** (~Rp 15.9M) for the 4 Jetson Nanos. | **Recurring OPEX of ~Rp 16,000,000 to Rp 20,000,000** every single month. |
| **ROI / Payback Period** | The Edge hardware is **cheaper than a single month** of Datacomm Cloud rental. It pays for itself immediately. | Infinite recurring sunk cost. |

#### Scenario 2: Scaling to 80 Cameras
At 80 cameras, utilizing DeepStream's capacity to handle 10 streams per unit, we require exactly **8 Jetson Nanos**.

| Metric / Parameter               | Our Decentralized Edge (8x Jetson Orin Nanos)                                                       | Datacomm CLB Cloud (2x NVIDIA L40S GPUs)                                  |
| :------------------------------- | :-------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------ |
| **Compute Hardware Setup**       | **8x** Jetson Orin Nano 8GB                                                                         | **2x** NVIDIA L40S GPUs                                                   |
| **Combined Compute (TFLOPS)**    | **~10.24 TFLOPS** (FP32 precision).                                                                 | **~183.2 TFLOPS** (FP32 precision).                                       |
| **Combined AI Inference (FP16)** | **136 TFLOPS** total (17 FP16 TFLOPS × 8 Units).                                                    | **1,466 TFLOPS** total (733 FP16 TFLOPS per L40S card).                   |
| **Compute Deployment Cost**      | **One-time CAPEX of $1,992** (~Rp 31.8M) for the 8 Jetson Nanos.                                    | **Recurring OPEX of ~Rp 16,000,000 to Rp 20,000,000** every single month. |
| **ROI / Payback Period**         | Even at this massive scale, the Edge hardware pays for itself completely in **less than 2 months**. | Infinite recurring sunk cost.                                             |
