# Existing Plant Knowledge Base (Balikpapan Site)

**Project:** Gas Turbine Water Quality & Monitoring System
**Last Updated:** Based on the "Water Quality Monitoring" & "Test Case" Client Presentation

This document serves as the master reference for the physical constraints, architecture, and baseline context of the Balikpapan Gas Turbine plant *prior* to our site inspection. It is synthesized from the client's architecture diagrams and formal test case requests.

---

## 1. Water Quality Flow Architecture
The plant follows a structured flow from raw storage into the final turbine engine feed. The overarching path is:
1. **Source:** `DW (Demineralized Water)` $\rightarrow$ `Pond`
2. **Side Loop:** `Pond` $\rightarrow$ `New Tank` $\rightarrow$ Returns to `DW`
3. **Treatment:** `Pond` $\rightarrow$ `WTP` (Housing Reverse Osmosis & Mixbed systems)
4. **Pre-Engine Storage:** `WTP` $\rightarrow$ Main `Tank`
5. **Final Injection:** Main `Tank` splits into dual pumps: `Transfer Pump` and `Pump SPRINT` $\rightarrow$ `Engine` (Gas Turbine)

## 2. Controller Mapping (PLC Existing vs. PLC New)
The site is undergoing an upgrade with a segregated PLC topology. Our system must target the core integration points. 

Based on the client diagram (Yellow Nodes/Control Points), the **PLC New** will explicitly monitor/control:
* **The New Tank** (Drawing off the DW Pond loop)
* **The Mixbed** (For regeneration and output controls)
* **The Final Supply Pumps** (`Transfer Pump` & `Pump SPRINT`) sending water to the Engine.

*Note: The **PLC Existing** continues managing legacy operations, but our primary critical interface for engine shutdown (trip signals) will likely interface directly with the nodes on the **PLC New**.*

## 3. Current Baseline Monitoring (Sensors)
Before our IoT upgrade, the plant's monitoring capability is heavily bottlenecked by manual routines.
* **Online (Continuous) Monitoring:** 
  * Only **Silica** is currently monitored continuously online in the processing system.
* **Routine (Manual/Lab) Monitoring:** 
  * **pH**
  * **Conductivity**
  * **TSS** (Total Suspended Solids)
  * **TDS** (Total Dissolved Solids)

*Actionable Insight:* The AI validation requires continuous `< 1-second` latency data. Because pH and Conductivity are currently "Routine", the plant *must* install the continuous IoT probes we specified in the Site Inspection Agenda to allow the AI to function.

## 4. Required AI Validation (Field Test Cases)
The client has demanded 12 strict field trials to prove our AI adds value. Our hardware installation must physically allow these simulated tests:
1. **Dosing Substitution:** Operator manually doses vs. AI calculates dosing. (Requires API/dashboard comparison).
2. **RO Fouling Prediction:** Client will manually alter the Permeate vs. Reject Flow valves over a specified time to see if the AI accurately recommends a membrane cleaning procedure.
3. **Mixbed Regeneration:** Client will ramp up Mixbed output to see if AI triggers a regeneration schedule warning.
4. **Trip Signal (Critical):** Client will simulate/inject "out of spec" water (bad pH/Conductivity/Silica). The AI must detect it instantly (High-High / Low-Low) and send a Trip Signal to the **PLC New / Transfer Pumps** to cut off supply to the Gas Turbine immediately.
5. **Latency Validation:** The new AI dashboard will be compared side-by-side with the plant's DCS. Delay must be $\le 1$ second. 
6. **Degradation:** We must physically simulate "imperfect/noisy" data (e.g., unplugging a sensor momentarily) and prove the system degrades gracefully with $< 10\%$ false alarms.
