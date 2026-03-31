# Dual LiDAR Spatial Mapping Math & Logic

## 1. Physical Geometry
The dual LiDAR system uses a custom 3D printed U-Bracket to mount two 360-degree 2D LiDAR sensors (Camsense X2) back-to-back or parallel to each other. 
- The U-Bracket mounts directly onto a 180-degree high-torque servo motor via a center cross-hole.
- The servo motor axis defines our **Z-axis** of rotation.
- The two LiDAR sensors are mounted on the left and right vertical walls of the U-Bracket, creating a separation gap of **70mm**.
- This means each sensor is offset from the center of rotation by $R = 35$ mm.

## 2. Sensor Orientation (Local Frame)
Because the LiDARs are mounted on the vertical walls, their rotating internal lasers no longer scan the floor (horizontal plane). Instead, they scan **vertical planes** (YZ plane in the local coordinate system).
- The LiDAR spinning angle is $\alpha$ (0 to 360 degrees).
- The measured distance to an obstacle is $d$.
- $\alpha = 0$ points "forward" along the local Y-axis.
- $\alpha = 90^\circ$ points "up" along the local Z-axis.

Thus, for a single reading $(d, \alpha)$, the local coordinates are:
$y_{local} = d \cdot \cos(\alpha)$
$z_{local} = d \cdot \sin(\alpha)$

For **LiDAR 1 (Right Sensor)**:
$x_{local1} = +35$ mm

For **LiDAR 2 (Left Sensor)**:
$x_{local2} = -35$ mm

## 3. Sweeping Rotation (Global Frame)
The servo motor rotates the entire U-bracket assembly around the Z-axis by a sweeping angle $\theta_S$ (0 to 180 degrees).
To compute the final 3D coordinates $(x, y, z)$ in the room, we apply a Z-axis rotation matrix to the local coordinates.

### Rotation Matrix:
$x = x_{local} \cos(\theta_S) - y_{local} \sin(\theta_S)$
$y = x_{local} \sin(\theta_S) + y_{local} \cos(\theta_S)$
$z = z_{local}$

### Final Equations:
**LiDAR 1 (Right):**
$$x_1 = 35 \cos(\theta_S) - d_1 \cos(\alpha_1) \sin(\theta_S)$$
$$y_1 = 35 \sin(\theta_S) + d_1 \cos(\alpha_1) \cos(\theta_S)$$
$$z_1 = d_1 \sin(\alpha_1)$$

**LiDAR 2 (Left):**
$$x_2 = -35 \cos(\theta_S) - d_2 \cos(\alpha_2) \sin(\theta_S)$$
$$y_2 = -35 \sin(\theta_S) + d_2 \cos(\alpha_2) \cos(\theta_S)$$
$$z_2 = d_2 \sin(\alpha_2)$$

## 4. Why This Configuration?
By separating the sensors by 70mm and mapping them onto tangent paths along the 70mm circle, the system gains several advantages:
1. **True 360° Hemispherical Vision:** A single servo 180° sweep covers the entire room because the vertical LiDAR planes carve out a solid volume.
2. **Dense Center Scanning:** The 70mm lateral separation overlaps paths when $\theta_S$ crosses $90^\circ$, ensuring superior detail directly above and ahead of the unit.
3. **Simultaneous Dual Acquisition:** We gather 2x the point cloud density per sweep second compared to a single LiDAR.
