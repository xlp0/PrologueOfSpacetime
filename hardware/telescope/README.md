# The Telescope (The Astronomer's Eye)

**Role**: To observe the Firefall (65,536 Probes).
**Function**: Magnification and Light Gathering.

## Hardware Required
To make this a *working* telescope, you need:

1.  **Objective Lens** (The Big One):
    *   **Diameter**: **50mm** (Standard DIY size).
    *   **Focal Length**: **360mm** (Short Tube / Travel Scope).
    *   *Source*: Surplus Shed, Amazon "50mm Doublet Lens", or a cheap $20 telescope kit.

2.  **Eyepiece** (The Small One):
    *   **Size**: **1.25"** (31.75mm) Standard Diameter.
    *   **Focal Length**: 20mm (Low Power) or 10mm (High Power).

3.  **Tube Material**:
    *   **Option A (3D Printed)**: Print multiple sections of the `main_tube` to reach 360mm length.
    *   **Option B (PVC Pipe)**: Use a 2-inch PVC pipe and adapt the cells (Recommended for strength).

## 3D Printing Instructions
**File**: `telescope_assembly.scad`
**Parts**:
1.  **Main Tube / Lens Cell**: Holds the 50mm Lens.
2.  **Focuser Tube**: Slides inside the main tube. Holds the Eyepiece.
3.  **Dew Shield**: Prevents stray light.

**Settings**:
*   **Material**: PLA (Black or Dark Grey to stop light leaks).
*   **Infill**: 20%
*   **Supports**: Required for the Focuser Knob overhangs.
