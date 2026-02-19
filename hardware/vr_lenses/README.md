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
1.  **Print**: The file generates 3 separate discs laid flat.
    *   **2x** Aperture Discs (22mm hole)
    *   **1x** Lens Seat Disc (24mm hole)
2.  **Stack**:
    *   **Bottom**: Aperture Disc (22mm)
    *   **Middle**: Aperture Disc (22mm)
    *   **Top**: Lens Seat Disc (24mm)
3.  **Lens**: Place the 24mm Lens into the Top Disc.
4.  **Bond**: Glue the stack together (Superglue/CA Glue) or press-fit into the headset.
5.  **Insert**: Place the completed 3mm stack into the VR Headset slot.
