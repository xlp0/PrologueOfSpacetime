# Prologue of Spacetime - Project Requirements

## 1. Project Overview
The **Prologue of Spacetime** is an integrated hardware/software curriculum designed to teach **Homotopy Type Theory (HoTT)**, **Logic**, and **Topology** through a physical "game" environment (a Retail Lab / Convenience Store).

## 2. Hardware Requirements (The "Physical Game")

### 2.1 Sensors & Tracking
*   **Kinect Cameras:** 
    *   **Quantity:** 2-3 units.
    *   **Model:** Xbox 360 / V1 (Low cost, <500k IDR).
    *   **Purpose:** Multi-angle volumetric tracking and depth sensing.
*   **Microphones:** 
    *   **Purpose:** Audio triangulation and sound wave detection (Time/Music pillar).
    *   **Integration:** Must support spatial audio processing.

### 2.2 Microcontrollers & IoT
*   **ESP32 Units:**
    *   **Quantity:** "A bunch" (Scalable tracking for objects).
    *   **Purpose:** Connecting physical retail objects to the digital system (IoT).

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
*   **Wi-Fi:**
    *   Custom Antennas for Long-Distance Peer-to-Peer connectivity.

## 3. Software Requirements (The "Engine")

### 3.1 Computer Vision & AI
*   **Multi-Camera Triangulation:** Bundle adjustment and epipolar geometry (OpenCV).
*   **Object Tracking:** YOLOv8 for person detection and Re-ID (Histograms/Features).
*   **Observability:** Tools to visualize "latent" errors (Ghost detection).

### 3.2 Fabrication Software
*   **Non-Planar Slicing:** Software to generate G-code that follows object geometry (curved layers) for strength.
*   **SAM 3D Integration:** AI-powered 3D reconstruction from 2D images (OBJ, GLB, PLY formats) for rapid model creation and prototyping workflows.

### 3.3 Communication
*   **Push Notifications:** VAPID implementation for real-time browser updates.
*   **Zero Trust Logic:** Integration of Identity/Key logic for access control.

## 4. Curriculum Requirements (The "Story")

### 4.1 Framework: The ABC Curriculum
The curriculum follows the **ABC** Structure:
*   **A - Abstract (Grammar/Arithmetic):** The naming system and formal types.
*   **B - Behavior (Logic/Geometry):** Physical movement, space, and time logic.
*   **C - Composition (Rhetoric/Music):** Cross-cutting concerns and complex composition.

### 4.2 The "Revived Quadrivium" Matrix
*   **Arithmetic:** Naming Systems & Type Theory.
*   **Geometry:** Spatial Analysis & Topology.
*   **Music:** Temporal Logic & Frequency.
*   **Astrobiology:** Spacetime integration.

### 4.3 Key Mathematical Concepts
*   **Homotopy Type Theory (HoTT):** Types as Spaces, Equality as Paths.
*   **Cosine Similarity & Pythagoras:** The "Judge" for reconciling space and time scales ($a^2 + b^2 = c^2$).

## 5. Deliverables & Benchmarks
*   **Benchmark:** Must rival/exceed the "Undergraduate Motion Tracking" reference project.
*   **Documentation:** All specs and "Story" content must be version-controlled in this repository.
