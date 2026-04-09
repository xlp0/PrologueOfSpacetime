# IP Camera Systems for Spatial Tracking

## Learning Objectives

Understanding network-based video streaming, computer vision pipelines, and spatial coordinate transformation through real-world retail analytics applications.

## Core Concepts

### 1. Network Video Protocols
- **RTSP (Real-Time Streaming Protocol)**: Industry-standard protocol for camera stream access
- **H.264/H.265 Encoding**: Video compression for bandwidth efficiency
- **Multi-Protocol Broadcasting**: HLS, WebRTC for browser compatibility

### 2. Homography & Inverse Perspective Mapping
- **2D-to-3D Transformation**: Converting pixel coordinates to real-world floor positions
- **Perspective Matrix Calibration**: Four-point correspondence for camera-to-floor mapping
- **Multi-Camera Fusion**: Combining overlapping camera views into unified coordinate space

### 3. Real-Time Computer Vision
- **YOLO Object Detection**: Person detection and bounding box extraction
- **Foot-Point Extraction**: Identifying ground contact points from bounding boxes
- **Spatial Tracking**: Persistent ID assignment across camera boundaries

## Hardware Components

### Network Cameras
- **Brand/Model**: Hikvision DS-2CD2021G1 (2MP IP Bullet Camera)
- **Purpose**: RGB video input for computer vision processing
- **Key Features**: RTSP stream support, H.264/H.265 encoding, 4mm fixed lens, 120 dB WDR, 30m IR night vision, 12V DC power
- **Learning Focus**: Network configuration, RTSP stream access, credential management, H.265+ compression

### Mounting & Calibration
- **Physical Placement**: Strategic positioning for coverage overlap
- **Calibration Process**: Four-corner marking for homography matrix generation
- **3D Printed Mounts**: Custom brackets designed and fabricated for optimal angles

## Software Integration

### Stream Processing Pipeline
```
RTSP Camera → OpenCV VideoCapture → YOLO Inference → 
Homography Transform → Floor Coordinates → WebSocket Broadcast
```

### Key Technologies
- **OpenCV**: Video capture and image processing
- **YOLO Models**: YOLOv8n, YOLOv8m, YOLOv11n, YOLOv11n-pose for person detection
- **ONNX Runtime**: Optimized model inference for CPU-bound servers
- **MediaMTX**: Stream transcoding and multi-protocol broadcasting server
- **FastAPI/WebSocket**: Real-time coordinate broadcasting
- **Python**: Primary implementation language for AI pipeline

## Pedagogical Value

### Geometry (Space)
- Understanding perspective projection and inverse mapping
- Spatial reasoning through coordinate system transformations
- Multi-view geometry and triangulation principles

### Astrobiology (Spacetime)
- Real-time tracking as temporal-spatial integration
- Observer position affecting measurement (parallax)
- Sensor fusion combining multiple observation points

### Zero Trust Architecture
- Camera network segmentation and access control
- Credential management and secure stream access
- Local processing before cloud transmission (privacy by design)

## Related Chapters
- **Chapter 02: The Meaning of Shape** - Spatial coordinate systems and transformations
- **Chapter 04: The Truth of Observation** - Multi-observer consensus and verification
- **Chapter 06: Network Pathfinding** - Data routing and stream distribution
