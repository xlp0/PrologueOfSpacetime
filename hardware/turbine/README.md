# Basic Turbine Model (The Engine)

**Role**: To harness the flow of energy (Wind, Water, Chaos).
**Function**: Demonstrates **Fluid Dynamics** and **Rotational Force**.

## Generator Model (Advanced)
**File**: `turbine_generator.scad` (OpenSCAD)
**Function**: Converts wind into **Electricity**.

**Components**:
1.  **Nacelle**: Holds the Motor (24mm Diameter).
2.  **Rotor**: Hub + 3 Blades (Press-fits onto 2mm Shaft).
3.  **Tail**: Self-orienting Fin.
4.  **Mount**: Fits onto a 15mm Pole/Pipe.

**Hardware Required**:
*   **DC Motor**: Standard Hobby Motor (RF-300 or similar, ~24mm Diameter).
*   **Wires**: To connect motor to LED or Multimeter.

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
