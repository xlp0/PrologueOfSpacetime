# Digital Synesthesia: The Oscilloscope

**Role**: The Biologist (Isaac Szpindel)
**Function**: To visualize the invisible (Voltage) as Geometry (Digital Synesthesia).

## Hardware Required
1.  **Arduino Uno or Nano**: The brain.
2.  **SSD1306 OLED Display (0.96" I2C)**: The eye.
3.  **Jumper Wires**: The nerves.
4.  **Signal Source**: A 555 timer, a battery, or a simple PWM signal.

## Wiring (I2C)
| Component | Arduino Uno | Arduino Nano |
| :--- | :--- | :--- |
| **OLED VCC** | 5V | 5V |
| **OLED GND** | GND | GND |
| **OLED SDA** | A4 | A4 |
| **OLED SCL** | A5 | A5 |
| **Input Signal** | A0 | A0 |

## Software Setup
1.  Install **Arduino IDE**.
2.  Install Libraries:
    *   `Adafruit SSD1306`
    *   `Adafruit GFX Library`
3.  Open `arduino_scope.ino`.
4.  Upload to board.

## 3D Printing (The Case)
**File**: `oscilloscope_case.scad` (OpenSCAD)
**Material**: PLA or PETG.
**Settings**:
*   Layer Height: 0.2mm
*   Infill: 20%
*   Supports: None (Designed for Flat Printing)

**Assembly**:
1.  Print Case and Lid.
2.  Slide OLED into top cutout (press fit or glue).
3.  Mount Arduino Nano inside.
4.  Route wires through front hole.
5.  Snap Lid shut.

## The Experience
When you touch the probe (A0) to a circuit, you will see the **Voltage Waveform** on the screen.
*   **Flat Line**: Silence / Death.
*   **Sine Wave**: Harmony.
*   **Square Wave**: Logic / Digital.
*   **Noise**: Entropy / Rorschach.

This is **Digital Synesthesia**: Seeing the "Feeling" of the electricity.
