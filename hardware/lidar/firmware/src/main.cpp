#include <Arduino.h>

#define LIDAR_RX_PIN 6 
#define LIDAR_TX_PIN 7 

void setup() {
  Serial.begin(115200);
  delay(1000); 
  Serial.println("\n--- ESP32-C3 LiDAR Parser Started ---");
  Serial1.begin(115200, SERIAL_8N1, LIDAR_RX_PIN, LIDAR_TX_PIN);
}

// Camsense X1 / YDLidar X2 clone packet state machine
uint8_t packet[36]; 
int p_idx = 0;
bool syncing = true;

void loop() {
  if (Serial1.available()) {
    uint8_t b = Serial1.read();
    
    if (syncing) {
      if (b == 0x55) { // First byte
        packet[0] = b;
        p_idx = 1;
        syncing = false;
      }
    } else {
      packet[p_idx++] = b;
      
      // Check fixed header sequence: 55 AA 03 08
      if (p_idx == 2 && packet[1] != 0xAA) { syncing = true; p_idx = 0; }
      else if (p_idx == 3 && packet[2] != 0x03) { syncing = true; p_idx = 0; }
      else if (p_idx == 4 && packet[3] != 0x08) { syncing = true; p_idx = 0; }
      
      else if (p_idx == 36) { // Full packet received
        // Start and End Angles
        uint16_t saRaw = packet[6] | (packet[7] << 8);
        uint16_t eaRaw = packet[32] | (packet[33] << 8);
        
        float startAngle = (saRaw - 0xA000) / 64.0;
        float endAngle = (eaRaw - 0xA000) / 64.0;
        
        // Handle angle wrap-around
        if (endAngle < startAngle) {
          endAngle += 360.0;
        }
        
        for (int i = 0; i < 8; i++) {
          int offset = 8 + (i * 3); // Samples start at byte 8
          
          uint16_t distL = packet[offset];
          uint16_t distH = packet[offset + 1];
          uint8_t quality = packet[offset + 2];
          
          uint16_t distance = distL | (distH << 8);
          
          // Only plot valid points
          // Physical constraint: X2 usually reads minimum 100mm, max 8000-12000mm
          if (distance > 100 && distance < 12000 && quality > 0) { 
            float ratio = (float)i / 7.0; // 8 samples: 0 to 7
            float angle = startAngle + (endAngle - startAngle) * ratio;
            
            while (angle >= 360.0) angle -= 360.0;
            while (angle < 0.0) angle += 360.0;
            
            // Print formatted payload to Python Visualizer
            Serial.print(angle, 2);
            Serial.print(",");
            Serial.println(distance);
          }
        }
        
        syncing = true;
        p_idx = 0;
      }
    }
  }
}
