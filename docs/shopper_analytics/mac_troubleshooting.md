# Troubleshooting Kinect on macOS

If `libfreenect` cannot find your Kinect even though it is plugged in, follow these steps to check permissions and hardware conflicts.

## 1. Check Camera Permissions
macOS treats the Kinect as a "Camera". Your terminal needs permission to access it.

1.  Open **System Settings**.
2.  Go to **Privacy & Security** -> **Camera**.
3.  Look for your terminal app (e.g., **Terminal**, **iTerm2**, or **VS Code**).
4.  **Enable** the switch next to it.
    *   *Note*: If you don't see your terminal listed, macOS hasn't detected a camera access attempt yet.

### What if it's NOT listed?
If you don't see Antigravity or Terminal in the Camera list, it means **macOS is blocking the USB connection** before the app can even ask for camera access.
**Solution**: Skip to **Step 3 ("Allow Accessories to Connect")**. This is the most likely cause on M3 Macs.

## 2. Check Input Monitoring
Sometimes USB data transfer is categorized under Input Monitoring.

1.  Go to **Privacy & Security** -> **Input Monitoring**.
2.  Ensure your terminal app is allowed.

## 3. "Allow Accessories to Connect" (CRITICAL for Apple Silicon M1-M4)
**This is the most common issue on Apple Silicon (M1, M2, M3, M4).** macOS blocks new USB devices from communicating until you explicitly allow them.

1.  Open **System Settings**.
2.  Go to **Privacy & Security**.
3.  Scroll down to the **Security** section.
4.  Find **"Allow accessories to connect"**.
5.  Change it to **"Always allow"** (The last option in your screenshot).
    *   *Why?* The current setting "Automatically allow when unlocked" often fails for older devices like Kinect.
    *   **Action**: After changing this, **Unplug** the Kinect and **Plug it back in**. The system should now silently allow the connection.

### Verification
If you don't see the popup:
1.  Unplug Kinect.
2.  Reboot your Mac.
3.  Plug Kinect in *after* logging in.

## 4. Reset Permissions (Advanced)
If nothing works, you can force macOS to ask for permission again. Open a terminal window and run:

```bash
tccutil reset Camera
```
Then run the debug script again: `sudo uv run debug_kinect.py`.

## 5. Kernel Driver Conflict
Sometimes macOS loads its own audio/camera driver that "hogs" the USB connection, preventing `libfreenect` from using it.

run this to see if a driver is attached:
```bash
ioreg -p IOUSB -w0 -l | grep "Kinect" -A 10
```
If you see `IOUSBHostInterface` drivers attached effectively, they might need to be unloaded (which is complex on macOS).
