# LiDAR to ESP32-C3 Wiring & Implementation Guide

This document specifically outlines the architecture and wiring design for connecting the **X2 360° LiDAR** to an **ESP32-C3** (RISC-V) microcontroller.

## 1. Hardware Overview

- **Sensor:** YDLidar X2 (2D 360° Laser Radar Scanning)
- **IMU:** GY-521 / MPU6050 (for inclination tracking via I2C)
- **Motor Control:** A4988 Stepper Motor Driver (controlling NEMA 17)
- **Controller:** ESP32-S (3.3V Logic)
- **Communication Protocol:** UART (Serial)
- **Logic Level:** 3.3V (The LiDAR's logic level safely matches the ESP32)

---

## 2. Wiring Diagram

The LiDAR unit typically has a 4-pin connection: `VCC`, `GND`, `TX`, and `RX`.

> [!WARNING]
> **Power Requirement:** Most 360° LiDAR motors require 5V to spin reliably and draw significant current (often >300mA during start-up). **Do NOT connect the LiDAR's VCC to the ESP32's `3V3` pin**, as it will likely brown out the ESP32 or fail to spin the LiDAR. You must connect it to the `5V` (or `VIN` / `VBUS`) pin on your ESP32 dev board, provided you are powering the ESP32 via USB.

| LiDAR Pin | ESP32-WROOM Pin   | Description / Purpose                                                             |
| :-------- | :---------------- | :-------------------------------------------------------------------------------- |
| **VCC**   | **5V / VIN**      | **Power:** Provides 5V to the LiDAR motor & internal electronics.                 |
| **GND**   | **GND**           | **Ground:** Common ground connection.                                             |
| **TX**    | **RX2 (GPIO 16)** | **Data to ESP32:** LiDAR sends scan data (distance/angle points) *to* the ESP32.  |
| **RX**    | **TX2 (GPIO 17)** | **Command from ESP32:** ESP32 sends control commands (start/stop) *to* the LiDAR. |

*Note: For the standard ESP32-WROOM, we utilize `HardwareSerial Serial2` strictly mapped to GPIOs 16 and 17. Do not use pins 6-11 as they are connected to internal flash memory and will crash the board.*

---

## 3. Visual Wiring Schema

```mermaid
flowchart LR
    subgraph LiDAR [X2 360° LiDAR]
        L_VCC[VCC]
        L_GND[GND]
        L_TX[TX - Transmit]
        L_RX[RX - Receive]
    end

    subgraph ESP32 [ESP32-WROOM]
        E_VIN[VIN / 5V]
        E_GND[GND]
        E_RX2[RX2 / GPIO 16]
        E_TX2[TX2 / GPIO 17]
    end

    L_VCC ==>|5V Power| E_VIN
    L_GND ==>|Common Ground| E_GND
    L_TX -->|Scan Data| E_RX2
    L_RX <--|Control Commands| E_TX2
```

---

## 4. Software Implementation Notes

When configuring the code (Arduino IDE or ESP-IDF) to read the LiDAR:

1. **Hardware Serial:** Initialize `Serial2` for communication.
2. **Baud Rate:** The X2 LiDAR typically communicates at **115200 baud** (check specific datasheet if data is garbled).
3. **Power Supply Caution:** If the ESP32 restarts randomly during LiDAR spin up, the USB port may not be supplying enough peak current. Consider using a dedicated 5V 2A external power supply, ensuring you connect the external power supply's GND to the ESP32's GND.

> [!CAUTION]
> **Protocol Mismatch (Camsense X1 Protocol):** Many unbranded LiDARs sold as "X2" do not use the official YDLidar X2 packet structure. They often use the **Camsense X1 Protocol**. This broadcasts 36-byte packets with the header `0x55 0xAA 0x03 0x08`. In this protocol, angles require applying a `0xA000` offset (`angle = (AngleRaw - 0xA000) / 64.0`), otherwise the angles will be incredibly scattered and form false straight lines instead of accurate room boundaries. Ensure your parser specifically checks for this 36-byte structure!

### Example Initialization (C++ / Arduino IDE)
```cpp
#define LIDAR_RX_PIN 16 // Connects to LiDAR TX
#define LIDAR_TX_PIN 17 // Connects to LiDAR RX

void setup() {
  // Start Serial Monitor for debugging
  Serial.begin(115200); 
  
  // Start Serial1 for LiDAR communication
  // Baud rate: 115200, Serial Mode: SERIAL_8N1, RX pin, TX pin
  Serial1.begin(115200, SERIAL_8N1, LIDAR_RX_PIN, LIDAR_TX_PIN);
  
  Serial.println("LiDAR Serial Initialized.");
}

void loop() {
  // Read incoming LiDAR data
  if (Serial1.available()) {
    uint8_t incomingByte = Serial1.read();
    // Process distance and angle data packets here
  }
}
```

---

## 5. A4988 Stepper Motor Driver & NEMA 17 Wiring

The A4988 controls the micro-stepping rotation of the NEMA 17 motor (17HS3401/42BYGH34-607A) that articulates the LiDAR.

> [!WARNING]
> **Power Requirement (VMOT):** The A4988 requires a minimum of **8V** on the `VMOT` pin to operate. You cannot power `VMOT` from the ESP32's 5V or 3.3V pin. You must use a dedicated 9V or 12V power supply for the motor. **Never connect or disconnect the stepper motor while the driver is powered, or you will destroy the A4988.**

### A4988 to ESP32 (Logic Connections)

| A4988 Pin | ESP32 Connection | Purpose |
| :--- | :--- | :--- |
| **VDD** | **ESP32 3V3** | Logic Power (matches ESP32 3.3V logic level). |
| **GND (Logic)** | **ESP32 GND** | Logic Ground. |
| **STEP** | **ESP32 D18 (GPIO 18)** | Sends logic pulses to rotate the motor. |
| **DIR** | **ESP32 D19 (GPIO 19)** | Sets rotation direction (HIGH/LOW). |
| **SLEEP** | **A4988 RESET Pin** | Jumper wire directly connecting SLEEP to RESET to wake up the driver. |
| **RESET** | **A4988 SLEEP Pin** | See above. |

### A4988 to Stepper Motor (Confirmed Working Configuration)

| A4988 Pin | Motor Assembly Connection | Purpose |
| :--- | :--- | :--- |
| **1A (or A1)** | **Black Wire** | Coil 1 (Phase A) |
| **1B (or A2)** | **Red Wire** | Coil 1 (Phase A) |
| **2A (or B1)** | **Yellow Wire** | Coil 2 (Phase B) |
| **2B (or B2)** | **Blue Wire** | Coil 2 (Phase B) |

### A4988 to External Power Supply (12V)

| A4988 Pin | Power Source Connection | Purpose |
| :--- | :--- | :--- |
| **VMOT** | **12V Power Supply (+)** | Motor Power (Min 8V, Max 35V). **Add a 100μF capacitor across VMOT and GND!** |
| **GND (Motor)** | **12V Power Supply (-)** | Motor Ground. **CRITICAL: Must also be tied back to the ESP32 GND to complete the logic circuit.** |

### Configuring the A4988

1. **Microstepping (MS1, MS2, MS3):** For smooth, slow-panning rotation to scan the room accurately, wire `MS1`, `MS2`, and `MS3` to `VDD` (3.3V) to enable **1/16th Microstepping**. This changes the motor from 200 steps/rev to 3,200 steps/rev for extreme precision.
2. **Current Limit (VREF Tuning):** Before attaching the motor, you must tune the tiny potentiometer on the A4988. 
   - NEMA 17s often handle 1A to 1.5A per phase. 
   - Formula: `VREF = Current Limit * 8 * Rsen` (If Rsen is 0.1Ω, `VREF = 1A * 8 * 0.1 = 0.8V`).
   - Use a multimeter: Black probe on GND, Red probe touching the metal screw of the potentiometer. Turn the screw until it reads **~0.6V to 0.8V** to ensure the motor doesn't overheat.

---

## 6. GY-521 (MPU6050) IMU Wiring

The GY-521 tracks the physical 3D tilt of the spinning LiDAR assembly. It communicates via I2C.

| GY-521 Pin | ESP32-C3 Pin | Purpose |
| :--- | :--- | :--- |
| **VCC** | **ESP32 3V3** | Power for the IMU. |
| **GND** | **ESP32 GND** | Common Ground. |
| **SDA** | **ESP32 GPIO 8** (Default I2C) | Serial Data Line. |
| **SCL** | **ESP32 GPIO 9** (Default I2C) | Serial Clock Line. |

*In your code, you will use standard `.begin()` with the `<Wire.h>` library to read the pitch and roll offsets and apply them mathematically to the LiDAR's 2D array output to synthesize the 3D point cloud.*
