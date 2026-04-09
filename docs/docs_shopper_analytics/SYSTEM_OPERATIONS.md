# SHOPPER ANALYTICS — System Operations Manual

> **Last Updated:** 2026-04-05  
> **Platform:** Ubuntu 24.04 LTS (x86_64) · `hpserver` · `hpserver.netbird.cloud`

---

## Table of Contents

1. [System Architecture Overview](#1-system-architecture-overview)
2. [Network & Access](#2-network--access)
3. [Starting the System](#3-starting-the-system)
4. [Stopping the System](#4-stopping-the-system)
5. [Camera Configuration](#5-camera-configuration)
6. [Dashboard (Port 5000)](#6-dashboard-port-5000)
7. [Floor Calibration — Matrix Lock](#7-floor-calibration--matrix-lock)
8. [MediaMTX Stream Engine (Port 8888)](#8-mediamtx-stream-engine-port-8888)
9. [AI Inference Pipeline](#9-ai-inference-pipeline)
10. [LiDAR Hardware](#10-lidar-hardware)
11. [NetBird VPN](#11-netbird-vpn)
12. [Troubleshooting](#12-troubleshooting)
13. [File Reference Map](#13-file-reference-map)

---

## 1. System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     SHOPPER ANALYTICS                           │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │  Hikvision   │    │  Hikvision   │    │  Hikvision   │      │
│  │  CAM-1       │    │  CAM-2       │    │  CAM-3       │      │
│  │192.168.100.24│    │192.168.100.34│    │192.168.100.26│      │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘      │
│         │ RTSP/554          │ RTSP/554           │ RTSP/554     │
│         └──────────────┬────┘────────────────────┘             │
│                        ▼                                        │
│            ┌───────────────────────┐                           │
│            │   inference.py ×3     │  ← YOLOv11n ONNX         │
│            │   (per-camera worker) │    People detection       │
│            │   + Homography IPM    │    Pixel → Floor (m)      │
│            └──────────┬────────────┘                           │
│                       │ RTSP re-publish                         │
│                       ▼                                         │
│            ┌───────────────────────┐                           │
│            │      MediaMTX         │  ← mediamtx.yml           │
│            │   HLS on :8888        │    cam-1, cam-2, cam-3    │
│            │   RTSP on :8554       │                           │
│            └──────────┬────────────┘                           │
│            ┌──────────┴────────────┐                           │
│            │  Browser (any device) │  http://<domain_proxy>    │
│            │  Reverse-Proxied 5000 │  or local :5000           │
│            └───────────────────────┘                           │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  LiDAR (ESP32 via /dev/ttyUSB0 @ 921600 baud)          │   │
│  │  → WebSocket broadcast → 3D WebGL Orbit Cloud          │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Key design decisions:**
- **No WebRTC** — streams use HLS over plain TCP (same as Twitch/YouTube). Zero ICE/STUN complexity.
- **ONNX Runtime** — YOLOv11n converted to static ONNX graph for CPU inference without PyTorch overhead.
- **Homography IPM** — converts 2D pixel detections to real-world floor coordinates (metres) using a perspective matrix.

---

## 2. Network & Access

| Resource | Address |
|---|---|
| Dashboard | `http://10.40.14.205:5000` |
| Dashboard (VPN) | `http://100.101.130.220:5000` |
| Dashboard (Domain) | `http://dashboard.yourdomain.com` (Mapped to 5000) |
| HLS Streams | Proxied dynamically over Dashboard Port via `/hls/cam-1/stream.m3u8` |
| MediaMTX Internal API | `http://localhost:9997/v3/` |
| Camera 1 RTSP | `rtsp://admin:***@192.168.100.24:554/Streaming/Channels/101` |
| Camera 2 RTSP | `rtsp://admin:***@192.168.100.34:554/Streaming/Channels/101` |
| Camera 3 RTSP | `rtsp://admin:***@192.168.100.26:554/Streaming/Channels/101` |
| NetBird IP | `100.101.130.220/16` |
| Server hostname | `hpserver.netbird.cloud` |

> [!IMPORTANT]
> Port **8080 is permanently disabled**. The old WebRTC proxy dashboard no longer exists. Use port **5000** exclusively.

---

## 3. Starting the System

### Full System Start (All Components)

Run these two commands — everything else auto-starts:

```bash
# 1. Start the FastAPI dashboard (port 5000)
cd /home/hpserver/SHOPPER-ANALYTICS
nohup uv run python src/dashboard/server.py > dashboard-daemon.log 2>&1 &

# 2. Start MediaMTX + all camera AI workers
nohup uv run hikvision_monitor.py \
    --serve \
    --cameras 192.168.100.24,192.168.100.34,192.168.100.26 \
    --user admin \
    --pass Bait695mash215 \
    > mediamtx-daemon.log 2>&1 &
```

After ~10 seconds, open `http://10.40.14.205:5000/` in your browser.

### What Happens at Boot

```
hikvision_monitor.py
  → writes mediamtx.yml (3 camera paths)
  → launches ./mediamtx mediamtx.yml

mediamtx (on startup, for each path):
  → runs: uv run src/inference.py --url <rtsp> --path cam-N --port <rtsp_port>

inference.py (per camera):
  → loads yolo11n.onnx into ONNX Runtime
  → reads matrix.json for homography corners (if calibrated)
  → connects to camera RTSP stream
  → runs person detection at ~10fps
  → re-publishes annotated stream back to MediaMTX via RTSP
  → POSTs floor coordinates to /api/vision/telemetry (WebSocket broadcast)

server.py:
  → serves index.html, style.css, app.js on :5000
  → opens /dev/ttyUSB0 (LiDAR) in background thread natively
  → hosts internal HLS proxy (/hls/*) mapping external traffic to internal 8888 flawlessly
  → broadcasts LiDAR + vision telemetry over WebSocket /ws to power the 3D WebGL engine
```

---

## 4. Stopping the System

```bash
# Stop everything safely
pkill -f "server.py"
pkill -f mediamtx
pkill -f inference.py
pkill -f hikvision_monitor.py
```

Or to restart cleanly:

```bash
pkill -f mediamtx; pkill -f server.py; pkill -f inference.py; sleep 2
cd /home/hpserver/SHOPPER-ANALYTICS
nohup uv run python src/dashboard/server.py > dashboard-daemon.log 2>&1 &
nohup uv run hikvision_monitor.py --serve \
    --cameras 192.168.100.24,192.168.100.34,192.168.100.26 \
    --user admin --pass Bait695mash215 \
    > mediamtx-daemon.log 2>&1 &
```

---

## 5. Camera Configuration

| ID | IP | Channel | Location |
|---|---|---|---|
| cam-1 | `192.168.100.24` | 101 | Entrance |
| cam-2 | `192.168.100.34` | 101 | Back-Left |
| cam-3 | `192.168.100.26` | 101 | Back-Right |

**Model:** Hikvision DS-2CD2021G1 (3MP, H.264, wide-angle fisheye)

Camera streams are read directly via RTSP at `554`. The `inference.py` worker connects, runs YOLO, and re-publishes the annotated stream back to MediaMTX which converts it to HLS for the browser.

---

## 6. Dashboard (Port 5000)

### Stack
| Component | Tech |
|---|---|
| Backend | FastAPI + Uvicorn + httpx Proxy routing |
| Video Streaming | FastAPI proxy (`/hls/*`) tunneling to internal MediaMTX |
| Real-time Data | WebSocket `/ws` |
| 3D Interface | Three.js WebGL rendering engine parsing arrays on GPU |
| Frontend | Vanilla HTML + CSS + JS |

### Controls

| Button | Action |
|---|---|
| **⌖ MATRIX LOCK** | Enter/exit homography calibration mode |
| **⏻ LI-DAR HALTED/ACTIVE** | Start/stop the LiDAR motor via serial command |

### Responsive Layout
- **>900px** — 3 camera row + telemetry panels side by side
- **≤1100px** — telemetry panels stack vertically  
- **≤640px** — full single-column mobile stack

### Log Files

```bash
tail -f /home/hpserver/SHOPPER-ANALYTICS/dashboard-daemon.log   # Server
tail -f /home/hpserver/SHOPPER-ANALYTICS/mediamtx-daemon.log    # MediaMTX + AI workers
```

---

## 7. Floor Calibration — Matrix Lock

This maps 2D pixel positions in each camera to real-world floor coordinates (X, Y in metres) for the 12m × 3.5m store floor plan.

### Step-by-Step

1. Open `http://10.40.14.205:5000/`
2. Click **[⌖ MATRIX LOCK]** — camera cards turn amber, cursor becomes a zoom icon
3. Click a camera card (**CAM-1**, **CAM-2**, or **CAM-3**)
   - The video expands to fullscreen with a crosshair cursor
4. Click **exactly 4 corners of the far wall** in this order:
   ```
   Top-Left → Top-Right → Bottom-Right → Bottom-Left
   ```
   Yellow dots appear at each click position
5. After the 4th click, title shows **"4 POINTS RECORDED SUCCESSFULLY"**
6. Click **[LOCK 4 POINTS & CLOSE]** — video returns to the grid
7. Repeat for **CAM-2** and **CAM-3**
8. Click **[⌖ MATRIX LOCK]** again to **save** — this writes `matrix.json`

### What Gets Saved

```json
// /home/hpserver/SHOPPER-ANALYTICS/matrix.json
{
    "cam-1": [[x1,y1], [x2,y2], [x3,y3], [x4,y4]],
    "cam-2": [[x1,y1], [x2,y2], [x3,y3], [x4,y4]],
    "cam-3": [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
}
```

Coordinates are in **camera pixel space** (mapped to 1280×720 intrinsic resolution). On save, `inference.py` workers automatically reload this matrix on next start.

> [!NOTE]
> The coordinates are `src_points` for `cv2.getPerspectiveTransform()`. The `dst_points` are the store floor corners in metres `(0,0), (3.5,0), (3.5,12), (0,12)`.

---

## 8. MediaMTX Stream Engine (Port 8888)

### Configuration: `mediamtx.yml`

```yaml
api: yes
paths:
  cam-1:
    runOnInit: uv run src/inference.py --url 'rtsp://...' --path $MTX_PATH --port $RTSP_PORT
    runOnInitRestart: yes
  cam-2:
    runOnInit: uv run src/inference.py --url '...'
    runOnInitRestart: yes
  cam-3:
    runOnInit: uv run src/inference.py --url '...'
    runOnInitRestart: yes
```

> [!IMPORTANT]
> `runOnInitRestart: yes` means if `inference.py` crashes, MediaMTX **automatically restarts it**. This is intentional.

### HLS URL Format

Because port 8888 is generally blocked on externally masked domains, the `server.py` daemon explicitly proxies video streams over the identical port 5000 as the dashboard.

Browser internal URL fetched efficiently:
```
http://<dashboard-domain-or-port-5000>/hls/<cam-id>/stream.m3u8
```

Example inside proxy mapping: `http://10.40.14.205:5000/hls/cam-1/stream.m3u8`

### Verify Streams via MediaMTX API

```bash
# Check which cameras have an active publisher
curl -s http://localhost:9997/v3/paths/list | python3 -m json.tool

# Check HLS muxer status
curl -s http://localhost:9997/v3/hlsmuxers/list
```

---

## 9. AI Inference Pipeline

### File: `src/inference.py`

**Flow per camera:**

```
RTSP Camera Input
      ↓
  cv2.VideoCapture (RTSP)
      ↓
  Frame decode (every 3rd frame to reduce CPU)
      ↓
  YOLOv11n ONNX Runtime (CPUExecutionProvider)
  → Detects class 0 (person) with conf > 0.35
      ↓
  Bounding box foot-point extraction
  → foot_point = (box_center_x, box_bottom_y)
      ↓
  Homography transform (if matrix.json loaded)
  → cv2.perspectiveTransform(foot_point, H)
  → Real-world (X, Y) in metres
      ↓
  POST to http://localhost:5000/api/vision/telemetry
  → WebSocket broadcast → Radar canvas
      ↓
  Annotated frame → RTSP re-publish to MediaMTX
  → HLS conversion → browser video feeds
```

### Model

| Property | Value |
|---|---|
| Model | YOLOv11n |
| Format | ONNX (static graph) |
| Provider | ONNX Runtime CPUExecutionProvider |
| Input | 640×640 |
| Classes | 80 (only class 0 = person used) |
| Confidence threshold | 0.35 |

### Python Path Fix

`inference.py` is launched by MediaMTX in a subprocess. To ensure `src.*` imports resolve correctly, the file includes:

```python
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

This must remain at the top of the file.

---

## 10. LiDAR Hardware

- **Device:** ESP32 via `/dev/ttyUSB0`
- **Baud Rate:** `921600`
- **Protocol:** Newline-delimited ASCII strings

### Telemetry Format

```
<SensorID>,<MotorAngle>,<DistanceMM>,<LidarAngle>
```

Example: `1,120,4000,314`

- **SensorID:** `1` = left sensor, `2` = right sensor
- **DistanceMM:** distance in millimetres (filtered: 100mm–12000mm)
- **LidarAngle:** angle in degrees used for spherical→cartesian trigonometric mapping

### Advanced Motor Sweep Firmware

The hardware natively utilizes a **FreeRTOS Sine-Wave Pendulum Algorithm** deployed in PlatformIO (`main.cpp`). Instead of sweeping at a constant velocity (which introduces mechanical jitter), the servo follows an accelerated sinusoidal curve smoothly mapping `0°-180°` tied natively to `millis()`, ensuring maximum sensor exposure exactly at the physical arc peaks effortlessly.

### Control Commands (via WebSocket → serial)

| Dashboard Button | Serial Command Sent |
|---|---|
| LI-DAR ACTIVE | `start\n` |
| LI-DAR HALTED | `stop\n` |

> [!NOTE]
> The LiDAR **starts in HALTED state** every time the dashboard boots. Click the button to activate it. The server works fine even if no LiDAR is connected.

---

## 11. NetBird VPN

NetBird is installed and connected, enabling secure remote access from any device.

```bash
# Check connection status
netbird status

# Output when connected:
# Management: Connected
# NetBird IP:  100.101.130.220/16
# FQDN:        hpserver.netbird.cloud
# Peers count: 6/10 Connected
```

### Remote Access URLs (via VPN or Secure External Proxy)

```
Dashboard:    http://100.101.130.220:5000
HLS Proxies:  http://100.101.130.220:5000/hls/...
```

> [!NOTE]
> All HLS Video requests dynamically natively funnel through the active Uvicorn Server Port ensuring identical-origin bypass functionality organically! You no longer need to explicitly whitelist Port 8888.

---

## 12. Troubleshooting

### Dashboard shows blank / hangs on load

```bash
# Check if server is running and responding
curl -s --max-time 5 http://localhost:5000/ | head -5

# If no response, restart:
pkill -f server.py; sleep 2
cd /home/hpserver/SHOPPER-ANALYTICS
nohup uv run python src/dashboard/server.py > dashboard-daemon.log 2>&1 &
cat dashboard-daemon.log
```

**Common cause:** `/dev/ttyUSB0` (LiDAR) blocking startup. Fixed in `server.py` — serial now opens in a background thread and will never block the HTTP server.

---

### Cameras show black / no video

```bash
# 1. Confirm cameras are publishing to MediaMTX
curl -s http://localhost:9997/v3/paths/list | grep '"type"'

# 2. Check if inference.py is running
pgrep -c inference

# 3. Check the MediaMTX log
tail -30 /home/hpserver/SHOPPER-ANALYTICS/mediamtx-daemon.log

# 4. If MediaMTX is dead, restart everything:
pkill -f mediamtx
nohup uv run hikvision_monitor.py --serve \
    --cameras 192.168.100.24,192.168.100.34,192.168.100.26 \
    --user admin --pass Bait695mash215 \
    > mediamtx-daemon.log 2>&1 &
```

---

### inference.py crashes with `ModuleNotFoundError: No module named 'src'`

This is fixed. The `sys.path.append(...)` at the top of `inference.py` resolves this permanently. If it reappears, check that `src/inference.py` still starts with:

```python
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
```

---

### `netbird status` hangs

Do NOT run with `sudo`. The daemon socket at `/var/run/netbird.sock` is accessible to regular users:

```bash
netbird status        # ✅ correct
sudo netbird status   # ❌ can deadlock if daemon socket is busy
```

---

### Camera 3 (or any camera) not visible in browser

The dashboard at port 5000 loads HLS streams from `http://<your-hostname>:8888`. If you're accessing the dashboard via a tunnel or different IP, port 8888 must also be accessible from your browser's machine.

Quick test:
```bash
curl http://10.40.14.205:8888/cam-3/stream.m3u8 | head -5
```
Should return `#EXTM3U` — if it does, the stream is live.

---

### `ps aux | grep ...` hangs for a long time

This happens when MediaMTX's `runOnInitRestart: yes` has created many short-lived `inference.py` processes that became zombies. Use `pgrep` instead:

```bash
pgrep -c inference   # fast count
pgrep -c mediamtx
pgrep -c server
```

---

## 13. File Reference Map

```
/home/hpserver/SHOPPER-ANALYTICS/
│
├── hikvision_monitor.py      # Entry point: generates mediamtx.yml, launches mediamtx
├── mediamtx.yml              # Auto-generated by hikvision_monitor.py (do not edit by hand)
├── mediamtx                  # MediaMTX binary v1.9.0
├── matrix.json               # Camera homography corners (written by dashboard UI)
│
├── src/
│   ├── inference.py          # Per-camera YOLO detector + homography + RTSP re-publisher
│   ├── main.py               # (legacy entry point)
│   │
│   ├── dashboard/
│   │   ├── server.py         # FastAPI app (port 5000), WebSocket, REST endpoints
│   │   └── static/
│   │       ├── index.html    # Dashboard structure + calibration modal HTML
│   │       ├── style.css     # Responsive CSS (glass panels, grid layout, animations)
│   │       └── app.js        # HLS.js init, WebSocket, radar canvas, matrix calibrator
│   │
│   ├── homography_fusion/
│   │   ├── homography_calibrator.py   # Compute H matrix from 4-point correspondences
│   │   └── bev_projection.py          # Bird's-eye-view projection + NMS clustering
│   │
│   ├── analytics/            # Dwell time, zone counting (future)
│   ├── camera/               # Camera utility helpers
│   └── training/             # Model fine-tuning scripts
│
├── docs/
│   ├── SYSTEM_OPERATIONS.md  # ← This file
│   ├── trinocular_math_and_logic.md
│   ├── PIPELINE_8080.md      # (legacy, kept for reference)
│   └── ...
│
├── dashboard-daemon.log      # FastAPI server stdout
└── mediamtx-daemon.log       # MediaMTX + inference.py workers stdout
```

### Key API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves the dashboard HTML |
| `GET` | `/static/*` | CSS, JS, assets |
| `GET` | `/api/lidar/toggle?state=start\|stop` | Start/stop LiDAR motor |
| `POST` | `/api/vision/telemetry` | Receive floor coords from inference.py |
| `POST` | `/api/vision/calibrate` | Save homography matrix from UI clicks |
| `WS` | `/ws` | Real-time LiDAR + vision broadcast to browser |

---

*Generated: 2026-04-05 — SHOPPER ANALYTICS System v1.0*
