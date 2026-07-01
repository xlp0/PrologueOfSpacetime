# Hikvision IP Camera Access Guide

**Last Updated**: April 1, 2026  
**Status**: ✅ Active  
**Location**: hpserver (biznetmaster)

## Overview

This guide provides step-by-step instructions for accessing Hikvision IP cameras through the hpserver node in the Kubernetes cluster.

## Camera Information

### Camera IP Addresses
- Camera 1: `192.168.100.24`
- Camera 2: `192.168.100.34`
- Camera 3: `192.168.100.26`

### Credentials
- **Username**: `admin`
- **Password**: `Bait695mash215`

### Access Ports
- **HTTP Web Interface**: Port 80 (default) or Port 8000 (alternative)
- **RTSP Stream**: Port 554

## Network Topology

### hpserver Network Configuration
```
hpserver (biznetmaster) interfaces:
- eth0: 103.87.66.218/23 (Public Internet)
- zt33ooxlbk: 10.40.14.17/24 (ZeroTier)
- zt33ojdugw: 10.71.161.17/24 (ZeroTier)
- ztaagjdq3p: 10.147.19.17/24 (ZeroTier)
- ztdiy7kspx: 10.254.81.17/24 (ZeroTier)
- wt0: 100.101.145.201/16 (Tailscale)
- Kubernetes networks: 10.244.x.x
```

### ⚠️ Network Issue Identified
**Problem**: hpserver does NOT have a network interface on the `192.168.100.0/24` subnet where the cameras are located.

**Impact**: 
- ✅ ICMP (ping) works - cameras respond to ping
- ❌ TCP connections fail - cannot access HTTP or RTSP ports
- ❌ No direct route to camera network

## Access Methods

### Method 1: SSH to hpserver (First Step)

```bash
# From your local machine
ssh hpserver

# Or with full details
ssh -i ~/.ssh/hpserver_key hpserver@10.40.14.205
```

### Method 2: Test Camera Connectivity

Once connected to hpserver, test basic connectivity:

```bash
# Test ping to cameras
ping -c 2 192.168.100.24
ping -c 2 192.168.100.34
ping -c 2 192.168.100.26

# Check network routes
ip route show

# Check network interfaces
ip addr show
```

**Expected Result**: Ping should work, but TCP connections will timeout.

### Method 3: Access Camera Web Interface

**From a device on 192.168.100.0/24 network:**

```
http://192.168.100.24
http://192.168.100.34
http://192.168.100.26

# Or try alternative port 8000
http://192.168.100.24:8000
http://192.168.100.34:8000
http://192.168.100.26:8000
```

**Login Credentials**:
- Username: `admin`
- Password: `Bait695mash215`

### Method 4: Access RTSP Streams

**RTSP URL Format**:
```
rtsp://admin:Bait695mash215@[camera-ip]:554/Streaming/Channels/[channel]
```

**Channel Options**:
- Channel 101: Main stream (high quality)
- Channel 102: Sub stream (lower quality)

**Complete RTSP URLs**:
```
rtsp://admin:Bait695mash215@192.168.100.24:554/Streaming/Channels/101
rtsp://admin:Bait695mash215@192.168.100.34:554/Streaming/Channels/101
rtsp://admin:Bait695mash215@192.168.100.26:554/Streaming/Channels/101
```

**How to View RTSP Streams**:

1. **Using VLC Media Player**:
   - Open VLC
   - Go to: Media → Open Network Stream
   - Paste RTSP URL
   - Click Play

2. **Using FFmpeg** (if installed):
   ```bash
   ffplay "rtsp://admin:Bait695mash215@192.168.100.26:554/Streaming/Channels/101"
   ```

3. **Using curl** (to test):
   ```bash
   curl -v --max-time 10 "rtsp://admin:Bait695mash215@192.168.100.26:554/Streaming/Channels/101"
   ```

## Solutions for Network Access

### Solution 1: Access from Device on Same Network ✅ Recommended

Access cameras from a computer/device that's on the `192.168.100.0/24` network:
- Your local computer (if on that network)
- A router/gateway with access to that subnet
- Another server with interface on 192.168.100.0/24

