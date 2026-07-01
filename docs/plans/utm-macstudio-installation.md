# UTM Mac Studio Installation

**Target**: Mac Studio with Apple Silicon  
**Objective**: Create Ubuntu VM to join Kubernetes cluster as worker node

## Prerequisites

### Required Files
- UTM.dmg (229 MB) - Download from https://mac.getutm.app/
- Ubuntu Server 22.04.5 ARM64 ISO (1.9 GB) - Download from https://ubuntu.com/download/server/arm

### Installation Scripts
- Automated Kubernetes setup script (setup-k8s-worker-vm.sh)
- Installation helper script (remote-install-utm.sh)

## Installation Procedure

### Step 1: Install UTM Application

Open Terminal on Mac Studio and execute:

```bash
# Mount UTM disk image
hdiutil attach ~/Downloads/UTM.dmg

# Install UTM to Applications (requires sudo password)
sudo cp -R /Volumes/UTM/UTM.app /Applications/

# Unmount disk image
hdiutil detach /Volumes/UTM

# Remove quarantine attribute
xattr -d com.apple.quarantine /Applications/UTM.app
```

Verify installation:
```bash
ls -la /Applications/UTM.app
```

### Step 2: Create Ubuntu VM

Open UTM application and configure:

1. Click **"Create a New Virtual Machine"**
2. Select **"Virtualize"** (for ARM64)
3. Select **"Linux"**
4. Configure VM:
   - **Name**: `k8s-worker-macstudio`
   - **Memory**: `4096 MB` (4GB)
   - **CPU Cores**: `2`
   - **Disk Size**: `40 GB`
5. **Boot ISO**: Browse to `~/Downloads/ubuntu-22.04.5-live-server-arm64.iso`
6. **Network**: Select "Bridged Mode" (required for cluster access)
7. Click "Save"

### Step 3: Install Ubuntu Server

Start VM and install Ubuntu with these settings:

- Hostname: k8s-worker-macstudio
- Username: ubuntu
- Password: [choose strong password]
- Network: DHCP
- Packages: OpenSSH Server (REQUIRED)
- Disk: Use entire disk (40GB)

After installation completes:
1. VM will reboot
2. Login with ubuntu user
3. Note the VM IP address: `ip addr show`

### Step 4: Setup Kubernetes Components

From control plane node, copy setup script to VM:

```bash
# Replace <VM_IP> with actual VM IP address
scp setup-k8s-worker-vm.sh [vm-username]@<VM_IP>:~/
```

SSH to VM and run setup:

```bash
# SSH to VM
ssh [vm-username]@<VM_IP>

# Make script executable
chmod +x setup-k8s-worker-vm.sh

# Run setup script (will take 5-10 minutes)
sudo ./setup-k8s-worker-vm.sh
```

The script will install:
- Containerd (container runtime)
- kubeadm, kubelet, kubectl (v1.30.14)
- Required kernel modules and sysctl settings
- Disable swap
- Configure networking

### Step 5: Join VM to Kubernetes Cluster

On control plane node, generate join token:

```bash
kubeadm token create --print-join-command
```

Example output:
```bash
kubeadm join [control-plane-ip]:6443 --token abc123.xyz789 \
    --discovery-token-ca-cert-hash sha256:1234567890abcdef...
```

On VM, run the join command with sudo:

```bash
sudo kubeadm join [control-plane-ip]:6443 --token abc123.xyz789 \
    --discovery-token-ca-cert-hash sha256:1234567890abcdef...
```

Expected output:
```
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Starting the kubelet
This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.
```

### Step 6: Verify Node Joined

On control plane node:

```bash
kubectl get nodes
```

Expected output:
```
NAME                    STATUS   ROLES           AGE   VERSION
control-plane           Ready    control-plane   10d   v1.30.14
worker-node-1           Ready    <none>          10d   v1.30.14
worker-node-2           Ready    <none>          9d    v1.30.14
vm-worker-node          Ready    <none>          1m    v1.30.14
```

