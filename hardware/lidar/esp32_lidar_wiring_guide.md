# LiDAR to ESP32-C3 Wiring & Implementation Guide

This document specifically outlines the architecture and wiring design for connecting the **X2 360° LiDAR** to an **ESP32-C3** (RISC-V) microcontroller.

## 1. Hardware Overview

- **Sensor:** YDLidar X2 (2D 360° Laser Radar Scanning)
- **Controller:** ESP32-C3 (3.3V Logic)
- **Communication Protocol:** UART (Serial)
- **Logic Level:** 3.3V (The LiDAR's logic level safely matches the ESP32)

---

## 2. Wiring Diagram

The LiDAR unit typically has a 4-pin connection: `VCC`, `GND`, `TX`, and `RX`.

> [!WARNING]
> **Power Requirement:** Most 360° LiDAR motors require 5V to spin reliably and draw significant current (often >300mA during start-up). **Do NOT connect the LiDAR's VCC to the ESP32's `3V3` pin**, as it will likely brown out the ESP32 or fail to spin the LiDAR. You must connect it to the `5V` (or `VIN` / `VBUS`) pin on your ESP32 dev board, provided you are powering the ESP32 via USB.

| LiDAR Pin | ESP32-WROOM Pin | Description / Purpose |
| :--- | :--- | :--- |
| **VCC** | **5V / VIN** | **Power:** Provides 5V to the LiDAR motor & internal electronics. |
| **GND** | **GND** | **Ground:** Common ground connection. |
| **TX** | **RX1 (GPIO 6)** | **Data to ESP32:** LiDAR sends scan data (distance/angle points) *to* the ESP32. |
| **RX** | **TX1 (GPIO 7)** | **Command from ESP32:** ESP32 sends control commands (start/stop) *to* the LiDAR. |

*Note: The ESP32-C3 only has two hardware UARTs. Since UART0 is used for flashing and monitor, we map `HardwareSerial Serial1` to pins 6 and 7 to securely handle the LiDAR data stream.*

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

    subgraph ESP32 [ESP32-C3]
        E_VIN[VIN / 5V]
        E_GND[GND]
        E_RX1[RX1 / GPIO 6]
        E_TX1[TX1 / GPIO 7]
    end

    L_VCC ==>|5V Power| E_VIN
    L_GND ==>|Common Ground| E_GND
    L_TX -->|Scan Data| E_RX1
    L_RX <--|Control Commands| E_TX1
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
