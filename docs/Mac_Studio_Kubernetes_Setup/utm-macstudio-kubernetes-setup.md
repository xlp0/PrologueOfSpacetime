# UTM Mac Studio - Kubernetes Worker Node Setup Plan

## Overview
Setup UTM virtualization on Mac Studio to run Ubuntu VM as worker node in Kubernetes cluster.

## Target Machine
- Hostname: [your-mac-hostname]
- IP Address: [your-mac-ip]
- OS: macOS
- Architecture: ARM64 (Apple Silicon)
- SSH Access: [username]@[your-mac-ip]

## Prerequisites
- Mac Studio with Apple Silicon (ARM64)
- Minimum 8GB RAM available (4GB for VM)
- Minimum 50GB disk space available
- Internet connection
- SSH access to Mac Studio

## Installation Plan

### Phase 1: Install UTM on Mac Studio

#### Step 1.1: Install Homebrew (if not installed)
```bash
ssh [username]@[your-mac-ip] '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
```

#### Step 1.2: Install UTM via Homebrew
```bash
ssh [username]@[your-mac-ip] "brew install --cask utm"
```

Alternative: Download UTM manually from https://mac.getutm.app/

### Phase 2: Download Ubuntu Server ARM64 ISO

#### Step 2.1: Download Ubuntu Server 22.04 LTS ARM64
```bash
ssh [username]@[your-mac-ip] "cd ~/Downloads && curl -LO https://cdimage.ubuntu.com/releases/22.04/release/ubuntu-22.04.5-live-server-arm64.iso"
```

ISO Details:
- Version: Ubuntu 22.04.5 LTS
- Architecture: ARM64
- Size: 1.9 GB

### Phase 3: Create Ubuntu VM in UTM

#### Step 3.1: VM Configuration
- Name: [vm-name]
- Type: Linux
- Architecture: ARM64 (aarch64)
- Memory: 4096 MB (4GB)
- CPU Cores: 2
- Disk Size: 40 GB
- Network: Bridged
- Boot ISO: ubuntu-22.04.5-live-server-arm64.iso

#### Step 3.2: Create VM via UTM GUI
Since UTM is a GUI application, this step requires:
1. Open UTM application on Mac Studio
2. Click "Create a New Virtual Machine"
3. Select "Virtualize" (for ARM64)
4. Select "Linux"
5. Configure resources as specified above
6. Attach Ubuntu ISO
7. Start VM and proceed with installation

Note: UTM GUI access requires VNC or physical access to Mac Studio. SSH cannot directly control UTM GUI.

### Phase 4: Install Ubuntu Server in VM

#### Step 4.1: Ubuntu Installation Settings
- Hostname: [vm-hostname]
- Username: [vm-username]
- Password: [choose-strong-password]
- Network: DHCP
- Packages: OpenSSH Server (required)
- Disk: Use entire disk (40GB)

#### Step 4.2: Post-Installation Configuration
After Ubuntu installation completes:

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y curl wget git vim net-tools

# Configure static IP (optional)
sudo nano /etc/netplan/00-installer-config.yaml
```

Netplan Configuration Example:
```yaml
network:
  version: 2
  ethernets:
    [interface-name]:
      dhcp4: no
      addresses:
        - [vm-ip]/24
      gateway4: [gateway-ip]
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

Apply network configuration:
```bash
sudo netplan apply
```

### Phase 5: Install Kubernetes Components in VM

#### Step 5.1: Disable Swap
```bash
sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
```

#### Step 5.2: Load Kernel Modules
```bash
cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter
```

#### Step 5.3: Configure Sysctl
```bash
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

sudo sysctl --system
```

#### Step 5.4: Install Containerd
```bash
# Install dependencies
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker repository
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install containerd
sudo apt-get update
sudo apt-get install -y containerd.io

# Configure containerd
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml

# Enable SystemdCgroup
sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml

# Restart containerd
sudo systemctl restart containerd
sudo systemctl enable containerd
```

#### Step 5.5: Install kubeadm, kubelet, kubectl
```bash
# Add Kubernetes repository
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.30/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg

echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.30/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list

# Install Kubernetes components
sudo apt-get update
sudo apt-get install -y kubelet=1.30.14-1.1 kubeadm=1.30.14-1.1 kubectl=1.30.14-1.1
sudo apt-mark hold kubelet kubeadm kubectl

# Enable kubelet
sudo systemctl enable kubelet
```

### Phase 6: Join VM to Kubernetes Cluster

#### Step 6.1: Generate Join Token (on control plane)
```bash
# On control plane node
kubeadm token create --print-join-command
```

