# Prologue of Spacetime - Project Requirements

## 1. Project Overview
The **Prologue of Spacetime** is an integrated hardware/software curriculum designed to teach **Homotopy Type Theory (HoTT)**, **Logic**, and **Topology** through a physical "game" environment (a Retail Lab / Convenience Store). It operationalizes the classical **Trivium** (Grammar, Logic, Rhetoric) and **Quadrivium** (Arithmetic, Geometry, Music, Astrobiology) as a unified computational framework, verified through the **Cubical Logic Model (CLM)** and powered by the **GASing Methodology**.

## 2. Hardware Requirements (The "Physical Game")

### 2.1 Sensors & Tracking
*   **Kinect Cameras:** 
    *   **Quantity:** 2-3 units.
    *   **Model:** Xbox 360 / V1 (Low cost, <500k IDR).
    *   **Purpose:** Multi-angle volumetric tracking and depth sensing.
*   **IP Cameras (Hikvision/Network Cameras):**
    *   **Purpose:** Real-time video stream processing for computer vision, RTSP protocol integration, multi-camera spatial tracking.
    *   **Learning Focus:** Understanding network protocols, H.264/H.265 encoding, homography transformation for 2D-to-3D coordinate mapping.
*   **LiDAR Sensors (360° 2D LiDAR):**
    *   **Purpose:** Distance measurement and spatial point cloud generation, servo-based sweeping mechanisms.
    *   **Learning Focus:** Spherical-to-Cartesian coordinate transformation, real-time sensor fusion, trigonometric spatial mapping.
*   **Microphones:** 
    *   **Purpose:** Audio triangulation and sound wave detection (Time/Music pillar).
    *   **Integration:** Must support spatial audio processing.

### 2.2 Microcontrollers & IoT
*   **ESP32 Units:**
    *   **Quantity:** "A bunch" (Scalable tracking for objects).
    *   **Purpose:** Connecting physical retail objects to the digital system (IoT), LiDAR servo control, serial communication protocols.
    *   **Learning Focus:** UART communication, FreeRTOS task scheduling, hardware PWM for servo control.

### 2.3 Robotics & Drones
*   **Drones:**
    *   **Type:** Small, programmable quadcopters (e.g., similar to "Joshua Bird" demo).
    *   **Purpose:** Demonstrating PID control, flight formation, and motion capture integration.

### 2.4 Fabrication
*   **3D Printer:**
    *   **Features:** Must have an **Enclosure** (e.g., Creality K1/Ender with box).
    *   **Materials:** ABS / PETG (High durability for structural parts).
    *   **Required Prints:**
        *   Drone chassis/parts.
        *   Ceiling mounts for Kinects.
        *   Cabinet/Rack for server equipment.
    *   **Workflow Integration:** Supports **SAM 3D** (Segment Anything Model 3D) for AI-powered image-to-3D conversion, enabling rapid model generation from photographs for prototyping and fabrication.

### 2.5 Infrastructure
*   **Server:** "White Little Computer" (Cubic Form Factor).
    *   **Network:** 2.5Gbps Ethernet.
    *   **Storage:** 48TB NAS/SSD capability.
    *   **Role:** Local data processing, "Game Server."
*   **Edge AI Computing (NVIDIA Jetson / Raspberry Pi):**
    *   **Purpose:** On-device AI inference, multi-stream video processing, edge-to-cloud architecture.
    *   **Learning Focus:** DeepStream SDK, TensorRT optimization, edge compute strategy, bandwidth reduction through local processing.
*   **Wi-Fi:**
    *   Custom Antennas for Long-Distance Peer-to-Peer connectivity.

## 3. Software Requirements (The "Engine")

### 3.1 Computer Vision & AI
*   **Multi-Camera Triangulation:** Bundle adjustment and epipolar geometry (OpenCV).
*   **Object Tracking:** YOLOv8/YOLOv11 for person detection and Re-ID (Histograms/Features).
*   **Homography & Inverse Perspective Mapping:** 2D pixel-to-3D floor coordinate transformation using perspective matrices.
*   **ONNX Runtime:** Model optimization for CPU inference, static graph execution for edge devices.
*   **Sensor Fusion:** Combining RGB camera data with LiDAR point clouds for spatial tracking.
*   **Observability:** Tools to visualize "latent" errors (Ghost detection).

### 3.2 Fabrication Software
*   **Non-Planar Slicing:** Software to generate G-code that follows object geometry (curved layers) for strength.
*   **SAM 3D Integration:** AI-powered 3D reconstruction from 2D images for rapid prototyping:
    *   **Input Formats:** JPEG, PNG, WebP (2D photographs, sketches, concept art)
    *   **Output Formats:** STL, OBJ, GLB, PLY (3D meshes ready for slicing)
    *   **Use Cases:** 
        - Character portraits → Game miniatures
        - Terrain photos → Dungeon tiles
        - Hand sketches → Rapid physical prototypes
    *   **Pipeline:** Image → SAM 3D segmentation/reconstruction → 3D mesh → Slicer → G-code → Printer → Physical object
    *   **Pedagogical Value:** Demonstrates compositional morphisms—each stage preserves essential properties while transforming dimensionality

