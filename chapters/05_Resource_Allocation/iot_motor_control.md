# IoT Motor Control: Animating the Frame

**Project Phase**: 2 (Life)
**Curriculum Column**: Arithmetic (Logic Phase)

## 1. The Philosophy of Animation
In **Chapter 02**, we built the Form (Geometry). Now, in **Chapter 05**, we must allocate **Resource** (Energy) to create **Motion**. This is the transition from **Abstract Specification** (the CAD model) to **Concrete Implementation** (the moving robot)—the CLM's first two dimensions made physical.
*   **The Monad**: The Token (Energy Unit). Each PWM pulse is a discrete allocation of energy—**Arithmetic** applied to voltage.
*   **The Actuator**: The Motor (Energy Consumer). The motor converts tokens into motion, embodying the **Coder's** role in the Miner-Coder-Trader Triad: transforming abstract value (voltage) into concrete action (rotation).

## 2. Technical Implementation
We use the **ESP32** to effectively count and distribute these energy tokens to the motors.

### Component List
*   **ESP32**: The Brain (Logic).
*   **L298N Driver**: The Muscle (Amplifier).
*   **DC Motor**: The Limb (Actuator).

### Code Logic (Arithmetic)
Movement is just arithmetic applied to voltage.
```cpp
void moveForward(int speed) {
    // Speed is a Resource (0-255)
    analogWrite(MOTOR_PIN, speed);
}
```

## 3. The Project: Giving it Life

> **Story Step 2: Animated Agency**
> *The frame now moves, but it is blind and alone.*

You have successfully wired the motors to the 3D printed frame. It can spin, but it cannot coordinate.
*   **Task**: Flash the `motor_test.ino` sketch to verify movement.

### Next Step: Connectivity
An isolated robot is just a toy. To become a **Node**, it must join the Network.
👉 **Proceed to [Chapter 06: VPN & Networking](../06_Network_Pathfinding/vpn_mesh_network.md)** to connect to the Swarm.