This will output a command like:
```bash
kubeadm join [control-plane-ip]:6443 --token <token> \
    --discovery-token-ca-cert-hash sha256:<hash>
```

#### Step 6.2: Join Worker Node (on VM)
```bash
# On VM
sudo kubeadm join [control-plane-ip]:6443 --token <token> \
    --discovery-token-ca-cert-hash sha256:<hash>
```

#### Step 6.3: Verify Node Status (on biznetmaster)
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

### Phase 7: Configure Network Access

#### Step 7.1: Configure Port Forwarding (if needed)
If VM is behind NAT, configure port forwarding on Mac Studio:
- VM IP: [vm-ip]
- Forward ports: 10250 (kubelet), 30000-32767 (NodePort services)

#### Step 7.2: Configure Firewall (if enabled)
```bash
# On VM
sudo ufw allow 10250/tcp
sudo ufw allow 30000:32767/tcp
```

### Phase 8: Install Node Exporter for Monitoring

#### Step 8.1: Deploy Node Exporter (automatic via DaemonSet)
Node exporter should be automatically deployed by the existing DaemonSet in the cluster.

Verify:
```bash
kubectl get pods -n monitoring -l app=node-exporter -o wide
```

### Phase 9: Update Grafana Dashboard

#### Step 9.1: Update Dashboard Mapping
Update the Grafana dashboard to include the new node:
- Add IP to node name mapping
- Update legend format

#### Step 9.2: Verify Metrics
Check that metrics are being collected from the new node in Grafana.

## Post-Installation Checklist

- [ ] UTM installed on Mac Studio
- [ ] Ubuntu VM created with correct resources
- [ ] Ubuntu Server installed and configured
- [ ] Static IP configured
- [ ] Containerd installed and running
- [ ] Kubernetes components installed (v1.30.14)
- [ ] VM joined to cluster successfully
- [ ] Node shows "Ready" status
- [ ] Node exporter pod running on new node
- [ ] Metrics visible in Grafana dashboard
- [ ] Documentation updated in cluster-status-2025.md

## Troubleshooting

### UTM GUI not accessible via SSH
Solution: UTM requires GUI access. Use VNC or physical access to Mac Studio.

### VM cannot reach cluster control plane
Solution: 
- Check network configuration (bridged vs NAT)
- Verify firewall rules
- Test connectivity: `ping [control-plane-ip]`

### Node stays in NotReady state
Solution:
- Check kubelet logs: `sudo journalctl -u kubelet -f`
- Verify CNI plugin (Flannel) is running
- Check containerd status: `sudo systemctl status containerd`

### Cannot SSH to VM from cluster nodes
Solution:
- Configure static IP for VM
- Add VM IP to /etc/hosts on cluster nodes
- Verify SSH service is running: `sudo systemctl status ssh`

## Network Topology

```
Internet
    |
Mac Studio ([your-mac-ip])
    |
    +-- UTM VM: [vm-name]
        |
        +-- IP: [vm-ip] (or bridged IP)
        +-- Connects to: control-plane ([control-plane-ip]:6443)
```

## Resources Allocation

- Mac Studio Total: Assume 32GB RAM, 10 CPU cores
- VM Allocation: 4GB RAM, 2 CPU cores, 40GB disk
- Remaining for macOS: 28GB RAM, 8 CPU cores

## Security Considerations

1. SSH Keys: Use SSH keys for VM access
2. Firewall: Enable UFW and allow only necessary ports
3. Updates: Keep Ubuntu and Kubernetes components updated
4. Network Isolation: Consider network segmentation if needed

## Maintenance

### Regular Tasks
- Monitor VM resource usage
- Update Ubuntu packages monthly
- Update Kubernetes components when cluster is updated
- Backup VM configuration

### VM Backup
```bash
# On Mac Studio
# UTM VMs are stored in: ~/Library/Containers/com.utmapp.UTM/Data/Documents/
# Backup the entire VM folder
```

## References

- UTM Documentation: https://docs.getutm.app/
- Ubuntu Server ARM64: https://ubuntu.com/download/server/arm
- Kubernetes Documentation: https://kubernetes.io/docs/
- kubeadm Join: https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-join/

## Notes

- This setup uses UTM instead of Parallels/VMware because UTM is free and open-source
- ARM64 architecture is fully supported by Kubernetes
- VM performance on Apple Silicon is excellent due to native virtualization
- Network configuration may vary depending on Mac Studio network setup

## Document Information

- Created: 2026-03-13
- Last Updated: 2026-03-13
- Status: Planning Phase
