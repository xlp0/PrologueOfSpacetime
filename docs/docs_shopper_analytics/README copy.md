 # Shopper Analytics AI (PoC)

**AI System for Shopper Analytics using Xbox Kinect**

## Project Overview

### Background
Merchandising evaluation and shopper behavior analysis are currently largely manual processes, resulting in inconsistent visibility of in-store conditions. Business decisions require objective insights into product availability on shelves and shopper movement patterns.

This **Shopper Analytics PoC** builds AI capabilities to generate measurable and anonymous visual insights to solve these challenges.

### Objectives
1.  **Stock Availability**: Detect whether products are visibly available or missing in observed shelf areas.
2.  **Traffic Flow Analysis**: Generate analytics on shopper movement, including:
    *   Entry points.
    *   First area visited.
    *   Flow toward checkout.
3.  **Hotspot Identification**: Identify areas that frequently receive attention or visits during the shopper journey.

---

## Scope of Work & Deliverables

### 1. AI Shopper Analytics Model
An AI model designed to generate stock availability indicators and shopper traffic flow analytics within the PoC scope.

*   **Stock Availability Analytics**: Visual analysis to identify product presence on shelves (visual check only, no backend inventory integration).
*   **Shopper Traffic Flow Analytics**: Analysis of movement patterns, entry points, and high-attention areas.

### 2. Shopper Analytics Dashboard
A visualization dashboard presenting:
*   Stock availability status (Available / Not Available).
*   Traffic flow visualization (Heatmaps, visit summaries, movement flows).

### 3. Camera System (Hardware)
*   **Device**: Xbox Kinect (v1/v2) or Azure Kinect.
*   **Role**: Collects RGB and Depth data for anonymous tracking.
*   **Provisioning**: Installed and configured to cover agreed PoC observation areas.

---

## Technical Setup

### Prerequisites
*   **macOS** or Linux.
*   **Python 3.9+**.
*   **uv** (Python package manager).
*   **Xbox Kinect** (USB model) + `libfreenect` drivers.

### Installation

1.  **Install `uv`** (if not installed):
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2.  **Install System Drivers (macOS)**:
    ```bash
    brew install libfreenect
    ```

3.  **Install Project Dependencies**:
    ```bash
    uv sync
    # OR manually:
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt
    ```

### Usage

Run the main application:
```bash
uv run src/main.py
```

*   **RGB Feed**: Shows the live camera view with motion tracking overlays.
*   **Depth Feed**: Shows the infrared depth map.
*   **Controls**: Press **`q`** to quit the application.

---

## Data & Privacy

| Data Category | Description | PoC Scope Notes |
| :--- | :--- | :--- |
| **Observation Video** | Store area recordings | Duration ±3–4 weeks |
| **Shopper Traffic** | Movement patterns | Visual flow (Entry → Browse → Checkout) |
| **Stock Availability** | Visual product presence | No internal stock validation |
| **Privacy** | **Anonymous Tracking** | Uses Depth/Shape data; no facial recognition storage |