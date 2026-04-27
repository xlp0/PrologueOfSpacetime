# Project Plan: Arduino Powered Micro Quadruped

## 1. Project Overview
A compact, robust, and low-cost quadruped robot designed for experimenting with complex gaits and dynamic locomotion using Inverse Kinematics (IK).

## 2. Bill of Materials (BOM)

### Electronics
*   **Microcontroller:** 1x Arduino Uno
*   **Actuators:** 12x TowerPro MG90S Micro Servos (Metal gear recommended)
*   **Shield:** 1x Arduino Sensor Shield (V5 preferred for external power ports)
*   **Power:** External 5V power supply (Servos should not draw power directly from the Arduino 5V pin)
*   **USB:** USB cable for programming

### Hardware & Tools
*   **3D Printer & Filament:** PLA (approx. 20 hours print time)
*   **Fasteners:** Standard M2/M3 screws (included with servos or sourced separately)

## 3. Digital Fabrication (3D Printing)

### Print Settings
*   **Infill:** 40%
*   **Perimeters:** 2
*   **Layer Height:** 0.1mm
*   **Nozzle:** 0.4mm

### Component List (22 Parts Total)
*   `leg1` (4x)
*   `leg2` (4x) + `leg2_cover` (4x)
*   `leg3` (2x) + `leg3_cover` (2x)
*   `leg3_mirror` (2x) + `leg3_mirror_cover` (2x)
*   `body` (1x)
*   `wire_cover` (1x)
*   *Optional:* `servo_horn_spacer` (24x) if screws are too long.

## 4. Mechanical Assembly

### Phase 1: Link Preparation
1.  Insert servo horns into `leg2` and secure with `leg2_cover`.
2.  Mount MG90S servos into `leg1`.

### Phase 2: Leg Assembly
1.  Insert servo horns into `leg3` and `leg3_mirror` components.
2.  Route wires from `leg1` servo through management slots in `leg3`.
3.  Secure `leg3_cover` and mount the second servo into the `leg3` assembly.

### Phase 3: Body & Final Integration
1.  Mount 4 servos to the `body` frame using internal screws to avoid leg interference.
2.  Connect the `leg3` assemblies to the body servos.
3.  Connect `leg2` links to join the body/thigh servos to the knee (`leg1`) servos.

## 5. Electronics & Wiring

### Power Modification
*   **Critical:** If using a Sensor Shield without a dedicated external power port, bend the shield's 5V pin so it does not connect to the Arduino. Provide 5V external power directly to the shield to prevent damaging the Arduino.

### Pin Mapping
| Leg | Hip 1 (Body) | Hip 2 (Thigh) | Knee |
| :--- | :--- | :--- | :--- |
| **FL (Front Left)** | Pin 7 | Pin 6 | Pin 5 |
| **FR (Front Right)** | Pin 4 | Pin 3 | Pin 2 |
| **BL (Back Left)** | Pin 13 | Pin 12 | Pin 11 |
| **BR (Back Right)** | Pin 10 | Pin 8 | Pin 9 |

## 6. Software & Calibration

### Initial Calibration (Zeroing)
1.  Download source code: [GitHub Repository](https://github.com/kousheekc/Micro-Quadruped-Robot)
2.  Upload the initialization code to set all servos to 90°.
3.  Attach mechanical links only after servos are powered and centered.
4.  Fine-tune offsets in the `zero_positions` array in `Quadruped.h` until legs are perfectly straight.
5.  ***Tutorial:** https://www.instructables.com/Arduino-Powered-Micro-Quadruped

### Gait Control
*   The system uses **Inverse Kinematics (IK)**. 
*   Use the `pos(x, y, z)` function to define foot coordinates; the library will automatically calculate the required joint angles.

## 7. Future Scalability
*   **Sensors:** Add IMU (MPU6050) for balance or Ultrasonic/LiDAR for obstacle avoidance.
*   **Manipulators:** Add a micro-gripper to the top mounting points.