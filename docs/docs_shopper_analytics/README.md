# Shopper Analytics — Documentation Index

Welcome to the documentation directory for the Shopper Analytics system. This folder contains all the technical guides, hardware specifications, networking topologies, and architecture explanations created throughout the development of this project.

## Where to start for Deployment & Operations?

If you are just cloning this repository and want to run the system, deploy to a new machine, or access the dashboard, read these files first:

1. **[SYSTEM_OPERATIONS.md](./SYSTEM_OPERATIONS.md)**
   **Read this to start the system.** Contains the full startup commands for Python, MediaMTX, the WebSocket servers, the dashboard, and debugging tools. It is the master runbook.

2. **[NETWORK_ACCESS_GUIDE.md](./NETWORK_ACCESS_GUIDE.md)**
   **Read this to share the streams.** Explains how other computers, tablets, and mobile phones on the Local Area Network (LAN) can access the live tracking dashboard, the HLS streams, and the RTSP feeds.

3. **[HARDWARE_AND_FLOP_BENCHMARKS.md](./HARDWARE_AND_FLOP_BENCHMARKS.md)**
   **Read this for scaling to a stronger machine via `.env`.** Contains the total CPU processing output of the AI pipeline, but most importantly, it handles **System Configuration**. It explains how to use the `.env` file to scale the AI model (from `yolo11n` to `yolo11x`) and remap the physical RTSP camera URLs when migrating hardware.

---

## Complete Documentation Reference

Below is a breakdown of all documentation files stored in this repository:

### Core Architecture & Deployment
*   **`SYSTEM_OPERATIONS.md`** - Master startup guide and workflow operations.
*   **`HARDWARE_AND_FLOP_BENCHMARKS.md`** - CPU payload metrics, `.env` file configuration limits, and floorplan tracking coverage map.
*   **`NETWORK_ACCESS_GUIDE.md`** - Host machine IP addresses and cross-device portal access (Port 5000, 8554, 8888, 8889).
*   **`PIPELINE_8080.md`** - Legacy details on the initial data pipeline handling bounding box feeds natively via sockets, and the initial integration of MediaMTX.
*   **`docker_setup_guide.md`** - Legacy/alternative constraints attempting to containerize this pipeline visually.

### Hardware & Sensors
*   **`hardware_explanation.md`** - Deep exploration of the i5-2400 edge-server constraints and why PyTorch NNPACK crashes occur.
*   **`edge_compute_strategy.md`** - Why the Pure-Python IoU Tracker was introduced to cleanly sidestep native library segfaults.
*   **`CAMERA_INTEGRATION.md`** - Multi-camera optical tracking constraints.
*   **`hikvision_ipcamera_access_guide.md`** - Setup credentials, RTSP formatting, and native configurations for the Hikvision network cameras.
*   **`hikvision_ds2CD2021g1_specs.md`** - Datasheet analysis for one of the primary optical lenses.
*   **`spc_bc1_3mp_specs.md`** - Datasheet for the secondary SPC IP optics.
*   **`lidar_compute_requirements.md`** - How the 360-degree serial LiDAR arrays operate synchronously alongside optical streams.
*   **`kinect_features.md`** - Notes on initial depth camera (Kinect RGB-D) potential capabilities natively.

### Maths & Logic 
*   **`trinocular_math_and_logic.md`** - Breakdown of the `homography_fusion` component, which maps 2D camera pixel coordinates (u,v) into real-world 3D physical meters natively.
*   **`AI_OPTIMIZATION_LOG.md`** - Details regarding PyTorch threading constraints, GIL blocking factors with `ffmpeg`, and how the team achieved stable 2fps tracking natively.
*   **`advanced_workarounds.md`** - Quick-reference edge cases.
*   **`mac_troubleshooting.md`** - Dev-environment workarounds effectively bridging Ubuntu dependencies into local MacOS spaces natively.
