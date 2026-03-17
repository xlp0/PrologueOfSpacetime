# MINUTES OF MEETING: INA AI Project Status and Shopper Analytics Technical Review

**Date:** 17/03/2026  
**Time:** 11:00 WITA – 13:00 WITA  
**Location:** Online Meeting

**Meeting Type:** Project Review and Technical Strategy Session

---

## ATTENDEES

**Present:**
- Alessandro Rumampuk
- Henry Koo
- Charlie Bachtiar Gunawan

**Absent:**
- N/A

**Guests/Observers:**
- N/A

---

## MEETING OBJECTIVE

The meeting aimed to synchronize the status of INA AI's current project portfolio and conduct a rigorous technical evaluation of transitioning from cloud-based AI to cost-effective edge computing solutions—specifically integrating LiDAR and Raspberry Pi hardware for the Shopper Analytics initiative.

---

## AGENDA ITEMS

### 1. Portfolio Project Status Updates

**Discussion Summary:**

The team reviewed the strategic necessity of maintaining momentum across concurrent workstreams to meet upcoming contractual milestones. We evaluated the architectural and operational progress of the following:

- **Home Cell / Games:** Deployment has been hindered by submission hurdles with the Google Play Store. The team is troubleshooting the build to ensure a resolution and deployment by the end of March.
- **BPJS (Badan Penyelenggara Jaminan Sosial):** Following a successful technical presentation to "Grop," the project is on track for a formal signing in April. This represents a significant milestone for INA AI's non-app product offerings.
- **Mayora (Supernetics):** Progress is currently stalled by retail store permissions. Stakeholders are expressing concern regarding data privacy and the physical footprint of the hardware (camera presence). We identified a critical need to pivot from cloud-based benchmarking to stress-testing in real-world "big store" environments to prove model efficacy under retail conditions.

**Decisions Made:**
- A "Big Meeting" involving Billy and the broader technical team will be convened post-Lebaran to finalize the Mayora project roadmap and address physical installation bottlenecks.

---

### 2. Shopper Analytics Hardware & Cost Optimization

**Discussion Summary:**

We evaluated the architectural trade-offs between centralized L40S GPU clusters and distributed edge nodes to optimize OpEx and improve after-sales sustainability.

- **Cloud vs. Edge Inference:** We analyzed the performance gap between the current L40S GPU cloud setup (~200 TFLOPS) and the proposed Raspberry Pi 4 Model B edge approach (~30 GFLOPS). A primary technical risk is Inference Latency Degradation; while YOLOv11s (Small) is optimized for the edge, inference speed drops significantly as occupancy increases (e.g., performance delta between 5 vs. 10+ people). We must ensure real-time capabilities for environments with 300+ people.
- **Hardware Specifications:** Discussed using 8GB and 16GB RAM variants for the Raspberry Pi. While Jetson Nano was considered for its superior processing power, the team will proceed with Raspberry Pi due to current resource availability and lower cost.
- **Sensor Fusion (LiDAR + IP Cameras):** To resolve Z-axis depth inaccuracies inherent in traditional 2D cameras, we are moving toward a "Triangular Stereo Vision" setup. This involves 3 cameras coupled with an internally assembled 3D LiDAR unit.
- **Cost Analysis:**
  - Vendor IP Cameras: 750,000 – 1,000,000 IDR per unit (includes installation/cabling).
  - Internal LiDAR/Camera Assembly: Target price of ~1,300,000 IDR for a custom-built unit (3 cameras + LiDAR + ESP32).
  - Optimization Potential: Henry identified raw component prices as low as 173k–300k IDR, offering a path for further margin optimization once we move past the prototype phase.

**Decisions Made:**
- Rolling Deployment Strategy: Implement a batch-based rollout (2 stores/max 100 cameras at a time) to cycle hardware and manage GPU/compute resources iteratively.

---

### 3. Pilot Testing Strategy & Facilities

**Discussion Summary:**

The absence of a physical "portfolio" environment is an immediate risk. We evaluated several facilities to simulate retail conditions and stress-test the LiDAR-Raspberry Pi integration.

- **Testing Site Options:** Duwi's warehouse (10x10m) was selected as the primary candidate. While the environment is "messy," it provides a realistic stress test for the AI's ability to handle occlusions and varied lighting. Other options (cafes, churches) remain in the parking lot for high-occupancy testing.
- **Environment Preparation:** The setup must include retail-style racks to accurately simulate store aisles and potential sensor blind spots.

**Action Items:**
- [ ] **Action:** Organize Duwi's warehouse with retail racks and set up the Shopper Analytics test case.  
  **Owner:** Alessandro / Bali Team  
  **Deadline:** Post-Lebaran  
  **Status:** Pending

