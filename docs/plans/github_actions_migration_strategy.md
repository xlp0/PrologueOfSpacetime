# Migrating from GitHub-Hosted Actions to Self-Hosted CI/CD

## Motivation
Currently, our Continuous Integration and Continuous Deployment (CI/CD) pipelines are running directly on GitHub-hosted runners. This approach has a few drawbacks for our specific setup:
1. **Resource Control**: We have powerful local hardware (Mac Studio running Kubernetes) that is underutilized.
2. **Security & Privacy**: Pushing deployments from GitHub directly to our internal network requires opening firewalls or exposing the Kubernetes API, which violates zero-trust principles.
3. **Cost & Limits**: GitHub-hosted runners have execution time limits and potential costs for private repositories.

To resolve this, we need to transition our workloads into our own environment.

## Recommended Strategy: GitOps with Argo CD + ARC

To maintain developer experience while migrating infrastructure inward, the recommended approach is a combination of two tools running on our local Kubernetes cluster:

### 1. Continuous Deployment (CD) with Argo CD
**Argo CD** is a declarative, GitOps continuous delivery tool for Kubernetes.
- Instead of GitHub Actions running commands like `kubectl apply` and pushing changes to our cluster, **Argo CD** runs *inside* our cluster.
- It continuously monitors a dedicated Git repository that contains our Kubernetes manifests.
- When it detects a change in Git, Argo CD automatically pulls the changes and reconciles the cluster state.
- **Benefit**: Our cluster no longer needs to be exposed to the internet. The cluster pulls down changes securely.

### 2. Continuous Integration (CI) with Actions Runner Controller (ARC)
We can continue using the familiar GitHub Actions syntax (`.github/workflows/`), but execute those jobs on our own hardware.
- **Actions Runner Controller (ARC)** is a Kubernetes operator that orchestrates self-hosted runners for GitHub Actions.
- When a GitHub Action is triggered, ARC spins up a temporary Pod in our Mac Studio Kubernetes cluster to execute the CI job (e.g., building, testing, linting, building Docker images).
- **Benefit**: We utilize our local compute power, keep source code closer to our local infrastructure, and don't need to rewrite all our current CI pipelines into a new format.

---

## Automatic Detection & Synchronization

One of the main questions is whether Argo CD can automatically detect "actions or changes" done by the user (e.g., developers pushing new code or creating new releases). **Yes, this is entirely possible and forms the core of GitOps.**

Here is what is possible and how the automatic detection pipeline works:

1. **Git Webhooks (Instant Detection)**: By default, Argo CD polls the Git repository every 3 minutes for changes. We can configure GitHub to send a **Webhook** directly to our Argo CD instance. Whenever a user pushes a commit or merges a pull request, GitHub instantly notifies Argo CD, which immediately begins the synchronization and deployment process.
   
2. **Argo CD Image Updater (Detecting New Builds)**: When a developer pushes code, our self-hosted CI (ARC) will build a new Docker image and push it to a container registry. We can install **Argo CD Image Updater** in our cluster. It monitors the registry, and when it sees a new Docker image tag for our application, it automatically detects it and tells Argo CD to deploy the new version without the user manually changing the Kubernetes manifest.

3. **Auto-Sync vs. Manual Sync**:
   - **Auto-Sync Enabled**: Argo CD will automatically apply the changes to the cluster as soon as it detects them.
   - **Manual Sync**: Argo CD will detect the changes and mark the application as "Out of Sync," but waits for a human to press the "Sync" button (good for production environments).

**What is Not Possible?**
- Argo CD cannot automatically generate Kubernetes manifests for your code. The configurations (Deployments, Services, Ingress) must already exist in a Git repository or Helm chart. Once they exist, Argo CD handles everything else automatically.

---

## Alternative Solutions

### A. Full Replacement: Argo Workflows & Argo Events
Instead of using GitHub Actions at all, we can replace the entire CI system with **Argo Workflows**.
- **Pros**: Completely independent of GitHub. Native to Kubernetes. Extremely powerful for complex parallel tasks.
- **Cons**: High learning curve. Requires rewriting all existing `.github/workflows` YAML files into Argo Workflow format.

### B. Lightweight Local CI: Gitea + Act Runner
If we want to move entirely away from GitHub in the future, we could host our own Git server (Gitea) inside our network and use Gitea Actions (which uses the `act` project to run GitHub Action-compatible workflows locally).

## Required Credentials & Secrets

To ensure the build and deployment processes run seamlessly on our self-hosted infrastructure, we must provision and store the following credentials securely as Kubernetes Secrets:

1. **GitHub Personal Access Token (PAT) or GitHub App Private Key**:
   - **For ARC**: Required for the Actions Runner Controller to authenticate with GitHub, register the self-hosted runners, and receive job payloads.
   - **For Argo CD (Private Repos)**: Required to read the Kubernetes manifests from our private repositories.

2. **Container Registry Credentials (e.g., Docker Hub, AWS ECR, or GHCR)**:
   - **For CI (ARC)**: The GitHub Action runner needs these credentials to push newly built Docker images to the registry.
   - **For CD (Argo CD Image Updater)**: Needed to monitor the registry for new image tags and update the deployments automatically.
   - **For Kubernetes Nodes**: Required as `imagePullSecrets` so the cluster itself can pull the private images to run the containers.

3. **Webhook Secrets (Optional but Recommended)**:
   - Used to secure the webhooks sent from GitHub to Argo CD so it can immediately detect pushes, preventing unauthorized parties from triggering synchronizations.

---

## Next Steps for Implementation

1. **Install Argo CD**: Deploy Argo CD onto the Mac Studio Kubernetes cluster. Set up the foundational GitOps repository.
2. **Move CD out of GitHub Actions**: Remove any `kubectl apply` or deployment steps from existing GitHub workflows. Let Argo CD handle deployments.
3. **Install ARC (Actions Runner Controller)**: Deploy ARC into the cluster. Authenticate it against our GitHub organization/repository.
4. **Transition Workflows**: Update our `.github/workflows/*.yaml` files to change `runs-on: ubuntu-latest` to our new custom runner labels (e.g., `runs-on: self-hosted-mac-studio`).

This phased approach allows us to securely stop running critical actions on GitHub infrastructure, shift the effort to our local Mac Studio Kubernetes cluster, and cleanly separate CI (building things) from CD (deploying things).
