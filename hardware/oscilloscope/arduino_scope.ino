/*
  Digital Synesthesia: The Biologist's Oscilloscope (Arduino Sketch)

  Object: Visualize "Voltage" as "Shape" (Geometry/Synesthesia).
  Hardware: Arduino Uno/Nano + SSD1306 OLED (128x64) + Analog Input (A0).
  Library: Adafruit_SSD1306, Adafruit_GFX.

  Connect:
  - OLED SDA -> A4 (Uno) / D4 (ESP8266)
  - OLED SCL -> A5 (Uno) / D5 (ESP8266)
  - Input Signal -> A0
*/

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Wire.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Buffer for waveform
int yBuffer[128];
int readIndex = 0;

void setup() {
  Serial.begin(115200);

  // Initialize OLED
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;)
      ;
  }

  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println(F("Digital Synesthesia"));
  display.println(F("Initializing..."));
  display.display();
  delay(1000);

  // Initialize buffer
  for (int i = 0; i < 128; i++) {
    yBuffer[i] = SCREEN_HEIGHT / 2;
  }
}

void loop() {
  // 1. Read Sensor (The Biologist's Hand)
  int sensorValue = analogRead(A0);

  // 2. Map to Screen Coordinates (The Transformation)
  // Inverse logic: 0 is top, 63 is bottom. So high voltage (1023) -> 0 (top)
  int yVal = map(sensorValue, 0, 1023, SCREEN_HEIGHT - 1, 0);

  // 3. Shift Buffer (Time Moving Forward)
  for (int i = 0; i < 127; i++) {
    yBuffer[i] = yBuffer[i + 1];
  }
  yBuffer[127] = yVal;

  // 4. Draw Waveform (The Geometry)
  display.clearDisplay();

  // Grid lines (Optional Context)
  display.drawLine(0, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT / 2,
                   SSD1306_WHITE); // Center line

  // Waveform
  for (int i = 0; i < 127; i++) {
    display.drawLine(i, yBuffer[i], i + 1, yBuffer[i + 1], SSD1306_WHITE);
  }

  // 5. Output Data (The Synesthetic Protocol)
  // Send to Serial for Grafana/Python integration
  Serial.print("Voltage:");
  Serial.println(sensorValue);

  display.display();
  // Speed control (remove delay for max speed)
  // delay(1);
}
