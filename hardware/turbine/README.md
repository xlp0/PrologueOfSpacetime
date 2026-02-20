# Basic Turbine Model (The Engine)

**Role**: To harness the flow of energy (Wind, Water, Chaos).
**Function**: Demonstrates **Fluid Dynamics** and **Rotational Force**.

## Generator Model (Advanced V2)
**File**: `turbine_generator.scad` (OpenSCAD)
**Function**: Converts wind into **Electricity** (High Efficiency).

**Components**:
1.  **Nacelle**: Split Body with **Clamp** (For firm Motor Grip).
2.  **Rotor (The Pro)**: **7 Blades** (Airfoil), **200mm Diameter**.
3.  **Spinner**: Aerodynamic Nose Cone.
4.  **Mount**: Fits on **1/2" PVC Pipe** (21.5mm OD).

**Hardware Required**:
*   **DC Motor**: Standard Hobby Motor (RF-300, ~24.5mm Dia).
*   **Pole**: Standard 1/2" PVC Pipe.
*   **Screws**:
    *   **2x M3 Screws** (20mm) + Nuts (For Motor Clamp).
    *   **1x M5 Screw** (30mm) (For Tower Swivel).
*   **Wires**: To connect motor.

## Basic Model (Simple)
**File**: `turbine_basic.scad` (OpenSCAD)
**Function**: Demonstrates **Fluid Dynamics** only (No electricity).

## Parameters
This model is **Parametric**. You can edit the variables at the top of the `.scad` file to change:
*   `blade_count`: Number of blades (Default: 8).
*   `twist_angle`: How much the blade twists (Default: 45°).
*   `blade_length`: Length of each blade.
*   `hub_d`: Size of the central hub.

## 3D Printing Instructions
**File**: `turbine_basic.scad` (OpenSCAD)
**Material**: PETG or PLA (Stronger is better for high speed)
**Settings**:
*   Layer Height: 0.2mm
*   Infill: 20-40% (Needs strength)
*   Supports: **Required** (Blades have overhangs) OR Print Flat if possible (though twist makes this hard). Usually print Hub-Down with supports.

## Uses
*   **Wind Tunnel**: Test aerodynamics.
*   **Water Wheel**: Harness stream flow.
*   **Drone Propeller**: (Theoretical - needs airfoil optimization).
