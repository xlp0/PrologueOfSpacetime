import serial
import matplotlib.pyplot as plt
import numpy as np
import threading
import time
import sys

PORT = '/dev/cu.usbmodem2101'
BAUD = 115200

angles = []
distances = []
data_lock = threading.Lock()

def read_serial():
    global angles, distances
    try:
        with serial.Serial(PORT, BAUD, timeout=1) as ser:
            while True:
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                if ',' in line:
                    try:
                        parts = line.split(',')
                        if len(parts) == 2:
                            ang = float(parts[0])
                            dist = float(parts[1])
                            if 10.0 < dist < 12000.0:
                                with data_lock:
                                    angles.append(np.radians(ang))
                                    distances.append(dist)
                                    # Keep 1500 points (about 2 dense rotations)
                                    if len(angles) > 1500:
                                        angles.pop(0)
                                        distances.pop(0)
                    except ValueError:
                        pass
    except Exception as e:
        print(f"Serial Error: {e}")
        
t = threading.Thread(target=read_serial, daemon=True)
t.start()

plt.ion()
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='polar')

print("Starting LiDAR plotting... Close window to stop.")

try:
    while plt.fignum_exists(fig.number):
        with data_lock:
            a = list(angles)
            d = list(distances)
            
        ax.clear()
        ax.set_theta_zero_location("N") 
        ax.set_theta_direction(-1) # Clockwise
        
        # Max 12 Meters radius (12000 mm)
        # Therefore, width of screen covers 24 meters diameter.
        ax.set_ylim(0, 12000)
        ax.set_title("Real-Time X2 LiDAR Point Cloud (12m Radius)")
        
        if len(a) > 0:
            ax.scatter(a, d, c='blue', s=8, alpha=0.7)
            
        # Draw frame ~ 10 FPS to entirely prevent GUI freezing
        plt.pause(0.1)
except KeyboardInterrupt:
    pass

plt.close()
sys.exit(0)
