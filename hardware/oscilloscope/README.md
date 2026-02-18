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

## The Experience
When you touch the probe (A0) to a circuit, you will see the **Voltage Waveform** on the screen.
*   **Flat Line**: Silence / Death.
*   **Sine Wave**: Harmony.
*   **Square Wave**: Logic / Digital.
*   **Noise**: Entropy / Rorschach.

This is **Digital Synesthesia**: Seeing the "Feeling" of the electricity.
