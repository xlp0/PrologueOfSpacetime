# Computational Requirements for LiDAR Spatial Mapping

## 1. Executive Summary
This document breaks down the exact mathematical operations and computational capabilities required to process the 3D spatial mapping equations for both a **Single LiDAR** and a **Dual LiDAR** configuration. 

Compared to Computer Vision workloads like YOLO object detection, processing pure geometric LiDAR point clouds requires virtually zero AI acceleration and runs effortlessly on basic CPUs.

---

## 2. Mathematical Operations Per Data Point

For every single laser dot reading ($d, \alpha$) captured by the LiDAR, the system calculates its exact 3D position in the room using the following local-to-global transformation matrix:

$$x = 35 \cos(\theta_S) - d \cos(\alpha) \sin(\theta_S)$$
$$y = 35 \sin(\theta_S) + d \cos(\alpha) \cos(\theta_S)$$
$$z = d \sin(\alpha)$$

Based on the equations above, placing a single dot in 3D space requires:
1.  **3 Trigonometric lookups** (Sine/Cosine)
2.  **6 Multiplications** 
3.  **2 Additions/Subtractions**

This amounts to roughly **11 to 15 floating-point operations (FLOPs)** required to position a single data point.

---

## 3. Computational Load (Single vs. Dual LiDAR)

A standard 360-degree LiDAR unit (specifically the Camsense X2 / YDLidar X2 you purchased) typically spins at 5-8 Hz and samples exactly **3,000 points per second** (3kHz Sample Rate).

### Option A: Single LiDAR System
*   **Data Rate:** 3,000 points per second.
*   **Math Load:** 3,000 points/sec × 15 operations/point = **45,000 FLOPS**.
*   **Total Compute Required:** **~0.000045 GFLOPS**.

### Option B: Dual LiDAR System (Current Architecture)
*   **Data Rate:** 6,000 points per second (2x X2 LiDARs running simultaneously).
*   **Math Load:** 6,000 points/sec × 15 operations/point = **90,000 FLOPS**.
*   **Total Compute Required:** **~0.000090 GFLOPS**.

---

## 4. Hardware Context & Conclusion

To understand how small these processing requirements are, we can compare the LiDAR load against the hardware processing power of industry-standard microcontrollers and AI embedded systems:

| Hardware Unit | Total Compute Capacity | Capacity Used by Dual LiDAR |
| :--- | :--- | :--- |
| **ESP32 Microcontroller** | ~0.02 GFLOPS | ~0.600% |
| **Raspberry Pi 5 CPU** | ~50.0 GFLOPS | ~0.0002% |
| **Jetson Orin Nano (CPU/GPU)** | ~1,280.0 GFLOPS | ~0.000009% |

### Strategic Conclusion
The computational power required to synthesize a Dual-LiDAR point cloud is **microscopically small/negligible**. 

Because this spatial math operates entirely independently of graphical tensor cores, the Jetson Orin Nano's entire 40 TOPS of AI capacity remains 100% available strictly for processing the 4MP video streams (YOLOv8 INT8 inference). The LiDAR processing represents zero bottleneck to the analytical pipeline.
