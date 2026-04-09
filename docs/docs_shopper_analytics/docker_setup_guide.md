# Docker USB/IP "Hack" for Kinect v2 on M4

**WARNING: This is an advanced, experimental procedure.**
It requires installing System Tools (Docker, Rust) and running complex terminal commands.

## Prerequisites
1.  **Docker Desktop 4.35.0+**: Essential. Older versions do not support USB/IP.
2.  **Rust Toolchain**: Required to run the USB/IP host server.
    *   Install: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`
3.  **Kinect v2 Adapter**: Connected and powered.

## Step 1: Install Host USB/IP Server
On your Mac (Host Terminal), we need a tool to "share" the USB device.
```bash
# Clone the Rust USBIP implementation
git clone https://github.com/jiegec/usbip.git
cd usbip
cargo build --release
# The binary will be at ./target/release/usbip
```

## Step 2: Run the USB/IP Server (Mac Host)
The Rust tool we built acts as the server. It exposes *all* your USB devices to the network.
Open a terminal in the `ShopAnalytics` folder and run:
```bash
# This command will hang/run forever. Keep this terminal open!
cd usbip
cargo run --release --example host
```

## Step 3: Run the Docker Container (New Terminal)
Open a **New Terminal Window** and run the Linux environment:
```bash
docker run -it --privileged --net=host \
  nucleardreamer/libfreenect2:latest \
  bash
```

## Step 4: Connect the Device (Inside Docker)
Inside the Docker terminal (Step 3), find and connect the Kinect:
```bash
# 1. Ask the Mac server what devices it has
local_ip="host.docker.internal"
usbip list -r $local_ip

# 2. Look for the Kinect Bus ID (e.g., "2-1") in the list.

# 3. Attach it! (Replace 2-1 with your actual ID)
usbip attach -r $local_ip -b 2-1
```

## Step 5: Verify & Run
Still inside Docker:
```bash
lsusb      # Should see Xbox NUI Sensor
Protonect  # The test app! Should open a window with video.
```
If `Protonect` shows video, CONGRATULATIONS! You have bridged the gap.
You can then run Python scripts *inside* this Docker container to do analytics.
