# MQTT & The Event Bus: The Nervous System

**Project Phase**: 5 (Communication)
**Curriculum Column**: Music (Logic Phase)

## 1. The Philosophy of Pub/Sub
In **Chapter 06**, we connected the nodes via VPN. But connection implies a direct line. In a massive swarm, direct lines create spaghetti code.
*   **The Solution**: The Event Bus (MQTT Broker). The broker is the concrete infrastructure that implements the chapter's core principle of **Directionality**: the Topic Structure (`status` vs `command`) enforces non-commutative event flow, ensuring that telemetry always precedes commands in the causal chain.
*   **The Metaphor**: The Town Square. You don't whisper to everyone; you shout in the square, and those who care listen.

## 2. Technical Implementation: Mosquitto

We use **Mosquitto** as our message broker.

### Topic Structure (Grammar)
Topics are the "URL" of the event bus. Structure matters.
*   `kinetic/swarm/01/status` (Telemetry)
*   `kinetic/swarm/01/command` (Action)

### The Code (Arduino/ESP32)
```cpp
// Subscribe to commands
client.subscribe("kinetic/swarm/01/command");

// Publish heartbeat
client.publish("kinetic/swarm/01/status", "ALIVE");
```

## 3. The Project: The Conversation

> **Story Step 5: The Voice**
> *The Node learns to speak.*

Your Node is online (VPN). Now it must report its status to the Historian.
*   **Task**: Set up a free HiveMQ or local Mosquitto broker.
*   **Goal**: Send a message "HELLO" from the ESP32 and see it on your laptop using `MQTT Explorer`.

### Next Step: Intelligence & Skills
Thinking is hard. Reacting is easy. How do we give the Node **Skills** to act on these messages?
👉 **Proceed to [Chapter 08: Orbit Prediction & OpenClaw](../08_Orbit_Prediction/openclaw_skills.md)** to install the Brain.
