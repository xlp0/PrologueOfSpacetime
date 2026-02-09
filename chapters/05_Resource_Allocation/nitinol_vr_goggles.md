# Nitinol VR Goggles: The Adaptive Lens

**Project Phase**: New Hardware (Material Science)
**Curriculum Column**: Resource Allocation (Arithmetic)

## 1. The Philosophy of Memory
Most materials are amnesiac; bend a copper wire, and it stays bent. **Nitinol** (Nickel Titanium Naval Ordnance Laboratory) remembers.
*   **The Metaphor**: Energy (Current) restores Form (Geometry).
*   **The Physics**: Phase transition between *Martensite* (cold/deformable) and *Austenite* (hot/rigid).

## 2. Technical Implementation
We replace bulky servos with silent, contracting Nitinol wire wires to actuate the focus mechanism of a VR headset.

### Bill of Materials (BOM)
| Component | Spec | Approx. Cost |
| :--- | :--- | :--- |
| **Nitinol Wire** | 0.005" - 0.010" Flexinol (HT) | ~$10/m |
| **Lenses** | 42mm Biconvex (Cardboard style) | ~$5 |
| **Display** | 5.5" HDMI LCD or Smartphone | ~$50 / Owned |
| **Housing** | Custom 3D Printed (PLA/PETG) | ~$2 |
| **Driver** | MOSFET Module (IRF520) | ~$2 |
| **Microcontroller** | ESP32 (PWM Control) | ~$5 |

### The Mechanism
1.  **Relaxed State**: A spring pulls the lens holder *away* from the eye.
2.  **Active State**: We pass current through the Nitinol wire. It heats up, contracts (by ~4%), and pulls the lens holder *towards* the eye.
3.  **Control**: PWM (Pulse Width Modulation) controls the average current, allowing precise, silent focus adjustment.

### Circuit Diagram (Concept)
```
[ESP32 Pin] --> [Gate Resistor] --> [MOSFET Gate]
[12V/High Current Source] --> [Nitinol Wire] --> [MOSFET Drain] --> [GND]
```
*Warning: Nitinol requires high current. Do not drive directly from GPIO.*

## 3. The Project: Building Synthetic Muscle

> **Story Step: The Living Material**
> *We have built machines that move with gears. Now we build machines that move like flesh.*

### Step 1: Characterization
*   **Goal**: Measure the contraction.
*   **Task**: Hang a weight on the wire. Apply current. Measure the lift.

### Step 2: The Focus Motor
*   **Goal**: Print the `vr_lens_mount.stl`. Thread the wire.
*   **Code**:
    ```cpp
    // Focus Control
    int focus_val = map(potentiometer, 0, 4095, 0, 255);
    analogWrite(NITINOL_PIN, focus_val); // Heat = Contraction
    ```

### Next Step: Integration
Integrate this mechanism into the **Kinetic Node**. Perhaps the Node uses Nitinol to deploy its sensors silently?
