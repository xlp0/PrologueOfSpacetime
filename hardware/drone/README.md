# The Sovereign Drone (The Eye)

**Role**: to detach the "Self" from gravity. To see the system from all angles (HoTT Path Tracing).
**Function**: **Autonomous Pathfinding** and **FPV Observation**.

## The Frame
**File**: `chassis.scad` (OpenSCAD)
**Configuration**: **True-X Quadcopter** (Symmetrical).
**Size**: **5-inch Props** (Standard Racing Size).
**Material**: Print in **PETG** or **Carbon-Nylon** (PLA will melt in the sun/crash).

## Hardware BOM (Bill of Materials)
To build a functional Sovereign Eye, you need:

1.  **Motors**: 4x **2207 Brushless Motors** (2300-2600KV).
2.  **Flight Controller (FC)**: Standard F4 or F7 Controller (30.5mm x 30.5mm Mount).
    *   *Role*: The "Cerebellum" (Stabilization).
3.  **ESC** (Electronic Speed Controller): 4-in-1 ESC (30.5mm Mount).
4.  **Camera**: Micro FPV Camera (19mm width).
    *   *Role*: The "Eye" (Input Sensor).
5.  **Video Transmitter (VTX)**: 5.8GHz VTX.
    *   *Role*: The "Optic Nerve" (Data Transmission).
6.  **Receiver (RX)**: ELRS or Crossfire (Long Range).

## Assembly
1.  **Print**: The Frame (Arms + Center Plate).
2.  **Mount Motors**: Use M3 Screws on the 16x19mm pattern.
3.  **Stack**: Mount the ESC and FC in the center (30.5mm holes).
4.  **Camera**: Slot the FPV camera into the front bracket.
