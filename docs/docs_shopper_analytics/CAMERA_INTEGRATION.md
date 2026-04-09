# Shopper Analytics - Camera Integration Guide

This document details the hardware configuration, stream processing, and AI models utilized by the Shopper Analytics system.

## 📷 IP Camera Hardware

The system actively monitors a cluster of Hikvision network cameras. By default, these cameras encode their video streams using H.265 (HEVC), which is highly efficient but incompatible with standard web browsers.

### Camera Credentials
* **Username:** `admin`
* **Password:** `Bait695mash215`

### Camera Network Array
1. **Camera 1:** `192.168.100.24`
2. **Camera 2:** `192.168.100.34`
3. **Camera 3:** `192.168.100.26`

**RTSP Stream Format:**
`rtsp://admin:Bait695mash215@<IP_ADDRESS>:554/Streaming/Channels/101`
*(Note: Channel `101` represents the high-resolution Main Stream. Channel `102` is the Sub-Stream).*

---

## 🌐 WebRTC Streaming Infrastructure (`hikvision_monitor.py`)

Because Hikvision cameras broadcast in raw H.265, they cannot be natively viewed in Chrome or Firefox. To solve this without modifying physical camera settings, the project includes an on-the-fly transcoding proxy.

### How it Works
1. When you run `make serve CAMERAS=192.168.100.24,192.168.100.34,192.168.100.26`, the system boots up the **MediaMTX** engine.
2. The proxy dynamically executes `FFmpeg` to pull the H.265 feeds.
3. FFmpeg transcodes the streams into universal **H.264** video in real-time.
4. MediaMTX encapsulates the H.264 video into an ultra-low latency **WebRTC** format.
5. The dashboard at `http://<ZeroTier-IP>:8080/` connects to these WebRTC channels and embeds them seamlessly.

---

## 🧠 AI Models (YOLO)

The `SHOPPER-ANALYTICS` suite is equipped with state-of-the-art computer vision models from Ultralytics to process the camera feeds. The following weights are currently available in the project root:

| Model File | Use Case | Size / Speed |
| :--- | :--- | :--- |
| `yolov8n.pt` | General object detection (people, carts, items) | Nano (Fastest, low latency) |
| `yolov8m.pt` | General object detection (higher accuracy) | Medium |
| `yolo11n.pt` | Next-generation object detection | Nano (Fastest) |
| `yolo11n-pose.pt` | Human pose estimation & tracking | Nano (Tracks skeletal movements and interactions) |

These `.pt` models are inherently designed to ingest the raw or transcoded frames pulled from the IP cameras via standard OpenCV `VideoCapture` protocols (as seen in `monitor_ip_cameras.py`).
