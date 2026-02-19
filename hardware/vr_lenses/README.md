# VR Lens Holder (The Synthesist's Eye)

**Role**: To hold the optics (Lenses) for the VR Headset, enabling Stereoscopic Vision.
**Function**: Digital Synesthesia Interface (The Screen -> The Eye).

## Hardware Specs
*   **Outer Diameter**: 37mm
*   **Total Height**: 3mm (3 Layers × 1mm)
*   **Aperture**: 22mm (Bottom 2 Layers)
*   **Lens Seat**: 24mm (Top 1 Layer)
*   **Fit**: Press-fit into Google Cardboard or similar VR Viewer.

## How to Turn `.scad` into `.stl`
To print this design, you need to convert the **Code** (SCAD) into a **3D Mesh** (STL).

1.  **Download**: Get [OpenSCAD](https://openscad.org/) (Free & Open Source).
2.  **Open**: Launch OpenSCAD and open `lens_holder.scad`.
3.  **Preview**: Press **F5** to see the 3 rings side-by-side.
4.  **Render**: Press **F6** (or *Design > Render*). This calculates the solid geometry.
5.  **Export**: Press **F7** (or *File > Export > Export as STL*). Save the file.
6.  **Slice**: Open the `.stl` file in your 3D Printer Slicer (Cura, PrusaSlicer, etc.) and print.

## 3D Printing Instructions
**File**: `lens_holder.scad` (OpenSCAD)
**Material**: PLA (Black recommended to reduce reflection)
**Settings**:
*   Layer Height: 0.1mm to 0.2mm (Precision needed for threads/steps)
*   Infill: 100% (Thin part)
*   Supports: None (Flat design)

## Assembly (The Stack)
1.  **Print File 1** (`lens_holder.scad`): Generates **6 discs** (Standard Set).
    *   **4x** Aperture Discs (22mm hole)
    *   **2x** Lens Seat Discs (24mm hole)
2.  **Print File 2** (`middle_layer.scad`): Generates **2 discs** (Middle Layer).
    *   **2x** Wide Aperture Discs (25mm hole, 2mm thick)
3.  **Stack Order** (Adjust keying as needed):
    *   **Base**: Aperture Disc (22mm)
    *   **Middle**: Wide Aperture Disc (25mm) - *Optional Spacer*
    *   **Top**: Lens Seat Disc (24mm)
4.  **Lens**: Place the 24mm Lens into the Top Disc.
5.  **Bond**: Glue the stack together.
6.  **Insert**: Place the completed stack into the VR Headset slot.