### Solution 2: Add Network Route on hpserver

If there's a gateway that can reach the camera network:

```bash
# Add static route (replace <gateway_ip> with actual gateway)
sudo ip route add 192.168.100.0/24 via <gateway_ip> dev eth0

# Make route persistent (add to /etc/netplan/ or /etc/network/interfaces)
```

### Solution 3: Add Secondary IP on hpserver

If hpserver has a physical network card that can connect to 192.168.100.0/24:

```bash
# Add secondary IP (replace <interface_name> and <ip>)
sudo ip addr add 192.168.100.<ip>/24 dev <interface_name>

# Bring interface up
sudo ip link set <interface_name> up
```

### Solution 4: SSH Tunneling via Gateway

If there's a machine that can access both hpserver and cameras:

```bash
# From your local machine
ssh -L 8080:192.168.100.24:80 user@gateway-machine

# Then access via localhost
http://localhost:8080
```

## Troubleshooting

### Issue: Cannot Access Camera Web Interface

**Symptoms**:
- Ping works
- HTTP connection times out
- Browser shows "Connection timeout"

**Diagnosis**:
```bash
# Check if port is accessible
nc -zv -w 3 192.168.100.24 80
nc -zv -w 3 192.168.100.24 8000

# Scan for open ports
nmap -Pn -p 1-10000 --open 192.168.100.24
```

**Solution**: Ensure you're accessing from a device on the same network (192.168.100.0/24).

### Issue: RTSP Stream Not Working

**Symptoms**:
- Connection timeout on port 554
- VLC shows "Connection failed"

**Diagnosis**:
```bash
# Test RTSP port
nc -zv -w 3 192.168.100.24 554

# Check with curl
curl -v --max-time 10 "rtsp://admin:Bait695mash215@192.168.100.24:554/Streaming/Channels/101"
```

**Solution**: 
1. Verify credentials are correct
2. Ensure RTSP is enabled on camera
3. Check if accessing from correct network
4. Try sub-stream (Channel 102) if main stream fails

### Issue: Wrong Password

**Symptoms**:
- "401 Unauthorized" error
- "Authentication failed"

**Solution**:
1. Verify password: `Bait695mash215`
2. Check if camera password was changed
3. Try resetting camera to factory defaults (last resort)

## Quick Reference

### Camera Quick Access

| Camera | IP | Web Interface | RTSP Stream |
|--------|-------|---------------|-------------|
| Camera 1 | 192.168.100.24 | http://192.168.100.24 | rtsp://admin:Bait695mash215@192.168.100.24:554/Streaming/Channels/101 |
| Camera 2 | 192.168.100.34 | http://192.168.100.34 | rtsp://admin:Bait695mash215@192.168.100.34:554/Streaming/Channels/101 |
| Camera 3 | 192.168.100.26 | http://192.168.100.26 | rtsp://admin:Bait695mash215@192.168.100.26:554/Streaming/Channels/101 |

### Common Commands

```bash
# SSH to hpserver
ssh hpserver

# Test camera connectivity
ping -c 2 192.168.100.24

# Check network routes
ip route show | grep 192.168.100

# Test HTTP port
curl -I --connect-timeout 5 http://192.168.100.24

# Test RTSP port
nc -zv -w 3 192.168.100.24 554
```

## Security Notes

⚠️ **Important Security Considerations**:

1. **Password Storage**: Never commit passwords to Git repositories
2. **Network Segmentation**: Cameras are on isolated network (192.168.100.0/24)
3. **Access Control**: Only authorized devices should access camera network
4. **RTSP Security**: RTSP credentials are sent in clear text - use VPN when accessing remotely

## Related Documentation

- [hpserver Setup Guide](./hpserver-setup-guide.md)
- [Network Configuration](../architecture/network-topology.md)
- [SSH Quick Reference](../quick-reference/ssh-quick-reference.md)

## Support

For issues or questions:
1. Check network connectivity first
2. Verify you're on the correct network segment
3. Test with ping before attempting TCP connections
4. Consult Hikvision documentation for camera-specific issues

---

**Document Version**: 1.0  
**Created**: April 1, 2026  
**Author**: System Documentation