Check node details:
```bash
kubectl describe node [vm-worker-node]
```

Verify node-exporter pod:
```bash
kubectl get pods -n monitoring -l app=node-exporter -o wide | grep [vm-worker-node]
```

### Step 7: Update Grafana Dashboard

Get VM IP:
```bash
kubectl get nodes [vm-worker-node] -o wide
```

Update dashboard mapping in your Grafana dashboard configuration.

Add new label_replace for the VM IP:

```json
label_replace(..., "nodename", "[vm-worker-node]", "instance", "[vm-ip]:9100")
```

Apply changes:
```bash
# Update ConfigMap
kubectl apply -f /path/to/updated/configmap

# Restart Grafana
kubectl rollout restart deployment grafana -n monitoring
```

## Post-Installation Tasks

1. Label node (optional):
   ```bash
   kubectl label node [vm-worker-node] node-role.kubernetes.io/worker=worker
   kubectl label node [vm-worker-node] location=[location-label]
   ```

2. Verify monitoring:
   ```bash
   kubectl get pods -n monitoring -o wide | grep [vm-worker-node]
   ```

3. Update documentation:
   - Update cluster documentation
   - Add node information (IP, specs, status)

## Important Notes

### Manual Installation Requirements

1. UTM is GUI application - Cannot be fully automated via SSH
2. Sudo access needed - Installing to /Applications requires admin password
3. VM creation - UTM GUI required for VM configuration
4. Ubuntu installation - Interactive installer in VM console

### Network Configuration

VM Network Mode: Bridged
- VM gets IP on same network as Mac Studio
- Accessible from Kubernetes cluster nodes
- No port forwarding needed

Alternative (if Bridged doesn't work): NAT with port forwarding
- Configure port forwarding for kubelet (10250)
- May need additional firewall rules

### Resource Allocation

Mac Studio (assumed specs):
- Total RAM: 32GB
- Total CPU: 10 cores

VM Allocation:
- RAM: 4GB
- CPU: 2 cores
- Disk: 40GB

Remaining for macOS:
- RAM: 28GB
- CPU: 8 cores

### Security Considerations

1. SSH Access: Ensure OpenSSH server installed in VM
2. Firewall: UFW will be configured by setup script
3. Updates: Keep Ubuntu and Kubernetes updated
4. Passwords: Use strong passwords for ubuntu user

## Troubleshooting

### Cannot install UTM (Permission denied)
Solution: Run with sudo: `sudo cp -R /Volumes/UTM/UTM.app /Applications/`

### Ubuntu ISO not found
Solution: Download manually:
```bash
cd ~/Downloads
curl -L -O https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.3-live-server-arm64.iso
```

### VM cannot reach cluster
Solution: 
- Verify network mode is Bridged
- Verify firewall rules on Mac Studio
- Test connectivity: `ping [control-plane-ip]` from VM

### Node stays NotReady
Solution:
- Check kubelet logs: `sudo journalctl -u kubelet -f`
- Verify containerd: `sudo systemctl status containerd`
- Check CNI plugin: `kubectl get pods -n kube-system | grep flannel`

### Cannot SSH to VM
Solution:
- Verify OpenSSH server installed during Ubuntu setup
- Check SSH service: `sudo systemctl status ssh`
- Verify VM IP: `ip addr show`

## Testing

Test deployment on new node:
```bash
kubectl run test-pod --image=nginx --overrides='{"spec":{"nodeSelector":{"kubernetes.io/hostname":"[vm-worker-node]"}}}'
```

## Estimated Time

- UTM Installation: 5 minutes
- VM Creation: 5 minutes
- Ubuntu Installation: 15-20 minutes
- Kubernetes Setup: 10 minutes
- Join to Cluster: 2 minutes
- Verification: 5 minutes

Total: 45-50 minutes

## References

- UTM Documentation: https://docs.getutm.app/
- Ubuntu ARM64: https://ubuntu.com/download/server/arm
- Kubernetes Documentation: https://kubernetes.io/docs/
- kubeadm Join: https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join/
