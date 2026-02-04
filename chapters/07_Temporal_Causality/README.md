# Chapter 07: Temporal Causality

> *"Time is the sequence of events, not the ticking of a clock."*

In the **Revived Quadrivium**, **Temporal Causality** is the Logic of Music. It answers the question: *How do we ensure that Cause precedes Effect in a distributed system?*

## 📚 Core Concepts

### 1. The Historian (The Monad)
The "Historian" is the keeper of the Log. In distributed systems, there is no Global Clock. There is only the **Event Log**.
*   **[MVP Card: The Historian](MVP_The_Historian.md)**: The philosophical definition of linear time.

## 2. Technical Implementation: MQTT Event Bus

To coordinate the Kinetic Swarm (from Ch 06), we cannot rely on synchronous HTTP requests. We need an asynchronous **Event Bus**.

### What is MQTT?
*   **Message Queuing Telemetry Transport**: A lightweight protocol for IoT.
*   **Pub/Sub**: Publishers (Sensors) scream into the void; Subscribers (actuators) listen for echoes.

### 3. Project: Kinetic Node (Phase 5)
We apply causality to **Communication**.
*   **[MQTT & The Event Bus](mqtt_event_bus.md)**: Configuring the Node to "Speak" and "Listen" via a Broker.
