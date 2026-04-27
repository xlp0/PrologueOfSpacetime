# How to Make Quadruped Spider Robot (using Arduino and 3D parts)

## 1. Project Overview
This project involves building a 4-legged spider robot (quadruped) that utilizes precise calculations and pre-programmed leg sequences for movement. The mechanical parts are custom-designed for 3D printing, specifically optimized for SLA (Resin) printing to ensure dimensional accuracy and smooth surface finishing.

## 2. Bill of Materials (BOM)

### Electronics
*   **Microcontroller:** 1x Arduino Nano V3.0 (ATmega328P)
*   **Actuators:** 12x SG90 Servo Motors
*   **Power Management:**
    *   1x LDO Voltage Regulator (5V/3A) (e.g., MIC29310-5.0WT, LM1085IT-5.0)
    *   2x 18650 Li-ion Batteries + 2-Slot Battery Case
    *   1x 6-Pin Self-Locking Switch (8x8mm)
    *   1x Screw Terminal Block Connector (5mm)
*   **Capacitors:**
    *   1x 100uF 16V Electrolytic Capacitor
    *   2x 470uF 10V Electrolytic Capacitors
*   **Connectors & Indicators:**
    *   12x Male Headers (2.54mm, 1x3P)
    *   2x Female Headers (2.54mm, 1x15P)
    *   1x LED (3mm, Red) + 1x Resistor (330Ω)

### 3D Printed Parts (STL)
*   **Body:** `body_d.stl` (Down), `body_u.stl` (Up)
*   **Coxa:** `coxa_l.stl`, `coxa_r.stl`
*   **Femur:** `femur_1.stl`
*   **Tibia:** `tibia_l.stl`, `tibia_r.stl`
*   **Support:** `s_hold.stl`

## 3. Fabrication & Tools

### Recommended Tools
*   Soldering Station & Wire
*   Wire Cutter
*   Silicone Soldering Mat
*   Isopropyl Electronics Cleaner

### 3D Printing Note
SLA (Resin) printing is highly recommended for this project. FDM (PLA) prints may require significant sanding and post-processing to ensure that moving mechanical parts fit correctly and move smoothly.

## 4. Assembly & Software Setup

### Phase 1: Servo Calibration (90° Centering)
1.  **Important:** Before assembling the rocker arms, all servos must be centered.
2.  Upload `quadruped_legs_correction.ino` to the Arduino Nano.
3.  This code rotates all servos to the 90-degree position.
4.  Once centered, attach the servo rocker arms.

### Phase 2: Main Programming
1.  **Library Requirement:** Install the **FlexiTimer2** library ([GitHub Link](https://github.com/wimleers/flexitimer2)).
2.  Upload the main source code: `quadruped_spider_robot_code.ino`.
3.  **Safety Note:** Remove the Nano board from the circuit/shield while uploading code to prevent power conflicts.

### Phase 3: Hardware Verification
*   Check the servo motor matching and verify that the pin numbers in the code correspond to the physical connections on the board.

## 5. Resources
*   **Tutorial:** [Instructables Guide](https://www.instructables.com/Arduino-Powered-Micro-Quadruped)
*   **Service & Files:** [PCBWay Project Page](https://www.pcbway.com/project/shareproject/)