- [ ] **Action:** Document the YOLOv11s model size and specific inference results (latency vs. person count) during warehouse testing.  
  **Owner:** Alessandro  
  **Deadline:** Post-Lebaran  
  **Status:** Pending

---

### 4. Strategic Roadmap & Partnerships (Nvidia & PKC)

**Discussion Summary:**

To ensure long-term scalability and mitigate the threat of Nvidia's DeepStream/Jetson retail solutions, we discussed a shift in market positioning.

- **Nvidia Strategy:** Alessandro is directed to contact Nvidia to explore a partnership as a "System Integrator." The goal is to avoid direct competition by leveraging their ecosystem while deploying INA AI's unique sensor fusion logic.
- **Personal Knowledge Container (PKC):** Defined PKC not just as a UI, but as a Browser-based IDE with Terminal Access. This allows the team to remotely manage, debug, and edit code on distributed Raspberry Pi nodes across various client sites (mining, retail) without being physically on-site.

**Decisions Made:**
- Formalize a "High-Level Roadmap" for Pak Pantro and non-technical stakeholders, emphasizing the value proposition of the Personal Knowledge Container (PKC)-Shopper Analytics ecosystem.

---

## KEY DECISIONS SUMMARY

1. **Edge Transition Strategy**  
   **Description:** Shift from L40S Cloud GPUs to localized Raspberry Pi 4 Edge nodes.  
   **Impact:** Drastic reduction in monthly OpEx (from 16M-20M IDR to one-time hardware costs); requires management of inference lag.

2. **Rolling Deployment**  
   **Description:** Staggered deployment in batches of 2 stores/100 cameras.  
   **Impact:** Minimizes CapEx risk and allows for iterative tuning of the edge model before full-scale rollout.

3. **Nvidia "Integrator" Position**  
   **Description:** Partnering with Nvidia's ecosystem rather than competing against DeepStream.  
   **Impact:** Provides access to superior hardware support and reduces competitive friction in the retail AI market.

---

## ACTION ITEMS SUMMARY

| # | Action Item | Owner | Deadline | Priority | Status |
|---|-------------|-------|----------|----------|--------|
| 1 | Organize Duwi's warehouse for retail simulation (including racks). | Alessandro | Post-Holiday | High | Pending |
| 2 | Design Hardware Topology (cameras vs. Pi nodes) for 1,200 sqm/7-aisle space. | Henry Koo | 27/03/2026 | High | Pending |
| 3 | Reach out to Nvidia to explore "System Integrator" partnership. | Alessandro | Post-Holiday | Medium | Pending |
| 4 | Develop High-Level Strategic Roadmap for Pak Pantro. | Alessandro | 27/03/2026 | Medium | Pending |
| 5 | Document YOLOv11s model size and inference latency results. | Alessandro | Post-Holiday | High | Pending |

---

## ISSUES & RISKS

**Issues Raised:**
- **Issue:** Lack of after-sales hardware support.  
  **Impact:** If a LiDAR sensor or camera fails at night, there is no technical team available for immediate maintenance, leading to data loss.  
  **Proposed Resolution:** Partner with established hardware vendors for the first two stores to leverage their field teams.

**Risks Identified:**
- **Risk:** Edge Inference Latency.  
  **Likelihood:** High  
  **Mitigation:** The team must optimize the YOLOv11s model specifically for the Raspberry Pi's GFLOPS limit; maintain the 100-camera "rolling" limit to avoid overextending compute nodes.

- **Risk:** Store Permissions & Privacy Concerns.  
  **Likelihood:** High  
  **Mitigation:** Develop a clearer technical brief for retailers emphasizing the "local processing" (Edge) nature of the system, which ensures video data never leaves the store.

---

## PARKING LOT

- High-Occupancy Testing Sites: Exploring churches or cafes as high-traffic alternatives if the warehouse test proves insufficient.
- Jetson Nano Transition: Tabled until Raspberry Pi 4 results are finalized; to be reconsidered if inference lag remains prohibitive.

---

## NEXT MEETING

**Date:** 27/03/2026 (Friday)
**Location:** Online Meeting

**Proposed Agenda:**
1. Comparison of Hardware Topology and Costing (Henry vs. Alessandro).
2. Review of the High-Level Strategic Roadmap for Pak Pantro.
3. Update on Duwi warehouse.

---

## APPROVAL

**Minutes Prepared By:**

Name: Alessandro Rumampuk  
Date: 17/03/2026

---

**Document Version:** 1.0  
**Last Updated:** 17/03/2026
