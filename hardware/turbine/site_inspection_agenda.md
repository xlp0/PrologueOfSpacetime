# Proposed Site Visit Agenda (Balikpapan)

**Objective:** Finalize sensor selection (sizing), verify physical installation viability, and confirm data integration pathways for the WTP and Gas Turbine Predictive Monitoring System.

---

### 1. Kick-Off & AI Team Alignment
* **Goal:** Align with the AI Team and plant operators (Pak April/Pak Pantro) on the predictive models they want to run.
* **Make Sure/Check:** Confirm if the area is classified as an ATEX Zone (hazardous/explosive), as this completely dictates which sensors we can physically buy and suggest. 

### 2. System Flow Room Tour & Physical Sensor Placement (Field Walkthrough)
* **Goal:** First, understand the overarching water processing line (system flow) and current goals. Then, verify that our suggested sensors will actually fit on the pipes and pumps.
* **Make Sure/Check:**
  * **System Flow & Wires:** Observe how the water flows through the plant and physically trace what kind of wiring the existing sensors are currently using.
  * **WTP:** Inspect the upstream pipe diameters to confirm sizing for pH, Turbidity, and Conductivity sensors. Confirm if the chemical dosing pumps can accept an automated electronic signal (4-20mA).
  * **Water Injection Pumps:** Locate exact flat surfaces on the pumps to mount Accelerometers (vibration) and RTDs (temperature).
  * **Lube Oil:** Identify tap points for the Dielectric (Oil Quality) and Laser Particle Counter sensors.

### 3. IT & Data Integration Sync (Control Room)
* **Goal:** Figure out how we extract existing data and handle the massive new sensor data load.
* **Make Sure/Check:**
  * Space availability in the server room/cabinet for our **Edge Computing Device** (crucial for processing the 10ms GT Datalog locally).
  * Verify the DCS/PLC brand and protocol (e.g., OPC-UA, Modbus TCP) to pull historical trips and alarms.
  * Establish API or database access for the digital lab input forms that are currently used for WTP.

### 4. Network & Power Infrastructure Check
* **Goal:** Ensure our suggested sensors can actually turn on and transmit data.
* **Make Sure/Check:**
  * Where can we draw 24V DC or 220V AC power for the IoT Gateways?
  * Detail the network coverage in the WTP and Turbine areas (Is there enterprise Wi-Fi we can piggyback on, or do we need to suggest Cellular/LoRaWAN gateways?).

### 5. Wrap-Up & Final Sensor Suggestion Approval
* **Goal:** Review the physical findings and finalize the hardware procurement list with Rizky and the AI Team.
