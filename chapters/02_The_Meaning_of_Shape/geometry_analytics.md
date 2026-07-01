# Spatial Tracking: Geometry in Practice

> *"The floor is not just space—it is a coordinate system waiting to be calibrated."*

## Overview

Spatial tracking demonstrates **Geometry** (Number in Space) through coordinate transformation. This operationalizes the core geometric concepts from Chapter 02 by transforming 2D observations into 3D real-world coordinates, combining multiple observation points into a unified spatial model.

**Implementation Hardware**:
- **IP Cameras**: Hikvision DS-2CD2021G1 (2MP, 4mm lens, H.265+)
- **LiDAR**: Camsense X2 or YDLidar X2/X2L (360° scanning)
- **Microcontroller**: ESP32 DevKit for LiDAR servo control
- **AI Processing**: YOLOv8n/YOLOv11n via ONNX Runtime
- **Streaming**: MediaMTX for multi-protocol video distribution

## The Geometric Foundation

### The Mapping Challenge
How do we map observations (pixels) to reality (meters)? This is the **fundamental problem of perception** that every autonomous system must solve through geometric transformation.

## Homography: The Bridge Between Spaces

### Understanding Homography
**Homography** (Inverse Perspective Mapping) transforms a perspective view into a flat, top-down view. It bridges **image space** and **world space**.

### The Transformation
Given a point in pixel coordinates $(u, v)$, the homography matrix $H$ (3×3) maps it to world coordinates $(X, Y)$:
$$
\begin{bmatrix} X \\ Y \\ 1 \end{bmatrix} = H \begin{bmatrix} u \\ v \\ 1 \end{bmatrix}
$$

### Calibration Through Correspondence
To compute $H$, we establish **four known correspondences** between image points and real-world positions. The system learns the camera's perspective through these known points—this is **learning by example**.

## Multi-Camera Fusion

### Coordinate Unification
Each camera has its own homography matrix. When multiple cameras observe the same space:
1. Each camera transforms its pixel observations to world coordinates
2. Observations within a spatial threshold are recognized as the same entity
3. Multiple observations merge into a unified position

This is **spatial consensus**: Multiple observers converge on the same physical location through coordinate proximity.

## LiDAR: Complementary Spatial Sensing

### Dual Modalities
Cameras provide appearance (RGB) while LiDAR provides precise distance. Together they form a complete spatial perception system.

**LiDAR Hardware**:
- **Sensors**: Camsense X2 (primary), YDLidar X2/X2L, RPLidar A1/A2
- **Servo**: MG996R metal gear for 180° sweep
- **Controller**: ESP32 with FreeRTOS for real-time coordination
- **Interface**: UART at 921600 baud

### Spherical to Cartesian Transformation
LiDAR outputs polar coordinates $(r, \theta, \phi)$ which we convert to Cartesian $(x, y, z)$:
$$
\begin{aligned}
x &= r \cdot \cos(\phi) \cdot \cos(\theta) \\
y &= r \cdot \sin(\phi) \\
z &= r \cdot \cos(\phi) \cdot \sin(\theta)
\end{aligned}
$$

### Sensor Fusion
Combining camera and LiDAR observations creates verified spatial positions through multi-modal consensus.

## Pedagogical Connections

### HoTT: Types as Spaces
In **Homotopy Type Theory**, a **Type** is a **Space** and a **Term** is a **Point** in that space.

The Shopper Analytics system operationalizes this:
- **Pixel Space**: Type `Image` with terms $(u, v)$
- **World Space**: Type `Floor` with terms $(X, Y)$
- **Homography**: A **morphism** (function) from `Image → Floor`

The calibration process is **proof construction**: We prove that the homography matrix correctly maps image points to floor points by verifying known correspondences.

### Universal Properties: Products and Coproducts
Multi-camera fusion demonstrates **Products** ($A \times B$):
- Camera 1's observation **AND** Camera 2's observation
- The **intersection** of their views is the consensus

Choosing between cameras demonstrates **Coproducts** ($A + B$):
- Camera 1's view **OR** Camera 2's view
- The **union** of their coverage is the total observable space

### Cubical Logic Model (CLM)
The entire system is a CLM triple:
- **Spec**: "Map pixels to floor coordinates"
- **Impl**: Homography matrix computation and application
- **Exp**: Verification by clicking known floor points and checking accuracy

## Learning Exercises

### Exercise 1: Calibration Process
Practice the four-point correspondence method:
1. Identify known reference points in image space
2. Map them to world coordinates
3. Observe how the homography matrix emerges from these correspondences
4. Verify accuracy through test observations

### Exercise 2: Coordinate Transformation
Apply homography transformation:
1. Normalize pixel coordinates relative to image dimensions
2. Apply the transformation matrix
3. Interpret the resulting world coordinates

### Exercise 3: Multi-Camera Consensus
Explore spatial clustering:
1. Calculate Euclidean distance between observations
2. Apply threshold-based clustering
3. Determine merged positions from multiple observations

## Advanced Concepts

### Non-Maximum Suppression
Merging multiple observations uses **spatial clustering**:
1. Compute pairwise distances between detections
2. Cluster observations within threshold
3. Output cluster centroids as unified positions

This demonstrates the same mathematical principles used in machine learning for grouping similar data points.

### Thermodynamic Verification
From Chapter 04: **verification costs energy**. Every observation—detection, transformation, clustering—requires computational work. This demonstrates **Landauer's Principle**: information extraction has a minimum energy cost.

### Scale-Free Architecture
The geometric principles remain constant across scales. The solution scales through **composition**: adding more homography matrices without redesigning the fundamental approach.

## Related Chapters
- **Chapter 01: The Value of Counting** - Computational cost accounting (FLOPs, energy)
- **Chapter 04: The Truth of Observation** - Multi-observer consensus and verification
- **Chapter 06: Network Pathfinding** - Data routing from cameras to dashboard
- **Chapter 09: Counting Water** - Discrete sampling and quantization (pixel grid)

## Further Reading
- Mathematical derivations in `docs/shopper_analytics/trinocular_math_and_logic.md`
- Hardware integration guides in `hardware/ip_camera/` and `hardware/lidar/`