### 3.3 Communication
*   **Streaming Protocols:** RTSP, HLS, WebRTC for low-latency video transmission.
*   **Media Servers:** MediaMTX for stream transcoding and multi-protocol broadcasting.
*   **WebSocket:** Real-time bidirectional communication for sensor telemetry and tracking data.
*   **Push Notifications:** VAPID implementation for real-time browser updates.
*   **Zero Trust Logic:** Integration of Identity/Key logic for access control.

## 4. Curriculum Requirements (The "Story")

### 4.1 Framework: The ABC Curriculum (Trivium × Quadrivium)
The curriculum follows the **ABC** Structure, mapped to the classical Trivium:
*   **A - Abstract (Grammar/Arithmetic):** The naming system and formal types. → **MCard** (Atomic knowledge storage)
*   **B - Behavior (Logic/Geometry):** Physical movement, space, and time logic. → **PCard** (Recursive composition)
*   **C - Composition (Rhetoric/Music):** Cross-cutting concerns and complex composition. → **VCard** (Value representation)

> **Implementation Order (Reverse Trivium):** Rhetoric First (Why) → Logic Second (How) → Grammar Last (What). Motivation precedes abstraction.

### 4.1.1 Board Games as Pedagogical Microcosms

Each game session is **authenticated**, **logged** (append-only move history), and **verifiable** (state reconstruction). Games embody the Reverse Trivium: motivation through competition (Rhetoric), pattern discovery through play (Logic), formal study after experience (Grammar).

### 4.2 The "Revived Quadrivium" Matrix
*   **Arithmetic:** Naming Systems, Type Theory, Zero Trust as Arithmetic Foundation.
*   **Geometry:** Spatial Analysis, Topology, HoTT (Types as Spaces).
*   **Music:** Temporal Logic, Frequency, Accounting as Temporal Coordination.
*   **Astrobiology:** Spacetime integration, Consciousness as Scale-Free Awareness.

### 4.3 Key Mathematical & Theoretical Concepts
*   **Homotopy Type Theory (HoTT):** Types as Spaces, Equality as Paths, Propositions as Types, Higher Inductive Types, Univalence Axiom.
*   **Cubical Logic Model (CLM):** Three-dimensional framework (Abstract Spec + Concrete Impl + Balanced Exp) as Universal Meta-Language. Scale-free, Context-Sensitive, Domain-Neutral.
*   **Single Source of Truth (SSOT):** SSOT as *Protocol* (verification procedure), not static repository. Follows 道生一 (Directionality → Unity). Procedural, Context-Explicit, Verifiable, Adaptive, Composable.
*   **Agentic Trinitarianism:** Miner-Coder-Trader Triad for value creation. Rooted in Computational Trinitarianism (Harper) and Curry-Howard-Lambek Isomorphism.
*   **Pentadic Threshold:** Five-fold dynamic layer: 五行 (Wǔxíng), Five ML Tribes, Big Five of Reverse Mathematics. Each chapter carries a Logical Depth Badge ($RCA_0$ through $\Pi^1_1\text{-}CA_0$).
*   **Universality:** Universal Properties (Initial Object, Terminal Object, Coproduct, Product, Identity) as compositional foundations across all domains.
*   **Cosine Similarity & Pythagoras:** The "Judge" for reconciling space and time scales ($a^2 + b^2 = c^2$).

### 4.4 Foundational Pedagogical Principles
*   **GASing Methodology:** Gampang (Easy/Grammar), Asyik (Fun/Logic), Menyenangkan (Enjoyable/Rhetoric). GASing as Adaptive Truth Protocol.
*   **Hoare Logic:** Every interaction as a Hoare Triple $\{P\} C \{Q\}$, operationalized by CLM.
*   **Kenosis (Self-Emptying):** Empty Schema Principle enables Universal Namespace.
*   **Zero Trust:** Verification-first architecture; learning is verified cryptographically.

## 5. Deliverables & Benchmarks
*   **Benchmark:** Must rival/exceed the "Undergraduate Motion Tracking" reference project.
*   **Documentation:** All specs and "Story" content must be version-controlled in this repository.
*   **CLM Compliance:** Every chapter must produce an MVP Card indexed as a CLM triple (Spec, Impl, Exp).
*   **Logical Depth Badges:** Each chapter must display its Logical Depth level (Big Five of Reverse Mathematics).
*   **Pentadic Coverage:** Each chapter must cycle through all five Wuxing phases (Explore, Create, Consolidate, Critique, Reflect).
