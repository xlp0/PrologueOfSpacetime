# Gas Turbine Site Inspection Preparation & Checklist

**Project:** Gas Turbine Water Quality & Monitoring System  
**Objective:** Identify required sensors, their installation points, and IT integration methods based on the detailed target requirements for the 4 core areas.  
**Key Contacts:** Pak April, Pak Pantro  
**Project Manager:** Mas Rizki  

---

## 1. Pre-Visit Preparation
- [ ] **Technical Briefing:** Attend PM briefing with Mas Rizki to align on technical execution and GT fundamentals.
- [ ] **Review Target Sensors:** Familiarize yourself with the specific industrial sensors recommended for the project (e.g., RTD Pt100, Eddy Current proximity probes, Coriolis flow meters, Optical Particle Counters).
- [ ] **Request Blueprints First:** Ask Pak April for the floor plans and P&ID (Piping and Instrumentation Diagram) *before* the visit. Crucially, ask them to pre-mark or indicate on the blueprints exactly where they prefer or expect the new sensors to be installed.
- [ ] **Request Engineering Assistance:** Ensure the specific designer or lead engineer of the area (e.g., WTP coordinator, Turbine engineer) is scheduled to accompany and assist you during the physical walkthrough.
- [ ] **Check CMMS/DCS Access:** Prepare questions about how data from existing systems (SAP/Maximo, DCS/PLC) can be exported or integrated via API/Modbus/OPC-UA.

## 2. General Best Practices for Site Inspection
- **Safety First:** Wear mandatory PPE (Hard hat, steel-toed boots, ear protection, safety glasses).
- **No Unapproved Touching:** Never touch control panels, valves, or running machinery.
- **Document Heavily:** Take extensive photos of piping, existing sensor tap points, junction boxes, and equipment nameplates. Note the environmental conditions (heat, vibration, moisture).

---

## 3. Area-Specific Detailed Checklist

### A. Water Treatment Plant (WTP)
*Target: Predict raw water quality, optimize chemical dosing real-time, detect RO fouling early.*
- **Sensors to Identify/Plan:**
  - **Water Quality Quality:** pH Meter, Turbidimeter, Silica Analyzer, Conductivity Sensor.
  - **Flow & Pressure:** DP Transmitter, Pressure Transmitter, Magmeter/Ultrasonic flow meters, Coriolis/Magnetic flow meter (small scale for dosing line).
- **Inspection Checklist:**
  - [ ] **Upstream Water:** Where can we physically tap into the line to measure pH, Conductivity, and Turbidity? *(Note: Fe, Manganese, Hardness will likely remain manual lab inputs).*
  - [ ] **Downstream/Mixbed:** Observe the existing mixbed outlet where monitoring currently happens.
  - [ ] **RO System:** Identify mounting points for DP and Pressure Transmitters across the membranes (suction/discharge) and flow meters for Permeate/Reject Flow.
  - [ ] **Data Systems:** Ask operators how they currently input lab data. Discuss digitizing the manual operator logbook (CIP, backwash, media change).
  - [ ] **Visuals:** Take photos of the whole WTP piping route and installed dosing pumps.

### B. Water Injection (WI) System
*Target: Monitor pump conditions comprehensively, measure injection water quality, prevent GT derating/damage.*
- **Sensors to Identify/Plan:**
  - **Pump Health:** Accelerometer/Velocity Sensor (Vibration), Embedded RTD Pt100 (Temperature), Power Meter/Protection Relay (Current/Voltage).
  - **Pipeline Flow/Pressure:** High-Accuracy Pressure Transmitter, Turbine / Vortex Flow Meter.
  - **Water Quality:** Online Conductivity & Silica Analyzer (dedicated to injection line).
- **Inspection Checklist:**
  - [ ] **WI Pumps:** Inspect the pump housing and bearings for ideal vibration and temperature sensor mounting locations.
  - [ ] **Piping:** Look for tap-in locations on the injection pipeline for pressure and flow transmitters.
  - [ ] **DCS/System Data:** Confirm access to the existing **GT Datalog #1 (10ms)** which already has Load (MW), Heat Rate, Exhaust/Blade Path Temps, and PCD.
  - [ ] **Maintenance Logs:** Ask how to pull Alarm & Event data from the DCS/PLC, and how they record Boroscope (HPT/LPT) results and pump seal replacements.

### C. Inlet Air Filter
*Target: Analyze filter performance in real-time, predict clogging, and enable condition-based replacement.*
- **Sensors to Identify/Plan:**
  - **Environment & Dust:** Industrial Temp & Humidity Sensor, Optical Particle Counter (OPC) / Dust Monitor.
  - **Airflow/Pressure:** High-precision Low-Range DP Transmitter, Thermal Mass Flow Meter (or calc from GT control).
- **Inspection Checklist:**
  - [ ] **Air Intake Area:** Identify a safe, representative spot to mount the OPC (Dust Monitor) and Temp/Humidity sensors.
  - [ ] **Filter Housing:** Locate the existing (but unreliable) DP sensor. See how a new, high-precision DP Transmitter could replace or supplement it.
  - [ ] **Documentation:** Request the filter specification sheets (F-class/H-class, max dust capacity) and check CMMS for historical filter lifespan data.

### D. Turbine Lube Oil System
*Target: Monitor oil degradation continuously, correlate oil condition with equipment health to prevent bearing damage.*
- **Sensors to Identify/Plan:**
  - **Oil Quality:** Online Dielectric/Moisture Sensor, Laser Particle Counter.
  - **System Ops:** Pressure/Temp Transmitter (RTD), Radar Level Transmitter (for oil tank), DP Transmitter (for filter).
  - **Rotating Equipment:** Proximity Probe / Eddy Current, Embedded RTD.
- **Inspection Checklist:**
  - [ ] **Sensors on Pipes/Tanks:** Find tap points for the Dielectric/Moisture Sensor and Laser Particle Counter. Locate the oil tank for a Radar Level Transmitter.
  - [ ] **Filter & Cooler:** Identify points to measure DP across the oil filter, and RTD Pt100 spots before/after the oil cooler.
  - [ ] **Bearings:** Inspect the rotating equipment area. Check if it's feasible to install Proximity Probes (Eddy Current) for radial/axial vibration and metal bearing temps.
  - [ ] **Lab Data:** Discuss the current process for OCM (Oil Condition Monitoring) lab testing. How can we upload this periodic data (Viscosity, TAN, Wear Metals, ISO particle count) into the new system?

---

## 4. Key Priorities and Questions for Pak April
1. **Physical Constraints & Sensor Installation:** Are the WTP and Turbine areas classified as hazardous (e.g., ATEX Zone 1/2)? Can we install new sensors while the turbine is running ("hot tapping"), or do we have to wait for a scheduled plant shutdown?
2. **Serial Connections vs. Analog:** For the existing WTP sensors and PLC systems, do they use **Serial Connections** (like RS-485 / Modbus RTU) or analog cables (4-20mA)? This determines the exact IoT gateway hardware we need to bring.
3. **Edge Computing for GT Datalog:** Since the GT Datalog generates data extremely fast (every 10ms), is there space in the control room to install an **Edge Computing Device** (like an Industrial PC or Mac Studio)? We need this to process the massive 10ms data locally instead of overloading cloud bandwidth.
4. **Data Integration:** What brand of DCS/PLC do they use? How do we extract existing alarms, lab results, and GT Datalog #1? Does the chemical lab have a LIMS system for automatic data pulls, or do operators need a custom web form?
5. **Power & Network:** Where will the gateways/IoT nodes get 24V/220V power and network access (Wi-Fi, Ethernet, Cellular, LoRa)?
