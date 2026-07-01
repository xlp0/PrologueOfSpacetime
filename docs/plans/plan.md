# Project Plan: Arduino Powered Micro Quadruped

## 1. Procurement

**Hardware Components:**
* 12x SG90 Servo Motor
* 1x Arduino Nano V3.0 ATMEGA328P Null
* 1x 100uF 16V Plugin D5xL7mm Aluminum Electrolytic Capacitors KS107M016D07RR0VH2FP0 CX(承兴)
* 12x 2.54mm Straight 1x3P Plugin Pin Male Headers 2.54-1*3P BOOMELE
* 1x Latching Straight DPDT Plugin Push Switches PS-5850A-6PL G-Switch
* 1x Straight 5mm Plugin Screw Terminal DB301V-5.0-2P DIBO
* 1x Red Plugin D=3mm Light Emitting Diodes 204-10SURD/S530-A3-L EVERLIGHT
* 1x Carbon Resister 330Ω Plugin Through Hole Resistors CF1/4W-330Ω±5% T CCO
* 2x 18650 Li-ion Battery
* 1x 18650 Battery Case 2 Slots
* 2x 470uF 10V Plugin,D8xL7mm Aluminum Electrolytic Capacitors KS477M010F07RR0VH2FP0 CX(承兴)
* 2x 2.54mm Straight 1x15P 15 Plugin Female Headers B-2200S15P-A120 Ckmtw

**Tools:**
* Soldering Station
* Soldering Wire
* Wire Cutter
* Silicone Soldering Mat
* Isopropyl Electronics Cleaner

## 2. 3D Printing (Mechanical Parts)
Fabricate the mechanical parts using the provided STL files. SLA (resin) printing is highly recommended over FDM (PLA) to ensure dimensional accuracy and smooth surfaces without requiring extra sanding.
* `body_d.stl`
* `body_u.stl`
* `coxa_l.stl`
* `coxa_r.stl`
* `femur_1.stl`
* `tibia_l.stl`
* `tibia_r.stl`
* `s_hold.stl`

## 3. Step-by-Step Execution

1.  **Mechanical Assembly (Phase 1):** Assemble the 3D-printed structural parts. Do not attach the servo rocker arms yet.
2.  **PCB Preparation:** Solder the electronic components (headers, capacitors, switch, and terminals) onto the custom PCB to avoid the complexity of a breadboard circuit.
3.  **Servo Calibration:** * Connect the Arduino Nano to your computer.
    * Upload the `quadruped_legs_correction.ino` code.
    * Connect the servos to the board to rotate and lock all positions to exactly **90 degrees**.
4.  **Rocker Arm Attachment:** Once servos are locked at 90 degrees, assemble the servo rocker arms onto the servos as shown in the design.
5.  **Final Mechanical Assembly:** Complete the robot assembly by securing the legs to the main body.
6.  **Software Configuration:**
    * Install the `FlexiTimer2` library in the Arduino IDE.
    * Verify servo motor matches and pin numbers connected to the feet within the code.
7.  **Main Code Upload:** Remove the Nano board from the circuit and upload the `quadruped_spider_robot_code.ino`.
8.  **Activation:** Re-insert the Nano, connect the batteries, and power on to initiate the pre-programmed sequences.

## 4. Servo Calibration
*Important:* Always remove the Arduino Nano board from the main circuit before uploading any code.
1. Connect the 12 SG90 servo motors to the Arduino Nano.
2. Upload the `quadruped_legs_correction.ino` code to the Arduino.
3. Wait for the code to rotate and lock all servo positions to exactly 90 degrees. 

## 5. Hardware Assembly
1. With the servos locked at 90 degrees, attach the servo rocker arms to the 3D-printed parts. 
2. Assemble the structural components (body, coxa, femur, and tibia).
3. Solder the electronic components based on the provided schematic layout (`Schematic_SpiderRobotNanoBoard_2023-03-02.png`).

## 6. Final Programming
1. Download and add the `FlexiTimer2` library to your Arduino IDE.
2. Verify that the servo motor connections and pin numbers match the assigned legs in the code.
3. Remove the Arduino Nano board from the circuit.
4. Upload the main source code (`quadruped_spider_robot_code.ino`).
5. Reconnect the Arduino Nano, insert the batteries, and power on the robot.