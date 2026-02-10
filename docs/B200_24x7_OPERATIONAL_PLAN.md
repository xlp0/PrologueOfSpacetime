# NVIDIA B200 GPU Cluster - 24x7 Operational Plan

**Document Version**: 1.0  
**Last Updated**: February 10, 2026  
**Status**: 🚀 Implementation Ready  
**Owner**: Institut Teknologi Del Infrastructure Team

---

## Executive Summary

This document provides a comprehensive operational plan for maintaining **24x7 uptime** of the NVIDIA B200 GPU cluster deployed at Institut Teknologi Del. The B200 represents critical infrastructure for the Brain Factory implementation, powering local AI inference for the OpenClaw platform running on PKC-OS.

**Uptime Target**: 99.9% (Maximum 8.76 hours downtime per year)

### Critical Success Factors

1. **Redundant Power Infrastructure** - Dual power supplies with UPS and generator backup
2. **Advanced Cooling Systems** - Precision cooling with N+1 redundancy
3. **Proactive Monitoring** - GPU health metrics, temperature, and performance tracking
4. **Rapid Response Procedures** - 24/7 on-call rotation with clear escalation paths
5. **Preventive Maintenance** - Scheduled maintenance windows with zero-downtime procedures

---

## Table of Contents

1. [Hardware Infrastructure Requirements](#1-hardware-infrastructure-requirements)
2. [Monitoring and Alerting Strategy](#2-monitoring-and-alerting-strategy)
3. [Redundancy and Failover Architecture](#3-redundancy-and-failover-architecture)
4. [Maintenance and Update Protocols](#4-maintenance-and-update-protocols)
5. [Incident Response and Recovery](#5-incident-response-and-recovery)
6. [Operational Best Practices](#6-operational-best-practices)

---

## 1. Hardware Infrastructure Requirements

### 1.1 Power Infrastructure

**Critical Requirement**: NVIDIA B200 GPUs are high-power devices requiring stable, redundant power delivery.

#### 1.1.1 Primary Power Configuration

**Power Specifications:**
- **Per B200 GPU**: ~700W TDP (Thermal Design Power)
- **Full System Power** (assuming 8x B200 cluster):
  - GPUs: 5,600W
  - CPUs & Memory: 1,500W
  - Networking & Storage: 500W
  - **Total**: ~7,600W (~8kW)
  - **With 20% headroom**: ~10kW required

**Redundant Power Supply Configuration:**
```
Primary Circuit (10kW) ──┬──> Server PSU 1 ──┐
                         │                    ├──> B200 Cluster
Secondary Circuit (10kW) ┴──> Server PSU 2 ──┘
```

**Implementation Checklist:**
- [ ] Dual power supplies (N+1 redundancy)
- [ ] Separate electrical circuits from different breaker panels
- [ ] Power distribution units (PDUs) with monitoring
- [ ] Automatic transfer switch (ATS) for seamless failover

#### 1.1.2 Uninterruptible Power Supply (UPS)

**UPS Requirements:**
- **Capacity**: 15kVA (to handle 10kW load with overhead)
- **Runtime**: Minimum 15 minutes at full load
- **Purpose**: Bridge power during:
  - Utility power fluctuations
  - Transfer to generator
  - Brief outages

**UPS Configuration:**
```yaml
UPS Specifications:
  Capacity: 15kVA / 12kW
  Runtime: 15-20 minutes at full load
  Battery Type: Sealed Lead Acid or Lithium-Ion
  Transfer Time: <4ms (no interruption)
  Monitoring: SNMP/Network card for remote monitoring
  Alerts: Email/SMS on power events
```

**Critical Monitoring Points:**
- Battery health and charge level
- Input/output voltage and frequency
- Load percentage
- Estimated runtime remaining
- Temperature

#### 1.1.3 Generator Backup (Optional but Recommended)

**For Extended Outages:**
- **Capacity**: 20kW diesel generator
- **Fuel**: 8-hour runtime minimum
- **Auto-start**: Triggered within 10 seconds of power loss
- **Transfer**: Automatic via ATS after UPS stabilizes load

**Implementation Priority**: High (for true 24x7 operation)

### 1.2 Cooling Infrastructure

**Critical**: B200 GPUs generate significant heat. Inadequate cooling = thermal throttling or hardware failure.

#### 1.2.1 Cooling Requirements

**Thermal Specifications:**
- **Heat Output**: ~8kW (from power consumption)
- **Cooling Capacity Required**: 10kW (with 25% overhead)
- **Target Temperature**: 18-27°C (64-80°F)
- **Maximum Temperature**: Never exceed 30°C (86°F)
- **Humidity**: 40-60% relative humidity

#### 1.2.2 Cooling Architecture

**N+1 Redundant Cooling:**
```
Primary CRAC Unit (6kW) ──┐
                          ├──> Server Room
Secondary CRAC Unit (6kW) ┘

Hot Aisle/Cold Aisle Configuration:
[Cold Aisle] → [Server Rack] → [Hot Aisle] → [Exhaust]
```

**Components:**
1. **Precision Air Conditioning (CRAC/CRAH)**
   - Two units, each capable of 6kW cooling
   - N+1 redundancy (one fails, other handles full load)
   - Variable speed fans for efficiency

2. **Airflow Management**
   - Hot aisle/cold aisle containment
   - Blanking panels in unused rack spaces
   - Cable management to prevent airflow blockage
   - Raised floor or overhead plenum for air distribution

3. **Direct GPU Cooling**
   - Ensure adequate airflow through server chassis
   - Consider liquid cooling if available on B200 models
   - Monitor individual GPU temperatures

#### 1.2.3 Temperature Monitoring

**Sensor Placement:**
- Inlet temperature (cold aisle): Target 20-22°C
- Outlet temperature (hot aisle): Monitor for <15°C delta
- GPU temperatures: Per-device monitoring via NVIDIA tools
- Room ambient: Overall environmental monitoring

**Alert Thresholds:**
```yaml
Temperature Alerts:
  Warning:
    Room: >25°C
    GPU: >75°C
  Critical:
    Room: >28°C
    GPU: >85°C
  Emergency Shutdown:
    Room: >30°C
    GPU: >90°C
```

### 1.3 Network Infrastructure

#### 1.3.1 Network Redundancy

**Dual Network Paths:**
```
B200 Cluster ──┬──> Switch 1 (Primary) ──┐
               │                          ├──> Core Network
               └──> Switch 2 (Secondary) ─┘
```

**Requirements:**
- Dual 100GbE or 200GbE connections per B200 node
- LACP (Link Aggregation) for bandwidth and redundancy
- Separate physical switches for true redundancy
- Automatic failover (<1 second)

#### 1.3.2 Network Monitoring

**Key Metrics:**
- Link status and utilization
- Packet loss and errors
- Latency and jitter
- Bandwidth consumption

**Integration**: Connect to existing Prometheus/Grafana stack

### 1.4 Physical Security and Access

**Environmental Protection:**
- [ ] Fire suppression system (FM-200 or equivalent, NOT water-based)
- [ ] Water leak detection sensors
- [ ] Physical access control (keycard/biometric)
- [ ] Security cameras with 30-day retention
- [ ] Environmental sensors (smoke, humidity, temperature)

---

## 2. Monitoring and Alerting Strategy

### 2.1 GPU Health Monitoring

#### 2.1.1 NVIDIA DCGM (Data Center GPU Manager)

**Deployment:**
```bash
# Install NVIDIA DCGM
kubectl apply -f nvidia-dcgm-exporter.yaml

# Or via Docker on bare metal
docker run -d --gpus all \
  --name dcgm-exporter \
  -p 9400:9400 \
  nvcr.io/nvidia/k8s/dcgm-exporter:latest
```

**Key Metrics Collected:**
```yaml
GPU Metrics:
  - dcgm_gpu_utilization              # GPU compute utilization %
  - dcgm_gpu_memory_utilization       # Memory utilization %
  - dcgm_gpu_temp                     # GPU temperature (°C)
  - dcgm_gpu_power_usage              # Power consumption (W)
  - dcgm_gpu_pcie_tx_throughput       # PCIe transmit throughput
  - dcgm_gpu_pcie_rx_throughput       # PCIe receive throughput
  - dcgm_gpu_nvlink_bandwidth         # NVLink bandwidth (if applicable)
  - dcgm_gpu_sm_clock                 # Streaming multiprocessor clock
  - dcgm_gpu_memory_clock             # Memory clock
  - dcgm_xid_errors                   # Hardware errors
```

#### 2.1.2 Prometheus Integration

**ServiceMonitor Configuration:**
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: nvidia-dcgm-exporter
  namespace: gpu-monitoring
  labels:
    release: prometheus-stack
spec:
  selector:
    matchLabels:
      app: nvidia-dcgm-exporter
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics
```

**Alert Rules:**
```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: nvidia-gpu-alerts
  namespace: gpu-monitoring
spec:
  groups:
  - name: nvidia_gpu
    interval: 30s
    rules:
    - alert: GPUHighTemperature
      expr: dcgm_gpu_temp > 80
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "GPU {{ $labels.gpu }} temperature is high"
        description: "GPU temperature is {{ $value }}°C"
    
    - alert: GPUCriticalTemperature
      expr: dcgm_gpu_temp > 85
      for: 1m
      labels:
        severity: critical
      annotations:
        summary: "GPU {{ $labels.gpu }} temperature is critical"
        description: "GPU temperature is {{ $value }}°C - immediate action required"
    
    - alert: GPUXIDError
      expr: increase(dcgm_xid_errors[5m]) > 0
      labels:
        severity: critical
      annotations:
        summary: "GPU {{ $labels.gpu }} hardware error detected"
        description: "XID error detected - potential hardware failure"
    
    - alert: GPULowUtilization
      expr: avg_over_time(dcgm_gpu_utilization[1h]) < 10
      for: 2h
      labels:
        severity: info
      annotations:
        summary: "GPU {{ $labels.gpu }} is underutilized"
        description: "Average utilization is {{ $value }}% over 1 hour"
    
    - alert: GPUMemoryPressure
      expr: dcgm_gpu_memory_utilization > 90
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "GPU {{ $labels.gpu }} memory pressure"
        description: "Memory utilization is {{ $value }}%"
```

### 2.2 Grafana Dashboards

#### 2.2.1 B200 Cluster Overview Dashboard

**Panels:**
1. **Cluster Health Summary**
   - Total GPUs online/offline
   - Average GPU utilization
   - Average GPU temperature
   - Total power consumption

2. **Per-GPU Metrics**
   - Individual GPU utilization (heatmap)
   - Temperature distribution
   - Memory usage
   - Power consumption

3. **Performance Metrics**
   - Inference throughput (if applicable)
   - Model loading times
   - Queue depth

4. **Environmental Metrics**
   - Room temperature
   - Cooling system status
   - Power supply status

#### 2.2.2 Dashboard Import

**Pre-built Dashboard:**
```bash
# Import NVIDIA DCGM dashboard
# Dashboard ID: 12239 (from Grafana.com)
curl -X POST https://grafana.pkc.pub/api/dashboards/import \
  -H "Content-Type: application/json" \
  -d '{"dashboard": {"id": 12239}}'
```

### 2.3 Log Aggregation

**Loki Integration:**
```yaml
# Collect GPU-related logs
{namespace="gpu-monitoring"} |= "GPU" or "CUDA" or "nvidia"

# Error logs only
{namespace="gpu-monitoring"} |~ "error|ERROR|fail|FAIL"

# Temperature warnings
{namespace="gpu-monitoring"} |~ "temperature|thermal|overheat"
```

### 2.4 Alerting Channels

**Multi-Channel Alerting:**
```yaml
Alertmanager Configuration:
  Routes:
    - Critical Alerts:
        - PagerDuty (immediate)
        - SMS (on-call engineer)
        - Email (team distribution list)
    
    - Warning Alerts:
        - Slack (#gpu-monitoring)
        - Email (team distribution list)
    
    - Info Alerts:
        - Slack (#gpu-monitoring)
```

**On-Call Rotation:**
- Primary: Infrastructure engineer (24/7)
- Secondary: Senior engineer (escalation)
- Tertiary: System architect (critical escalation)

---

## 3. Redundancy and Failover Architecture

### 3.1 GPU Workload Distribution

**Kubernetes Node Configuration:**
```yaml
apiVersion: v1
kind: Node
metadata:
  name: itdelb200b
  labels:
    node-role.kubernetes.io/gpu-worker: ""
    gpu.nvidia.com/class: B200
    gpu.nvidia.com/count: "8"
spec:
  taints:
  - key: nvidia.com/gpu
    value: "true"
    effect: NoSchedule
```

**GPU Resource Allocation:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ai-inference-worker
spec:
  containers:
  - name: inference
    image: ai-model:latest
    resources:
      limits:
        nvidia.com/gpu: 1  # Request 1 GPU
      requests:
        nvidia.com/gpu: 1
  nodeSelector:
    gpu.nvidia.com/class: B200
  tolerations:
  - key: nvidia.com/gpu
    operator: Exists
    effect: NoSchedule
```

### 3.2 Workload Redundancy Strategy

**Multi-Replica Deployment:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-inference-service
spec:
  replicas: 3  # Run on 3 different GPUs
  template:
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchLabels:
                app: ai-inference-service
            topologyKey: nvidia.com/gpu.id  # Different GPU per replica
```

**Benefits:**
- If one GPU fails, others continue serving
- Load distributed across multiple GPUs
- Rolling updates without downtime

### 3.3 Failover Procedures

#### 3.3.1 GPU Failure Detection

**Automatic Detection:**
1. DCGM detects XID error or GPU unresponsive
2. Kubernetes marks node as NotReady (if entire node fails)
3. Pods on failed GPU are evicted
4. Scheduler places pods on healthy GPUs

**Manual Detection:**
```bash
# Check GPU health
nvidia-smi

# Check for XID errors
nvidia-smi -q | grep -i "xid"

# DCGM diagnostics
dcgmi diag -r 3  # Level 3 diagnostic
```

#### 3.3.2 Graceful Degradation

**Capacity Planning:**
```
8 GPUs Total:
- Normal Operation: 6 GPUs active, 2 spare (75% utilization)
- 1 GPU Failure: 7 GPUs available, redistribute workload
- 2 GPU Failures: 6 GPUs available, still operational
- 3+ GPU Failures: Critical - manual intervention required
```

**Load Shedding:**
```yaml
# Prioritize critical workloads
apiVersion: v1
kind: Pod
metadata:
  name: critical-inference
spec:
  priorityClassName: system-cluster-critical  # High priority
  
---
apiVersion: v1
kind: Pod
metadata:
  name: batch-training
spec:
  priorityClassName: low-priority  # Can be evicted if needed
```

### 3.4 Data Redundancy

**Model Storage:**
- Store AI models in MinIO with Active-Active replication
- Models cached locally on GPU nodes for performance
- Automatic re-download if local cache corrupted

**Inference Results:**
- Stream results to distributed storage immediately
- No critical data stored only on GPU nodes
- Stateless inference services (can restart anywhere)

---

## 4. Maintenance and Update Protocols

### 4.1 Preventive Maintenance Schedule

**Monthly Tasks:**
- [ ] Visual inspection of hardware (fans, cables, dust)
- [ ] Review GPU error logs and metrics
- [ ] Test UPS battery (load test)
- [ ] Verify cooling system operation
- [ ] Check power consumption trends

**Quarterly Tasks:**
- [ ] Deep clean server chassis (compressed air)
- [ ] Thermal paste inspection (if accessible)
- [ ] UPS battery replacement (if needed)
- [ ] Firmware updates (BIOS, BMC, GPU)
- [ ] Disaster recovery drill

**Annual Tasks:**
- [ ] Full hardware audit
- [ ] Cooling system maintenance (CRAC units)
- [ ] Electrical system inspection
- [ ] Fire suppression system test
- [ ] Review and update documentation

### 4.2 Driver and Firmware Updates

**NVIDIA Driver Updates:**
```bash
# Check current driver version
nvidia-smi

# Update procedure (zero-downtime)
# 1. Drain one GPU node
kubectl drain itdelb200b --ignore-daemonsets

# 2. Update driver
sudo apt update
sudo apt install nvidia-driver-550  # Or latest stable

# 3. Reboot node
sudo reboot

# 4. Verify GPU functionality
nvidia-smi
dcgmi diag -r 1

# 5. Uncordon node
kubectl uncordon itdelb200b

# 6. Repeat for other nodes one at a time
```

**Update Policy:**
- **Production**: Only LTS (Long Term Support) drivers
- **Testing**: Validate new drivers in test environment first
- **Rollback Plan**: Keep previous driver package available
- **Timing**: During low-usage windows (weekends/nights)

### 4.3 Kubernetes Updates

**Node Update Procedure:**
```bash
# Update one node at a time
# 1. Drain node (moves pods to other nodes)
kubectl drain itdelb200b --ignore-daemonsets --delete-emptydir-data

# 2. Perform system updates
sudo apt update && sudo apt upgrade -y

# 3. Update Kubernetes components
sudo apt install -y kubelet=1.30.14-00 kubectl=1.30.14-00

# 4. Restart kubelet
sudo systemctl restart kubelet

# 5. Verify node health
kubectl get nodes

# 6. Uncordon node
kubectl uncordon itdelb200b
```

### 4.4 Maintenance Windows

**Scheduled Maintenance:**
- **Frequency**: Monthly
- **Duration**: 2-4 hours
- **Timing**: Sunday 02:00-06:00 WIB (lowest usage)
- **Notification**: 7 days advance notice to users

**Emergency Maintenance:**
- Critical security patches: 24-hour notice
- Hardware failure: Immediate (with redundancy, no downtime)

---

## 5. Incident Response and Recovery

### 5.1 Incident Classification

**Severity Levels:**

**P0 - Critical (Complete Outage)**
- All GPUs offline
- Complete power failure
- Cooling system failure (>30°C)
- Response Time: Immediate (15 minutes)
- Escalation: All hands on deck

**P1 - High (Partial Outage)**
- >50% GPUs offline
- Single power supply failure
- Cooling degraded (>28°C)
- Response Time: 30 minutes
- Escalation: On-call + senior engineer

**P2 - Medium (Degraded Service)**
- 1-2 GPUs offline
- Performance degradation
- Temperature warnings (>25°C)
- Response Time: 2 hours
- Escalation: On-call engineer

**P3 - Low (Minor Issues)**
- Single GPU underperforming
- Non-critical alerts
- Informational warnings
- Response Time: Next business day
- Escalation: Standard support

### 5.2 Incident Response Procedures

#### 5.2.1 GPU Failure Response

**Immediate Actions:**
```bash
# 1. Identify failed GPU
nvidia-smi
dcgmi discovery -l

# 2. Check for XID errors
nvidia-smi -q | grep -i "xid"
dmesg | grep -i nvidia

# 3. Isolate failed GPU
# Prevent workload scheduling
kubectl cordon itdelb200b

# 4. Drain workloads from failed GPU
kubectl drain itdelb200b --ignore-daemonsets

# 5. Attempt GPU reset
sudo nvidia-smi -r -i <gpu_id>

# 6. If reset fails, schedule hardware replacement
# Document incident in ticketing system
```

**Recovery:**
```bash
# After GPU replacement/repair
# 1. Verify GPU functionality
nvidia-smi
dcgmi diag -r 3

# 2. Re-enable node
kubectl uncordon itdelb200b

# 3. Monitor for 24 hours
# Watch for recurring issues
```

#### 5.2.2 Cooling Failure Response

**Critical Temperature Alert (>28°C):**
```bash
# IMMEDIATE ACTIONS (within 5 minutes)

# 1. Check cooling system status
# Verify CRAC units are running
# Check for blocked airflow

# 2. Reduce GPU load temporarily
# Scale down non-critical workloads
kubectl scale deployment batch-training --replicas=0

# 3. If temperature continues rising (>30°C)
# EMERGENCY SHUTDOWN to prevent hardware damage
kubectl drain itdelb200b --force --delete-emptydir-data

# 4. Contact HVAC technician (emergency)

# 5. Monitor temperature continuously
watch -n 5 'sensors | grep temp'
```

**Recovery:**
```bash
# After cooling restored
# 1. Verify temperature stable (<25°C for 30 minutes)

# 2. Gradually restore workloads
kubectl uncordon itdelb200b

# 3. Scale up workloads slowly
kubectl scale deployment batch-training --replicas=1
# Wait 10 minutes, monitor temperature
kubectl scale deployment batch-training --replicas=2
# Continue gradual scale-up

# 4. Document root cause and preventive measures
```

#### 5.2.3 Power Failure Response

**UPS Activation:**
```bash
# UPS provides 15-20 minutes runtime

# IMMEDIATE ACTIONS:
# 1. Check generator status
# If generator available: Wait for auto-start (10 seconds)

# 2. If no generator or generator fails:
# Initiate graceful shutdown sequence

# Priority 1: Save inference state (if applicable)
kubectl exec -it <pod> -- /app/save-state.sh

# Priority 2: Graceful pod shutdown
kubectl delete pod <pod> --grace-period=60

# Priority 3: Node shutdown
sudo shutdown -h +10  # 10 minute warning
```

**Recovery:**
```bash
# After power restored
# 1. Verify power stability (wait 5 minutes)

# 2. Power on nodes
# Check BIOS POST, verify all components detected

# 3. Verify GPU detection
nvidia-smi

# 4. Start Kubernetes
sudo systemctl start kubelet

# 5. Verify cluster health
kubectl get nodes
kubectl get pods -A

# 6. Restore workloads
kubectl apply -f deployments/
```

### 5.3 Disaster Recovery

#### 5.3.1 Complete Cluster Rebuild

**Scenario**: Catastrophic failure requiring full rebuild

**Recovery Steps:**
```bash
# 1. Restore hardware
# Replace failed components
# Verify all hardware functional

# 2. Reinstall OS (Ubuntu 24.04 LTS)
# Use automated installation if available

# 3. Install NVIDIA drivers
sudo apt install nvidia-driver-550

# 4. Install Kubernetes
# Follow cluster setup documentation

# 5. Restore configurations from backup
# Pull from Git repository
git clone https://github.com/org/b200-cluster-config.git
kubectl apply -f b200-cluster-config/

# 6. Restore AI models from MinIO
# Models automatically downloaded on first use

# 7. Verify functionality
# Run test inference workload
kubectl apply -f test-inference.yaml

# 8. Restore production workloads
kubectl apply -f production/
```

**Recovery Time Objective (RTO)**: 4 hours  
**Recovery Point Objective (RPO)**: 0 (no data loss, stateless services)

#### 5.3.2 Backup and Configuration Management

**What to Backup:**
```yaml
Critical Configurations:
  - Kubernetes manifests (Git repository)
  - NVIDIA driver versions (documented)
  - System configurations (/etc backup)
  - Monitoring dashboards (Grafana exports)
  - Alert rules (Prometheus rules)
  - Network configurations
  - Access credentials (encrypted vault)

AI Models and Data:
  - Model files (MinIO with replication)
  - Training datasets (if applicable)
  - Inference logs (Loki retention)
```

**Backup Locations:**
- Primary: MinIO cluster (local)
- Secondary: Cloud storage (offsite)
- Tertiary: Git repository (configurations)

---

## 6. Operational Best Practices

### 6.1 Daily Operations Checklist

**Morning Check (09:00 WIB):**
- [ ] Review Grafana dashboards for anomalies
- [ ] Check overnight alerts
- [ ] Verify all GPUs online and healthy
- [ ] Review GPU utilization trends
- [ ] Check cooling system status
- [ ] Verify backup completion

**Evening Check (17:00 WIB):**
- [ ] Review day's incidents
- [ ] Check scheduled jobs completion
- [ ] Verify monitoring systems operational
- [ ] Review capacity utilization
- [ ] Plan next day's maintenance (if any)

### 6.2 Capacity Planning

**Utilization Targets:**
```yaml
Healthy Utilization:
  GPU Compute: 60-80% average
  GPU Memory: 70-85% average
  Power: <90% of capacity
  Cooling: <80% of capacity

Warning Thresholds:
  GPU Compute: >85% sustained
  GPU Memory: >90% sustained
  Power: >90% of capacity
  Cooling: >85% of capacity

Action Required:
  GPU Compute: >90% sustained for 7 days → Add capacity
  GPU Memory: >95% sustained → Optimize models or add capacity
  Power: >95% → Upgrade power infrastructure
  Cooling: >90% → Upgrade cooling infrastructure
```

**Growth Planning:**
- Review utilization trends monthly
- Forecast capacity needs quarterly
- Plan infrastructure upgrades 6 months in advance

### 6.3 Performance Optimization

**GPU Utilization Optimization:**
```bash
# Enable GPU persistence mode (reduces initialization time)
sudo nvidia-smi -pm 1

# Set optimal power limit (balance performance/power)
sudo nvidia-smi -pl 650  # 650W for B200 (adjust as needed)

# Enable MIG (Multi-Instance GPU) if workloads are small
# Allows multiple workloads per GPU
nvidia-smi mig -cgi 9,9,9,9,9,9,9 -C
```

**Workload Scheduling:**
- Batch jobs during off-peak hours
- Real-time inference during business hours
- Model training overnight
- Maintenance during weekends

### 6.4 Documentation and Knowledge Management

**Required Documentation:**
- [ ] Hardware inventory and specifications
- [ ] Network topology diagrams
- [ ] Power and cooling schematics
- [ ] Runbooks for common incidents
- [ ] Vendor contact information
- [ ] Warranty and support contracts
- [ ] Change log (all modifications)

**Knowledge Base:**
- Confluence/Wiki with troubleshooting guides
- Post-mortem reports for all P0/P1 incidents
- Lessons learned from maintenance activities
- Best practices and optimization tips

### 6.5 Training and Skill Development

**Required Skills for Operations Team:**
- NVIDIA GPU architecture and troubleshooting
- Kubernetes administration
- Prometheus/Grafana monitoring
- Linux system administration
- Network troubleshooting
- Incident management

**Training Plan:**
- NVIDIA DLI (Deep Learning Institute) courses
- Kubernetes certification (CKA)
- Regular incident response drills
- Knowledge sharing sessions (monthly)

### 6.6 Vendor and Support Contacts

**Critical Contacts:**
```yaml
NVIDIA Support:
  Level: Enterprise Support
  SLA: 4-hour response for P0
  Contact: support@nvidia.com
  Phone: [Enterprise support number]

Hardware Vendor:
  Vendor: [Dell/HPE/Supermicro/etc.]
  Support Level: 24/7 with 4-hour onsite
  Contact: [Vendor contact]

Cooling/HVAC:
  Vendor: [Local HVAC company]
  Emergency: [24/7 emergency number]
  Regular Maintenance: [Scheduled contact]

Electrical:
  Electrician: [Licensed electrician]
  Emergency: [24/7 emergency number]

UPS Vendor:
  Vendor: [APC/Eaton/etc.]
  Support: [Support contact]
  Battery Replacement: [Service contact]
```

---

## 7. Success Metrics and KPIs

### 7.1 Availability Metrics

**Target SLAs:**
```yaml
Availability:
  Target: 99.9% uptime
  Measurement: Monthly
  Calculation: (Total time - Downtime) / Total time

Mean Time Between Failures (MTBF):
  Target: >720 hours (30 days)
  Measurement: Per GPU

Mean Time To Repair (MTTR):
  Target: <2 hours
  Measurement: Per incident

Mean Time To Detect (MTTD):
  Target: <5 minutes
  Measurement: Per incident
```

### 7.2 Performance Metrics

**GPU Performance:**
```yaml
Inference Latency:
  Target: <100ms p95
  Measurement: Continuous

Throughput:
  Target: [Based on workload requirements]
  Measurement: Requests per second

GPU Utilization:
  Target: 60-80% average
  Measurement: Hourly average

Model Loading Time:
  Target: <30 seconds
  Measurement: Per model
```

### 7.3 Operational Metrics

**Incident Management:**
```yaml
P0 Incidents:
  Target: 0 per month
  Response Time: <15 minutes

P1 Incidents:
  Target: <1 per month
  Response Time: <30 minutes

P2 Incidents:
  Target: <3 per month
  Response Time: <2 hours

Alert Fatigue:
  False Positive Rate: <5%
  Alert Response Rate: >95%
```

**Maintenance:**
```yaml
Planned Maintenance:
  Frequency: Monthly
  Downtime: 0 (rolling updates)
  Success Rate: 100%

Preventive Maintenance:
  Completion Rate: 100%
  On-Time Rate: >95%
```

---

## 8. Continuous Improvement

### 8.1 Monthly Review Process

**Review Meeting Agenda:**
1. Availability metrics review
2. Incident post-mortems
3. Capacity planning update
4. Upcoming maintenance schedule
5. Action items from previous month
6. New risks or concerns

**Participants:**
- Infrastructure team
- Development team (OpenClaw)
- Management
- Vendor representatives (quarterly)

### 8.2 Quarterly Improvements

**Focus Areas:**
- Automation opportunities
- Monitoring enhancements
- Documentation updates
- Training needs
- Infrastructure upgrades

**Continuous Optimization:**
- Review and tune alert thresholds
- Optimize workload scheduling
- Improve runbooks based on incidents
- Update disaster recovery procedures
- Benchmark performance improvements

---

## Appendix A: Quick Reference Commands

### GPU Health Check
```bash
# Basic GPU status
nvidia-smi

# Detailed GPU info
nvidia-smi -q

# Watch GPU metrics (updates every 2 seconds)
watch -n 2 nvidia-smi

# GPU temperature only
nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader

# GPU utilization
nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader

# Check for errors
nvidia-smi -q | grep -i "xid\|error"

# DCGM diagnostics
dcgmi diag -r 1  # Quick test
dcgmi diag -r 3  # Comprehensive test
```

### Kubernetes GPU Operations
```bash
# List GPU nodes
kubectl get nodes -l gpu.nvidia.com/class=B200

# Check GPU resource allocation
kubectl describe node itdelb200b | grep -A 5 "Allocated resources"

# List pods using GPUs
kubectl get pods -A -o json | jq '.items[] | select(.spec.containers[].resources.limits."nvidia.com/gpu" != null) | .metadata.name'

# GPU pod logs
kubectl logs -n <namespace> <pod-name>

# Drain GPU node for maintenance
kubectl drain itdelb200b --ignore-daemonsets --delete-emptydir-data

# Restore GPU node
kubectl uncordon itdelb200b
```

### Monitoring Queries
```bash
# Prometheus queries (via promtool or Grafana)

# Average GPU temperature
avg(dcgm_gpu_temp)

# GPU utilization by GPU
dcgm_gpu_utilization

# Total power consumption
sum(dcgm_gpu_power_usage)

# GPUs with errors
dcgm_xid_errors > 0

# GPU memory pressure
dcgm_gpu_memory_utilization > 90
```

---

## Appendix B: Emergency Contact Card

**Print and post in server room:**

```
╔════════════════════════════════════════════════════════════╗
║          NVIDIA B200 CLUSTER - EMERGENCY CONTACTS          ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  PRIMARY ON-CALL: [Name]                                   ║
║  Phone: [Number]                                           ║
║  Email: [Email]                                            ║
║                                                            ║
║  SECONDARY ON-CALL: [Name]                                 ║
║  Phone: [Number]                                           ║
║                                                            ║
║  NVIDIA SUPPORT: [Enterprise Support Number]               ║
║                                                            ║
║  HVAC EMERGENCY: [24/7 Number]                             ║
║                                                            ║
║  ELECTRICAL EMERGENCY: [24/7 Number]                       ║
║                                                            ║
║  FACILITY SECURITY: [Number]                               ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║  EMERGENCY SHUTDOWN PROCEDURE:                             ║
║  1. Alert on-call engineer immediately                     ║
║  2. If temperature >30°C: kubectl drain itdelb200b --force ║
║  3. Document incident in ticketing system                  ║
║  4. Do not restart until cleared by engineer               ║
╚════════════════════════════════════════════════════════════╝
```

---

## Document Change Log

| Date | Version | Author | Changes |
|------|---------|--------|---------|
| 2026-02-10 | 1.0 | Infrastructure Team | Initial document creation |

---

**Document Review Schedule**: Quarterly  
**Next Review Date**: 2026-05-10  
**Document Owner**: Institut Teknologi Del Infrastructure Team
