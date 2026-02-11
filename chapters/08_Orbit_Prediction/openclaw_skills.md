# OpenClaw & AI Skills: The Pilot

**Project Phase**: 6 (Intelligence)
**Curriculum Column**: Astrobiology (Logic Phase)

## 1. The Philosophy of Skills
In **Chapter 07**, the Node learned to speak (MQTT). Now, in **Chapter 08**, it learns to **Do**. As the chapter README describes, this is where the full **Miner-Coder-Trader Triad** converges. Here we see that convergence in concrete components:
*   **The Brain**: The Large Language Model (DeepSeek/Gemini) — ingests validated sensor data.
*   **The Hands**: The MCP Server (OpenClaw) — implements skill definitions as **PCard** transformations.
*   **The Delivery**: The MQTT command published back to the swarm — closes the action loop.

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
