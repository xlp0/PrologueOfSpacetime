# Network Access Guide

This document details how any other computer, phone, or tablet on the same local network (LAN) can access the live dashboard and raw camera streams processing on the `hpserver` machine.

## Server IP Address
The primary IP address for the edge AI server (`hpserver`) is:
**`192.168.100.29`**

---

## 1. Web Dashboard (Live Heatmaps & Radar)

The primary interface containing the floorplan radar, LiDAR visualization, and the live camera feeds is running on a standard web server on **Port 5000**.

*   **URL:** `http://192.168.100.29:5000`
*   **Requirements:** Any modern web browser (Chrome, Firefox, Safari, Edge).
*   **Access Level:** Full access to view real-time tracks, trailing, and embedded camera feeds.

---

## 2. Direct Camera Stream Access (No UI)

If you have a 3rd-party NVR or simply want to view the raw camera streams directly without the web dashboard, the server automatically re-broadcasts the streams in three different protocols.

The available stream paths are:
*   `cam-1` (Entrance)
*   `cam-2` (Back-Left)
*   `cam-3` (Back-Right)

### A. RTSP (For VLC / OBS / NVR Systems)
RTSP is the most universally supported protocol for dedicated camera software.
*   **Port:** `8554`
*   **Software Requirements:** VLC Media Player, OBS Studio, or any NVR software.
*   **Connection URLs:**
    *   `rtsp://192.168.100.29:8554/cam-1`
    *   `rtsp://192.168.100.29:8554/cam-2`
    *   `rtsp://192.168.100.29:8554/cam-3`

### B. HLS (HTTP Live Streaming)
HLS is best for embedding the raw camera feed into standard web pages or viewing natively on mobile devices (like iOS Safari). It has a slight delay (~2-3 seconds) but is extremely stable over poor wifi connections.
*   **Port:** `8888`
*   **Software Requirements:** Safari, Edge, or web video players (like Video.js).
*   **Connection URLs:**
    *   `http://192.168.100.29:8888/cam-1`
    *   `http://192.168.100.29:8888/cam-2`
    *   `http://192.168.100.29:8888/cam-3`

### C. WebRTC (Ultra-Low Latency)
WebRTC provides the lowest possible latency (< 0.5 seconds) for real-time monitoring directly in the browser.
*   **Port:** `8889`
*   **Requirements:** Chrome or Firefox.
*   **Connection URLs:**
    *   `http://192.168.100.29:8889/cam-1`
    *   `http://192.168.100.29:8889/cam-2`
    *   `http://192.168.100.29:8889/cam-3`

---

## Firewall Considerations
If for any reason you are unable to connect from another machine, ensure that `ufw` or `iptables` on `hpserver` allows incoming traffic natively on TCP ports `5000`, `8554`, `8888`, and `8889`. 

Currently, the server binds to `0.0.0.0` securely organically smoothly flawlessly, opening these ports immediately on boot natively automatically.
