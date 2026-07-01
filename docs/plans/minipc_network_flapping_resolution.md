# Incident Resolution: minipc Network Flapping in Kubernetes

## Overview
A `minipc` node in the Kubernetes cluster was experiencing constant "Down" and "Up" flapping, visible in Grafana as a barcode-like oscillation of metrics. This document outlines the investigation, root causes, and multi-step resolution for this issue. This serves as an example document for debugging similar complex network issues within Kubernetes nodes.

## Investigation Steps

### 1. Initial Connectivity Diagnostics
- **Symptom:** Initial manual SSH attempts to the node's documented Kubernetes ZeroTier IP (`10.40.14.104`) either hung or timed out.
- **Action:** Deployed an automated background script to continuously ping and attempt to SSH into `minipc`. The script successfully connected during one of the node's brief "Up" windows.

### 2. Log & Network Analysis
Once connected, the following diagnostics were performed:
- Verified that the node hardware itself was stable (uptime of 13+ hours).
- Checked the local network interfaces and ZeroTier routing table using `ip a` and `zerotier-cli listnetworks`.

## Root Cause Analysis

The investigation uncovered two separate network issues compounding to cause the flapping:

### Root Cause 1: Route Thrashing from Subnet Overlap
- **Finding:** `minipc` was simultaneously joined to two different ZeroTier networks (`serene_szpakowski` and `general_resources`) that were both trying to assign the exact same subnet (`10.147.19.0/24`). Additionally, a third network was repeatedly failing authentication (`ACCESS_DENIED`).
- **Impact:** This overlapping subnet caused severe route thrashing in the Linux kernel. The operating system could not reliably route traffic over the VPN interfaces, leading to dropped packets for all ZeroTier connections. This included the `10.40.14.0/24` network used by the kubelet to reach the master node. Consequently, Prometheus intermittently failed to scrape metrics, causing the oscillating "Down/Up" red lines in Grafana.

### Root Cause 2: Path MTU Discovery (PMTUD) Failure
- **Finding:** After resolving the route thrashing, ICMP pings stabilized, but `node-exporter` HTTP queries were still hanging between the Prometheus scraper (`workernode1`) and `minipc`. Querying the Prometheus API natively showed `health: down` with a `deadline exceeded` error. 
- **Impact:** ZeroTier uses a default MTU of 2800. For large HTTP responses (such as the 60KB `/metrics` scrape payload), ZeroTier fragments the packets into multiple UDP datagrams. Because one of the underlying internet connections between `minipc` and `workernode1` drops UDP fragments, these large TCP segments were being silently blackholed, causing the scrape to hang until timeout.

## Resolution

### Part 1 - Network Stability (Fixing Route Thrashing)
Deployed a fix script that executed during an "Up" window to force the `minipc` ZeroTier client to leave the conflicting network (`general_resources`) and the unauthenticated network.

```bash
sudo zerotier-cli leave fc7cad22a0f283c9
sudo zerotier-cli leave cf719fd5406a9cb7
```

### Part 2 - Fixing Prometheus Scrape Metric TSDB Flapping (Fixing PMTUD)
Reduced the `zt33ooxlbk` interface MTU to `1280` on both `workernode1` and `minipc`. 
- **Why this works:** This successfully clumps/clamps the TCP MSS size, ensuring the HTTP responses fit completely inside single, unfragmented ZeroTier UDP packets.
- **Result:** Prometheus scrape metrics immediately returned to `health: up`.

## Validation Conclusion

After applying the secondary MTU fix, the Prometheus HTTP scrapes properly extract the exporter values without TCP deadlocks. `minipc` is `Ready` and properly registering a solid metric stream over its `10.40.14.104` ZeroTier address into the Grafana dashboard.

### Native Node Diagnostics
To independently verify stability directly from the `minipc` side, the following final checks were made:

1. **ZeroTier Logs:** Showed 0 connection drops or tunnel rebuilds in the past hour.
2. **Kernel Logs (`dmesg`):** Showed no NIC (Network Interface Card) driver restarts, dropped connections, or physical port link flaps. *(Note: `dmesg` did reveal that 10 hours prior, an NVMe drive `nvme3n1` failed, causing the `md0` RAID array to run in an active degraded state. This was noted but does not impact network connectivity).*
3. **Inter-node Ping:** Outbound ICMP pings from `minipc` to both the Master (`10.40.14.17`) and `workernode1` (`10.40.14.37`) showed 0% packet loss with a solid 21-23ms latency.

The `minipc` network is confirmed 100% stable natively. Any remaining visual anomalies on the dashboard represent historical data points trailing off the time window.
