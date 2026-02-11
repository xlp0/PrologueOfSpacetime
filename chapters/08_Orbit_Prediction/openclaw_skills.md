# OpenClaw & AI Skills: The Pilot

**Project Phase**: 6 (Intelligence)
**Curriculum Column**: Astrobiology (Logic Phase)

## 1. The Philosophy of Skills
In **Chapter 07**, the Node learned to speak (MQTT). Now, in **Chapter 08**, it learns to **Do**. This is where all three roles of the **Miner-Coder-Trader Triad** converge in a single execution cycle:
*   **The Brain**: The Large Language Model (DeepSeek/Gemini). The Miner validates the historical data (sensor readings) that feeds the prediction.
*   **The Hands**: The MCP Server (OpenClaw). The Coder implements the skill definitions—the **PCard** transformations that convert intent into action.
*   **The Delivery**: The MQTT command published back to the swarm. The Trader delivers the prediction to the actuators that execute the correction.

## 2. Technical Implementation: MCP (Model Context Protocol)

We define "Skills" using the **Model Context Protocol**, which standardizes how AI discovers and calls tools.

### Defining a Skill
A Skill is a JSON schema that describes a function to the AI.
```json
{
  "name": "set_motor_speed",
  "description": "Sets the speed of the Kinetic Node's motor.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "speed": { "type": "integer", "description": "0-255 PWM value" }
    }
  }
}
```

### OpenClaw Integration
**OpenClaw** acts as the *Agentic Runtime*. It:
1.  Listens to the **Historian** (MQTT Events).
2.  Decides an action (Prediction).
3.  Calls the **Skill** (MCP Tool).
4.  Publishes the command back to MQTT (`kinetic/swarm/01/command`).

## 3. The Project: The Pilot

> **Story Step 6: The Agency**
> *The machine is no longer reactive. It is proactive.*

You have a connected, speaking robot. Now give it a goal.
*   **Task**: Write an MCP server that exposes the `mqtt.publish` function as a tool.
*   **Goal**: Ask OpenClaw "Turn on the motor if the temperature is above 30C." Watch it query the sensor and execute the command.
