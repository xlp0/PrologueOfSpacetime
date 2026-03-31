# Edge Compute Performance Strategy

## 1. The Core Limitation
*   **Goal:** Eliminate 1 Terabyte of continuous video stream bandwidth per store.
*   **Constraint:** 100 cameras running the full continuous YOLO + DINOv2 pipeline requires **~1,436 FP16 TFLOPS**. 
*   **Capacity:** A single Jetson Orin Nano provides **40 INT8 TOPS (17 FP16 TFLOPS)**.

## 2. Continuous Module Compute (Edge vs Cloud)
Heavy continuous load breaks local limits and must be pushed to the Cloud. The Edge only tracks and crops bounding boxes to save bandwidth.

| Module | Execution Rate | Model Cost | Total Load (100 Cams) | Host |
| :--- | :--- | :--- | :--- | :--- |
| **Person & Product Tracking (Deep SORT)** | 20 FPS | 10 BFLOPs | ~20 TFLOPS | **Edge (Local)** |
| **Person & Product Detection (YOLO26 XL)** | 20 FPS | 388 BFLOPs | ~776 TFLOPS | **Cloud** |
| **Person ReID (DINOv2 Giant)** | 20 FPS | 320 BFLOPs | ~640 TFLOPS | **Cloud** |

*Note: Since the total continuous tracking load is ~20 TFLOPS, we only need **ONE** Jetson Orin Nano (40 INT8 TOPS) running locally per store. The Cloud receives only tiny image crops, reducing bandwidth enormously.*

## 3. One-Time Module Compute (Edge)
Triggered only for new shoppers (estimating 50 per hour per camera = 0.0139 FPS).

| Module | Execution Rate | Model Cost | Total Load (100 Cams) | Host |
| :--- | :--- | :--- | :--- | :--- |
| **Face Detection (YOLO26 XL)** | 0.0139 FPS | 194 BFLOPs | ~0.26 TFLOPs | **Edge** |
| **Face Alignment (Landmarks)** | 0.0139 FPS | 5 BFLOPs | ~0.01 TFLOPs | **Edge** |
| **Gender & Age Class. (DINOv2 Giant)** | 0.0139 FPS | 640 BFLOPs | ~0.88 TFLOPs | **Edge** |
| **Total One-Time Load** | **0.0139 FPS** | **--** | **~1.16 TFLOPS** | **--** |

### Off-Time Optimization Strategy
Does a retail store need real-time face/gender alignment instantly? **No.** 
We can queue captured face images locally and process this ~1.16 TFLOPS workload overnight during store "Off-Time" (when 0 TFLOPS are being used for tracking) to maximize edge hardware efficiency without interrupting daytime performance.

## 4. Hardware Unit Performance & Alternatives

### NVIDIA Edge Device Comparison Matrix
We must select strictly new, enterprise-grade NVIDIA Edge hardware. Below is the direct comparison for individual edge nodes to determine the optimal price-to-performance ratio for a 100-camera store.

| Device | Memory | Compute (INT8) | Compute (FP16) | Power Draw | Hardware Price (New) | Deployment Tradeoffs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Jetson Orin Nano** | 8GB | 40 TOPS | 17 TFLOPS | 15W | **$249** | Our optimal baseline. A single unit easily handles the 20 TFLOPS tracking load for all 100 cameras. |
| **Jetson Orin NX** | 16GB | 100 TOPS | ~42 TFLOPS | 25W | **$599** | Complete overkill for the 20 TFLOPS tracking load, but provides massive headroom for future expansion. |
| **Jetson AGX Orin** | 64GB | 275 TOPS | ~137 TFLOPS | 60W | **$1,999** | Unnecessary expense. Too powerful for basic tracking, yet too weak to handle the massive 1,436 TFLOPS Cloud pipeline. |

**Verdict:** The **Jetson Orin Nano 8GB** ($249) is the absolute perfect fit. We only need **ONE** Jetson to process the 10 BFLOPs/frame human and product tracking pipeline for a 100-camera store, making it incredibly cost-effective while solving the bandwidth crisis.

## 5. Final Architectural Conclusion
By deploying Jetson edge hardware on-site, we achieve our primary goals:
1. **Bandwidth Reduction:** A single Jetson Orin Nano processes the raw video stream locally to perform Deep SORT tracking, cropping out only the necessary bounding boxes. By transmitting these tiny semantic patches instead of full video streams, bandwidth usage is **significantly decreased**, easily bypassing the 1 TB/store/month limitation.
2. **Compute Efficiency:** We only need one low-power Jetson Orin Nano per store to handle the local tracking and overnight batch workloads. This allows us to safely and cheaply offload the massive YOLO26/DINOv2 continuous detection requirements to the centralized Datacomm CLB Cloud.
